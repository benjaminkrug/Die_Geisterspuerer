# Cover-Prompt Band 1 — Das Haus, das flüstert (Neubau 2026-08-04)

> Gilt zusammen mit `Dokumentation/Cover_Reihenstandard.md`. Die Blöcke A–E von
> dort sind unten eingesetzt; geändert wird der Standard dort, nicht hier.
>
> **Ersetzt** `Cover_Prompt_Band1_v5_FINAL.md`. Format: **6 × 9 Zoll** (Band 1
> lief bisher als einziger Band auf 5 × 8 — er wird umgestellt).

---

## Was am alten Band-1-Cover nicht stimmte

Nachgemessen am ausgelieferten Bild, nicht vermutet:

| Befund | Folge |
|---|---|
| **1024 × 1536 px = 166 dpi** | schlechteste Auflösung der Reihe, ~1,8× Upscale nötig |
| **Untertitel steht unterhalb der Sicherheitslinie** | kann im Druck angeschnitten werden |
| **Reihenname groß, Buchtitel klein in Schreibschrift** | umgekehrt zu Band 2–5 — der Käufer sieht nicht, wie das Buch heißt |
| **Keine Bandnummer** | im Regal nicht als Reihe erkennbar |
| **5 × 8 Zoll** | kleineres Buch als der Rest der Reihe |
| Rückseite im Repo gehört zum **Spielbuch**, nicht zum Roman | eine Roman-Rückseite existiert nicht |

**Was gut war und bleibt:** die Bildidee. Ein Altbau bei Nacht, gestaffeltes
Licht in den Stockwerken, **ein Fenster kalt und blau mit dem Wort HILF im
Kondenswasser** — das ist der Kern des Buchs (Kapitel 3 und 4, wörtlich), es
funktioniert im Thumbnail, und kein anderer Band der Reihe sieht so aus.

---

## Design-Entscheidungen Band 1

| Regel | Umsetzung |
|-------|-----------|
| **70 % Hintergrund** | Ein einzelner alter Gravenstedter Altbau bei Nacht, von unten gesehen. Tiefes Indigo/Violett, nasses Kopfsteinpflaster. |
| **20 % Titel** | `DAS HAUS, DAS FLÜSTERT` — zweizeilig, dominant. Erstmals ist der **Titel** der große Text, nicht der Reihenname. |
| **10 % Hingucker** | **Das eine kalte, beschlagene Fenster mit HILF.** Ein Wort, von einem Kinderfinger ins Kondenswasser geschrieben. |
| **Lichtstaffelung** | Erdgeschoss ganz dunkel · **erster Stock warm bernstein — bis auf EIN Fenster, das kalt blau und beschlagen ist** · zweiter Stock ganz dunkel. Das Falsche sitzt mitten in der warmen Reihe, im eigenen Zuhause. |
| **Differenzierung** | B1 = **Indigo + kaltes Blau** · B2 Waldgrün · B3 Stahlblau · B4 Blaugrau+Gold · B5 Braunschwarz+Silber |
| **Kein Geist** | Lina erscheint **nicht**. Nur ihr Wort. Serienregel — und es stellt eine Frage, statt sie zu beantworten. |
| **Thumbnail-Anker** | Genau drei Dinge: der Titel, das blaue Fenster, Schattens Bernsteinauge. |
| **Ton** | Grusel 3/10 — der sanfteste Band. Das Haus ist unheimlich, nicht bedrohlich. |

**Warum Lina nicht aufs Cover kommt:** Ein Kind, das ein Wort an ein Fenster
schreibt, ist unheimlicher als ein gemaltes Gespenst — und ein gemaltes
Gespenst wäre der einzige Band der Reihe mit einer klaren Geistergestalt.
Band 2 hat diesen Fehler gemacht (zwei Geister mit Gesichtern).

### Zwei Korrekturen gegenüber dem alten Cover — beide gegen das Manuskript geprüft

**1. Das Wort steht im ERSTEN Stock, nicht im zweiten.**
Auf dem alten Cover glüht ein Fenster im zweiten Stock kalt blau und trägt das
Wort. Das Buch sagt etwas anderes:

- Kapitel 1: *„Erste Etage. Ihr werdet sie mögen."* — dort wohnen Nora und Theo.
- Kapitel 3: *„Sonnenlicht fiel durch das Küchenfenster … Die Scheibe war
  beschlagen … Es waren Buchstaben. Auf Augenhöhe, mit dem Finger geschrieben."*

Das Wort steht in **ihrer eigenen Küche**, im ersten Stock. Der zweite Stock ist
Frau Silbers leere Wohnung — der kalte Raum, aber **ohne Schrift am Fenster**.

Deshalb neu: Erdgeschoss dunkel, **erster Stock warm bernstein — und genau eines
dieser warmen Fenster ist beschlagen und kalt blau**, mit HILF darin. Zweiter
Stock ganz dunkel.

Das ist nicht nur richtiger, es ist stärker: Ein kaltes Fenster in einer Reihe
warmer Fenster **auf derselben Etage** ist ein schärferer Kontrast als eines,
das ein Stockwerk höher allein steht. Und es sagt genau das, was das Buch sagt —
das Falsche ist nicht oben im leeren Stockwerk, es ist **bei ihnen zu Hause**.

**2. Die angelehnte Haustür entfällt.**
Sie stand nicht im Buch, und sie war ein zweiter dunkler Blickfang neben dem
Fenster. Die Reihe erlaubt genau einen. Stattdessen sitzt Schatten vor dem
geschlossenen Haus auf dem Pflaster — das steht wörtlich in Kapitel 7:
*„Draußen saß Schatten auf dem Pflaster … Er starrte auf ihr Haus.
Kirchgasse 14."*

### Die eine bewusste Abweichung

Ein Wort, das von innen in beschlagenes Glas geschrieben wurde, erscheint von
der Straße aus **spiegelverkehrt**. Auf dem Cover steht es trotzdem lesbar.
Das ist eine bewusste Entscheidung, kein Versehen: spiegelverkehrt wäre es im
Thumbnail unleserlich und würde wie ein Fehler aussehen. Falls dir das wichtiger
ist als die Lesbarkeit, sag Bescheid — der Prompt lässt sich in einem Satz
umstellen.

---

## HAUPT-PROMPT — VORDERSEITE

> Bildformat **2 : 3 hochkant**, so groß wie möglich erzeugen. Anschließend auf
> mindestens **1838 × 2775 px** hochskalieren.

