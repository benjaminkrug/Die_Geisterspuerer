# Cover Vorderseite — Band 2 „Der Friedhof ohne Namen" — FINAL v2 (Ein-Prompt, Text im Bild)

> Ein einziger Prompt erzeugt die komplette Vorderseite inkl. aller Texte + CYOA-Badge.
> Für GPT-4o (Bildgenerierung) oder Nano Banana 2.
> **Vorschalt-Satz beim Einfügen:**
> *„Generate a single children's book cover illustration in portrait orientation. Render ALL the
> specified text lines exactly as written, spelled letter-for-letter, large and legible — the typography
> and the corner badge are part of the illustration, not an overlay. Prioritise a bold, high-contrast
> composition that still reads clearly as a tiny thumbnail."*

---

## DESIGN-PRINZIPIEN (warum das Cover so gebaut ist)

| Prinzip | Umsetzung |
|--------|-----------|
| **EIN dominantes Motiv** | Das aufragende Friedhofstor + der sich weigernde Hund mit Leucht-Augen. Alles andere ordnet sich klar unter (kein visuelles Gedränge → Thumbnail-tauglich). |
| **USP + Alter sofort sichtbar** | ZWEI Eck-Badges: oben rechts „12 ENDEN – DU WÄHLST" (interaktiv + Spielwert, der Haupt-Hook), oben links „AB 10 JAHREN" (Zielgruppe). Jedes Badge sagt etwas ANDERES — keine Doppelung. |
| **Kein Untertitel** | Bewusst weggelassen (sagte dasselbe wie das interaktiv-Badge). Der Platz geht an einen größeren Titel. |
| **Extra großer Titel** | Haupttitel ~45–55 % der Bildhöhe, dominantestes Element. |
| **Kontrast als Mechanik** | Heller Nebel-Bereich HINTER dem Titel, damit die hellen Buchstaben auf Dunkel knallen; Silhouetten tiefschwarz; nur EIN warmer Akzent (Hundeaugen). |
| **Reihen-DNA (Band 1)** | 2 Kinder + Hund von hinten, aufragender Ort, kalter Leucht-Eyecatcher, Weggabelung, „Lockwood & Co. meets Goosebumps". |
| **Differenzierung B1** | Farbwelt Waldgrün/Schwarz statt Indigo/Lila. |

---

## DER PROMPT

