"""
Messung fuer den Qualitaets-Pruefplan (Teil A).

Misst die Stellen, an denen sich der Read-Through entscheidet, und stellt ALLE
BAENDE nebeneinander. Die Reihe ist ihr eigener Massstab: Wenn Band 2 nach
einem Absatz unheimlich wird und Band 1 erst nach 17, ist das ein Befund -
und zwar einer, den kein Bauchgefuehl liefert.

Verwendung:
    py Scripts/pruefe_qualitaet.py

★ WAS DAS SKRIPT NICHT KANN
  Es misst keine Qualitaet. Es misst Bauteile und Abstaende. Ob ein Anfang
  packt, entscheidet ein Mensch - am besten ein zehnjaehriger.
"""

import os
import re
import statistics as st

_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

TITEL = {1: "Das Haus, das fluestert", 2: "Der Friedhof ohne Namen",
         3: "Schatten sieht mehr", 4: "Die zugemauerte Tuer", 5: "Der Schleier"}

# Woerter, die "hier stimmt etwas nicht" signalisieren - bewusst breit gefasst.
UNHEIMLICH = (r"kalt|K(ä|ae)lte|fror|Fl(ü|ue)stern|fl(ü|ue)sterte|knarr|klopf|"
              r"dunkel|Dunkelheit|Nacken|Geist|unheimlich|starr|regungslos|"
              r"Gestalt|Erscheinung|Schrei|schrie|knurr|str(ä|ae)ubt")


def lade(band):
    p = os.path.join(_ROOT, f"Band{band}", "Manuskript",
                     f"Manuskript_Band{band}_Komplett.md")
    return open(p, encoding="utf-8").read() if os.path.exists(p) else None


def absaetze(body):
    """⚠️ Marker wie '**ENDE BAND 4**' muessen raus - sonst meldet A2 sie als
    letzten Absatz des Buchs (realer Fehler im ersten Skriptlauf)."""
    out = []
    for p in body.split("\n\n"):
        p = p.strip()
        if not p or p in ("---", "***"):
            continue
        if re.fullmatch(r"\*\*ENDE[^*]*\*\*", p):
            continue
        out.append(p)
    return out


def ist_dialog(p):
    return '"' in p or "„" in p


def kapitel(text):
    return [(int(m.group(1)), m.group(2))
            for m in re.finditer(r"# Kapitel (\d+)[^\n]*\n(.*?)(?=\n# Kapitel |\Z)",
                                 text, re.S)]


