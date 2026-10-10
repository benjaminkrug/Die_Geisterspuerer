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

---

## Entscheidung des Autors · 2026-10-10

> „KDP-Fragen brauchst du nicht beachten. Bearbeite es erstmal komplett und achte nicht darauf,
> wieviel du kürzt. Achte auch auf Qualität und Spannung.“

Folge: Die Stopp-Regel (0.5) ist **vom Autor aufgehoben**. Das Wortbudget wird zur Obergrenze für
Füllstoff, nicht zur Untergrenze für Kürzungen. **Maßstab ist Qualität und Spannung.** Schritt 1
(Anhang und QR-Code) wartet auf die Domain („das Feld bearbeiten wir später“).

---

## Schritt 2 – Der Schluss (Kap. 14–18 → 14–16) · 2026-10-10

### 2a Szenenliste

| Alte Szene | Wo jetzt | Grund |
|---|---|---|
| K14 Aufwachen, Frühstück, Lebenslauf-Witz, Spinnen | **K14**, gekürzt | Atempause nach dem Abschied, Humor bleibt |
| K14 Namensliste „Wir haben es geschafft“ | **K14** | Ein Satz, der zeigt, was sie erreicht haben |
| K14 Karte hinter dem Brett (Versteck durch Klopfen) | **K14**, jetzt findet **Schatten** das Brett | W7: kein viertes Klopf-Versteck |
| K14 12 Kreise, frische Tinte | **K14**, ans Kapitelende verschoben, verschärft: Staub vor dem Versteck unberührt | Neuer, stärkerer Haken |
| K15 Notizen auf der Karte (Heinrich B., Clara, Helene) | **K15** | Anker für Band 2 |
| K15 GRAVEN, roter Kreis | **K14** | Gehört zur Entdeckung der Karte |
| K15 Bibliothek 3 (Chronik) | **K14**, aus **Silbers eigener Chronik** (Kap. 5) | W6: dritte Bibliothek weg |
| K15 Friedhof, Gestalt starrt | **K15**, ausgebaut: Atemwolke, **Raureif am Zaun**, Tor schlägt zu | Mehr Spannung. Der Raureif bereitet das Schlussbild vor |
| K16 Flucht nach Hause | **K15**, gekürzt | – |
| K16 Entscheidung „Wir hören auf“ → Theo überzeugt Nora | **K15, umgedreht:** Nora entscheidet **selbst**, Theos vorbereitete Rede läuft ins Leere | W1: keine Wiederholung von Kap. 11. Zeigt Noras Entwicklung, Humor |
| K16 Mama erzählt von der Nachbarin | **gestrichen** | W11: Der Leser kennt das seit Kap. 5 und 6 |
| K17 Brief unter der Diele (Klopfen) | **K15-Ende**, jetzt zeigt **Schatten** die Diele | W7. Der Umschlag ist der Kapitelhaken |
| K17 Brief: Anrede, Silber, Tür vor 200 Jahren, Anna, Schatten, Schleier | **K16**, nur Neues oder Vertiefung. Anna → Theo verbindet „Danke“ mit Linas DANKE | W3 |
| K17 „Wenn ihr diesen Brief lest, bin ich nicht mehr hier“ | **auf den Umschlag** (Ende K15) | Stärkerer Haken |
| K17 „Hütet euch vor dem Ersten“ + Schatten als Schild | **K16**, ohne die Wiederholung aus Kap. 11 („Hand hat gezittert“). Neu: *„Im Notizbuch hat sie über ihn geschrieben. Hier schreibt sie an uns.“* | W2: Steigerung statt Wiederholung |
| K17 „Er tat etwas, das er noch nie getan hatte“ | **gestrichen** | Widerspruch zu Kap. 3 und 10, wo Schatten sich schon vor die Kinder stellt |
| K18 Nacht am Fenster, Stadt, Mama, Theo („mutigster Zehnjähriger“), Taschenlampen-Murmeln | **K16**, gekürzt | Warmer Ausklang, Humor |
| K18 „Morgen fangen wir an. Mit dem Friedhof.“ | **gestrichen** | X2: Band 2 spielt einen Monat später |
| K18 blaues Licht, Schatten bellt | **gestrichen**, ersetzt durch: **Raureif auf der Karte am Friedhofskreis**, eine zweite Hand „von der anderen Seite“ | W4: neues Schlussbild, das auf Band 2 zeigt |
| K16 Gespräch Theo über die Gestalt „seit 1887 allein“ | **K16 (Nacht)** | Übergang von Grusel zu Mitgefühl, Kern der Reihe |

