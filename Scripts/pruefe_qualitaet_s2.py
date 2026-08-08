"""
Qualitaets-Messung (Teil A) fuer Staffel 2 — im Vergleich mit Band 1-5.

Duenner Aufsatz auf Scripts/pruefe_qualitaet.py: **die Messfunktionen werden
importiert, nicht nachgebaut.** Regel 5 des Logik-Pruefplans ("das Werkzeug hat
auch Fehler") gilt doppelt fuer nachgebaute Muster — zwei Kopien derselben Regex
driften auseinander, und dann misst man zwei verschiedene Dinge.

Geaendert ist nur die Quelle: pruefe_qualitaet.lade() kennt ausschliesslich
Band1..Band5; dieses Skript reicht zusaetzlich die Staffel-2-Baende nach.

Verwendung:
    python Scripts/pruefe_qualitaet_s2.py

Liest bevorzugt das kompilierte Manuskript (Phase 5). Fehlt es, setzt es die
Einzelkapitel zusammen — damit die Messung auch vor dem Kompilieren laeuft.

⚠️ Was hier NICHT gemessen wird, steht in Dokumentation/Qualitaets_Pruefplan.md
   Abschnitt F0: Gruselwort-Dichte, Humor und Eskalationskurve sind an Band 1-5
   nachweislich anti-korreliert oder gar nicht auffindbar.
"""

import os
import re
import sys
import glob
import statistics as st

_HIER = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, _HIER)
import pruefe_qualitaet as Q          # noqa: E402  (Pfad muss vorher stehen)

ROOT = os.path.dirname(_HIER)

STAFFEL2 = {
    "S2-1": "Der Gast, der blieb",
}


def lade_s2(label: str):
    """Kompiliertes Manuskript, sonst die Einzelkapitel."""
    d = os.path.join(ROOT, "Staffel2", label, "Manuskript")
    fertig = os.path.join(d, f"Manuskript_{label}_Komplett.md")
    if os.path.exists(fertig):
        return open(fertig, encoding="utf-8").read(), "kompiliert"
    teile = sorted(glob.glob(os.path.join(d, "Kapitel_*.md")))
    if not teile:
        return None, None
    return "\n\n".join(open(p, encoding="utf-8").read().strip()
                       for p in teile) + "\n", "Einzelkapitel"


def messe(text):
    kaps = Q.kapitel(text)
    ab = Q.absaetze(kaps[0][1])

    def worte_bis(pruef):
        w = 0
        for p in ab:
            if pruef(p):
                return w
            w += len(p.split())
        return w

    ks = [len(body.split()) for _, body in kaps]
    w1 = sum(len(p.split()) for p in ab)
    d1 = sum(len(p.split()) for p in ab if Q.ist_dialog(p))

    body = text[text.index("# Kapitel 1"):]
    wl = body.split()
    probe = " ".join(wl[:int(len(wl) * 0.10)])

    return {
        "dialog_w": worte_bis(Q.ist_dialog),
        "grusel_w": worte_bis(lambda p: re.search(Q.UNHEIMLICH, p, re.I)),
        "k1_w": w1,
        "k1_dialog": 100 * d1 // w1,
        "erster_satz": ab[0].split(".")[0][:52],
        "kapitel": len(ks),
        "mittel": st.mean(ks),
        "max": max(ks),
        "min": min(ks),
        "streuung": st.pstdev(ks),
        "letzter_absatz": Q.absaetze(kaps[-1][1])[-1][:60],
        "probe_w": len(probe.split()),
        "probe_signale": len(re.findall(Q.UNHEIMLICH, probe, re.I)),
    }


def main():
    reihe = []
    for b in sorted(Q.TITEL):
        t = Q.lade(b)
        if t:
            reihe.append((f"Band {b}", Q.TITEL[b], messe(t), "kompiliert"))
    for label in STAFFEL2:
        t, quelle = lade_s2(label)
        if t:
            reihe.append((label, STAFFEL2[label], messe(t), quelle))

    print("=" * 96)
    print("QUALITAETS-MESSUNG TEIL A — Staffel 1 und Staffel 2 nebeneinander")
    print("=" * 96)
    print("\n>> IN WOERTERN GEMESSEN, NIE IN ABSAETZEN (Fehlbefund 2026-07-18).\n")

    print(f"{'Band':<7} {'->Rede':<8} {'->Grusel':<10} {'K1 W':<7} {'Dial%':<7} "
          f"{'Kap.':<6} {'Ø W':<7} {'min':<6} {'max':<6} {'Streu':<6}")
    print("-" * 96)
    for name, _titel, m, _q in reihe:
        print(f"{name:<7} {m['dialog_w']:<8} {m['grusel_w']:<10} {m['k1_w']:<7} "
              f"{m['k1_dialog']:<7} {m['kapitel']:<6} {m['mittel']:<7.0f} "
              f"{m['min']:<6} {m['max']:<6} {m['streuung']:<6.0f}")

    print("\n  Richtwerte: erstes Unheimliches <= 270 W · erste Figurenrede <= 150 W ·")
    print("  Dialoganteil K1 >= 25 %. Ab ~400 W lohnt ein Blick auf den Einstieg.")
    print("  ⚠️ Der Grusel-Regex trifft auch VERNEINUNGEN ('kein kalter Luftzug').")
    print("     Einen niedrigen Wert immer am Text gegenlesen.")

    print("\n\n### ERSTER UND LETZTER SATZ\n")
    for name, titel, m, _q in reihe:
        print(f"  {name} — {titel}")
        print(f"      erster:  {m['erster_satz']}...")
        print(f"      letzter: {m['letzter_absatz']}")

    print("\n\n### AMAZON-LESEPROBE (erste ~10 %)\n")
    for name, _titel, m, quelle in reihe:
        urteil = "traegt" if m["probe_signale"] >= 5 else "duenn, pruefen"
        print(f"  {name}: {m['probe_w']:>5} W, {m['probe_signale']:>3} Grusel-Signale "
              f"-> {urteil}   [{quelle}]")


if __name__ == "__main__":
    main()
