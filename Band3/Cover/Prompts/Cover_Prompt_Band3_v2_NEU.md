# Cover-Prompt Band 3 — Schatten sieht mehr (Neubau 2026-08-05)

> Gilt zusammen mit `Dokumentation/Cover_Reihenstandard.md`.
> **Ersetzt** `Cover_Prompt_Band3_v1.md` und `Cover_Prompt_Band3_Rueckseite_ChatGPT_Ready.md`.
>
> **Format: 6 × 9 Zoll**, 106 Seiten, Buchrücken 6,1 mm.
> Bild in **2:3** erzeugen — passt fast exakt (Panel 0,662), unter 1 % Beschnitt.

---

## Ausgangslage: Band 3 war der sauberste der fünf

Das ist wichtig für die Erwartung. Beim Vergleich aller fünf verkauften Cover
war Band 3 der einzige, an dem inhaltlich **nichts** falsch war:

| | Band 3 |
|---|---|
| Reihenzeile mit korrektem Ü | ✅ |
| Bandnummer `BAND 3` | ✅ |
| Titel dominant, Untertitel, Autor | ✅ |
| Aller Text innerhalb der Sicherheitslinie | ✅ |
| Kein Siegel, kein Rahmen, kein Verlagslogo | ✅ |
| Kein klar erkennbarer Geist | ✅ |
| **Auflösung 1188 × 1758 = 190 dpi** | ❌ |

**Der einzige echte Mangel ist die Auflösung.** Deshalb ist dieser Prompt kein
Umbau, sondern eine Schärfung: dieselbe Bildidee, präziser gefasst, mit den
drei kanonischen Details, die dem alten Cover fehlen — und in Druckauflösung.

> Falls dir das alte Motiv lieber ist als jedes neue: Es ließe sich auch
> einfach hochskalieren. Bei 1,58× auf gemalte Illustration wäre das
> vertretbar. Der Grund, es trotzdem neu zu machen, ist der Serien-Beat unten.

---

## Das neue Motiv

**Der Serien-Beat: Schatten zieht zum ersten Mal HINEIN.**

Die Reihe erzählt den Hund über fünf Bände als Kurve:

| | Was Schatten tut |
|---|---|
| Band 1 | sitzt vor dem Haus und **wartet** |
| Band 2 | **verweigert** das Tor — vier Pfoten auf dem Pflaster |
| **Band 3** | **zieht voraus, hinein** — zum ersten Mal aktiv |
| Band 4 | zieht ins Warme |
| Band 5 | **wird gezogen** — er kämpft und verliert |

Auf dem Cover von Band 2 ist die Leine **nach hinten** straff. Auf Band 3 ist
sie **nach vorn** straff. Dieselbe Geste, umgedreht. Wer beide Bücher hat,
sieht es sofort — und wer nur eines hat, merkt nichts Fehlendes.

Der Grund steht im Buch: Er erkennt den Ort. Es war der Ort von Frau Silber.
Kapitel 1, am Gitter über den Treppen:

> *„Schatten drückte die Nase zwischen die Stäbe. Er winselte. Nicht ängstlich.
> **Sehnsüchtig.**"*

**Der Blickfang: der Kreidepfeil.**

Kapitel 4, wörtlich:

> *„Dort, auf Augenhöhe, in die Schwärze der alten Kacheln gemalt: ein Pfeil.
> Weiß. Kreide. Er zeigte den Bahnsteig hinunter, in die Dunkelheit, dorthin,
> wo Schatten schon hinsah. **Die Kreide war nicht alt.**"*

Das ist das Band-3-Äquivalent zu HILF (Band 1) und den zu langen Schatten
(Band 2): ein Ding, das ein Kind sofort sieht und sofort falsch findet.
**Jemand war vor Kurzem hier unten.** Und es ist zum ersten Mal der
übergreifende Reihenfaden, der sichtbar wird.