```
========================================
READ THIS BLOCK FIRST - IT OVERRIDES ANY EARLIER CONTEXT
========================================

This cover belongs to the German children's series "DIE GEISTERSPÜRER"
(The Ghost Trackers), for ages 10-12. It is NOT "Die Herrenhaus-Detektive"
and NOT any other series. Ignore any other book series, title, manor house
or branding from earlier in this conversation.

EXACTLY these four texts appear on the cover - no others, none invented:
  1. series line : DIE GEISTERSPÜRER · BAND 1
  2. main title  : DAS HAUS, DAS FLÜSTERT
  3. subtitle    : Ein Grusel-Abenteuer für Kinder ab 10 Jahren
  4. author      : Benjamin Krug

Forbidden anywhere: any publisher name, imprint or logo; any badge, seal,
sticker, ribbon, banner or emblem; any age roundel; any painted frame or
border around the artwork; any word not in the four texts above.
========================================

SAFE MARGINS (CRITICAL - the outer edges are trimmed off when the book is
printed, and the e-book version is cropped narrower still):
- EVERY line of text must sit inside the central 84% of the width. There must
  be clearly visible empty background - at least the width of two capital
  letters - to the LEFT of the leftmost letter and to the RIGHT of the
  rightmost letter of every single line.
- Keep at least 6% of the height free of text at the TOP and at the BOTTOM.
- NO letter may touch or approach an outer edge.
- Better a slightly smaller title with clear margins than a big title that
  reaches the edge. When in doubt, shrink the text.
- The illustration itself still fills the whole image to all four edges -
  only the TEXT stays inside the safe area.

Children's book cover illustration, painterly semi-realistic digital painting
with visible brushwork, rich texture and cinematic lighting. It should look
like a film poster for a middle-grade ghost-adventure for ages 10-12. NOT
chibi, NOT manga, NOT flat-colour cartoon, NOT photorealistic, NOT cute, NOT
gory. Vertical book cover, portrait 2:3.

Built around ONE idea: a single word written by a child's finger in the
condensation of a cold blue window, high up in an old apartment house at
night.

VERTICAL LAYOUT (top to bottom - this ordering keeps the title and the glowing
window out of each other's way):
- TOP ~32% : night sky and the roofline of the house, dark and calm. The
  SERIES LINE, the MAIN TITLE and the SUBTITLE all sit inside this band and
  never reach below it.
- MIDDLE ~34-62% : the facade with its levels of light. The one COLD BLUE
  FOGGED WINDOW sits at about 48% of the height, slightly right of centre.
  This is the eye-catcher.
- LOWER THIRD ~66-100% : the two children and the dog, seen from behind, on
  wet cobblestones in front of the house. The AUTHOR NAME sits at the very
  bottom, on the dark cobblestones, clear of the figures.
Keep a clear band of dark sky between the bottom of the subtitle and the top
of the lit windows so they never overlap.

SETTING (70%) - THE HOUSE:
ONE single old German Altbau apartment house, three storeys, a grey plastered
facade cracked like an old face, tall narrow windows with peeling paint, an
ornate stone doorway with a closed front door. Seen from slightly below so the
building looms over the viewer. It fills the centre and upper half of the
image. The street is narrow and still; the neighbouring houses lean toward
each other and are only dark suggestions at the edges. Thin fog. Wet
cobblestones in the foreground reflect the window light in long vertical
streaks. Cold silver moonlight from the upper left.

THE LIGHT ON THE FACADE - get this exactly right, it is the whole picture:
- GROUND FLOOR windows: COMPLETELY DARK. No light at all.
- SECOND (top) FLOOR windows: COMPLETELY DARK as well. Nobody lives there.
- FIRST FLOOR (the middle row): the windows glow WARM golden-amber (#d4920b),
  soft and lived-in - EXCEPT ONE.
- THAT ONE WINDOW, in the middle of the warm row, is FOGGED OVER on the
  inside and glows COLD BLUE (#c8dff5) instead: a flat, milky, colourless
  blue, obviously wrong beside the warm windows on either side of it.
  The contrast between the warm windows and this single cold one, ON THE SAME
  FLOOR, is the point of the picture. Do not move the cold window to another
  floor and do not make a second one cold.

THE WORD (the focal point):
Into the misted condensation of that one cold window, at eye height, a single
German word has been drawn with a fingertip. The strokes are clumsy and
dragging, and where the finger wiped the glass clear, the light behind shines
through, so the LETTERS THEMSELVES GLOW brighter than the milky pane around
them. Small droplets run down from each stroke.

    HILF

Four capital letters, plainly legible and correctly oriented (not mirrored).
Do not add any further letters and do not complete it to "HILFE". It should be
small in the frame but unmistakable - the thing a reader's eye finds second,
right after the title.

THE THREE FIGURES - ALL SEEN FROM DIRECTLY BEHIND, in the lower third,
standing close together on the wet cobblestones, looking UP at the blue
window. The viewer stands behind them and looks past their shoulders. We see
the BACK of their heads. Their faces are simply not in the picture - not in
profile, not in three-quarter view, not glimpsed. This is a fixed rule of the
series. They are NOT flat silhouettes: they are fully painted figures lit from
the front by the windows above, so their clothing colours read clearly even
though they are seen from behind.

NORA (girl, 12) - LEFT. Straight shoulder-length MID-BROWN hair (not red, not
blonde). DARK TEAL zip-up hoodie (#2a8a7a), a clear blue-green. This is her
fixed series colour and must be plainly visible. Head tilted back, looking up.

THEO (boy, 10) - RIGHT, smaller, half a step behind his sister. Messy slightly
curly DARK-BLOND hair. Oversized MILITARY OLIVE-GREEN bomber jacket (#6b7a3a),
a dull yellow-green. His fixed series colour, plainly visible. Shoulders
pulled up, hands in his pockets - he does not want to be here.

DO NOT SWAP THESE COLOURS: the GIRL wears TEAL, the BOY wears OLIVE. Readers
identify them by exactly this.

SCHATTEN (the dog) - CENTRE, between and slightly ahead of the two children.
Medium-sized shaggy mixed-breed, dark almost-black fur, visibly THIN with a
matted, unkempt coat - a stray. A plain narrow LEATHER COLLAR (no harness, no
chest straps, no vest). He sits upright on the wet cobblestones, facing the
house, ears forward, head turned in profile toward the cold window so that ONE
eye is visible: a LUMINOUS AMBER EYE (#d4920b), glowing from within. It is the
single living warm point of the cover and must stay visible at thumbnail size.
He is completely still - he has been sitting here, staring at this house, for
a long time.

LIGHTING - SINGLE-SOURCE DISCIPLINE: all light in this picture comes from the
windows of the house and from cold moonlight. Trace every highlight back to
one of those. The children are lit from the front, by the house. No street
lamp, no torch, no flashlight, no car lights.

COLOUR PALETTE (70/20/10):
- DOMINANT: deep indigo night (#1a1a3e), violet-black shadow (#2d1b4e),
  wet-stone grey-blue.
- TYPOGRAPHIC: chalk-bone-white (#e8e6e0) title, steel-grey (#9aa6b0) series
  line and subtitle.
- ACCENT: warm amber windows and the dog's eye (#d4920b), and the one COLD
  BLUE window (#c8dff5).
The picture must NOT be uniformly dark - the contrast between warm amber
windows and the single cold blue one is what carries it.

TITLE TYPOGRAPHY (rendered inside the image, top ~32%):
CRITICAL SPELLING - render every German word letter-perfect:
- The series line MUST read "DIE GEISTERSPÜRER" with the umlaut Ü (TWO DOTS
  above the U - not an accent, not a grave, not a tilde).
- The main title MUST read "DAS HAUS, DAS FLÜSTERT" - with the COMMA after
  "HAUS" and the umlaut Ü in "FLÜSTERT".
- The subtitle MUST read "für" with ü.

SERIES LINE (small, at the very top, thin widely spaced capitals, steel-grey
#9aa6b0):
DIE GEISTERSPÜRER · BAND 1

MAIN TITLE (large, clearly the dominant text on the cover, heavy carved
capitals, slightly condensed, chalk-bone-white #e8e6e0 with a hard dark shadow
so it stays readable against the night sky). Set on TWO centred lines:
    DAS HAUS,
    DAS FLÜSTERT
The comma at the end of the first line is required. The second line is the
wider and more dominant one. The whole title block stays in the top third and
must not reach down into the lit windows.

SUBTITLE (small, clean, single line, steel-grey, directly below the title with
a comfortable gap - and still inside the calm dark top band, well above the
lit windows):
Ein Grusel-Abenteuer für Kinder ab 10 Jahren

AUTHOR (small, centred, at the very bottom of the cover, on the dark wet
cobblestones below the figures, light grey - inside the safe margin, not
overlapping the children or the dog):
Benjamin Krug

DO NOT INCLUDE: children's faces or any face in profile; a clearly rendered
ghost figure, a girl at the window, a face or silhouette behind the glass; an
open or ajar front door; monsters,
skeletons, bones, blood, gore, scary grimaces; a third child or any additional
person; publisher logos, badges, seals, age roundels; a painted frame or
border around the image; modern elements, cars, phones, screens; neon colours;
manga, anime or flat cartoon style; any text beyond the four given lines and
the word HILF in the window.

MOOD: a new city, a house that is too old, a dog that will not leave, and one
window that says something. Uneasy and inviting at the same time - the gentlest
book of the series (scare level 3 out of 10). Kribbeln, kein Albtraum.
```

