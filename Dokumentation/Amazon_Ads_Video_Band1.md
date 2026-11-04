# Amazon-Video „Das Haus, das flüstert“ (Band 1, Staffel 1)

Stand 2026-11-04. Sponsored Brands Video, geplanter Start etwa 18.11. Quellen: vier Bildschirmaufnahmen
(`E:\Repos\App-Ideen\SmartInvoice\Marketing\Tiktok\video2\amazonVidAds\`), Bild für Bild im Sekundentakt ausgewertet.

## 1. Was die vier Videos zeigen

| | 1 Die verschwundene Insel | 2 Hase Hollywood | 3 Weil du ein wunderbarer Junge bist | 4 Unglaubliches Wissen |
|---|---|---|---|---|
| Länge (Schleife gemessen) | 25,2 s | 45,0 s | 17,1 s | 26,4 s |
| Machart | animierte Grafik | gefilmtes Buch | eine Illustration, leicht bewegt | 5 Bilder als Diashow, je ~5 s |
| Einstieg | Behauptung: „Eine ganze Insel einfach weg“ | Buch und Satz, was es ist | Bild ohne Text | „Schluss mit öden Faktenlisten!“ |
| Text gesamt | rund 20 Wörter, groß | 1 Band am Anfang | nur Cover | rund 80 Wörter, oft klein |
| Inneres gezeigt | ja | ja, Hauptinhalt | nein | ja |
| Cover zu sehen | ja, mehrfach | am Schluss | fast durchgehend | fast durchgehend |
| Aufforderung | „Jetzt bestellen“ | keine | keine | keine |
| Eltern-Argument | keins | keins | über das Cover | Geschenk, Leselust, „ab 8“ |
| Sonstiges | CC, Pause | Lautsprecher aus | CC, Pause | Lautsprecher aus, Label „KI-generiert“ |

**Was das Material hergibt**
- Alle vier zeigen das Cover. Das ist die einzige Gemeinsamkeit ohne Ausnahme.
- Es gibt keine feste Formel: 17 bis 45 Sekunden, von Hochglanz bis Diashow.
- Einfache Formate kommen durch: Video 3 und 4 sind mit wenig Aufwand gemacht und laufen als Anzeige.
- Wenig großer Text (1) liest sich besser als viel kleiner Text (4). Das ist unsere Einschätzung, keine Messung.
- Ecken sind belegt: oben rechts CC, unten rechts Pause und Lautsprecher, oben links teils ein Label.

**Was es nicht hergibt**
- Keines der vier ist Grusel, keines ein reines Textbuch.
- Es liegen keine Verkaufszahlen vor, nur Rang #8.809 bei Video 1. Welches Video gut läuft, ist **nicht belegt**.
  Auch mit Zahlen wäre der Anteil des Videos am Verkauf offen.

## 2. Idee

Die Kurzformel aus der Buchbeschreibung lautet: „Ein Wort im Kondenswasser. Ein Hund, der Geister spürt. Und ein Haus,
das nicht loslässt.“ Das aktuelle Cover enthält alle drei Teile. Das Video beginnt nah am Wort und fährt zurück, bis
aus dem Fenster das Buch wird. Der Betrachter sieht das Cover also nicht nur, er kommt dort an.

| Übernommen | von |
|---|---|
| Neugier im ersten Satz, klarer Schluss | Video 1 |
| Ruhe statt Tempo | Video 2 und 3 |
| Geringer Aufwand aus vorhandenem Material | Video 3 |
| Eltern-Argumente: Alter, Geschenk | Video 4 |

## 3. Skript

Format 16:9, 1920 × 1080, 18 Sekunden, stumm verständlich. Kein Kindergesicht, kein sichtbarer Geist.
Sprache: nur Texteinblendungen. Text nie in die vier Ecken, Rand mindestens 7 %.

| Zeit | Bild | Text | Zweck |
|---|---|---|---|
| 0:00–0:03 | Beschlagene Scheibe im Halbdunkel, kaltes Blau. Die Buchstaben **H I L F** erscheinen einzeln, wie von einem unsichtbaren Finger gezogen, unten läuft ein Tropfen | keiner | Bewegung und Frage, ohne lesen zu müssen |
| 0:03–0:06 | Dieselbe Scheibe, leichter Push-in | „Kondenswasser schreibt keine deutschen Wörter!“ / klein: Theo, 10 | Humor nimmt sofort die Härte, zeigt den Ton der Reihe |
| 0:06–0:09 | Überblendung auf das HILF-Fenster des Covers, Kamera fährt zurück: warme Fenster, ein blaues, die ganze Fassade | keiner | Der Moment der Idee: Aus dem Wort wird das Haus |
| 0:09–0:11,5 | Fahrt nach unten zu Nora, Theo und Schatten, alle von hinten, Nebel zieht | „Ein Hund, der Geister spürt.“ | Figuren und Besonderheit der Reihe |
| 0:11,5–0:14 | Dunkler Grund, Buch als Objekt fährt ein | „Kribbeln ja, Albträume nein.“ / „Für Kinder ab 10“ | Beruhigt Eltern, nennt das Alter |
| 0:14–0:18 | Buch rechts, Text links, Ende auf Dunkel für die Schleife | „Das Geschenk für mutige Leser“ / „Band 1 von 5 · Jetzt entdecken“ | Grund zum Kaufen, Hinweis auf die Reihe |

Rund 30 Wörter. Nach dem 24.12. wird die Zeile „Das Geschenk für mutige Leser“ durch „Der Auftakt der Reihe“ ersetzt.

### Belege

| Text | Quelle |
|---|---|
| HILF im Kondenswasser | Band 1, Kapitel 4; im aktuellen Cover als Fenster |
| „Kondenswasser schreibt keine deutschen Wörter!“ | Kapitel 4, Theo, wörtlich; auch in `DE_Basis` (gedruckte Fassung) |
| Theo, 10 | Reihenkanon Staffel 1 |
| Ein Hund, der Geister spürt | Verkaufssatz aus `KDP_Beschreibungen.md`, nicht als Zitat gesetzt |
| Kribbeln ja, Albträume nein | Reihenversprechen, `KDP_Beschreibungen.md` |
| ab 10, Band 1 von 5 | Cover, `KDP_Beschreibungen.md` |

## 4. Material

Nur ein neues Bild ist nötig. Der Rest kommt aus `Band1/Cover/Bilder/front_band1.jpg` (2186 × 3262), Schnitt, Text und
Buchstaben-Animation entstehen per ffmpeg und Python. Kein Videogenerator nötig.

Bildausschnitte aus dem Cover: Fassade unterhalb des Untertitels, Kinder und Hund im unteren Bereich, jeweils ohne
Titel und ohne Autorenzeile. Bei 1920 px Breite wird das Bild leicht hochskaliert; das Kontrollbild entscheidet, ob 1280 × 720
schärfer wirkt.

Bild-Prompt für den ersten Clip:

```text
Photorealistic close-up of an old wooden kitchen window pane seen from inside a dark room, in very dim cold
blue pre-dawn light. The whole glass is covered evenly with fine grey condensation fog, softly glowing blue
from behind. Peeling white paint on the wooden frame at the edges, a few tiny water droplets. The centre of
the glass stays smooth and empty. Quiet, slightly eerie, cinematic, shallow depth of field. Aspect ratio 16:9,
landscape. ABSOLUTELY NO letters, words, numbers, symbols, handprints, faces, people, or figures anywhere.
```

## 5. Selbstkritik

1. **Beweis fehlt.** Das Skript folgt Überlegung und Mustern, nicht belegten Verkäufen. Erst die Anzeige selbst liefert Zahlen.
2. **HILF kann Eltern irritieren.** Ein Hilferuf ohne Zusammenhang liest sich in einer Kinderbuch-Suche hart. Deshalb
   kommt der Witz schon nach 3 Sekunden. Wirkt es beim Test trotzdem zu hart, steht der Witz schon ab 0:01,5.
3. **Das Innere des Buchs fehlt bewusst**, obwohl drei von vier Videos es zeigen. Dort tragen es Illustrationen oder es ist
   Sachbuch-Inhalt. Eine Textseite verkauft in 18 Sekunden wenig, und „Blick ins Buch“ gibt es auf der Produktseite.
4. **Ein gemaltes HILF kann billig wirken.** Es muss zur Scheibe passen. Sieht der Test falsch aus, ist das ein Grund, doch einen
   bezahlten Clip zu erzeugen.
5. **Text gegen Ruhe.** 30 Wörter in 18 Sekunden sind vertretbar, aber das Limit. Beim Kürzen fällt zuerst „Theo, 10“.
6. **Amazon-Prüfung offen.** Regeln zu Grusel-Bildern bei Kinderbüchern, zu Pflichtton und zum Label „KI-generiert“ sind nicht geklärt.
   Beim Hochladen prüfen und mindestens 72 Stunden Reserve einplanen.
7. **Cover-Bild ist KI-erzeugt.** Falls Amazon eine Angabe verlangt, wird sie gemacht, nicht umgangen.

## 6. Prüfung vor dem Hochladen

- Ohne Ton und auf Handygröße ansehen: Ist nach 6 Sekunden klar, was das ist?
- Jede Texteinblendung langsam vorlesen: Reicht die Zeit?
- Liegt Text in einer Ecke? Dann versetzen.
- Kein Gesicht, kein Geist, kein Titelrest im Ausschnitt.
- Mindestens 6 und höchstens 45 Sekunden, 16:9, MP4.
