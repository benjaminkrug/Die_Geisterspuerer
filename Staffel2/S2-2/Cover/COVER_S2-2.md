# Cover — S2-2 „Die Uhr, die rückwärts läuft"

> **Basis:** [`Dokumentation/Cover_Reihenstandard.md`](../../../Dokumentation/Cover_Reihenstandard.md)
> (Panel-Maße, Prompt-Blöcke A–E, Figuren-Grammatik) und
> [`Staffel2/PLAN_Staffel2.md`](../../PLAN_Staffel2.md) Abschnitt 10 (Staffel-2-Abweichungen,
> S2-2-Farbwelt). Nichts davon wird neu erfunden — dieses Blatt ergänzt nur das, was erst nach
> dem **fertigen Manuskript** entschieden werden konnte. Struktur 1:1 von
> [`S2-1/Cover/COVER_S2-1.md`](../../S2-1/Cover/COVER_S2-1.md) übernommen.
>
> ⚠️ **Kein Bild erzeugt.** Dieses Blatt ist die vollständige Arbeitsvorlage (Motiv, Prompts,
> Zonen, Prüfliste) — Bildgenerierung ist ein bewusst separater, expliziter nächster Schritt.
>
> ⚠️ **Rückseiten-Prompt fehlt noch — und zwar absichtlich.** Er braucht den echten
> KDP-Klappentext wörtlich (siehe S2-1-Vorlage, Abschnitt 4). Für S2-2 existiert noch kein
> `KDP_S2-2.md` — die Beschreibung wurde in dieser Sitzung bewusst noch nicht geschrieben. Ein
> Rückseiten-Prompt mit erfundenem oder vorweggenommenem Klappentext wäre genau der Fehler, den
> `Kontinuitaet_S2-1.md`s A3-Lehre und die Memory-Notiz „Verkaufstexte nie geprüft" beide
> beschreiben. **Erst KDP_S2-2.md schreiben (wörtlich gegen das Manuskript geprüft), dann
> Abschnitt 4 hier ergänzen.**

---

## 0. ★ Visueller Abgleich mit dem echten S2-1-Cover (nachgeholt)

Der erste Entwurf dieses Blatts stützte sich nur auf `COVER_S2-1.md` (Text), nicht auf die
tatsächlich fertigen Bilder `Staffel2/S2-1/Cover/vorderseite.png` / `rueckseite.png`. Beim
Ansehen der echten Bilder vier Funde, alle unten in Abschnitt 3 eingearbeitet:

1. **🔴 Physikalisch unmögliche Anweisung korrigiert.** Der erste Entwurf verlangte Uhrzeiger,
   die „visibly moving backwards" sind — ein Standbild kann Bewegungsrichtung nicht zeigen,
   eine rückwärtslaufende Uhr sieht in einem Einzelbild identisch aus wie eine normale. Ersetzt
   durch eine Zeigerstellung, die eindeutig falsch/unmöglich aussieht (z. B. beide Zeiger auf
   derselben Seite über 12 hinaus), statt Bewegung zu behaupten.
2. **🟠 Farbverlust durch Dunkelheit.** Auf dem echten S2-1-Bild sind Noras Teal-Hoodie und
   Theos Oliv-Jacke kaum von Schwarz zu unterscheiden — das Bild ist insgesamt sehr dunkel,
   obwohl der Prompt „never black and never harsh" verlangte. Für S2-2 ergänzt: eine explizite
   Gegenprobe, dass beide Farben sichtbar gesättigt bleiben müssen, nicht in Schwarz absaufen.
