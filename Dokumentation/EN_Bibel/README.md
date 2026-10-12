# Übersetzungs-Bibel — englische Ausgabe

Arbeitsgrundlage für die Übersetzung der Geisterspürer ins Englische (US).
Plan: `Dokumentation/Internationalisierung_Vorgehensplan.md`, Phase A.

## Stand Phase A

| # | Teil | Datei | Stand |
|---|---|---|---|
| A1 | Glossar (inkl. vorgezogener Titelprüfung aus A10) | [A1_Glossar.md](A1_Glossar.md) | ✅ Entwurf · **12 Entscheidungen des Autors offen** (Abschn. 1) |
| A2 | Stimmen der Figuren | – | ⏳ offen |
| A3 | Witz-Liste (B1–B5, liest jeden Band ganz) | – | ⏳ offen · ergänzt die Sprachwitze in A6 für B2–B5 |
| A4 | Motiv-Liste | – | ⏳ offen |
| A5 | Satz-Register | [A5_Satz_Register.md](A5_Satz_Register.md) | ✅ 42 Einträge · Englisch vorläufig bis Pilot |
| A6 | Fallen-Liste | [A6_Fallen_Liste.md](A6_Fallen_Liste.md) | ✅ messbare Fallen B1–B5 · Sprachwitze B1 vollständig, B2–B5 mit A3 |
| A7 | Szenen-Absicht je Kapitel | – | ⏳ offen · Autor prüft |
| A8 | Stil-Brief EN | – | ⏳ offen |
| A9 | US-Zielwerte (Vergleichstitel) | – | ⏳ offen |
| A10 | US-Marktanalyse | – | ⏳ offen · Titelprüfung schon in A1 |
| A11 | Prüfskripte | `Scripts/en_bibel_extrakt.py` | 🟡 Extraktion fertig (mit Selbsttest) · EN-Prüfungen + D8-Vergleich offen |

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