| Regel | Umsetzung |
|-------|-----------|
| **70 % Hintergrund** | Stillgelegter U-Bahnhof Altstadt-Nord: gekachelter Bahnsteig, schwarzes Tunnelmaul, Staub, kein Strom seit 1972 |
| **20 % Titel** | `SCHATTEN SIEHT MEHR` — zweizeilig, dominant. **Kein Umlaut im Titel** |
| **10 % Hingucker** | Der **frische weiße Kreidepfeil** auf den schwarzen Kacheln + der Taschenlampenstrahl, der sich im Tunnel verliert |
| **Serien-Beat** | **Schatten zieht nach vorn.** Leine straff — die Umkehrung von Band 2 |
| **Differenzierung** | B1 Indigo-Nacht · B2 Waldgrün+Abendgold · **B3 = Stahlblau, unterirdisch** · B4 Blaugrau+Türgold · B5 Braunschwarz+Silber |
| **Kein Geist** | Marlene erscheint **nicht**. Nur ihr Pfeil-Ziel: die Schwärze, in die alles zeigt |
| **Thumbnail-Anker** | Drei Dinge: der Titel, der Taschenlampenkegel im schwarzen Tunnelmaul, die Dreiergruppe |
| **Ton** | Grusel 6/10 — der erste Band mit **echter körperlicher Gefahr**. Trotzdem kein Monster: der Geist ist eine verzweifelte Mutter |

### Was NICHT aufs Cover darf

- **Kein Kind, keine Kindergestalt, keine Frau, keine Silhouette im Tunnel.**
  Der ganze Twist von Band 3 ist, dass der Leser das verlorene Kind erwartet
  und eine Mutter findet. Ein Kind im Tunnel nimmt die Enttäuschung vorweg,
  eine Frau verrät den Twist.
- **Kein Einsturz, keine fallenden Steine.** Das ist der Höhepunkt.
- Keine Ratten, keine Spinnweben-Klischees, kein Blut.

### Warum das obere Drittel diesmal fast schwarz ist

B1 hat Nachthimmel, B2 hat Abendhimmel — B3 spielt unter der Erde, es gibt
keinen Himmel. Der Titel steht auf der dunklen gekachelten Decke bzw. auf
reiner Schwärze. Das ist genau der Kontrast, der Band 3 im Regal von Band 1
und 2 abhebt: **kein Horizont.**

---

## HAUPT-PROMPT — VORDERSEITE

> Bildformat **2:3 hochkant**, so groß wie möglich (Ziel mindestens
> 1838 × 2775 px, besser 4K).

