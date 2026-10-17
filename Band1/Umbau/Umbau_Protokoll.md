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

---

## Nachprüfung Schritt 3 (auf Wunsch des Autors) · 2026-10-10

Basis: `617b313`. Gelesen: **das ganze Kapitel 13**, nicht nur der Einschub, gegengeprüft mit Kap. 7
(Noras Versprechen), Kap. 9 (Tagebuch), Kap. 10 (Keller) und Band 5.

### Was am Einschub stimmt und bleibt (mit Beleg)

| Aussage | Beleg |
|---|---|
| *„Sie hat nie geschrieben: Findet raus, was passiert ist.“* | Wörtlich richtig. Lina wollte es **selbst** wissen, aber mit dem Ziel, dass man ihr glaubt: *„Wenn ich es verstehe, glauben mir vielleicht die anderen“* (Kap. 9). Dazu *„Niemand glaubt mir“*, *„soll jemand wissen, dass ich die Wahrheit gesagt habe“*. „Glaubt mir“ ist also **im Text belegt**, nicht hineingedeutet. |
| Stelle im Kapitel | Der Absatz davor endet mit *„das allein in den Keller gegangen war“*. Die Frage ergibt sich daraus. |
| Reihenfolge harte Frage → tröstende Frage („wie Einschlafen“) | Das Kapitel landet weich, bevor das blaue Licht kommt. |
| Kanon | Band 5: *„Lina, die auch niemand gehört hatte“*. K8: keine neuen Fakten zum Tod, Faber 0. |

### Gefundene Probleme

| # | Problem | Herkunft | Eingriff | Warum besser |
|---|---|---|---|---|
| P1 | **Widerspruch zur Vision im selben Kapitel:** *„für einen Herzschlag war Nora Lina … Aber sie verstand jetzt“*, und später *„Ich weiß es nicht.“* | **Schritt 3** | *„Ich weiß es nicht. Vorhin, als das Licht da war, hab ich nur gespürt, wie es sich angefühlt hat. Kalt. Und ganz allein.“* | Klärt: Nora kennt das **Gefühl**, nicht den **Hergang**. Die Vision wird genutzt, statt ihr zu widersprechen. Kein neuer Fakt. |
| P2 | **Unkommentiertes Versprechen:** Kap. 7 *„Wir finden raus, was passiert ist. Wir finden es raus.“* Kap. 13 „Ich weiß es nicht“, ohne Bezug darauf. Wirkt wie vom Autor vergessen. | **Schritt 3** | Theo: *„Du hast gesagt, wir finden es raus.“* – Nora: *„Stimmt. Aber ich glaube, das war nicht das Wichtigste für sie.“* | Aus einem gebrochenen Versprechen wird **Noras Entwicklung**: von „Fakten finden“ (die Rationale aus Kap. 1–4) zu „zuhören“. Das ist das Thema der Reihe (Codewort Band 1: ZUHÖREN). |
| P3 | Theo fragt **zweimal** fast dasselbe: *„Tut ihr das weh?“* (während) und *„Meinst du, es hat wehgetan?“* (danach). Mit dem Einschub stehen jetzt drei Theo-Fragen hintereinander. | Original; durch Schritt 3 verstärkt | Die erste Frage gestrichen (2 Zeilen) | Die zweite hat die stärkere Antwort („wie Einschlafen“). Der Abschied wird stiller: Licht wird kleiner → „Und dann war es weg.“ |
| P4 | *„Theo trat neben sie“* zweimal. Er steht schon neben ihr. | Original | Zweite Stelle → *„Er suchte ihre Hand.“* | Logik. Zuerst geplant war „griff nach ihrem Ärmel“, das wurde **verworfen**: Es ist Theos **Angst**-Geste (Kap. 1, 10, 11), hier staunt er aber. „Seine Hand suchte ihre“ wurde ebenfalls verworfen: zweimal „Seine …“ als Satzanfang. |
| P5 | „Ich weiß es nicht“ … „Ich weiß.“ zwei Zeilen auseinander | Nachprüfung | „Stimmt.“ | Regel 3, Echo |

### Bewusst NICHT geändert

| Stelle | Warum nicht |
|---|---|
| Keine Ursache für Linas Tod | Plan 7.1: Jede Ursache führt zur Frage „wovor floh sie?“ und damit zu Band 4 (Faber, kaltes Zimmer). Das Gefühl („kalt, ganz allein“) reicht. |
| „Glaubt mir“ als Antwort statt einer Tatsache | Ein Teil der Kinder wird trotzdem den Hergang wissen wollen. Das prüft der Testleser-Bogen (Frage 1). Eine echte Antwort ginge nur zusammen mit Band 4. |
| *„Zum ersten Mal seit Tagen“*, *„seit Tagen festgesessen“* | Passt zur neuen Zeitlinie (zwei Tage) |
| Kapitelende (blaues Licht) | Tabu. Es wird seit der Nachprüfung von Schritt 2 in Kap. 14 aufgegriffen. |

### Kontrolle

| Prüfung | Ergebnis |
|---|---|
| `pruefe_band1_umbau.py --basis 617b313` | ✅ bestanden; Kap. 13 +9 W |
| gegen `4e983cf` | ✅ Kap. 13 insgesamt **+98 W** (Budget Schritt 3: +40 bis +100) ✅; Stimme +2 % / +10 % |
| K8 (keine neuen Fakten) | ✅ 0; Faber 0 |
| K6 Kapitelende Kap. 13 | ✅ unverändert |
| `pruefe_logik.py 1` | 8 Kandidaten, keine neuen |
| Lesung Kap. 13 komplett | ✅ |
| Kapitel-Dateien | neu erzeugt, 0 Abweichungen |

---

## Nachprüfung Schritt 4 (auf Wunsch des Autors) · 2026-10-10

