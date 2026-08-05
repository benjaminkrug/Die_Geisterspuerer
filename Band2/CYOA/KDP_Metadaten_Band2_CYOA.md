# KDP-Metadaten — Band 2 CYOA „Der Friedhof ohne Namen"

Zentrale Sammelstelle für alle Nummern/Metadaten rund um die Veröffentlichung.

---

## Identifikatoren

| Feld | Wert | Verwendung |
|------|------|-----------|
| **ISBN-13 (KDP)** | `9798185116203` | Barcode auf der Cover-**Rückseite**; optional Impressum-Seite |
| **ASIN** | `B0H75HWHFQ` ✅ (eingetragen 2026-07-01) | **QR-Code zur Amazon-Bewertung** (im Buch, Rezensions-Seite) — aktiv im Build |

### ⏳ Offener Punkt: ASIN besorgen
- Die ASIN steht in der **KDP-Bücherliste** beim Titel bzw. in der Amazon-Produktseiten-URL: `…/dp/BXXXXXXXXX`.
- **Nicht mit der ISBN verwechseln** — der Bewertungslink `amazon.de/review/create-review?asin=…` funktioniert nur mit der ASIN.
- Sobald vorhanden: in `Scripts/build_cyoa_taschenbuch_band2.py` die Zeile `AMAZON_ASIN = ""` mit der ASIN füllen und den Build neu laufen lassen → dann erscheint der echte QR-Code (statt des aktuellen Text-Fallbacks).

---

## Produktseiten-Daten (Quelle: Dokumentation/KDP_Beschreibungen.md)

| Feld | Wert |
|------|------|
| **Titel** | Der Friedhof ohne Namen |
| **Untertitel** | Grusel-Spielbuch mit 12 Enden für Kinder ab 10 Jahren – du entscheidest |
| **Serie** | Die Geisterspürer Spielbuch · Band 2 |
| **Autor** | Benjamin Krug |
| **Preis TB (Vorschlag)** | 16,99 EUR |
| **Beschreibung + 7 Keywords + Kategorien** | siehe `Dokumentation/KDP_Beschreibungen.md` (Abschnitt „Band 2 CYOA") |

---

## Cover — Status

| Teil | Status |
|------|--------|
| Vorderseite | ✅ Prompt final (`Band2/Cover/Prompts/Cover_Prompt_Band2_Vorderseite_FINAL.md`), Bild generiert |
| Rückseite | ⏳ offen — braucht Klappentext + **Barcode-Zone für ISBN 9798185116203** |
| Buchrücken | ⏳ offen — Breite hängt von finaler Seitenzahl ab (kommt nach KDP-Upload des Innenteils) |