**Pflicht-Anker:** alle 32 vorhanden (K1). Der Brief bleibt als Gegenstand (B4 Z.960, B5 Z.298/562).
Die Anrede *„Für die, die nach mir kommen“* passt zu B4: *„Ich habe es jemandem hinterlassen, von
dem ich hoffte, dass es ihn gab“*, daher Noras Satz *„Sie hat es gehofft.“*

### 2b–2e Kontrolle

| Prüfung | Ergebnis |
|---|---|
| `pruefe_band1_umbau.py --basis 4e983cf --schritt 2` | ✅ alle harten Prüfungen bestanden |
| Wörter | 27.179 → **23.125**; neue Kapitel 1.128 / 1.132 / 1.132 W (Band 3/4 Ø ≈ 1.000–1.070) |
| K5 neue Sätze > 18 W | 0 (zuerst 1 gemeldet: **Fehlalarm des Werkzeugs**, kursiver Satz endete auf `.*`. Skript korrigiert, trennt jetzt zuerst nach Absätzen) |
| K9 Schritt 2 | „Wir hören auf“ 1×, „Hand hat gezittert …“ 1×, „Schon wieder ihr zwei“ 0×, „Morgen fangen wir an“ 0× |
| K10 Stimme | Und-Anfänge +0 %, Kurzabsätze +11 % (Korridor ±15 %) |
| `pruefe_logik.py 1` | 18 → **9** Kandidaten. Zwei waren selbst verursacht und sind behoben: „keuchte“ (kein erlaubtes Sprechverb) und ein Satz, der wortgleich in Kap. 3 steht. Der Ersatz „rang nach Luft“ wurde verworfen (Echo mit „holte tief Luft“ drei Zeilen später, Regel 3). |
| Kapitelenden | alle drei neu (erlaubt): „Und trotzdem war die Tinte nass.“ / „*Wenn ihr das lest, bin ich nicht mehr hier.*“ / „Genau auf derselben Stelle.“ |
| Übergang Band 2 | Kein Satz legt eine Zeit fest. Die Karte liegt am Ende auf dem Schreibtisch, so beginnt Band 2 (*„Frau Silbers Karte lag seit Tagen auf ihrem Schreibtisch“*). |
| Band 4 (kaltes Zimmer) | Nicht verschärft. Der Satz „Die Wohnung … Aber die Kälte war weg“ sagt nichts über die Zukunft des Zimmers. |
| Lesung K14–16 am Stück | Ein missverständlicher Satz („Niemand hatte sie überreden müssen“) → „Und diesmal musste Theo sie nicht überreden.“ |
| Grusel → Humor | K14 Tinte → (Kapitelende), K15 Friedhof → Theos Rede; K16 „der Erste“ → „Können wir jetzt nach unten gehen? Bitte?“ |

---

## Schritt 3 – Die Lina-Frage aussprechen (Kap. 13) · 2026-10-10

Basis: `0382068` (Ende Schritt 2).

**Eingefügt** vor *„Meinst du, es hat wehgetan?“*: Theo fragt, was im Keller passiert ist. Nora:
*„Ich weiß es nicht.“* Sie glaubt aber, dass das nicht das Wichtigste für Lina war: *„Sie hat nie
geschrieben: Findet raus, was passiert ist.“* – *„Sondern?“* – *„Glaubt mir.“* – *„Haben wir.“*

