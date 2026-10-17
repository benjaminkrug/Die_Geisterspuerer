# Übergabe: am PC weiterarbeiten (Stand 2026-10-17)

## 1. Wo der Stand liegt
**Alles ist in `main`** (zusammengeführt 2026-10-17 aus `ccr-c33fc6fe-peyki0` = deutsches Buch und
`ccr-15523105-z095g4` = englische Ausgabe; nach dem Zusammenführen geprüft: Selbsttest, K1–K16 0 Befunde,
beide eBook-Bauskripte, `pruefe_band1_umbau.py`, `DE_Basis` = deutsches Manuskript). Die beiden Arbeits-Branches
werden nicht mehr gebraucht.

## 2. Am PC holen
```
git fetch origin
git checkout main
git pull
```

## 3. Was am PC installiert sein muss
- Python 3 mit `python-docx` und `Pillow` (`py -m pip install python-docx pillow qrcode`)
- für PDF-Vorschau: LibreOffice (die deutschen Skripte erwarten es unter `C:\Program Files\LibreOffice`)
- optional `pandoc` (Word-Arbeitsfassung)
- Kontrolle: `py Scripts/pruefe_en.py selbsttest` → „SELBSTTEST BESTANDEN"

## 4. Mit Claude Code weitermachen
Claude liest beim Start `CLAUDE.md` (Arbeitsweise, wo was liegt). Guter Einstieg:
> „Lies `Dokumentation/Internationalisierung_Vorgehensplan.md` (Stand), `Band1/Manuskript_EN/README.md` und
> `Band1/Manuskript_EN/Nachanalyse/Nachanalyse_Band1.md`. Nächster Schritt ist A9. Arbeite nach
> `Dokumentation/EN_Bibel/Vorlagen_Pruefdurchgaenge.md`."

Am PC zusätzlich möglich, was hier nicht ging: **QR-Codes erzeugen** (`qrcode` installierbar), Kindle Previewer, KDP-Upload, Cover in Canva.

## 5. Nächste Schritte
1. **A9** US-Lesbarkeitswerte → Abnahme Band 1 EN.
2. **A10** Titelprüfung + US-Marktanalyse → **Cover-Briefing** → Cover (Autor).
3. Taschenbuch EN, KDP-Texte (US, neu geschrieben), KI-Angabe im Dashboard; nach Veröffentlichung ASIN in `BOOK1_ASIN_EN` eintragen, neu bauen, Datei ersetzen.
4. Deutsch (Autor): eBook Band 1 neu hochladen (Korrekturen + festes Inhaltsverzeichnis), Band 2 neu hochladen (Zeitangaben), QR-Code Taschenbuch Band 1, Inhaltsverzeichnis Band 2–5 in der KDP-Vorschau prüfen.