3. **✅ Stilfrage offen gelegt, jetzt vom Autor entschieden (2026-09-02).** Herbert auf dem
   S2-1-Cover ist eine solide, klar umrissene dunkle Gestalt (nur von hinten, im Dunkeln) —
   nicht wörtlich „verschwommen/nebelhaft". Zur Wahl standen: derselbe solide Stil (Konsistenz
   mit S2-1) oder ein durchscheinender Nebel-Umriss (näher an K6s Wortlaut „schmal und
   verschwommen"). **Entscheidung: nebelhaft-durchscheinend**, bewusst als sichtbarer
   Stilwechsel zwischen den Covern — jeder Geist der Reihe darf seine eigene, textlich
   begründete Erscheinungsweise bekommen, statt einer starren Cover-Technik zu folgen.
4. **🟢 Szenen-Komplexität reduziert.** Der erste Entwurf hatte mehr gleichzeitige Einzel-
   Anforderungen (Schlösser + mehrere Uhren + eine rückwärtslaufende + verstreute Lichtpunkte
   + Gestalt) als S2-1s vergleichsweise einfache Tür-Schrank-Gestalt-Komposition. Jede
   zusätzliche Anforderung ist ein zusätzliches Risiko für das Bildmodell. Reduziert auf
   weniger, klarere Einzelteile (s. u.).

5. **🔴 KDP-ABLEHNUNG WEGEN UNLESBARER SCHRIFT (nachgetragen 2026-09-03).** Die erzeugte und
   hochgeladene Vorderseite wurde von KDP beanstandet: *„Text … schwer lesbar, verschwimmt mit
   dem Hintergrund oder wird von anderen Elementen verdeckt."* Analyse der Datei
   `vorderseite.png`:
   - Der **Untertitel** („Ein Grusel-Abenteuer für Kinder ab 12 Jahren") sitzt direkt über dem
     beleuchteten Oberfenster und dem hellen Uhrenkopf — **hellgrau auf hellgrau**. Die
     Buchstaben lösen sich in den Fenstersprossen auf.
   - Die **zweite Titelzeile** („rückwärts läuft") überlappt rechts die beleuchtete Wand neben
     der Uhr — Gold verliert dort den Kontrast.
   - **Ursache ist nicht die Schriftfarbe.** Die Layout-Karte verlangte 0–38 % „calm, dark",
     die Szene-Beschreibung aber „the ONLY light … through a row of grimy, **high overhead**
     windows". *Hoch* + *overhead* zieht das hellste Objekt des Bildes nach oben in die
     Textzone. Die eine Regel, die die Textzone dunkel halten sollte, wurde von der Szene
     widerlegt.
   - **Fix:** neuer Pflichtblock **F** in `Cover_Reihenstandard.md` (Lesbarkeit/Kontrast),
     hier in Abschnitt 3 und 4 eingearbeitet: Lichtquelle strikt ins mittlere Drittel
     (44–62 %), obere 44 % + untere 14 % nahezu schwarz, Abdunkel-Scrim unter dem Text,
     hellgrau `#9aa6b0` → `#c8d0d8` angehoben, dünne dunkle Kontur an jeder Zeile,
     Graustufen-Gegenprobe in der Prüfliste. **Beide Bilder müssen neu erzeugt werden.**

**Nicht als Problem eingestuft:** Das S2-1-Bild ist insgesamt sehr dunkel (Graphit/Schiefer-
Palette), was zur kalten Farbwelt des Bandes passt. S2-2s Farbwelt (gedämpftes Messing/Kupfer)
ist von Natur aus wärmer — das dürfte demselben Über-Verdunklungs-Trend der Bildmodelle
entgegenwirken, wird aber trotzdem im Prompt explizit verankert (Punkt 2 oben), statt sich
darauf zu verlassen.

---

## 1. Das Motiv — aus dem Manuskript, nicht erfunden

Der Staffelplan legt für S2-2 fest (Abschnitt 10): *„Uhrmacher-/Schlosserwerkstatt … gedämpftes
Messing/Kupfer … Bernstein + viele kleine kalte Lichtpunkte."* Das war die Vorgabe **vor** dem
fertigen Manuskript. Jetzt existiert das Buch, und **Kapitel 4 und Kapitel 6 zusammen** liefern
eine Komposition, die alle acht Regeln der Reihen-Grammatik erfüllt, ohne dass etwas
dazuerfunden werden müsste:

> Dahinter lag ein weiter, hoher Raum, kaum beleuchtet. Nur graues Licht fiel durch die
> schmutzigen Oberfenster.
>
> Regale, so weit man sehen konnte. Nicht mit Büchern. Mit Schlössern. […] An den Wänden
> dazwischen: Uhren. […] Eine, ganz in der Nähe der Tür, drehte sich sichtbar rückwärts.
> (K4)
>
> Eine Gestalt, schmal und verschwommen, stand zwischen zwei Regalen, halb hinter einem
> Ständer voller Schlösser verborgen. Kein Gesicht, das man hätte erkennen können. Nur
> Umrisse, die manchmal schärfer wurden und manchmal fast verschwanden. (K6)

| Regel der Reihen-Grammatik | Wie K4/K6 sie erfüllen |
|---|---|
| 1 Zwei Kinder + Hund von hinten, unteres Drittel | sie stehen im Gang zwischen den Regalreihen |
| 2 Sie blicken **in eine Öffnung** hinein | den Gang hinunter, in die Tiefe des Raums, wo die Gestalt steht |
| 3 Genau **eine** Lichtquelle in der Bildmitte | das graue Licht der schmutzigen Oberfenster, das auf die Gestalt fällt |
| 4 Schattens Auge als einziger lebendiger Punkt | er steht angespannt neben ihnen, den Blick auf die Gestalt gerichtet |
| 5 Oberes Drittel ruhig | dunkle Regaloberkanten, verschwommen im Halbdunkel |
| 6 **Nie ein klar erkennbarer Geist** | Grete steht „schmal und verschwommen … kein Gesicht" — im Buch selbst schon unscharf, nicht kaschiert |
| 7 Kein Blut, keine Fratze | eine müde, verschwommene Frauengestalt |
| 8 Alles führt zur Bildmitte | Regalgang → Gestalt → das eine Fenster-Licht |

**Der Titelbezug sitzt im Bild selbst:** die rückwärtslaufende Uhr aus K4 kann als kleines,
konkretes Detail nahe der Gestalt erscheinen — ein Zifferblatt, dessen Zeiger sichtbar falsch
herum stehen. Kein erfundenes Symbol, sondern eine Zeile aus dem Buch.

### Warum das nicht mit S2-1 kollidiert

S2-1 zeigt eine **einzelne** Tür mit **einem** Lichtspalt in einer Wohnung. S2-2 zeigt einen
**offenen, tiefen Raum** voller Regale — der Größenunterschied selbst ist die Pointe des
Bandes (ein Sammel-Knoten statt eines Einzelfalls) und trägt auch im Thumbnail:

| | S2-1 | S2-2 |
|---|---|---|
| Raum | schmaler Flur, eine Tür | weiter, hoher Lagerraum, viele Regalreihen |
| Licht | ein schmaler, kalter Spalt | diffuses graues Fensterlicht, weiter verteilt |
| Wiederkehrendes Detail | ein Schloss (Einzahl) | Dutzende Schlösser + Uhren (Menge) |
| Grundton | Graphit/Schiefer | **gedämpftes Messing/Kupfer** |

### Die Staffel-Signatur: viele kalte Lichtpunkte statt eines Fadens

S2-1 trägt einen einzelnen Leine-Lichtfaden (Halders Bindungssignatur an einem Geist). S2-2
zeigt laut Staffelplan bewusst **viele kleine kalte Lichtpunkte** statt eines einzelnen Fadens —
konsequent für ein Buch, in dem nicht ein Geist, sondern ein ganzer Raum voller Geister
gebunden ist. Praktisch: ein feines, kaltes Glitzern auf den Metallflächen der Schlösser und
Uhrengehäuser im Halbdunkel, verstreut statt linear. Blass, nie dominant — die Akzentfarbe
bleibt Bernstein (Schattens Auge).

---

## 2. Technische Eckdaten

| | Wert |
|---|---|
| Format | **6 × 9 Zoll**, weißes Papier (Staffel-2-Standard) |
| Seitenzahl | **82** — **real gemessen** am gebauten `Output/S2-2/KDP_S2-2_Manuskript.pdf` (nicht geschätzt, anders als S2-1 an diesem Punkt) |
| Buchrücken bei 82 S. | 82 × 0,002252 Zoll = 0,1847 Zoll = **4,69 mm** |
| Vollcover bei 82 S. | 12,435 × 9,250 Zoll ≈ **3730 × 2775 px** @ 300 dpi |
| Vorderseite allein | mindestens **1838 × 2775 px** |

> ⚠️ **Trotzdem vor dem echten Cover-Build neu prüfen.** Die Seitenzahl ändert sich, sobald
> Widmung/Epigraph eingefügt werden (S2-1 hat mit Frontmatter mehr Seiten als ohne) — dieser
> Wert gilt für den Taschenbuch-Build **ohne** Widmung/Epigraph (Stand dieser Sitzung). Nach
> Freigabe von Widmung/Epigraph: neu bauen, Seitenzahl neu ablesen, `PAGES` im Cover-Skript
> erst dann setzen.
>
> **02.09.2026 nachgetragen:** Ursprünglich waren es 78 Seiten — unter KDPs harter Grenze
> von 79 Seiten, unter der überhaupt kein Rückentext gedruckt wird. Manuskript deshalb um
> 6 Kapitel / +1.055 Wörter erweitert (Details: `Kontinuitaet_S2-2.md`, Abschnitt
> „Seitenzahl-Erweiterung"). Bei jetzt 82 Seiten druckt der Rücken Text, aber nur bei
> 2,9–3,4 pt („kaum lesbar" laut Skript-eigener Warnung) — echte Lesbarkeit (wie beim
> schmalsten bisherigen Vergleichsband, Band 4 mit 95–97 Seiten) hätte nochmal +2.100–2.500
> Wörter gebraucht. Nutzer-Entscheidung: bei 82 Seiten belassen, kein weiterer Ausbau.

### Zonen (identisch zu S2-1 — Staffel-2-Standard)

```
  0 – 44 %   Kopfbereich  — NAHEZU SCHWARZ, vier Textebenen, KEIN Licht, kein Fenster
 44 – 62 %   Mittelzone   — Regalgang, Gestalt, das eine Fensterlicht (hier, nicht höher)
 62 – 70 %   Übergang
 70 – 100 %  Figurenzone  — Nora, Theo, Schatten von hinten; unterste 13 % nahezu schwarz
```

Sicherheitsränder oben/unten: **13 %** (Staffel-2-Standard). Seitlich zentrale 84 % der Breite.

★ **Das Fensterlicht ist die einzige Lichtquelle und liegt tief** — als niedriges Fensterband
auf Uhrenhöhe (46–62 %), **nicht** hoch unter der Decke. Die oberen 44 % und die unteren 13 %
sind der dunkelste Teil des Bildes. Grund: Block F in `Cover_Reihenstandard.md` und der
KDP-Ablehnungsbefund in Abschnitt 0, Punkt 5.

### Die fünf Textzeilen

```
DIE GEISTERSPÜRER                              klein, helles Stahlgrau #c8d0d8 (fast weiß)
DIE GEBUNDENEN · BAND 2                        1,6–1,8× Zeile 1, #c8d0d8
Die Uhr, die rückwärts läuft                   groß, warmes Creme-Weiß #efe7d3, dominant
Ein Grusel-Abenteuer für Kinder ab 12 Jahren   klein, #c8d0d8
Benjamin Krug                                  klein, #c8d0d8
```

★ **KDP hat 3× wegen „Text verschwimmt" abgelehnt.** Ursache: (1) antikisierte, rissige
Schrift, (2) Gold als Mittelton. Deshalb ab jetzt: **Titel in Creme-Weiß statt Gold**
(eindeutig hell auf dunkel, wie KDPs Lösungstext verlangt), und **jede** Schriftzeile
**sauber, voll gefüllt, scharfkantig — keine verwitterte / abgeblätterte / rissige /
gehämmerte Textur**. Gold/Bernstein nur noch für Schattens Auge.

Jede Zeile steht auf **Nahezu-Schwarz**, mit dünner dunkler Kontur/Schattenkante. Kein
Buchstabe berührt Fenster, Lichtkante, Regalkante, Figur oder Geist. Farbe wird nie
abgedunkelt, um einen zu hellen Fleck zu kaschieren — stattdessen der Hintergrund.

⚠️ **„ab 12 Jahren"**, nicht 10.
⚠️ Umlautkontrolle Buchstabe für Buchstabe: **GEISTERSPÜRER** (Ü), **für** (ü),
**rückwärts** (ü).

---

## 3. Prompt Vorderseite

```
========================================
READ THIS BLOCK FIRST - IT OVERRIDES ANY EARLIER CONTEXT
========================================

This cover belongs to the German children's series "DIE GEISTERSPÜRER"
(The Ghost Trackers). This is the SECOND book of its SECOND cycle, which
carries the additional series name "DIE GEBUNDENEN". It is NOT "Die
Herrenhaus-Detektive" and NOT any other series. Ignore any other book
series, title, manor house or branding from earlier in this conversation.

EXACTLY these five texts appear on the cover - no others, none invented:
  1. tiny series line : DIE GEISTERSPÜRER
  2. cycle line       : DIE GEBUNDENEN · BAND 2
  3. main title       : Die Uhr, die rückwärts läuft
  4. subtitle         : Ein Grusel-Abenteuer für Kinder ab 12 Jahren
  5. author            : Benjamin Krug

Line 2 is 1.6-1.8 times the cap height of line 1. Line 3 is by far the
largest and most dominant text on the cover, in BRIGHT WARM CREAM / bone
white (#efe7d3) - clean light-on-dark, NOT gold, NOT a mid-tone. Lines 1, 2
and 4 are PALE steel grey (#c8d0d8), close to white. The only gold/amber on
the whole cover is the dog's eye.

★ LETTERING QUALITY - this is why the previous versions were REJECTED by the
print service ("text blends into the background"):
Every letter of every line is CLEAN, SOLID, SHARP-EDGED and EVENLY FILLED,
like fresh crisp printing or clean digital type. Absolutely NO distressed,
weathered, antiqued, eroded, cracked, scratched, grungy, "vintage-worn" or
textured lettering. No broken strokes, no gaps inside letters, no flaking,
no rough or crumbling edges, no metal-hammered texture. A reader must be
able to read every line instantly at thumbnail size. Plain, bold, legible.

REQUIRED IN THE IMAGE - non-negotiable, this is the series signature:
TWO CHILDREN AND A DOG, seen FROM BEHIND, in the lower third, looking down
the aisle. Girl in dark teal hoodie, boy in olive-green jacket, dark shaggy
dog between them with ONE glowing amber eye. If they are missing, the cover
is wrong. (Full detail in THE THREE FIGURES below.)

The blurred ghost is a small extra, far back and off to one side - never a
substitute for the three, never centre stage. She is a faint smudge of fog
with NO FACE at all (no eyes, no sockets, no mouth, nothing skull-like) and
is not scary. This is a book for 12-year-olds: a shiver, never a nightmare.
A ghost with a visible or gaunt face makes the cover unusable.

Forbidden anywhere: any publisher name, imprint or logo; any badge, seal,
sticker, ribbon, banner or emblem; any age roundel; any painted frame or
border around the artwork; any word not in the five texts above.
========================================

════════════════════════════════════════
TEXT-BACKGROUND CONTRAST - READ BEFORE THE LAYOUT
The print service REJECTED this cover THREE TIMES for text that "blends into
the background". The likely causes: distressed/textured lettering (see
LETTERING QUALITY above) and a mid-tone gold title. Both are fixed now:
clean solid letters, cream-white title. These rules override any wish:
════════════════════════════════════════

0. ALL LETTERING IS CLEAN AND SOLID - no distressed / weathered / eroded /
   cracked / textured type anywhere (full rule above). This is rule zero.

1. EVERY line of text sits on a NEAR-BLACK background - the darkest tone in
   the whole image, no brighter than a very deep charcoal. Imagine the
   finished cover turned to greyscale: every letter must be obviously far
   lighter than everything it touches.

2. THE LIGHT SOURCE STAYS OUT OF THE TEXT ZONES. The single light source
   (the grimy windows at the far end) sits in the MIDDLE THIRD of the height,
   between 46 and 62. It NEVER rises above 44. The whole top 44% of the image
   and the bottom 14% are the darkest parts of the picture: plain, near-black,
   out of focus. No window, no lit edge, no glow, no bright shelf rim, no
   reflection reaches into them.

3. A DARKENING SCRIM UNDER THE TYPE. The illustration fades to almost solid
   near-black across the top (0 to 44) and again across the bottom (82 to
   100). This is a smooth part of the painting - deep shadow that happens to
   sit exactly where the text goes - NOT a drawn box, bar or rectangle.

4. TEXT COLOUR IS CLEAN LIGHT-ON-DARK. Title = bright warm cream / bone white
   (#efe7d3). Series line, cycle line, subtitle, author = pale steel grey
   (#c8d0d8), close to white. NO gold, NO amber, NO mid-tone anywhere in the
   text - KDP's contrast check wants unambiguous light-on-dark. If the area
   behind a line is not near-black, the BACKGROUND is wrong, not the text -
   darken the background there. Never dim, recolour or shrink-to-hide text.

5. A THIN SAFETY OUTLINE. Every line of text carries a soft, narrow dark halo
   (a subtle near-black drop shadow / thin outline), just enough to hold its
   edge if a faint highlight ever drifts behind a letter. Keep it subtle -
   cleanly printed, not stickered and not glowing.

6. NOTHING CROSSES THE TEXT. No letter overlaps a window, a lit edge, a
   bright reflection, a shelf edge, a figure, or the blurred figure. Between
   any illustration detail and any letter there is clear near-black space.

════════════════════════════════════════
LAYOUT MAP - WHERE EACH LINE SITS
════════════════════════════════════════

Think of the image height as 100 units, top = 0, bottom = 100.

  0 - 13   EMPTY BAND. Near-black. Plain out-of-focus dark shelving in deep
           shadow. NO text of any kind here.
 14 - 17   ZONE 1  series line   DIE GEISTERSPÜRER          (near-black behind)
 18 - 23   ZONE 2  cycle line    DIE GEBUNDENEN · BAND 2    (near-black behind)
 25 - 35   ZONE 3  main title    Die Uhr, die rückwärts läuft  (near-black behind BOTH lines)
 37 - 41   ZONE 4  subtitle      Ein Grusel-Abenteuer für Kinder ab 12 Jahren  (near-black behind)
 44 - 78   THE SCENE - windows, clock, blurred figure, aisle. No text.
 80 - 86   ZONE 5  author        Benjamin Krug             (calm near-black floor behind)
 87 - 100  EMPTY BAND. Plain near-black floor. NO text of any kind here.

THE TWO EMPTY BANDS AND THE NEAR-BLACK TEXT ZONE (0 TO 44) ARE THE MOST
IMPORTANT PART OF THIS LAYOUT. The whole upper 44% is quiet, dark and almost
featureless so that all four upper lines read cleanly. The visible part of
the scene begins BELOW that, at about 44 to 46.

Above the first line of text there must be a clearly visible strip of plain
near-black background, at least TWICE AS TALL as the capital letters of that
line. Below the author's name there must be an equally visible strip of plain
near-black floor, at least TWICE AS TALL as the letters of the author's name.

If you cannot fit everything, make the TEXT SMALLER. Never move it outwards,
and never move it down into the lit scene. A slightly smaller title with
generous empty near-black margins is correct. A large title that reaches
towards an edge, or down onto the windows, is wrong and unusable.

SIDE MARGINS: every line of text sits inside the central 84% of the width.
To the left of the leftmost letter and to the right of the rightmost letter
of EVERY line there must be visible empty background at least as wide as two
capital letters.

The outer edges of this image are trimmed off when the book is printed, and
the e-book thumbnail is cropped narrower still. Anything close to an edge
will be lost. The ILLUSTRATION still fills the whole image to all four edges -
only the TEXT stays inside the safe area.

ZONE 5 NOTE: the composition must leave a calm, dark patch of floor in the
centre at that height, so the author's name reads clearly against it.

════════════════════════════════════════
THE SCENE - a long, high storage room inside an old clockmaker's and
locksmith's workshop, at dusk. The scene occupies ONLY the lower 56% of the
image (from about 44 downward). Everything above 44 is deep near-black
shadow - see the contrast rules and the layout map.
════════════════════════════════════════

We are looking down a narrow aisle between two very tall shelving units,
from behind three figures. The shelves stretch back into shadow, packed
with small dark padlocks of many shapes and sizes - dozens of them,
suggested rather than individually detailed, not each one picked out. The
TOP of the shelving, above about 44, is lost in near-black shadow and
completely out of focus - no rim light, no catch-light on the shelf edges
up there.

On the wall at the deep end of the aisle, centred, hangs ONE large standing
clock, clearly visible, its face at about 50 to 60 of the height. Its two
hands both point to positions past the 12, close together, an angle a
working clock would never show - a single wrong, impossible instant frozen
in place. Do not attempt to depict motion or a direction of movement; show
only this one still, wrong clock face.

The ONLY light in the picture is a row of grimy windows at the far end of
the aisle, set LOW - a narrow clerestory band roughly level with the clock,
between 46 and 62 of the height, NOT high up under the ceiling. Through them
falls a soft, cold, grey daylight, diffuse rather than a single beam,
lighting the deep end of the room and fading before it reaches the figures.
The wall ABOVE the windows is dark and unlit. No part of this light, and no
glow from it, reaches above 44.

Roughly two-thirds of the way back into the scene, OFF-CENTRE (not framed
by the window), half-hidden behind a shelf of locks: a THIN, BLURRED FEMALE
FIGURE. She is barely there - little more than a paler smudge of fog in the
grey light, the vague shape of a woman in a long dress, her edges dissolving
into the air around her. You could almost miss her.
[✅ Stilentscheidung bestätigt (Autor, 2026-09-02): nebelhaft-durchscheinend,
bewusst anders als Herberts solide dunkle Silhouette auf dem S2-1-Cover —
siehe COVER_S2-2.md Abschnitt 0, Punkt 3.]

‼️ THIS IS A CHILDREN'S BOOK (age 12) - "a shiver, never a nightmare". The
figure has ABSOLUTELY NO FACE: no eyes, no eye sockets, no mouth, no
features, no expression, nothing skull-like or gaunt, nothing sunken. If a
viewer can point to a face on her, the cover is unusable and must be redone.
She is NOT a wraith, NOT a horror-film ghost, NOT menacing, NOT reaching
out. She is a sad, faint, half-dissolved outline who does not move - only
unresolved. Keep her small, soft and easy to overlook, well behind the
children. Her head stays below 50 - she never rises into the subtitle.

COLOUR WORLD: muted brass and copper dominate in the lower half - warm metal
tones softened by dust and shadow, never bright or polished. The palette
stays cool and desaturated where the grey window light falls, warmer and
darker in the brass shelving nearer the viewer, and NEAR-BLACK across the
whole top 44% and the very bottom. The only warm, saturated point in the
entire image is the dog's amber eye.

★ DO NOT LET THE SCENE ITSELF GO TOO DARK. Separately from the deliberately
near-black text zones: WITHIN the scene (44 to 100) keep enough ambient
light that Nora's teal hoodie and Theo's olive jacket stay clearly readable
colours at normal viewing size, not just at full zoom. This was a failure
mode of the S2-1 cover. The result you want: near-black text zones above,
and a legibly-lit scene below them.

THE THREE FIGURES - ALL SEEN FROM DIRECTLY BEHIND, occupying roughly 58 to
100 of the height. Their heads must not reach higher than 56, so that they
stay well clear of the subtitle and below the clock face.
The viewer stands behind them and looks past their shoulders, down the
aisle. We see the BACK of their heads. Their faces are simply not in the
picture - not in profile, not in three-quarter view, not glimpsed. This is
a fixed rule of the series. They are NOT flat silhouettes: they are fully
painted figures lit from the front by the scene's single light source, so
their clothing colours read clearly even though they are seen from behind.

NORA (girl, 13) - straight shoulder-length MID-BROWN hair (not red, not
blonde). DARK TEAL zip-up hoodie (#2a8a7a), a clear blue-green. This is her
fixed series colour and must be plainly visible - a colour a reader could
name at a glance, not a shape that merely reads as "dark".

THEO (boy, 11) - smaller, half a step behind. Messy slightly curly DARK-BLOND
hair. Oversized MILITARY OLIVE-GREEN bomber jacket (#6b7a3a), a dull
yellow-green. His fixed series colour, plainly visible - likewise clearly
green, not merely a dark silhouette.

DO NOT SWAP THESE COLOURS: the GIRL wears TEAL, the BOY wears OLIVE. Readers
identify them by exactly this. Both colours must survive the scene's overall
darkness - light the two jackets enough that their hue is unmistakable,
even though the rest of the scene stays shadowed.

SCHATTEN (the dog) - medium-sized shaggy mixed-breed with dark, almost black
fur, a plain narrow LEATHER COLLAR (no harness, no chest straps, no vest).
Seen from behind and slightly to the side so that ONE eye is visible: a
LUMINOUS AMBER EYE (#d4920b), glowing from within. It is the single living
warm point of the cover and must stay visible at thumbnail size. His body is
tense, weight low, ears turned toward the blurred figure at the end of the
aisle.

They stand a good distance short of the figure, deep in the aisle between
the shelves. Nora is slightly ahead of Theo. Schatten stands close between
them, alert but not aggressive - not moving forward.

BETWEEN AND BELOW the figures, in the centre at about 80 to 86 of the
height, leave a calm, NEAR-BLACK, uncluttered patch of floor - this is where
the author's name goes. And keep the very bottom band (87 to 100) plain
near-black floor: no bright detail, no scattered points of light, no text.

════════════════════════════════════════
FINAL CHECK BEFORE YOU FINISH
════════════════════════════════════════

✓ GREYSCALE TEST: picture the cover in black and white. Is EVERY line of
  text obviously far lighter than everything directly behind and around it?
✓ Is the entire top 44% near-black - no window, no glow, no lit shelf edge,
  no bright wall anywhere behind the series line, cycle line, title or
  subtitle?
✓ Does the subtitle "Ein Grusel-Abenteuer für Kinder ab 12 Jahren" sit on
  plain near-black - NOT over the windows, the clock or any lit wall?
✓ Does no letter, on any line, touch or overlap a window, a lit edge, a
  reflection, a shelf edge, a figure or the blurred figure?
✓ Are the windows LOW - level with the clock, in the middle third - never
  high up under the ceiling?
✓ Is there a clearly visible EMPTY near-black band above "DIE GEISTERSPÜRER",
  at least twice as tall as its capital letters?
✓ Is there a clearly visible EMPTY near-black band below "Benjamin Krug",
  at least twice as tall as its letters?
✓ Does every line have visible empty background left and right of it?
✓ Does it say "ab 12 Jahren" - NOT "ab 10 Jahren"?
✓ GEISTERSPÜRER with Ü, für with ü, rückwärts with ü, DIE GEBUNDENEN · BAND 2
  with the middle dot?
✓ Is the title BRIGHT CREAM / bone white (NOT gold, NOT a mid-tone) and
  clearly the largest text? Series, cycle, subtitle, author all pale
  near-white grey?
✓ Is EVERY letter clean, solid and sharp - NO distressed, weathered,
  cracked, flaking or hammered texture on any line?
✓ Girl in TEAL, boy in OLIVE - not swapped? Are both colours clearly
  readable in the scene, not sunk into black?
✓ Is the dog's amber eye visible?
✓ No face anywhere - not the children's, and ESPECIALLY not the ghost's
  (no eyes, no sockets, no mouth, nothing gaunt or skull-like)?
✓ Is the ghost a small, faint, off-centre smudge of fog - NOT a clearly
  rendered figure, NOT centre-frame in the window, NOT scary?
✓ Is the dominant palette of the SCENE muted brass/copper (the text zones
  are deliberately near-black)?
✓ No badge, no logo, no frame, no invented words?

DO NOT INCLUDE: children's faces or any face in profile; a clearly rendered
ghost figure with a visible face; monsters, skeletons, bones, blood, gore,
scary grimaces; a third child or any additional person (no Frieda);
publisher logos, badges, seals, age roundels; a painted frame or border
around the image; modern elements, cars, phones, screens; neon colours;
manga, anime or flat cartoon style; any text beyond the five given lines.
```

---

## 4. Prompt Rückseite — All-in-One, mit allen Texten

> ✅ **Voraussetzung erfüllt:** `Staffel2/S2-2/KDP_S2-2.md` existiert jetzt, Abschnitt 6 trägt
> den Rückseitentext (Pull-Quote + Klappentext + Alters-/Reihenzeile), jedes Zitat/jede Zahl
> darin einzeln gegen das Manuskript geprüft (Abschnitt 3 desselben Dokuments dokumentiert die
> Fundstellen). Alle Texte unten sind **wörtlich** von dort übernommen, nichts neu formuliert.
>
> **Die gewählte Vorderseite als Referenzbild anhängen.** Ohne sie driften Palette und
> Lichtqualität auseinander.
>
> **Aufbau geändert (2026-09-03) gegenüber dem S2-1-Prompt:** Alle Texte stehen jetzt als
> wörtlicher Block **[A]–[K] ganz oben** (nicht mehr verteilt in nummerierten Zonen), die
> Szenenbeschreibung ist kurz und steht dahinter. Grund: siehe Warnkasten am Ende des
> Prompts. Für künftige Bände gehört diese Reihenfolge (Text zuerst, wörtlich) in den
> `Cover_Reihenstandard.md`.

```
Generate a complete, print-ready BACK COVER for a German children's book:
6 x 9 inch paperback, vertical portrait, aspect ratio 2:3. ONE single image -
a dark background illustration with every text block below rendered onto it,
crisp, correctly spelled, nothing missing.

The chosen FRONT COVER is attached. Match its palette and its light exactly.

╔══════════════════════════════════════════════════════╗
  THE TEXT - THIS BLOCK IS THE ONLY SOURCE OF TRUTH
╚══════════════════════════════════════════════════════╝

Render the blocks [A] to [K] below, in this order, top to bottom, WORD FOR
WORD. Do NOT translate, shorten, expand, summarise, rephrase, "improve",
reorder or invent a single word. Copy the letters exactly, every umlaut
(ä ö ü) and ß as printed, German curly quotes „ " on block [C].

[A]  Die Geisterspürer

[B]  Die Gebundenen · Band 2

[C]  „Eine von hundert. Neunundneunzig übrig."

[D]  Seit drei Monaten liegt das Schloss aus ihrem letzten Fall in der
     Küchenschublade. Nora und Theo wissen immer noch nicht, wer es gemacht hat.

[E]  Die Spur führt an den Rand der Stadt, zu einer verlassenen Uhrmacher- und
     Schlosserwerkstatt. Betrieb eingestellt, steht im Register. Im obersten
     Stockwerk brennt trotzdem Licht.

[F]  Drinnen finden sie nicht ein Schloss. Sie finden hundert. Regale voller
     kleiner, kalter Schlösser. Wände voller Uhren, die alle die falsche Zeit
     zeigen. Zum ersten Mal ist sogar Schatten überwältigt.

[G]  Eine der Gefangenen ist Grete. Sie weiß nicht mehr, warum sie hier ist -
     nur, dass sie unterwegs war, zu jemandem, der auf sie wartete.

[H]  Jemand hat das alles gebaut. Und jetzt gibt es auch jemanden, der es für
     ihn bewacht.

[I]  Grusel-Abenteuer für mutige Leser ab 12 Jahren — Kribbeln ja, Albträume nein.

[J]  Band 2 der Gebundenen. Band 1, Der Gast, der blieb, ist bereits erschienen.

[K]  Benjamin Krug

There is NO other text on this cover. No further headline, sentence, tagline,
keyword row, blurb, quote, motto, price, website, publisher, or number of any
kind appears anywhere.

FORBIDDEN TEXT - never render any of the following. They belong to other
books, not this one, and putting them here ruins the file:
- ANY barcode, ISBN, EAN, price code, digit sequence, or block of parallel
  vertical lines - anywhere on the image.
- "ab 10 Jahren" or "Für Leserinnen und Leser ab ..." in any form. The age
  is TWELVE and block [I] is the ONLY age line.
- the words Whitby, Docklands, Hafen, Werft, Technologie, Entwicklung,
  Experiment, tödlich, Gefahr, überleben, "drei Freunde".
- keyword / theme rows such as "Freundschaft · Mut · Geheimnisse" or
  "Geister, die binden · Wahlen, die alles verändern".
- any generic adventure blurb the model might reach for instead of [D]-[H].

╔══════════════════════════════════════════════════════╗
  LAYOUT   (image height = 0 at top, 100 at bottom; all text centred
  horizontally inside the central 84% of the width)
╚══════════════════════════════════════════════════════╝

  0 -  9   empty near-black wall. No text.
 10 - 17   [A] on top, [B] smaller directly under it. Clean elegant serif -
           NOT distressed, NOT worn, NOT antiqued. Pale steel grey #c8d0d8
           (close to white), [B] a touch dimmer.
 19 - 24   a thin faint horizontal rule, then [C]. Clean italic serif, pale
           warm cream #efe7d3 (light-on-dark). One or two centred lines. A
           second faint rule below it.
 26 - 68   the Klappentext: [D], [E], [F], [G], then [H]. Left-aligned inside
           a centred column about 76% of the width. Clean readable serif
           (Georgia / Garamond feel), warm light-white #eaedf2. One blank
           line between blocks. [H] in italic, centred. Line spacing ~155%.
           If it does not all fit, make the type SMALLER - never drop,
           shorten or merge a block.
 70 - 77   a thin faint rule, then [I]. Clean sans-serif, muted light grey
           #c0c8c0. May wrap to two centred lines.
 79 - 83   [J], centred, smaller, dim grey #8d959c.
 85 - 89   [K], centred, clean sans-serif, pale steel grey #c8d0d8.
 90 - 100  empty near-black floor. No text.

Above [A] and below [K] there must be a clear strip of plain near-black
background at least twice as tall as that line's capital letters.

╔══════════════════════════════════════════════════════╗
  BACKGROUND - subtle, and it must never fight the text
╚══════════════════════════════════════════════════════╝

The same clockmaker's-and-locksmith's workshop as the front cover, same
muted brass/copper palette, never bright or polished.

The whole CENTRE - the full height of the text column - is smooth
NEAR-BLACK wall: the darkest tone in the image, no detail, no highlight,
no window light bleeding in. Warm brass appears ONLY as a thin frame at the
four edges:
- TOP edge (upper ~10%): a dark shelf of indistinct padlocks in deep shadow.
- LEFT edge (left ~10%): the edge of one grimy window, a faint cold
  grey-silver light falling right and downward, gone well before the centre.
  This is the only light in the image.
- RIGHT edge (right ~10%): a dark strip of clocks in deep shadow, faces
  unreadable, none lit. This strip STOPS at about 60 of the height - the
  entire lower-right quarter is plain near-black with nothing in it.
- BOTTOM edge (lower ~10%): bare dark floorboards, a few faint cold light
  points on the LEFT only, never crossing into the right half.

NO FIGURES anywhere - no children, no dog, no ghost, no person, no silhouette.

BOTTOM-RIGHT QUARTER (the right 42% of the width by the bottom 20% of the
height): plain near-black, completely empty. No text, no light, no object,
no rule, no rectangle, and above all NO barcode and NO digits. The printer
drops the real barcode onto this dark area later - your only job is to leave
it clean, flat and dark.

╔══════════════════════════════════════════════════════╗
  TEXT-BACKGROUND CONTRAST (KDP rejected the front of this book 3x for
  "text blends into the background")
╚══════════════════════════════════════════════════════╝

- ALL LETTERING IS CLEAN AND SOLID: sharp-edged, evenly filled, like fresh
  crisp printing. NO distressed / weathered / antiqued / eroded / cracked /
  flaking / textured type anywhere, on any line, including [A] and [C].
- Text colour is clean light-on-dark ONLY: body #eaedf2, headline/quote/age/
  author pale cream or near-white grey. NO gold, NO amber, NO mid-tone text.
- Every line sits on near-black. Imagine the cover in greyscale: every
  letter must read as clearly far lighter than everything behind it.
- Nothing behind any letter: no window light, shelf, clock, sparkle or
  reflection touches the text column.
- If a patch behind a line is not near-black, darken the BACKGROUND there -
  never dim, recolour or shrink the text to hide a bright patch.
- Each line carries a subtle, narrow near-black outline / drop shadow so its
  edge holds. Cleanly printed - not glowing, not stickered.

╔══════════════════════════════════════════════════════╗
  BEFORE YOU FINISH - CHECK
╚══════════════════════════════════════════════════════╝

1. Read every rendered sentence and compare it letter by letter to blocks
   [A]-[K]. Any word not found there is an error - remove it.
2. [D] [E] [F] [G] [H] are all present, complete, in order; [H] is italic.
3. It says "ab 12 Jahren". "Whitby" does not appear. No keyword/theme row.
   No second blurb.
4. NO barcode, NO ISBN, NO digits anywhere. The lower-right quarter is
   empty and dark.
5. Umlauts correct, no ae/oe/ue: Geisterspürer, für, weiß, Schlösser, Wände,
   überwältigt, Gefangenen, Albträume.
6. „ and " on [C] are German curly quotes.
7. Greyscale test: every one of the eleven blocks is clearly lighter than
   its background.
8. No figures. Warm brass only at the four edges; the centre is near-black.
```

> ⚠️ **Realistische Erwartung — der erste Versuch (2026-09-03) ist genau hier gescheitert.**
> Das Modell hat den kompletten Klappentext ignoriert und einen generischen erfunden
> („Docklands von Whitby", „technologische Entwicklung … tödliche Folgen", „drei Freunde",
> „ab 10 Jahren") und zusätzlich einen **Barcode samt Fantasie-ISBN** ins Bild gemalt. Der
> Prompt oben ist daraufhin umgebaut: **alle Texte wörtlich als Block [A]–[K] ganz oben**,
> Szene stark gekürzt, eine namentliche Verbotsliste gegen genau diese Halluzinationen.
>
> Trotzdem: ein Klappentext dieser Länge bleibt die schwerste Aufgabe für ein Bildmodell.
> **4–6 Varianten** erzeugen, jede Zeile Buchstabe für Buchstabe gegen [A]–[K] prüfen. Wenn
> nach **drei bis vier Versuchen** keine Variante fehlerfrei ist: **abbrechen und den sicheren
> Weg gehen** — dieselbe Szene ohne Text erzeugen (nur der Hintergrund-Block, keine Zonen,
> Barcode-Feld leer) und die Texte [A]–[K] in einem Layoutprogramm (Affinity, InDesign, auch
> Canva) sauber setzen. Dann stimmt jedes Wort garantiert, und der Kontrast ist voll unter
> Kontrolle.

---

## 5. Ablauf und Prüfliste

1. **Erst `KDP_S2-2.md` mit echtem Klappentext schreiben** (Voraussetzung für Abschnitt 4).
2. Vorderseite erzeugen, **4–6 Varianten**.
3. Beste wählen. Zwei Prüfungen, beide zwingend:
   a) **Texte Buchstabe für Buchstabe** — `GEISTERSPÜRER` (Ü), `für` (ü), `rückwärts` (ü),
      **`ab 12 Jahren`** (nicht 10), **`DIE GEBUNDENEN · BAND 2`**.
   b) **Lesbarkeit / Kontrast (Block F):** Variante in Graustufen umrechnen. Hebt sich jede
      Zeile klar ab? Liegt hinter jeder Zeile Nahezu-Schwarz? Liegt das Fensterlicht tief
      (mittleres Drittel), nicht hinter Untertitel/Titel? Berührt kein Buchstabe Fenster,
      Lichtkante, Regalkante, Figur oder Geist? Fällt eine Variante durch: **nicht auswählen**,
      neu erzeugen. Schrift nie nachträglich abdunkeln.
4. Rückseite mit der gewählten Vorderseite als Referenz erzeugen (erst nach Schritt 1) —
   dieselbe Graustufen-Prüfung (3b) auch hier.
5. Beide hochskalieren auf mindestens **1838 × 2775 px**.
6. Ablegen als `Staffel2/S2-2/Cover/Bilder/front_s2_2.png` und `back_s2_2.png`.
7. Falls Widmung/Epigraph inzwischen freigegeben: Taschenbuch-PDF neu bauen, **echte
   Seitenzahl neu ablesen** → `PAGES` im Cover-Skript.
8. Cover-Build-Skript laufen lassen (analog `Scripts/build_cover_kdp_band4.py` /
   `build_cover_s2_1.py`).
9. **Kontrollbild ansehen** — liegt aller Text innerhalb der cyanen Linie? Ist das
   magentafarbene Barcode-Feld leer? Stimmt der Rückentitel? Ist der gemalte Buchrücken so
   breit wie der rechnerische?
10. **150-px-Thumbnail** — erkennbar müssen bleiben: Titel, die rückwärtslaufende Uhr (falls
    im Bild), das Bernsteinauge, und „DIE GEBUNDENEN · BAND 2".
11. Erst dann zu KDP.

---

## 6. Offen

| Punkt | Blockiert durch |
|---|---|
| ~~Rückseiten-Prompt (Abschnitt 4)~~ | ✅ erledigt — `KDP_S2-2.md` existiert, Text wörtlich übernommen |
| ~~Bilder von KDP 3× wegen 》Text verschwimmt《 abgelehnt~~ | ✅ behoben (04.09.2026). Ursachen: antikisierte/rissige Schrift + Gold als Mittelton (+ ESRGAN-Textur). Fix: Regel 0 (Schrift sauber), **Titel Creme-Weiß `#efe7d3` statt Gold**, kein KI-Upscaler. Beide Bilder neu erzeugt (4096×6144, ohne ESRGAN), Text jetzt sauber+kontrastreich. **Vollcover neu gebaut, ohne `--unscharf-erlauben`.** |
| Szene = Bibliothek statt Uhrmacher-Werkstatt; keine Uhren auf der Vorderseite; Geist voll sichtbar mittig; 》tro✝zdem《 auf der Rückseite | **bewusst akzeptiert (Nutzer, 04.09.2026)** — trotz meiner Einwände. „Passt genau so, gibt Persönlichkeit." Nicht mehr ändern. |
| ~~Cover-Build-Skript für S2-2~~ | ✅ erledigt — `Scripts/build_cover_s2_2.py` gelaufen `--seiten 82 --final`, ohne `--unscharf-erlauben`. Output: `Output/S2-2/KDP_S2-2_Cover_*` |
| ~~Seitenzahl unter der KDP-Rücken-Grenze~~ | ✅ behoben — Manuskript auf 82 Seiten erweitert (02.09.2026, siehe `Kontinuitaet_S2-2.md`) |
| ~~Bild-Auflösung unter dem 300-dpi-Druckstandard~~ | ✅ behoben (03.09.2026) — Real-ESRGAN x4plus (GPU) auf beide Bilder, dann LANCZOS auf **2560 × 3840 px**. Originale gesichert als `vorderseite_src1024.png` / `rueckseite_src1024.png`. Build lief ohne `--unscharf-erlauben` durch, Buchstabenkanten sauber (Crops geprüft). Native 4K-Erzeugung wäre minimal besser, ist aber nicht nötig. |
| ~~Buchrücken-Text 2,9–3,4 pt~~ | ✅ behoben (04.09.2026) — **war der Grund für die 2./3. KDP-Ablehnung** („Text schwer lesbar"). KDP-Cover-Guideline: **mind. 7 pt überall, auch auf dem Rücken** (`kdp.amazon.com/help/topic/G201834260`). Bei 82 Seiten (16 px nutzbar) passt kein 7-pt-Text → `build_cover.py` lässt den Rücken jetzt **textfrei**, wenn 7 pt nicht passt. Sauberer leerer Rücken statt Schmierer. |
| Echte Seitenzahl **mit** Frontmatter | Widmung/Epigraph noch nicht freigegeben. **Wenn freigegeben → Seitenzahl ändert sich → Cover mit neuer Zahl neu bauen** (Rückenbreite hängt daran). |
