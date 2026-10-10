# Umbau-Protokoll Band 1

> Gehört zu `Band1/PLAN_Durchlesequote.md`, Abschnitt 7.
> Für jeden Schritt: Datum, Basis, Ergebnis der Kontrollen, Entscheidung.
> **Was hier nicht steht, gilt als nicht geprüft.**

---

## Schritt 0 – Vorbereitung · 2026-10-10

### 0.1 Basis (der eingefrorene Maßstab)

| | Wert |
|---|---|
| Basis-Commit des Manuskripts | **`4e983cf`** (2026-08-05, „stafel 1 fertig“). Letzter Commit, der `Manuskript_Band1_Komplett.md` geändert hat. |
| Git-Blob der Datei | `88ab33c49d90fe4a53e84fb1a490f8dd57826031` |
| Warum ein Commit statt eines Tags | Ein Tag lebt nur im lokalen Klon und ginge mit dem Container verloren. Ein Commit-Hash auf dem Branch ist dauerhaft. |
| Aufruf für alle späteren Vergleiche | `py Scripts/pruefe_band1_umbau.py --basis 4e983cf` |

### 0.2 Komplett-Datei gegen Kapitel-Dateien

18 von 18 Kapitel-Dateien sind **inhaltlich identisch** mit der Komplett-Datei (Leerzeichen und
Trenner normalisiert). Die Kapitel-Dateien dürfen also am Ende (Schritt 7) aus der Komplett-Datei
neu erzeugt werden, ohne dass etwas verloren geht.

### 0.3 Ausgangswerte

| Messung | Wert | Rohdaten |
|---|---|---|
| `pruefe_band1_umbau.py --basis 4e983cf` | **alle harten Prüfungen bestanden** (K1–K8, K10) | `S0_pruefe_band1_umbau.txt` |
| Wörter gesamt (Prüfskript) | **27.179** | ebd. |
| `pruefe_logik.py 1` | **18 Kandidaten** (hohe Trefferquote): 1 Kapiteltitel doppelt in der Serie, 6 Zeitangaben, 6 Zahlen, 3 Sprechverben, 2 wörtlich wiederholte Sätze | `S0_pruefe_logik.txt` |
| `pruefe_qualitaet.py` | Einstieg: erstes Unheimliches nach 213 W; letzter Absatz: „Ihre Hände zitterten nicht.“ | `S0_pruefe_qualitaet.txt` |
| Stimme (K10): „Und“-Anfänge im Erzähltext | **2,26 / 1.000 W** (harter Korridor ±15 %) | Prüfskript |
| Stimme (K10): Kurzabsätze ≤ 4 W | **7,75 %** (harter Korridor ±15 %) | Prüfskript |
| Stimme: Ø Wörter je Erzählsatz | 4,81 | Prüfskript (Hinweis) |
| Stimme: Ø Wörter je Absatz | 14,83 | Prüfskript (Hinweis) |
| Sätze über 18 Wörter (Erzähltext) | 11 | Prüfskript |
| Anführungszeichen | 1.078 öffnend `„` / 1.078 schließend (ASCII `"`), also halb umgestellt (Fehler 3, wird in Schritt 1 behoben) | Prüfskript |

**Wörter je Kapitel (Basis):**

| Kap. | Titel | Wörter |
|---|---|---|
| 1 | Neue Stadt, altes Haus | 1.538 |
| 2 | Schatten | 1.488 |
| 3 | Drei Mal Klopfen | 1.446 |
| 4 | Kondenswasser | 1.487 |
| 5 | Frau Silbers Wohnung | 1.635 |
| 6 | Die Namensliste | 1.682 |
| 7 | Lina | 1.579 |
| 8 | Hinter der Tapete | 1.440 |
| 9 | Das Tagebuch | 1.534 |
| 10 | Der Keller | 1.320 |
| 11 | Zeichen an der Wand | 1.487 |
| 12 | Konfrontation | 1.441 |
| 13 | Die Befreiung | 1.651 |
| 14 | Frau Silbers Karte | 1.494 |
| 15 | Die Karte lesen | 1.328 |
| 16 | Entscheidung | 1.484 |
| 17 | Frau Silbers Brief | 1.605 |
| 18 | Nachtschatten | 1.535 |

### 0.4 Seitenzahl, gemessen statt angenommen

