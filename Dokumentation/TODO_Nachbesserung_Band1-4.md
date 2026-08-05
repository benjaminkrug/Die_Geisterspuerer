# TODO — Nachbesserung Band 1–4 → ✅ AUSGEFÜHRT 2026-07-18

> ## ✅ ERLEDIGT — beide Fehler in allen vier Bänden behoben
>
> | Band | Fehl-Ornamente | Leseprobe | Seiten neu |
> |---|---|---|---|
> | 1 | 17 → **0** | 32 erfundene → **20 echte** aus Band 2 | 187 |
> | 2 | 14 → **0** | 24 erfundene → **16 echte** aus Band 3 | 114 |
> | 3 | 15 → **0** | 16 erfundene → **18 echte** aus Band 4 | 106 |
> | 4 | 15 → **0** | 12 erfundene → **20 echte** aus Band 5 | 95 |
>
> Verifiziert **am fertigen DOCX**, nicht am Skript. Echte Szenentrenner unverändert
> erhalten (45/49/105/80). Zusätzlich korrigiert: „Erscheint 2026 auf Amazon" →
> **„Jetzt überall erhältlich"** (alle Bände sind erschienen).
>
> ### ★★ WICHTIGSTER FUND: Band 2s Kapitel-Dateien sind VERALTET
> Vor dem Bauen geprüft, ob die Komplett-Manuskripte mit ihren Kapitel-Dateien
> übereinstimmen. **Band 1, 3, 4: identisch. Band 2: 13 von 15 Kapiteln weichen ab.**
> Am gedruckten Buch verifiziert: **das gedruckte Band 2 stimmt mit dem KOMPLETT-Manuskript
> überein**, nicht mit den Kapitel-Dateien. Das Komplett wurde nach der Generierung
> redaktionell nachbearbeitet (Beispiel Kap. 2: Satz „Er schwitzte immer noch." entfernt,
> Szenentrenner eingefügt); die Kapitel-Dateien sind seitdem stale.
>
> **→ Konsequenz für die Umsetzung:** Der Separator-Bug wurde **NICHT** an der Wurzel
> (Kompilier-Skripte + Neugenerierung der Komplett-Dateien) gefixt, sondern **in den
> Renderern** — sonst hätte die Neugenerierung von Band 2 **veröffentlichte redaktionelle
> Änderungen stillschweigend zurückgedreht.**
> **→ Regel: Die `Manuskript_BandN_Komplett.md` sind die publizierte Wahrheit. Niemals
> ungeprüft aus den Kapitel-Dateien neu erzeugen.**
>
> ### Was genau geändert wurde
> - `build_taschenbuch_docx.py`, `..._band2.py`, `..._band3.py`, `..._band4.py` und
>   `build_ebook_docx.py`: defensiver Skip — ein Szenentrenner direkt vor einer
>   Kapitelüberschrift wird übersprungen (gleiche Lösung wie Band 5).
> - Dieselben vier Taschenbuch-Skripte: `teaser_paragraphs` durch den echten Anfang des
>   Folgebandes ersetzt (Quelle: **Komplett-Manuskript**, s. o.).
> - `build_cover_kdp_band3.py` PAGES 107→106, `..._band4.py` PAGES 97→95.
>
> ### ⚠️ OFFEN: Cover prüfen
> Durch die kürzeren Leseproben und die entfernten Ornamente haben sich die Seitenzahlen
> geändert → der Buchrücken wird minimal schmaler:
> **Band 3: −0,06 mm · Band 4: −0,11 mm** (KDP-Toleranz für Rücken-Freiraum: 1,6 mm).
> Für Band 1 und 2 sind die alten Seitenzahlen unbekannt (dort gibt es keine Cover-Skripte).
> **Empfehlung: Innenteile hochladen und die KDP-Vorschau entscheiden lassen** — sie meldet
> eine Rücken-Abweichung zuverlässig. Erst dann Cover nachziehen.
>
> ### Neue Dateien
> `Output/Band1..4/KDP_BandN_Manuskript.docx` + `.pdf` (Band 1 hat kein PDF im Skript —
> per LibreOffice separat konvertiert).
>
> ---
>
> ## ✅ NACHTRAG 2026-07-18: Rezensions-QR-Code jetzt in ALLEN FÜNF Bänden
>
> Band 1 hatte als einziger einen QR-Code auf der „Hat dir gefallen?"-Seite. Band 2–5 haben
> ihn jetzt auch — gleiche Gestaltung, gleicher Text, gleiche Größe (1,6 Zoll).
> Der Code führt **direkt auf das Amazon-Bewertungsformular**, nicht nur auf die Produktseite.
>
> | Band | ASIN | QR im gebauten Buch dekodiert |
> |---|---|---|
> | 1 | B0GNZVXDDJ | ✅ (unverändert) |
> | 2 | B0GV8R8QJ6 | ✅ |
> | 3 | B0H4VQHBLX | ✅ |
> | 4 | B0H869XC17 | ✅ |
> | 5 | B0H9DJF3T9 | ✅ |
>
> **Neues Werkzeug: [`Scripts/build_qr_rezension.py`](../Scripts/build_qr_rezension.py)**
> erzeugt alle Codes aus einer ASIN-Tabelle — und **liest jeden erzeugten Code mit OpenCV
> wieder ein und prüft ihn gegen die Soll-URL.** Ein QR-Code, der im gedruckten Buch ins
> Leere führt, wäre nicht mehr korrigierbar; deshalb keine Annahme, sondern eine Messung.
> Zusätzlich wurden die **im fertigen DOCX eingebetteten** Codes dekodiert und gegen die
> ASINs geprüft (nicht nur die PNG-Dateien).
> Bei neuer Ausgabe/ASIN: Tabelle im Skript anpassen, `py Scripts/build_qr_rezension.py --force`.
>
> **Seitenzahlen unverändert** (187/114/106/95/104) — die Cover sind von dieser Änderung
> also nicht betroffen.
>
> ⚠️ **Nebenbefund, behoben:** `build_taschenbuch_docx_band5.py` hatte durch einen früheren
> Reparaturlauf doppelte Zeilenenden (`\r\r\n`, 724 Stück). Syntaktisch harmlos, aber die
> Datei war unlesbar geworden. Bereinigt; die übrigen Skripte waren nicht betroffen.

