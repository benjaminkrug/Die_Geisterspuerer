"""
Kontrolle fuer den schrittweisen Umbau von Band 1 (Band1/PLAN_Durchlesequote.md, Abschnitt 7).

Vergleicht das Manuskript mit einem Git-Stand (Basis) und prueft harte Regeln.
Aendert NICHTS am Text.

Verwendung:
    py Scripts/pruefe_band1_umbau.py                 # Basis = HEAD
    py Scripts/pruefe_band1_umbau.py --basis band1-vor-umbau   # Basis = Tag vor dem Umbau
    py Scripts/pruefe_band1_umbau.py --schritt 2     # zusaetzlich die Zielwerte von Schritt 2

Exit-Code 0 = alle harten Pruefungen bestanden, 1 = mindestens eine nicht bestanden.

★ WAS DAS SKRIPT NICHT KANN
  Es prueft keine Qualitaet und keine Logik. Ein gruener Lauf heisst nur: Kein Anker
  fehlt, keine Grenze ist gerissen. Lesen muss trotzdem ein Mensch (Logik_Pruefplan, Regel 1).
  Treffer sind Kandidaten (Regel 5): erst das Suchmuster pruefen, dann dem Treffer glauben.
"""

import os
import re
import subprocess
import sys

_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REL = "Band1/Manuskript/Manuskript_Band1_Komplett.md"

# --- Pflicht-Anker -----------------------------------------------------------
# Alles, worauf sich Band 2-5, der Klappentext oder die Leseprobe stuetzen.
# (Bezeichnung, Regex, Mindestzahl, Begruendung). Belegt per Textsuche 2026-10-10.
ANKER = [
    ("Kirchgasse 14", r"Kirchgasse 14", 1, "Klappentext, Kanon: Haus der Familie"),
    ("HILF", r"\bHILF\b", 1, "Klappentext"),
    ("HIER", r"\bHIER\b", 1, "Wortfolge Kondenswasser"),
    ("VERGISS NICHT", r"VERGISS NICHT", 1, "Wortfolge Kondenswasser"),
    ("DANKE", r"\bDANKE\b", 1, "Wortfolge Kondenswasser"),
    ("Kondenswasser", r"Kondenswasser", 1, "Klappentext, B5"),
    ("Lina Vogt", r"Lina Vogt", 1, "Klappentext, Kanon"),
    ("1974", r"1974", 1, "Klappentext, Kanon"),
    ("Unfall (Zeitung)", r"Unfall", 1, "Kanon: 'Unfallfolgen' - darf nicht ersetzt werden"),
    ("Tagebuch", r"Tagebuch", 1, "B2, B5"),
    ("Keller", r"Keller", 1, "Kanon: dort starb Lina"),
    ("goldenes Licht", r"golden", 1, "B2, B3, B5 erinnern an das goldene Licht"),
    ("Margret Silber", r"Margret Silber", 1, "B3-B5"),
    ("Namensliste", r"Namensliste|Liste", 1, "Klappentext, B2-B5"),
    ("Foto Silber + Hund", r"M\. Silber, 2019", 1, "Schattens Herkunft (B3)"),
    ("Notizbuch", r"Notizbuch", 1, "B2-B5: Karte, Brief, Notizbuch als drei Dinge"),
    ("Brief", r"Brief", 1, "B4 Z.960, B5 Z.298/562"),
    ("Karte", r"Karte", 1, "B2-B5"),
    ("zwoelf Markierungen", r"[Zz]w(ö|oe)lf", 1, "B2-Leseprobe, Kanon"),
    ("durchgestrichen", r"durchgestrichen", 1, "B2 nimmt die frische Tinte auf"),
    ("Heinrich B. / 1887", r"Heinrich B\.", 1, "B2: 15x '1887'"),
    ("1887", r"1887", 1, "B2"),
    ("GRAVEN", r"GRAVEN", 1, "B2-B5"),
    ("Alwin Graven", r"Alwin Graven", 1, "B4, B5"),
    ("1823", r"1823", 1, "B5, Kanon"),
    ("roter Kreis", r"rote[nr]? Kreis|Kreis.{0,40}rot", 1, "B3-B5 'der rote Kreis'"),
    ("Der Erste", r"[Dd](er|en|em) Erste", 1, "B3-B5"),
    ("Die Unruhigen", r"Unruhige", 1, "B2, B3"),
    ("Schleier", r"Schleier", 1, "B2-B5"),
    ("Anrede Brief", r"Die, die nach mir kommen", 1, "B4 Z.960 'jemandem hinterlassen'"),
    ("Anna (1923)", r"Anna", 1, "B2, B4"),
    ("bernsteinfarben", r"bernsteinfarben", 1, "Klappentext, Kanon"),
]