| Quelle | Seiten | Einordnung |
|---|---|---|
| KDP (live, laut `Scripts/build_cover.py`, „bestaetigt=True“) | **186** | **maßgeblich** |
| `TODO_Nachbesserung_Band1-4.md` | 187 | weicht um 1 ab. Vermutlich der Stand vor dem QR-Nachtrag oder anders gezählt. **Im KDP-Bücherregal ablesen.** |
| Eigener Bau: `build_taschenbuch_docx.py` → LibreOffice-PDF | 211 | **Absolut unbrauchbar:** Die Schrift Georgia fehlt in dieser Umgebung, Ersatz ist DejaVu Serif (breiter). Brauchbar nur **relativ**: alte und neue Fassung mit derselben Ersatzschrift messen und das Verhältnis vergleichen. |

**Mess-Regel für alle Schritte:** Seiten-Änderung = (LibreOffice-Seiten neu ÷ 211) − 1. Gilt nur
bei unveränderten Satzeinstellungen (Schriftgröße, Ränder, Zeilenabstand).

### 0.5 KDP-Regel zu Inhaltsänderungen: **Stopp-Regel ausgelöst, Entscheidung nötig**

**Ergebnis der Recherche** (2026-10-10; die KDP-Seiten selbst waren aus dieser Umgebung nicht
erreichbar. Der Wortlaut stammt aus den Suchergebnissen zu den offiziellen Hilfeseiten und **muss im
KDP-Konto gegengelesen werden**):

- KDP-Hilfe „Update Your Book“: *„For small changes, you can upload a revised manuscript. For
  significant changes, such as new chapters, publish a new edition.“*
- KDP-Hilfe „Editions“: Als wesentlich gilt eine Änderung, bei der sich **die Seitenzahl um mehr
  als 10 % ändert**. Tippfehler und Groß-/Kleinschreibung brauchen keine neue Ausgabe.
- KDP-Hilfe „Update Your Manuscript“: Wer das Manuskript wesentlich ändert, hat eine neue Ausgabe,
  und die soll als **neues Buch** veröffentlicht werden. Folge: neue ASIN, **Rezensionen und Ranking
  fangen bei null an.**

**Was das für den Plan heißt (gerechnet):**

| | Wörter | Seiten (≈ 154 W/S im Fließtext) | Änderung |
|---|---|---|---|
| Heute | 27.179 | 186 | – |
| Plan-Ziel ~22.000 | −5.200 | ≈ −34 | **≈ −18 %** 🔴 über 10 % |
| Grenze 10 % | ≈ −2.850 | ≈ −18,6 | genau an der Grenze |
| Mit Sicherheitsabstand (8 %) | ≈ −2.300 → **≈ 24.900 W** | ≈ −15 | 🟢 |

Dazu kommt: Der Plan streicht zwei Kapitel (18 → 16). KDP nennt als Beispiel „neue Kapitel“. Ob
*weniger* Kapitel genauso zählen, sagt der Wortlaut nicht.

**→ Laut Plan (Schritt 0, Stopp-Regel) geht es hier nicht weiter, bevor der Autor entscheidet.**
Die Optionen stehen im Plan, Abschnitt 7.6.

### 0.6 Testleser Runde 1

Bogen liegt bereit: `Band1/Umbau/Testleser_Bogen.md`. **Offen: 5 bis 8 Kinder finden (Autor).**

| Kind | Alter | Ausstieg nach Kap. | Ø Wert K1–10 | Ø Wert K11–13 | Ø Wert K14–18 | Frage 1 („Keller“) |
|---|---|---|---|---|---|---|
| | | | | | | |

### 0.7 Stand Schritt 0

| Aufgabe | Status |
|---|---|
| Basis festhalten | ✅ |
| Komplett ↔ Kapitel-Dateien | ✅ identisch |
| Ausgangswerte aller Prüfskripte | ✅ |
| Prüfskript um Stimmen-Messung (K10) erweitert und gegengeprüft (eingeschleuster Drift +128 % wird gemeldet) | ✅ |
| Seitenzahl gemessen, Mess-Regel festgelegt | ✅ (186 im KDP-Konto bestätigen) |
| KDP-Regel geklärt | ⚠️ **Stopp-Regel ausgelöst**, Entscheidung des Autors nötig (Plan 7.6) |
| Testleser Runde 1 | ⏳ Bogen fertig, Kinder fehlen |
