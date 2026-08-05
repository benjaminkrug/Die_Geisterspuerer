# Illustrationen-Prompts — Die Geisterspürer Band 2 CYOA „Der Friedhof ohne Namen"

15 Schwarz-Weiß-Illustrationen (Pen-and-Ink, Crosshatching) für das interaktive Taschenbuch.
Stil identisch zu Band 1 — **eine bewusste Abweichung** (s. Stil-Vorgabe, Punkt Technik): Band 2 erlaubt
**ein Smartphone**, weil es kanonisch vorkommt (Temperaturmessung, das Archiv-Foto). Sonst keine moderne Technik.

---

## Stil-Vorgabe (für alle 15 Illustrationen identisch)

**Stil-Prefix (immer zuerst einfügen):**

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
- EXCEPTION FOR BAND 2: a simple smartphone is allowed ONLY where explicitly specified (held by a child). No other modern technology (no laptops, tablets, headphones, earbuds, smartwatches).
- No animals other than the one dog (Schatten) unless explicitly specified. No cats, no birds (EXCEPTION: the starling flock in P2, explicitly specified), no insects, no spiders, no bats, no rats, no mice.
- No food or drink items unless explicitly specified.
- The dog (Schatten) must ALWAYS look identical: medium-sized mixed breed, thin but healthy, wiry dense BLACK fur, pointed upright ears, AMBER EYES rendered as bright white highlights against dark fur. Old worn leather collar with a leash (Band 2: he is mostly OUTSIDE gates/walls). He looks like a black German Shepherd/Belgian Malinois mix, but thinner and wirier.

RECURRING CHARACTERS (keep identical across all images):
- Nora: girl, 12, practical, observant. Shoulder-length dark hair, often slightly tousled. Plain everyday clothes (jacket, jeans). Carries a small backpack and a notebook.
- Theo: boy, 10, Nora's younger brother. Shorter, a bit rounder face, expressive. Hoodie. Often nervous body language but trying to be brave.
- Brenner (the grey ghost): translucent grey male figure, an old gravedigger, stooped, head bowed, simple 19th-century working clothes. NEVER threatening. Rendered in lighter, hazier hatching than living people.
- Voss (the black ghost): a towering pitch-black silhouette, larger than a human, NO facial features, no eyes — pure black shape and oppressive presence. Always rendered as the darkest element in the image.
- Kloss: cemetery caretaker, 50s, stout, balding with a thin hair ring, knitted cardigan, sweating, anxious posture.

TECHNICAL:
- Portrait orientation (taller than wide).
- High contrast between deep black shadows and white highlights.
- Fine detailed crosshatching for midtones and textures.
- Resolution: minimum 2000x3000 pixels, 300 DPI.
- Aspect ratio target for generation: portrait (Nano Banana: choose tall/portrait; GPT-4o: portrait).
```

---

## Verteilung über die Pfade

Prinzip (wie Band 1): Bilder so verteilen, dass jeder Leser 7–9 sieht, und die stärksten/atmosphärischsten
Momente jedes Pfads abgedeckt sind. Mischung aus **Szenen** (Figuren/Orte) und **Artefakt-Close-ups** (Objekte).

| Bereich | Anzahl | Abschnitte |
|---------|--------|------------|
| Front Matter (Stadtkarte) | 1 (= Bild 1) | separate Seite |
| Prolog (alle Leser) | 3 | P1, P2, P3 |
| Pfad A | 4 | A2, A5, A7, A10 |
| Pfad B | 3 | B1, B3, B6 |
| Pfad C | 3 | C1, C5, C8 |
| Ende | 1 | EC1 |
| **Gesamt** | **15** | |

---

## ILLUSTRATION_MAP (für build_cyoa_taschenbuch_band2.py)

```python
# WICHTIG: Keys = exakte Graph-IDs (kurz: A2 nicht A02!), sonst greift die Zuordnung nicht.
ILLUSTRATION_MAP = {
    "P1":  [2],   # Schatten verweigert das Tor
    "P2":  [3],   # Zwei Zonen + auffliegende Stare
    "P3":  [4],   # Der kippende Stein + Silhouette
    "A2":  [5],   # Der Stein mit dem Hund (Artefakt)
    "A5":  [6],   # Die erste Blechdose im Schuppen (Artefakt)
    "A7":  [7],   # Zwei Geister: Brenner duckt sich vor Voss
    "A10": [8],   # Theo allein am Kapellenfenster (POV Nora außen)
    "B1":  [9],   # Das Archivblatt-Foto: H.B. + G. Voss (Artefakt) — DEINE IDEE
    "B3":  [10],  # Schuppen-Suche / Blechdose im UV-Licht
    "B6":  [11],  # Das unterirdische Registerbüro (Ort, klaustrophobisch)
    "C1":  [12],  # Kloß schwitzt + Doppelschatten im Bürofenster
    "C5":  [13],  # Protokollbuch 1886 mit Voss' Unterschrift (Artefakt)
    "C8":  [14],  # Kloß stellt sich vor Nora, klagt Voss an (Höhepunkt)
    "EC1": [15],  # Brenner aufrecht, löst sich auf; Schatten legt sich hin
}
# Bild 1 (Stadtkarte von Gravenstedt mit Markierungen) = separate Front-Matter-Seite.
```

---

## Die 15 Prompts

> Jeweils **Stil-Prefix + Szenen-Prompt**. Szenen-Prompts sind englisch (für Nano Banana / GPT-4o).

### Bild 1 — Stadtkarte (Front Matter)

**Motiv:** Frau Silbers handgezeichnete Karte von Gravenstedt — dasselbe Artefakt wie in Band 1. Sie zeigt
die ganze Stadt von oben, mit zwölf eingekreisten Orten (Geister), von denen einer durchgestrichen ist
(Lina, bereits befreit). Die Karte liegt auf Noras Schreibtisch. Kein lesbarer Text (KI rendert Schrift
unsauber) — Handschrift nur als angedeutete Kringel-Linien.

```
A close, slightly top-down view of an old hand-drawn map lying on a wooden desk, lit by a single warm desk lamp from the upper left (rendered as high-contrast light and deep shadow, pure black-and-white pen-and-ink, dense crosshatching — NO colour, NO grey wash).