# --- Schutz fuer Punkt 2: keine neuen Fakten zu Linas Tod ---------------------
# Ein Satz, der Lina mit diesen Woertern verbindet, waere ein neuer Fakt,
# der Band 4 (Faber, kaltes Zimmer) beruehren kann. Neue Treffer = nicht bestanden.
U2_SCHUTZ = r"(gestürzt|Sturz|stürzte|Treppe hinunter|Faber|Uhren|Schleier|Riss|wer.{0,20}heimgesucht)"

VERBOTEN = r"\b(Manifestation|paranormal|Entität|Entitaet|Leiche|blutig|Blutlache)\b"

# --- Zielwerte je Schritt (Plan Abschnitt 7.4: 2=Schluss, 4=Zone A, 5=Mittelteil) --------------------------------
# (Bezeichnung, Regex, Hoechstzahl) - gezaehlt im ganzen Buch.
ZIELE = {
    2: [("'Wir hören auf' als Entscheidung", r"Wir hören auf", 1),
        ("'Hand hat gezittert, als sie über ihn'", r"gezittert, als sie über ihn", 1),
        ("Bibliothek im Schlussteil", r"Schon wieder ihr zwei", 0),
        ("'Morgen fangen wir an'", r"Morgen fangen wir an", 0)],
    4: [("zweite Bibliothek-Ausrede", r"Für die Schule\?", 1)],
    5: [("'offiziell festhalten/protokoll'", r"offiziell festhalten|protokoll", 2),
        ("Tagebuch-Zitat in K12 (Datum)", r"(Vierzehnter September|Fünfzehnter Oktober|Siebundzwanzigster Oktober)", 0)],
}


def lade_aktuell():
    return open(os.path.join(_ROOT, REL), encoding="utf-8").read()


def lade_basis(ref):
    try:
        return subprocess.run(["git", "-C", _ROOT, "show", f"{ref}:{REL}"],
                              capture_output=True, text=True, check=True,
                              encoding="utf-8").stdout
    except subprocess.CalledProcessError:
        sys.exit(f"Basis '{ref}' nicht gefunden.")


def kapitel(text):
    teile = re.split(r"^# (Kapitel \d+.*)$", text, flags=re.M)
    return [(teile[i].strip(), teile[i + 1]) for i in range(1, len(teile), 2)]


def woerter(t):
    return len(re.sub(r"^#.*$", "", t, flags=re.M).split())


def erzaehler(t):
    t = t.replace("“", '"').replace("„", '"')
    return re.sub(r'"[^"\n]*"', " ", t)


def lange_saetze(t, grenze=18):
    s = re.split(r"(?<=[.!?])\s+", erzaehler(t))
    return [x.strip() for x in s if len(x.split()) > grenze]


def letzter_absatz(body):
    abs_ = [a.strip() for a in body.split("\n\n")
            if a.strip() and a.strip() != "---" and not a.strip().startswith("**ENDE")]
    return abs_[-1] if abs_ else ""


def saetze_mit(t, wort, muster):
    s = re.split(r"(?<=[.!?])\s+", t)
    return {x.strip() for x in s if wort in x and re.search(muster, x)}


