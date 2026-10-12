#!/usr/bin/env python3
"""Phase A der englischen Ausgabe: Rohdaten fuer die Uebersetzungs-Bibel.

Liest die Komplett-Manuskripte von Band 1-5 und erzeugt zwei Rohlisten:

  register  Saetze (>= MIN_WOERTER Woerter), die mehr als einmal vorkommen,
            im selben Band oder ueber Baende hinweg -> Grundlage fuer A5 Satz-Register.
  fallen    Stellen, die beim Uebersetzen Entscheidungen brauchen (Stockwerke,
            Masse, Schule, Kulturbezuege, Sie/du, Sprachbezuege) -> Grundlage fuer A6.
  stimmen   Wörtliche Rede je Figur und Band (Anzahl, Länge, Fragen, Ausrufe,
            Beispielsätze) -> Grundlage fuer A2.
  motive    Wiederkehrende Bilder je Band mit ihren genauen Wortlauten -> Grundlage fuer A4.

Aufruf:
  python3 Scripts/en_bibel_extrakt.py register [--band1 PFAD]
  python3 Scripts/en_bibel_extrakt.py fallen   [--band1 PFAD]
  python3 Scripts/en_bibel_extrakt.py stimmen  [--band1 PFAD]
  python3 Scripts/en_bibel_extrakt.py motive   [--band1 PFAD]
  python3 Scripts/en_bibel_extrakt.py selbsttest

--band1 erlaubt, die umgebaute Fassung von Band 1 von einem anderen Branch zu lesen.
Die Ausgabe ist Markdown auf stdout; die kuratierten Listen stehen in
Dokumentation/EN_Bibel/.
"""
import argparse
import tempfile
import re
import sys
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
MIN_WOERTER = 4

FALLEN = {
    "Stockwerk": r"(?i)\b(Erdgeschoss\w*|Dachgeschoss\w*|Etage\w*|(?:ersten|zweiten|dritten|obersten|erste[rn]?|zweite[rn]?|dritte[rn]?|oberste[rn]?)\s+Stock(?:werk)?\w*)\b",
    "Mass/Zahl": r"\b\d+\s*(?:Grad|Meter|Zentimeter|Kilometer|Kilo|Gramm|Liter)\b|\b(?:ein|zwei|drei|vier|fünf|sechs|sieben|acht|neun|zehn|zwanzig|dreißig|hundert)\w*\s+(?:Grad|Meter|Zentimeter|Kilometer|Kilo|Kilogramm|Liter)\b",
    "Schule": r"\b(Klasse\w*|Gymnasium|Grundschule|Realschule|Gesamtschule|Zeugnis\w*|Hausaufgabe\w*|große[n]? Pause|Sommerferien|Herbstferien)\b",
    "Kultur/Alltag": r"\b(Adventskalender|Weihnachtsmarkt|Fasching|Karneval|Sankt Martin|Laterne\w*|Brezel\w*|Kakao|Müsli|Pfand\w*|Bäcker\w*|Kiosk|Schultüte|Bohnerwachs|Handy\w*|Altbau|Schrebergarten|Stammtisch|Feierabend|Kaffee und Kuchen|Mikrofiche)\b",
    "Anrede Frau/Herr": r"\b(Frau|Herr)\s+[A-ZÄÖÜ]\w+",
    "Sie/du-Wechsel": r"\b(duzen|siezen|geduzt|gesiezt|du darfst du sagen)\b",
    "Sprachbezug": r"\b(deutsch\w*|Wortspiel|buchstabier\w*|reimt?|Anfangsbuchstabe\w*|rückwärts gelesen)\b",
}


def baende(band1):
    pfade = {1: Path(band1) if band1 else ROOT / "Band1/Manuskript/Manuskript_Band1_Komplett.md"}
    for n in range(2, 6):
        pfade[n] = ROOT / f"Band{n}/Manuskript/Manuskript_Band{n}_Komplett.md"
    return pfade


def kapitel_zeilen(text):
    """Liefert (kapitelnummer, zeile) fuer jede Zeile."""
    kap = 0
    for zeile in text.splitlines():
        m = re.match(r"#\s*Kapitel\s+(\d+)", zeile)
        if m:
            kap = int(m.group(1))
            continue
        yield kap, zeile