Basis: `cc22b11`. Gelesen: **Kap. 4–7 vollständig**. Gegengeprüft mit Kap. 2–3 (Mamas Schichten),
Kap. 8–16 (Bezüge auf Entferntes), Kap. 10/13 und Kanon (wo Lina starb) und Klappentext.

### Was an Schritt 4 stimmt und bleibt (mit Beleg)

| Entscheidung | Beleg |
|---|---|
| Lina-Zettel schon in Kap. 5 | Er entspricht jetzt **wörtlich dem Klappentext** (*„Ganz unten, in blauer Tinte und ohne Häkchen: Lina Vogt? – 1974?“*), den Käufer vorher gelesen haben. Vorher stand es nur in Noras Erinnerung (Kap. 6). |
| Eine Bibliothek statt zwei | Kein späteres Kapitel bezieht sich auf den zweiten Besuch (Suche „Bibliothek“ in Kap. 8–16: nur K15 „gegenüber der Bibliothek“, und das passt). Digital → Mikrofiche ist schlüssig: Silber vermisst seit März (digital, „letzte fünf Jahre“), Lina 1974 (Mikrofiche). |
| Neues Ende Kap. 6 („Das ist unsere Adresse … Nach Hause.“) | Stärkster Haken der Buchmitte. Schattens Blick „die Straße hinunter“ wird damit eingelöst. |
| Friedhof-Blick in Kap. 7 | Wird in K15 aufgegriffen (*„Sie waren gestern daran vorbeigegangen“*), passt. |
| Herbert gestrichen, Hamster-Witz bleibt einmal | Ein Witz braucht keine Fortsetzung. Ein benanntes Tier ohne Rolle war ein loser Faden. „Mein Hamsterreferat“ (Kap. 6) ist ein eigener Witz von Theo. |

### Gefundene Probleme

| # | Problem | Herkunft | Eingriff | Warum besser |
|---|---|---|---|---|
| P1 | **Mama arbeitet zwei Schichten an einem Tag:** Kap. 3 *„Frühschicht“*, Kap. 4 *„Bin gegen sechs zurück“*, Kap. 7 *„Ich muss los. Spätschicht.“* | **Schritt 4** (beim Beheben des Hämmer-Problems eingebaut) | Mama: *„Ich bin seit fünf auf den Beinen. Ich geh heute früh schlafen.“* Kap. 8 nach dem Türknall: *„Ihr erster Gedanke war Mama. Aber hinter der Schlafzimmertür blieb es still. Mama schlief, wie sie seit dem Umzug schlief. Wie ein Stein.“* | Kein Widerspruch zu Kap. 3/4. Der tiefe Schlaf ist **angelegt** (Kap. 2: *„so tief, dass man neben ihr staubsaugen konnte“*) und **wird später bestätigt** (Kap. 12: *„Wie immer schlief ihre Mutter tief und fest“*). Die Leserfrage „Warum hört Mama nichts?“ wird an der Stelle beantwortet, an der sie aufkommt. |
| P2 | Theo: *„Ein Mädchen ist in **unserer Wohnung gestorben**“*, *„Sie ist **dort gestorben**“*. Der Artikel nennt nur die Hausadresse, und Lina starb **im Keller** (Kap. 10, Kanon Z.278). | Original. Schritt 4 hat die Stelle nur verschoben. | *„Ein Mädchen hat in unserem Haus gewohnt. Vor fünfzig Jahren. Und ist gestorben.“* / *„Sie hat da gewohnt.“* / *„Ein Mädchen hatte **in ihrem Haus** gelebt“* (statt mehrdeutigem „hier“ in der Bibliothek) | Keine Tatsache, die das Buch später widerlegt. Theos Angst bleibt (*„in die Wohnung, in der ein totes Mädchen –“*), als Angst, nicht als Behauptung. |
| P3 | **Kälte in der Brust zweimal** in Kap. 7 | **Schritt 4** (zwei Abschnitte aus altem Kap. 6 und 7 zusammengelegt) | Zweite Stelle → *„Nora fröstelte. Kurz. Wie ein Eiswürfel im Nacken.“* Der erste Ersatz „Ein Schauer lief Nora über den Rücken“ wurde **verworfen**: Fast derselbe Satz steht in Kap. 8 (Z.1632). | Regel 3 |
| P4 | Kap. 6: Theo *„Also hat sie es bei der nicht geschafft“*, und Nora sagt sofort fast dasselbe | **Schritt 4** (neu geschriebene Zeilen) | Theos Zeile gestrichen | Doppelte Aussage |
| P5 | Kap. 4: „Kreide“ zweimal in zwei Sätzen | **Schritt 4** (Kürzung) | „Ein Lehrer, der Brüche erklärte.“ | Echo |
| P6 | Kap. 7: *„Etwas Schweres legte sich auf Noras **Brust**“* bei einer dritten Brust-Formulierung im selben Kapitel | Original + Zusammenlegung | „auf Noras Schultern“ | Echo |

### Bewusst NICHT geändert

| Stelle | Warum nicht |
|---|---|
| Kap. 7: *„Kondenswasser … Am Nachmittag“*, obwohl Mama „gegen sechs“ zurück ist | Später Nachmittag im Juli. Keine Leserin merkt hier eine Uhrzeit. Eine Änderung brächte nichts. |
| Kap. 7: *„Du meinst in die Wohnung, in der ein totes Mädchen –“* | Theos **Angst**, keine Behauptung. Der Satz bricht ab. |
| Kap. 8: Die „Flurtür“ knallt, obwohl die Kinder im Flur stehen, *„dahinter der leere Flur“* | **Alter Fehler**, nicht aus Schritt 4. Wie die Räume liegen, ist unklar, aber für die Szene nicht wichtig. Minimal-Regel: nicht anfassen. Notiert für eine spätere Logik-Runde. |
| Kap. 6: Theo „*Gesundheit.*“ bei „Mikrofiche“, „Kapitel eins von *Wir hätten zu Hause bleiben sollen*“ | Humor nach Grusel. Das Skript zur vierten Wand meldet nichts. Theo spricht über einen Film, nicht über das Buch. |
| Kap. 5: Schattens Foto-Szene, Kinderschritte | unverändert stark |