| Prüfung | Ergebnis |
|---|---|
| Wortbudget +40 bis +100 | **+86** ✅ |
| K8 keine neuen Fakten (Sturz, Treppe, Unfall, Faber, Schleier …) | ✅ 0 neue Sätze, Faber 0 |
| Letzter Absatz Kap. 13 unverändert | ✅ (K6 leer) |
| Regel 3 (neue Formulierungen im ganzen Buch gesucht) | „Glaubt mir“, „Findet raus“, „Haben wir“ kommen nur hier vor. Zwei selbst erzeugte Echos behoben: „Dann nickte er“ (vgl. „Theo nickte“ 6 Zeilen später) und „Nora dachte an …“ zweimal hintereinander. „Fußabdrücke“ → „Fußspuren“ (Wortwahl aus Kap. 10). |
| Bezug zum Kanon | „Glaubt mir“ greift Linas Tagebuch auf (*„Niemand glaubt mir“*, *„soll jemand wissen, dass ich die Wahrheit gesagt habe“*) und passt zu Band 5 (*„Lina, die auch niemand gehört hatte“*) |
| Lesung Kap. 13 | Die Frage kommt nach dem Abschied, nicht davor, und zerredet das Licht nicht. Theos „Haben wir“ schließt warm ab. |
| Offen | Die Zustimmung des Autors „klingt nach Theo und Nora“ (Plan 7.4, Schritt 3) |

---

## Schritt 4 – Zone A straffen (Kap. 4–7) · 2026-10-10

Basis: `bde071d` (Ende Schritt 3).

| Eingriff | Was | Warum |
|---|---|---|
| Kap. 4 Schultag | Klasse, Vorstellung und das Grübeln über die Frage gekürzt. Bleiben: HILF im Kopf, der Spiegel, Theos Hamster-Witz, Theos *„Jemand bittet um Hilfe“*. Der Hamster „Herbert“ auf dem Heimweg ist gestrichen. **Fehler im Original behoben:** *„Das ist kein Drohung“* → *„keine Drohung“*. | Zone A, kein Fortschritt im Schultag. Ein loser Faden weniger (Sommersprossen-Mädchen und Herbert kommen in Band 1–5 nie wieder vor; geprüft) |
| Kap. 5 Liste | Nora sieht den blauen Zettel *„Lina Vogt? – 1974?“* und die Häkchen **an der Wand** | X4: vorher erzählte sie das erst in Kap. 6 aus dem Gedächtnis |
| Kap. 6 | **Ein** Besuch in der Bibliothek: Silber-Artikel (digital) → Lina (Mikrofiche) → Adresse = Kirchgasse 14. **Neues Kapitelende:** *„Das ist unsere Adresse.“* … *„Nach Hause.“* | W6: Der zweite Besuch mit gleichem Ablauf („Für die Schule?“) entfällt, ebenso der Logikbruch „Sie sind schon in der Bibliothek und gehen trotzdem heim“. Das stärkste Ende der Buchmitte rückt ans Kapitelende. |
| Kap. 7 | Verarbeitung im Archiv → draußen Schattens Blick zum Friedhof (aus Kap. 6) → Heimweg → Mama mit der Neuigkeit von der Nachbarin, dann bricht sie zur **Spätschicht** auf → VERGISS NICHT → Kratzen (Ende unverändert) | Neue Reihenfolge. Mama ist weg, sonst hätte sie das Hämmern in Kap. 8 gehört (Logik). Der Beruf (Krankenhaus, Schicht) ist Kanon. |

| Prüfung | Ergebnis |
|---|---|
| `pruefe_band1_umbau.py --basis bde071d --schritt 4` | ✅ alle harten Prüfungen bestanden |
| Wörter | 23.215 → **22.611** (Kap. 4 −175, Kap. 5 +45, Kap. 6 −36, Kap. 7 −434) |
| K9 „Für die Schule?“ | 1× ✅ |
| K6 Kapitelenden | nur Kap. 6 geändert (erlaubt); 4, 5, 7 unverändert ✅ |
| K10 Stimme | Und-Anfänge +0 %, Kurzabsätze +3 % |
| `pruefe_logik.py 1` | 9 Kandidaten, keine neuen |
| Lesung Kap. 6–7 am Stück | **Zwei selbst erzeugte Fehler gefunden und behoben:** (1) Nora band Schatten erst los, *nachdem* sie losgegangen waren. (2) Mama legte sich schlafen, und die Kinder hämmerten danach in Kap. 8 die Wand auf → Mama geht zur Spätschicht. Außerdem zwei Satzanfänge „Nora …“ hintereinander, und „Pizza im Kühlschrank“ als Echo zu Kap. 4 → „Essen steht im Kühlschrank“. |
| Zeitachse | Kap. 6 und 7 sind jetzt **ein** Tag (vorher zwei). Kap. 8–11 geprüft: passt. `Die_Geisterspuerer_Author_Info.md` (Tag 3/4, 4/5) wird in Schritt 7 nachgezogen. |
| Bewusster Rückbezug | Kap. 7 *„Wir finden raus, was passiert ist“* ↔ Kap. 13 *„Sie hat nie geschrieben: Findet raus, was passiert ist“* |

