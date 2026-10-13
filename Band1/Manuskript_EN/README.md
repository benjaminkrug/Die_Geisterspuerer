# Band 1 · englische Ausgabe *The Whispering Window* — Arbeitsstand

> Grundlage: `DE_Basis/` (eingefroren, Commit 6f251d2). Verfahren: `Dokumentation/Internationalisierung_Vorgehensplan.md`
> Phase D, Regeln aus `Dokumentation/EN_Bibel/Pilot/Pilot_Auswertung.md` Abschn. 5 und 8.
> Arbeitsanweisung: `Dokumentation/EN_Bibel/A8_Stil_Brief.md`.

## Ablauf je Block (4 Kapitel, in Buchreihenfolge)

1. **D2** ein Übersetzer übersetzt den Block nacheinander; liest vorher die englischen Kapitel davor.
2. **D3** Mehrdeutigkeits-Leser · **D4** Bedeutung · **D5** US-Lektor · **D6** Kinderleser — je Kapitel getrennt.
3. **D2** überarbeitet nach Vorrangregel (Pilot 5.1); **D4-Gegenprobe** auf alle späten Änderungen (5.2a).
4. **D7** `python3 Scripts/pruefe_en.py pruefen DE_Basis/Kapitel_XX.md Kapitel_XX.md` → 0 Befunde.
5. **Fertig**, wenn: US-Lektor „klingt nicht übersetzt", TRANSLATED ≤ 7 (Startwert), D4 0 FEHLER, Skript 0 (Pilot 5.2).

## Stand

| Kap. | D2 | D3 | D4 | D5 | D6 | Überarb. | Gegenprobe | Skript | fertig |
|---|---|---|---|---|---|---|---|---|---|
| 1 | Pilot + Nachzug ✅ | Pilot | Pilot | Pilot | ✅ | – | ✅ 5/5 OK | 0 | ✅ |
| 2 | ✅ | ✅ | ✅ | ✅ R1–R3 | ✅ | R2, R3 | ✅ | 0 | ✅ (Meldung: R3 „ja, knapp“) |
| 3 | ✅ | ✅ | ✅ | ✅ R1–R2 | ✅ | R2 | ✅ | 0 | ✅ |
| 4 | ✅ | ✅ | ✅ | ✅ R1–R2 | ✅ | R2 | ✅ | 0 | ✅ |
| 5–8 | Block 2 | | | | | | | | |
| 9 | Pilot + Nachzug | | | | | | | | |
| 10–12 | Block 3 | | | | | | | | |
| 13–16 | Block 4 | | | | | | | | |

**Block 1 fertig (2026-10-13)** — Auswertung: `Pruefung/Auswertung_Block1.md`.
Nach Block 1: Leseprobe an US-Lesegruppen (`Dokumentation/EN_Bibel/E2_Anschreiben_Testleser.md`).
Am Ende: Gesamtdurchgang (Stimmen, Running Gags), Kinderleser am Stück, D8 Nachanalyse, Rahmen (Titelei, Impressum mit KI-Hinweis, Anhang).

**Offene Entscheidung für den Anhang:** Die deutsche Leseprobe stammt aus Band 2 — auf Englisch gibt es Band 2 noch nicht.