### Nachfass-Sätze

| Problem | Nachfassen mit |
|---|---|
| Umlaut falsch (`Geisterspùrer`) | *„The series line is misspelled. It must read exactly DIE GEISTERSPÜRER — the U has TWO DOTS above it (an umlaut), not an accent. Fix only the text, keep the image."* |
| Komma im Titel fehlt | *„The title is missing the comma. Line one must read exactly: DAS HAUS, — with a comma at the end."* |
| HILF unleserlich / falsch | *„The word in the window must read exactly HILF — four capital letters, H-I-L-F, no more. Written by a fingertip in the condensation, with drips running down."* |
| Ein Geist im Fenster | *„Remove the figure at the window. The window shows only the blue glow and the written word — no person, no face, no silhouette behind the glass."* |
| Alle Fenster gleich hell | *„Ground floor windows completely dark, first floor warm amber, and exactly ONE second-floor window cold blue. The other second-floor windows are dark."* |
| Gesichter sichtbar | *„All three figures are seen from directly behind. We see the backs of their heads only — no faces, not even in profile."* |
| Titel zu nah am Rand | *„The title touches the edge. Make it smaller and leave at least 8% empty background on the left and on the right of every line."* |
| Kinderfarben falsch | *„The GIRL on the left wears a dark TEAL hoodie (blue-green). The BOY on the right wears an OLIVE-GREEN bomber jacket (yellow-green). Do not swap them."* |