---

## Schritt 5 – Wiederholungen im Mittelteil · 2026-10-10

Basis: `e217139` (Ende Schritt 4).

| # | Eingriff | Warum |
|---|---|---|
| W5 | Kap. 12: Das Tagebuch wird **nicht mehr ein zweites Mal zitiert** (vorher fünf Einträge mit Datum), sondern zusammengefasst. Nur *„Niemand glaubt mir“* wird vorgelesen, und Nora liest es zweimal, *„damit er im Raum blieb“*. Neu: Schatten schaut auf eine Stelle neben dem Bett, *„wo niemand saß“*. | Wiederholung von Kap. 9. Der Satz bereitet Kap. 13 vor („Glaubt mir“). |
| W7 | Verstecke: in Schritt 2 erledigt (Karte und Brief findet jetzt Schatten). Durch Klopfen gefunden wird nur noch die Tapete in Kap. 8. | – |
| W9 | Kap. 10: Der Fehlalarm „Theo ist weg“ ist ersetzt durch: **Das Handylicht geht aus**. Schwärze, Theos Hand am Ärmel, das Licht kommt schwächer zurück. *„Akku?“* – Anzeige: 80 %. Nora sagt nichts. | Der zweite Fehlalarm desselben Typs (Kap. 5) wirkte nicht mehr. Die neue Szene ist echter Grusel ohne Auflösung „war nichts“ |
| W10 | Kap. 10: zweimal „offiziell festhalten“ → Theo: *„Kennst du die Stelle im Film … Ich bin einer von denen im Kino.“* und *„Neue Regel: keine Keller mehr. Nie wieder. Auch nicht zum Getränkeholen.“* | Humor wird **ersetzt, nicht gestrichen** (Humor-Regel). Bleibt 2×: Kap. 4 (Grabstein) und Kap. 5 |
| Titel | Kap. 12 „Konfrontation“ → **„Bitte“** | Der Titel versprach einen Kampf. Das Wort steht im Kapitel an den Fenstern. Kein Kapitel der Serie heißt so (geprüft). Kein Dokument außerhalb von Band 1 zitiert den alten Titel (geprüft). |
| Altfehler | Kap. 10: *„etwas, das Nora noch nie von ihm gehört hatte. Er winselte.“* → *„so noch nie“* | Widerspruch im Original: Schatten winselt schon in Kap. 2 und 8, und der nächste Satz sagt selbst *„Nicht das … Winseln von vorhin“*. Minimal-Regel Stufe 1 (ein Wort). |

| Prüfung | Ergebnis |
|---|---|
| `pruefe_band1_umbau.py --basis e217139 --schritt 5` | ✅ alle harten Prüfungen bestanden |
| K9 | „offiziell festhalten/protokoll“ 2×, datierte Tagebuch-Zitate in Kap. 12: 0× |
| K6 | Kap. 12 als „geändert“ gemeldet: **Fehlalarm**, das Werkzeug ordnet über den Titel zu. Der letzte Absatz ist wortgleich (geprüft). |
| K10 | Und-Anfänge +0 %, Kurzabsätze +1 % |
| `pruefe_logik.py 1` | 9 Kandidaten, keine neuen |
| Lesung Kap. 10 und 12 | „Ich bin die im Kino“ → „Ich bin einer von denen im Kino“ (Theo ist ein Junge). „Handy“ als Lichtquelle passt zu Kap. 10. |