```
========================================
READ THIS BLOCK FIRST - IT OVERRIDES ANY EARLIER CONTEXT
========================================

This cover belongs to the German children's series "DIE GEISTERSPÜRER"
(The Ghost Trackers), for ages 10-12. It is NOT "Die Herrenhaus-Detektive"
and NOT any other series. Ignore any other book series, title, manor house
or branding from earlier in this conversation.

EXACTLY these four texts appear as cover typography - no others, none
invented:
  1. series line : DIE GEISTERSPÜRER · BAND 3
  2. main title  : SCHATTEN SIEHT MEHR
  3. subtitle    : Ein Grusel-Abenteuer für Kinder ab 10 Jahren
  4. author      : Benjamin Krug

In addition, and ONLY these, TWO pieces of text may appear as part of the
scene itself, painted on the tiled wall:
  - the station name  ALTSTADT-NORD  (with the hyphen)
  - the year          1972
Both are old, weathered station signage. Render them exactly, or leave them
out entirely - but never invent other words, letters or numbers anywhere.

Forbidden anywhere: any publisher name, imprint or logo; any badge, seal,
sticker, ribbon, banner, emblem or age roundel; any painted frame or border
around the artwork; graffiti; advertising posters; any word not listed above.
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
  Below the author name there must be a clearly visible band of empty ground.
- Centre every line on the exact horizontal middle of the image.
- When in doubt, make the text SMALLER rather than wider.
- The illustration itself still fills the whole image to all four edges -
  only the TEXT stays inside the safe area.

Children's book cover illustration, painterly semi-realistic digital painting
with visible brushwork, rich texture and cinematic lighting. It should look
like a film poster for a middle-grade ghost-adventure for ages 10-12. NOT
chibi, NOT manga, NOT flat-colour cartoon, NOT photorealistic, NOT cute, NOT
gory. Vertical book cover, portrait 2:3.

Built around ONE idea: deep under the city, on the platform of a subway
station that has had no power since 1972, the dog is pulling the two children
FORWARD into the dark - and someone has recently drawn a fresh white chalk
arrow on the wall pointing the same way.

VERTICAL LAYOUT (top to bottom):
- TOP ~30% : the dark vaulted tiled ceiling of the platform hall, almost
  black, calm and uncluttered. There is NO sky in this picture. The SERIES
  LINE, the MAIN TITLE and the SUBTITLE all sit inside this band.
- MIDDLE ~34-64% : the tiled platform wall on the left with the fresh WHITE
  CHALK ARROW at eye height, and straight ahead the black mouth of the tunnel
  swallowing the torch beam.
- LOWER THIRD ~66-100% : the two children and the dog TOGETHER, seen from
  behind, on the platform. The AUTHOR NAME sits at the very bottom on the dark
  platform floor, clear of the figures.

SETTING (70%) - THE ABANDONED STATION:
An underground subway platform, sealed and forgotten for over fifty years.
Walls of small square tiles, once white, now grey-black with grime, many
cracked or missing. A low vaulted ceiling. Thick pale dust on the floor,
disturbed only by the three sets of fresh tracks the group has just made.
No electric light anywhere - the station has no power. Cold damp air, a faint
haze of dust hanging in the torch beam. Deep steel-blue darkness everywhere
the torch does not reach.

Far ahead, where the platform ends, the TUNNEL MOUTH: a black arch that the
torchlight does not penetrate. It is simply, completely black - the darkest
shape in the picture, and everything in the composition leads to it.

Old weathered station signage on the tiled wall, half-legible under the dirt:
the station name ALTSTADT-NORD, and elsewhere the year 1972. Both faded and
grimy. If they cannot be rendered cleanly, leave them out rather than render
scrambled letters.

THE CHALK ARROW - THE EYE-CATCHER, GET THIS EXACTLY RIGHT:
On the dark tiles of the left-hand wall, at a child's eye height, someone has
drawn an ARROW in WHITE CHALK. It points along the platform, into the tunnel -
the same direction the dog is pulling. The chalk is BRIGHT, CLEAN and
UNSMUDGED: obviously drawn recently, in sharp contrast to fifty years of dirt
on every other surface. It should read instantly as "someone was down here
NOT LONG AGO". The torch beam catches it so it is the brightest white in the
picture apart from the beam itself. No letters, no words, no signature next to
it - the arrow alone.

FOREGROUND - ALL THREE TOGETHER, seen from directly behind, in the lower
third, on the dusty platform. The viewer stands behind them and looks past
their shoulders down the platform toward the tunnel. We see the BACK of the
children's heads. Their faces are simply not in the picture - not in profile,
not in three-quarter view, not glimpsed. This is a fixed rule of the series.
They are NOT silhouettes: the torch beam bounces off the tiles and lights them
from the front, so their clothing colours read clearly even from behind.

‼️ THE POSTURE IS THE STORY - GET THIS EXACTLY RIGHT:
The dog is AHEAD of the children, already a step or two further into the dark,
LEANING FORWARD into his collar and PULLING. The leash between him and the
girl is STRETCHED TIGHT, a straight taut line pointing FORWARD, toward the
tunnel. The girl is leaning back very slightly against the pull.
He is not afraid and he is not being dragged - he is the one leading, and that
is what makes it unsettling.

SCHATTEN (the dog) - CENTRE, in front of both children, the largest and most
central foreground shape. Medium-sized shaggy mixed-breed with dark, almost
black fur, thin and unkempt. A plain narrow LEATHER COLLAR - no harness, no
chest straps, no vest.
- Body low and stretched forward, front paws planted ahead, tail level, ears
  pricked forward toward the tunnel mouth.
- His head is turned just enough to the side that ONE eye is visible: a
  LUMINOUS AMBER EYE (#d4920b), glowing from within. It is the only warm point
  in this cold blue picture and must stay visible at thumbnail size.

NORA (girl, 12) - LEFT. Straight shoulder-length MID-BROWN hair (not red, not
blonde). DARK TEAL zip-up hoodie (#2a8a7a), a clear blue-green. Her fixed
series colour, plainly visible.
- ‼️ She holds the LEASH taut in one hand and a small TORCH in the other. The
  torch is aimed low and forward, down the platform - a narrow beam, not a
  wide floodlight. It is the only light source in the picture.

THEO (boy, 10) - RIGHT, smaller, half a step behind. Messy slightly curly
DARK-BLOND hair. Oversized MILITARY OLIVE-GREEN bomber jacket (#6b7a3a), a
dull yellow-green. His fixed series colour, plainly visible.
- One hand gripping the strap of his backpack, shoulders pulled up. He is
  following, not leading.

DO NOT SWAP THESE COLOURS: the GIRL wears TEAL, the BOY wears OLIVE.

LIGHTING - SINGLE-SOURCE DISCIPLINE: the girl's torch is the ONLY light in
this picture. Trace every highlight back to it. Bright where the beam strikes
tiles, dust and chalk; falling away rapidly into deep steel-blue darkness at
the edges and in the tunnel. No electric lamps, no emergency lighting, no
daylight, no magical glow, no moon - the station has no power.

COLOUR PALETTE (70/20/10):
- DOMINANT: deep steel blue (#1b2a3d), cold tile grey-blue (#3f5468), black.
- TYPOGRAPHIC: warm gold (#dfb057) title, steel-grey (#9aa6b0) series line and
  subtitle.
- ACCENT: the warm-white torch beam, the bright white chalk arrow, and the
  dog's amber eye (#d4920b).
The picture must NOT be uniformly black - the torch beam raking across tiles
and dust against the cold blue dark is what carries it.

TITLE TYPOGRAPHY (rendered inside the image, top ~30%):
CRITICAL SPELLING - render every German word letter-perfect:
- The series line MUST read "DIE GEISTERSPÜRER" with the umlaut Ü (TWO DOTS
  above the U - not an accent, not a grave accent, not a tilde).
- The main title "SCHATTEN SIEHT MEHR" contains NO umlaut at all.
- The subtitle MUST read "für" with ü.

SERIES LINE (small, at the very top, thin widely spaced capitals, steel-grey
#9aa6b0):
DIE GEISTERSPÜRER · BAND 3

MAIN TITLE (large and dominant, but NEVER wider than 82% of the image - heavy
carved capitals, slightly condensed, in warm GOLD (#dfb057, with a lighter
gold highlight along the top edge of the letters and a darker gold along the
bottom) with a hard dark shadow so it stays readable against the black
ceiling). Set on TWO centred lines:
    SCHATTEN
    SIEHT MEHR
The whole title block stays in the top third and must not reach down into the
tiled wall or the tunnel mouth.

SUBTITLE (small, clean, single line, steel-grey, directly below the title with
a comfortable gap, still inside the calm dark top band):
Ein Grusel-Abenteuer für Kinder ab 10 Jahren

AUTHOR (small, centred, at the very bottom of the cover, on the dark dusty
platform floor below the figures, light grey - inside the safe margin, not
overlapping the figures):
Benjamin Krug

DO NOT INCLUDE: children's faces or any face in profile; ‼️ ANY figure in the
tunnel - no child, no boy, no woman, no adult, no silhouette, no pale shape,
no glowing eyes in the dark: the tunnel mouth is simply empty blackness;
ghosts, spirits, transparent figures; skeletons, bones, skulls, blood, gore;
a collapsing ceiling or falling rocks; rats, cobwebs, spiders; a third child
or any additional person; graffiti or advertising posters; publisher logos,
badges, seals, age roundels; a painted frame or border; modern elements, cars,
phones, screens; neon colours; manga, anime or flat cartoon style.

MOOD: a station that has been dark since 1972, a chalk mark that is only days
old, and a dog who suddenly knows exactly where he is going. The unease comes
from the dog's certainty, not from a monster. "Kribbeln, kein Albtraum."
```