```
A single children's book cover illustration, PORTRAIT orientation, tall aspect ratio 1600 x 2560, 300 DPI, for a German middle-grade spooky-adventure series for ages 10–12. Painterly digital illustration with rich texture and cinematic lighting, slightly stylized. NOT photorealistic, NOT manga, NOT anime, NOT chibi, NOT flat vector cartoon, NOT cute/babyish. Overall mood: genuinely spooky but SAFE and inviting — a delicious shiver, never gory, never bloody, never violent, no jump-scare faces. Reference feel: "Lockwood & Co." UK cover art meets classic "Goosebumps" colour punch.

━━━━━━━━ THE ONE BIG FOCAL MOTIF ━━━━━━━━
Keep the composition BOLD and SIMPLE so it reads at 150 px thumbnail size. There is ONE hero motif: a huge, old wrought-iron cemetery GATE seen from a LOW angle looking UPWARD, towering and imposing, half-open in the centre, black paint peeling, pointed rusted finials against the night sky. Directly in front of it, small but central, the three heroes seen FROM BEHIND (no faces). Everything else (stones, fog, distant ghost) is secondary background — do NOT let it clutter the silhouette.

━━━━━━━━ THE THREE HEROES (foreground, lower-centre, backs to viewer) ━━━━━━━━
- NORA (left): a 12-year-old girl, shoulder-length tousled dark hair, FOREST-GREEN zip hoodie, small backpack, standing braced, half-turned toward the gate.
- THEO (right): her 10-year-old brother, a little shorter, messy dark hair, CHARCOAL-GREY jacket, hanging slightly back, nervous posture.
- SCHATTEN (centre, between them): a thin, medium-sized BLACK dog with pointed upright ears, sitting braced and clearly REFUSING to enter — his BODY faces AWAY from us toward the gate (we see his back and haunches), but he has turned his HEAD back OVER HIS SHOULDER to look directly BACK at the viewer/camera. His FULL FACE (muzzle, snout, both eyes) is clearly visible, twisted around toward us in a natural over-the-shoulder head-turn (like a dog glancing back at its owner). The two AMBER EYES GLOW warm amber-gold (#e0a020) and look straight into the camera — placed correctly in his forward-facing FACE (never on the back of his head). This glowing gaze is the single brightest, warmest point in the whole image and the eye-catcher. His front legs are stiff and braced against a TAUT leash pulling toward the gate.

━━━━━━━━ BACKGROUND (secondary, must stay subordinate) ━━━━━━━━
Beyond the gate bars: rows of small, crooked, moss-covered BLANK nameless gravestones dissolving into cold fog and dense dark chestnut trees. Thin fog tendrils seep between the bars. FAR back between two stones, a very faint, translucent GREY stooped ghostly figure — kept subtle and sad, NOT a scary face, easy to miss (atmospheric bonus, not a focal point). Wet cobblestones in the foreground; the path SPLITS into a subtle Y-shaped FORK (one branch to the gate, one curving into darkness) — the "you choose your path" cue.

━━━━━━━━ COLOUR, LIGHT & CONTRAST (make it POP) ━━━━━━━━
Palette: deep forest green (#0f2417), near-black silhouettes, cold slate-grey fog, misty grey-green. Cold pale moonlight from the upper left. STRONG, punchy contrast — this is important:
- Render a band of LIGHTER, luminous grey-green fog/moon-glow in the upper-middle sky BEHIND the title area, so the pale title letters sit on a lighter halo and stand out hard.
- Push the gate, trees and children to near-BLACK silhouette for maximum contrast against that glow.
- The ONLY warm colour anywhere is the dog's glowing amber eyes (and a tiny amber glint on the wet stones). Everything else stays cold green/grey. This colour restraint makes the eyes and the title pop.
Do NOT make the image a uniform flat dark — it must have clear bright-to-black contrast so it survives thumbnail scaling.

━━━━━━━━ TYPOGRAPHY — render exactly, EXTRA LARGE, part of the art ━━━━━━━━
Elegant slightly-gothic serif display face, bone-white / pale bone-grey with a subtle carved-stone texture and a soft dark drop-shadow/outline so every letter is crisp against the background. Centre-aligned. Spell every line EXACTLY, letter-for-letter, including the German umlaut Ü. Do not translate, duplicate, misspell, or add any other words. There is NO subtitle line — keep the title area clean and let the title dominate.

1. SERIES LINE — very top, small caps, letter-spaced, medium size:
   DIE GEISTERSPÜRER
2. MAIN TITLE — the absolutely DOMINANT element, render it EXTRA LARGE and bold, filling roughly 45–55% of the image height across the upper half, stacked on two lines, edge-to-edge wide and unmistakably the biggest thing on the cover:
   DER FRIEDHOF
   OHNE NAMEN
3. BAND TAG — just beneath the title, small and understated: BAND 2
4. AUTHOR — very bottom, small caps: BENJAMIN KRUG
(No other text lines. Especially NO subtitle such as "Ein interaktives Grusel-Abenteuer" — that message is carried by the badge instead, so it must NOT appear as a subtitle.)

━━━━━━━━ TWO CORNER BADGES (top corners — the selling points) ━━━━━━━━
Two bold, high-contrast badges, one in each TOP corner, sitting in the corners so they do NOT overlap or crowd the big title. Both must be clearly legible even at thumbnail size and must NOT touch each other or the title. Use a warm bone/parchment badge with dark lettering (or a dark seal with bone lettering) so they pop against the dark sky.

- UPPER-LEFT badge — a small round seal/stamp, spelled EXACTLY, only these words on it:
  AB 10 JAHREN
- UPPER-RIGHT badge — a bold round seal or short torn banner, a bit larger and punchier (this is the main hook), spelled EXACTLY, only these words on it:
  12 ENDEN – DU WÄHLST
(Keep each badge to exactly the words listed, nothing more. Short, bold, readable. The right badge is the eye-catching one.)

━━━━━━━━ HARD RULES ━━━━━━━━
- The ONLY text anywhere in the whole image is: the title block lines (DIE GEISTERSPÜRER / DER FRIEDHOF / OHNE NAMEN / BAND 2 / BENJAMIN KRUG) PLUS the two badges (AB 10 JAHREN) and (12 ENDEN – DU WÄHLST). Absolutely NO other words, NO subtitle, NO gibberish letters, NO text on the gravestones (they are BLANK), NO watermark, NO signature.
- Children shown from BEHIND, no visible faces.
- No blood, gore, skulls, monsters, weapons, grinning ghost faces.
- The dog's amber glowing eyes = brightest point; the title = large and legible; strong contrast overall.
- DOG HEAD: the glowing eyes must be on his real FACE, which is turned back over his shoulder toward the camera. Do NOT put eyes on the back of his head; do NOT show a faceless back-of-head with glowing dots. Body away, head turned back, face and both eyes visible.
- Must read clearly and look striking at 150 px width: bold gate+dog silhouette, big readable title, punchy badge.
```