---

## Schritt 6 – Widersprüche · 2026-10-10

Basis: `5c921b8` (Ende Schritt 5).

| # | Widerspruch | Status / Eingriff |
|---|---|---|
| X1 | „Erster Schultag“ (Kap. 4) ↔ *„was ich in den Sommerferien gemacht habe“* (Kap. 13) | → *„Falls in der Schule mal jemand fragt, was ich so in meiner Freizeit mache.“* |
| X2 | *„Morgen fangen wir an“* ↔ Band 2 (*„letzten Monat“*, Herbst) | in Schritt 2 weggefallen, **per Suche bestätigt: 0×** |
| X3 | *„rot vom Weinen am Vortag“*, *„Du hattest gestern Angst vor dem Kellerlicht“* (Kap. 11). Tagebuch, Keller und Streit liegen am selben Tag (das Juli-Tageslicht reicht bis in den Abend). | → *„rot vom Weinen“* und *„Du hast dich eben im Keller an meinem Ärmel festgekrallt“*. Das greift die neue Handylicht-Szene aus Schritt 5 auf. |
| X4 | Lina erst in Kap. 6 genannt | in Schritt 4 behoben |
| X5 | *„hundertmal hier oben“ – „Dreimal“* | in Schritt 2 weggefallen, **per Suche bestätigt: 0×** |
| **X6 (neu gefunden)** | Kap. 4: *„Nora stellte die Tasse ab“*, aber ihr ist gerade die **Müslischüssel** heruntergefallen (Ende Kap. 3, Anfang Kap. 4) | → *„Nora stieg über die Scherben.“* |

Nebenbei, Regel 3: In Kap. 11 standen „noch rot … noch immer“ direkt hintereinander → „rot vom Weinen“.
Theos Geste „mit dem Ärmel über die Augen“ kam durch den neuen Text in Kap. 12 auf 4× → dort „Theo
zog die Nase hoch“.

| Prüfung | Ergebnis |
|---|---|
| `pruefe_band1_umbau.py --basis 5c921b8` | ✅ alle harten Prüfungen bestanden, ±1 Wort |
| `pruefe_logik.py 1` | 9 Kandidaten, keine neuen |
| `git diff` Zeile für Zeile | Jede geänderte Zeile gehört zu X1, X3, X6 oder zum Regel-3-Hinweis oben |

---

## Schritt 7 – Endabnahme · 2026-10-10

Stand nach Schritt 6 plus Endabnahme. Verglichen mit der Basis **`4e983cf`** (Fassung vor dem Umbau).

