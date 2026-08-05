# Illustrationen-Prompts — Die Geisterspuerer Band 1 CYOA

15 Schwarz-Weiss-Illustrationen (Pen-and-Ink, Crosshatching) fuer das interaktive Taschenbuch.

---

## Stil-Vorgabe (fuer alle 15 Illustrationen identisch)

**Stil-Prefix (immer zuerst einfuegen):**

```
Black and white pen-and-ink illustration for a German children's ghost story book, target age 10-12. Style: detailed crosshatching, deep atmospheric shadows, genuinely spooky but never gory or bloody. Heavier on shadow and darkness than typical children's books. Similar to classic 'Gaensehaut' (Goosebumps) or 'Gruselgeschichten' interior illustrations, but with the fine detail of 'Die drei Fragezeichen' pen-and-ink work.

MANDATORY RULES FOR ALL ILLUSTRATIONS:
- Pure black and white. No color. No greyscale wash. Only ink lines and crosshatching.
- No manga style. No anime style. No cartoon style. No chibi. No exaggerated proportions.
- Realistic proportions for European children aged 10-12.
- No text, no speech bubbles, no captions, no watermarks, no signatures inside the image.
- No logos, no brand names, no recognizable commercial products.
- No weapons, no blood, no wounds, no gore, no body horror, no decomposition.
- No sexualized content of any kind.
- No modern technology unless explicitly specified (no smartphones, no laptops, no tablets, no headphones, no earbuds, no smartwatches).
- No animals other than the one dog (Schatten) unless explicitly specified. No cats, no birds, no insects, no spiders, no bats, no rats, no mice.
- No food or drink items unless explicitly specified.
- No plants or flowers unless explicitly specified.
- No wall decorations, posters, paintings, or photographs unless explicitly specified.
- The dog (Schatten) must ALWAYS look identical: medium-sized mixed breed, thin but healthy, wiry dense BLACK fur, pointed upright ears, AMBER EYES rendered as bright white highlights against dark fur. No collar. No leash. No tags. He looks like a black German Shepherd/Belgian Malinois mix, but thinner and wirier.

TECHNICAL:
- Portrait orientation (taller than wide).
- High contrast between deep black shadows and white highlights.
- Fine detailed crosshatching for midtones and textures.
- Resolution: minimum 2000x3000 pixels, 300 DPI.
```

---

## Verteilung ueber Pfade

| Bereich | Illustrationen | Leser sieht |
|---------|---------------|-------------|
| Prolog (alle lesen) | 4 | Alle |
| Pfad A (Schatten folgen) | 4 | ~33% |
| Pfad B (Bibliothek) | 3 | ~33% |
| Pfad C (Mama erzaehlen) | 3 | ~33% |
| Endings | 1 | variiert |
| **Gesamt** | **15** | **7-9 pro Leser** |

---

## ILLUSTRATION_MAP (fuer build_cyoa_taschenbuch_v3.py)

```python
ILLUSTRATION_MAP = {
    "P1":   [2],      # Kirchgasse 14
    "P2":   [3],      # Charakterbild
    "P3":   [4],      # HILF am Fenster
    "A04":  [5],      # Der kalte Raum
    "A11":  [6],      # Sie ist hier
    "A29":  [7],      # Die Karte (Close-up)
    "A34":  [8],      # Graven am Friedhof
    "B04":  [9],      # Rote Tinte
    "B16":  [10],     # Der Schluessel
    "B21":  [11],     # Helds Warnung
    "C03":  [12],     # Theo rebelliert
    "C05":  [13],     # Mama traeumt
    "C07e": [14],     # Staffeluebergabe
    "E23":  [15],     # Mamas Frage
}
```

Illustration 1 (Stadtkarte) wird als separate Seite in Front Matter eingefuegt.

---

## 15 Illustrationen — Vollstaendige Prompts

---

### Illustration 1: Stadtkarte von Gravenstedt
**Platzierung:** Separate Seite nach Charaktere-Seite, vor Anleitung (Front Matter)

```
[Stil-Prefix einfuegen]

A hand-drawn map of a fictional German city called "Gravenstedt". The map fills the entire image. There are no human figures, no animals except one small dog drawing, and no three-dimensional buildings. This is a FLAT, top-down city plan drawn in ink on old paper.

FORMAT: The image shows ONLY the map. No border frame, no hands holding it, no table underneath it. The map fills edge to edge.

THE PAPER:
- Yellowed parchment-colored background (rendered in ink as light stippling/texture).
- The edges are torn and uneven — the paper is old and fragile.
- One coffee ring stain in the upper-left corner, rendered as a faint circular ink mark. ONLY ONE coffee stain. No other stains.
- No folds, no creases, no burn marks.

THE MAP CONTENT (bird's-eye view, flat 2D plan):
- A network of streets drawn as thin black ink lines.
- EXACTLY these street names written in small, slightly shaky old-woman's handwriting: "Kirchgasse", "Marktplatz", "Friedhofstrasse", "Schulweg", "Am Brunnen".
- A small church with a steeple icon at the center, labeled "Kirche".
- A small fountain icon at a square, labeled "Marktplatz".
- Blocks of buildings represented as simple rectangular outlines (no 3D, no roofs, just floor-plan blocks). Buildings are 3-5 stories indicated by tiny numbers ("3", "4", "5") next to some blocks.
- Streets are narrow and winding — an old European city, not a grid.

KEY LOCATIONS (each labeled in careful handwriting):
- "Kirchgasse 14" — one building block on a side street, marked with a THICK BLACK CIRCLE drawn around it (thicker ink than the map lines, clearly emphasized). Next to it in handwriting: "Lina". A tiny star above the building labeled "Silber" (indicating the top floor).
- "Bibliothek" — a wider building block near the Marktplatz.
- "Friedhof" — at the BOTTOM-RIGHT EDGE of the city, outside the street network. Drawn as a rectangle with tiny crosses inside (graves). Surrounded by 6 small tree icons. ONE grave at the center of the cemetery is marked with a heavy BLACK X. Next to the X in HEAVY, PRESSED handwriting: "GRAVEN". The X and the word GRAVEN are drawn with thicker, darker lines than anything else on the map — the pen was pressed hard, almost tearing the paper.

ELEVEN ADDITIONAL CIRCLES scattered at different locations across the map. Each circle is drawn with THICK ink (same weight as Kirchgasse 14). No labels next to these circles — just empty thick circles at various addresses. EXACTLY eleven circles plus the one at Kirchgasse 14 = twelve total.

DECORATIVE ELEMENTS:
- An ornate compass rose in the BOTTOM-LEFT corner. Simple 4-point design with N/S/O/W (German: Nord/Sued/Ost/West). Drawn in fine detailed ink.
- A decorative banner at the TOP CENTER: the word "GRAVENSTEDT" in gothic blackletter-style hand-drawn lettering. The banner is a simple scroll shape.
- In the BOTTOM-RIGHT corner (below the cemetery): a small pen-and-ink drawing of a sitting dog — thin, wiry, pointed ears, alert posture, facing toward the cemetery. This is Schatten. EXACTLY one dog. No other animals.

NOTHING ELSE ON THE MAP. No other decorations, no other text, no legend/key box, no scale bar, no date, no arrows, no additional drawings.

DO NOT include: Color of any kind. Three-dimensional buildings. Perspective drawing. Human figures. Multiple animals (only the one small dog drawing). Modern elements (cars, traffic lights, antennas). Rivers or bodies of water. Parks or green spaces (only the cemetery trees). Roads leading out of the city. A legend or key box. Page numbers. Frame or border around the map. Mountains or terrain. Bridges. Any text not explicitly listed above.
```

---

### Illustration 2: Kirchgasse 14 — Das Haus
**Platzierung:** Abschnitt P1 (nach Header, vor Text)

