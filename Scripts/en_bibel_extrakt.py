#!/usr/bin/env python3
"""Phase A der englischen Ausgabe: Rohdaten fuer die Uebersetzungs-Bibel.

Liest die Komplett-Manuskripte von Band 1-5 und erzeugt zwei Rohlisten:

  register  Saetze (>= MIN_WOERTER Woerter), die mehr als einmal vorkommen,
            im selben Band oder ueber Baende hinweg -> Grundlage fuer A5 Satz-Register.
  fallen    Stellen, die beim Uebersetzen Entscheidungen brauchen (Stockwerke,
            Masse, Schule, Kulturbezuege, Sie/du, Sprachbezuege) -> Grundlage fuer A6.

Aufruf:
  python3 Scripts/en_bibel_extrakt.py register [--band1 PFAD]
  python3 Scripts/en_bibel_extrakt.py fallen   [--band1 PFAD]
  python3 Scripts/en_bibel_extrakt.py selbsttest

--band1 erlaubt, die umgebaute Fassung von Band 1 von einem anderen Branch zu lesen.
Die Ausgabe ist Markdown auf stdout; die kuratierten Listen stehen in
Dokumentation/EN_Bibel/.
"""
import argparse
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
    print("SELBSTTEST BESTANDEN" if ok else "SELBSTTEST FEHLGESCHLAGEN")
    return 0 if ok else 1


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("modus", choices=["register", "fallen", "selbsttest"])
    ap.add_argument("--band1")
    a = ap.parse_args()
    if a.modus == "selbsttest":
        sys.exit(selbsttest())
    pfade = baende(a.band1)
    for p in pfade.values():
        if not p.exists():
            sys.exit(f"fehlt: {p}")
    {"register": register, "fallen": fallen}[a.modus](pfade)


if __name__ == "__main__":
    main()