| # | Prüfung | Ergebnis |
|---|---|---|
| 1 | `pruefe_band1_umbau.py --basis 4e983cf` | ✅ alle harten Prüfungen bestanden. **27.179 → 22.6xx Wörter, 18 → 16 Kapitel** |
| 2 | `pruefe_logik.py 1` | ✅ **18 → 9 Kandidaten**, alle im Kontext gelesen: 1× doppelter Kapiteltitel „Der Keller“ (B1/B3, bekannt, Kanon Z.431). 3× „gestern“ in Kap. 3/4 (alt, passt: nach Mitternacht bzw. am Morgen danach). 1× „damals“ (verweist richtig auf Kap. 7). 1× „vor drei Wochen“ (passt zu „in drei Wochen“). „presste“ und „schnaubte“ sind Handlungen, keine Redeverben. 1× wörtlich wiederholter Satz „Sein Fell sträubte sich vom Nacken bis zum Schwanz“ (stand schon in der Basis 2×, alt) |
| 3 | Stimme (K10) gegen `4e983cf` | ✅ Und-Anfänge +2 %, Kurzabsätze **+10 %** (lag nach Schritt 6 bei +15 %, also am Rand → sechs erzählende Kurzabsätze in Kap. 14–16 zusammengelegt, wo kein Effekt verloren ging) |
| 4 | Lesung | ✅ **für alle geänderten Kapitel am Stück** (4–7, 10, 12–16) und an jedem Übergang. ⚠️ Kap. 1–3, 8, 9 und 11 sind bis auf Einzelwörter unverändert und wurden nicht noch einmal ganz gelesen. |
| 5 | **Testleser Runde 2** | ⏳ **offen**. Bogen: `Band1/Umbau/Testleser_Bogen.md` (für 16 Kapitel) |
| 6 | Kapitel-Dateien aus der Komplett-Datei neu erzeugt | ✅ 16 Dateien, `Kapitel_17.md` und `Kapitel_18.md` entfernt. Abgleich Komplett ↔ Kapitel: **0 Abweichungen** |
| 7 | Dokumente nachgezogen | ✅ `Die_Geisterspuerer_Author_Info.md` (Zeitlinie Kap. 5–16 neu), `Story_Outline.md` (Hinweis 16 Kapitel), `Band1/Analyse.md` (als **überholt** markiert), `Stimmen_Pruefplan.md` (Maßstab = `4e983cf`, F1), `Serien_Kanon.md` Z.385 (Zitat aus Kap. 6 entfällt; Band 2–5 stützen sich nicht darauf, geprüft) |
| 8 | Klappentext (F2) | ✅ `KDP_Beschreibungen.md` Z.58: „18 Kapitel“ → **„16 Kapitel“**. ⏳ **Bei KDP eintragen: Autor** |
| 9 | Am fertigen Artefakt | ✅ **Taschenbuch** (`build_taschenbuch_docx.py`): 16 Kapitel, 0 Fehl-Ornamente, kein ENDE-Marker, keine Wortzahl-Zeile im Druck. Romanteil: 909 `„` / 909 `“` / **0** gerade, 0 doppelt öffnend. ✅ **eBook** (`build_ebook_docx.py`): 16 Kapitel, 921/921, 0 gerade. Hinweis: Ein Ornament steht nach dem letzten Satz vor dem Anhang (wie in der alten Fassung). |
| 10 | Seitenzahl | LibreOffice-Proxy 211 → **179 (−15,2 %)**, also ≈ **158 KDP-Seiten** statt 186. ⏳ **Cover-Rücken** (`build_cover.py`, `seiten=186`) erst neu bauen, wenn KDP die echte Seitenzahl zeigt. Die 10-%-Regel wurde auf Wunsch des Autors nicht beachtet (siehe Entscheidung oben). |
| 11 | Spielbuch (CYOA) Band 1 | ⏳ **offen**. Es beruht auf der alten Fassung. Abgleich vor dem Upload empfohlen (Kap. 6/7 und der Schluss haben sich geändert). |

### Fehler 3 (Anführungszeichen) mit erledigt

Nach der Anleitung in `TODO_Nachbesserung_Band1-4.md`: Vorbedingung geprüft (`„` = gerade `"`,
0 × `“`) → alle geraden `"` durch `“` ersetzt → Nachbedingung geprüft. Komplett-Datei 909 Paare,
die 16 Kapitel-Dateien zusammen ebenfalls 909. **Die Renderer bleiben unverändert**, sie wandeln
für Band 1 weiter nichts um. Am Artefakt bestätigt (Punkt 9).
**Noch offen:** 22 gerade Anführungszeichen in der **Leseprobe von Band 2 im Anhang**. Die Leseprobe
wird in Schritt 1 ersetzt.

### Die Kurve, neu bewertet (gleiches Raster wie im Plan, Abschnitt 2)

| Kap. | alt | neu | warum |
|---|---|---|---|
| 6 | 5 | **8** | Silber + Lina + Adresse in einem Kapitel, endet auf „Das ist unsere Adresse … Nach Hause.“ |
| 7 | 7 | 7 | Doppelte Bibliothek weg, Inhalt sonst gleich |
| 10 | 9 | 9 | Fehlalarm ersetzt (Handylicht). Gleich stark, weniger durchschaubar |
| 12 | 6 | 6 | Kein zweites Zitieren mehr |
| 13 | 5 | 5 | Lina-Frage ausgesprochen (Gefühl, nicht Spannung) |
| 14 (Karte) | 4 | **6** | GRAVEN, Chronik, frische Tinte bei unberührtem Staub |
| 15 (Friedhof) | 6/3 | **8** | Raureif am Zaun, Tor schlägt zu, Noras eigene Entscheidung, der Umschlag als Haken |
| 16 (Brief/Nacht) | 4/4 | **7** | Brief nur mit Neuem, Warnung „an uns“, Schlussbild Raureif auf der Karte |

