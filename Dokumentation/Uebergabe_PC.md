# Übergabe: am PC weiterarbeiten (Stand 2026-10-17)

## 1. Wo der Stand liegt
Alles ist gepusht, aber auf **zwei Branches**, noch nicht in `main`:

| Branch | Inhalt |
|---|---|
| `ccr-15523105-z095g4` | Englische Ausgabe: Bibel, Skripte (`pruefe_en.py`, `build_ebook_en_band1.py`), Band 1 EN komplett, Prüfberichte, Nachanalyse D8, Rahmen, diese Übergabe |
| `ccr-c33fc6fe-peyki0` | Deutsches Buch: alle Korrekturen an Band 1 (Fundliste) und Band 2 Kap. 1, Bauskripte DE (festes Inhaltsverzeichnis, Output-Ordner) |

Beide gehen ohne Konflikt zusammen (getestet: zusammengeführt, alle Prüfungen und beide Bauskripte laufen, `DE_Basis` = deutsches Manuskript).
**Empfehlung:** beide in `main` zusammenführen (zwei Pull Requests), dann am PC nur noch `main`.

## 2. Am PC holen
```
git fetch origin
git checkout main && git pull            # falls zusammengeführt
# sonst:
git checkout ccr-15523105-z095g4         # Englisch
git checkout ccr-c33fc6fe-peyki0         # Deutsch (eigener Ordner: git worktree add ../GS_DE ccr-c33fc6fe-peyki0)
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