def normalisiere(satz):
    satz = satz.replace("*", "")
    satz = re.sub(r"[„“”\"'‚‘’»«]", "", satz)
    satz = re.sub(r"\s+", " ", satz).strip(" -–—")
    return satz


def saetze(zeile):
    # Wörtliche Rede und Begleitsatz getrennt behandeln: „Es gibt eine Erklärung“, sagte Nora.
    # soll als „Es gibt eine Erklärung“ gezählt werden, egal wer es sagt.
    for abschnitt in re.split(r"[„“”\"]", zeile):
        for teil in re.split(r"(?<=[.!?…])\s+", abschnitt):
            s = normalisiere(teil).strip(" ,;:")
            if s.startswith(("sagte", "flüsterte", "rief", "murmelte", "zischte", "fragte")):
                continue
            if len(s.split()) >= MIN_WOERTER:
                yield s


def register(pfade):
    fund = defaultdict(list)
    for band, pfad in pfade.items():
        for kap, zeile in kapitel_zeilen(pfad.read_text(encoding="utf-8")):
            for s in saetze(zeile):
                fund[s.lower()].append((band, kap, s))
    treffer = {k: v for k, v in fund.items() if len(v) > 1}
    ueber_baende = {k: v for k, v in treffer.items() if len({b for b, _, _ in v}) > 1}
    print(f"# Rohliste Satz-Register (Saetze >= {MIN_WOERTER} Woerter, mehrfach)\n")
    print(f"Mehrfache Saetze gesamt: {len(treffer)} · davon ueber Baende hinweg: {len(ueber_baende)}\n")
    print("| Satz | Vorkommen | Stellen |\n|---|---|---|")
    for k, v in sorted(treffer.items(), key=lambda kv: (-len({b for b, _, _ in kv[1]}), -len(kv[1]), kv[0])):
        stellen = ", ".join(f"B{b} K{c}" for b, c, _ in v)
        print(f"| {v[0][2]} | {len(v)} | {stellen} |")


def fallen(pfade):
    print("# Rohliste Fallen (Stellen mit Uebersetzungs-Entscheidung)\n")
    for name, muster in FALLEN.items():
        rx = re.compile(muster)
        zaehl = defaultdict(int)
        beispiele = defaultdict(list)
        for band, pfad in pfade.items():
            for kap, zeile in kapitel_zeilen(pfad.read_text(encoding="utf-8")):
                for m in rx.finditer(zeile):
                    wort = m.group(0)
                    zaehl[wort] += 1
                    if len(beispiele[wort]) < 3:
                        beispiele[wort].append(f"B{band} K{kap}")
        print(f"## {name}\n")
        if not zaehl:
            print("_keine Treffer_\n")
            continue
        print("| Ausdruck | Anzahl | erste Stellen |\n|---|---|---|")
        for wort, n in sorted(zaehl.items(), key=lambda kv: -kv[1]):
            print(f"| {wort} | {n} | {', '.join(beispiele[wort])} |")
        print()


# Sprecher: Name im Begleitsatz. Reihenfolge = Vorrang bei mehreren Namen im Absatz.
SPRECHER = {
    "Nora": r"\bNora\b",
    "Theo": r"\bTheo\b",
    "Mutter": r"\b(?:ihre Mutter|Mama|Mutter)\b",
    "Frau Silber": r"\b(?:Frau Silber|Margret|Silber)\b(?!s)",
    "Frau Held": r"\bFrau Held\b",
    "Pawlik": r"\bPawlik\b",
    "Kloß": r"\bKloß\b",
    "Faber": r"\bFaber\b",
    "Graven": r"\bGraven\b",
    "Marlene": r"\b(?:Marlene|Frau Weber)\b",
    "Jonas": r"\bJonas\b",
    "Brenner": r"\bBrenner\b",
    "Voss": r"\bVoss\b",
}
REDE = re.compile(r"[„\"]([^“”\"]+)[“”\"]")
VERB = r"(?:sagte|flüsterte|rief|murmelte|zischte|fragte|antwortete|meinte|schrie|brummte|knurrte)"


