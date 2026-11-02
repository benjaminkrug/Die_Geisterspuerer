"""
Logik-Vorpruefung (Durchgang A) fuer Staffel-2-Baende.

Duenner Aufsatz auf Scripts/pruefe_logik.py: **alle Checks werden importiert,
nicht nachgebaut** (Logik-Pruefplan Regel 5 - zwei Kopien derselben Regex
driften auseinander). Geaendert sind nur zwei Dinge:

  1. Die Quelle: die Einzelkapitel Staffel2/<label>/Manuskript/Kapitel_*.md
     (pruefe_logik.lade() kennt nur Band1..Band5 und nur kompilierte Dateien).
  2. Check 1 (doppelte Kapiteltitel) laeuft ueber Band 1-5 UND alle
     Staffel-2-Baende - sonst waere "serienweit" an genau der Stelle blind,
     an der die neuen Titel entstehen.

Verwendung:
    python Scripts/pruefe_logik_s2.py S2-5
    python Scripts/pruefe_logik_s2.py S2-5 --alle
"""

import glob
import os
import sys

_HIER = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, _HIER)
import pruefe_logik as L  # noqa: E402

ROOT = os.path.dirname(_HIER)


def lade_s2(label):
    d = os.path.join(ROOT, "Staffel2", label, "Manuskript")
    teile = sorted(glob.glob(os.path.join(d, "Kapitel_*.md")))
    if not teile:
        raise SystemExit(f"Keine Kapitel gefunden: {d}")
    return "\n\n".join(open(p, encoding="utf-8").read().strip() for p in teile) + "\n"


def titel_serienweit():
    tit = {}
    for b in range(1, 6):
        p = os.path.join(ROOT, f"Band{b}", "Manuskript", f"Manuskript_Band{b}_Komplett.md")
        if os.path.exists(p):
            for nr, t, _ in L.kapitel(open(p, encoding="utf-8").read()):
                tit.setdefault(t, []).append(f"B{b}K{nr}")
    for d in sorted(glob.glob(os.path.join(ROOT, "Staffel2", "S2-*"))):
        label = os.path.basename(d)
        try:
            text = lade_s2(label)
        except SystemExit:
            continue
        for nr, t, _ in L.kapitel(text):
            tit.setdefault(t, []).append(f"{label}K{nr}")
    return [f"{t!r} kommt vor in: {', '.join(v)}" for t, v in tit.items() if len(v) > 1]


def main():
    if len(sys.argv) < 2:
        raise SystemExit("Verwendung: python Scripts/pruefe_logik_s2.py S2-5 [--alle]")
    label = sys.argv[1]
    alle = "--alle" in sys.argv
    text = lade_s2(label)

    print("=" * 78)
    print(f"LOGIK-VORPRUEFUNG - {label}   ({len(L.kapitel(text))} Kapitel, "
          f"{len(text.split()):,} Woerter)")
    print("=" * 78)
    print("Alle Treffer sind KANDIDATEN. Jeden im Kontext lesen (Regel 1).")

    n = 0
    n += L.zeige("1. Doppelte Kapiteltitel (serienweit, inkl. Staffel 2)", titel_serienweit())
    n += L.zeige("2. Zeitangaben", L.check_zeitangaben(text))
    n += L.zeige("3. Zahlen, die zusammenpassen muessen", L.check_zahlen(text))
    n += L.zeige("4. Verdaechtige Sprechverben", L.check_sprechverben(text))
    n += L.zeige("5. Verbotene Begriffe (Content-Grenzen)", L.check_verbotene_begriffe(text))
    n += L.zeige("6. POV-Bruch (Innenleben anderer Figuren)", L.check_pov(text))
    n += L.zeige("7. Kapitel ohne Schatten-REAKTION", L.check_schatten(text))
    n += L.zeige("8. Woertlich wiederholte Saetze", L.check_wiederholte_saetze(text))
    n += L.zeige("9. VIERTE WAND (Meta-Sprache)", L.check_vierte_wand(text))
    L.zeige("9. Kapitel-Schlusssaetze (Cliffhanger-Pflicht)", L.check_cliffhanger(text), limit=30)
    if alle:
        L.zeige("10. Wort-Echo im Satz", L.check_wort_echo(text), limit=8)
        L.zeige("11. Pronomen-Ambiguitaet", L.check_pronomen(text), limit=8)
        L.zeige("12. Tageszeit-Spruenge", L.check_tageszeit(text), limit=8)
    print("\n" + "=" * 78)
    print(f"{n} Kandidaten in den Checks mit hoher Trefferquote.")


if __name__ == "__main__":
    main()
