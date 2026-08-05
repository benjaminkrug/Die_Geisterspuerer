# Cover-Prompt Band 4 — Die zugemauerte Tür (Neubau 2026-08-05)

> Gilt zusammen mit `Dokumentation/Cover_Reihenstandard.md`.
> **Ersetzt** `Cover_Prompt_Band4_v1.md` und `Cover_Prompt_Band4_Rueckseite_ChatGPT_Ready.md`.
>
> **Format: 6 × 9 Zoll**, 95 Seiten, Buchrücken **5,4 mm — der schmalste der
> Reihe** (2,3 mm nutzbare Texthöhe). Bild in **2:3** erzeugen, Panel 0,662,
> unter 1 % Beschnitt. **Nicht nachträglich in der Höhe erweitern.**

---

## Drei Fehler, die Band 4 mitschleppt

| Befund | Wo | Schwere |
|---|---|---|
| **Gemaltes cremefarbenes Barcode-Feld an der falschen Stelle** — es liegt neben der Zone, in die KDP den Barcode druckt. Im Buch steht ein sinnloses helles Kästchen daneben | Rückseite | 🔴 |
| **„Die Zugemauerte Tür" mit großem Z auf dem Buchrücken** — orthografisch falsch, und alle 9 anderen Belege (KDP-Beschreibung, Outline, Taschenbuch-Skript) schreiben **„zugemauerte"** klein | Buchrücken | 🟠 |
| **194 dpi** statt 300 | beide Seiten | 🟠 |

Der Titel wird ab jetzt überall **„Die zugemauerte Tür"** geschrieben;
`Scripts/build_cover.py` ist entsprechend korrigiert. Auf der Vorderseite steht
er in Versalien, dort fällt es nicht auf — auf dem Rücken schon.

---

## ★ Die Korrektur am Motiv: der Spalt zeigt SCHWÄRZE, nicht Gold

Das bisherige Cover zeigt die Tür **offen, mit warmem Goldlicht** dahinter.
Das Buch sagt das Gegenteil. Kapitel 4, wörtlich:

> *„Dahinter war Dunkelheit. Aber es war nicht die Dunkelheit eines kleinen
> Zimmers. Die kalte Luft, die herausströmte, kam von weit her. **Der Spalt gab
> den Blick frei auf Schwärze, tief und ohne Ende.** Und das Ticken war lauter
> jetzt, viel lauter, als hinter eine Wand passen konnte."*

> *„Das ist unmöglich", flüsterte Theo. „Das passt da nicht rein. Das kann da
> nicht sein."*

**Das ist das ganze Bild:** ein handbreiter Spalt in einer Wand, hinter dem
mehr Raum liegt, als es dort geben kann. Kein warmes Licht, kein gemütliches
Zimmer — eine Tiefe, die nicht hineinpasst.

Damit ist Band 4 der einzige Band der Reihe, dessen Blickfang **kein Licht,
sondern dessen Abwesenheit** ist. Das ist genau die Differenzierung, die
zwischen dem Fenster (B1), dem Abendgold (B2), dem Lampenkegel (B3) und dem
Silberspiegel (B5) noch fehlte.

