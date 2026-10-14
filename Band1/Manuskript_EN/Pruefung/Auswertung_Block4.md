# Auswertung Block 4 (Kapitel 13–16) — 2026-10-14

## Ergebnis

| Kap. | Runden | US-Lektor „übersetzt?" (letzte Runde) | Bedeutung FEHLER | Skript | Status |
|---|---|---|---|---|---|
| 13 | 3 | **nein**, knapp (R1: ja, leicht) | 0 | 0 | ✅ fertig |
| 14 | 2 | **nein** (sauberstes Kapitel) | 0 | 0 | ✅ fertig |
| 15 | 3 | **nein**, knapp | 0 | 0 | ✅ fertig |
| 16 | 3 | **nein** | 0 | 0 | ✅ fertig |

Kinderleser (**ganzes Buch K1–K16 am Stück**): Ende befriedigend, will Band 2 („der wütende Friedhofsgeist, das nasse Kreuz, *I am no longer here*, GRAVEN, ein Hund, der mindestens 40 Jahre alt ist"). Grusel-Kurve 3 · 5 · 6 · 4 · 6 · 3 · 4 · 6 · 6 · **8** · 6 · 6 · 3 · 5 · 6 · 6 — nichts zu gruselig. Beste Momente: Fußspuren hinter Nora (K10), THANK YOU am Fenster (K12), nasses Kreuz (K14). Silbers Brief funktioniert vorgelesen.
Umfang Block 4: 5.283 → 5.638 Wörter (+7 %). **Ganzes Buch: 22.867 Wörter Deutsch → 24.162 Englisch (+6 %).** Skript K1–K16: 0 Befunde. Einheitlichkeit: 6 Stellen, alle geprüft und gewollt bzw. alt.

## Buchende
DE: *Es fühlte sich an, als läge auf der anderen Seite gerade eine zweite Hand. / Genau auf derselben Stelle.*
EN: *Right then it felt as if another hand were lying flat against the other side. / In exactly the same spot.*
Weg dorthin: Erstfassung *a second hand lay …* — drei Prüfer unabhängig: klingt nach Sekundenzeiger (die Kirchturmuhr schlägt im selben Kapitel). R2 *there was another hand* verlor die Berührung (D4) und hatte eine Kommakette (D5). R3 erfüllt beides; Gegenprobe R3: OK.

## Was Block 4 verändert hat

| Änderung | Auslöser |
|---|---|
| **Deutsch:** K15 *den Schraubenzieher* statt nicht eingeführtem *Brieföffner* (8820bb3) — eBook neu gebaut | drei Prüfer; Kinderleser „unfreiwillig komisch"; Autor |
| **Nasses Kreuz bleibt offen** (Band-2-Haken) | Autor; Kinderleser zählt es zu den besten Momenten |
| Theos Satzzeichen-Witz neu gebaut: *Angry. Grave. The end.* (statt *period*) | D5 + D6: *period* kichert, *grave* doppeldeutig |
| Brief in verschachtelten Anführungszeichen wie Silbers Notizbuch in K11 | D6: Briefzeile klang wie Nora |
| Übersetzer bekam vorab die typischen Lehnübersetzungen aus Block 1–3 | Lehre Block 3 — Erstfassung: US-Lektor K14–K16 „nein" schon in Runde 1 |

## Kritisch
- **Der Vorab-Hinweis auf typische Lehnübersetzungen hat gewirkt:** In Block 1–3 sagte der US-Lektor in Runde 1 meist „ja, übersetzt"; in Block 4 nur bei K13.
- **Die unabhängige Gegenprobe fand wieder etwas**, das alle anderen übersahen (*there was another hand* ohne Berührung).
- **Bewusst nicht geändert:** K15 *long stripes of shade* (R3-Gegenprobe: leichte SCHWÄCHE, *Schatten* wäre genauer). Wörtlich hieße es *long shadows* direkt vor *Shadow trotted* — genau die Vorlese-Verwechslung, die wir seit Block 1 vermeiden. Die Ruhe vor dem Schreck (A7) bleibt laut Gegenprobe erhalten. Keine vierte Runde.
- **Ein Prüferbefund war falsch:** D5 hielt *Third floor* (K13) für einen Zählfehler — deutsch *zweiter Stock* = US *third floor*, richtig.
- **Alle Urteile sind KI-Urteile.** US-Testleser stehen aus.

## Nächste Schritte (Gesamtdurchgang, Plan Phase D)
1. Echte US-Testleser (E2-Anschreiben) — jetzt mit dem ganzen Buch möglich.
2. Rahmen: Titelei, Impressum (mit KI-Hinweis), Anhang (deutsche Leseprobe ist aus Band 2 — offene Entscheidung).
3. D8 Nachanalyse; EN-Bausatz für KDP (eBook/Taschenbuch).

## Nachprüfung (Autor-Auftrag „letzte 2 Schritte sehr genau", 2026-10-14)

**Echte Funde → behoben**
- **Inhaltsverzeichnis im eBook (EN und DE):** war ein Word-Feld, das bis zur Aktualisierung nur einen Platzhalter enthält („Table of contents (updates when opened)" / „Inhaltsverzeichnis wird beim Öffnen aktualisiert."). Ob KDP Felder aktualisiert, ist nicht gesichert → festes Inhaltsverzeichnis mit internen Links auf Textmarken; 16/16 Links per Umwandlung geprüft; das Bauskript bricht ab, wenn einer fehlt. Deutsch: Commit 7373e43 (Band-1-Branch).
- **Metadaten:** Autor stand als „python-docx", kein Titel; deutsches eBook hatte Sprache en-US → Titel, Autor, Sprache gesetzt.
- **Lücke im Ablauf:** K14/K15 wurden nach Runde 2/3 nicht mehr vom US-Lektor gelesen → Endkontrolle: 14 Funde, 11 umgesetzt (u. a. *couldn't go* → *couldn't leave* — Klo-Kicher-Gefahr; *Ghost release* im Lebenslauf → *Freeing ghosts*; *long stripes of shade* → *Long bands of shade … in the low evening sun*), 3 begründet abgelehnt (Schule, *Veil*, Schraubenzieher). Gegenprobe: 0 FEHLER, 2 SCHWÄCHE — eine davon **mein Vorgabefehler** (*until earlier today* für *Bis vorhin*) → behoben; die andere (*Closed with red sealing wax*) bleibt wegen des A7-Echos.

**Geprüft, in Ordnung:** Gesamtfassung = Kapiteldateien; Satzbild (keine geraden Anführungszeichen, `--`, `...`, Doppel-Leerzeichen); Skript K1–K16 0 Befunde; Einheitlichkeit 6 Stellen (bekannt); Leseprobe und Buchende selbst gelesen.