### Kontrolle

| Prüfung | Ergebnis |
|---|---|
| `pruefe_band1_umbau.py --basis cc22b11 --schritt 4` | ✅ alle harten Prüfungen bestanden (+14 W: Kap. 8 +23 für den Mama-Satz, Kap. 4/6 −10) |
| gegen `4e983cf` | ✅ 27.179 → 22.703 W; Stimme +2 % / +10 % |
| K8 | ✅ 0 neue Fakten zu Linas Tod. P2 **entfernt** eine falsche Ortsangabe, fügt keine hinzu. |
| K6 Kapitelenden | ✅ unverändert |
| `pruefe_logik.py 1` | 8 Kandidaten, keine neuen |
| Regel 3 (neue Formulierungen im ganzen Buch gesucht) | „fröstelte“, „Wie ein Stein“, „erster Gedanke“, „auf den Beinen“, „früh schlafen“: je 1× |
| Kapitel-Dateien | neu erzeugt, 0 Abweichungen |
| Doku | Zeitlinie Kap. 7 in `Die_Geisterspuerer_Author_Info.md` |

---

## Nachprüfung Schritt 5 (auf Wunsch des Autors) · 2026-10-10

Basis: `15fbd15`. Gelesen: **Kap. 10 und 12 vollständig**. Gegengeprüft mit Kap. 1–11 (Bellen),
Kap. 9 (Tagebuch-Inhalt), Kap. 11 (Rückbezug „Ärmel“), Kap. 13–14 und dem Spielbuch-Material
(Titel).

### Was an Schritt 5 stimmt und bleibt (mit Beleg)

| Änderung | Prüfung | Urteil |
|---|---|---|
| **Handylicht statt „Theo ist weg“** (Kap. 10) | Ist es nur ein **anderer** Fehlalarm? Nein. „Theo ist weg“ löste sich in „war nichts“ auf. Das Licht dagegen bleibt **unerklärt** (80 % Akku, „Sie sagte nichts“) und steigert sich: Licht aus → Winseln → Kratzspuren → Präsenz → Fußspuren. Kap. 11 bezieht sich jetzt darauf (*„Du hast dich eben im Keller an meinem Ärmel festgekrallt“*). | bleibt |
| **Theos Kino-Witz** statt „offiziell festhalten“ | Nora antwortet wie im Original (*„Wir sind nicht in einem Film.“* – *„Im Film gibt es wenigstens Hintergrundmusik“*), der Dialog bleibt geschlossen. Passt zu Theos Film-Bezügen (Kap. 3: *„So fangen alle Horrorfilme an“*). | bleibt |
| **„Neue Regel: keine Keller mehr … Auch nicht zum Getränkeholen.“** | Passt zu Kap. 11: Theo will weitermachen, aber nicht in den Keller. Kein Widerspruch, eher eine Pointe. | bleibt |
| **„so noch nie“** (Winseln) | Der Widerspruch ist mit **einem** Wort gelöst (Kap. 2/8 winselt Schatten schon) | bleibt |
| **Tagebuch zusammengefasst** (Kap. 12) | Jede Zusammenfassung stimmt mit Kap. 9 überein (Geburtstag/lila Tinte, Luna/Stock, Sterne/Dach, kaltes Zimmer, Kratzen, *Einbildung*). *„Niemand glaubt mir“* ist ein wörtliches Zitat (19. Oktober). „Alles. Jedes Wort.“ greift Noras Ankündigung im selben Kapitel auf. | bleibt |
| **Schatten schaut auf die leere Stelle neben dem Bett** | Ein leiser Hinweis auf Lina, ohne neuen Fakt. Passt zu Schattens Rolle (er spürt, sie sehen nicht). | bleibt |
| **Titel „Bitte“** | Das Wort steht im Kapitel an den Fenstern, Theo nennt es ausdrücklich. Kein Kapitel der Serie heißt so. „Konfrontation“ im Spielbuch-Material (`moral_map.md`) ist ein **allgemeines Wort**, kein Kapitelverweis (geprüft). | bleibt |
| *„Seit sie ihn kannten, hatte Schatten nie gebellt“* | Kap. 1 sagt ausdrücklich *„Er bellte nicht“*. Das „Bell“ in Kap. 6 ist Theos Aufforderung. Stimmt. | bleibt |

### Gefundene Probleme

| # | Problem | Herkunft | Eingriff | Warum besser |
|---|---|---|---|---|
| P1 | **Ärmel zweimal neu gepackt** in Kap. 10: beim Lichtausfall *„Seine Hand fand ihren Ärmel und krallte sich fest“*, später *„Sie spürte seine Hand an ihrem Ärmel, die sich festhielt“* | **Schritt 5** (Lichtausfall) trifft auf das Original | Zweite Stelle → *„Seine Hand hielt noch immer ihren Ärmel fest.“* | Aus einer Wiederholung wird eine **Fortsetzung**: Theo lässt seit dem Dunkel nicht mehr los. Das trägt Kap. 11 (*„festgekrallt“*). |
| P2 | **Schwanzklopfen zweimal in Kap. 12:** mein neuer Satz (Z.135) und das **unveränderliche** Kapitelende (*„Sein Schwanz schlug einmal auf den Boden“*), dazu Kap. 14 | **Schritt 5** | Mein Satz gestrichen. Schatten schaut auf die leere Stelle und legt den Kopf ab. | Das Kapitelende ist tabu, also muss meine Stelle weichen. Das Bild der leeren Stelle wirkt ohne den Zusatz stärker. Kap. 14 behält es, dort trägt es Bedeutung („Als hätte er etwas wiedererkannt“). |
| P3 | Theo: *„in dem vor fünfzig Jahren ein Mädchen **verschwunden** ist“*. Lina war nicht verschwunden, sie starb (Zeitungsartikel Kap. 6, Kanon Z.278: *„dort starb Lina“*). | Original, nicht Schritt 5 | → *„gestorben ist“* | Ein Wort. Theo selbst sagt in Kap. 9 *„Und sie ist nicht wieder hochgekommen“*. Kein neuer Fakt (K8 grün). |