**Schlussteil (ab Lina erlöst): Ø 4,2 → Ø 7,0.** Lina ist erlöst bei 77 % (vorher 73 %).

⚠️ **Diese Neubewertung stammt von dem, der den Text geschrieben hat.** Das ist der schwächste
Beleg in diesem Protokoll. Er ersetzt **nicht** Testleser Runde 2. Erst deren Kurve zeigt, ob die
Delle weg ist.

### Offen für den Autor

1. **Testleser** Runde 1 (alte Fassung, gedrucktes Buch) und Runde 2 (neue Fassung)
2. Freigabe der neuen Theo- und Nora-Stellen („klingt nach den beiden“)
3. Schritt 1: Anhang + QR-Code (Domain), dabei die Leseprobe von Band 2 ersetzen
4. KDP: Klappentext „16 Kapitel“; nach dem Upload Seitenzahl ablesen → Cover-Rücken
5. Spielbuch Band 1 gegen die neue Fassung querlesen

---

## Nachprüfung Schritt 2 (auf Wunsch des Autors) · 2026-10-10

Basis: `af3d359`. Auftrag: Schritt 2 noch einmal genau prüfen, jede Änderung begründen, nur
einbauen, was den Text wirklich verbessert, und Logikfehler suchen.

### Gefundene Logikfehler

| # | Fehler | Herkunft | Eingriff |
|---|---|---|---|
| L1 | **Zeitspanne:** Von der Ankunft bis zu Linas Befreiung vergehen zwei Tage. Der Text sagte aber „in drei Wochen“ (K14), „vor drei Wochen“ (K16), „seit Wochen“ (K14), „in all den Wochen“ (K12), „in ihrer ersten Woche“ (K13). | Im Original angelegt (dort ~4 Tage, aber „Wochen“). Schritt 2 hat zwei Stellen übernommen bzw. neu geschrieben, Schritt 4 hat die Zeit weiter verkürzt. | „seit dem Umzug“, „Vor ein paar Tagen“, „Seit sie ihn kannten“, „am ersten Tag“. Theos Witz („bei dem Tempo bin ich dreißig“) rechnete mit drei Wochen und ist ersetzt: *„Wenn jeder so gruselig wird wie Lina, hab ich mit elf graue Haare.“ – „Du bist zehn.“ – „Eben. Ein Jahr noch.“* Mama: „gut eingelebt“ → „schnell eingelebt“. |
| L2 | **Nasse Tinte:** Nora folgerte „heute Nacht durchgestrichen“. Nasse Tinte heißt aber: höchstens Minuten alt. | Schritt 2 | „Tinte trocknet schnell. Dieses Kreuz konnte höchstens ein paar Minuten alt sein.“ |
| L3 | **Staub:** „Ohne Fingerabdruck … nur Schattens Nase“. Nora hatte das Brett aber selbst herausgezogen. | Schritt 2 | „Darin nur zwei Spuren. Schattens Nase. Und ihre eigenen Finger von vorhin.“ |
| L4 | **Selbst erzeugt bei L2:** Die Karte lag unbeaufsichtigt in der Küche, während Nora im Arbeitszimmer las. „Minuten alt“ hätte dann bloß bedeutet, dass jemand in dieser Zeit in der Küche war, und das unberührte Versteck wäre als Beweis wertlos (Regel 2: ein Fix bricht etwas anderes). | Nachprüfung | Nora nimmt die Karte mit ins Arbeitszimmer und gibt sie nicht aus der Hand. Jetzt ist es wirklich unmöglich: Minuten alt, aber bis eben in einem Versteck, das seit Monaten niemand geöffnet hat. |
| L5 | „Schatten hatte **damals** hingestarrt.“ Der Bibliotheksbesuch war gestern. | Schritt 2 | „Sie waren gestern daran vorbeigegangen.“ |
| L6 | „**Die Erste**, der ich geholfen habe, hieß Anna“ steht zwei Absätze vor „hütet euch vor **dem Ersten**“. Verwechslungsgefahr für Kinder. | Schritt 2 (Original: „den ersten Menschen“) | „Der erste Mensch, dem ich geholfen habe, war ein Mädchen. Anna.“ |
| L7 | „vor **fast** zweihundert Jahren“ und Noras Gedanke „1823 … fast zweihundert Jahre“. Es sind gut 200. | Brief im Original; Schritt 2 hat es durch Noras Gedanken betont | „vor rund zweihundert Jahren“. Noras Gedanke nur noch „Im Jahr 1823.“ |
| L8 | Am Morgen nach dem ersten Schultag sind die Kinder nicht in der Schule. | Original (ebenso im alten Kap. 14) | Ein Satz: „Samstag. Keine Schule.“ |

