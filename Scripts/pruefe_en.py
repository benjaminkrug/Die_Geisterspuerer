#!/usr/bin/env python3
"""A11 / D7 / D8: Prüfungen für die englische Ausgabe.

Vergleicht ein deutsches Kapitel (oder Komplett-Manuskript) mit seiner englischen Übersetzung
und prüft alles, was messbar ist. Grundlage: Dokumentation/EN_Bibel/ (A1, A2, A4, A5, A6, A8).

Aufruf:
  python3 Scripts/pruefe_en.py pruefen  DE.md EN.md   Befunde (Exit 1, wenn es welche gibt)
  python3 Scripts/pruefe_en.py bericht  DE.md EN.md   D8.1 Gleichwertigkeits-Bericht + Kapitelende
  python3 Scripts/pruefe_en.py konsistenz ORDNER      gleicher deutscher Satz → überall gleiches Englisch?
                                                      (ORDNER/DE_Basis/Kapitel_XX.md ↔ ORDNER/Kapitel_XX.md)
  python3 Scripts/pruefe_en.py hinweise               sammelt EN_Hinweise.md (Schreibregeln S1/S4)
  python3 Scripts/pruefe_en.py selbsttest             eingeschleuste Fehler müssen gefunden werden

Was das Skript NICHT kann (bleibt bei D4/D5/D6): Sinn, Ton, Witz, Stimme einer Figur. Es misst nur
Form. Ein sauberer Lauf heißt „keine Formfehler", nicht „gute Übersetzung".
"""
import argparse
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
REGISTER = ROOT / "Dokumentation/EN_Bibel/A5_Satz_Register.md"

# --- Verbotslisten (Quelle in Klammern) -------------------------------------------------------
VERBOTE = {
    "Fluch (A2, A8)": r"\b(?:damn\w*|hell|crap\w*|sucks?|shit\w*|oh my god|omg|jesus|christ)\b",
    "Britisch (A6, A8)": r"\b(?:mum|mummy|torch(?:es)?|pavement|rubbish|colour\w*|grey\w*|metres?|centre\w*|realis\w+|"
                         r"favourite\w*|neighbour\w*|learnt|spelt|whilst|(?:the|a|our|her|his|their|my) flat)\b",
    "Anrede ohne Punkt (A8)": r"(?-i:\bMrs?\b)(?!\.)",
    "Glossar (A1)": r"\b(?:Frau|Herr|Handy|Emily|Ghost Trackers|Celsius)\b|Kloß|°C",
    "Motiv-Wortlaut (A4)": r"\b(?:golden eyes|honey(?:-colou?red)? eyes|yellow eyes|whimper\w*|fur (?:bristled|stood on end)|"
                           r"(?:lilac|violet|mauve) ink|ink was (?:still )?damp|damp ink)\b|\bknock[,.]\s*knock\b",
    "Dialogverb (A8)": r"\b(?:exclaimed|stated|remarked|uttered|inquired|queried|replied)\b",
    "Satzbau (A8)": r"\bsaid (?:Theo|Nora|Mom)\b",
    "Wortwahl nach Pilot (A8 Abschn. 6)": r"\b(?:cellar|muzzle|ceiling lamp|name card|kids' rooms?|food box|supermarket|"
                                         r"blamed it on the heat|raised (?:his|her) head)\b",
    "Deutsch-Rest": r"[„‚äöüÄÖÜß]|\b(?:und|nicht|ist|ich|wir|aber|auch|noch|schon|sagte)\b",
}

ORDINAL_DE = {"erd": 0, "erste": 1, "zweite": 2, "dritte": 3, "vierte": 4}
ORDINAL_EN = {"first": 1, "second": 2, "third": 3, "fourth": 4, "fifth": 5}
ZAHL_DE = {"ein": 1, "zwei": 2, "drei": 3, "vier": 4, "fünf": 5, "sechs": 6, "sieben": 7, "acht": 8, "neun": 9,
           "zehn": 10, "elf": 11, "zwölf": 12, "fünfzehn": 15, "zwanzig": 20}