def sprecher_von(zeile):
    """Sprecher aus dem Begleitsatz. Erst 'sagte X' / 'X sagte', dann erster Name außerhalb der Rede."""
    rest = REDE.sub(" ", zeile)
    for name, rx in SPRECHER.items():
        if re.search(VERB + r"\s+" + rx, rest) or re.search(rx + r"\s+" + VERB, rest):
            return name
    treffer = [(m.start(), name) for name, rx in SPRECHER.items() for m in [re.search(rx, rest)] if m]
    return min(treffer)[1] if treffer else None


def reden(pfade):
    """(band, kap, sprecher, sicher, text) für jede wörtliche Rede. Ohne Begleitsatz: Wechsel der
    letzten beiden Sprecher (typisches Hin und Her) — als 'erschlossen' markiert."""
    for band, pfad in pfade.items():
        letzte = []
        for kap, zeile in kapitel_zeilen(pfad.read_text(encoding="utf-8")):
            teile = REDE.findall(zeile)
            if not teile:
                if zeile.strip():
                    letzte = letzte[-2:]
                continue
            wer = sprecher_von(zeile)
            sicher = wer is not None
            if not sicher and len(letzte) >= 2 and letzte[-1] != letzte[-2]:
                wer = letzte[-2]
            if wer:
                letzte.append(wer)
            text = " ".join(t.strip() for t in teile)
            yield band, kap, wer or "?", sicher, text