THE MAP ITSELF: a careful but amateur cartographer's drawing of a fictional old German town called Gravenstedt, seen from above. A winding river cutting through the town. A dense tangle of narrow medieval streets and small rooftops drawn as tiny hatched blocks. A market square. A church. At the lower edge of the town, slightly apart, an old walled cemetery drawn with rows of tiny crosses and gravestones. The paper is aged and worn: soft fold creases, one dog-eared corner, faint water stains rendered as lighter mottled hatching, slightly curling edges.

THE MARKINGS (important): exactly TWELVE small hand-drawn circles scattered across different places of the town (the market, the harbour/river, near the church, side streets, and ONE circle directly on the walled cemetery at the lower edge). The circles look ink-drawn by hand, slightly uneven. ONE of the twelve circles is crossed out with a single firm X / strike-through (this one is the already-solved case). The cemetery circle is drawn a little heavier, as if recently traced over, to subtly draw the eye. NO numbers, NO letters, NO readable text anywhere — any 'writing' is only suggested as illegible looping pen-strokes.

MOOD: quiet, mysterious, the feeling of a private investigator's working document. A child's notebook and a pencil lie partly visible at the very edge of the frame. Portrait orientation, the map filling most of the frame.
```
*(Hinweis: Die zwölf Kreise + eine Durchstreichung sind Kanon — nicht ändern. Falls der Generator Text
erzeugt, im Re-Prompt „absolutely no legible text/numbers, only illegible scribbles" verstärken.)*

### Bild 2 — P1: Schatten verweigert das Tor

**Szene (P01):** Schatten weigert sich zum ersten Mal, irgendwohin mitzugehen. Die Leine spannt sich
straff, er gibt keinen Millimeter nach. Stärkster Beat: Nora steht halb durch das Tor (ein Fuß drinnen,
einer draußen), der Hund liegt/sitzt fest draußen und starrt wissend an ihr vorbei ins Dunkle dahinter.
Heller Herbstmorgen draußen — unheimliches Dunkel hinter dem Tor. Theo kniet beim Hund, Hand auf dessen Rücken.

```
A tall, old wrought-iron cemetery gate, the black paint peeling and flaking, topped with pointed rusted finials, one hinge bracket holding a small rusted blank sign plate (NO readable text on it — just rust and corrosion). The gate stands half-open, having just been pushed inward; faint motion lines or scuffed cobblestones suggest it just creaked open. Pure black-and-white pen-and-ink, dense crosshatching, high contrast, NO colour, NO grey wash.

LIGHT: clear golden autumn morning OUTSIDE the gate — bright cobblestone pavement, long crisp shadows, sharp white highlights. BEHIND the gate: unnaturally dense darkness. Tall old chestnut trees crowd close behind the bars so thickly that the inside of the cemetery is swallowed in deep black shadow, even though it is a sunny morning. This light/dark contrast between the bright street and the black interior is the emotional core of the image.

THE DOG (Schatten): a thin but healthy medium-sized mixed-breed dog with wiry dense BLACK fur, pointed upright ears (black German-Shepherd/Malinois mix, but leaner). CRUCIAL recurring feature — his EYES must clearly GLOW: render both eyes as two distinct BRIGHT WHITE highlights shining out of the dark fur, the single brightest points on the dog, unmistakable even though he is dark (this is his signature look across every illustration).

His POSTURE must clearly read as REFUSAL, not walking: he is OUTSIDE the gate on the bright pavement, BRACING himself AWAY from the gate — front legs stiff and angled, weight leaned BACKWARD against the pull, sitting/haunching low, all four paws dug in and resisting. The old leather LEASH runs from his collar toward the gate and is pulled drum-TIGHT and straining, clearly being pulled FORWARD while the dog leans BACK and will not budge (a tug-of-war the dog is winning by sheer stubbornness). He is NOT stepping forward and NOT leaving the frame. His head is turned to stare fixedly THROUGH the gate into the darkness, as if he sees something there no one else can — a low, knowing dread in his whole body (warning, not aggression).

THE CHILDREN: Nora, a practical 12-year-old girl with shoulder-length tousled dark hair, plain jacket and jeans, a small backpack, caught mid-step in the gateway — ONE foot inside the dark threshold, ONE foot still on the bright pavement — turning back to look at the dog, the taut leash in her hand. Theo, her 10-year-old brother, rounder face, hoodie, has crouched down beside the dog with one hand resting gently on the dog's back, looking up worried.

COMPOSITION: portrait orientation, the gate towering over the children, the bright street in the lower/foreground, the black gateway dominating the upper half. MOOD: the loyal dog who follows them everywhere suddenly refuses — quiet dread, something is wrong.
```

### Bild 3 — P2: Zwei Zonen + Stare

**Szene (P02):** Die Kinder stehen genau an der Grenze zwischen dem gepflegten vorderen Friedhof und dem
namenlosen hinteren Teil. Nora misst mit dem Handy die Kälte (ihr Atem steht als weiße Wolke — Zeichen
der übernatürlichen Kälte). Im Höhepunkt brechen schlagartig alle Stare auf einmal aus den Kastanien.
**Hauptaktion = der explosionsartige Stare-Aufbruch; die zwei Zonen sind das Setting drumherum.**

```
A cemetery seen at ground level, sharply divided into two worlds by a narrow unpaved dirt path that runs across the middle of the image like a threshold line. Pure black-and-white pen-and-ink, dense crosshatching, very high contrast, NO colour, NO grey wash.