```
[Stil-Prefix einfuegen]

SCENE: A tall narrow apartment building on a quiet German side street, viewed from below (child's eye level, looking up). One dog sits in front of the open front door. No humans visible. No other animals.

VIEWPOINT: Low angle, from the cobblestone street looking up at the building facade. The building dominates the upper two-thirds of the image. The street occupies the lower third.

THE BUILDING (center of image, filling the width):
- EXACTLY 4 stories tall. Narrow — roughly the width of 3 windows per floor.
- Grey plaster walls with visible cracks and patches where plaster has chipped away, revealing brick underneath in 2-3 small spots.
- EXACTLY 12 windows total (3 per floor x 4 floors). All windows are dark. Windows on floors 1-3 have old half-drawn curtains. The 4th floor (top) has ONE window slightly ajar — the rest are shut.
- The front door is OPEN — a heavy old wooden door, dark brown, paint peeling in strips. The door stands open at roughly 45 degrees. Behind the door: pitch darkness — the hint of a narrow staircase going up, only the first 2-3 steps barely visible.
- ONE brass nameplate mounted on the wall to the right of the door — small, tarnished, text too small to read.
- No balconies. No awnings. No satellite dishes. No air conditioning units. No mailboxes on the outside. No graffiti. No house number visible.

THE DOG (in front of the door):
- Schatten sits on the stone threshold of the open door. Centered in the doorway.
- Sitting upright, perfectly still, facing the viewer directly.
- Thin, wiry black fur. Pointed upright ears. Amber eyes rendered as bright white highlights.
- His posture is REGAL — straight back, head high, ears forward. He is a guardian, not a stray.
- No collar. No leash. No bowl. No toys.

THE STREET:
- Cobblestone pavement (Kopfsteinpflaster) — uneven, old stones.
- To the LEFT of the building, partially out of frame: the back end of a plain white moving van (Umzugsauto). Only the rear doors are visible, one door open, 3 brown cardboard boxes visible stacked just inside. No writing on the van. No license plate visible.
- The building casts a LONG shadow across the street toward the viewer — rendered with dense crosshatching. The shadow is unnaturally long for summer.
- Sunlight hits the street from the upper right — bright, harsh summer light on the cobblestones OUTSIDE the shadow.
- No other buildings fully visible — only narrow slivers of neighboring facades at the very edges of the frame, cropped off.

NOTHING ELSE IN THE SCENE:
- No people — no pedestrians, no children, no adults, no silhouettes in windows.
- No other vehicles besides the moving van.
- No street lamps, no trash cans, no benches, no trees, no flower pots, no signs, no advertisements.
- No birds. No cats. No insects.
- No sky details — no clouds, no sun, no moon. The sky is white/empty above the building.

DO NOT include: People. Additional animals. Street furniture (lamps, benches, trash cans, parking meters). Shop signs. House numbers. Bicycles. Motorcycles. Visible graffiti. Flower boxes on windows. Curtains that are open and cheerful. A visible ghost or shadow figure in any window. A bright or inviting atmosphere — the building must feel COLD and WATCHING despite the summer sunlight.
```

---

### Illustration 3: Die Geschwister und der Hund (Charakterbild)
**Platzierung:** Abschnitt P2 (nach Header, vor Text)

```
[Stil-Prefix einfuegen]

SCENE: Three-quarter-length portrait of EXACTLY two children and EXACTLY one dog, standing together in an old stairwell. This is the CHARACTER INTRODUCTION image — it defines how these three look for all remaining illustrations.

VIEWPOINT: Straight-on, at the children's eye level. The three figures fill roughly 70% of the image height.

NORA (left side of image, 12 years old, female):
- HEIGHT: slightly tall for 12 — about 150cm. Slim build.
- HAIR: straight brown hair, shoulder-length, no bangs. Tucked behind her LEFT ear, hanging loose on the right side. Clean, practical cut. No hair accessories — no clips, no bands, no bows.
- FACE: determined expression. Jaw set firmly. Eyes sharp, observant, looking slightly to the right (toward the stairs behind them). Left eyebrow raised slightly. Mouth closed, lips pressed together. No makeup. No freckles. No glasses.
- CLOTHING: plain dark hoodie (no logo, no pattern, no zipper — pullover style), dark straight-leg jeans, plain dark sneakers with white soles. No jewelry. No watch. No backpack.
- POSE: standing slightly FORWARD compared to Theo — one small step ahead, protective. Right hand at her side with fingers loosely curled. Left hand resting on top of Schatten's head between his ears (casual, unconscious gesture). Weight on both feet, balanced, ready.

THEO (right side of image, 10 years old, male):
- HEIGHT: shorter than Nora by about 10cm — about 140cm. Thin, slight build. Still has round childish cheeks.
- HAIR: dark brown hair, short-ish but MESSY — sticking out in multiple directions as if he never combs it. Cowlick at the crown.
- FACE: mixed expression — mouth slightly open (about to say something sarcastic), but eyes are WIDE and nervous. Eyebrows raised. No glasses. No freckles.
- CLOTHING: pajama top with small ASTRONAUT PRINT (tiny rockets and stars pattern across the fabric — clearly visible), regular dark jeans (he dressed in a hurry — pajama top with day jeans). Plain socks, no shoes. No watch. No jewelry.
- POSE: standing one small step BEHIND Nora. His left hand grips the wooden stair railing behind him (ready to flee). His right hand holds a small black flashlight, switched OFF, dangling at his side. His shoulders are slightly raised (tense).

SCHATTEN (center, between the children):
- SITTING on the floor between Nora and Theo, facing the viewer directly.
- Medium-sized dog (about knee-height when sitting). Thin but healthy — wiry build, visible ribs just barely suggested through the fur.
- Dense, dark BLACK fur — seems to absorb light. Fur along the back of the neck is SLIGHTLY raised (not full bristle, just alert).
- Pointed upright ears, both facing forward.
- AMBER EYES: the brightest element in the entire image. Rendered as strong WHITE highlights with dark pupils, surrounded by dark fur. The eyes appear to glow.
- Mouth closed, nose slightly wet (small highlight). No tongue visible.
- Tail wrapped around his left side, resting on the floor.
- No collar. No leash. No tags. No bandana.

THE STAIRWELL (background):
- Old wooden staircase directly behind the three figures, going UP and to the right, disappearing into DARKNESS after about 8 visible steps.
- Peeling wallpaper on the walls — faded floral pattern, one large strip of wallpaper hanging loose.
- ONE small window on the landing above — dusty glass, pale diffuse light filtering through, creating the only illumination in the scene.
- Wooden banister/railing — dark wood, slightly worn smooth by hands.
- The floor is dark wood parquet, dusty.

NOTHING ELSE:
- No other people. No other animals. No posters or pictures on walls. No mailboxes. No door visible (only the staircase). No shoes or objects on the floor. No light switches visible. No electrical outlets.

DO NOT include: Smiling faces. Bright lighting. Modern devices (phones, tablets, earbuds). Colorful clothing (everything is dark/neutral). Additional accessories (hats, scarves, bags except as specified). Adults. Cartoon proportions. Cute/cuddly dog appearance — Schatten is lean, alert, and slightly unsettling in how intelligent his eyes look.
```

---

### Illustration 4: HILF am Fenster
**Platzierung:** Abschnitt P3 (nach Header, vor Text)

```
[Stil-Prefix einfuegen]

SCENE: The interior of a kitchen. In the center of the image: a kitchen window completely fogged with condensation. Written in the condensation by an invisible finger: the German word "HILF" (HELP). One girl's hand reaches toward the word. At the far right edge: a dog at the bottom of a staircase.

VIEWPOINT: Standing in the kitchen, facing the window straight-on. Eye level with the window (adult height).

THE WINDOW (center of image, dominant element):
- Standard German double-pane kitchen window, white plastic frame. EXACTLY one window pane, rectangular, landscape orientation.
- The ENTIRE glass surface is covered in condensation — fine water droplets, opaque, like breath on cold glass in winter. But this is JULY.
- Through the fogged glass: only a vague, blurry impression of bright green and sunlight outside. Trees suggested as blurry green shapes. The contrast between summer outside and frost inside is the key horror element.
- Written in the condensation, CENTER of the glass: "HILF" — four letters in childlike handwriting, crooked, slightly shaky, as if written by a scared 12-year-old girl's finger. The letters are roughly 8cm tall. The glass is CLEAR where the letters are — the finger wiped away the condensation.
- BELOW the word "HILF": a small arrow pointing UPWARD. Same childlike finger-writing. The arrow points toward the ceiling/upper floors.
- Water droplets are running DOWN from the bottom of each letter, like the word is crying. Streaks of water on the fogged glass below the letters.
- No other words. No other marks. No handprints. No face prints.

FOREGROUND (below the window):
- A kitchen counter/windowsill with EXACTLY three items: one plain white ceramic mug (empty, no text on it), one striped dish towel (folded), one ceramic fruit bowl containing exactly 3 apples. Nothing else on the counter.
- NORA'S HAND reaches into the frame from the lower-left. ONLY her right hand and forearm are visible — the rest of her body is out of frame. Her hand is 12-year-old girl's hand — small, clean, short nails. Her fingers are spread, reaching toward the word "HILF" on the glass. She has NOT touched it yet — her fingertips are 5cm from the glass. She hesitates.
- Her BREATH is visible — one small white cloud in front of her fingers. It is unnaturally cold in this kitchen despite summer.

FAR RIGHT EDGE OF IMAGE:
- Schatten (the dog) stands at the bottom of a wooden staircase that is visible at the right edge of the frame, partially cropped. Only his full body and the first 3 stairs are visible.
- He faces AWAY from the viewer, looking UPWARD toward the upper floors. His body is tense — all four legs planted, spine rigid, fur along the back raised in a ridge.
- His amber eyes are not visible from this angle (he faces away). His pointed ears are forward, alert.
- The staircase goes up into darkness.

LIGHTING:
- Main light: natural summer daylight from a second window (off-frame to the left) — warm light on the counter and floor.
- The fogged window itself: dim, the condensation blocks the light. The area immediately around the window is DARKER — the cold swallows the light.
- The water droplets on the glass catch tiny pinpoints of light.

NOTHING ELSE IN THE KITCHEN:
- No other appliances visible (no toaster, no coffee machine, no microwave). No refrigerator in frame. No stove in frame. No cabinets (cropped above frame). No clock. No calendar. No photos on the wall. No plants. No other dishes.

DO NOT include: A visible ghost or figure outside the window. A face in the condensation. Handprints on the glass. Blood. Broken or cracked glass. Dark/stormy weather outside (it MUST be bright summer). Other words besides "HILF" and the arrow. Other people. More than one mug, one towel, one fruit bowl on the counter. A full view of Nora (only her hand/forearm). Horror-movie lighting (green, red, dramatic). Candles. The dog facing the viewer (he faces the stairs). Any animals besides the one dog.
```

