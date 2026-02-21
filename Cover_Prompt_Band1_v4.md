# Cover-Prompt v4 -- Band 1: Das Haus, das fluestert

## Was ist neu in v4?

Dieser Prompt basiert auf dem Original (Cover_Prompt_Band1.md) und adressiert gezielt die 8 Illustrationsprobleme aus dem v3-Cover:

| Problem in v3 | Loesung in v4-Prompt |
|----------------|----------------------|
| "HILF" fehlt im Fenster | Eigener Abschnitt, als CRITICAL REQUIREMENT markiert |
| Stockwerke nicht differenziert | 3-Zonen-Beleuchtung separat und detailliert beschrieben |
| Stadtskyline fehlt | Explizit als eigenes Element im Background |
| Haustuer nicht sichtbar offen | "SLIGHTLY AJAR with PITCH DARKNESS" betont |
| Keine Nebel-Ranken | Detaillierte Beschreibung der Nebel-Richtung und -Quelle |
| Theos Jacke braun statt olivgruen | "OLIVE-GREEN (NOT brown)" mit Wiederholung |
| Keine Geister-Andeutungen | Als separates Bildelement beschrieben |
| Kamerawinkel zu flach | Erster Satz der Komposition, fett markiert |

---

## Verwendung

### Variante A: Direkt als ChatGPT-Prompt (empfohlen)

1. ChatGPT oeffnen (GPT-4o mit Bildgenerierung)
2. Das aktuelle v3-Cover hochladen mit der Nachricht:

> Hier ist das aktuelle Cover meines Kinderbuchs. Ich brauche eine komplett neue, verbesserte Version. Bitte generiere ein neues Bild basierend auf der folgenden detaillierten Spezifikation. Generiere NUR die Illustration -- KEINEN Text ausser dem Wort "HILF" das im Fenster geschrieben steht.

3. Dann den Haupt-Prompt aus Abschnitt "DER PROMPT" unten einfuegen
4. Nach der ersten Generation: Iterativ verfeinern (siehe Abschnitt "Iteratives Verfeinern")

### Variante B: Midjourney (falls GPT-4o nicht genuegt)

Den kompakten Midjourney-Prompt aus dem Appendix verwenden. ACHTUNG: Midjourney kann "HILF" nicht zuverlaessig rendern -- dieses Detail muss in Photopea nachbearbeitet werden.

---

## DER PROMPT (Englisch fuer GPT-4o / ChatGPT)