---

<details><summary>Ursprüngliche Arbeitsliste (historisch)</summary>

# TODO — Nachbesserung Band 1–4 (nach der Band-5-Veröffentlichung)

> **★ STATUS 2026-07-18: JETZT DRAN. Band 5 ist veröffentlicht, die Reihe ist komplett.**
> Die Sperre („erst Band 5 fertig") ist damit aufgehoben.
>
> **Und der Zeitpunkt ist jetzt der bestmögliche:** Fehler 1 (erfundene Leseproben) war bisher
> gar nicht sauber behebbar, weil der jeweils nächste Band noch nicht existierte. **Jetzt
> existieren alle fünf** — jede Leseprobe kann endlich den echten nächsten Band zeigen.
> Aus der Reparatur wird ein Verkaufsargument.
>
> _(Ursprüngliche Entscheidung vom 2026-07-17: Band 5 zuerst. Erledigt.)_
>
> Gefunden 2026-07-17 beim Bauen von Band 5. **Band 5 ist von beidem NICHT betroffen** — die
> Fixes sind dort bereits an der Wurzel eingebaut.

---

## Was gemessen wurde (an den GEDRUCKTEN DOCX, nicht an den Skripten)

| | Fehl-Ornamente | Leseprobe: real / gedruckt |
|---|---|---|
| Band 1 | 17 | **0 von 32** 🔴 |
| Band 2 | 14 | 9 von 24 |
| Band 3 | 15 | 1 von 16 |
| Band 4 | 15 | 0 von 12 |
| **Band 5** | **0** ✅ | keine (kein Nachfolger) |

Zusätzlich für Band 4 geprüft und **in Ordnung**: Frontmatter identisch zwischen Kompilat und
Druck, kein ENDE-Marker im Buch. Es sind wirklich nur diese zwei Punkte.

---

## Fehler 1 — Erfundene Leseproben ⚠️ DAS IST DER ERNSTE

**Was:** Band 1–4 drucken je eine „Vorschau auf Band N+1". Diese Leseproben wurden
**spekulativ geschrieben, bevor der nächste Band existierte — und nie nachgezogen.**

Beispiel Band 4 → Band 5:
- **Gedruckt:** *„Es begann mit dem Hund. Schatten hatte die ganze Nacht am Fenster
  gestanden… Und dann, weit hinten, ging eines der Lichter aus… ‚Theo, wach auf.'"*
- **Real (Band 5, K1):** *„Es gibt eine Kälte, die von draußen kommt… Nora saß am Küchentisch…
  Vor ihr auf dem Tisch lag Frau Silbers Karte."*

Kompletter anderer Anfang. Von 12 Absätzen existiert **kein einziger**. (Die eine Überlappung
— *„Was siehst du?"* — ist Zufall: Leseprobe und K1 wurden aus demselben Plan geschrieben.)

**Warum das der ernste Fehler ist:** Keine Kosmetik, sondern eine **Falschaussage im
verkauften Produkt.** Es trifft genau den Leser, der am meisten investiert hat: das Kind, das
den Band liebte, die Vorschau las, auf den nächsten wartete — und die Szene dann nicht findet.
**Am schwersten wiegt Band 1** (Einstiegsband, meistgelesen, Vorschau zu 100 % erfunden). Wer
die Reihe durchliest, merkt es viermal.

**Fix:** In `Scripts/build_taschenbuch_docx_band{1..4}.py` die Liste `teaser_paragraphs`
durch den **echten** Anfang des nächsten Bandes ersetzen (aus `Band{N+1}/Manuskript/Kapitel_01.md`).

**★ Der ideale Zeitpunkt ist NACH Band 5:** Dann existieren alle Folgebände, die Leseproben
können endlich den echten Text zeigen, und die Listings lassen sich gleich mit „Reihe
abgeschlossen" auffrischen. **Aus der Reparatur wird ein Verkaufsargument.**

**Regel für die Zukunft (gilt auch für Staffel 2):** Nie einen Teaser vor dem nächsten
Manuskript schreiben. Erst danach — und Absatz für Absatz gegen den echten Text prüfen.

---

## Fehler 2 — Separator-Bug (Fehl-Ornamente)

**Was:** Hinter dem Cliffhanger jedes Kapitels steht ein „✦ ✦ ✦", dann erst der Seitenumbruch.

**Ursache:** `---` ist überladen — es bedeutet *Szenentrenner* **und** *Kapiteltrenner*. Die
Parser (`build_taschenbuch_docx_band*.py` **und** `build_ebook_docx.py`) machen aus **jedem**
`---` einen Szenentrenner. Die Kompilier-Skripte setzen aber zusätzlich eins zwischen die Kapitel.

**⚠️ Ehrliche Einordnung — das ist Kosmetik, kein Drama.** Ein Ornament am Kapitelende liest
sich für einen Leser **nicht als Fehler**; viele Bücher setzen dort bewusst eine Vignette. Der
echte Einwand ist handwerklich: dasselbe Symbol bedeutet zwei Dinge, und es steht etwas
zwischen dem Cliffhanger und dem Umblättern. **Kein Kind legt deswegen das Buch weg.**
Allein wäre das keinen Neu-Upload wert — zusammen mit Fehler 1 nimmt man es mit.

**Fix (eine Zeile pro Skript):** In `Scripts/build_manuskript_komplett{,_band2,_band3,_band4}.py`
```python
parts.append("\n\n---\n\n")   →   parts.append("\n\n")
```
Die Kapitelüberschrift `# Kapitel N` markiert die Grenze bereits eindeutig, und **kein Skript
splittet auf `---`** (geprüft). Danach Manuskript **und** Taschenbuch neu bauen.

**Optional zusätzlich (Gürtel und Hosenträger):** den defensiven Skip aus
`build_taschenbuch_docx_band5.py` übernehmen — er überspringt einen Trenner vor einer
Kapitelüberschrift, egal was im Manuskript steht.

---

## Vorgehen, wenn es losgeht

1. **Vorlage ist Band 5.** `build_manuskript_komplett_band5.py` und
   `build_taschenbuch_docx_band5.py` enthalten beide Fixes plus Selbstprüfungen. Von dort
   ableiten, nicht von Band 4.
2. Pro Band: Kompilier-Skript fixen → Manuskript neu bauen → Leseprobe durch echten Text
   ersetzen → Taschenbuch neu bauen.
3. **★ Verifikation am ARTEFAKT, nicht am Skript.** Das ist die Lehre aus dem Band-5-Bau:
   Beide Fehler waren im Code unsichtbar. Beim Band-5-Bau kam so noch ein dritter zutage
   (`**ENDE**`-Marker aus Kapitel_18.md schlug bis in den Druck durch) — gefunden **nur**,
   weil ich das gebaute DOCX ausgelesen habe. Prüfskript:
   ```python
   from docx import Document
   voll=[p.text.strip() for p in Document(PFAD).paragraphs if p.text.strip()]
   orn='✦  ✦  ✦'
   bad=[voll[i+1][:34] for i,p in enumerate(voll[:-1]) if p==orn and voll[i+1].startswith('Kapitel ')]
   print('Fehl-Ornamente:', bad or 'KEINE')
   ```
4. **eBooks nicht vergessen:** `build_ebook_docx.py` hat denselben Parser-Fehler.
   ⚠️ Offen: Ein EPUB existiert nur für Band 1. Ob B2–B4 eBooks haben (und wo), ist ungeklärt.
5. **KDP:** 4 Bücher neu hochladen, je ~72 h Prüfung. **Bewertungen und Rankings bleiben
   erhalten.** Risiko gering.

---

## Reihenfolge (falls nicht alles auf einmal)

1. **Band 1** — größter Hebel: Einstiegsband, meistgelesen, Leseprobe zu 100 % erfunden.
2. **Band 4** — führt direkt zu Band 5, die Leseprobe ist die Brücke zum Finale.
3. Band 3, Band 2.

---

Verwandt: `Band5/PLAN_Band5.md` (Phase 5), `Dokumentation/Stimmen_Pruefplan.md`.

</details>