---

## PROMPT — RÜCKSEITE

> **Referenzbild anhängen: die gewählte Vorderseite** (ChatGPT-Fassung,
> Kirchgasse 14 bei Nacht). Die Rückseite soll zur eigenen Front passen, nicht
> zu einem anderen Band. Der Prompt unten ist bereits **auf dieses Bild
> abgestimmt** — indigoblaue Nacht, Mond, nasses Kopfsteinpflaster mit warmen
> Lichtreflexen, grauer rissiger Putz, kahle Äste, Bodennebel.
>
> ⚠️ **Das ist der riskanteste Prompt der ganzen Reihe.** Er verlangt vom
> Bildmodell rund 110 deutsche Wörter mit Umlauten. Auf Band 2 ist der
> Bildgenerator schon an **zwei** Wörtern gescheitert („Die Geisterspùrer").
> **4–6 Varianten erzeugen und Wort für Wort gegenlesen.** Wenn keine sauber
> ist: Variante B unten (Hintergrund ohne Text, Satz separat) — das kostet
> zwanzig Minuten und ist danach fehlerfrei.
>
> Gutes Zeichen: Auf der Vorderseite hat dasselbe Modell `GEISTERSPÜRER`,
> `FLÜSTERT` und `für` **fehlerfrei** gesetzt, inklusive Komma. Die Chance steht
> also besser als bei Band 2 damals.

```
========================================
READ THIS BLOCK FIRST - IT OVERRIDES ANY EARLIER CONTEXT
========================================
This is the BACK COVER of the same book as the attached front cover: the
German children's ghost-adventure "DAS HAUS, DAS FLÜSTERT", Band 1 of the
series "DIE GEISTERSPÜRER", ages 10-12. Take the art style, brushwork, palette
and night mood EXACTLY from the attached front cover - same painterly
semi-realistic digital painting, same deep indigo night, same cold moonlight,
same wet cobblestones with long warm reflections, same grey cracked plaster,
same thin ground fog. The two images must look like one object folded open.

Portrait 2:3, same proportions as the front.

No publisher logo, no imprint, no badge, no seal, no age roundel, no painted
frame or border, no barcode, and no words other than the text given below.
========================================

BARCODE ZONE (CRITICAL): the BOTTOM-RIGHT of the image - the right 42% of the
width by the bottom 20% of the height - must stay calm, dark, empty
background: no text, no focal detail, no bright object.
Do NOT paint a grey, cream or white rectangle there, and do NOT paint a
barcode. The printer places the real barcode on top of the plain background.

LAYOUT AND SAFE ZONES:
- ALL text sits within the upper 78% of the height. The bottom 20% carries no
  text at all.
- Every line keeps at least 8% of the width free to the left and to the right,
  and at least 6% of the height free at the top.
- Do NOT stretch the text down the page. Set it compact in the upper area;
  calm empty background at the bottom is intended and correct.

BACKGROUND - THE SAME STREET, TURNED AROUND:
We now stand where the children stood on the front cover and look the OTHER
WAY: down the empty, narrow Kirchgasse, away from the house. Wet cobblestones
run away from the viewer into thin fog that swallows the far end of the lane.
Tall old plastered housefronts - the same weathered grey, the same cracked
render as on the front - rise steeply on the LEFT and RIGHT edges and frame the
image like a soft dark vignette. Bare black branches reach in from the upper
left, exactly like the tree on the front cover. Between the rooftops, a narrow
strip of deep indigo night sky (#1a1a3e) with the same drifting clouds; the
moon is out of frame here, only its cold silver light remains.

‼️ THE CENTRE MUST STAY DARK, CALM AND ALMOST EMPTY. This is where the text
goes. Treat the middle of the image as a quiet, gently darkened wall of night -
as if a soft dark overlay lay over it. No architecture detail, no bright
object, no strong texture in the centre.

The ONLY warmth: two or three small WARM AMBER window reflections lying in the
wet cobblestones near the bottom, from windows we cannot see. They echo the
front cover's reflections and tie the two sides together. Keep them low and
small - they must not compete with the text.

In the wet cobblestones at the LOWER LEFT: a short trail of small DOG PAW
PRINTS leading out of the picture, and one or two dry autumn leaves. That is
the only trace that anyone was here.

NO people, NO children, NO dog, NO ghost, NO figure of any kind, NO lit window
visible directly, NO street lantern that is switched on.

TEXT - render every word EXACTLY as written below, correctly spelled,
including the German letters ä, ö, ü and the dash —. Use the SAME classic
serif as the title on the attached front cover, in warm cream / off-white
(#e8e6e0), with a soft dark glow behind the letters so they stay readable
against the night. All lines horizontal and centred, generous spacing between
the blocks, comfortable reading size - this is a back cover, the text is the
main element here, not decoration. From top to bottom:

SERIES LINE (two lines, centred, in the same title-case serif as the other
Geisterspürer back covers - NOT all caps):
Die Geisterspürer
Band 1

QUOTE (italic, slightly larger, two lines, with a gap below):
„Kondenswasser schreibt keine deutschen Wörter!"
— Theo, 10 Jahre

BODY (normal size, each line on its own line, small gaps between the groups,
do NOT merge into one paragraph):
Nora und Theo ziehen nach Gravenstedt, in eine alte Wohnung
in der Kirchgasse 14. Die Wände knarren. Im Stockwerk darüber
steht eine Wohnung leer, in der es eiskalt ist — mitten im Juli.
Und vor der Haustür sitzt ein dünner Hund mit bernsteinfarbenen
Augen, der nicht weggeht.

Nachts beginnt das Klopfen. Dreimal. Pause. Dreimal.

Am Morgen steht ein Wort im beschlagenen Küchenfenster: HILF.

Nora glaubt an kalte Leitungen und Zugluft. Bis Schatten sie die
Treppe hinaufführt, in die leere Wohnung. Dort liegt eine Liste
mit Namen — und die Geschichte eines Mädchens, das vor fünfzig
Jahren in genau dieser Wohnung gelebt hat.

CLOSING LINE (italic):
Ein Mädchen, das nicht vergessen werden wollte.

FOOTER (small, two lines):
Grusel-Abenteuer für mutige Leser ab 10 Jahren —
Kribbeln ja, Albträume nein.

AUTHOR (small, centred, below the footer):
Benjamin Krug

IMPORTANT: spell every German word exactly as given, including ä, ö, ü and the
dash —. Keep all text in the upper area described above and completely clear of
the bottom-right corner. Do NOT invent or add any extra words, letters,
numbers, logos or signatures.

DO NOT INCLUDE: people, children, a dog, a ghost or any figure; monsters,
skeletons, blood; a painted barcode or a light rectangle; a frame or border;
modern elements, cars, phones; neon colours; manga or cartoon style.
```

### Variante B — Rückseite ohne Text (Rückfallebene)

Wenn nach 4–6 Versuchen keine Variante fehlerfrei ist: denselben Prompt
verwenden, den kompletten `TEXT`-Block streichen und stattdessen einsetzen:

```
NO TEXT ANYWHERE IN THE IMAGE. No letters, no numbers, no words, no
watermark, no signature. Just the empty night alley. Keep the centre of the
image calm, even and darkened so that text can be placed on top afterwards.
```

Der Textblock oben wird dann in Canva/Affinity gesetzt: zentriert, Creme
`#e8e6e0`, klassische Serife, weicher dunkler Schein hinter der Schrift.
**Kein Textpixel innerhalb von 8 % der Breite an den Seiten** und nichts in der
Barcode-Zone unten rechts.

---

## Checkliste nach der Generation

**Texte (Buchstabe für Buchstabe, nicht überfliegen):**
- [ ] `DIE GEISTERSPÜRER` — Ü mit **zwei Punkten**, kein Akzent (Band 2 hat hier `ù`)
- [ ] `DAS HAUS, DAS FLÜSTERT` — **Komma** nach HAUS, **Ü** in FLÜSTERT
- [ ] `Ein Grusel-Abenteuer für Kinder ab 10 Jahren` — ü in „für"
- [ ] `Benjamin Krug`
- [ ] `BAND 1` vorhanden
- [ ] Keine erfundenen Zusatzwörter, kein Verlagslogo, kein Siegel
- [ ] Rückseite: `„Kondenswasser schreibt keine deutschen Wörter!"` — **mit
      Ausrufezeichen**, so steht es in Kapitel 4, und es ist **Theos** Satz
- [ ] Rückseite: **die Mutter wird nicht genannt** — sie hat in den Büchern
      keinen Namen (der Name „Sarah" steht nur in der alten Outline)

**Bild:**
- [ ] Das Wort im Fenster liest sich als `HILF` — vier Buchstaben, nicht „HILFE"
- [ ] Die Buchstaben **leuchten heller** als die beschlagene Scheibe (Finger hat
      das Glas freigewischt), Tropfen laufen herunter
- [ ] **Erdgeschoss dunkel, zweiter Stock dunkel, erster Stock warm** — und
      genau **ein** Fenster in der warmen Reihe kalt blau und beschlagen
- [ ] Haustür **geschlossen** (kein Spalt, kein Nebel darunter)
- [ ] **Keine Gestalt am Fenster**, kein Geist, kein Gesicht
- [ ] Alle drei Figuren **von hinten**, keine Gesichter
- [ ] Nora **Teal**, Theo **Oliv**, nicht vertauscht
- [ ] Schattens **Bernsteinauge** sichtbar
- [ ] Halsband, kein Geschirr
- [ ] Kein gemalter Rahmen ums Bild

**Technik:**
- [ ] Aller Text innerhalb der zentralen 84 % der Breite, 6 % oben/unten frei
- [ ] Rückseite: Barcode-Zone unten rechts leer, **kein gemaltes helles Feld**
- [ ] Beide Bilder auf **mindestens 1838 × 2775 px** hochskaliert
- [ ] **Thumbnail-Test bei 150 px:** Titel lesbar? Blaues Fenster erkennbar?
      Bernsteinauge sichtbar? Wenn nicht: Fenster größer, Titel schwerer.

---

## Ablauf Band 1

- [ ] 1. Manuskript auf **6 × 9** umbauen, bei KDP hochladen, **echte Seitenzahl** notieren
- [ ] 2. Vorderseite generieren (4–6 Varianten), Texte prüfen
- [ ] 3. Rückseite generieren mit der gewählten Front als Referenz
- [ ] 4. Beide auf ≥ 1838 × 2775 hochskalieren
- [ ] 5. Ablegen als `Band1/Cover/Bilder/front_band1.png` und `back_band1.png`
- [ ] 6. Seitenzahl in `Scripts/build_cover.py` eintragen, `bestaetigt = True`
- [ ] 7. `py Scripts/build_cover.py 1`
- [ ] 8. Kontrollbild und Thumbnail ansehen
- [ ] 9. KDP-Previewer