---

### Illustration 5: Der kalte Raum
**Platzierung:** Abschnitt A04 (nach Header, vor Text)

```
[Stil-Prefix einfuegen]

SCENE: A girl (Nora, 12) stands in the doorway of a small empty room. The door is open. On the inside of the door: deep scratches from fingernails. Behind her in the hallway: a dog refuses to enter.

VIEWPOINT: From inside the hallway, looking THROUGH the doorway into the room. Nora stands in the doorframe, backlit slightly by the dim hallway light. The dark room is beyond her.

THE ROOM (beyond Nora, visible through the open door):
- Small room, roughly 3x3 meters. Completely EMPTY — no furniture, no objects, no carpet.
- Bare plaster walls with 3-4 hairline cracks. Pale grey plaster, no wallpaper.
- Bare wooden floorboards, dusty. A thin layer of undisturbed dust covers the entire floor. No footprints in the dust.
- ONE window on the far wall — standard German window. The glass is covered in FROST PATTERNS — crystalline ice formations on the inside of the glass. This is July. The frost is impossible.
- Dense crosshatching fills the room's air — the air itself is VISIBLE, cold, heavy. Denser than the hallway air. The crosshatching is tighter inside the room than outside.
- 4-5 dust particles suspended in midair inside the room — FROZEN, not floating. They hang motionless.
- No light source inside the room. The only light comes from the hallway behind Nora and the faint grey light through the frosted window.

THE DOOR (the horror element — must be clearly visible):
- Old dark wooden door, swung OPEN toward the viewer (into the hallway), roughly 90 degrees.
- On the INSIDE surface of the door (the side that faces into the room, now visible because the door is open toward us): SCRATCH MARKS.
- EXACTLY five parallel vertical scratches, repeated 4 times in groups — like a hand with five fingers clawed down the door from top to bottom. The scratches are 40-50cm long each, roughly 1cm deep.
- The wood is gouged — splinters visible, the scratches are dark with age. These are DECADES old.
- The scratches run from roughly 120cm height down to 60cm height — the height of a 12-year-old girl reaching up and dragging her nails down.
- This is the most important visual detail — it must draw the eye immediately.

NORA (in the doorway):
- Standing in the doorframe, facing INTO the room (her back is slightly toward the viewer, about 3/4 turn).
- Her RIGHT hand grips the metal door handle — she is pulling her hand BACK slightly, as if the cold metal burned her.
- Her LEFT hand hangs at her side, fingers curled into a half-fist.
- Her head is turned to the RIGHT — she is looking at the SCRATCHES on the open door. Her eyes are wide. Her mouth is slightly open.
- Her breath is a thick WHITE CLOUD in front of her face.
- CLOTHING: dark hoodie (hood down), dark jeans, dark sneakers. Same as Illustration 3.
- HAIR: shoulder-length brown hair, tucked behind left ear. Same as Illustration 3.
- Her body weight shifts BACKWARD — one foot forward in the room, the other braced behind her in the hallway. She wants to step back.

SCHATTEN (in the hallway, behind Nora):
- Two steps behind Nora, still in the hallway. He will NOT cross the threshold.
- His front paws are planted firmly — braced, refusing to move forward.
- Neck fur fully raised — a visible ridge of bristling fur along the spine from head to shoulders.
- Lips slightly pulled back, top teeth just barely visible — he is growling.
- Amber eyes LOCKED on the interior of the room (not on Nora).
- His body leans slightly AWAY from the door while his head pushes forward — torn between guarding and retreating.

NOTHING ELSE:
- No furniture in the room. No objects in the room. No curtains on the window. No light fixtures. No radiator. No wallpaper. No pictures on walls.
- No ghost visible. No shadow figure. No face. No blood. No cobwebs. No spiders.
- No other people. No other animals.

DO NOT include: A visible ghost or apparition. Blood on the scratches or walls. Cobwebs or spiders. Broken furniture or debris. Any warm or cozy elements. Candlelight. Other rooms visible. Modern fixtures (light switches, outlets — keep walls bare). Mold or water damage. A mirror. Curtains.
```

---

### Illustration 6: Sie ist hier (Kellerpraesenz)
**Platzierung:** Abschnitt A11 (nach Header, vor Text)

```
[Stil-Prefix einfuegen]

SCENE: A girl (Nora, 12) stands ALONE in a dark stone cellar, holding a flashlight. On the dusty floor: child-sized bare footprints walking in a perfect circle. No ghost is visible. The dog is NOT in this scene.

VIEWPOINT: From the side, slightly above — as if looking down into the cellar from a slightly elevated position. Nora is on the LEFT side of the image, the circle of footprints dominates the RIGHT and CENTER.

THE CELLAR:
- Old stone walls — rough-cut grey stone blocks, mortar visible between them. Low ceiling roughly 180cm — Nora nearly touches it.
- The floor is rough concrete or stone, covered in a thick layer of grey-brown dust. Undisturbed dust everywhere EXCEPT the footprint circle.
- ONE bare lightbulb hangs from the ceiling on a wire — it is OFF/broken. Dark glass.
- Along the LEFT wall: one set of old wooden shelves with exactly 4 dusty glass jars (empty or dark contents, unlabeled) and 2 wooden crates stacked.
- ONE small puddle of water on the floor in the back-right corner — a single water drop caught mid-fall from the ceiling, reflecting the flashlight beam.
- No windows. No natural light. No other exits visible. One set of stone stairs at the far back leading UP (where Nora came from), disappearing into darkness.

THE FOOTPRINTS (center-right of image, the MAIN HORROR ELEMENT):
- In the dust: bare footprints. CHILD-SIZED — roughly 20cm long, 12-year-old girl's feet. No shoes.
- The footprints form a perfect CIRCLE roughly 2 meters in diameter.
- The prints overlap dozens of times — someone walked this exact circle over and over and over. Hundreds of laps. The dust is compressed in a circular path roughly 15cm wide.
- INSIDE the circle: the dust is slightly MORE disturbed than outside — as if the air is denser there, as if something just walked through.
- OUTSIDE the circle: undisturbed thick dust.
- The footprints are clearly illuminated by Nora's flashlight beam.

NORA (left side of image):
- Standing at the EDGE of the circle — her toes nearly touch the circular path but she has NOT stepped into it.
- Her RIGHT hand holds a black flashlight (cylindrical, roughly 20cm long). The beam points at the footprints. The beam TREMBLES — render this with slight motion blur or double-edge on the light cone.
- Her LEFT hand is pressed flat against her own chest, fingers spread — holding herself together.
- Her face: tears on both cheeks — rendered as 2-3 small bright highlights per cheek. Her eyes are wide but her expression is SAD, not screaming. Her lips are slightly parted — she is about to speak.
- Her breath: one thick WHITE CLOUD in front of her face. The cellar is unnaturally cold.
- CLOTHING: dark hoodie (hood down), dark jeans, dark sneakers. Same as previous illustrations.
- She is ALONE. No dog. No brother. No other person.

LIGHTING:
- The flashlight is the ONLY light source. It creates a cone of light from Nora's hand toward the footprints.
- Inside the cone: visible dust particles — but they are FROZEN, suspended, not drifting.
- Outside the cone: PITCH BLACK. The edges of the cellar dissolve into complete darkness. Heavy crosshatching fading to solid black.
- The flashlight beam dims slightly where it crosses the CENTER of the footprint circle — as if the air is denser there, swallowing light.

NOTHING ELSE:
- No visible ghost. No figure. No shadow-person. No glowing eyes. No face. No hands.
- No dog (Schatten stayed upstairs). No other animals. No rats. No spiders. No insects.
- No blood. No bones. No body. No clothing items on the floor.
- No furniture besides the one shelf unit. No tools. No boxes beyond the 2 crates specified.

DO NOT include: A visible ghost or spirit in any form. A shadow figure or silhouette of a person. Glowing or floating objects. Blood or body parts. Rats, mice, spiders, insects, or any animals. The dog (he is NOT in this scene). Other people. Candles. Additional light sources. Chains or shackles. A mirror. Writing on the walls. Modern fixtures.
```