### Nachfass-Sätze

| Problem | Nachfassen mit |
|---|---|
| Gestalt im Tunnel | *„Remove the figure in the tunnel. The tunnel mouth must be completely empty black — no child, no woman, no silhouette, no shape, no glowing eyes."* |
| Hund zieht nicht | *„The dog must be AHEAD of both children, leaning forward into his collar and pulling. The leash from the girl's hand to his collar must be a straight, visibly TAUT line pointing forward toward the tunnel."* |
| Kreidepfeil fehlt / wirkt alt | *„The white chalk arrow on the tiled wall must look freshly drawn — bright, clean, unsmudged white chalk, in sharp contrast to the fifty years of grime around it. It points along the platform into the tunnel."* |
| Zu viel Licht | *„The station has no electricity. The girl's torch is the only light source — everything it does not reach falls away into deep steel-blue darkness."* |
| Falsche Beschriftung | *„The wall signage must read exactly ALTSTADT-NORD with a hyphen, and the year 1972. If you cannot render them cleanly, leave the signs blank instead."* |
| Gesichter sichtbar | *„Both children are seen from directly behind. We see the backs of their heads only — no faces, not even in profile."* |
| Zu warm / zu braun | *„Shift the whole picture colder — deep steel blue and grey tile, not brown. Only the torch beam, the chalk and the dog's eye are warm."* |