def stimmen(pfade):
    daten = defaultdict(list)
    for band, kap, wer, sicher, text in reden(pfade):
        daten[wer].append((band, kap, sicher, text))
    print("# Rohliste Stimmen (wörtliche Rede je Figur)\n")
    print("Sprecher ohne Begleitsatz sind aus dem Wechsel erschlossen (Spalte 'sicher' zählt nur Begleitsätze).\n")
    print("| Figur | Reden | davon sicher | Bände | Wörter/Rede | Fragen | Ausrufe | ≤ 3 Wörter |\n|---|---|---|---|---|---|---|---|")
    for wer, r in sorted(daten.items(), key=lambda kv: -len(kv[1])):
        w = [len(t.split()) for _, _, _, t in r]
        b = "".join(str(x) for x in sorted({x for x, _, _, _ in r}))
        print(f"| {wer} | {len(r)} | {sum(s for _, _, s, _ in r)} | {b} | {sum(w)/len(w):.1f} | "
              f"{sum('?' in t for *_, t in r)*100//len(r)} % | {sum('!' in t for *_, t in r)*100//len(r)} % | "
              f"{sum(x <= 3 for x in w)*100//len(r)} % |")
    for wer, r in sorted(daten.items(), key=lambda kv: -len(kv[1])):
        if wer == "?" or len(r) < 5:
            continue
        print(f"\n## {wer}\n")
        sicher = [x for x in r if x[2]]
        schritt = max(1, len(sicher) // 12)
        for band, kap, _, text in sicher[::schritt][:12]:
            print(f"- B{band} K{kap}: {text}")


MOTIVE = {
    "Klopfen": r"\b[Kk]lopf\w*",
    "Kälte/Atem": r"\b(?:eiskalt\w*|Kälte\w*|Atem\w* dampf\w*|dampfend\w* Atem)",
    "Kondenswasser": r"\b(?:Kondenswasser|beschlagen\w*)",
    "Bernsteinaugen": r"\bbernstein\w*",
    "Tinte": r"\bTinte\w*",
    "grau/durchscheinend": r"\b(?:durchscheinend\w*|durchsichtig\w*)",
    "metallisch": r"\bmetallisch\w*",
    "Gänsehaut/Nacken": r"\b(?:Gänsehaut|Nackenhaar\w*)",
    "Schleier": r"\bSchleier\w*",
    "blaues Leuchten": r"\bblau\w*\s+(?:Leuchten|Licht|Schimmer)\w*",
    "Karte/Markierung": r"\bMarkierung\w*",
    "Lavendel": r"\bLavendel\w*",
}


def motive(pfade):
    print("# Rohliste Motive (Anzahl je Band, häufigste Wortlaute)\n")
    print("| Motiv | B1 | B2 | B3 | B4 | B5 |\n|---|---|---|---|---|---|")
    wortlaute = defaultdict(lambda: defaultdict(list))
    for name, muster in MOTIVE.items():
        rx = re.compile(muster)
        je_band = defaultdict(int)
        for band, pfad in pfade.items():
            for kap, zeile in kapitel_zeilen(pfad.read_text(encoding="utf-8")):
                for s in re.split(r"(?<=[.!?…])\s+", zeile):
                    if rx.search(s):
                        je_band[band] += 1
                        wortlaute[name][normalisiere(s)].append(f"B{band} K{kap}")
        print(f"| {name} | " + " | ".join(str(je_band[b]) for b in range(1, 6)) + " |")
    for name, w in wortlaute.items():
        print(f"\n## {name}\n")
        for satz, stellen in sorted(w.items(), key=lambda kv: -len(kv[1]))[:10]:
            print(f"- ({len(stellen)}×) {satz[:160]} — {', '.join(stellen[:4])}")


def selbsttest():
    """Eingeschleuste Faelle muessen gefunden werden, sonst ist das Skript wertlos."""
    text = (
        "# Kapitel 1\n„Es gibt eine Erklärung“, sagte Nora.\nIm ersten Stock war es kalt, zehn Grad.\n"
        "# Kapitel 2\n„Es gibt eine Erklärung“, sagte Nora leise.\nSie trank Kakao.\n"
        "Dritter Stock, Regal acht. Frau Silbers Wohnung war leer.\n"
    )
    ok = True
    gefunden = defaultdict(list)
    for kap, zeile in kapitel_zeilen(text):
        for s in saetze(zeile):
            gefunden[s.lower()].append(kap)
    # Derselbe Satz mit unterschiedlichem Begleitsatz muss als EIN Eintrag mit 2 Stellen zählen.
    if gefunden.get("es gibt eine erklärung") != [1, 2]:
        print("FEHLT: wiederkehrender Satz trotz anderem Begleitsatz", dict(gefunden))
        ok = False
    # Jeder erwartete Ausdruck muss einzeln gefunden werden (auch am Satzanfang, auch im Genitiv).
    for name, erwartet in (("Stockwerk", "ersten Stock"), ("Stockwerk", "Dritter Stock"), ("Mass/Zahl", "zehn Grad"),
                           ("Kultur/Alltag", "Kakao"), ("Anrede Frau/Herr", "Frau Silbers")):
        if erwartet not in [m.group(0) for m in re.finditer(FALLEN[name], text)]:
            print(f"FEHLT: {name} ({erwartet})")
            ok = False
    # Sprecher: Begleitsatz vor und nach der Rede, und erschlossener Wechsel ohne Begleitsatz.
    dialog = ("# Kapitel 1\n„Ich sage, wir drehen um“, sagte Theo.\n\n„Theo.“\n\nNora sagte: „Nein.“\n\n"
              "„Doch.“\n\n„Kommt“, sagte ihre Mutter.\n")
    with tempfile.NamedTemporaryFile("w", suffix=".md", delete=False, encoding="utf-8") as f:
        f.write(dialog)
        probe = Path(f.name)
    erwartet = ["Theo", "Theo", "Nora", "Theo", "Mutter"]
    gefunden_wer = [w for _, _, w, _, _ in reden({1: probe})]
    probe.unlink()
    # „Theo.“ steht ohne Begleitsatz: Der Name IN der Rede darf nicht als Sprecher zählen.
    # Nach Theo und Nora ist „Doch.“ aus dem Wechsel erschlossen wieder Theo.
    if gefunden_wer != erwartet[:1] + ["?"] + erwartet[2:]:
        print("FEHLT: Sprecherzuordnung", gefunden_wer)
        ok = False
    print("SELBSTTEST BESTANDEN" if ok else "SELBSTTEST FEHLGESCHLAGEN")
    return 0 if ok else 1


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("modus", choices=["register", "fallen", "stimmen", "motive", "selbsttest"])
    ap.add_argument("--band1")
    a = ap.parse_args()
    if a.modus == "selbsttest":
        sys.exit(selbsttest())
    pfade = baende(a.band1)
    for p in pfade.values():
        if not p.exists():
            sys.exit(f"fehlt: {p}")
    {"register": register, "fallen": fallen, "stimmen": stimmen, "motive": motive}[a.modus](pfade)


if __name__ == "__main__":
    main()