---

### Illustration 7: Die Karte (Artefakt-Close-up)
**Platzierung:** Abschnitt A29 (nach Header, vor Text)

```
[Stil-Prefix einfuegen]

SCENE: Close-up of a hand-drawn map lying flat on a wooden desk, lit by a desk lamp. A child's hand touches the map. Around the map: exactly 3 objects. This is an OBJECT SHOT — no full persons visible.

VIEWPOINT: Top-down, slightly angled (roughly 30 degrees from directly above), looking down at the desk surface. The map fills roughly 60% of the image.

THE MAP (center of image):
- A hand-drawn city map on YELLOWED PAPER — thin, old, edges torn on 2 sides (left and bottom). One corner (top-right) is folded over.
- The paper is roughly A4 size, landscape orientation on the desk.
- The map shows a simplified street plan: thin black pen lines for streets, small rectangular blocks for buildings, a small church icon with steeple, a small fountain icon.
- HANDWRITING on the map: small, precise, slightly shaky old-woman's handwriting. Street labels: "Kirchgasse", "Marktplatz", "Friedhofstr." — 3 readable labels, the rest too small.
- EXACTLY 12 CIRCLES on the map — drawn with THICKER ink than the map lines (clearly darker/heavier). COUNT THEM: there must be twelve, no more and no fewer. Breakdown:
  - 11 circles are OPEN (just circles, no fill).
  - PLUS 1 circle (at "Kirchgasse 14") that is CROSSED OUT with two diagonal lines. Next to it in FRESH handwriting (slightly different shade of ink — cleaner, newer): "Lina. Kirchgasse 14."
  - 11 open + 1 crossed-out = 12 total. Verify the count.
  - The circles are scattered across different parts of the city.
  - Do NOT write any year numbers, dates, or numeric labels next to the circles. No "1892", no "1920", no numbers anywhere on the map except the house number in "Kirchgasse 14." and in "GRAVEN".
  - Next to 3 of the circles: tiny barely-legible notes (suggest illegible squiggly handwriting, NOT readable words and NOT numbers).
- ONE BLACK MARKING at the bottom-right of the map, separate from the 12 circles:
  - A heavy BLACK X drawn with much thicker, harder-pressed ink. The paper is slightly indented/torn where the pen pressed.
  - Next to the X in URGENT capital letters: "GRAVEN. Der Erste. NICHT ANFASSEN."
  - These letters are drawn with heavier ink — the darkest text on the entire map.

THE DESK (visible around the map):
- Dark brown wooden desk surface — old, scratched, well-used.
- EXACTLY 3 objects around the map (and NOTHING else):
  1. To the LEFT of the map: a sealed white envelope. Written on it in old handwriting: "Fuer die Naechste". The envelope is yellowed with age. No stamp.
  2. To the UPPER-RIGHT of the map: a brass candle holder with a STUB of red candle — mostly melted down, roughly 3cm of wax remaining. The candle is NOT lit. Dried wax drips on the brass holder.
  3. To the LOWER-RIGHT of the map: a small leather-bound book (diary) — dark brown leather, CLOSED, with a dark ribbon bookmark hanging out from between pages. Roughly 15x10cm. Old, worn.
- A desk lamp casts warm light from the UPPER-LEFT — the light falls diagonally across the map. The lamp itself is NOT visible (it is above/out of frame). Only the light cone is visible on the desk surface.

NORA'S HAND (one hand only):
- A 12-year-old girl's RIGHT hand enters the frame from the BOTTOM-LEFT corner.
- Only the hand and wrist are visible — no arm above the wrist, no body.
- Her thumb presses on the BLACK X marking (the Graven marking) — and is pulling AWAY, as if the spot is cold. The thumb is slightly lifted, mid-recoil.
- Her other 4 fingers rest spread on the map's edge.
- Small hand, clean, short nails, one tiny scratch on the index knuckle.

NOTHING ELSE:
- No other objects on the desk. No pens, no coffee cups, no phone, no papers besides the map and envelope.
- No full person visible — only the one hand.
- No dog visible in this image.

DO NOT include: Year numbers or dates anywhere on the map (no "1892", "1920", or any years — these are wrong and must not appear). More or fewer than 12 circles. Full persons. The dog. A lit candle or any flame/glow at the candle wick (the candle is a USED STUB, completely unlit). Additional objects on the desk. Modern items (phone, laptop, pen with logo). Color (the "red" circles should be rendered as thicker/darker ink circles distinguishable from the thinner map lines). A visible lamp (only its light). Other furniture visible. Writing besides what's specified. Creases or large stains on the map (only torn edges and the one folded corner).
```

---

### Illustration 8: Graven am Friedhof
**Platzierung:** Abschnitt A34 (nach Header, vor Text)

```
[Stil-Prefix einfuegen]

SCENE: A cemetery at sunset. EXACTLY 2 children and 1 dog in the foreground (seen from behind). Behind the largest gravestone: a tall grey FIGURE with hollow black eyes. EXACTLY these 4 beings — nothing else alive or moving.

VIEWPOINT: From behind the children, over their shoulders, looking toward the large gravestone and the figure behind it. The children are in the lower third, the gravestone and figure in the center-upper area.

THE CEMETERY:
- Old German city cemetery. Iron wrought-iron fence visible at the LEFT edge of the image — black, pointed finials on top.
- EXACTLY 8 gravestones visible in rows — old, grey stone, some leaning, some with moss. Simple rectangular stones, no angels, no crosses on the small stones. Different sizes.
- EXACTLY 4 old trees — 2 on the left, 2 on the right — gnarled oaks with heavy branches creating a partial canopy above. Leaves are still (no wind).
- Sunset light from the LEFT — golden-orange, casting long shadows to the right. Light rays visible between tree trunks.
- BUT: around the central gravestone, the light STOPS. A circle of shadow roughly 3 meters in diameter around the central stone. The crosshatching is significantly denser here — impenetrable shadow.
- DEAD GRASS in a perfect circle around the central gravestone — yellowed, flattened, dead. The boundary between living grass and dead grass is sharp and unnatural.

THE CENTRAL GRAVESTONE:
- The LARGEST stone in the cemetery — roughly 2 meters tall, 1 meter wide. Smooth polished grey granite. Rectangular slab, no ornamentation, no cross, no angel. Just flat stone.
- Engraved text (partially visible): "ALWIN GRAVEN" on the first line, "1789 — 1847" on the second line. Clean, chiseled letters.
- No flowers at the base. No candles. No offerings. No one visits this grave.

THE FIGURE — GRAVEN (behind the gravestone, the MAIN HORROR ELEMENT):
- Stands behind and slightly to the RIGHT of the gravestone — not hiding, positioned deliberately.
- TALLER than a human — roughly 220-230cm. Thin but broad-shouldered.
- His body is GREY — the same grey as ash or old concrete. Not transparent, not solid — somewhere in between. His outlines are slightly blurred, as if he vibrates.
- He wears a long coat reaching to his ankles. The coat moves to the RIGHT — but the leaves on the trees are STILL. There is NO wind. Only his coat moves.
- His FACE: not decomposed, not skeletal. A human face but WRONG — hollow cheeks, sharp cheekbones, a thin line for a mouth. No expression. No emotion. Just presence.
- His EYES: two BLACK HOLES. Not dark eyes — HOLES. No whites, no iris, no pupil. Two voids. Bottomless. They are the DARKEST points in the entire image — pure black circles in his grey face.
- His hands hang at his sides — long fingers, grey, still.
- He does not lean or reach or grasp. He simply STANDS.

NORA AND THEO (foreground, backs to viewer):
- Nora (LEFT, taller, 12): standing still, feet planted. Her fists are clenched at her sides. Her head is tilted UP to look at Graven. Dark hoodie, dark jeans, shoulder-length brown hair — seen from behind.
- Theo (RIGHT, shorter, 10): half a step BEHIND Nora. His RIGHT hand grips the back of Nora's hoodie at the waist level. His left hand hangs at his side. Messy dark hair. Astronaut pajama top visible (seen from behind — pattern on the back). He is looking up at Graven.
- Both children are SMALL compared to the gravestone and the figure. The size difference is dramatic — emphasize this.

SCHATTEN (between the children and the gravestone):
- Standing roughly 1 meter in front of the children, 2 meters from the gravestone. He is between the children and Graven — a living shield.
- EVERY hair on his body is raised — his fur stands straight up like a brush, especially along the spine and neck.
- His teeth are BARED — lips pulled back, both rows of teeth visible. Wrinkled muzzle.
- His amber eyes face Graven's black voids — the brightest points (Schatten's eyes) facing the darkest points (Graven's eyes).
- All four legs braced, body low, leaning FORWARD — aggressive defensive posture.
- His tail is straight out behind him, bristled.

NOTHING ELSE:
- No other people. No other animals. No birds. No bats. No fog.
- No other figures in the cemetery — living or dead.
- No moon (it's SUNSET, not night). No stars.
- No chapel or cemetery building visible.

DO NOT include: Blood. Decomposition. Visible bones or skeleton. Zombie features. Bats. An owl. Fog or mist (the air is CLEAR). A full moon (it's sunset). Other ghost figures. A scythe or weapons. Chains. Gravestones with skulls. Cemetery chapel. A path or road. Other people walking.
```