# --- Grundbausteine ---------------------------------------------------------------------------
def absaetze(text):
    """Absätze = Blöcke zwischen Leerzeilen. Szenentrenner (---) und Leerblöcke zählen nicht."""
    bl = [b.strip() for b in re.split(r"\n\s*\n", text)]
    return [b for b in bl if b and not re.fullmatch(r"-{3,}|\*{3,}", b)]


def satzzahl(absatz):
    """Sätze im Absatz. Ende = . ! ? … (ggf. mit Anführungszeichen), danach Großbuchstabe."""
    absatz = re.sub(r"\b(Mrs?|Ms|Dr|St)\.", r"\1", absatz)  # Anrede-Punkt ist kein Satzende
    # “Did you hear that?” Theo whispered. — Frage/Ausruf vor dem Begleitsatz ist kein Satzende.
    absatz = re.sub(r"([?!])([”\"’])\s+(?=(?:[A-Z]\w+\s+)?(?:said|asked|whispered|called|shouted|yelled|screamed|"
                    r"muttered|murmured|hissed|answered|he|she|they)\b)", r"\1\2 ~", absatz)
    enden = re.findall(r"[.!?…]+[\"“”»«’‘']*\s+(?=[\"„“‚‘»«(*_]*[A-ZÄÖÜ])", absatz)
    return len(enden) + 1


def dialoganteil(text):
    rede = re.findall(r"[„“\"]([^„“”\"]+)[“”\"]", text)
    gesamt = len(re.sub(r"\s+", " ", text))
    return 100 * sum(len(r) for r in rede) / gesamt if gesamt else 0.0


def silben(wort, de):
    w = wort.lower()
    gruppen = re.findall(r"[aeiouyäöü]+" if de else r"[aeiouy]+", w)
    n = len(gruppen)
    if not de and w.endswith("e") and n > 1 and not w.endswith(("le", "ee")):
        n -= 1
    return max(1, n)


def silben_je_satz(text, de):
    saetze = [s for s in re.split(r"(?<=[.!?…])\s+", re.sub(r"[#*_„“”\"‚‘’]", "", text)) if s.strip()]
    if not saetze:
        return 0.0
    return sum(silben(w, de) for s in saetze for w in re.findall(r"[^\W\d_]+", s)) / len(saetze)


def norm(s):
    """Zum Vergleichen: ohne Satzzeichen, Hervorhebung, Groß-/Kleinschreibung. So findet sich
    „Es gibt eine Erklärung“, sagte … auch dann, wenn der Satz im Register mit Punkt steht."""
    s = re.sub(r"[*_„“”\"‚‘’'.,!?…;:()\[\]>#]|[—–-]+", " ", s)
    return re.sub(r"\s+", " ", s).strip().lower()


# --- Register aus A5 einlesen -----------------------------------------------------------------
def register_paare():
    """(nr, deutsch, englisch) aus den Tabellen in A5. Englisch = erster kursiver Abschnitt der
    Englisch-Spalte. Nur Einträge mit eindeutigem Wortlaut (keine 'sinngemäß'-Stellen)."""
    paare = []
    if not REGISTER.exists():
        return paare
    for zeile in REGISTER.read_text(encoding="utf-8").splitlines():
        m = re.match(r"\|\s*(R\d+)\s*\|([^|]+)\|([^|]+)\|([^|]+)\|", zeile)
        if not m:
            continue
        nr, de, _, en = m.groups()
        de = re.sub(r"\(.*?\)|Motto B\d:", "", de).replace("/", " ")
        en_m = re.search(r"\*([^*]+)\*", en)
        if not en_m:
            continue
        en = en_m.group(1).replace("/", " ")
        if len(norm(de).split()) >= 3 and norm(en):
            paare.append((nr, norm(de), norm(en)))
        # Mehrsatz-Einträge zusätzlich Satz für Satz: Im Text steht oft ein Einschub dazwischen
        # (B3 K7: „… Hier ist nicht das Kind gefangen." – „Nora—" – „Es ist die Mutter …").
        teile_de = [s for s in re.split(r"(?<=[.!?…])\s+", de.strip(" *")) if s.strip()]
        teile_en = [s for s in re.split(r"(?<=[.!?…])\s+", en.strip(" *")) if s.strip()]
        if len(teile_de) > 1 and len(teile_de) == len(teile_en):
            for k, (d, e) in enumerate(zip(teile_de, teile_en)):
                if len(norm(d).split()) >= 3:
                    paare.append((f"{nr}.{k + 1}", norm(d), norm(e)))
    return paare


