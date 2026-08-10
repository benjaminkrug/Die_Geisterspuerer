# Cover — S2-1 „Der Gast, der blieb"

> **Basis:** [`Dokumentation/Cover_Reihenstandard.md`](../../../Dokumentation/Cover_Reihenstandard.md)
> (Panel-Maße, Prompt-Blöcke A–E, Figuren-Grammatik) und
> [`Staffel2/PLAN_Staffel2.md`](../../PLAN_Staffel2.md) Abschnitt 10 (Staffel-2-Abweichungen).
> Nichts davon wird neu erfunden — dieses Blatt ergänzt nur das, was erst nach dem
> **fertigen Manuskript** entschieden werden konnte.
>
> ⚠️ **Kein Bild erzeugt.** Bildgenerierung ist hier nicht möglich; ebenso wenig laufen die
> Cover-Skripte (`PyMuPDF` und `Pillow` sind nicht installierbar). Dieses Blatt ist die
> vollständige Arbeitsvorlage: Motiv, Prompts, Zonen, Prüfliste.

---

## 1. Das Motiv — Kapitel 2 hat es bereits geschrieben

Der Staffelplan legte am 2026-08-07 fest: *„fremde Altbauwohnung, Geist als ‚Gast' gefangen"*.
Das war **vor** dem Manuskript. Jetzt existiert das Buch, und Kapitel 2 enthält eine
Komposition, die **alle acht Regeln der Reihen-Grammatik gleichzeitig erfüllt** — ohne dass
etwas dazuerfunden werden müsste:

> Die Tür zum Schrankzimmer stand einen Spalt offen. Kein Luftzug hätte sie so gerade und
> so still gehalten.
>
> Nora hielt den Atem an und sah hindurch.
>
> Für eine Sekunde, nicht länger, stand dort eine Gestalt. Ein Mann, grau und verschwommen
> wie durch Nebel gesehen. Der Rücken zu ihnen gewandt, den Kopf leicht gesenkt.

| Regel der Reihen-Grammatik | Wie K2 sie erfüllt |
|---|---|
| 1 Zwei Kinder + Hund von hinten, unteres Drittel | sie stehen im Flur vor der Tür |
| 2 Sie blicken **in eine Öffnung** hinein | der Türspalt |
| 3 Genau **eine** Lichtquelle in der Bildmitte | das vergitterte Fenster des Zimmers (K3), kaltes Licht durch den Spalt |
| 4 Schattens Auge als einziger lebendiger Punkt | er bleibt auf der Schwelle stehen (K2) — er ist im Bild, wo er hingehört |
| 5 Oberes Drittel ruhig | dunkle Flurwand und Türsturz |
| 6 **Nie ein klar erkennbarer Geist** | Herbert steht **mit dem Rücken zum Betrachter**, Kopf gesenkt — kein Gesicht, weil er sich abgewandt hat, nicht weil es kaschiert wurde |
| 7 Kein Blut, keine Fratze | ein alter Mann, der wegsieht |
| 8 Alles führt zur Bildmitte | Flur → Spalt → Schrank |

**Regel 6 ist der Punkt.** Auf allen bisherigen Covern musste die Gesichtslosigkeit
kaschiert werden. Hier ist sie **Handlung**: Herbert hat sich abgewandt, und genau das
erzählt das Buch — ein Mann, der zwölf Jahre lang nicht hingesehen hat.

### Warum das nicht mit Band 4 kollidiert

Band 4 hat ebenfalls eine Tür mit Lichtspalt. Der Unterschied trägt auch im
150-px-Thumbnail:

| | Band 4 | S2-1 |
|---|---|---|
| Tür | **zugemauert** — dahinter ist nichts | einen Spalt offen — dahinter ein Raum |
| Spaltlicht | **warmes Gold** | **kaltes Grau-Silber** |
| Im Spalt sichtbar | nichts | dunkler Schrank + graue Gestalt |
| Grundton | Blaugrau | **Graphit/Schiefer**, entsättigt |

### Die Staffel-Signatur: der Leine-Lichtfaden