---

## CHECKLISTE NACH GENERIERUNG

- [ ] Titel EXTRA groß, 2 Zeilen, dominantestes Element, klar lesbar auf hellem Nebel-Halo?
- [ ] KEIN Untertitel mehr im Bild?
- [ ] Kontrast stark (helle Titel-Zone vs. tiefschwarze Silhouetten) — funktioniert das Thumbnail?
- [ ] Badge oben rechts „12 ENDEN – DU WÄHLST" auffällig + korrekt geschrieben?
- [ ] Badge oben links „AB 10 JAHREN" korrekt + lesbar, ohne den Titel zu bedrängen?
- [ ] Beide Badges in den Ecken, berühren sich/den Titel NICHT?
- [ ] Titelzeilen korrekt (GEISTERSPÜRER mit Ü, FRIEDHOF, WÄHLST mit Ä)?
- [ ] KEIN sonstiger/verdrehter Text, keine Buchstaben auf Grabsteinen?
- [ ] Waldgrün/Schwarz-Palette, nur die Hundeaugen warm (klar anders als Band 1)?
- [ ] 2 Kinder von hinten + Hund; Schatten weigert sich, Leine straff?
- [ ] Schattens Augen leuchten amber = hellster Punkt?
- [ ] Hund: Körper weg, KOPF über die Schulter zur Kamera gedreht — Gesicht + beide Augen im GESICHT sichtbar (NICHT am Hinterkopf)?
- [ ] Tor dominant, leichte Untersicht; Steine/Nebel/Geist bleiben untergeordnet?
- [ ] Weggabelung (CYOA-Cue) im Vordergrund erkennbar?
- [ ] Bei 150 px Breite: Motiv + Titel + Badge noch klar erkennbar?

## FALLS TEXT MISSLINGT
Häufigstes Problem = langer Haupttitel oder Badge verdreht. Vorgehen:
1. 2–3 Neuversuche.
2. Wenn nur der Titel klappt und das Badge nicht (oder umgekehrt): den funktionierenden Teil behalten, den anderen im Prompt isoliert betonen (z. B. „the badge must clearly read DU ENTSCHEIDEST! in two words").
3. Notfalls Bild ohne Text/Badge generieren und beides in Canva sauber setzen
   (Schriftvorlage: Band1/Cover/Canva_Typografie_Anleitung.md).