def stimme(text):
    """Stimmen-Werte wie Dokumentation/Stimmen_Pruefplan.md Abschnitt 5 (gleiche Definitionen),
    aber je 1.000 Woerter, damit alte und gekuerzte Fassung vergleichbar sind."""
    body = "\n".join(l for l in text.splitlines() if not l.startswith("#"))
    paras = [p.strip() for p in body.split("\n\n") if p.strip() and p.strip() not in ("---", "***")
             and not p.strip().startswith("**ENDE")]
    W = len(re.findall(r"[A-Za-zÄÖÜäöüß']+", body))
    erz = 0
    for p in paras:
        if '"' in p or "\u201e" in p:
            continue
        erz += sum(1 for s in re.split(r"(?<=[.!?])\s+", p) if re.match(r"Und ", s.strip().lstrip('"\u201e»—* ')))
    kurz = [p for p in paras if len(re.findall(r"[A-Za-zÄÖÜäöüß']+", p)) <= 4 and '"' not in p and "\u201e" not in p]
    erz_text = erzaehler(body)
    saetze = [s for s in re.split(r"(?<=[.!?])\s+", erz_text) if s.strip()]
    return {
        "Und-Anfang Erzähler /1000 W": 1000 * erz / W,
        "Kurzabsätze (≤4 W) %": 100 * len(kurz) / len(paras),
        "Ø Wörter je Erzählsatz": sum(len(s.split()) for s in saetze) / len(saetze),
        "Ø Wörter je Absatz": W / len(paras),
        "'zum ersten Mal' /1000 W": 1000 * len(re.findall(r"[Zz]um ersten Mal", body)) / W,
    }