---

### Illustration 9: Rote Tinte (Bibliotheksrecherche)
**Platzierung:** Abschnitt B04 (nach Header, vor Text)

```
[Stil-Prefix einfuegen]

SCENE: A girl (Nora, 12) sits alone at a wooden reading table in an old library, hunched over an open book. In the book's margins: handwritten notes in different ink. Through a window in the background: the dog waits outside on the steps. No other people in the library.

VIEWPOINT: From across the table, at seated eye level, looking at Nora who sits on the far side. The open book is between the viewer and Nora.

THE LIBRARY:
- Old German public library interior. EXACTLY 2 tall wooden bookshelves visible behind Nora — floor to ceiling (roughly 3 meters), dark wood, packed tightly with old hardcover books. No gaps, no empty shelves.
- The reading table: heavy dark wood, rectangular, about 2 meters long. Nora sits at the far side.
- ONE green-shaded banker's lamp on the table (brass base, green glass shade) — switched ON, casting warm light downward onto the table surface.
- ONE tall arched window to the RIGHT of the bookshelves — late afternoon dusty light filtering through. The window has no curtains.
- The rest of the library fades into shadow — the bookshelves recede into darkness.
- Hardwood floor, polished dark wood.
- No computers. No screens. No modern technology. No photocopier.

NORA (seated at the far side of the table):
- Hunched forward over the large open book, her face close to the page.
- Her RIGHT hand holds the page flat, fingers spread. Her LEFT hand is frozen mid-air near a pencil on the table — she was about to pick it up but stopped.
- EXPRESSION: intense focus. Eyes narrowed, studying the marginal notes. Mouth slightly open. Not scared — analytical. She is a detective.
- CLOTHING: dark hoodie, hair tucked behind left ear. Same as all previous illustrations.

THE OPEN BOOK (center of image, key detail):
- Large format book, roughly A3 when open. Thick, old. Yellowed pages. Old serif typography.
- The MARGIN of the right page has HANDWRITTEN NOTES: small, careful handwriting. The notes are in a different ink weight than the printed text — darker, thinner lines (representing red ink in the original, rendered as distinct from the printed text through different line weight).
- ONE note is partially legible: "Schleier. 1823." (rendered as careful small handwriting).
- At the bottom of the page: the initials "E.S." underlined once.
- EXACTLY 2 paper bookmarks stick out from other places in the book — white paper strips.

OTHER ITEMS ON THE TABLE (EXACTLY these, nothing more):
- To the LEFT of the book: a small spiral-bound notebook (Nora's) — open, with fresh handwriting on it (her notes). One pencil lying next to it.
- To the RIGHT of the book: EXACTLY 2 more closed library books, stacked. Different sizes. No other objects.
- NO coffee cup. NO water bottle. NO phone. NO bag.

THROUGH THE WINDOW (right background, subtle):
- Through the library window: Schatten sits on the stone steps OUTSIDE the building.
- He is small in the frame — a dark silhouette seen through the window glass.
- He sits upright, facing the library door (which is off-frame). Ears forward. Alert posture.
- The evening light casts his shadow long across the steps.

NOTHING ELSE:
- No other people — no librarian, no other readers. Nora is completely alone.
- No modern devices. No clock on the wall. No posters.
- No plants. No decorative objects.
- No microfilm machine (removed from this prompt for simplicity).
- No library card visible.

DO NOT include: Other people (she is alone). Modern equipment (computers, printers, screens). Bright cheerful lighting. Visible ghosts. Horror elements (this is detective work, not horror). A coffee cup or food. A phone or tablet. Library signage. More than 2 additional books on the table. A backpack or bag.
```

---

### Illustration 10: Der Schluessel
**Platzierung:** Abschnitt B16 (nach Header, vor Text)

```
[Stil-Prefix einfuegen]

SCENE: CLOSE-UP of two pairs of hands and a key between them. An old woman's hands extend a brass key on a red ribbon toward a child's reaching hands. Between the hands: the dog's face looking up. No full bodies visible — this is an intimate hands-only composition.

VIEWPOINT: Horizontal, roughly table-height, looking at the space between the two people. The image is dominated by the four hands and the key.

FRAU HELD'S HANDS (upper portion of image, coming from the top):
- Old woman's hands — wrinkled skin, visible veins, 2-3 liver spots on the back of the right hand. The fingers are STRONG, not trembling (she has made her decision).
- She wears a plain knitted cardigan — only the cuffs and forearms are visible. Simple knit pattern, no color details, no buttons visible.
- Her RIGHT hand holds the key between thumb and forefinger, extending it DOWNWARD toward Nora. The key dangles from a ribbon.
- Her LEFT hand rests on the edge of a dark wooden drawer (a chest of drawers, partially open — the drawer she took the key from).
- ONLY her hands and forearms up to the elbows are visible. No face, no body.

THE KEY (CENTER of image, the FOCAL POINT):
- Old brass key, roughly 8cm long. Tarnished — dark patina, not shiny. Simple rounded bow (top), straight shaft, simple ward (teeth) at the bottom.
- Attached to a RIBBON: faded, frayed at both ends, roughly 15cm long. The ribbon hangs in a slight curve from Held's fingers.
- The key hangs in the AIR between the two pairs of hands — in the exact center of the image.
- ONE bright highlight on the key's shaft where light catches it.
- No other keys. No keyring. No tag.

NORA'S HANDS (lower portion of image, coming from the bottom):
- A 12-year-old girl's hands reaching UPWARD toward the key. Palms up, fingers slightly curled, reaching but NOT YET TOUCHING the key. There is a gap of roughly 5cm between her fingertips and the key.
- Small hands compared to Held's — the size difference is visible and important.
- Clean, practical hands. Short nails. One tiny scratch on the right index knuckle.
- ONLY her hands and wrists are visible. No face, no body, no sleeve (bare wrists).

SCHATTEN'S FACE (between the two pairs of hands, background):
- The dog's face is visible in the space between the four hands — slightly behind and between them, looking UPWARD at the key.
- His amber eyes reflect the key's metallic highlight — two bright points looking up.
- His head is tilted slightly to the LEFT. His expression is calm, patient. Mouth closed.
- ONLY his head and the top of his neck are visible. His body is below frame/behind something.
- His fur is smooth (not bristling) — he is at ease.

BACKGROUND (minimal, blurred/suggested):
- Behind the hands: a dim, warm interior. Suggested by a few crosshatch lines:
  - The dark wooden chest of drawers (where the key was stored), partially open top drawer.
  - A small framed photograph on top of the dresser — too small and distant to see the face, just the rectangular frame shape.
  - Warm dim lamplight from the right side (source off-frame).
- The background is deliberately UNFOCUSED — looser crosshatching, less detail. All focus is on the hands and key.

NOTHING ELSE:
- No full bodies. No faces of Held or Nora. No other furniture clearly visible.
- No other objects in the hands. No wallet, no letter, no book.
- No other people. No other animals.

DO NOT include: Full body shots of either person. Their faces. Other objects in their hands. Modern objects (phone, watch). A bright or clinical lighting. Other keys or a keyring. A lit candle. Jewelry on either person's hands (no rings, no bracelets). A collar on the dog. Decorative elements on the key.
```