LEFT / FOREGROUND ZONE (the tended part): large upright 19th-century gravestones, neat and well-kept, one with a carved stone angel, fresh chrysanthemum flowers standing in vases on the graves, the gravel raked into clean lines. Lighter, calmer, more white space.

RIGHT / BACKGROUND ZONE (the nameless part): small, low, crooked sandstone markers, leaning at odd angles, swallowed by thick dark moss that has erased every inscription — these stones are BLANK (no text, no names). Rendered darker, denser hatching, creeping shadow. This half feels colder and wrong.

THE CHILDREN at the dividing path: Nora (12, tousled dark shoulder-length hair, jacket, jeans, small backpack) has stepped just across the line into the nameless zone, holding a small simple smartphone out in front of her to read it; her breath rises as a clear WHITE PUFF of fog in front of her mouth (the only 'cold' cue — it is autumn but not winter, so the visible breath is unnatural and important). Theo (10, hoodie, rounder face) stands a step behind her on the tended side, flinching.

THE SHOCK (main action): from the tall dense chestnut trees above and behind them, a huge flock of starlings ERUPTS all at once — a violent black torrent of hundreds of birds bursting upward into the sky in a single explosive surge, wings rendered as sharp black slashes and chaotic motion. The suddenness is the point: it should read as a startling BANG of black against the sky. (Birds are normally not allowed in these illustrations — this starling flock is the one explicit exception.)

COMPOSITION: portrait orientation. Lower half = the two divided zones and the children at the threshold; upper half = the exploding flock and dark chestnut canopy. MOOD: a beautiful sunny autumn morning that has suddenly turned wrong.
```

### Bild 4 — P3: Der kippende Stein

**Szene (P03):** Direkt nach dem Stare-Aufbruch — plötzliche Totenstille. Drei Meter vor den Kindern
kippt langsam ein kleiner, moosbedeckter Grabstein um, von selbst, ohne Wind, ohne Geräusch. Im selben
Augenblick steht für eine Sekunde zwischen zwei weiter hinten gelegenen Steinen eine dunkle, schmale,
aufrechte Gestalt — zu still für einen Menschen. **Hauptmotiv = der kippende Stein im Vordergrund; die
Silhouette ist ein subtiler, kaum sichtbarer Hintergrund-Schauer, den die Kinder noch NICHT bemerkt haben.**

```
The nameless, neglected section of an old cemetery, in the cold shadow of tall chestnut trees, even though it is morning. Pure black-and-white pen-and-ink, dense crosshatching, very high contrast, NO colour, NO grey wash. The sky above is suddenly EMPTY — not a single bird left — conveying a heavy, dead silence after the flock has gone.

MAIN SUBJECT (foreground, ~3 metres from the viewer): a small, low, moss-covered sandstone gravestone caught mid-fall, tilting over at an unnatural angle, about to topple into the tall grass. Crumbs of dark earth and a little dust break loose from its base as it moves. CRUCIAL DETAIL: NOTHING ELSE in the scene is moving — the tall grass around the stone stands perfectly straight and still, the trees are motionless, there is clearly NO WIND and NO hand touching the stone. The stone falls entirely by itself. This contrast (everything frozen still, only the stone moving) is what makes it uncanny. Show the impossible motion through the stone's steep tilting angle and the loosened soil, while all surrounding grass blades stay rigid and upright.

THE SILHOUETTE (mid-background, subtle, easy to miss on first glance): far behind the falling stone, between two upright gravestones, a thin, dark, perfectly upright human-shaped silhouette — featureless, rendered as the deepest black in the image, unnaturally still, too motionless to be a living person. It is half-glimpsed, partly hidden by a gravestone, almost blending into the shadows. The children have NOT noticed it yet — it is there for the reader to spot, not them.

THE CHILDREN (foreground): Nora (12, tousled dark hair, jacket, jeans, backpack) and Theo (10, hoodie), both staring in shock at the FALLING STONE in front of them, recoiling half a step back, eyes on the stone — NOT looking at the distant silhouette behind it.

COMPOSITION: portrait orientation, the toppling stone and the recoiling children in the lit foreground, the dark still silhouette small and barely visible deep in the shadowy background. MOOD: oppressive dead silence, a single impossible movement, an unseen watcher.
```

### Bild 5 — A2: Der Stein mit dem Hund (Artefakt-Close-up)

**Szene (A2):** Nora findet einen breiten Grabstein ohne Namen, in den nur ein Hund und „1887" gemeißelt
sind. Schlüsseldetail: Der Stein ringsum ist uralt und vermoost — aber die eingravierten Linien sind
**glatt, scharf, kaum verwittert, als hätte sie jemand nachgezogen** (heimliche Pflege = Mystery-Hinweis).
Die Hund-Gravur ähnelt auf unheimliche Weise Schatten (sitzend, Spitzohren).

```
Extreme close-up of a broad, flat, weathered sandstone grave marker lying low to the ground, filling most of the frame. This MUST be a hand-drawn PEN-AND-INK ILLUSTRATION with visible ink lines and dense CROSSHATCHING — NOT a photograph, NOT photorealistic, NOT a black-and-white photo. Everything (stone, moss, hand, grass) is rendered in drawn ink hatching and stippling, the same illustrated style as the other interior illustrations. NO colour, NO greyscale photo wash, high contrast. (Artefakt close-ups like this tend to drift into photorealism — actively avoid that: keep it clearly an ink drawing.)