def main():
    args = sys.argv[1:]
    basis_ref = args[args.index("--basis") + 1] if "--basis" in args else "HEAD"
    schritt = int(args[args.index("--schritt") + 1]) if "--schritt" in args else None
    neu, alt = lade_aktuell(), lade_basis(basis_ref)
    fehler = 0

    def ergebnis(ok, text):
        nonlocal fehler
        fehler += 0 if ok else 1
        print(("  OK    " if ok else "  NEIN  ") + text)

    print(f"Basis: {basis_ref}   Datei: {REL}\n")

    print("K1 Pflicht-Anker (Band 2-5, Klappentext)")
    for name, rx, mind, warum in ANKER:
        n = len(re.findall(rx, neu))
        if n < mind:
            ergebnis(False, f"{name}: {n}x (mind. {mind}) - {warum}")
    if fehler == 0:
        print(f"  OK    alle {len(ANKER)} Anker vorhanden")

    print("\nK2 Wortzahl")
    wa, wn = woerter(alt), woerter(neu)
    print(f"  Basis {wa}  ->  jetzt {wn}  (Differenz {wn - wa:+d})")
    ka, kn = dict(kapitel(alt)), kapitel(neu)
    for titel, body in kn:
        diff = woerter(body) - woerter(ka.get(titel, ""))
        flag = "" if titel in ka else "   [neu/umbenannt]"
        if diff or flag:
            print(f"    {titel[:40]:40} {woerter(body):5} W ({diff:+d}){flag}")
    for titel in ka:
        if titel not in dict(kn):
            print(f"    {titel[:40]:40} ENTFERNT/umbenannt")

    print("\nK3 Anführungszeichen")
    auf, zu_ascii, zu_typo = neu.count("„"), neu.count('"'), neu.count("“")
    ergebnis(auf == zu_ascii + zu_typo,
             f"öffnend {auf} / schließend {zu_ascii + zu_typo} (ASCII {zu_ascii}, typogr. {zu_typo})")

    print("\nK4 Schatten (der Hund) in jedem Kapitel")
    # Kap. 1 nennt ihn nur "der Hund" - er bekommt seinen Namen erst in Kap. 2.
    # "Schatten" heisst auch "Schatten an der Wand": nur ein Anwesenheits-Indiz (Regel 5).
    leer = [t for t, b in kn if not re.search(r"\bSchatten\b|\bHund\b", b)]
    ergebnis(not leer, "jedes Kapitel nennt Schatten/den Hund" if not leer else f"fehlt in: {leer}")

    print("\nK5 Sätze über 18 Wörter (nur Erzähltext)")
    la, ln = set(lange_saetze(alt)), set(lange_saetze(neu))
    neue_lange = ln - la
    ergebnis(not neue_lange, f"Basis {len(la)}, jetzt {len(ln)}, davon NEU {len(neue_lange)}")
    for s in list(neue_lange)[:8]:
        print(f"        > {s[:110]}")

    print("\nK6 Kapitelenden (Cliffhanger)")
    enden_alt = {t: letzter_absatz(b) for t, b in kapitel(alt)}
    for t, b in kn:
        e = letzter_absatz(b)
        if enden_alt.get(t) != e:
            print(f"  GEÄNDERT {t[:34]:34} -> „{e[:70]}“")
    print("  (Jede Änderung hier muss im Schritt erlaubt sein, sonst zurücknehmen.)")

    print("\nK7 Verbotene Wörter")
    va, vn = len(re.findall(VERBOTEN, alt)), len(re.findall(VERBOTEN, neu))
    ergebnis(vn <= va, f"Basis {va}, jetzt {vn}")

    print("\nK8 Schutz Punkt 2: keine neuen Fakten zu Linas Tod")
    sa, sn = saetze_mit(alt, "Lina", U2_SCHUTZ), saetze_mit(neu, "Lina", U2_SCHUTZ)
    neue = sn - sa
    ergebnis(not neue, f"neue Sätze mit Lina + Sturz/Faber/Schleier/...: {len(neue)}")
    for s in list(neue)[:5]:
        print(f"        > {s[:110]}")
    # Faber gehoert Band 4 und kommt in Band 1 nicht vor (Basis: 0). Jede Nennung waere
    # ein Vorgriff, der Band 4 beruehrt - auch ohne das Wort "Lina" im selben Satz.
    fa, fn = len(re.findall(r"Faber|Cornelius", alt)), len(re.findall(r"Faber|Cornelius", neu))
    ergebnis(fn <= fa, f"Faber/Cornelius: Basis {fa}, jetzt {fn}")

    print("\nK10 Stimme gegen die Basis (Band 1 ist der Stimmen-Maßstab der Serie)")
    # Hart: die beiden Werte, die der Stimmen-Pruefplan als Drift-Signal fuehrt, +-15 %.
    # Die anderen sind Hinweise - bei kleinen Zahlen schwanken sie stark (Regel 5).
    sa_, sn_ = stimme(alt), stimme(neu)
    for k in sa_:
        rel = (sn_[k] - sa_[k]) / sa_[k] * 100 if sa_[k] else 0
        hart = k in ("Und-Anfang Erzähler /1000 W", "Kurzabsätze (≤4 W) %")
        text = f"{k}: Basis {sa_[k]:.2f}, jetzt {sn_[k]:.2f} ({rel:+.0f} %)"
        if hart:
            ergebnis(abs(rel) <= 15, text + "  [Korridor ±15 %]")
        else:
            print("  INFO  " + text)

    if schritt in ZIELE:
        print(f"\nK9 Zielwerte Schritt {schritt}")
        for name, rx, hoechst in ZIELE[schritt]:
            n = len(re.findall(rx, neu))
            ergebnis(n <= hoechst, f"{name}: {n}x (höchstens {hoechst})")

    print("\n" + ("ALLE HARTEN PRÜFUNGEN BESTANDEN" if fehler == 0
                  else f"{fehler} PRÜFUNG(EN) NICHT BESTANDEN"))
    sys.exit(0 if fehler == 0 else 1)


if __name__ == "__main__":
    main()