# --- Prüfungen ------------------------------------------------------------------------------
def pruefen(de_text, en_text, register=None):
    befunde = []
    a_de, a_en = absaetze(de_text), absaetze(en_text)

    # 1. Absätze 1:1 und Ein-Satz-Absätze (A8 Abschn. 3, D8.1)
    if len(a_de) != len(a_en):
        erst = next((i for i, (d, e) in enumerate(zip(a_de, a_en)) if satzzahl(d) == 1 and satzzahl(e) > 1), None)
        hinweis = f" — erste Abweichung vermutlich bei Absatz {erst + 1}: {a_de[erst][:60]!r}" if erst is not None else ""
        befunde.append(("Absätze", f"DE {len(a_de)} ≠ EN {len(a_en)}{hinweis}"))
    else:
        for i, (d, e) in enumerate(zip(a_de, a_en)):
            if satzzahl(d) == 1 and satzzahl(e) > 1 and len(d) < 200:
                befunde.append(("Ein-Satz-Absatz", f"Absatz {i + 1}: DE {d[:50]!r} → EN hat {satzzahl(e)} Sätze"))

    # 2. Ausrufezeichen (A2: Original 1–4 %)
    if en_text.count("!") > de_text.count("!"):
        befunde.append(("Ausrufezeichen", f"DE {de_text.count('!')} · EN {en_text.count('!')}"))

    # 3. Verbotslisten
    for name, muster in VERBOTE.items():
        treffer = sorted({m.group(0) for m in re.finditer(muster, en_text, re.I)})
        if treffer:
            befunde.append((name, ", ".join(treffer)))

    # 3b. Mutter im Erzähltext: Mom, nicht their mother (A2, nach Pilot) — einzelne Ausnahmen erlaubt
    n_mutter = len(re.findall(r"\btheir mother\b", en_text, re.I))
    if n_mutter > 2:
        befunde.append(("Mutter (A2)", f"{n_mutter}× 'their mother' — Erzähltext sagt 'Mom'"))

    # 4. Stockwerke: deutsche Zahl + 1 (Glossar E9)
    de_st = {ORDINAL_DE[m.group(1).lower()] for m in
             re.finditer(r"(?i)\b(erd|erste|zweite|dritte|vierte)[nrs]?(?:geschoss|\s+stock|\s+etage)", de_text)}
    en_st = {ORDINAL_EN[m.group(1).lower()] for m in re.finditer(r"(?i)\b(first|second|third|fourth|fifth) floor", en_text)}
    falsch = en_st - {n + 1 for n in de_st}
    if de_st and falsch:
        befunde.append(("Stockwerk (E9)", f"DE {sorted(de_st)} → erwartet EN {sorted(n + 1 for n in de_st)}, gefunden {sorted(en_st)}"))

    # 5. Temperaturen umgerechnet? (E10)
    de_grad = {int(z) if z.isdigit() else ZAHL_DE.get(z.lower(), -1)
               for z in re.findall(r"(?i)\b(\d+|" + "|".join(ZAHL_DE) + r")\s+Grad\b", de_text)}
    en_grad = {int(z) for z in re.findall(r"\b(\d+)\s*(?:degrees|°)", en_text)}
    if de_grad & en_grad:
        befunde.append(("Temperatur (E10)", f"nicht umgerechnet? gleiche Zahl(en) {sorted(de_grad & en_grad)}"))

    # 6. Register-Sätze wörtlich (A5)
    de_n, en_n = norm(de_text), norm(en_text)
    for nr, de_s, en_s in (register if register is not None else register_paare()):
        if de_s in de_n and en_s not in en_n:
            befunde.append(("Register (A5)", f"{nr}: erwartet {en_s!r}"))

    # 7. Satzbild (A8 Abschn. 5): typografische Apostrophe passend zu “ ”, Striche, Auslassungspunkte
    typo = []
    if re.search(r"[A-Za-z]'[A-Za-z]|s'(?=\s)", en_text):
        typo.append(f"gerader Apostroph ' ({len(re.findall(chr(39), en_text))}×) statt ’")
    if '"' in en_text:
        typo.append('gerade Anführung "')
    if re.search(r" [—–] |(?<!-)--(?!-)", en_text):  # --- (Szenentrenner) ist erlaubt
        typo.append("Gedankenstrich mit Leerzeichen oder --")
    if "..." in en_text:
        typo.append("... statt …")
    if typo:
        befunde.append(("Satzbild (A8)", "; ".join(typo)))

    # 8. Kursiv (Tagebuch, Notizbuch, Gedanken) muss erhalten bleiben
    k_de, k_en = len(re.findall(r"\*[^*\n]+\*", de_text)), len(re.findall(r"\*[^*\n]+\*", en_text))
    if k_de != k_en:
        befunde.append(("Kursiv", f"DE {k_de} · EN {k_en} kursive Stellen"))

    # 9. Schattens Code (A4 Abschn. 2, R44): jedes Signal im Deutschen braucht sein festes Wort
    for de_rx, en_rx, name in ((r"knurr", r"growl", "knurrt → growl"), (r"winsel", r"whin", "winselt → whine"),
                               (r"sträub", r"hackles", "Fell sträubt sich → hackles")):
        n_de, n_en = len(re.findall(de_rx, de_text, re.I)), len(re.findall(en_rx, en_text, re.I))
        if n_en < n_de:
            befunde.append(("Schattens Code (A4)", f"{name}: DE {n_de} · EN {n_en}"))

    # 10. Kleines „shadow" klingt beim Vorlesen wie der Hund (Block 1). Erlaubt nur im Wortspiel K12.
    if re.search(r"\bshadows?\b", en_text) and "nicht unseren Schatten" not in de_text:
        n = len(re.findall(r"\bshadows?\b", en_text))
        befunde.append(("Kleines shadow (Wortliste)", f"{n}× – shape/darkness/silhouette verwenden"))
    return befunde