THE STONE: clearly very old — the surrounding surface is pitted, cracked and edged with thick dark moss that creeps in from the corners (on neighbouring stones this moss has swallowed everything). BUT the centre of this stone has been kept clear of moss, as if someone tends it in secret.

THE CARVING (the focal point): cut into the cleared centre, a CRUDE, simple, almost pictogram-like engraving of a SITTING DOG in profile — pointed upright ears, tail tucked close to the body — carved by a 19th-century stonemason with only a few rough, confident chiselled lines, reduced and slightly naive, NOT a fine realistic animal portrait. Despite its crudeness, the silhouette unmistakably resembles Schatten (the children's thin, pointed-eared dog) — an uncanny echo. Below the dog, carved deep: the number 1 8 8 7. NO name, NO letters, NO other text — only the dog symbol and that one year.

CRUCIAL UNCANNY DETAIL: while the stone itself is ancient and worn, the engraved lines of the dog and the number are SHARP, smooth and CLEAN at the edges — far fresher than the weathered stone around them, as if a hand has recently re-traced every groove. Light this so a low raking light catches the carved grooves: the fresh sharp lines throw crisp deep shadows, while the old weathered surface stays soft — making the contrast 'old stone / freshly tended carving' visible.

CONTEXT: a child's hand (Nora's), itself clearly drawn in ink hatching (NOT a photoreal hand), enters at the lower edge of the frame, fingertips just brushing along the carved grooves. Far in the background, half-sunk in the grass, a second small blank gravestone is barely visible (the 'H.B.' stone, loosely/lightly drawn to push it back). Cold shade of chestnut trees. MOOD: a quiet, deeply mysterious discovery — someone has been caring for an unmarked grave for a very long time. Reminder: rendered entirely as a pen-and-ink crosshatched illustration, never as a photograph.
```

### Bild 6 — A5: Die Blechdose im Schuppen (Fund, normales Licht)

**Szene (A5):** Die Kinder sind im alten Werkzeugschuppen EINGESPERRT (die Eisentür ist von selbst
zugefallen, KEIN Griff von innen). Im Halbdunkel finden sie hinter einer losen Wandplanke eine versteckte
runde Blechdose mit einer alten Namensliste (23 Namen, ganz unten nachgetragen „Johann — mein Sohn",
emotionaler Beat). Ganz hinten im tiefsten Schatten ein kaum wahrnehmbarer grauer Hauch — die Kinder
sehen ihn noch nicht. **(Abgrenzung: Dies ist der Fund bei normalem Licht. Bild 10 zeigt dieselbe Dose
später unter UV-Licht — nicht verwechseln.)**

```
Interior of an old, cramped wooden tool shed, dim and claustrophobic. Pure black-and-white pen-and-ink, dense crosshatching, very high contrast, NO colour, NO grey wash. Rusted tools hang on the plank walls — spades, rakes, a sledgehammer; a half-collapsed shelf; dried earth and dead leaves on the floor.

THE TRAP (important background detail): on one wall a heavy IRON DOOR is shut tight, and on its inner side there is clearly NO handle — just smooth iron and a few desperate scratch marks near the bottom. This conveys that the children are locked in. Thin hard shafts of light fall from a small, filthy skylight high in the wall, the only light source.

THE DISCOVERY (focal point, lit by a shaft of that light): in the back wall, a broad wooden plank has been pried loose, revealing a fist-sized hollow cavity behind it. Out of the cavity has come a round old TIN CAN — paint flaked and peeling, a rusted pry-tab lid, now opened. Beside it on the rough boards lies a folded, yellowed sheet of paper covered in dense, looping old handwriting — clearly a LIST of many names in narrow rows (rendered as convincing illegible old script — NO actual readable letters or words). The focused shaft of light falls precisely on the can and the list, leaving the rest of the shed in deep shadow.

THE CHILDREN: Nora (12, tousled dark hair, jacket, backpack) kneels and holds the yellowed list carefully in both hands, reading, her expression tightening with quiet emotion (she has just seen the last line about a son). Theo (10, hoodie) leans in close beside her, looking at the list, uneasy.

THE FIRST HINT (very subtle, easy to miss): in the deepest, darkest back corner of the shed — far from the light — the faintest, barely-there suggestion of a translucent grey human shape just beginning to coalesce out of the shadow. It is almost invisible, NOT yet a clear figure, and the children have NOT noticed it. It is there only for the attentive reader.

COMPOSITION: portrait orientation, the lit can-and-list in the lower foreground, the locked handleless iron door and the faint grey hint in the shadowed background. MOOD: locked in, a haunting discovery, an emotional gut-punch (a father who listed his dead son), and something forming in the dark.
```

### Bild 7 — A7: Zwei Geister (der Twist-Beat)

**Szene (A7):** Der Schlüsselmoment des ganzen Buches im Bild: Es gibt ZWEI Geister, und sie sind
Gegensätze. Der graue Geist (Brenner) ist das Opfer — er duckt sich in eingeübter Schutzhaltung, wie
jemand, der diese Schläge schon hundertmal bekommen hat. Der schwarze Geist (Voss) ist der Täter — er
kommt DURCH die Schuppenwand, ragt fast bis unters Dach, wirft einen Spaten. Die Kinder werfen sich zu Boden.
**Wichtigster Rendering-Befehl: die zwei Geister müssen optisch GEGENSÄTZLICH aussehen (hell-transparent vs. massiv-schwarz).**

```
Inside the cramped dark tool shed, a violent supernatural moment. Pure black-and-white pen-and-ink, very high contrast, NO colour, NO grey wash. The two ghosts MUST be rendered as visual opposites — this contrast is the whole point of the image:

THE GREY GHOST (Brenner, the victim): a TRANSLUCENT, pale, hazy male figure — an old stooped gravedigger in simple 19th-century working clothes. Render him in LIGHT, thin, airy hatching so he looks faint and see-through, almost made of mist; the shed wall is faintly visible through him. His posture is the emotional heart: he has spun around and is COWERING — shoulders hunched up to his ears, head twisted away, both arms half-raised to shield his face — the practised, automatic flinch of someone who has taken these blows a hundred times before. He is small, bowed, defenceless.

THE BLACK GHOST (Voss, the threat): the absolute OPPOSITE — a towering, pitch-BLACK, solid, featureless silhouette, the single darkest mass in the entire image, no face, no eyes, larger than a man, almost reaching the shed roof so the low ceiling makes him feel crushing and oppressive. He is stepping THROUGH the wooden plank wall as if it were paper (show planks behind/around him, his black shape emerging straight through them). He radiates menace and downward pressure.

THE ATTACK: a heavy iron SPADE has been torn from the wall and flies fast and flat across the shed like a thrown blade, mid-air, just over the children — a genuine near-miss, aimed where a head just was.

THE CHILDREN (foreground, low): Nora (12) is actively YANKING her little brother Theo (10) down to the dirt floor by his arm to get him under the flying spade — she is protecting him, mid-motion, both dropping low. Fear on their faces.

COMPOSITION: clear depth layering so it does not feel crowded — Voss looming large and black at the back/top; Brenner cowering pale in the middle; the spade slicing across; the two children low in the front. MOOD: terror and revelation — the reader instantly understands one ghost is a frightened victim, the other a towering aggressor.
```

### Bild 8 — A10: Theo allein am Kapellenfenster (POV nora_aussen)

**Szene (A10):** Theo ist allein in der Kapelle eingesperrt. STRENGE POV-REGEL: alles von AUSSEN, aus
Noras Blick — wir sehen Theo NUR durch das hohe Fenster. Der Grusel: Theo steht ruhig mitten im dunklen
Raum und REDET halblaut mit jemandem, den Nora (und der Betrachter) NICHT sehen kann. Nora hat sich am
schmalen hohen Fenstersims hochgezogen und späht hinein. Schatten bricht durch — gerissenes Halsband —
und wirft sich gegen die Kapellenwand. **Tageszeit: trübes Tageslicht/Dämmerung, NICHT Nacht.**

```
Exterior view of a small, squat stone cemetery chapel wall in dull, overcast DAYLIGHT (early evening grey — NOT night). Pure black-and-white pen-and-ink, dense crosshatching, very high contrast, NO colour, NO grey wash. A dead fallen tree leans against the rough stone wall, its trunk having cracked the window frame. Brambles claw at the base of the wall.

THE POINT OF VIEW IS STRICTLY FROM OUTSIDE THE CHAPEL (this is essential). High up in the stone wall: one narrow, tall window with a cracked, broken frame.

NORA (outside): a 12-year-old girl has JUMPED and pulled herself up, hanging by her fingers from the narrow window ledge, body pressed and straining against the rough wall, one cheek to the stone, peering desperately through the gap. Her position is awkward and precarious — clearly hard work, not comfortable tiptoes. This is how we, the viewer, see inside.

THROUGH THE WINDOW (Theo, the horror beat): inside the dark chapel, small and far below in the cone of a little flashlight, her 10-year-old brother Theo stands CALMLY in the middle of the stone room — not panicking, not at the wall — turned toward an empty patch of darkness and clearly TALKING to it, mid-sentence, as if having a quiet conversation. CRUCIAL: there is NO visible figure he is talking to — the spot he faces is just dark and empty (at most the faintest, almost-invisible hint of something). The viewer shares Nora's dread of not being able to see who is there.

SCHATTEN (the breakthrough payoff): at the base of the same chapel wall, the thin black dog with amber-white-highlight eyes has just smashed onto the cemetery grounds — a snapped, torn piece of leather collar/leash still trailing from his neck — and hurls himself bodily against the stone wall, as if trying to break through it with his head to reach Theo. Pure desperate force.

COMPOSITION: a strong VERTICAL stack along the single chapel wall so it reads as one connected moment — Nora hanging at the high window (upper), tiny Theo glimpsed talking through the window glass, the dog flinging himself at the wall below. MOOD: helpless dread — a brother locked in, talking to something unseen, a sister who can't reach him, a dog breaking every rule to get in.
```

### Bild 9 — B1: Das Archivblatt-Foto (Artefakt — deine Idee)

**Szene (B1):** Im Stadtarchiv: ein alter Friedhofs-Registerband, aus dem die Sektion-C-Seiten absichtlich
HERAUSGERISSEN wurden (erster Beweis, dass jemand etwas verbirgt). Am Rand der letzten verbliebenen Seite
stehen zwei Namen in zwei sehr verschiedenen Handschriften: „H.B." klein und heimlich mit Bleistift,
„G. Voss" fest und dunkel mit Tinte. Theo fotografiert die Seite. **WICHTIG für den späteren Twist
(B2): ‚G. Voss' ist hier NOCH NICHT durchgestrichen — der Name ist ganz und unversehrt.** Der Strich
erscheint erst später auf dem Foto, nicht hier.

```
Extreme close-up, top-down, of an open old leather-bound archive ledger lying on an archive reading table, lit by the focused pool of a single archive desk lamp; fine dust motes hang in the beam. Pure black-and-white pen-and-ink, dense crosshatching, very high contrast, NO colour, NO grey wash. The paper is aged, foxed and yellowed (rendered through hatching), with faint ruled columns of old handwriting.

THE TORN-OUT PAGES (plot-central, must be obvious): in the middle of the open book, several pages have been deliberately TORN OUT — a ragged line of frayed paper stubs left along the spine/gutter, the book gaping open at that gap. This sabotage should be clearly visible, not subtle.