### Bewusst NICHT geändert

| Stelle | Warum nicht |
|---|---|
| *„Wie Blut. Wie alte Münzen.“* (Kap. 10), *„Wie Blut nach einem Biss auf die Wange“* (Kap. 5), *„wie Blut in eingeschlafene Hände“* (Kap. 12) | In der Nachprüfung von Schritt 2 habe ich *„Tinte wie getrocknetes Blut“* ersetzt. **Ist das jetzt inkonsequent?** Nein. Dort war es ein **Bild** von Blut, das man sieht und das Gruselgewicht trägt. Hier sind es ein **Geschmack** (den jedes Kind vom Zahnwechsel kennt) und ein Körpergefühl. CLAUDE.md meint *„blood/decay/body horror“*, also Szenen. Das sind keine. |
| Zwei Bilder für die weichende Kälte in Kap. 12 (Eisblock, Welle) | Sie stehen für zwei Phasen (Beginn, Fortschritt). Schritt 5 hat sie aus dem Original übernommen, ein Echo ist das nicht. |
| Fehlalarm „Theo ist weg“ in **Kap. 5** | Er ist jetzt der einzige seiner Art und legt Noras Regel *„Nicht allein. Nicht hier.“* an, die Kap. 15 wieder aufnimmt (*„Keiner geht allein irgendwohin“*). |
| *„Die Kälte traf sie wie ein Schlag“* (Kap. 12) ↔ *„Die Kälte traf Nora wie ein Schlag“* (Kap. 9) | Alt, drei Kapitel auseinander, nicht aus Schritt 5. Notiert, nicht angefasst (Minimal-Regel). |

### Kontrolle

| Prüfung | Ergebnis |
|---|---|
| `pruefe_band1_umbau.py --basis 15fbd15 --schritt 5` | ✅ alle harten Prüfungen bestanden (Kap. 10 −2 W, Kap. 12 −7 W) |
| K9 Schritt 5 | „offiziell festhalten/protokoll“ 2×, datierte Tagebuch-Zitate 0× |
| K6 Kapitelenden | ✅ unverändert (das Ende von Kap. 12 war der Grund für P2) |
| K8 | ✅ 0 neue Fakten, Faber 0 |
| gegen `4e983cf` | ✅ 22.689 W; Stimme +2 % / +10 % |
| `pruefe_logik.py 1` | 8 Kandidaten, keine neuen |
| Kapitel-Dateien | neu erzeugt, 0 Abweichungen |

---

## Nachprüfung Schritt 6 (auf Wunsch des Autors) · 2026-10-10

Basis: `cd8486b`. Bei jedem Ein-Satz-Eingriff wurde **der ganze Abschnitt drumherum** gelesen (Ende
Kap. 3 und Anfang Kap. 4, Anfang Kap. 11, Kap. 13). Kleine Korrekturen erzeugen leicht neue
Widersprüche im Umfeld. Dazu gehört die Frage, ob die Endabnahme die Logik-Kandidaten zu Recht
abgetan hat.

### Prüfung der drei Korrekturen aus Schritt 6

| # | Korrektur aus Schritt 6 | Prüfung | Urteil |
|---|---|---|---|
| X6 | *„Nora stellte die Tasse ab“* → *„Nora stieg über die Scherben“* | **Neuer räumlicher Fehler:** Die Scherben liegen *„hinter ihr“*, sie steht vor dem Fenster und geht dann *„zum Fenster“*. Über etwas zu steigen, das hinter ihr liegt, ergibt keinen Sinn. | **Ersetzt** durch *„Nora ließ die Arbeitsplatte los.“* Das greift zwei Absätze vorher auf (*„Ihre Finger schlossen sich um die Kante der Arbeitsplatte“*). Logische Bewegung: festhalten → loslassen → zum Fenster → bei Schwindel wieder greifen (Z.710). |
| X3 | *„rot vom Weinen am Vortag“* → *„rot vom Weinen“*; *„gestern Angst vor dem Kellerlicht“* → *„eben im Keller an meinem Ärmel festgekrallt“* | Theo weinte in Kap. 9 am selben Abend, das passt. Der Ärmel passt seit der Nachprüfung von Schritt 5 genau (Theo hält ihn ab dem Lichtausfall fest). „Tageslicht“ beim Verlassen des Kellers passt zu einem Juli-Abend. | **Bleibt** |
| X1 | *„was ich in den Sommerferien gemacht habe“* → *„was ich so in meiner Freizeit mache“* | Widerspruch weg, aber **der Witz ist schwächer geworden**: „Was ich in den Sommerferien gemacht habe“ ist das Aufsatzthema, das jedes Kind kennt, „Freizeit“ ist blass. Seit der Nachprüfung von Schritt 2 steht fest: Diese Nacht geht von Freitag auf Samstag. | **Ersetzt** durch *„Falls die Lehrerin am Montag fragt, was ich am Wochenende gemacht habe.“* Die Erzählrunde am Montag ist genauso bekannt **und** passt zur Zeitlinie. |

### Selbstkorrektur: Endabnahme

