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

> Aufbau: Block A (Kopf) · Block B (Sicherheitsränder) · Bandinhalt · Block C (Figuren) ·
> Block D (Verbote). Blöcke A–D stehen **wörtlich** im Reihenstandard, hier nur um die
> Staffel-2-Punkte ergänzt (dritte Kopfzeile, ab 12, 13 % oben/unten).

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

SAFE MARGINS (CRITICAL - the outer edges are trimmed off when the book is
printed, and the e-book version is cropped narrower still):
- EVERY line of text must sit inside the central 84% of the width. There must
  be clearly visible empty background - at least the width of two capital
  letters - to the LEFT of the leftmost letter and to the RIGHT of the
  rightmost letter of every single line.
- Keep at least 13% of the height free of text at the TOP and at the BOTTOM.
- NO letter may touch or approach an outer edge.
- Better a slightly smaller title with clear margins than a big title that
  reaches the edge. When in doubt, shrink the text.
- The illustration itself still fills the whole image to all four edges -
  only the TEXT stays inside the safe area.

THE SCENE - a narrow hallway inside an old German apartment, at dusk.

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

THE UPPER THIRD of the image is calm, dark hallway wall and door lintel -
plain surface with no detail, because the title text sits there.

THE THREE FIGURES - ALL SEEN FROM DIRECTLY BEHIND, in the lower third.
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

DO NOT INCLUDE: children's faces or any face in profile; a clearly rendered
ghost figure with a visible face; monsters, skeletons, bones, blood, gore,
scary grimaces; a third child or any additional person; publisher logos,
badges, seals, age roundels; a painted frame or border around the image;
modern elements, cars, phones, screens; neon colours; manga, anime or flat
cartoon style; any text beyond the five given lines.
```

---

## 4. Prompt Rückseite

> Die gewählte Vorderseite als Referenzbild anhängen. Der Klappentext steht **noch nicht
> fest** — er entsteht mit der KDP-Beschreibung und wird nachträglich gesetzt, nicht
> vom Bildmodell gemalt.

```
BACK COVER for the same book - attach the chosen front cover as reference.

Same apartment, same cold graphite palette, same light quality. This time we
see the small room itself: the old carved WARDROBE standing against a wall,
seen straight on from a few steps away. A small barred window high on the left
lets in the same cold grey-silver light. Dust. Bare floorboards. Nothing else
in the room.

NO figures at all on the back cover - no children, no dog, no ghost.

The upper half stays calm and dark - the blurb text will be placed there later.

BARCODE ZONE (CRITICAL): the BOTTOM-RIGHT of the back cover - the right 42%
of the width by the bottom 20% of the height - must stay calm, dark, empty
background: no text, no focal detail, no bright object.
Do NOT paint a grey, cream or white rectangle there, and do NOT paint a
barcode. The printer places the real barcode on top of the plain background.

DO NOT INCLUDE: children's faces or any face in profile; a clearly rendered
ghost figure with a visible face; monsters, skeletons, bones, blood, gore,
scary grimaces; a third child or any additional person; publisher logos,
badges, seals, age roundels; a painted frame or border around the image;
modern elements, cars, phones, screens; neon colours; manga, anime or flat
cartoon style; any text anywhere - the back cover carries NO text at all.
```

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
| Klappentext auf der Rückseite | entsteht mit der KDP-Beschreibung |