---

### Illustration 11: Helds Warnung
**Platzierung:** Abschnitt B21 (nach Header, vor Text)

```
[Stil-Prefix einfuegen]

SCENE: Interior of an old apartment. An old woman sits in an armchair holding a teacup, telling a story. EXACTLY 2 children and 1 dog also in the room. Through the window behind the old woman: city rooftops at night, and one faint light at the distant cemetery edge.

VIEWPOINT: From the children's position, facing the old woman. Held is in the center-background, the window behind her. The children are in the foreground edges.

THE APARTMENT INTERIOR:
- An old-fashioned German apartment living room. Warm, cozy, cluttered with books.
- ONE floor lamp to the RIGHT of Held's chair — tall, brass, with a fabric shade. Switched ON — it casts warm golden light on Held's face from the right side, leaving her LEFT side in shadow.
- Behind Held: EXACTLY 1 tall bookshelf (floor to ceiling, dark wood, full of books) to the left, and the WINDOW to the right.
- The floor: a worn oriental-style carpet, faded pattern. Dark wood floor visible at the edges.
- Against the back wall (beside the bookshelf): a small desk with papers on it and the MAP (visible as a flat yellowed paper with small dark markings — the ghost-tracking map from Illustration 7).
- EXACTLY 3 small framed photographs on a shelf between the bookshelf and window — too small to see faces, just rectangular frames.
- No TV. No radio. No modern electronics. No clock on the wall.

FRAU HELD (center of image):
- Sits in an old wingback armchair — dark upholstery, high back, slightly too large for her. She is small in the big chair.
- Old woman, roughly 75 years. White hair pulled back in a simple bun. Small build, thin. Wears a plain knitted cardigan over a dark blouse.
- Holds a plain white teacup in BOTH hands (no saucer) — hands wrapped around the cup for warmth.
- Her face: half lit by the floor lamp (right side golden), half in shadow (left side dark). Her EXPRESSION: her eyes are DISTANT — she looks past the children, past the room, into the past. Her mouth is drawn tight, slightly downturned. She is remembering something terrible.
- She is mid-sentence — her mouth is slightly open, speaking.

THROUGH THE WINDOW (behind Held, to the right):
- The window shows Gravenstedt at NIGHT — dark sky, darker rooftops silhouetted, 1 church spire visible, a few small dots of streetlights.
- Far in the DISTANCE, near the bottom of the visible skyline: a FAINT cold point of light near what could be the cemetery. It could be a streetlight. Or something else. It is the ONLY cold element in an otherwise warm image.
- The window has simple white curtains, partially open.

NORA (foreground LEFT, partial view):
- Sits on the edge of a simple wooden chair. ONLY her right side is visible — she is at the left edge of the frame, partly cropped.
- Leaning forward, turned toward Held, listening intently.
- Her right hand grips the edge of the wooden chair seat.
- Her head is turned slightly toward the window — she sees the distant light too.
- EXPRESSION: serious, alert, absorbing every word. No smile.

THEO (foreground RIGHT, partial view):
- Sits cross-legged on the carpet near Schatten. ONLY his left side is visible — he is at the right edge of the frame, partly cropped.
- His LEFT hand rests on Schatten's back.
- His expression: uncomfortable. He has heard enough.

SCHATTEN (on the carpet, center-right foreground):
- Lies on the carpet between Nora's chair and Theo.
- He has LIFTED his head and turned it toward the window. His ears are pointed forward.
- His amber eyes are focused on the distant faint light at the cemetery. He is alert.
- His body is relaxed (lying down), but his head and ears are TENSE — he senses something the humans are only beginning to understand.
- His mouth is closed but his lips twitch slightly — the beginning of a growl.

NOTHING ELSE:
- No other people. No other animals.
- No food or drink besides Held's one teacup. No tea set. No cookies.
- No candles burning. No fireplace.

DO NOT include: A visible ghost. Supernatural elements inside the room (only the distant light through the window). Modern furniture or electronics. A TV. A fireplace. Food or snacks. More than one teacup. Additional people. Pets besides the one dog. Decorative items not specified (no plants, no vases, no ornaments). Bright or cheerful lighting — the room is warm but the mood is heavy.
```

---

### Illustration 12: Theo rebelliert
**Platzierung:** Abschnitt C03 (nach Header, vor Text)

```
[Stil-Prefix einfuegen]

SCENE: A dark apartment hallway at night. EXACTLY 1 boy (10), 1 girl (12), and 1 dog. The boy stands at the bottom of a staircase with a flashlight. The girl stands in her bedroom doorway behind him. The dog stands between them.

VIEWPOINT: From the side of the hallway, looking lengthwise. Theo and the stairs are to the LEFT. Nora's doorway is to the RIGHT. Schatten is in the CENTER.

THE HALLWAY:
- Old German apartment hallway. Dark wood parquet floor (Fischgraet-pattern). High ceiling roughly 3 meters.
- NO lights on — the hallway is dark. The ONLY light sources are: moonlight through one small hallway window (upper right area of image), and Theo's flashlight.
- The small hallway window: rectangular, roughly 40x60cm, high on the wall. Pale blue-white moonlight filters through — casting a faint rectangle of light on the opposite wall.
- Wallpaper on walls: old, faded floral pattern. No peeling (unlike the stairwell — this is a lived-in apartment, maintained by Mama).
- EXACTLY these items visible in the hallway: 1 coat rack (wooden, with 2 jackets hanging and 1 scarf), 2 pairs of shoes on the floor below the coat rack. Nothing else.
- EXACTLY 2 doors visible: Nora's bedroom door (open, right side) and Mama's bedroom door (CLOSED, further down the hall on the right, barely visible in darkness).

THE STAIRCASE (left side of image):
- Old wooden stairs going UP to the right, disappearing into COMPLETE darkness after roughly 6 visible steps.
- The stairs lead to the 3rd floor (Silber's apartment, unseen).
- Wooden banister on the left side of the stairs.
- At the VERY TOP of the visible stairs: the vague suggestion of a door in the darkness — is it ajar? Hard to tell. Just a slightly different shade of black.
- One step CREAKS under Theo's weight — convey this by showing the step slightly bowed/depressed under his foot.

THEO (left side, at the stairs):
- Stands with his RIGHT foot on the FIRST step and his LEFT foot on the hallway floor. Mid-step — he is going UP.
- CLOTHING: Astronaut pajamas — FULL SET (top and bottom matching). The pajama pattern: small rockets, stars, and Saturn-like planets scattered across the fabric. The pattern must be clearly visible.
- Bare feet — no socks, no slippers. His toes grip the wooden step.
- His RIGHT hand holds a flashlight (small, black, cylindrical), pointed UPWARD along the staircase, the beam illuminating the first 4-5 steps above him before fading into darkness.
- His LEFT hand grips the banister.
- His FACE: jaw set, determined, eyes narrowed. He is SCARED (his shoulders are pulled up high around his ears) but he is GOING. This is not his usual joking face — this is stubborn courage.
- His messy dark hair sticks up in all directions (bedhead).

NORA (right side, in doorway):
- Stands in her bedroom doorway, roughly 3 meters behind Theo.
- The door is open. Her bedroom behind her is DARK — no light on.
- Her RIGHT hand grips the doorframe. Her LEFT hand hangs at her side.
- She wears an oversized plain sleep t-shirt (reaching mid-thigh) over what might be pajama shorts (barely visible). Her feet are bare. Her hair is messy from sleep.
- Her EXPRESSION: surprise (eyebrows raised, mouth slightly open) mixed with reluctant recognition that Theo is RIGHT. She is not stopping him. She is deciding whether to follow.

SCHATTEN (center of hallway, between them):
- Standing in the middle of the hallway, exactly between Nora and Theo.
- His head is turned LEFT toward Theo. But his body faces RIGHT toward Nora. He is MID-TURN — deciding who to follow.
- His tail hangs low, swinging slightly to the left. Not tucked (not frightened) — just undecided.
- His amber eyes catch the edge of Theo's flashlight beam — 2 bright points in the dark hall.
- His fur is flat (not bristling) — he is alert but not alarmed.
- All four legs planted, weight even — he waits.

NOTHING ELSE:
- No other people. Mama is ASLEEP behind her closed door — she is NOT visible.
- No other animals.
- No visible ghost on the stairs. No figure. No shadow.
- No light under Mama's closed door. She sleeps.

DO NOT include: A visible ghost or figure on the stairs. Light under Mama's door. Other family members awake or visible. Bright lighting. Overhead hallway light on. A phone or device. Dramatic horror lighting (colored, extreme contrast). A window on the staircase. More than the 2 doors, 1 window, 1 coat rack, and shoes specified. Toys or children's items in the hallway.
```