---

## PROMPT — RÜCKSEITE

> **Referenzbild anhängen: die gewählte Vorderseite.**
>
> ⚠️ ~110 deutsche Wörter mit Umlauten. **4–6 Varianten, Wort für Wort
> gegenlesen.** Fällt nichts Sauberes an: Hintergrund ohne Text, Satz in Canva.

```
========================================
READ THIS BLOCK FIRST - IT OVERRIDES ANY EARLIER CONTEXT
========================================
This is the BACK COVER of the same book as the attached front cover: the
German children's ghost-adventure "SCHATTEN SIEHT MEHR", Band 3 of the series
"DIE GEISTERSPÜRER", ages 10-12. Take the art style, brushwork, palette and
mood EXACTLY from the attached front cover - same painterly semi-realistic
digital painting, same abandoned tiled subway station, same deep steel-blue
darkness, same hanging dust. The two images must look like one object folded
open.

Portrait 2:3, same proportions as the front.

No publisher logo, no imprint, no badge, no seal, no age roundel, no painted
frame or border, no barcode, and no words other than the text given below.
========================================

BARCODE ZONE (CRITICAL): the BOTTOM-RIGHT of the image - the right 42% of the
width by the bottom 20% of the height - must stay calm, dark, empty
background: no text, no focal detail, no bright object.
Do NOT paint a grey, cream or white rectangle there, and do NOT paint a
barcode. The printer places the real barcode on top of the plain background.

LAYOUT AND SAFE ZONES - a strip along every edge will be PHYSICALLY CUT AWAY.
- ALL text sits within the upper 76% of the height. The bottom 22% carries no
  text at all.
- Every line keeps at least 10% OF THE WIDTH free to the left and to the
  right, and at least 9% of the height free at the top.
- Do NOT stretch the text down the page. Set it compact in the upper area;
  calm empty background at the bottom is intended and correct.

BACKGROUND - THE EMPTY PLATFORM:
The same abandoned station as the front cover, but seen along the empty
platform with nobody in it. The tiled walls run away from the viewer on both
sides and frame the image like a soft dark vignette; the vaulted ceiling
closes over the top. Far away at the end, the black mouth of the tunnel, very
small. Thick pale dust on the floor. A faint cold glimmer on the old rails
below the platform edge.

‼️ THE CENTRE MUST STAY DARK, CALM AND ALMOST EMPTY. This is where the text
goes. Treat the middle of the image as a quiet, gently darkened wall of dusty
darkness - no tile detail, no bright object, no strong texture in the centre.

In the dust of the floor at the LOWER LEFT: a short trail of DOG PAW PRINTS
leading away from the viewer, toward the tunnel. That is the only trace that
anyone was here.

NO people, NO children, NO dog, NO ghost, NO figure of any kind, NO chalk
arrow on this side.

TEXT - render every word EXACTLY as written below, correctly spelled,
including the German letters ä, ö, ü and the dash —. Use the SAME classic
serif as the title on the attached front cover, in warm cream / off-white
(#e8e6e0), with a soft dark glow behind the letters so they stay readable.
All lines horizontal and centred, generous spacing between the blocks,
comfortable reading size. From top to bottom:

SERIES LINE (two lines, centred, title case - NOT all caps):
Die Geisterspürer
Band 3

QUOTE (italic, slightly larger, two lines, with a gap below):
„Unser Geisterhund freut sich.
Das ist schlimmer, als wenn er knurren würde."
— Theo, 10 Jahre

BODY (normal size, each line on its own line, small gaps between the groups,
do NOT merge into one paragraph):
Unter der Altstadt liegt eine U-Bahn-Station, die es
offiziell nicht mehr gibt. Kein Strom seit 1972. Ein
verrostetes Gitter, und dahinter Stufen, die nach vier
Schritten im Schwarzen verschwinden.

Schatten verweigert diesmal nicht. Er zieht.
Zum ersten Mal will er hinein.

Unten im Tunnel ist ein Pfeil an die Wand gemalt. Weiß,
mit Kreide, auf Augenhöhe. Die Kreide ist nicht alt.

Aus der Dunkelheit ruft eine Kinderstimme nach seiner
Mutter. Nora und Theo sind sicher, dass sie ein
verlorenes Kind suchen.

Sie irren sich. Und der Tunnel hat noch nicht vergessen,
was 1972 hier passiert ist.

FOOTER (small, two lines):
Grusel-Abenteuer für mutige Leser ab 10 Jahren —
Kribbeln ja, Albträume nein.

AUTHOR (small, centred, below the footer):
Benjamin Krug

IMPORTANT: spell every German word exactly as given, including ä, ö, ü and the
dash —. Keep all text in the upper area described above and completely clear
of the bottom-right corner. Do NOT invent or add any extra words, letters,
numbers, logos or signatures.

DO NOT INCLUDE: people, children, a dog, a ghost or any figure; skeletons,
bones, blood; a painted barcode or a light rectangle; a frame or border;
graffiti; modern elements; neon colours; manga or cartoon style.
```