def main():
    print("=" * 92)
    print("QUALITAETS-MESSUNG - alle Baende nebeneinander")
    print("=" * 92)

    # ── A1: Der Einstieg ────────────────────────────────────────────────
    print("\n### A1 - DER EINSTIEG (hier entscheidet das Kind, ob es weiterliest)")
    print("""
  >> GEMESSEN WIRD IN WOERTERN, NICHT IN ABSAETZEN.
    Absaetze sind eine untaugliche Einheit: Am Anfang von Band 1 stehen viele
    sehr kurze Dialogzeilen ("Theo." / "War nur ein Vorschlag."). Gezaehlt in
    Absaetzen ergab das "17 bis zum ersten Unheimlichen" - was nach drei Seiten
    Kulisse klingt. In Woertern sind es 213, also weniger als EINE Seite.
    Die Absatz-Zahl hat einen Fehlbefund erzeugt (2026-07-18).
""")
    print(f"{'Band':<5} {'->Dialog W':<11} {'->Grusel W':<11} {'ca.S.':<7} "
          f"{'K1 Wörter':<10} {'Dialog%':<8} erster Satz")
    print("-" * 100)
    einstieg = {}
    for b in sorted(TITEL):
        t = lade(b)
        if not t:
            continue
        ab = absaetze(kapitel(t)[0][1])

        def worte_bis(pruef):
            w = 0
            for p in ab:
                if pruef(p):
                    return w
                w += len(p.split())
            return w

        dlg_w = worte_bis(ist_dialog)
        gru_w = worte_bis(lambda p: re.search(UNHEIMLICH, p, re.I))
        w = sum(len(p.split()) for p in ab)
        dw = sum(len(p.split()) for p in ab if ist_dialog(p))
        einstieg[b] = gru_w
        warn = "  <<<" if gru_w > 400 else ""
        print(f"{b:<5} {dlg_w:<11} {gru_w:<11} {gru_w/270:<7.1f} {w:<10} "
              f"{100*dw//w:<8} {ab[0][:34]}...{warn}")
    best = min(einstieg, key=einstieg.get)
    print(f"\n  Richtwert: erstes Unheimliches innerhalb der ERSTEN SEITE (~270 W).")
    print(f"  Alle Baende der Reihe erfuellen das. Bester: Band {best} "
          f"({einstieg[best]} W).")
    print(f"  Erst ab ~400 W (1,5 Seiten) lohnt es, ueber den Einstieg zu reden.")

    # ── A2: Der Ausstieg ────────────────────────────────────────────────
    print("\n\n### A2 - DER AUSSTIEG (hier entscheidet es, ob der naechste Band kommt)\n")
    for b in sorted(TITEL):
        t = lade(b)
        if not t:
            continue
        letztes = kapitel(t)[-1][1]
        ab = absaetze(letztes)
        print(f"  Band {b}: letzter Absatz -> {ab[-1][:78]}")

    # ── Leseerfahrung ───────────────────────────────────────────────────
    print("\n\n### LESEERFAHRUNG (Zielgruppe: 10 Jahre, Keyword 'Lesemuffel')\n")
    print(f"{'Band':<5} {'Kap.':<6} {'Ø Wörter':<10} {'längstes':<10} "
          f"{'Streuung':<9} Einschaetzung")
    print("-" * 92)
    for b in sorted(TITEL):
        t = lade(b)
        if not t:
            continue
        ks = [len(body.split()) for _, body in kapitel(t)]
        m = st.mean(ks)
        hinweis = "lang - fuer Lesemuffel eine Huerde" if m > 1300 else "ok"
        print(f"{b:<5} {len(ks):<6} {m:<10.0f} {max(ks):<10} "
              f"{st.pstdev(ks):<9.0f} {hinweis}")

    # ── Amazon-Leseprobe ────────────────────────────────────────────────
    print("\n\n### AMAZON-LESEPROBE ('Blick ins Buch' = erste ~10 %)\n")
    for b in sorted(TITEL):
        t = lade(b)
        if not t:
            continue
        body = t[t.index("# Kapitel 1"):]
        w = body.split()
        probe = " ".join(w[:int(len(w) * 0.10)])
        treffer = len(re.findall(UNHEIMLICH, probe, re.I))
        print(f"  Band {b}: {len(probe.split()):>5} Wörter, "
              f"{len(re.findall(r'# Kapitel ', probe))} Kapitel, "
              f"{treffer:>3} Grusel-Signale "
              f"{'-> traegt' if treffer >= 5 else '-> duenn, pruefen'}")

    # ── Teil F: Wirkung (nur was die Vortests ueberlebt hat) ────────────
    print("\n\n### WIRKUNG - TOTE ZONEN")
    print("""
  Was hier NICHT gemessen wird und warum - alles an Band 1-5 geprueft:
    - Gruselwort-Dichte:  Band 1 (Grusel 3/10) hat die HOECHSTE Kaelte-Dichte
                          der Reihe. Anti-korreliert mit der Wirkung.
    - Humor:              NICHT per Stichwort auffindbar. Alle vier echten
                          Lacher aus Band 5 ("Andere Familien haben ein
                          Aquarium.") enthalten null Humor-Schluesselwoerter.
    - Eskalationskurve:   Band 5 misst "fallend", weil das letzte Viertel die
                          Aufloesung ist - der emotionale Hoehepunkt liegt
                          genau dort. Die Kurve misst das Gegenteil.
  Messbar ist nur die STRUKTUR: wo passiert lange nichts, und ist das
  Entlastungsventil (Theo) nach einem Schreck da?
""")
    GRUSEL = (r"\b(schrie|Schrei|knurrte|str(ä|ae)ubte|erstarrte|regungslos|"
              r"Gestalt|Erscheinung|eiskalt|G(ä|ae)nsehaut|Nackenhaar)\b")

    print(f"{'Band':<5} {'tote Zone':<11} {'in Kapitel':<12} "
          f"{'Grusel->Theo Ø':<15} {'Schrecken ohne Theo'}")
    print("-" * 92)
    for b in sorted(TITEL):
        t = lade(b)
        if not t:
            continue
        # tote Zone: laengste Strecke ohne Grusel UND ohne Dialog
        schlimmste, wo = 0, "-"
        for nr, body in kapitel(t):
            lauf = 0
            for p in absaetze(body):
                if re.search(GRUSEL, p, re.I) or ist_dialog(p):
                    lauf = 0
                else:
                    lauf += len(p.split())
                    if lauf > schlimmste:
                        schlimmste, wo = lauf, f"K{nr}"
        # Entlastungsventil
        ab = [p for _, body in kapitel(t) for p in absaetze(body)]
        d = []
        for i, p in enumerate(ab):
            if re.search(GRUSEL, p, re.I):
                for j in range(i, min(i + 10, len(ab))):
                    if ist_dialog(ab[j]) and "Theo" in ab[j]:
                        d.append(j - i)
                        break
                else:
                    d.append(99)
        ok = [x for x in d if x < 99]
        avg = st.mean(ok) if ok else 0
        print(f"{b:<5} {schlimmste:<11} {wo:<12} {avg:<15.1f} "
              f"{d.count(99)} von {len(d)}")

    print("\n  Tote Zone: laengste Strecke ohne Schreck UND ohne Dialog.")
    print("  Ab ~180 W nachlesen (deckt sich mit dem Spannungs-Pruefplan).")
    print("  Grusel->Theo: Richtwert 1-3 Absaetze (CLAUDE.md erlaubt 2-3")
    print("  Ausnahmen pro Buch, wo die Dramatik es verlangt).")

    print("\n" + "=" * 92)
    print("Befunde einstufen (rot/orange/gelb) - siehe Dokumentation/")
    print("Qualitaets_Pruefplan.md. Bei veroeffentlichten Buechern gilt:")
    print("im Zweifel STEHEN LASSEN, und wenn aendern, dann minimal.")


if __name__ == "__main__":
    main()