In der Endabnahme (Schritt 7, Punkt 2) habe ich *„Sie hatten sie gestern offen gelassen“* und
*„Wie der Raum gestern“* (Kap. 3) mit **„passt: nach Mitternacht“** abgetan. **Das war zu bequem.**
Der Wecker zeigt 23:47 (Kap. 2), Nora geht direkt danach hoch, und der Besuch oben war **am selben
Nachmittag**. Für eine Zwölfjährige, die noch nicht geschlafen hat, ist das „heute“. Ein Leser
stolpert über „gestern“.

| Stelle | Eingriff |
|---|---|
| *„Sie hatten sie gestern offen gelassen.“* | → *„Sie hatten sie am Nachmittag offen gelassen.“* |
| *„Kalt. Eiskalt. Wie der Raum gestern. Wie der Raum, den Schatten nicht betreten wollte.“* | *„Wie der Raum gestern.“* gestrichen (Minimal-Regel Stufe 3). Der zweite Vergleich sagt dasselbe genauer. |

**Lehre für weitere Prüfungen:** Ein Kandidat aus dem Logik-Skript wird erst abgehakt, wenn die
Begründung **am Text** steht (hier: Uhrzeit Kap. 2 + Besuch Kap. 2). „Klingt plausibel“ reicht nicht.

### Bewusst NICHT geändert

| Stelle | Warum nicht |
|---|---|
| „Arbeitsplatte“ 4× in Kap. 4 | Drei davon sind **eine Bewegung** (greifen – loslassen – wieder greifen), keine Wiederholung. Die vierte ist eine andere Szene am Nachmittag. |
| Theo kommt **barfuß** in die Küche mit Scherben | Er bleibt an der Tür stehen, und Nora räumt die Scherben später auf. Das Original ist hier stimmig. |
| *„Keine Reaktion wie gestern Nacht“* (Kap. 4), *„Sie waren gestern daran vorbeigegangen“* (Kap. 15) | Beide stimmen: Morgen nach der Nacht bzw. Samstag nach dem Freitag. |
| *„Sein Fell sträubte sich vom Nacken bis zum Schwanz“* 2× (Kap. 2 und 11) | Alt, neun Kapitel auseinander, kein Widerspruch. |

### Kontrolle

| Prüfung | Ergebnis |
|---|---|
| `pruefe_band1_umbau.py --basis cd8486b` | ✅ alle harten Prüfungen bestanden (Kap. 3 −3 W, Kap. 13 −2 W) |
| gegen `4e983cf` | ✅ 22.684 W; Stimme +2 % / +10 % |
| `pruefe_logik.py 1` | **8 → 6** Kandidaten (beide falschen „gestern“ in Kap. 3 entfallen). Die übrigen 6 einzeln begründet (s. o. und Endabnahme). |
| K6 / K8 | ✅ Kapitelenden unverändert; keine neuen Fakten, Faber 0 |
| Regel 3 | „am Nachmittag“, „Wochenende“, „Lehrerin“: je 1× |
| Kapitel-Dateien | neu erzeugt, 0 Abweichungen |

---

## Gesamtanalyse nach allen Nachprüfungen · 2026-10-10

Stand: `6482afb`. Verglichen mit der Fassung vor dem Umbau (`4e983cf`). Alle 16 Kapitel sind in der
aktuellen Fassung gelesen (Kap. 1–3 und 9 seit der ersten Lesung bis auf Anführungszeichen und
„gestern“ unverändert).

### Kürzung

| | vorher | nachher | Änderung |
|---|---|---|---|
| Wörter | 27.179 | **22.684** | **−4.495 (−16,5 %)** |
| Kapitel | 18 | **16** | −2 |
| Ø Wörter je Kapitel | 1.510 | 1.418 | −6 % |
| Seiten (KDP, geschätzt über LibreOffice-Verhältnis) | 186 | ≈ 158 | ≈ −15 % |
| Dialoganteil gesamt | 24 % | 24 % | ± 0 |
| Text nach Linas Befreiung | 7.446 W (27 %) | 3.464 W (15 %) | −54 % |

**Wo gekürzt wurde:** fast ganz im Schluss (Kap. 14–18 → 14–16: −3.982 W) und in Zone A (Kap. 4–7:
−563 W). Zugefügt: Kap. 13 (+96, Lina-Frage), Kap. 8 (+23, Mama), Kap. 5 (+45, Lina-Zettel).
**Kap. 1–3, 9, 11 sind praktisch unverändert.** Das war Absicht: Dort lagen keine Absprungzonen.

### Spannungskurve (Raster wie Plan Abschnitt 2: Neues 0–3, Gefahr 0–3, Gefühl 0–2, Sog 0–2)

| Kap. neu | Inhalt | Punkte | (alt) |
|---|---|---|---|
| 1 | Ankunft, Hund, „SILBER“ | 7 | 7 |
| 2 | eiskalter Raum, Name, Klopfen | 7 | 7 |
| 3 | nachts oben, Tür zu, HILF | 7 | 7 |
| 4 | HILF, Schule (gekürzt), HIER | 6 | 6 |
| 5 | Arbeitszimmer, Lina-Zettel, Foto, Kinderschritte | 8 | 8 |
| 6 | **eine** Bibliothek: Silber + Lina + Adresse | **7** | 5 |
| 7 | Friedhof-Blick, VERGISS NICHT, Kratzen | 7 | 7 |
| 8 | Wand, Türknall, Tagebuch | 8 | 8 |
| 9 | Tagebuch | 7 | 7 |
| 10 | Keller: Licht aus, Präsenz, Fußspuren | 9 | 9 |
| 11 | Entscheidung, Notizbuch, „der Erste“ | 6 | 6 |
| 12 | „Bitte“: Fenster, Vorlesen | 6 | 6 |
| 13 | Befreiung, Lina-Frage | 5 | 5 |
| 14 | Karte, GRAVEN, blaues Licht → Friedhof, unmögliche Tinte | **6** | 4 |
| 15 | Friedhof: Raureif, Gestalt, Tor; Nora entscheidet; Umschlag | **8** | 6 / 3 |
| 16 | Brief, Warnung „an uns“, Nacht, Raureif auf der Karte | **7** | 4 / 4 |