### Variante B — Rückseite ohne Text (Rückfallebene)

`TEXT`-Block streichen und ersetzen:

```
NO TEXT ANYWHERE IN THE IMAGE. No letters, no numbers, no words, no watermark,
no signature. Just the empty dark platform. Keep the centre of the image calm,
even and darkened so that text can be placed on top afterwards.
```

---

## Checkliste nach der Generation

**Texte (Buchstabe für Buchstabe):**
- [ ] `DIE GEISTERSPÜRER` — Ü mit zwei Punkten
- [ ] `SCHATTEN SIEHT MEHR` — kein Umlaut
- [ ] `Ein Grusel-Abenteuer für Kinder ab 10 Jahren` — ü in „für"
- [ ] `BAND 3` vorhanden
- [ ] Wandschrift: **`ALTSTADT-NORD` mit Bindestrich**, `1972` — oder gar nichts.
      Verstümmelte Buchstaben sind schlimmer als leere Schilder
- [ ] Keine erfundenen Wörter, kein Graffiti, keine Plakate

**Bild:**
- [ ] **Schatten ist VORNE und zieht** — Leine straff **nach vorn** (Umkehrung
      von Band 2, wo sie nach hinten straff ist)
- [ ] Schattens **Bernsteinauge** sichtbar — das einzige Warm im kalten Bild
- [ ] **Der Kreidepfeil sieht frisch aus** — helles, sauberes Weiß gegen
      fünfzig Jahre Dreck
- [ ] **Das Tunnelmaul ist leer** — keine Gestalt, kein Kind, keine Frau,
      keine leuchtenden Augen. Der Twist darf nicht verraten werden
- [ ] Nur **eine** Lichtquelle: Noras Taschenlampe. Kein Notlicht, kein Strom
- [ ] Nora **Teal**, Theo **Oliv**, nicht vertauscht
- [ ] **Titel in Gold** (`#dfb057`) — Reihenstandard seit 2026-08-05, gemessen
      an Band 2 und 3. Band 1 bleibt als einziger kalkweiß (bereits veröffentlicht)
- [ ] Kein gemalter Rahmen, kein Siegel

**Technik:**
- [ ] Aller Text innerhalb der zentralen **82 %** der Breite, **9 %** oben/unten frei
- [ ] Rückseite: Barcode-Zone unten rechts leer, **kein gemaltes helles Feld**
- [ ] Beide Bilder mindestens **1838 × 2775 px**
- [ ] **Thumbnail-Test bei 150 px:** Titel lesbar? Taschenlampenkegel und
      schwarzes Tunnelmaul erkennbar? Dreiergruppe klar?

---

## Ablauf Band 3

- [ ] 1. Vorderseite generieren (4–6 Varianten), Texte prüfen
- [ ] 2. Rückseite generieren mit der gewählten Front als Referenz
- [ ] 3. Falls nötig hochskalieren auf ≥ 1838 × 2775
- [ ] 4. Ablegen als `Band3/Cover/Bilder/front_band3.jpg` und `back_band3.jpg`
- [ ] 5. `py Scripts/build_cover.py 3`
- [ ] 6. Kontrollbild und Thumbnail ansehen
- [ ] 7. KDP-Previewer