# --- Einheitlichkeit über Kapitel (Nachprüfung Block 1) ---------------------------------------
def saetze(absatz):
    absatz = re.sub(r"\b(Mrs?|Ms|Dr|St)\.", r"\1", absatz)
    return [s for s in re.split(r"(?<=[.!?…])[\"“”»«’‘']*\s+(?=[\"„“‚‘»«(*_]*[A-ZÄÖÜ])", absatz) if s.strip()]


def konsistenz(paare):
    """paare: [(kapitel, de_text, en_text)]. Ordnet Absätze 1:1 zu, bei gleicher Satzzahl auch Sätze.
    Meldet deutsche Sätze (≥ 2 Wörter), die in mehreren Kapiteln stehen, aber verschieden übersetzt sind."""
    stellen = {}
    for kap, de_text, en_text in paare:
        a_de, a_en = absaetze(de_text), absaetze(en_text)
        if len(a_de) != len(a_en):
            continue
        for d, e in zip(a_de, a_en):
            s_de, s_en = saetze(d), saetze(e)
            einheiten = list(zip(s_de, s_en)) if len(s_de) == len(s_en) else [(d, e)]
            for sd, se in einheiten:
                if len(norm(sd).split()) >= 2:
                    stellen.setdefault(norm(sd), []).append((kap, se.strip()))
    befunde = []
    for de, vork in sorted(stellen.items()):
        if len({k for k, _ in vork}) > 1 and len({norm(e) for _, e in vork}) > 1:
            befunde.append((de, vork))
    return befunde