Blass, kalt, dünn wie ein Draht: von **Herberts Brust** (K10: *„Er legte eine
durchscheinende Hand auf seine Brust. Hier. Immer hier."*) nach unten zu einem winzigen
Punkt an der **unteren rechten Ecke der Schranktür** — dort sitzt das Schloss.

Der Faden darf im Thumbnail verschwinden. Er ist der Reihen-Wiedererkennungsfaden für
S2-1 bis S2-4 und fehlt im Finale bewusst.

---

## 2. Technische Eckdaten

| | Wert |
|---|---|
| Format | **6 × 9 Zoll**, weißes Papier (Staffel-2-Standard, alle fünf Bände) |
| Seitenzahl (**geschätzt**) | **≈ 102** — aus 16.723 Wörtern bei Ø 163,5 W/Seite (Band 4: 164,2 · Band 5: 162,8) |
| Buchrücken bei 102 S. | 0,2297 Zoll = **5,83 mm** |
| Vollcover bei 102 S. | 12,480 × 9,250 Zoll = **3744 × 2775 px** @ 300 dpi |
| Vorderseite allein | mindestens **1838 × 2775 px** |

> ‼️ **Die Seitenzahl ist geschätzt und darf so nicht in den Druck.** Der Buchrücken hängt
> direkt daran. Erst das fertige Taschenbuch-PDF bauen, die **echte** Seitenzahl ablesen,
> dann `PAGES` im Cover-Skript setzen. Band 5s Vollcover hatte beim ersten Versuch einen
> **dreimal zu breiten** gemalten Buchrücken (5,84 % statt 1,88 % der Bildbreite) — KDP
> hätte mitten in die Rückenfläche gefaltet.

### Zonen (Staffel-2-Abweichung vom Reihenstandard)

```
  0 – 37 %   Kopfbereich  (Staffel 1: 0–30 %) — drei Textebenen statt zwei
 37 – 64 %   Mittelzone   (Staffel 1: 34–64 %) — Tür, Spalt, Schrank, Gestalt
 64 – 68 %   Übergang
 68 – 100 %  Figurenzone  (unverändert) — Nora, Theo, Schatten von hinten
```

**Sicherheitsränder oben/unten: 13 %** statt der 9 % aus Staffel 1 — bewusster Aufschlag
für alle fünf Staffel-2-Bände. Seitlich bleibt es beim zentralen 84 % der Breite.

### Die fünf Textzeilen

```
DIE GEISTERSPÜRER                              winzig, Stahlgrau #9aa6b0
DIE GEBUNDENEN · BAND 1                        1,6–1,8× Zeile 1, Stahlgrau
Der Gast, der blieb                            groß, Gold #dfb057, dominant
Ein Grusel-Abenteuer für Kinder ab 12 Jahren   klein
Benjamin Krug                                  klein
```

⚠️ **„ab 12 Jahren"**, nicht 10 — bewusste Staffel-2-Entscheidung.
⚠️ Umlautkontrolle Buchstabe für Buchstabe: **GEISTERSPÜRER** (Ü) und **für** (ü).

---

## 3. Prompt Vorderseite

> ### ★ Fassung 2 (2026-08-09) — nach dem ersten Bild umgeschrieben
>
> **Was Fassung 1 falsch machte, ist am Ergebnis ablesbar.** Sie enthielt nur die
> **negative** Regel *„Keep at least 13% of the height free of text at the TOP and at the
> BOTTOM"*. Ergebnis: Reihenzeile bei ~5 %, Autorenname bei ~2,5 % — beides unter dem
> technischen Minimum von 6 %.
>
> Der **Rückseiten**-Prompt derselben Sitzung hat seine Ränder dagegen gehalten. Der
> Unterschied: Er gibt **nummerierte Zonen mit positiven Positionsangaben** („Zone 1,
> centred, top 6-11%"), statt zu sagen, wo nichts hin soll. Genau das bekommt die
> Vorderseite hier.
>
> Drei Änderungen: **(1)** eine LAYOUT MAP mit Zone und Prozentposition für jede der fünf
> Zeilen · **(2)** die Randregel positiv formuliert plus ein *vergleichbarer* Anker
> („ein Band leeren Hintergrunds, mindestens doppelt so hoch wie die Großbuchstaben
> darunter") — Prozentzahlen allein setzt kein Bildmodell zuverlässig um · **(3)** eine
> Endkontrollliste, die Fassung 1 gar nicht hatte, die Rückseite aber schon.

```
========================================
READ THIS BLOCK FIRST - IT OVERRIDES ANY EARLIER CONTEXT
========================================

This cover belongs to the German children's series "DIE GEISTERSPÜRER"
(The Ghost Trackers). This is the FIRST book of its SECOND cycle, which
carries the additional series name "DIE GEBUNDENEN". It is NOT "Die
Herrenhaus-Detektive" and NOT any other series. Ignore any other book
series, title, manor house or branding from earlier in this conversation.

EXACTLY these five texts appear on the cover - no others, none invented:
  1. tiny series line : DIE GEISTERSPÜRER
  2. cycle line       : DIE GEBUNDENEN · BAND 1
  3. main title       : Der Gast, der blieb
  4. subtitle         : Ein Grusel-Abenteuer für Kinder ab 12 Jahren
  5. author           : Benjamin Krug

Line 2 is 1.6-1.8 times the cap height of line 1. Line 3 is by far the
largest and most dominant text on the cover, in warm gold (#dfb057).
Lines 1, 2 and 4 are steel grey (#9aa6b0).

Forbidden anywhere: any publisher name, imprint or logo; any badge, seal,
sticker, ribbon, banner or emblem; any age roundel; any painted frame or
border around the artwork; any word not in the five texts above.
========================================

════════════════════════════════════════
LAYOUT MAP - WHERE EACH LINE SITS
════════════════════════════════════════

Think of the image height as 100 units, top = 0, bottom = 100.

  0 - 13   EMPTY BAND. Plain dark hallway wall. NO text of any kind here.
 14 - 17   ZONE 1  series line   DIE GEISTERSPÜRER
 18 - 22   ZONE 2  cycle line    DIE GEBUNDENEN · BAND 1
 24 - 33   ZONE 3  main title    Der Gast, der blieb
 35 - 38   ZONE 4  subtitle      Ein Grusel-Abenteuer für Kinder ab 12 Jahren
 39 - 78   THE SCENE. No text.
 80 - 86   ZONE 5  author        Benjamin Krug
 87 - 100  EMPTY BAND. Plain dark hallway floor. NO text of any kind here.

THE TWO EMPTY BANDS ARE THE MOST IMPORTANT PART OF THIS LAYOUT.

Above the first line of text there must be a clearly visible strip of plain
dark background, at least TWICE AS TALL as the capital letters of that line.
Below the author's name there must be an equally visible strip of plain dark
floor, at least TWICE AS TALL as the letters of the author's name.

If you cannot fit everything, make the TEXT SMALLER. Never move it outwards.
A slightly smaller title with generous empty margins is correct. A large
title that reaches towards an edge is wrong and unusable.

SIDE MARGINS: every line of text sits inside the central 84% of the width.
To the left of the leftmost letter and to the right of the rightmost letter
of EVERY line there must be visible empty background at least as wide as two
capital letters.

The outer edges of this image are trimmed off when the book is printed, and
the e-book thumbnail is cropped narrower still. Anything close to an edge
will be lost. The ILLUSTRATION still fills the whole image to all four edges -
only the TEXT stays inside the safe area.

ZONE 5 NOTE: the composition must leave a calm, dark patch of hallway floor
in the centre at that height, so the author's name reads clearly against it.

════════════════════════════════════════
THE SCENE - a narrow hallway inside an old German apartment, at dusk.
════════════════════════════════════════

We are looking down the hallway from behind three figures. At the far end of
the hallway there is a plain interior door standing very slightly AJAR - open
by no more than a hand's width. The door has not been pushed; it simply stands
open, perfectly still.

Through that narrow gap falls the ONLY light in the picture: a cold, pale,
grey-silver light, as if from a small barred window in the room beyond. It is
not warm, not golden, not blue - it is the colour of frost.

Inside the gap, dimly visible in that cold light: the dark bulk of a very old
carved wooden WARDROBE against the far wall, and in front of it the GREY,
BLURRED SHAPE OF AN OLD MAN, seen entirely FROM BEHIND, his head slightly
lowered. He is a soft grey silhouette, like a figure seen through fog - no
face, no features, no detail. He is turned away from us.

A single hair-thin thread of PALE COLD LIGHT runs from the middle of his back
downwards and disappears at a tiny point near the BOTTOM RIGHT corner of the
wardrobe door. The thread is faint and delicate - it must not dominate.

A fine silvery frost is forming on the dark wood of the wardrobe door, spreading
outwards from that same low point.

COLOUR WORLD: cool graphite and slate grey dominate, desaturated and cold.
The only warm point in the entire image is the dog's amber eye. Overall the
image is darker and cooler than a typical children's cover, but never black
and never harsh.

EVERYTHING FROM 0 TO 38 (see the layout map) is calm, dark hallway wall and
door lintel - plain surface with no detail, because all the title text sits
there. The open door begins BELOW that, at about 40.

THE THREE FIGURES - ALL SEEN FROM DIRECTLY BEHIND, occupying roughly 55 to 100
of the height. Their heads must not reach higher than 55, so that they never
come near the subtitle.
The viewer stands behind them and looks past their shoulders. We see the BACK
of their heads. Their faces are simply not in the picture - not in profile,
not in three-quarter view, not glimpsed. This is a fixed rule of the series.
They are NOT flat silhouettes: they are fully painted figures lit from the
front by the scene's single light source, so their clothing colours read
clearly even though they are seen from behind.

NORA (girl, 13) - straight shoulder-length MID-BROWN hair (not red, not
blonde). DARK TEAL zip-up hoodie (#2a8a7a), a clear blue-green. This is her
fixed series colour and must be plainly visible.

THEO (boy, 11) - smaller, half a step behind. Messy slightly curly DARK-BLOND
hair. Oversized MILITARY OLIVE-GREEN bomber jacket (#6b7a3a), a dull
yellow-green. His fixed series colour, plainly visible.

DO NOT SWAP THESE COLOURS: the GIRL wears TEAL, the BOY wears OLIVE. Readers
identify them by exactly this.

SCHATTEN (the dog) - medium-sized shaggy mixed-breed with dark, almost black
fur, a plain narrow LEATHER COLLAR (no harness, no chest straps, no vest).
Seen from behind and slightly to the side so that ONE eye is visible: a
LUMINOUS AMBER EYE (#d4920b), glowing from within. It is the single living
warm point of the cover and must stay visible at thumbnail size.

They stand in the hallway, a few steps short of the door, looking towards the
gap. Nora is closest to it. Schatten has STOPPED and is not moving forward -
he stands slightly apart, refusing to go nearer, his one amber eye catching
the cold light.

BETWEEN AND BELOW the figures, in the centre at about 80 to 86 of the height,
leave a calm, dark, uncluttered patch of hallway floor - this is where the
author's name goes. And keep the very bottom band (87 to 100) plain dark
floor: no bright detail, no text.

════════════════════════════════════════
FINAL CHECK BEFORE YOU FINISH
════════════════════════════════════════

✓ Is there a clearly visible EMPTY dark band above "DIE GEISTERSPÜRER",
  at least twice as tall as its capital letters?
✓ Is there a clearly visible EMPTY dark band below "Benjamin Krug",
  at least twice as tall as its letters?
✓ Does every line have visible empty background left and right of it?
✓ Does it say "ab 12 Jahren" - NOT "ab 10 Jahren"?
✓ GEISTERSPÜRER with Ü, für with ü, DIE GEBUNDENEN · BAND 1 with the middle dot?
✓ Is the title warm gold and clearly the largest text?
✓ Girl in TEAL, boy in OLIVE - not swapped?
✓ Is the dog's amber eye visible?
✓ No face anywhere - not the children's, not the old man's?
✓ No badge, no logo, no frame, no invented words?

DO NOT INCLUDE: children's faces or any face in profile; a clearly rendered
ghost figure with a visible face; monsters, skeletons, bones, blood, gore,
scary grimaces; a third child or any additional person; publisher logos,
badges, seals, age roundels; a painted frame or border around the image;
modern elements, cars, phones, screens; neon colours; manga, anime or flat
cartoon style; any text beyond the five given lines.
```

---

## 4. Prompt Rückseite — All-in-One, mit allen Texten

> **Die gewählte Vorderseite als Referenzbild anhängen.** Ohne sie driften Palette und
> Lichtqualität auseinander.
>
> Aufbau nach dem Muster von Band 2 (`Band2/Cover/Prompts/Cover_Prompt_Band2_Rueckseite_ChatGPT_Ready.md`):
> Hintergrund in Kantenzonen, dann nummerierte Textzonen. Alle Texte stammen wörtlich aus
> [`KDP_S2-1.md`](../KDP_S2-1.md) Abschnitt 6.
>
> ⚠️ **Eine Abweichung von Band 2, und sie ist wichtig:** Band 2s Prompt ließ das Modell
> einen hellen Barcode-Kasten samt Platzhalter-Strichcode malen. Der Reihenstandard hat
> genau das später **verboten** (Block E) — bei Band 4 und Band 5 saß der gemalte Kasten
> *neben* der echten Barcode-Position. Hier bleibt die Zone leer.

```
Generate a complete, print-ready BACK COVER for a German children's book. This
is a single image containing BOTH the background illustration AND all
typographic text rendered directly onto it. No placeholder boxes, no lorem
ipsum. All German text must be spelled correctly including umlauts (ä ö ü ß).

The chosen FRONT COVER is attached as reference. Match its palette, its light
quality and its level of detail exactly.

FORMAT: vertical portrait, aspect ratio 2:3. This is the back cover of a
6 x 9 inch paperback.

════════════════════════════════════════
BACKGROUND ILLUSTRATION
════════════════════════════════════════

The same apartment as on the front cover, in the same cold graphite and slate
palette - desaturated, cold, never black and never harsh. The illustration is
SUBTLE: it frames the edges and stays dark and uniform in the centre so that
text is readable.

TOP EDGE (upper 12%): the dark upper part of a plain old wall and a simple
door lintel. Nothing else. Quiet surface.

LEFT EDGE (left 12%): the edge of a small BARRED WINDOW high up, letting in a
cold grey-silver light - the same frost-coloured light as on the front cover.
It is the only light source in the image. The light falls to the right and
downward and fades out well before the centre.

RIGHT EDGE (right 12%): the dark vertical edge of a very old carved wooden
WARDROBE, seen from the side. Only a strip of it - carved vines and leaves in
deep shadow. On its lower part, a fine silvery FROST is forming on the wood.
‼️ THIS WARDROBE STRIP MUST END WELL ABOVE THE BOTTOM QUARTER OF THE IMAGE.
Below it, on the right, there is only plain dark wall and floor - no carving,
no ornament, no highlight. The reason is Zone 7 further down.

BOTTOM EDGE (lower 12%): bare, dusty floorboards. A thin, hair-fine thread of
PALE COLD LIGHT lies across them, running from the LEFT towards the centre,
where it fades out. It must NOT reach the right half of the image. It is faint
and delicate and must not dominate.

CENTRE (the large middle area): smooth, dark, atmospheric - dust in still air,
deep graphite gradient. This is the text zone and must stay uniform and dark
enough for light text to read clearly. No bright spots, no detail here.

NO FIGURES ANYWHERE on the back cover - no children, no dog, no ghost, nobody.

════════════════════════════════════════
TEXT LAYOUT - RENDER ALL TEXT EXACTLY AS SPECIFIED
════════════════════════════════════════

Do not alter, shorten, translate or paraphrase any text. Render every word
exactly as written.

──── EMPTY BAND (top 0-8%) ────

Plain dark wall. NO text of any kind. Above the first line of text there must
be a clearly visible strip of empty background, at least twice as tall as the
capital letters of that line.

──── ZONE 1 - TOP (centred, 9-14% from top) ────

Line 1 (larger):   Die Geisterspürer
Line 2 (smaller, directly below):   Die Gebundenen · Band 1

- Font: elegant, slightly worn serif. Readable, not decorative.
- Colour line 1: steel grey (#9aa6b0), line 2 slightly dimmer.
- Size: line 1 about 3.2% of image height, line 2 about 2%.

──── ZONE 2 - PULL QUOTE (centred, about 14-20% from top) ────

A thin faint separator rule above and below this zone.

Render exactly, including the German quotation marks:
„Es ist nicht nur ein Schloss. Es ist an mir dran."

- Font: italic serif, literary.
- Colour: warm AMBER GOLD (#d4920b). This is the ONLY warm-coloured element
  on the entire back cover. It must stand out.
- Size: about 2.1% of image height. Break into two centred lines.

──── ZONE 3 - KLAPPENTEXT (about 23-70% from top) ────

Left-aligned text inside a centred column about 76% of the image width.

- Font: clean readable serif, like a book set in Georgia or Garamond.
- Colour: warm light-white (#eaedf2)
- Size: about 1.7% of image height per line, line spacing about 160%.

Render the following paragraphs exactly, with a blank line between each:

PARAGRAPH 1:
Frau Brandt klopft an eine fremde Wohnungstür, weil sie nicht mehr weiß,
wohin. In ihrer Wohnung ist ihr Vater. Er ist seit einem Jahr tot,
achthundert Kilometer entfernt gestorben — und diese Stadt hat er nie gesehen.

PARAGRAPH 2:
Nora und Theo wissen, wie das geht. Zuhören. Das hat immer gereicht.

PARAGRAPH 3:
Es reicht auch diesmal. Der alte Mann sagt alles, was er zwölf Jahre lang
nicht gesagt hat. Er fängt an zu gehen — und wird zurückgerissen. Als hinge
er an einer Kette.

PARAGRAPH 4:
Die Kette gibt es wirklich. Ganz unten an einer alten Schranktür sitzt ein
Schloss, kaum größer als ein Daumennagel, und es ist eiskalt. Wer daran
zieht, tut nicht dem Schloss weh.

PARAGRAPH 5:
Der Schlosser war im August im Haus. In jeder Wohnung, auch in den leeren.
Die Familie zog erst im November ein.

PARAGRAPH 6 - render in ITALIC, same colour, centred:
Jemand hat das gebaut und dann gewartet. Bis irgendwer hineinpasste.

──── ZONE 4 - AGE & GENRE LINE (centred, about 73-77%) ────

A thin faint separator rule above this zone.

Render exactly:
Grusel-Abenteuer für mutige Leser ab 12 Jahren — Kribbeln ja, Albträume nein.

- Font: clean sans-serif, slightly bolder than the body text.
- Colour: muted light grey (#c0c8c0)
- Size: about 1.5% of image height. Centred, may break into two lines.

──── ZONE 5 - SERIES NOTE (centred, about 79-82%, small) ────

Render exactly:
Band 1 einer neuen Reihe. Die fünf Bände der ersten Geisterspürer-Reihe sind
bereits erschienen.

- Font: clean sans-serif, light weight.
- Colour: dim grey (#8d959c)
- Size: about 1.2% of image height - clearly smaller than Zone 4.

──── ZONE 6 - AUTHOR (centred, about 84-88%) ────

Render exactly:
Benjamin Krug

- Font: clean sans-serif.
- Colour: steel grey (#9aa6b0)
- Size: about 1.8% of image height.

──── EMPTY BAND (bottom 89-100%) ────

Plain dark floor. NO text of any kind. Below the author's name there must be
a clearly visible strip of empty background, at least twice as tall as the
letters of the name. If everything does not fit, make the TEXT SMALLER -
never move it outwards.

──── ZONE 7 - BARCODE ZONE (CRITICAL - LEAVE IT EMPTY) ────

The BOTTOM-RIGHT of the back cover - the right 42% of the width by the
bottom 20% of the height - must stay calm, dark, EMPTY background: no text,
no focal detail, no bright object, no thread of light.

Do NOT paint a grey, cream or white rectangle there. Do NOT paint a barcode,
an ISBN, or any placeholder digits. The printer places the real barcode on
top of the plain dark background.

No text from any other zone may reach into this area.

════════════════════════════════════════
TYPOGRAPHY RULES (ALL TEXT)
════════════════════════════════════════

- German umlauts must be correct: ä ö ü Ä Ö Ü ß - never replaced by ae oe ue
- German quotation marks: „opening" and "closing" - not English " or '
- Em-dashes: — not hyphens
- Crisp and anti-aliased, never blurry
- All text stays inside the central 84% of the width and keeps at least 13%
  of the height free at the very top and the very bottom
- Text lives in the dark centre and must not overlap illustration detail

════════════════════════════════════════
FINAL CHECK BEFORE YOU FINISH
════════════════════════════════════════

✓ All SIX paragraphs of the Klappentext are present and complete
✓ Paragraph 6 is italic
✓ The pull quote is amber gold and italic - the only warm element
✓ "Die Geisterspürer" and "Die Gebundenen · Band 1" stand at the top
✓ It says "ab 12 Jahren" - NOT "ab 10 Jahren"
✓ "Benjamin Krug" stands near the bottom
✓ The bottom-right barcode area is EMPTY and DARK - no rectangle, no barcode,
  no carved wardrobe detail, no light on the floor reaching into it
✓ Is there an empty dark band above the first line and below the author's name?
✓ No figures anywhere
✓ The image is dark, cold and graphite - not blue, not brown, not bright

════════════════════════════════════════
DO NOT INCLUDE
════════════════════════════════════════

Any face; any figure; a clearly rendered ghost; monsters, skeletons, bones,
blood, gore, scary grimaces; publisher logos, badges, seals, age roundels;
a painted frame or border around the image; modern elements, cars, phones,
screens; neon colours; manga, anime or flat cartoon style; any text beyond
the zones specified above.
```

> ⚠️ **Realistische Erwartung:** Ein Klappentext dieser Länge ist für ein Bildmodell die
> schwerste Aufgabe des ganzen Covers — Band 2s Anleitung rechnet ausdrücklich mit
> Umlautfehlern und Nachgenerieren. Wenn nach drei bis vier Versuchen kein Durchgang
> fehlerfrei ist, ist der **Rückfallweg**: dieselbe Szene ohne Text erzeugen (Zonen 1–6
> weglassen, Zone 7 behalten) und die Texte in einem Layoutprogramm setzen. Das ist kein
> Rückschritt — Band 4 und 5 sind so gebaut.

---

## 5. Ablauf und Prüfliste

1. Vorderseite erzeugen, **4–6 Varianten**
2. Beste wählen. **Texte Buchstabe für Buchstabe prüfen** — `GEISTERSPÜRER` (Ü), `für` (ü),
   **`ab 12 Jahren`** (nicht 10), **`DIE GEBUNDENEN · BAND 1`**
3. Rückseite mit der gewählten Vorderseite als Referenz erzeugen
4. Beide hochskalieren auf mindestens **1838 × 2775 px**
5. Ablegen als `Staffel2/S2-1/Cover/Bilder/front_s2_1.png` und `back_s2_1.png`
6. **Taschenbuch-PDF bauen und die echte Seitenzahl ablesen** → `PAGES` im Cover-Skript
7. `python Scripts/build_cover_kdp_s2_1.py`
8. **Kontrollbild ansehen** — nicht optional: Liegt aller Text innerhalb der cyanen Linie?
   Ist das magentafarbene Barcode-Feld leer? Stimmt der Rückentitel? Ist der **gemalte
   Buchrücken so breit wie der rechnerische**?
9. **150-px-Thumbnail** — erkennbar müssen bleiben: Titel, der helle Türspalt, das
   Bernsteinauge **und die Zeile „DIE GEBUNDENEN · BAND 1"** (neuer Punkt für Staffel 2)
10. Erst dann zu KDP

---

## 6. Offen

| Punkt | Blockiert durch |
|---|---|
| Bilder erzeugen | keine Bildgenerierung in dieser Umgebung |
| Cover-Skript laufen lassen | `PyMuPDF` und `Pillow` nicht installierbar |
| Echte Seitenzahl für den Buchrücken | Taschenbuch-PDF ungebaut (`python-docx` fehlt) |
| ~~Klappentext auf der Rückseite~~ | ✅ erledigt — steht in [`KDP_S2-1.md`](../KDP_S2-1.md) Abschnitt 6 und wörtlich im Rückseiten-Prompt |
