# Übersetzungs-Bibel — englische Ausgabe

Arbeitsgrundlage für die Übersetzung der Geisterspürer ins Englische (US).
Plan: `Dokumentation/Internationalisierung_Vorgehensplan.md`, Phase A.

## Stand Phase A

| # | Teil | Datei | Stand |
|---|---|---|---|
| A0 | **Prüfung Phase A** (Fehler, Hinterfragung, neue Reihenfolge) | [A0_Pruefung_Phase_A.md](A0_Pruefung_Phase_A.md) | ✅ 2026-10-12 · 6 Fehler korrigiert |
| A1 | Glossar (inkl. vorgezogener Titelprüfung aus A10) | [A1_Glossar.md](A1_Glossar.md) | ✅ **entschieden** (E1–E12 übernommen 2026-10-12) |
| A2 | Stimmen der Figuren | – | ⏳ offen |
| A3 | Witz-Liste (B1–B5, jeder Band ganz gelesen) | [A3_Witz_Liste.md](A3_Witz_Liste.md) | ✅ ≈ 280 Witze · 36 Umbauten · 2 Neuerfindungen · 13 Running Gags über Bände · Nebenfunde im Original |
| A4 | Motiv-Liste | – | ⏳ offen |
| A5 | Satz-Register | [A5_Satz_Register.md](A5_Satz_Register.md) | ✅ 43 Einträge · Englisch vorläufig bis Pilot |
| A6 | Fallen-Liste | [A6_Fallen_Liste.md](A6_Fallen_Liste.md) | ✅ vollständig B1–B5 (30 Fallen) |
| A7 | Szenen-Absicht je Kapitel | – | ⏳ offen · wird aus Story_Outline / Cliffhanger-Register gezogen · Autor prüft Band 1 |
| A8 | Stil-Brief EN | – | ⏳ offen |
| A9 | US-Zielwerte (Vergleichstitel) | – | ⏳ offen |
| A10 | US-Marktanalyse | – | ⏳ offen · Titelprüfung schon in A1, Gegenprobe (Amazon.com, USPTO) vor dem Cover |
| A11 | Prüfskripte | `Scripts/en_bibel_extrakt.py` | 🟡 Extraktion fertig (mit Selbsttest) · EN-Prüfungen + D8-Vergleich offen |

**Reihenfolge ab jetzt** (A0, Abschn. 5): A2 + A4 → A8 → A11 → Pilot → A7/A9 → A10.

## Weitere Unterlagen

| Datei | Wofür |
|---|---|
| [E2_Anschreiben_Testleser.md](E2_Anschreiben_Testleser.md) | Anschreiben für Lesegruppen (Autor kennt keine EN-Testleser persönlich) |

## Grundlage

- **Band 1: umgebaute Fassung** (16 Kapitel, Branch `ccr-c33fc6fe-peyki0`). Die alte Fassung wird
  nicht übersetzt.
- Band 2–5: veröffentlichte Fassung.
- Rohdaten neu erzeugen:
  ```
  python3 Scripts/en_bibel_extrakt.py selbsttest
  python3 Scripts/en_bibel_extrakt.py register --band1 <Pfad zur umgebauten Fassung>
  python3 Scripts/en_bibel_extrakt.py fallen   --band1 <Pfad zur umgebauten Fassung>
  ```

## Regeln

1. Glossar und Register werden **einmal** festgelegt. Änderungen nur mit Eintrag im
   Änderungsprotokoll von A1.
2. Was das Original wiederholt, wiederholt die Übersetzung — nicht glätten.
3. Neue Funde (aus Übersetzung, Prüfung, Lesern) kommen hierher zurück (Lernschleife E4).
4. Jede Regel, die den **deutschen** Text berührt, wird gegen die Build-Skripte geprüft (Lehre aus A0, P1).