⚠️ **Selbstkorrektur:** In der Endabnahme stand für Kap. 6 eine **8**. Mit dem Raster sind es **7**.
Die emotionale Verarbeitung der Adresse ist mit Schritt 4 nach Kap. 7 gewandert (Gefühl 1 statt 2).

```
        alt (18 Kap.)                      neu (16 Kap.)
K 1  ███████   7                    K 1  ███████   7
K 2  ███████   7                    K 2  ███████   7
K 3  ███████   7                    K 3  ███████   7
K 4  ██████    6                    K 4  ██████    6
K 5  ████████  8                    K 5  ████████  8
K 6  █████     5                    K 6  ███████   7
K 7  ███████   7                    K 7  ███████   7
K 8  ████████  8                    K 8  ████████  8
K 9  ███████   7                    K 9  ███████   7
K10  █████████ 9  ← Höhepunkt 56 %  K10  █████████ 9  ← Höhepunkt 64 %
K11  ██████    6                    K11  ██████    6
K12  ██████    6                    K12  ██████    6
K13  █████     5  ← Lina frei 73 %  K13  █████     5  ← Lina frei 85 %
K14  ████      4                    K14  ██████    6
K15  ██████    6                    K15  ████████  8
K16  ███       3                    K16  ███████   7  ← Ende
K17  ████      4
K18  ████      4  ← Ende
```

| Kennzahl | alt | neu |
|---|---|---|
| Ø Punkte je Kapitel | 6,06 | **6,94** (+0,9, ≈ +15 %) |
| Ø Punkte, gewichtet nach Wörtern | 6,02 | **6,91** |
| **Textanteil in Kapiteln mit ≤ 4 Punkten** | **22,5 %** | **0 %** |
| Ø nach dem Höhepunkt | 4,75 | **6,33** |
| Ø nach Linas Befreiung | 4,20 | **7,00** |
| Höhepunkt der Gefahr bei | 56 % | 64 % |
| Lina frei bei | 73 % | 85 % |
| Letztes Kapitel | 4 (blaues Licht wiederholt) | **7** (neues Bild, zeigt auf Band 2) |

### Wie belastbar ist „spannender“?

- **Belastbar (Fakten, am Text gezählt):** Die Wiederholungen W1–W11 sind beseitigt oder auf ein
  Mal reduziert. 14 Logik- und Zeitfehler sind behoben (X1–X6 und die Funde der Nachprüfungen).
  Der Schluss ist halb so lang. Kein Kapitel liegt mehr unter 5 Punkten. Das Buch endet auf einem
  neuen Haken statt auf einer Wiederholung.
- **Nicht belastbar (Einschätzung):** Die Punktzahlen stammen von **dem, der die Änderungen
  geschrieben hat**. Das Raster misst weder Humor noch Sprache. „+15 % spannender“ ist eine Aussage
  über dieses Raster, **nicht** über Kinder.
- **Nicht vorhersagbar:** Wie stark die Durchlesequote zu Band 2 steigt. Der Umbau beseitigt die
  beiden Absprungzonen, die der Text erkennen ließ. Ob Kinder dort wirklich ausgestiegen sind, zeigen
  erst **Testleser** (Kurve) und **QR-Scans** (wie viele kommen bis zum Ende).

### Was nicht besser geworden ist (bewusst oder offen)

| Stelle | Stand |
|---|---|
| **Kap. 11–13 (6/6/5)** | Eine flache Strecke zwischen Keller und Befreiung bleibt. Kap. 13 ist **gewollt** ruhig (Abschied). Kap. 11/12 wären der nächste Ansatzpunkt, falls die Testleser hier aussteigen. |
| Dialoganteil Kap. 2, 5, 10, 12, 13 (14–17 %) | Nicht Ziel des Umbaus. Band 1 ist der Stimmen-Maßstab, und der Stimmen-Prüfplan sagt ausdrücklich: Dialog-% ist kein Ziel. |
| Linas Tod | **Bewusst** nur als Gefühl beantwortet (wegen Band 4). Testleser-Frage 1 prüft, ob das Kinder stört. |
| Kap. 14–16 je ~1.150 W | Unter dem Richtwert von ~1.200, im Rahmen von Band 3/4. |
| Kap. 8 „Flurtür“ (Lage der Räume unklar), Theo „hundert Jahre alt“ (Haus von 1826) | Alt und klein, notiert. Theos Zahl ist eine Kinderschätzung. |
| Offen für den Autor | Testleser, Schritt 1 (Anhang/QR), KDP (Seiten −15 % > 10-%-Regel, Klappentext „16 Kapitel“, Cover-Rücken), Spielbuch-Abgleich |

---

## Kleine Verbesserungen Kap. 11–13 · 2026-10-10

Basis: `47a4ab1`. Auftrag: nur kleine Änderungen, die das Buch besser machen; jede begründet und
hinterfragt. Gesucht wurde nach dem, was im Raster Punkte kostet: schwacher Sog, **Vorbereitungen
ohne Wirkung**, Angst ohne Einlösung.

### Umgesetzt