```
Children's book cover illustration in a modern, semi-realistic digital painting style with slight cartoon proportions. Painterly visible brushstrokes, rich textures, and cinematic lighting. The style should feel like a movie poster for a children's horror-adventure film for ages 10-12. NOT chibi, NOT manga, NOT flat-color cartoon, NOT photorealistic, NOT cute or childish.

IMPORTANT -- CAMERA ANGLE: The entire scene is viewed from a SLIGHTLY LOW ANGLE, looking UPWARD at the children and the building. This makes the children appear brave and heroic, and the building appear tall, imposing, and towering. The viewer is crouching on the cobblestones, looking up. This low perspective is critical for the dramatic effect.

COMPOSITION -- VERTICAL FORMAT (aspect ratio 2:3, portrait orientation):

The image has three clear depth layers:

═══════════════════════════════════════
FOREGROUND (bottom third)
═══════════════════════════════════════

Two children and a dog stand on old, wet cobblestones. They face AWAY from the viewer, looking UP at the building. Their backs and side profiles are visible, NOT their full faces. The wet cobblestones REFLECT the moonlight, creating a shimmering surface that adds depth.

LEFT CHILD -- NORA (girl, 12 years old):
- Slightly taller of the two
- Shoulder-length straight brown hair, tucked behind one ear
- Wearing a dark TEAL zip-up hoodie (#2a8a7a) -- this is the MOST SATURATED color on any character, making her visually "pop" against the dark background
- Dark jeans and sneakers
- One hand reaching toward the building entrance
- Posture: determined but tense, shoulders slightly raised, head tilted upward
- She is clearly the leader

RIGHT CHILD -- THEO (boy, 10 years old):
- Shorter than Nora by about a head
- Messy, slightly curly dark-blond hair
- Wearing an oversized OLIVE-GREEN BOMBER JACKET (military olive green -- NOT brown, NOT dark brown, NOT khaki -- clearly OLIVE GREEN)
- Dark cargo pants, worn-out sneakers
- One hand gripping backpack strap, other hand hanging with fingers slightly curled (nervous)
- Posture: curiosity mixed with fear, leaning slightly forward but body angled as if ready to run
- He stands half a step BEHIND Nora

BETWEEN AND SLIGHTLY IN FRONT OF THE CHILDREN -- SCHATTEN (the dog):
- Medium-sized mixed-breed dog with dark, almost black fur
- Striking, luminous AMBER-COLORED EYES (#d4920b) that glow faintly -- warm, like light reflecting from within, NOT laser-like or supernatural
- Sitting alert between the children, facing the building
- Ears pointed forward, hackles (fur along spine) slightly raised
- His glowing amber eyes are one of the MOST EYE-CATCHING elements of the entire cover

═══════════════════════════════════════
MIDDLE GROUND (center of the image) -- THE BUILDING
═══════════════════════════════════════

An old, tall, narrow 3-story German "Altbau" apartment building fills the center. This is Kirchgasse 14. The building TOWERS over the children (emphasized by the low camera angle).

Architectural style: Weathered plaster facade (once white, now grey-yellowish with age), tall narrow windows with dark wooden frames, decorative but crumbling cornices, arched stone entrance.

*** CRITICAL: THREE-ZONE LIGHTING ON THE BUILDING ***
The building has THREE distinct lighting zones from bottom to top. These MUST be clearly different from each other:

ZONE 1 -- GROUND FLOOR: All windows are DARK. No light. The arched entrance is visible.
The FRONT DOOR is SLIGHTLY AJAR, revealing PITCH DARKNESS inside. The gap between door and frame is visible and ominous -- something could be watching from inside.

ZONE 2 -- FIRST FLOOR (1. OG): Windows show WARM GOLDEN-AMBER LIGHT (#d4920b). This is the family's apartment -- a small island of safety and normalcy. The warm glow is contained and comforting, like a nightlight in a dark hallway.

ZONE 3 -- SECOND FLOOR (2. OG): This is the FOCAL POINT of the entire building. The windows emit a COLD, BLUISH-WHITE, EERIE GLOW (#c8dff5). This light is clearly UNNATURAL and completely DIFFERENT from the warm light below. It is pale, cold, and unsettling -- like moonlight coming from inside a room. This is Frau Silber's abandoned apartment.

*** CRITICAL: "HILF" IN WINDOW CONDENSATION ***
On ONE of the second-floor windows, visible in the condensation on the glass, a single word is written as if traced by a child's finger: "HILF" (four letters: H-I-L-F, German for "HELP"). The letters are:
- Slightly dripping downward (condensation running)
- Uneven, childlike handwriting (not neat, not printed)
- Visible but not immediately obvious -- a "discovery" element
- Lighter than the surrounding condensation (finger wiped away the moisture)
This detail is NON-NEGOTIABLE. It must be present in the image.

*** COLD FOG TENDRILS ***
Thin tendrils of pale, cold FOG or MIST (#c8dff5 at low opacity) seep out from:
1. Under the front door -- curling outward along the cobblestones toward the children
2. Around the cracks of the second-floor window frame -- curling DOWNWARD along the facade
The fog is cold and unnatural, clearly different from natural mist.

═══════════════════════════════════════
BACKGROUND (top third)
═══════════════════════════════════════

SKY: Deep dark gradient from dark navy blue (#1a1a3e) at the top to deep purple-indigo (#2d1b4e) at the rooftops. The sky in the UPPER CENTER should be relatively UNIFORM and DARK -- this area must remain clear for title text overlay. No clouds or detail in the center-top zone.

MOON: A large, pale full moon in the UPPER-LEFT area, partially obscured by thin wispy clouds. The moon casts cold, silvery light on the facade and creates long shadows on the cobblestones.

CITY SKYLINE: Behind and beside the main building, the SILHOUETTE of a large city skyline is faintly visible: church spires, old rooftops, chimneys, and a few taller modern buildings in the far distance. This is Gravenstedt -- an old city. The skyline is dark, almost black, with a few tiny warm-yellow lights in distant windows.

GHOSTLY SUGGESTIONS: Faintly -- almost imperceptibly -- in the fog above the rooftops, there is the BAREST suggestion of translucent shapes drifting. These are NOT clearly visible ghosts. They are slightly lighter areas in the mist, like faces or figures that MIGHT be there or MIGHT be just fog. This ambiguity is intentional. If someone sees them clearly, they are too visible -- reduce opacity. They should trigger "Wait... is that a face?" not "Look, a ghost."

═══════════════════════════════════════
LIGHTING
═══════════════════════════════════════

1. PRIMARY: Full moon (upper left) -- cold silver-blue light from above-left
2. SECONDARY: Eerie bluish-white glow from 2nd floor window -- cold light on facade below
3. TERTIARY: Warm amber from 1st floor window -- small, contained, comforting contrast
4. ACCENT: Schatten's amber eyes -- tiny warm light points in the dark foreground
5. REFLECTION: Wet cobblestones reflecting moonlight (shimmering, adds depth)

Overall: LOW and ATMOSPHERIC. Dark but NOT pitch black -- every element clearly visible. Think: "just after sunset, streetlights have gone out, only moonlight remains."

═══════════════════════════════════════
COLOR PALETTE
═══════════════════════════════════════

DOMINANT: Deep navy blue (#1a1a3e), dark indigo-purple (#2d1b4e), cool blue-grey (#3a4a6b)
ACCENT 1 (eerie): Cold bluish-white (#c8dff5) -- window glow, fog, moonlight
ACCENT 2 (warmth): Rich amber-gold (#d4920b) -- Schatten's eyes, 1st floor window
ACCENT 3 (pop): Muted teal-turquoise (#2a8a7a) -- ONLY on Nora's hoodie

ABSOLUTELY FORBIDDEN: bright red, neon green, hot pink, orange, any high-saturation warm colors. This is a moody, atmospheric, cool-toned image.

═══════════════════════════════════════
TEXT-FREE ZONES (for typography overlay)
═══════════════════════════════════════

These areas must be kept relatively FREE of detail:
- UPPER QUARTER of the sky (center): uniform dark area for series title + book title. Moon is offset LEFT.
- LOWER EDGE: cobblestones becoming darker/quieter at the very bottom for subtitle.

═══════════════════════════════════════
WHAT TO AVOID
═══════════════════════════════════════

- NO text, title, or lettering ANYWHERE except "HILF" in the window condensation
- NO clearly visible ghosts, monsters, skulls, blood, gore
- NO bright or happy colors
- NO cute or cartoonish proportions
- NO photorealistic rendering
- NO generic fantasy elements (dragons, wands, portals)
- NO daytime or sunset lighting
```