### Inhaltliche Verbesserungen (nur diese)

| # | Was | Warum es wirklich besser ist |
|---|---|---|
| V1 | **Das blaue Licht (Ende Kap. 13) wird aufgegriffen.** Nora erkennt auf der Karte die Richtung wieder: Friedhof, „Drei, vielleicht vier Straßen“. „Sicher war sie nicht. Aber die Richtung stimmte.“ | Schritt 2 hatte einen **Cliffhanger ohne Folge** hinterlassen (das alte Kap. 14 griff ihn auf, das neue nicht). Jetzt läuft eine Linie: blaues Licht → Friedhofskreis → Gestalt (K15) → Raureif auf der Karte (K16). Abstand passt zu Band 2 (*„drei Straßen von ihrer Wohnung“*). Band 2–5 nennen das blaue Licht nicht (geprüft); Band 5 kennt „blaue Markierungen“ auf der Karte, das passt. |
| V2 | „Tinte … wie getrocknetes **Blut**“ → „Dunkelrot wie altes Siegelwachs“ | CLAUDE.md: kein Blut. Der Vergleich stammte aus dem alten Kap. 15. Das Siegelwachs verbindet den roten Kreis mit Silbers rotem Siegel in K15. |

### Bewusst NICHT geändert

| Stelle | Warum nicht |
|---|---|
| Theo: *„Wir waren auf einem Friedhof.“* (eigentlich gegenüber) | Theos Übertreibung, Figurenstimme (vgl. „Das hört man wahrscheinlich in Hamburg“). Kein Fehler. |
| *„Schatten stand im Türrahmen. Er kam nicht herein.“* | Gewolltes Unbehagen beim Wort „der Erste“. Kein Widerspruch zu Kap. 5. |
| Der Mann am Friedhof nur als „Umrisse eines Mannes“ | Band 2 hat zwei Gestalten (Brenner klein und gebückt, Voss groß). Jede Beschreibung legt fest, wer es war. Offenlassen ist richtig. |
| Länge der Kapitel 14–16 (~1.130–1.180 W) | Unter dem Richtwert von ~1.200, aber im Rahmen von Band 3/4. Mehr wäre Füllstoff. |

### Kontrolle

| Prüfung | Ergebnis |
|---|---|
| `pruefe_band1_umbau.py --basis af3d359 --schritt 2` | ✅ alle harten Prüfungen bestanden |
| gegen `4e983cf` | ✅ 27.179 → 22.680 W; Stimme: Und-Anfänge +2 %, Kurzabsätze +10 % |
| `pruefe_logik.py 1` | **9 → 8** Kandidaten („damals“ entfällt) |
| Regel 3 | Echo „ganz frisch“ / „ganz neu“ behoben → „höchstens ein paar Minuten alt“ |
| Suche „Woche(n)“ | nur noch 2×, beide über die Zeit **vor** dem Umzug (richtig) |
| Kapitel-Dateien | neu erzeugt, 0 Abweichungen zur Komplett-Datei |
| Doku | Zeitlinie in `Die_Geisterspuerer_Author_Info.md`: Samstag, blaues Licht, Tinten-Logik, Zeitspanne |