def bericht(de_text, en_text):
    a_de, a_en = absaetze(de_text), absaetze(en_text)
    eins_de = sum(satzzahl(a) == 1 for a in a_de)
    eins_en = sum(satzzahl(a) == 1 for a in a_en)
    zeilen = [
        ("Absätze", len(a_de), len(a_en), "± 10 %"),
        ("Ein-Satz-Absätze", eins_de, eins_en, "keiner verloren"),
        ("Dialoganteil %", round(dialoganteil(de_text), 1), round(dialoganteil(en_text), 1), "± 5 Punkte"),
        ("Ausrufezeichen", de_text.count("!"), en_text.count("!"), "EN ≤ DE"),
        ("Silben je Satz (nur Info)", round(silben_je_satz(de_text, True), 1), round(silben_je_satz(en_text, False), 1), "Korridor erst nach Pilot"),
    ]
    print("| Wert | DE | EN | Grenze | |\n|---|---|---|---|---|")
    for name, d, e, grenze in zeilen:
        ok = "✅"
        if name == "Absätze" and d and abs(e - d) / d > 0.10:
            ok = "⚠️"
        if name == "Ein-Satz-Absätze" and e < d:
            ok = "⚠️"
        if name.startswith("Dialog") and abs(e - d) > 5:
            ok = "⚠️"
        if name == "Ausrufezeichen" and e > d:
            ok = "⚠️"
        if "Info" in name:
            ok = "–"
        print(f"| {name} | {d} | {e} | {grenze} | {ok} |")
    print("\n**Kapitelende** (letzter Absatz) — gleich scharf?\n")
    print(f"- DE: {a_de[-1] if a_de else ''}\n- EN: {a_en[-1] if a_en else ''}")


def hinweise():
    dateien = sorted(ROOT.glob("**/EN_Hinweise.md"))
    if not dateien:
        print("Keine EN_Hinweise.md gefunden (Schreibregeln S1/S4 noch nicht angewandt).")
    for d in dateien:
        print(f"## {d.relative_to(ROOT)}\n\n{d.read_text(encoding='utf-8')}\n")


# --- Selbsttest -----------------------------------------------------------------------------
DE_PROBE = """# Kapitel 1 – Probe

„Kommt“, sagte ihre Mutter. „Erste Etage. Ihr werdet sie mögen!“

Frau Silber wohnte im zweiten Stock. Die Wetter-App zeigte 13 Grad.

Genau aus Frau Silbers Wohnung.

Klopf. Klopf. Klopf.

Nora las: „Der Schleier wird dünner.“ Schatten sah sie an, mit seinen bernsteinfarbenen Augen. Er knurrte. *Lila Tinte.*
"""

EN_GUT = """# Chapter 1: Test

“Come on,” their mother said. “Second floor. You’ll love it!”

Mrs. Silber lived on the third floor. The weather app said 55 degrees.

Right from Mrs. Silber’s apartment.

Thump. Thump. Thump.

Nora read: “The Veil is getting thinner.” Shadow looked at her with his amber eyes. He growled. *Purple ink.*
"""

EN_SCHLECHT = """# Chapter 1: Test

Their mother waved. Their mother smiled. Their mother left the cellar. “Come on!” exclaimed their mother. “First floor. You'll love it, damn it!”

Frau Silber lived on the second floor, in her grey flat. The weather app said 13 degrees. Right from Mrs Silber's apartment. Creepy.

Knock, knock. Knock.

Nora read: “The veil grows thinner und thinner.” Shadow looked at her with golden eyes — he snarled. Purple ink...
"""