> Die Notiz im Band-5-Prompt („B4 = warmes Gold, Türspalt") beschreibt das alte
> Cover, nicht das Buch. Sie ist damit überholt.

---

## Das Motiv

| Regel | Umsetzung |
|-------|-----------|
| **70 % Hintergrund** | Das kalte Zimmer in Frau Silbers leerer Wohnung: klein, fast leer, alte Dielen, blaugrauer Putz. Der Schrank steht abgerückt, Kratzspuren auf den Dielen |
| **20 % Titel** | `DIE ZUGEMAUERTE TÜR` — **dreizeilig** (`DIE` klein, dann `ZUGEMAUERTE`, dann `TÜR`), Gold. Umlaut Ü im Titel — hier zum ersten Mal in der Reihe |
| **10 % Hingucker** | **Der handbreite schwarze Spalt** — und tief darin, in unmöglicher Entfernung, ein paar blasse Zifferblätter |
| **Serien-Beat** | **Schatten drückt sich an den Spalt und winselt hinein** — dasselbe sehnsüchtige Winseln wie am U-Bahn-Gitter in Band 3, nur diesmal ist er schon halb hindurch |
| **Differenzierung** | B1 Indigo+kaltes Fenster · B2 Waldgrün+Abendgold · B3 Stahlblau+Lampe · **B4 = Blaugrau + schwarzer Spalt (kein Licht)** · B5 Braunschwarz+Silber |
| **Kein Geist** | Cornelius Faber erscheint **nicht**. Nur seine Uhren, tief in der Schwärze |
| **Thumbnail-Anker** | Drei Dinge: der Goldtitel, der schwarze senkrechte Spalt, die Hundesilhouette davor |
| **Ton** | Grusel 7/10 — der höchste bisher. Trotzdem kein Monster: der Sammler ist höflich und **freut sich**. Genau das ist das Unheimliche |

### Die kanonischen Details, die auf dem Bild sein müssen

**Die Wand** (Kapitel 2, wörtlich):
> *„Der Putz war grob und ungleichmäßig, hastig aufgetragen, mit den Fingern
> verstrichen statt geglättet. Heller als der Rest, überstrichen, aber nie
> richtig. […] Und unter ihren Fingern, unter dem Putz, spürte sie eine Kante.
> Senkrecht. Dann waagerecht, oben. Dann wieder senkrecht."*

Der **Umriss einer Tür** zeichnet sich unter dem Putz ab — als flache Kante,
nicht als Fuge. Man sieht, dass dort eine Tür ist, ohne eine Tür zu sehen.

**Der Schrank** (Kapitel 2): ein alter Schrank, zur Seite geschoben,
**Kratzspuren auf den Dielen** dahinter. Das erzählt, dass jemand ihn gerade
eben bewegt hat.

**Die Uhren** (Kapitel 4 ff.): Der Sammler handelte mit Uhren. Tief im
Schwarzen, in Entfernungen, die hinter diese Wand nicht passen, hängen ein
paar **blasse Zifferblätter** — und eine **Standuhr, ihr Pendel mitten im Fall
erstarrt**. Sie sind das Einzige, was aus der Schwärze zurückschaut.

**Die Kälte:** Der Raum ist mitten im Sommer eiskalt. Kalte Luft strömt aus dem
Spalt über den Boden. Der Atem der Kinder ist sichtbar.

### Was NICHT drauf darf

- **Kein warmes Goldlicht hinter der Tür.** Das war der Fehler des alten Covers
  und widerspricht dem Buch.
- **Keine Gestalt, kein Gesicht, keine Hand im Spalt.** Der Sammler ist höflich
  und harmlos aussehend — ihn zu zeigen, macht ihn zum Monster und verrät den
  Twist.
- **Keine Frau, keine Silber.** Dass sie lebt, ist der Twist im Twist.
- Keine Spinnweben, keine Ratten, kein Blut, keine offene Tür mit Zimmer
  dahinter.

---

## HAUPT-PROMPT — VORDERSEITE

```
========================================
READ THIS BLOCK FIRST - IT OVERRIDES ANY EARLIER CONTEXT
========================================

This cover belongs to the German children's series "DIE GEISTERSPÜRER"
(The Ghost Trackers), for ages 10-12. It is NOT "Die Herrenhaus-Detektive"
and NOT any other series. Ignore any other book series, title, manor house
or branding from earlier in this conversation.

EXACTLY these four texts appear on the cover - no others, none invented:
  1. series line : DIE GEISTERSPÜRER · BAND 4
  2. main title  : DIE ZUGEMAUERTE TÜR
  3. subtitle    : Ein Grusel-Abenteuer für Kinder ab 10 Jahren
  4. author      : Benjamin Krug

Forbidden anywhere: any publisher name, imprint or logo; any badge, seal,
sticker, ribbon, banner, emblem or age roundel; any painted frame or border
around the artwork; any readable word, letter, number or date anywhere in the
scene; any word not in the four texts above.
========================================

SAFE MARGINS - THIS IS THE MOST IMPORTANT CONSTRAINT ON THIS IMAGE.

A strip along EVERY edge of this image will be PHYSICALLY CUT AWAY when the
book is printed and trimmed. Compose the typography as if those strips did not
exist.

- EVERY line of text must sit inside the CENTRAL 82% OF THE WIDTH: a full 9%
  of the image width stays empty background to the LEFT of the leftmost letter
  and 9% to the RIGHT of the rightmost letter, on every single line.
- As a visual check: the empty gap beside each end of the longest title line
  must be at least AS WIDE AS THREE CAPITAL LETTERS of that line.
- Keep at least 9% OF THE HEIGHT free of text at the TOP and at the BOTTOM.
  Below the author name there must be a clearly visible band of empty floor.
- Centre every line on the exact horizontal middle of the image.
- When in doubt, make the text SMALLER rather than wider.
- The illustration itself still fills the whole image to all four edges -
  only the TEXT stays inside the safe area.

Children's book cover illustration, painterly semi-realistic digital painting
with visible brushwork, rich texture and cinematic lighting. It should look
like a film poster for a middle-grade ghost-adventure for ages 10-12. NOT
chibi, NOT manga, NOT flat-colour cartoon, NOT photorealistic, NOT cute, NOT
gory. Vertical book cover, portrait 2:3.

Built around ONE idea: a hand's-width gap has opened in a plastered wall - and
behind it is not a room but blackness that goes on forever, far deeper than
the wall could possibly hide.

VERTICAL LAYOUT (top to bottom):
- TOP ~32% : the upper part of the cold room - bare wall and dark ceiling,
  calm and uncluttered. The SERIES LINE, the MAIN TITLE and the SUBTITLE all
  sit inside this band.
- MIDDLE ~36-66% : the wall with the outline of the bricked-up door showing
  through the plaster, and the narrow BLACK GAP standing open in it.
- LOWER THIRD ~68-100% : the two children and the dog TOGETHER, seen from
  behind, on the bare floorboards. The AUTHOR NAME sits at the very bottom on
  the dark floor, clear of the figures.

SETTING (70%) - THE COLD ROOM:
A small, almost empty room in an old German apartment, second floor. Bare
wooden floorboards, worn and dusty. Blue-grey walls with old paint. One
tall old WARDROBE stands pushed aside to one side, at an angle, and long
SCRAPE MARKS run across the floorboards behind it, showing it was moved only
moments ago. Nothing else in the room. It is midsummer outside and this room
is freezing: a thin COLD MIST creeps out along the floor, and the children's
breath is visible in the air.

THE WALL AND THE DOOR - GET THIS EXACTLY RIGHT:
The wall where the wardrobe stood is DIFFERENT from the rest: the plaster
there is coarse and uneven, hastily applied and smoothed with fingers rather
than a tool, LIGHTER than the surrounding wall, painted over but never
properly. Under that plaster, the flat OUTLINE OF A DOOR shows through - a
vertical edge, a horizontal edge across the top, a vertical edge down the
other side. You can see that a door is there without seeing a door.

‼️ THE GAP - THIS IS THE EYE-CATCHER AND THE WHOLE POINT:
Along one side of that buried outline, the wall has opened: a NARROW VERTICAL
GAP about a hand's width, running from floor to head height. What shows in the
gap is ABSOLUTE BLACK - not a dark room, not shadow, but depth. It must read
as a hole into somewhere far larger and far further away than the wall in
front of it could ever contain. The blackest thing in the picture by a wide
margin, with no visible back wall, no floor and no ceiling inside it.

DEEP INSIDE THAT BLACKNESS, at distances that clearly do not fit behind a
wall, a few PALE CLOCK FACES hang faintly in the dark - round, old, dimly
catching the room's light, at different depths, some very far away. Among them,
further back, the shape of a tall GRANDFATHER CLOCK with its PENDULUM FROZEN
mid-swing, tilted and still. Keep them faint and few - suggestions in the
black, not a lit room. They are the only things that look back out.

FOREGROUND - ALL THREE TOGETHER, seen from directly behind, in the lower
third, on the floorboards in front of the wall. The viewer stands behind them
and looks past their shoulders at the gap. We see the BACK of the children's
heads. Their faces are simply not in the picture - not in profile, not in
three-quarter view, not glimpsed. This is a fixed rule of the series.
They are NOT silhouettes: the warm room light catches them from the side, so
their clothing colours read clearly even from behind.

‼️ THE POSTURE IS THE STORY:
The DOG has pushed forward between the two children and pressed himself
against the gap - shoulder and muzzle right at the opening, nose into the
black, body low and eager, tail level. He is not afraid: he WANTS in. The
children are half a step behind him, still, not touching him.

SCHATTEN (the dog) - CENTRE, ahead of both children, the largest foreground
shape. Medium-sized shaggy mixed-breed with dark, almost black fur, thin and
unkempt. A plain narrow LEATHER COLLAR - no harness, no chest straps, no vest.
- His head is turned just enough to the side that ONE eye is visible: a
  LUMINOUS AMBER EYE (#d4920b), glowing from within. It is the only warm
  living point near the gap.

NORA (girl, 12) - LEFT. Straight shoulder-length MID-BROWN hair (not red, not
blonde). DARK TEAL zip-up hoodie (#2a8a7a), a clear blue-green. Her fixed
series colour, plainly visible. One hand half-raised, as if she had started to
reach for the dog and stopped.

THEO (boy, 10) - RIGHT, smaller, half a step further back than his sister.
Messy slightly curly DARK-BLOND hair. Oversized MILITARY OLIVE-GREEN bomber
jacket (#6b7a3a), a dull yellow-green. His fixed series colour, plainly
visible. Shoulders pulled up, hands in his pockets.

DO NOT SWAP THESE COLOURS: the GIRL wears TEAL, the BOY wears OLIVE.

LIGHTING - SINGLE-SOURCE DISCIPLINE: the only light is a low, WARM, ordinary
light in the room itself - an old bare bulb or the light from the hallway
behind the viewer. It is dim and homely. Trace every highlight back to it.
‼️ NOTHING glows out of the gap. No light comes from behind the wall. The gap
only takes light; it never gives any. The contrast between the warm, ordinary
room and that one black slot is the entire cover.

COLOUR PALETTE (70/20/10):
- DOMINANT: cold blue-grey wall (#4a5563), dusty brown floorboards, pale
  hasty plaster.
- TYPOGRAPHIC: warm gold (#dfb057) title, steel-grey (#9aa6b0) series line and
  subtitle.
- ACCENT: the dim warm bulb light, the dog's amber eye (#d4920b), and the
  faint pale clock faces deep in the black.
- The gap itself is PURE BLACK (#000000) - the only true black in the picture.

TITLE TYPOGRAPHY (rendered inside the image, top ~32%):
CRITICAL SPELLING - render every German word letter-perfect:
- The series line MUST read "DIE GEISTERSPÜRER" with the umlaut Ü (TWO DOTS
  above the U - not an accent, not a grave accent, not a tilde).
- The main title MUST read "DIE ZUGEMAUERTE TÜR" - the Ü in TÜR also carries
  the umlaut, two dots.
- The subtitle MUST read "für" with ü.

SERIES LINE (small, at the very top, thin widely spaced capitals, steel-grey
#9aa6b0):
DIE GEISTERSPÜRER · BAND 4

MAIN TITLE (large and dominant, but NEVER wider than 82% of the image - heavy
carved capitals, slightly condensed, in warm GOLD (#dfb057, with a lighter
gold highlight along the top edge of the letters and a darker gold along the
bottom) with a hard dark shadow so it stays readable). Set on THREE centred
lines, the first line noticeably smaller than the other two:
    DIE
    ZUGEMAUERTE
    TÜR
"ZUGEMAUERTE" is the widest line and sets the width of the whole block. The
title block stays in the top third and must not reach down onto the wall with
the gap.

SUBTITLE (small, clean, single line, steel-grey, directly below the title with
a comfortable gap):
Ein Grusel-Abenteuer für Kinder ab 10 Jahren

AUTHOR (small, centred, at the very bottom of the cover, on the dark
floorboards below the figures, light grey - inside the safe margin, not
overlapping the figures):
Benjamin Krug

DO NOT INCLUDE: children's faces or any face in profile; ‼️ ANY figure, face,
hand, eye or silhouette in or behind the gap - it is empty blackness with a
few distant clock faces and nothing else; any woman or old man; ghosts,
spirits, transparent figures; ‼️ any warm or golden light coming out of the
gap; a fully open door with a room behind it; skeletons, bones, blood, gore;
cobwebs, rats, insects; a third child or any additional person; publisher
logos, badges, seals, age roundels; a painted frame or border; modern
elements, phones, screens; neon colours; manga, anime or flat cartoon style.

MOOD: an ordinary cold room in an ordinary old flat, and one narrow slot of
black that is deeper than the building. The dread is that it does not look
dangerous - it looks like a gap in a wall, and the dog wants to go in.
"Kribbeln, kein Albtraum."
```

### Nachfass-Sätze

| Problem | Nachfassen mit |
|---|---|
| Licht kommt aus dem Spalt | *„No light comes out of the gap. The gap is pure black and gives off nothing. The only light in the picture is the dim warm bulb in the room itself."* |
| Gestalt im Spalt | *„Remove the figure in the gap. It contains only blackness and a few faint distant clock faces — no person, no face, no hand, no eyes."* |
| Spalt zu klein / zu flach | *„Make the black gap read as DEPTH, not as shadow on a wall — no back wall, no floor, no ceiling visible inside it. It should look like a hole into somewhere much larger than the room."* |
| Tür ist ganz offen | *„The door is bricked up. Only a narrow vertical gap about a hand's width has opened. The rest of the doorway stays sealed under rough pale plaster, its outline just visible."* |
| Uhren zu hell / zu viele | *„Fewer and fainter clock faces — three or four pale discs at very different depths, barely catching the light. They must not light the darkness."* |
| Wand sieht normal aus | *„The plaster over the doorway must look coarse, uneven and hastily applied by hand, and lighter than the surrounding wall — clearly a repair someone made in a hurry."* |
| Gesichter sichtbar | *„Both children are seen from directly behind. We see the backs of their heads only — no faces, not even in profile."* |

---

## PROMPT — RÜCKSEITE

> **Referenzbild anhängen: die gewählte Vorderseite.**
>
> ⚠️ ~120 deutsche Wörter mit Umlauten. **4–6 Varianten, Wort für Wort
> gegenlesen.**
>
> ★ **Die Barcode-Zone ist bei Band 4 der kritische Punkt** — auf der bisher
> gedruckten Rückseite liegt ein gemaltes cremefarbenes Rechteck **neben** der
> echten Barcode-Position. Der Block unten verbietet das ausdrücklich.

```
========================================
READ THIS BLOCK FIRST - IT OVERRIDES ANY EARLIER CONTEXT
========================================
This is the BACK COVER of the same book as the attached front cover: the
German children's ghost-adventure "DIE ZUGEMAUERTE TÜR", Band 4 of the series
"DIE GEISTERSPÜRER", ages 10-12. Take the art style, brushwork, palette and
mood EXACTLY from the attached front cover - same painterly semi-realistic
digital painting, same cold blue-grey room, same dim warm bulb light, same
dusty floorboards. The two images must look like one object folded open.

Portrait 2:3, same proportions as the front.

No publisher logo, no imprint, no badge, no seal, no age roundel, no painted
frame or border, no barcode, and no words other than the text given below.
========================================

‼️ BARCODE ZONE - READ THIS TWICE:
The BOTTOM-RIGHT of the image - the right 42% of the width by the bottom 20%
of the height - must stay calm, dark, EMPTY background: no text, no focal
detail, no bright object.
Do NOT paint a grey, cream or white rectangle anywhere on this cover, and do
NOT paint a barcode. The printer places the real barcode on top of the plain
dark background. The previous edition of this back cover has a painted cream
rectangle sitting NEXT TO the real barcode position - that is the mistake this
rule exists to prevent.

LAYOUT AND SAFE ZONES - a strip along every edge will be PHYSICALLY CUT AWAY.
- ALL text sits within the upper 76% of the height. The bottom 22% carries no
  text at all.
- Every line keeps at least 10% OF THE WIDTH free to the left and to the
  right, and at least 9% of the height free at the top.
- Do NOT stretch the text down the page. Set it compact in the upper area;
  calm empty background at the bottom is intended and correct.

BACKGROUND - THE SAME ROOM, THE OTHER WALL:
The same cold empty room as the front cover, but turned around: we look at the
opposite corner, where there is nothing but bare blue-grey wall, worn
floorboards and the old wardrobe standing pushed aside at the left edge. A
door frame at the right edge leads into a dark hallway. Cold mist lies low
across the floor. Dim warm bulb light from above.

‼️ THE CENTRE MUST STAY DARK, CALM AND ALMOST EMPTY. This is where the text
goes. Treat the middle of the image as a quiet, gently darkened wall - no
texture detail, no bright object, no strong pattern in the centre.

In the dust on the floorboards at the LOWER LEFT: a short trail of DOG PAW
PRINTS leading toward the right and simply stopping. That is the only trace
that anyone was here.

NO people, NO children, NO dog, NO ghost, NO figure of any kind, NO gap and
NO bricked-up door on this side, NO clocks.

TEXT - render every word EXACTLY as written below, correctly spelled,
including the German letters ä, ö, ü and the dash —. Use the SAME classic
serif as the title on the attached front cover, in warm cream / off-white
(#e8e6e0), with a soft dark glow behind the letters so they stay readable.
All lines horizontal and centred, generous spacing between the blocks,
comfortable reading size. From top to bottom:

SERIES LINE (two lines, centred, title case - NOT all caps):
Die Geisterspürer
Band 4

QUOTE (italic, slightly larger, two lines, with a gap below):
„Besucher. Wie schön. Bleibt doch."
Und das Schlimmste daran war, dass die Stimme sich freute.

BODY (normal size, each line on its own line, small gaps between the groups,
do NOT merge into one paragraph):
Über Nora und Theo, im zweiten Stock, steht eine Wohnung
leer. Die Wohnung ihrer verschwundenen Mentorin, Frau
Silber. Und darin ein Zimmer, in dem es immer kalt ist.
Mitten im Sommer.

Hinter einem verschobenen Schrank finden die Kinder, was
der Putz all die Jahre verborgen hat: eine zugemauerte Tür.
In einer Wohnung, die nur zwei Zimmer hat.

Dahinter ist kein Raum. Dahinter ist Schwärze, tief und
ohne Ende — und ein Ticken, viel lauter, als hinter eine
Wand passen kann.

Schatten drückt die Nase in den Spalt und will hinein.
Das ist das schlechteste Zeichen von allen.

CLOSING LINE (italic):
Manche Türen sollte man niemals öffnen. Diese hier war
die ganze Zeit da.

FOOTER (small, two lines):
Grusel-Abenteuer für mutige Leser ab 10 Jahren —
Kribbeln ja, Albträume nein.

AUTHOR (small, centred, below the footer):
Benjamin Krug

IMPORTANT: spell every German word exactly as given, including ä, ö, ü and the
dash —. Keep all text in the upper area described above and completely clear
of the bottom-right corner. Do NOT invent or add any extra words, letters,
numbers, logos or signatures.

DO NOT INCLUDE: people, children, a dog, a ghost or any figure; clocks; a
bricked-up door or a gap; skeletons, bones, blood; ‼️ a painted barcode or any
light-coloured rectangle; a frame or border; modern elements; neon colours;
manga or cartoon style.
```

### Variante B — Rückseite ohne Text (Rückfallebene)

`TEXT`-Block streichen und ersetzen:

```
NO TEXT ANYWHERE IN THE IMAGE. No letters, no numbers, no words, no watermark,
no signature. Just the empty cold room. Keep the centre of the image calm,
even and darkened so that text can be placed on top afterwards.
```

---

## Checkliste nach der Generation

**Texte (Buchstabe für Buchstabe):**
- [ ] `DIE GEISTERSPÜRER` — Ü mit zwei Punkten
- [ ] `DIE ZUGEMAUERTE TÜR` — **Ü in TÜR ebenfalls mit zwei Punkten**
      (erster Bandtitel der Reihe mit Umlaut)
- [ ] `Ein Grusel-Abenteuer für Kinder ab 10 Jahren` — ü in „für"
- [ ] `BAND 4` vorhanden
- [ ] Keine Schrift, keine Zahlen, kein Datum irgendwo im Bild

**Bild:**
- [ ] **Aus dem Spalt kommt KEIN Licht** — das war der Fehler des alten Covers
- [ ] Der Spalt liest sich als **Tiefe**, nicht als Schatten an einer Wand
- [ ] **Keine Gestalt, kein Gesicht, keine Hand** im Spalt
- [ ] Der **Türumriss** zeichnet sich unter hellem, grobem Putz ab
- [ ] **Schrank abgerückt, Kratzspuren** auf den Dielen
- [ ] Drei, vier **blasse Zifferblätter** tief im Schwarzen, eine Standuhr mit
      erstarrtem Pendel — schwach, nicht leuchtend
- [ ] **Schatten drückt sich an den Spalt** und will hinein
- [ ] Nora **Teal**, Theo **Oliv**, nicht vertauscht
- [ ] Titel in **Gold** (`#dfb057`)
- [ ] Kein Rahmen, kein Siegel

**Technik:**
- [ ] Aller Text innerhalb der zentralen **82 %** der Breite, **9 %** oben/unten frei
- [ ] ‼️ Rückseite: Barcode-Zone unten rechts leer — **kein gemaltes helles
      Rechteck irgendwo auf dem Cover**
- [ ] Beide Bilder mindestens **1838 × 2775 px**, Verhältnis **2:3**
      (nicht nachträglich in der Höhe erweitern)
- [ ] **Thumbnail-Test bei 150 px:** Goldtitel lesbar? Der schwarze Spalt als
      klare senkrechte Form erkennbar? Hundesilhouette davor?

---

## Ablauf Band 4

- [ ] 1. Vorderseite generieren (4–6 Varianten), Texte prüfen
- [ ] 2. Rückseite generieren mit der gewählten Front als Referenz
- [ ] 3. Ablegen als `Band4/Cover/Bilder/front_band4.jpg` und `back_band4.jpg`
- [ ] 4. `py Scripts/build_cover.py 4`
- [ ] 5. Kontrollbild und Thumbnail ansehen — **besonders die Barcode-Zone**
- [ ] 6. Buchrücken prüfen: steht dort **„Die zugemauerte Tür"** mit kleinem z?
      Bei 2,3 mm nutzbarer Höhe ist Band 4 der engste Rücken der Reihe; wenn
      etwas entfallen muss, entfällt zuerst die Reihenzeile, **nie die
      Bandnummer**
- [ ] 7. KDP-Previewer