| # | Befund (Beleg) | Änderung | Warum besser | Risiko geprüft |
|---|---|---|---|---|
| K1 | **Kap. 11 endet schwach:** unbestimmtes Klicken, Knurren, dann Schlaf. Im Raster Sog 1 von 2, das schwächste Kapitelende des Buches. | Nach dem Klicken: Schatten starrt *„Zur letzten Tür. Zum kalten Zimmer.“* – *„Dann hörten sie es. Klopf. Klopf. Klopf. Pause. Klopf. Klopf. Klopf.“* | Das Klopfen ist das Signal, mit dem das Buch begann (Kap. 2/3), jetzt kommt es gesteigert zurück. Es **begründet** im Nachhinein Linas „OBEN“ (Kap. 12) und warum sie genau in diesem Zimmer erlöst wird (Kap. 13). Das war die offene Frage O4, **ohne neuen Fakt**. | Kap. 13: *„die Tür, die immer geschlossen gewesen war. Das kalte Zimmer“* passt. Das Klopfen kommt in Kap. 2/3 *„aus Frau Silbers Wohnung“* (passt). Ein Kapitelende zu ändern ist hier ausnahmsweise begründet: Die Tabu-Regel schützt starke Enden, dieses war das schwächste. |
| K2 | Nach K1 fehlt der Übergang: Klopfen, und im nächsten Satz liegt Nora im Bett. | Kap. 12: *„Am Abend hatte das Klopfen aufgehört, bevor sie sich getraut hatten, die Tür zu öffnen. Nora hatte lange wach gelegen.“* | Logik. Erklärt, warum die Tür in Kap. 13 *„immer geschlossen gewesen“* war und jetzt *„offen stand“*. | Der erste Satz von Kap. 12 ist unverändert (Anschlussstelle) |
| K3 | **Kap. 12: angelegte Angst ohne Einlösung.** Nora: *„Was, wenn es alles schlimmer machte? Was, wenn die Kälte stärker zurückkam?“* Danach wurde es nur wärmer. | Beim Lesen der dunklen Seiten wird die Kälte **zuerst stärker**: Eisblumen am Fenster, steife Seiten, Theo: *„Nora. Es wird schlimmer.“* Nora liest weiter, **dann** weicht die Kälte. | Die Angst wird eingelöst, und der Höhepunkt des Kapitels bekommt eine Schwelle: Die Wende wird erkämpft, nicht geschenkt. | **Erster Entwurf verworfen:** *„neues Kondenswasser … verschluckte die Wörter“* widersprach dem Kapitelende (*„Die Wörter waren verblasst … als hätte die Wärme sie weggewischt“*). Eisblumen tauen dagegen genau zu dem Wasserstreifen, in dem „DANKE“ erscheint. |
| K4 | **Kap. 13: Vorbereitung ohne Wirkung.** *„Soll ich es mitnehmen?“ – „Nimm es mit.“* Danach kommt das Tagebuch nicht mehr vor. | Theo legt es neben das Licht: *„Es gehörte ihr.“* Das Licht gleitet *„über den Einband des Tagebuchs“*, bevor es geht. | Die Vorbereitung hat jetzt eine Wirkung. *„Es gehörte ihr“* greift Noras Gedanken vom Kapitelanfang auf (*„Das Tagebuch gehörte Lina“*). | **Erster Entwurf verworfen:** *„Als würde er es ihr zurückgeben“* stand direkt vor *„Als würde er jemanden verabschieden“* (zweimal „Als würde er“). Der Verbleib des Tagebuchs danach ist offen. Das stört nicht, kein späterer Text widerspricht (B2/B5 erwähnen es nur allgemein). |

### Verworfen (mit Grund)

| Idee | Warum nicht |
|---|---|
| Drittes Notizbuch-Zitat in Kap. 11 kürzen (*„versteht. Nicht nur kennt.“*) | Es trägt das Thema, auf das Band 4/5 aufbauen (*„Bei Lina … hatte Verstehen den Geist gehen lassen“*). Wiederholt sich nur scheinbar. |
| Gefahr in Kap. 13 einbauen | Kap. 13 ist der Abschied. Gefahr würde den emotionalen Höhepunkt stören. Ein ruhiges Kapitel nach dem Höhepunkt ist Absicht. |
| Ende Kap. 12 („DANKE. OBEN.“) schärfen | Es trägt schon und wird durch K1 sogar stärker (das Klopfen kam von oben). |

### Kontrolle

| Prüfung | Ergebnis |
|---|---|
| `pruefe_band1_umbau.py --basis 47a4ab1` | ✅ bestanden (+97 W: Kap. 11 +22, Kap. 12 +54, Kap. 13 +21) |
| gegen `4e983cf` | ✅ 22.781 W (−16,2 %); Stimme: Und-Anfänge +2 %, Kurzabsätze **+12 %** (Korridor ±15 %, im Auge behalten) |
| K6 | Nur das Ende von Kap. 11 geändert (begründet, s. K1) |
| K8 | ✅ 0 neue Fakten, Faber 0 |
| `pruefe_logik.py 1` | 6 Kandidaten, keine neuen |
| Regel 3 | „Eisblumen“, „Es wird schlimmer“, „bevor sie sich getraut“, „Zur letzten Tür“, „Es gehörte ihr“: je 1× |
| Kapitel-Dateien | neu erzeugt, 0 Abweichungen |

### Neubewertung (ehrlich)

| Kap. | vorher | nachher | warum |
|---|---|---|---|
| 11 | 6 | **7** | Sog 1 → 2 (Klopfen statt Klicken) |
| 12 | 6 | 6 | Mehr Spannung beim Lesen, aber die Gefahr stand schon auf 2 (Gestalt im Flur). Das Raster bildet die Verbesserung nicht ab. |
| 13 | 5 | 5 | Das Gefühl stand schon auf 2. K4 verbessert die Stimmigkeit, nicht die Punktzahl. |

**Ø je Kapitel 6,94 → 7,0.** Das ist bewusst wenig. Der Gewinn dieser Runde liegt vor allem darin,
dass **drei Vorbereitungen jetzt eine Wirkung haben** (Klopfen → OBEN → Zimmer; Noras Angst →
Kälte wehrt sich; Tagebuch mitnehmen → zurückgeben). Das misst das Raster nicht, Leser
spüren es aber als „alles passt zusammen“.