THE TWO NAMES (the focal point — these specific letters ARE the subject of the image, so this small bit of lettering is intentionally allowed here, unlike the no-text rule elsewhere): on the narrow margin of the last remaining page, two short handwritten marks side by side, in two CONTRASTING hands —
  • "H.B." — tiny, faint, nervous PENCIL, lightly and secretly scratched in, almost shy.
  • "G. Voss" — right beside it, in a completely different hand: firm, confident, in dark, heavy, slightly glossy INK (this stands in for red ink in black-and-white — render it as the boldest, darkest writing on the page).
CRITICAL: the name "G. Voss" is WHOLE and INTACT — there is absolutely NO line, NO strike-through, NO cross-out over it. Keep it perfectly clean and un-marked. (Apart from these two short names, NO other readable words anywhere — all surrounding handwriting is illegible old script.)

THE PHOTOGRAPHING: at the upper edge of the frame, a child's hands hold a simple smartphone over the page, screen facing down toward the book, in the act of taking a photo (the phone is a secondary edge detail, the real page is the subject). 

MOOD: a cold, quiet, detective-like discovery in a hushed archive — the first hard evidence that someone tore the truth out of the record.
```

### Bild 10 — B3: Die Liste unter UV-Licht (forensisches Close-up)

**Szene (B3):** Auf Pfad B leuchtet Nora die gefundene Namensliste mit einer schmalen schwarzen
UV-Lampe (aus Frau Silbers Wohnung) ab. Unter dem UV-Licht tritt VERBORGENE Schrift hervor, die im
normalen Licht unsichtbar war: weitere Namen und ganz unten ein abgesetzter Hinweissatz. **Abgrenzung
zu Bild 6 (A5): Bild 6 ist die weite Schuppen-Fundszene bei normalem Licht mit grauem Hauch im Schatten.
Bild 10 ist ein ENGES, fast forensisches Close-up auf das Blatt selbst unter UV — KEIN Geist, keine
weite Schuppenkulisse, andere Bildsprache.**

```
A tight, near-forensic close-up of an old yellowed sheet of paper (the unfolded name-list) lying on rough wood, examined under ultraviolet light in an otherwise dark space. Pure black-and-white pen-and-ink, dense crosshatching, very high contrast, NO colour, NO grey wash. The framing is CLOSE on the paper — almost the whole frame is the document; we do NOT see the wide shed interior (this keeps it clearly different from Bild 6).

THE TWO LAYERS OF WRITING (the key effect): on the same sheet, two kinds of handwriting coexist —
  • the ORIGINAL list: rows of dense, dark, normal old ink handwriting (the visible names), rendered as ordinary dark script.
  • the HIDDEN writing revealed by UV: between and below the normal lines, additional faint writing GLOWS — rendered as bright, ghostly, luminous lines standing out PALE against the darkened paper, clearly a different, secret layer that was invisible before. At the very bottom, one separate revealed line stands apart, glowing (this is the crucial clue pointing to the buried book).
  IMPORTANT: keep ALL of this handwriting ILLEGIBLE — convincing looping old script and glowing strokes, but NO actual readable letters or words (the reader learns the wording from the text, not the image).

THE LIGHT: a slim black UV flashlight held at the edge of frame casts a hard pool of ultraviolet glow across the page; everything outside that pool falls into deep black shadow. The light comes from a low angle.

THE CHILDREN (partial, at the upper edge): the faces of Nora (12) and Theo (10) lean in from above, lit eerily FROM BELOW by the UV pool — sharp highlights on chins and noses, eye sockets in shadow — both intent, investigative, slightly unsettled. Only their lit faces and a hand holding the flashlight are in frame.