def selbsttest():
    register = [("R45", norm("Der Schleier wird dünner."), norm("The Veil is getting thinner."))]
    ok = True
    gut = pruefen(DE_PROBE, EN_GUT, register)
    if gut:
        print("FEHLALARM bei sauberer Übersetzung:", gut)
        ok = False
    schlecht = {k for k, _ in pruefen(DE_PROBE, EN_SCHLECHT, register)}
    erwartet = {"Absätze", "Ausrufezeichen", "Fluch (A2, A8)", "Britisch (A6, A8)", "Anrede ohne Punkt (A8)", "Glossar (A1)",
                "Motiv-Wortlaut (A4)", "Dialogverb (A8)", "Deutsch-Rest", "Stockwerk (E9)",
                "Temperatur (E10)", "Register (A5)", "Mutter (A2)", "Wortwahl nach Pilot (A8 Abschn. 6)",
                "Satzbild (A8)", "Kursiv", "Schattens Code (A4)"}
    for k in sorted(erwartet - schlecht):
        print("FEHLT:", k)
        ok = False
    # Ein-Satz-Absatz braucht gleiche Absatzzahl: eigener Fall
    # Kein Fehlalarm bei Frage + Begleitsatz in US-Reihenfolge (Pilot K1, Absatz 53)
    if pruefen("Eins.\n\n---\n\nZwei.\n", "One.\n\n---\n\nTwo.\n", []):
        print("FEHLALARM: Szenentrenner --- als Gedankenstrich gezählt")
        ok = False
    if pruefen("„Hast du das gehört?“, flüsterte Theo.\n", "“Did you hear that?” Theo whispered.\n", []):
        print("FEHLALARM: Frage vor Begleitsatz als Satzende gezählt")
        ok = False
    de = "Erster Absatz. Zweiter Satz.\n\nGenau aus Frau Silbers Wohnung.\n"
    en = "First paragraph. Second sentence.\n\nRight from Mrs. Silber's apartment. It was cold.\n"
    if not any(k == "Ein-Satz-Absatz" for k, _ in pruefen(de, en, [])):
        print("FEHLT: Ein-Satz-Absatz")
        ok = False
    if not any(k.startswith("Kleines shadow") for k, _ in pruefen("Ein Schatten.\n", "A shadow.\n", [])):
        print("FEHLT: Kleines shadow")
        ok = False
    if pruefen("Ein Schatten. Aber nicht unseren Schatten.\n", "A shadow. But not our Shadow.\n", []):
        print("FEHLALARM: Wortspiel K12 als kleines shadow gemeldet")
        ok = False
    k = konsistenz([("01", "Die Tür ging auf.\n\nStille.\n", "The door opened.\n\nSilence.\n"),
                    ("02", "Die Tür ging auf.\n", "The door swung open.\n"),
                    ("03", "Stille.\n", "Quiet.\n")])
    if [d for d, _ in k] != ["die tür ging auf"]:
        print("FEHLT/FEHLALARM: Konsistenz", [d for d, _ in k])
        ok = False
    if len(register_paare()) < 30:
        print("FEHLT: Register aus A5 eingelesen (weniger als 30 Paare)")
        ok = False
    print("SELBSTTEST BESTANDEN" if ok else "SELBSTTEST FEHLGESCHLAGEN")
    return 0 if ok else 1


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("modus", choices=["pruefen", "bericht", "konsistenz", "hinweise", "selbsttest"])
    ap.add_argument("de", nargs="?")
    ap.add_argument("en", nargs="?")
    a = ap.parse_args()
    if a.modus == "selbsttest":
        sys.exit(selbsttest())
    if a.modus == "hinweise":
        return hinweise()
    if a.modus == "konsistenz":
        ordner = Path(a.de or "Band1/Manuskript_EN")
        paare = [(en.stem[-2:], (ordner / "DE_Basis" / en.name).read_text(encoding="utf-8"), en.read_text(encoding="utf-8"))
                 for en in sorted(ordner.glob("Kapitel_*.md")) if (ordner / "DE_Basis" / en.name).exists()]
        befunde = konsistenz(paare)
        print(f"Kapitel verglichen: {', '.join(k for k, _, _ in paare)}\n")
        for de, vork in befunde:
            print(f"- **{de}**")
            for kap, e in vork:
                print(f"  - K{kap}: {e}")
        print(f"\n{len(befunde)} uneinheitliche Stelle(n). Nicht jede ist ein Fehler — Zusammenhang prüfen.")
        return
    if not (a.de and a.en):
        sys.exit("DE- und EN-Datei angeben")
    de, en = Path(a.de).read_text(encoding="utf-8"), Path(a.en).read_text(encoding="utf-8")
    if a.modus == "bericht":
        return bericht(de, en)
    befunde = pruefen(de, en)
    reg = [nr for nr, d, _ in register_paare() if d in norm(de)]
    print(f"Register-Sätze im deutschen Text: {len(reg)} ({', '.join(reg) or '–'})\n")
    for art, text in befunde:
        print(f"- **{art}:** {text}")
    print(f"\n{len(befunde)} Befund(e).")
    sys.exit(1 if befunde else 0)


if __name__ == "__main__":
    main()