---

### Illustration 13: Mama traeumt
**Platzierung:** Abschnitt C05 (nach Header, vor Text)

```
[Stil-Prefix einfuegen]

SCENE: A mother sits upright in bed, drenched in sweat, eyes wide with terror. EXACTLY 2 children stand in the bedroom doorway. The dog has jumped onto the bed and presses against the mother. The time is 3 AM.

VIEWPOINT: From inside the bedroom, facing the bed. The bed is center-left. The doorway with the children is center-right. The viewer stands roughly where a dresser would be.

THE BEDROOM:
- Simple German bedroom. A double bed (no headboard, just a mattress on a plain bed frame) center-left, white sheets and a white duvet. ONE nightstand to the left of the bed.
- The nightstand has EXACTLY 3 items: 1 digital alarm clock showing "3:00" (the only modern item), 1 bedside lamp (switched ON — harsh bright light illuminating the scene), 1 glass of water KNOCKED OVER — water dripping off the nightstand edge onto the dark wood floor below. A small puddle forming on the floor.
- The bed sheets are TANGLED — pulled to one side, twisted, half on the floor on the left. The duvet is bunched at the foot of the bed. She thrashed in her sleep.
- The PILLOW: on Mama's side, where her head was: a SUBTLE cold spot. Rendered as slight condensation/frost texture on the pillow surface — you almost miss it. A small patch roughly the size of a face. This is the only supernatural element in the room.
- No other furniture clearly visible. No dresser, no wardrobe (or they are in deep shadow). No pictures on the wall. No curtains (or they are in shadow). No rug. Dark wood floor.

MAMA (on the bed, center-left):
- Mid-30s woman. Short brown hair, practical cut, currently PLASTERED to her forehead and neck with sweat.
- She sits BOLT UPRIGHT — her torso is vertical, legs still under the tangled sheet. Her back does not touch any headboard or wall.
- Her HANDS grip the sheet at her lap — knuckles WHITE, fingers digging into the fabric.
- Her FACE: eyes WIDE open — staring straight ahead (not at the children yet, not at anything visible — she stares at where the presence WAS). Mouth slightly open, rapid breathing. Sweat visible as small bright highlights on her forehead (3-4 droplets), on her neck, at her hairline.
- She wears a plain dark sleep t-shirt, dark with sweat at the collar and chest area.
- Her EXPRESSION: raw, primal, unprocessed fear. Her rational world just shattered. She is an adult who just felt something impossible.

THE CHILDREN (in the doorway, center-right):
- The bedroom door is OPEN. The hallway behind them is DARK — pitch black.
- NORA (left, closer to the bed): stands in the doorway, her RIGHT hand on the doorframe. She faces Mama. Her expression: initially worried, but shifting to UNDERSTANDING — "She finally FELT it." A flicker of relief behind the concern. She wears the same sleep t-shirt from Illustration 12.
- THEO (right, behind Nora): peers over/past Nora's shoulder. His eyes are HUGE — wide, scared. But he is not scared of the ghost. He is scared because his MOTHER is scared. He has never seen Mama like this. His LEFT hand grips Nora's right sleeve. He wears the astronaut pajamas from Illustration 12.
- Both children are barefoot on the dark wood floor.

SCHATTEN (on the bed):
- He has JUMPED onto the bed — he lies on the RIGHT side of the bed, pressed against Mama's right arm/side.
- His body is warm — his presence is COMFORT against the cold that woke her.
- His fur is smooth (not bristling) — he is calm, grounding, protective.
- Mama's RIGHT hand has moved from the sheet to rest on Schatten's back — she pets him without realizing it, an automatic comfort gesture.
- His amber eyes are OPEN, calm, looking toward the doorway (toward the children). He knew this would happen.
- His chin rests on the bed sheet near Mama's thigh.

NOTHING ELSE:
- No ghost visible. No figure. No shadow. No hands. No face other than the 3 humans and the dog.
- No second pet. No toys. No books on the nightstand.
- No visible window (it's 3 AM, the room is interior-lit only by the bedside lamp).

DO NOT include: A visible ghost or shadow figure anywhere in the room. Hands or faces appearing in the dark. Blood. A partner/father in the bed (Mama sleeps alone). A child's toy or stuffed animal. Curtains blowing. An open window. Any light source besides the one bedside lamp. A mirror. A closet door ajar. Horror-movie effects (green lighting, dramatic angles). The pillow frost being TOO obvious — it should be subtle, almost unnoticeable.
```

---

### Illustration 14: Staffeluebergabe
**Platzierung:** Abschnitt C07e (nach Header, vor Text)

```
[Stil-Prefix einfuegen]

SCENE: CLOSE-UP of a kitchen table. A mother's hands hold her daughter's hands. On the table between them: an old diary and a key. The dog sits beside the table, looking up. ONLY hands, the table surface, and the dog visible — no full bodies, no faces. Morning sunlight.

VIEWPOINT: Horizontal, at table height, looking across the table surface. The image is dominated by the hands, diary, key, and the dog's face.

THE TABLE SURFACE (fills most of the image):
- Plain wooden kitchen table — light-colored wood (birch or pine), simple, with some scratches and wear marks. Natural wood grain visible.
- Morning sunlight enters from the RIGHT side of the image — warm, golden, casting soft shadows to the left.

MAMA'S HANDS (entering from the TOP of the image):
- A woman's hands, mid-30s — not old, not young. Clean, practical, no nail polish. A few fine lines. No rings. No jewelry.
- Her RIGHT hand holds BOTH of Nora's hands — wrapping around them from above. Her fingers are intertwined with Nora's smaller fingers. This is a warm, firm grip — not desperate, not fragile. Protective.
- Her LEFT hand has just placed the KEY on the table — her fingertips still touch the key, just releasing it. The placement was deliberate and ceremonial.
- ONLY her hands and wrists are visible. She wears a plain long-sleeved top — only the cuffs at the wrists are visible, pushed up slightly.

NORA'S HANDS (entering from the BOTTOM of the image):
- A 12-year-old girl's hands. Smaller than Mama's. Short nails. One tiny scratch on the right index knuckle (consistent with all illustrations).
- Both hands are held by Mama's right hand.
- Her LEFT hand fingers also touch the edge of the DIARY — she is accepting it.
- ONLY her hands and wrists are visible. Bare wrists, no sleeves visible.

THE DIARY (center-left of the table):
- An old leather-bound book, roughly 15x10cm, dark brown leather, well-worn.
- It is OPEN to a page near the middle. The visible page shows handwritten text in small old-woman's handwriting — not legible at this angle, just lines of ink on yellowed paper. At the bottom of the visible page: marks in a different ink weight (suggesting the "red" annotations of Silber).
- A dark ribbon bookmark hangs out from between pages.

THE KEY (center-right of the table, just released by Mama's left hand):
- A simple iron key, roughly 7cm long. Dark iron, not brass (this is the CELLAR key, different from the brass apartment key in Illustration 10).
- It lies flat on the table between the diary and a plain white coffee mug.
- The morning light catches it — one bright highlight on the shaft.
- No ribbon or tag on this key. Just the bare iron key.

EXACTLY 2 OTHER ITEMS ON THE TABLE:
1. ONE plain white coffee mug to the RIGHT of the key — half-full (dark liquid visible at the rim). No text or design on the mug.
2. ONE small plate with 2 toast crusts to the FAR LEFT — Theo ate and left. No other food.

SCHATTEN (beside the table, center-bottom of image):
- Sits on the floor next to the table, visible in the space between the table legs and chairs.
- His head is AT table height, looking UP at the hands and the key.
- His amber eyes are WARM — not alert, not bristling. Content. Approving.
- His tail wags in a SLOW, deliberate sweep — visible on the floor behind him. Not excited-wagging. Ceremonial.
- His mouth is closed. His ears are relaxed, tilted slightly forward.
- His fur is smooth — he is completely at ease.

NOTHING ELSE ON THE TABLE:
- No phone. No newspaper. No napkins. No sugar bowl. No second mug. No fruit. No jam. No butter.
- No full bodies visible of any human.
- No window visible (implied by the directional sunlight).

DO NOT include: Full body shots. Faces. Other people (Theo is gone). More than the 4 items on the table (diary, key, mug, plate with crusts). A phone or device. A sugar bowl or other kitchen items. Dark or cold lighting. Horror elements. A window view. Walls or kitchen cabinets (everything beyond the table is softly blurred or out of frame). Another animal. A second key. A lit candle.
```