---

## ITERATIVES VERFEINERN

Nach der ersten Generation in ChatGPT: Pruefliste durchgehen und gezielt korrigieren.

### Runde 1 -- Komposition
Lade das generierte Bild erneut hoch und frage:
> Pruefe dieses Bild gegen meine Spezifikation. Ist der Kamerawinkel leicht von unten (die Kinder und das Gebaeude von unten betrachtet)? Falls nicht, generiere eine neue Version mit einem niedrigeren Kamerawinkel.

### Runde 2 -- Gebaeude-Beleuchtung
> Pruefe: Sind die drei Stockwerk-Zonen klar unterscheidbar? Erdgeschoss DUNKEL, 1. OG WARMES goldenes Licht, 2. OG KALTER blau-weisser unheimlicher Schein? Der Unterschied zwischen warm (1. OG) und kalt (2. OG) muss sofort auffallen. Falls nicht, korrigiere dies.

### Runde 3 -- Kritische Details
> Pruefe: (1) Ist "HILF" im Kondenswasser des 2. OG-Fensters sichtbar? (2) Ist Theos Jacke olivgruen (nicht braun)? (3) Ist die Haustuer leicht geoeffnet mit Dunkelheit dahinter? (4) Sind kalte Nebelranken aus der Tuer und dem 2. OG-Fenster sichtbar? Falls etwas fehlt, korrigiere es.

