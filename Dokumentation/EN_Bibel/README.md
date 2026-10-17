# Übersetzungs-Bibel — englische Ausgabe

Arbeitsgrundlage für die Übersetzung der Geisterspürer ins Englische (US).
Plan: `Dokumentation/Internationalisierung_Vorgehensplan.md`, Phase A.

## Stand Phase A

| # | Teil | Datei | Stand |
|---|---|---|---|
| A0 | **Prüfung Phase A** (Fehler, Hinterfragung, neue Reihenfolge) | [A0_Pruefung_Phase_A.md](A0_Pruefung_Phase_A.md) | ✅ 2026-10-12 · 6 Fehler korrigiert |
| A1 | Glossar (inkl. vorgezogener Titelprüfung aus A10) | [A1_Glossar.md](A1_Glossar.md) | ✅ **entschieden** (E1–E12 übernommen 2026-10-12) |
| A2 | Stimmen der Figuren | [A2_Stimmen.md](A2_Stimmen.md) | ✅ 13 Figuren, gemessen + nachgelesen · 3 Fälle „Pilot entscheidet" |
| A3 | Witz-Liste (B1–B5, jeder Band ganz gelesen) | [A3_Witz_Liste.md](A3_Witz_Liste.md) | ✅ ≈ 280 Witze · 36 Umbauten · 2 Neuerfindungen · 13 Running Gags über Bände · Nebenfunde im Original |
| A4 | Motiv-Liste | [A4_Motive.md](A4_Motive.md) | ✅ 12 Motive mit festem Wortlaut · Schattens Code · neue Falle *Knock, knock* |
| A5 | Satz-Register | [A5_Satz_Register.md](A5_Satz_Register.md) | ✅ 45 Einträge · Englisch vorläufig bis Pilot |
| A6 | Fallen-Liste | [A6_Fallen_Liste.md](A6_Fallen_Liste.md) | ✅ vollständig B1–B5 (31 Fallen) |
| A7 | Szenen-Absicht je Kapitel | [A7_Szenen_Absicht_Band1.md](A7_Szenen_Absicht_Band1.md) | ✅ Band 1 alle 16 Kapitel · mit Setups/Rückgriffen · 285 Zitate maschinell geprüft · **Autor prüft** |
| A8 | Stil-Brief EN | [A8_Stil_Brief.md](A8_Stil_Brief.md) | ✅ Fassung 0 · wird im Pilot geschärft |
| A9 | US-Zielwerte (Vergleichstitel) | – | **gestrichen** (Autor, 2026-10-17) · Lesbarkeit = Gleichwertigkeit mit dem Deutschen (D8.1) · Plan 9.7 |
| A10 | US-Marktanalyse | – | ⏳ offen · Titelprüfung schon in A1, Gegenprobe (Amazon.com, USPTO) vor dem Cover |
| A11 | Prüfskripte | `Scripts/en_bibel_extrakt.py` · `Scripts/pruefe_en.py` | ✅ Extraktion (register, fallen, stimmen, motive) · EN-Prüfung (Absätze, Ein-Satz-Absätze, Ausrufe, Flüche, britisch, Glossar, Motive, Dialogverben, Deutsch-Reste, Stockwerke, Temperaturen, Register) · D8.1-Bericht · beide mit Selbsttest |

**Reihenfolge ab jetzt** (A0, Abschn. 5): ~~A2 + A4 → A8 → A11 → Pilot~~ ✅ → A7 ✅ → ~~A9~~ (gestrichen) → A10.

**Pilot (Phase C) gelaufen:** [Pilot/Pilot_Auswertung.md](Pilot/Pilot_Auswertung.md) — K1 und K9, drei Runden,
alle Berichte in `Pilot/`.

## Weitere Unterlagen

| Datei | Wofür |
|---|---|
| [Band1_Fundliste_DE.md](Band1_Fundliste_DE.md) | **Fehler im deutschen Band 1** (39 Funde, nach Gewicht) — vor dem Einfrieren entscheiden |
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
  python3 Scripts/en_bibel_extrakt.py stimmen  --band1 <Pfad zur umgebauten Fassung>
  python3 Scripts/en_bibel_extrakt.py motive   --band1 <Pfad zur umgebauten Fassung>
  python3 Scripts/en_bibel_extrakt.py zitate <Bibel-Datei> --band1 <Pfad>   # stimmt jedes Zitat wörtlich?
  ```

## Regeln

1. Glossar und Register werden **einmal** festgelegt. Änderungen nur mit Eintrag im
   Änderungsprotokoll von A1.
2. Was das Original wiederholt, wiederholt die Übersetzung — nicht glätten.
3. Neue Funde (aus Übersetzung, Prüfung, Lesern) kommen hierher zurück (Lernschleife E4).
4. Jede Regel, die den **deutschen** Text berührt, wird gegen die Build-Skripte geprüft (Lehre aus A0, P1).