---

### Illustration 15: Mamas Frage (Das beste Familienende)
**Platzierung:** Ende E23 (nach Header, vor Text)

```
[Stil-Prefix einfuegen]

SCENE: A kitchen on a bright Sunday morning. EXACTLY 1 woman, 2 children, and 1 dog. Pancakes on the table. Sunlight flooding through a large window. This is the WARMEST and BRIGHTEST illustration in the book — maximum contrast to all the dark illustrations before it.

VIEWPOINT: From a corner of the kitchen, at standing eye level, showing the whole kitchen scene — the table, the stove, the window, all 4 beings.

THE KITCHEN:
- Bright morning sunlight floods through ONE large kitchen window on the LEFT wall — white curtains pushed aside, clean clear glass (NO frost, NO condensation — this is important: the window that had "HILF" in Illustration 4 is now warm and clear).
- The kitchen is WARM — render this with MINIMAL crosshatching. More white space than any other illustration. Light, airy, open lines.
- Plain white walls. Light-colored cabinets above a counter (only partially visible). A simple gas stove to the LEFT, near the window.
- A small flower vase on the windowsill — ONE simple vase with 3 small flowers (daisies or similar). The only decorative element.
- On the floor near the stove: ONE dog food bowl — full. Metal bowl. This is significant: Schatten has his OWN bowl now. He is family.
- The kitchen floor: light-colored tiles. Clean.
- Down the hallway (visible through an open kitchen doorway in the background): Nora's bedroom door is OPEN with warm light visible inside. The room that was cold is now warm. (Subtle detail, small in the background.)

THE TABLE (center of image):
- Wooden kitchen table, same as Illustration 14.
- CENTER of table: ONE plate/platter with a STACK of 5 pancakes. Steaming — render 2-3 wavy lines above the stack for heat.
- ON the table, EXACTLY these items: the pancake plate, 1 small jar of jam (lid off), 3 plates (one per person), 3 forks, 1 glass of juice (in front of Nora), 1 coffee mug (in front of Mama's place — currently empty, she's at the stove). NO syrup bottle. NO butter dish.

MAMA (at the stove, LEFT side):
- Stands at the gas stove, holding a frying pan in her LEFT hand and a spatula in her RIGHT hand. She has just TURNED her body to face the table — her hips face the stove but her torso and head are turned toward the children.
- Her EXPRESSION: thoughtful, serious but not grim. She is about to ask an important question. Her eyes focus on Nora. Her mouth is slightly open — mid-thought, not yet speaking.
- Mid-30s, short brown hair (dry, clean — not sweaty like Illustration 13). Wears a casual light-colored long-sleeve top and an apron.
- The pan has ONE pancake in it — mid-cooking.

NORA (at the table, RIGHT-CENTER):
- Sits at the table with BOTH hands wrapped around a glass of juice (orange juice, rendered as medium-grey liquid in the glass).
- She looks AT Mama — calm, steady, waiting. Her expression: quiet confidence. She knows what Mama is going to ask. She is ready.
- She sits straight — not slouching. Shoulders back.
- CLOTHING: casual t-shirt (not the sleep shirt — she is dressed for the day). Hair tucked behind her ear as always.

THEO (at the table, FAR RIGHT):
- Sits across from Nora. His plate has pancake remnants — he is MID-CHEW, mouth full, cheeks puffed slightly.
- His RIGHT hand holds a fork with a piece of pancake on it, frozen mid-air. He looks between Mama and Nora — he KNOWS what is about to be said.
- His LEFT hand rests on the table near his plate.
- His messy hair. 2-3 small crumbs on his chin and lower lip.
- His expression: a small GRIN under the full mouth — even in serious moments, Theo is Theo.
- CLOTHING: a regular t-shirt (not the astronaut pajamas — it is morning, he changed).

SCHATTEN (under the table):
- Lies under the table, between the children's feet and chair legs. He is visible through the TABLE LEGS.
- His amber eyes are HALF-CLOSED — content, peaceful, sleepy-satisfied.
- His tail wags SLOWLY — the tip of his tail brushes against Nora's left ankle.
- His chin rests on his front paws, flat on the floor.
- 2-3 small pancake crumbs near his nose on the floor (Theo fed him).
- His fur is smooth, his body relaxed. He is HOME.

NOTHING ELSE:
- No additional people. No visitors.
- No supernatural elements. No frost. No condensation. No cold spots. No shadows.
- No modern devices on the table (no phone, no tablet). No newspaper.

DO NOT include: Dark shadows. Cold elements. Frost or condensation on ANY surface. Supernatural phenomena. The map or diary visible (they are not in this scene). A sad or worried mood. Dramatic lighting. Candles. An additional pet. The father/partner. A TV or radio visible. More than the specified items on the table. Any horror element whatsoever. This is PURE DOMESTIC WARMTH — the payoff after 14 illustrations of darkness.
```

---

## Zusammenfassungstabelle

| Nr. | Szene | Abschnitt | Pfad | Typ |
|-----|-------|-----------|------|-----|
| 1 | Stadtkarte Gravenstedt | Front Matter | Alle | Karte |
| 2 | Kirchgasse 14 + Schatten | P1 | Alle | Establishing Shot |
| 3 | Nora, Theo, Schatten | P2 | Alle | Charakterbild |
| 4 | HILF am Fenster | P3 | Alle | Uebernatuerlicher Moment |
| 5 | Der kalte Raum (Kratzer) | A04 | Pfad A | Horror |
| 6 | Sie ist hier (Keller, allein) | A11 | Pfad A | Psycho-Horror |
| 7 | Die Karte (12 rote Kreise) | A29 | Pfad A | Artefakt Close-up |
| 8 | Graven am Friedhof | A34 | Pfad A | Antagonist |
| 9 | Rote Tinte (Bibliothek) | B04 | Pfad B | Detektivarbeit |
| 10 | Der Schluessel (Uebergabe) | B16 | Pfad B | Generationenwechsel |
| 11 | Helds Warnung (blaues Licht) | B21 | Pfad B | Atmosphaere |
| 12 | Theo rebelliert (Astronautenpyjama) | C03 | Pfad C | Charakter-Moment |
| 13 | Mama traeumt (3 Uhr nachts) | C05 | Pfad C | Familie + Uebernatuerliches |
| 14 | Staffeluebergabe (Tagebuch + Schluessel) | C07e | Pfad C | Emotionaler Wendepunkt |
| 15 | Mamas Frage (Pfannkuchen) | E23 | Pfad C Ende | Familienaufloesung |

---

## Hinweise zur Nutzung

1. **Stil-Prefix**: Den VOLLSTAENDIGEN Stil-Prefix IMMER als ersten Absatz einfuegen — einschliesslich der MANDATORY RULES
2. **Reihenfolge**: Zuerst Illustration 3 (Charakterbild) generieren und als Referenz nutzen
3. **Konsistenz-Anweisung**: Nach dem ersten Bild bei JEDEM weiteren Prompt hinzufuegen: "Use the EXACT same art style, line weight, crosshatching density, and character designs as the previous illustrations. The characters must be recognizable across all images."
4. **Schatten-Konsistenz**: Der Hund MUSS in jedem Bild identisch aussehen — duenn, drahtig, dunkles Fell, Bernsteinaugen, spitze Ohren, kein Halsband. Wie ein duenner schwarzer Schaeferhund/Malinois-Mix.
5. **Format**: Hochformat (portrait), mindestens 2000x3000 Pixel, 300 DPI
6. **Keine Farbe**: Alle Bilder sind reines Schwarz-Weiss (Pen-and-Ink, Crosshatching). Keine Grautöne-Waschungen.
7. **Unterschied zum Herrenhaus**: Die Geisterspuerer-Illustrationen sind DUNKLER, ATMOSPHAERISCHER, mit mehr Schatten und Kontrast — passend zur aelteren Zielgruppe (10-12 statt 8-10)
8. **Bei Korrekturen**: Wenn ein Bild ungewollte Elemente enthaelt, den Prompt wiederholen mit dem Zusatz: "REMOVE [Element]. This element must NOT appear. Replace with empty space / the background continuing."