---

## Schritt 1 · Anhang und Brücke zu Band 2 · 2026-10-10

Nur die Bau-Skripte, **kein Manuskripttext**. Neu: `Scripts/band1_anhang.py` (gemeinsame Daten für
Taschenbuch und eBook), `Scripts/pruefe_band1_anhang.py` (Prüfung am gebauten DOCX),
`Band1/Cover/band2_vorderseite_leseprobe.jpg` (Vorderseite aus `Band2/Cover/Bilder/v1.png`,
dieselbe Datei nutzt das A+-Content von Band 2).

### Neue Reihenfolge des Anhangs

| # | Seite | Warum |
|---|---|---|
| 1 | „Wie geht es weiter?“ · „Elf Kreise auf Frau Silbers Karte. Der nächste liegt am alten Friedhof.“ · Cover Band 2 | Direkt nach der letzten Seite ist die Neugier am größten. Beide Sätze stimmen mit Band 1 (Kap. 14–16) und Band 2 (S. 1) überein. |
| 2 | **Leseprobe** Band 2, Kap. 1 (37 Absätze, 480 Wörter) | Wird beim Bau aus `Manuskript_Band2_Komplett.md` gelesen und geprüft, nicht abgetippt. |
| 3 | „Wie es weitergeht, steht in …“ · **QR-Code zu Band 2** · Zeile für Eltern | Taschenbuch: QR. eBook: klickbarer Link. |
| 4 | Rezensionsbitte mit QR (Text unverändert, passt jetzt auf eine Seite) | Kommt nach Band 2: Wer bis hier liest, mochte das Buch. |
| 5 | Bandliste, Mitmach-Buch in einem Satz, andere Serien gekürzt auf Titel + Alter | |

### Entscheidungen mit Begründung

- **Leseprobe endet bei** „Schatten saß auf dem Gehsteig. Vier Pfoten fest auf dem Pflaster. Er war
  keinen Millimeter durch das Tor getreten.“ Starker Haken, derselbe wie im Band-2-Klappentext.
  **Nicht weiter**, weil danach „Er ist noch nie …“ / „War er nicht.“ kommt. In Band 1 hat sich
  Schatten schon geweigert (Kap. 2, Kap. 5 sagt es ausdrücklich).
- **Ein Absatz ausgelassen:** „Er hatte recht. Von der Straße aus sah man nur die Bäume — hohe, alte
  Kastanien …“. In Band 1, Kap. 15, sehen die Kinder von der anderen Straßenseite Grabsteine und eine
  Gestalt. Direkt hintereinander gelesen fällt das auf. Ohne den Absatz liest sich die Stelle glatt.
- **Plan-Kontrolle (b) aufgehoben** („kein Herbst, kein ‚letzten Monat‘“): Sie sollte den Widerspruch
  zum alten Schlusswort „Morgen“ verhindern. Das gibt es nach Schritt 2 nicht mehr, und Band 2 sagt
  beides auf Seite 1. Die Regel hätte jede echte Leseprobe blockiert. Ersetzt durch: keine Reste der
  erfundenen Leseprobe.
- **Ornament am Buchende entfernt:** Das Manuskript endet auf „---“ + ENDE-Marker. Beide Renderer
  ließen das „---“ stehen, also stand hinter dem letzten Satz des Buches ein Ornament (war schon in
  der veröffentlichten Fassung so). Jetzt wird ein Trenner am Textende immer entfernt.
- **eBook:** erfundene Leseprobe („Heinrich M. – 1847“, „vor drei Wochen“, „mitten im Juli“ am
  Friedhof) und „Erscheint 2026“ ersetzt. Links statt QR-Codes.
- **QR-Ziel:** Solange die Domain fehlt, führt der Code direkt auf `amazon.de/dp/B0GV8R8QJ6`.
  Umstellen: in `band1_anhang.py` `WEITERLEITUNG_BAND2` setzen → `build_qr_rezension.py` erzeugt den
  Code automatisch neu.

### Kontrolle (am gebauten DOCX, `pruefe_band1_anhang.py`)

| | Taschenbuch | eBook |
|---|---|---|
| (a) Leseprobe wörtlich, vollständig, in Reihenfolge | ✅ | ✅ |
| (b) keine Reste der alten Leseprobe | ✅ | ✅ |
| (c) QR / Links | ⏳ QR „Band 2“ **fehlt** (s. u.); Rezensions-QR eingebettet ✅ | ✅ beide Links |
| (d) Anführungszeichen „ 926 / “ 926 / gerade 0 / doppelt 0 | ✅ | ✅ |
| (e) Fehl-Ornamente 0 (auch am Buchende) | ✅ | ✅ |
| Kapitel 16 + Leseprobe | ✅ | ✅ |

⚠️ **Der QR-Code „weiter zu Band 2“ konnte hier nicht erzeugt werden:** Die Umgebung kommt nicht an
PyPI (`qrcode`, `opencv` fehlen). Der Code-Pfad ist mit Attrappen durchgetestet (erzeugen, wieder
einlesen, zweiter Lauf „unverändert“), die echte Erzeugung läuft beim Autor:
`py Scripts/build_qr_rezension.py` → `py Scripts/build_taschenbuch_docx.py` →
`py Scripts/build_ebook_docx.py` → `py Scripts/pruefe_band1_anhang.py` (muss „ALLES BESTANDEN“
melden). Ohne den Code bricht der Taschenbuch-Bau ab; `--entwurf` setzt nur zum Seitenzählen einen
Platzhalter.

### Seitenzahl

LibreOffice-Proxy: 179 (Stand nach Schritt 7) → **181** (+2). Hochgerechnet ≈ **160 KDP-Seiten**
(181 ÷ 211 × 186). Die echte Zahl zeigt erst die KDP-Vorschau → dann Cover-Rücken.