MOOD: cool, precise, detective-like (Pfad B's identity) — the quiet thrill of hidden writing surfacing out of nowhere, as if the dead are slipping a secret message to the living.
```

### Bild 11 — B6: Das unterirdische Registerbüro

**Szene (B6):** Über eine Falltür im Boden steigen die Kinder in ein winziges, niedriges Kellerbüro von
1886, in dem seit Jahrzehnten niemand war. Theo muss den Kopf einziehen, so niedrig ist die Decke
(gezeigte, nicht behauptete Klaustrophobie). Nora zieht aus einem Regal das schwarze Protokollbuch.
Subtiler Mystery-Hinweis: Die Falltür ging zu leicht auf — als hätte jemand gewollt, dass sie hereinkommen.

```
A tiny, low, cramped underground records room from the 1880s, buried beneath a cemetery office, where no one has set foot in decades. Pure black-and-white pen-and-ink, dense crosshatching, very high contrast, NO colour, NO grey wash. The ONLY light is a child's flashlight beam plus a thin pale shaft of daylight falling from an open trapdoor in the ceiling above.

THE CLAUSTROPHOBIA (shown, not stated): the stone ceiling hangs oppressively LOW, right above the children's heads. Theo (10, hoodie) stands with his head and shoulders visibly DUCKED, hunched under the low ceiling, holding the flashlight — his cramped posture is the main cue for how tight the space is. The walls press close on all sides.

THE ROOM: dusty desks furred with decades of grime; sagging wooden shelves crammed with bulging, warped old file folders and rolled documents; an old typewriter in the corner draped in thick cobweb; a toppled chair; thick dust hanging and swirling in the flashlight beam. Everything coated in undisturbed grey dust (rendered in hatching, no actual grey wash — use stippling/texture).

THE FIND (focal point): Nora (12, tousled dark hair, jacket, backpack) pulls a thick, heavy ledger bound in black leather with a faint gold-stamped spine from a shelf — the flashlight beam falls directly on this book so it is the brightest, sharpest object in the frame, drawing the eye. Dust cascades from it.

TWO SUBTLE DETAILS: (1) up at the trapdoor, a single old file folder has been wedged into the gap to PROP THE DOOR OPEN (cautious Nora refusing to be trapped). (2) very subtly, in the thick dust on the floor or a shelf, a FRESH disturbance — a clean wipe-mark or recent track — hinting someone passed through here not long ago, despite the decades of dust.

COMPOSITION: portrait, the low ceiling crushing down from the top of the frame, the pale daylight shaft from the trapdoor above, the flashlight-lit ledger and the two children below in the tight black space. MOOD: buried, airless, claustrophobic, the cold thrill of a forgotten room giving up its secret.
```

### Bild 12 — C1: Doppelschatten im Bürofenster

**Szene (C1):** Nora dreht sich im Weggehen noch einmal um und sieht durch das Fenster des
Verwalterhäuschens: Kloß steht allein im Raum mit seiner gesprungenen Tasse — aber in der GLASSCHEIBE
spiegelt sich nicht nur er, sondern eine zweite, größere dunkle Gestalt direkt hinter ihm, die im echten
Raum nicht da ist. Der Schauer passiert am hellichten Vormittag. **Wichtig: es ist eine Spiegelung IM
GLAS, kein Schlagschatten an der Wand.**

```
View from OUTSIDE a small brick cemetery caretaker's office, looking in through its window, in bright clear MID-MORNING daylight (NOT dusk, NOT night — the daytime setting makes the haunting more unsettling). Pure black-and-white pen-and-ink, dense crosshatching, very high contrast, NO colour, NO grey wash. On the office door, small sign plates (NO readable text — only the shapes of signs). Through the window: a glimpse of an office interior — cemetery section maps pinned on the walls, a desk, a cracked empty coffee cup.

THE MAN: inside, the caretaker Kloss (mid-50s, stout, balding with a thin ring of hair, sweating despite the mild day, wearing a knitted cardigan) stands alone in the middle of the room, holding the cracked cup, his back/side to the window, an anxious slumped posture. He has just bolted the door. He does NOT know anything is behind him.

THE HORROR (key effect — a REFLECTION in the glass, not a wall shadow): in the surface of the window GLASS we see Kloss reflected — and overlapping his reflection, standing directly BEHIND him, a SECOND figure that is not present in the real room: a taller, pitch-black, featureless silhouette (the same visual language as the black ghost Voss elsewhere — larger than a man, no face, the darkest mass in the image). The single man casts/owns TWO shapes in the glass: his own ordinary reflection, and this second towering dark one that does not match his posture. It should read as: one man alone in the room, but two silhouettes in the window.

NORA (foreground, outside): seen from behind/over her shoulder, the 12-year-old girl has half-turned away to leave and frozen mid-step, looking back through the glass, just catching the second silhouette — the moment of almost having missed it. Her stillness conveys dawning dread.

COMPOSITION: portrait. Foreground = Nora's shoulder/head outside, looking in. Middle = the bright window pane carrying both the see-through view of Kloss AND the uncanny double reflection. Subtle and quiet, not flashy — the kind of detail you have to look twice at. MOOD: broad daylight, an ordinary nervous man, and something enormous standing behind him that only the glass reveals.
```

### Bild 13 — C5: Das Protokollbuch 1886 (Artefakt-Close-up)

**Szene (C5):** Im unterirdischen Registerbüro — diesmal hat KLOSS aufgeschlossen und ist dabei. Nora
findet im dicken schwarzen Protokollbuch die Seite vom 12. November 1886 mit Voss' offizieller, gestempelter,
UNTERSCHRIEBENER Genehmigung der Massengräber: der schriftliche Beweis. **Abgrenzung zu Bild 9: Bild 9 ist
eine heimliche Bleistift-Randnotiz auf einer zerrissenen Registerseite. Bild 13 ist ein dickes, offizielles,
gestempeltes Protokollbuch mit großer schwungvoller Unterschrift — ein Amtsdokument, kein Geheimkritzel.**

```
A close-up, top-down view of a thick, heavy ledger bound in black leather, lying open on a dusty old desk in the cramped underground records room, lit by the hard yellow-tinged cone of an old long-handled flashlight. Pure black-and-white pen-and-ink, dense crosshatching, very high contrast, NO colour, NO grey wash. Dust motes in the beam; deep black shadow all around the single lit page.

THE PAGE (the focal point): a full official 19th-century minutes page, densely filled with neat columns of formal old administrative handwriting (rendered as convincing but ILLEGIBLE old script — NO actual readable words). What makes THIS book different from the torn archive page in Bild 9: this is clearly a formal, intact, official record book — and at the BOTTOM of the entry sit the two marks that matter most:
  • a large, bold, confident SIGNATURE with a sweeping flourish — deliberately rendered as an authentic signature scrawl, NOT cleanly legible (a real signature is loops and strokes, so this elegantly avoids readable text while clearly being 'a powerful man's signature').
  • beside/over it, a round official INK STAMP (just the circular stamped shape and inner rings — NO readable text inside it).
These two elements — signature and stamp — are the DARKEST, sharpest, most deliberate marks on the page, where the eye lands: the proof of guilt.

THE HANDS: a girl's hand (Nora's) rests at the edge of the page, fingertips just beside the signature, having gone still. At the opposite edge of the frame, a second, older adult hand and the long-handled flashlight belong to Kloss — subtly signalling he is the one lighting this discovery (the descendant of the accomplice illuminating the evidence). Only the hands and the flashlight are in frame, not full figures.

MOOD: cold, hushed, weighty — the quiet horror of a crime confessed in tidy official handwriting and signed without shame, found a century too late.
```

### Bild 14 — C8: Kloß klagt Voss an (Höhepunkt Pfad C)

**Szene (C8):** Der Wendepunkt des Pfads: Der ängstliche Verwalter Kloß überwindet sich, schiebt sich mit
seinem ganzen Körper schützend zwischen die geduckten Kinder und den riesigen schwarzen Geist Voss — und
liest dessen Schuld LAUT und anklagend aus dem Protokoll vor („Ich lasse mich nicht mehr einschüchtern").
Voss ist auf dem HÖHEPUNKT seiner Macht (noch nicht zerfallend). Schatten bellt vom Türrahmen her als
Verbündeter. **Tageszeit: erstes Morgengrauen, 5 Uhr (dunkel mit erstem Lichtstreif) — korrekt.**

```
Inside a cramped, cold stone chapel in the near-dark of 5 a.m. (a faint sliver of dawn light at a high window; otherwise deep shadow). Pure black-and-white pen-and-ink, dense crosshatching, maximum contrast, NO colour, NO grey wash.

VOSS (at the peak of his power, NOT yet dissolving): a towering, pitch-BLACK, solid, featureless silhouette — no face, no eyes — the single darkest mass in the image, so large that he is too big for the room, bending and pressing up against the low chapel ceiling, radiating crushing downward pressure that seems to compress the whole space. He dominates one half of the frame.

THE COURAGE BEAT (emotional core): the caretaker Kloss — stout, balding, sweating, in his knitted cardigan, an ordinary frightened man — has stepped forward and planted his whole broad body BETWEEN the towering blackness and the children. He is clearly terrified (sweat, trembling hands) but standing his ground, head RAISED, and he is actively READING ALOUD an accusation from an open record book / file held in his shaking hands — mouth open mid-sentence, accusing the black figure. This contrast — a small, soft, scared man squarely facing a giant of darkness — is the whole point of the image.

THE CHILDREN: Nora (12) and Theo (10) are low and DUCKED behind Kloss's protecting body, shielding their heads, small against the threat — making Kloss look larger and braver by contrast.

THE VIOLENCE: a heavy stone grave slab has just been torn from the chapel wall and hurtles across the room with force (motion, dust, debris), a real and dangerous projectile, not a gentle float.

SCHATTEN (the ally): in the open chapel doorway stands the thin black dog, amber eyes as bright white highlights, barking hard and bright toward Voss — backing Kloss up, no longer afraid of the cemetery.

PROPS: an open ledger on the stone floor / in Kloss's hands (the proof he reads from). COMPOSITION: portrait, Voss's black mass looming top and one side, Kloss standing defiant in the centre with the book, ducked children behind, the dog barking from the lit doorway. MOOD: terror meeting defiance — the moment a coward finally speaks the truth out loud.
```

### Bild 15 — EC1: Brenners Befreiung (warmer Schluss-Gipfel)

**Szene (EC1):** Das letzte Bild des Buches — bewusst das GEGENTEIL von Bild 14 (dort Schwärze/Angst,
hier Licht/Frieden, derselbe Raum verwandelt). Voss ist fort. Brenner steht zum ersten Mal aufrecht,
Kopf erhoben; Nora und Theo lesen gemeinsam seine 47 Namen vor; bei Johanns Namen wird es ganz leise.
Brenner schließt die Augen, formt ein lautloses „Danke" und löst sich sanft auf wie Morgennebel. Kloß
sitzt erschöpft dabei und hört zu. Schatten kommt friedlich herein und legt sich auf die warme Stelle,
wo Brenner stand. Ruhige, helle, „atmende" Abschluss-Komposition.

```
Inside the same small stone chapel as the previous scene, but utterly TRANSFORMED: where there was crushing blackness, soft warm dawn light now streams in through the high window and pools on the floor. Pure black-and-white pen-and-ink, but with much MORE white space and light, gentler, softer hatching than the tense images — this should feel calm, warm and final. NO colour, NO grey wash.

BRENNER (freed, the emotional centre): the translucent grey ghost of the old gravedigger stands UPRIGHT for the first time — no longer stooped or cowering — head RAISED, shoulders open, dignified and at peace. His EYES ARE CLOSED and his lips form a silent, soundless word of thanks ('Danke'). He is gently beginning to DISSOLVE, like morning mist burning off in sunlight — rendered with light, thinning, dispersing hatching from the edges inward, the warm light passing through him. Serene, not sad.

THE CHILDREN: Nora (12) and Theo (10) stand close together, sharing one open book (Brenner's ledger of names) between them, reading aloud TOGETHER, heads bowed slightly over the page, their expressions soft and moved (they have just reached the little son's name). On the floor beside them, a small open tin can with a tiny dried bound twig inside it (Johann's keepsake) — a quiet detail.

KLOSS: the caretaker sits heavily on a low stone nearby, the old file resting on his knees, exhausted and quiet, simply listening — his courage spent, his part done. His presence completes his arc.

SCHATTEN (his arc resolved): the thin black dog with amber-white-highlight eyes has come calmly in through the open chapel door — no panic now — crosses to the warm patch of light where Brenner stood, lies down there, and lets out a deep settling sigh with his eyes closing. The dog that refused this cemetery now rests peacefully inside it.

COMPOSITION: portrait, balanced and open, lots of warm light and air — the visual opposite of the dark cramped tension before. MOOD: profound gentle relief, peace, an ending — a man finally allowed to rest, remembered by name.
```

---

## Build-Einbindung

Sobald die 15 Bilder generiert sind:
1. Als `Illustration 1.png` … `Illustration 15.png` in `Band2/CYOA/Illustrationen/` ablegen.
2. In `Scripts/build_cyoa_taschenbuch_band2.py` das `ILLUSTRATION_MAP` (oben) eintragen.
3. Bild 1 (Stadtkarte) wird wie in Band 1 als separate Front-Matter-Seite gesetzt.
4. Build neu laufen lassen — `get_illustration_path` lädt sie automatisch.