### Runde 4 -- Hintergrund
> Pruefe: (1) Ist eine Stadtskyline-Silhouette hinter dem Gebaeude sichtbar? (2) Gibt es ganz schwache, kaum erkennbare geisterhafte Andeutungen im Nebel ueber den Daechern? (3) Ist der obere Himmelsbereich (Mitte) frei genug fuer Textplatzierung? Falls etwas fehlt, ergaenze es.

### Runde 5 -- Feinschliff
> Pruefe: (1) Reflektieren die nassen Kopfsteine das Mondlicht? (2) Ist Noras Hoodie deutlich teal/tuerkis (#2a8a7a) und sticht als staerkster Farbpunkt heraus? (3) Leuchten Schattens Augen bernsteinfarben und warm? (4) Ist die Gesamtstimmung mysterioes und einladend -- "Ich will wissen, was da drin ist"?

---

## APPENDIX: MIDJOURNEY-PROMPT (v6.1 / v7)

Falls GPT-4o nicht die gewuenschte kuenstlerische Qualitaet liefert:

```
Children's book cover, semi-realistic digital painting, painterly brushstrokes, cinematic lighting, middle-grade horror-adventure, moody atmospheric night scene, slightly low camera angle looking upward --

Two children and a dark dog seen from behind on wet reflective cobblestones, facing a tall narrow 3-story German Altbau apartment building at night --

Girl 12 years in teal hoodie on the left reaching toward building, boy 10 years in olive-green bomber jacket on the right gripping backpack strap nervously, dark dog with glowing amber eyes sitting alert between them with raised hackles --

Building details: front door slightly ajar revealing pitch darkness inside, ground floor windows completely dark, first floor windows warm golden amber light, second floor windows cold eerie bluish-white unnatural glow with fog tendrils seeping from window cracks curling downward --

Background: full moon upper left casting silver-blue light, deep navy-purple sky gradient, faint city skyline silhouette with church spires behind building, barely perceptible ghostly shapes in fog above rooftops --

Color palette deep navy blue #1a1a3e dark indigo purple #2d1b4e cool blue grey #3a4a6b, accents cold bluish white #c8dff5 rich amber gold #d4920b muted teal #2a8a7a, no bright red no neon no pink no orange --

Upper sky area kept relatively uniform and clear for text overlay, lower cobblestones fading darker at bottom edge --ar 2:3 --style raw --s 250
```

**WICHTIG:** Bei Midjourney muss "HILF" im Fenster IMMER in Photopea nachbearbeitet werden (siehe Canva-Anleitung).

---

## APPENDIX: QUALITAETS-VERGLEICH v3 vs. v4-ZIEL

| Element | v3 (aktuell) | v4 (Ziel) |
|---------|-------------|-----------|
| Kamerawinkel | Augenhoehe | Leicht von unten (heroisch) |
| EG-Fenster | Teilweise beleuchtet | Komplett dunkel |
| 1.OG-Fenster | Warm (unklar) | Warm bernstein (Sicherheit) |
| 2.OG-Fenster | Warm (falsch!) | Kalt blau-weiss (unheimlich) |
| "HILF" | Fehlt | Sichtbar im Kondenswasser |
| Haustuer | Geschlossen/unklar | Leicht offen, Dunkelheit dahinter |
| Nebel | Allgemeine Atmosphaere | Gezielte Ranken aus Tuer + Fenster |
| Theos Jacke | Braun | Olivgruen |
| Stadtskyline | Fehlt | Silhouette hinter Gebaeude |
| Geister-Andeutungen | Fehlen | Kaum sichtbar im Nebel |
| Kopfsteine | Matt | Nass und reflektierend |
