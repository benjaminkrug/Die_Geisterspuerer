# Cover-Reihenstandard — Die Geisterspürer, Band 1–5

> Der gemeinsame Unterbau aller fünf Cover-Prompts. Was hier steht, wird in jedem
> Band-Prompt vorausgesetzt und nicht wiederholt begründet. Geändert wird es hier,
> nicht in einer einzelnen Prompt-Datei.
>
> **Stand 2026-08-04.** Erstellt beim Neubau aller zehn Cover-Bilder.

---

## 1. Warum es dieses Blatt gibt

Die fünf verkauften Cover sind nach fünf verschiedenen Regeln gebaut worden.
Nachgemessen an den ausgelieferten Dateien:

| | Reihenzeile | Bandnummer | Titel-Hierarchie | Siegel | Format |
|---|---|---|---|---|---|
| Band 1 | „Die Geisterspürer" groß | fehlt | **Reihe groß, Titel klein** | — | **5 × 8 Zoll** |
| Band 2 | **„Die Geisterspùrer"** ✗ | fehlt | Titel groß | „Ab 10 Jahren" | 6 × 9 |
| Band 3 | „DIE GEISTERSPÜRER · BAND 3" | ✓ | Titel groß | — | 6 × 9 |
| Band 4 | „DIE GEISTERSPÜRER · BAND 4" | ✓ | Titel groß | — | 6 × 9 |
| Band 5 | „DIE GEISTERSPÜRER · BAND 5" | ✓ | Titel groß | — | 6 × 9 |

Band 3–5 sind sich einig. **Dieser Standard schreibt Band 3–5 fest und zieht
Band 1 und 2 nach.** Band 2 trägt den Reihennamen mit Gravis statt Umlaut —
„Geisterspùrer" — auf einem verkauften Buch.

Dazu zwei Fehler, die auf keinem Bildschirm auffallen:

- **Band 4 und 5 haben ein gemaltes Barcode-Rechteck an der falschen Stelle.**
  KDP druckt den Barcode unten rechts an einer festen Position; das gemalte
  Kästchen liegt daneben. Im Buch steht dort ein sinnloses helles Feld neben
  dem echten Barcode. → **Nie wieder ein Barcode-Feld malen lassen.** Die Zone
  bleibt einfach leerer Hintergrund.
- **Alle zehn Bilder liegen unter 300 dpi** (166–268 dpi). Band 1–4 sind
  unscharf und zusätzlich um 2 % gestaucht gedruckt.

---

## 2. Technische Vorgaben (KDP, weißes Papier)

**★ Zwei Formate. Band 1 ist 5 × 8, Band 2–5 sind 6 × 9.**

Das ist kein Versehen und wird auch nicht angeglichen: KDP lässt die
Trimmgröße eines veröffentlichten Taschenbuchs nicht ändern. Ein Wechsel wäre
ein **neues Buch mit neuer ASIN** — und die Rezensionen des Einstiegsbands
wandern nicht zuverlässig mit. Der Größenunterschied im Regal ist der bewusst
bezahlte Preis dafür. *(Geprüft und verworfen am 2026-08-04; die Umstellung
war gebaut und hätte 186 → 152 Seiten ergeben.)*

| | Band 1 (5 × 8) | Band 2–5 (6 × 9) |
|---|---|---|
| Panel inkl. Anschnitt | **1538 × 2475** px | **1838 × 2775** px |
| in Zoll | 5,125 × 8,25 | 6,125 × 9,25 |
| Verhältnis | **0,621** | **0,662** |
| Sichtbar nach dem Schnitt | 1500 × 2400 | 1800 × 2700 |
| eBook-Cover | 1600 × 2560 | 1600 × 2560 |

### Seitenverhältnis beim Erzeugen

Bildgeneratoren bieten `2:3` = 0,667 an. Das passt für **Band 2–5 fast exakt**
(0,662, unter 1 % Beschnitt).

**Für Band 1 nicht.** 0,667 gegen 0,621 heißt **6,7 % Breitenverlust**, also
3,35 % je Seite. Ein näheres Verhältnis gibt es im Angebot der Generatoren
nicht (`9:16` = 0,563 würde stattdessen 10 % Höhe kosten). Konsequenz:

> **Bei Band 1 muss aller Text im erzeugten Bild in den zentralen 78 % der
> Breite liegen** — nicht 84 % wie bei Band 2–5. Sonst rutscht er beim
> Beschnitt in den Sicherheitsrand. Genau das ist beim ersten Band-1-Bild
> passiert: „DAS FLÜSTERT" lag 7 px zu weit rechts und musste per
> `front_shift` um 11 px zurückgeholt werden.

Umgekehrt ist der **eBook-Beschnitt bei Band 1 praktisch null** (1600 × 2560 =
0,625 gegen Trimmverhältnis 0,625). Bei Band 2–5 fallen seitlich je 2,8 % weg —
dort muss Text die Seitenränder deutlich meiden, sonst steht er im Druck
korrekt und ist im eBook angeschnitten.

### Auflösung — der Punkt, an dem bisher alles scheiterte

Alle zehn verkauften Cover-Bilder liegen bei 166–268 dpi. Ursache: ChatGPT /
DALL·E liefert höchstens **1024 × 1536 px = 166 dpi** — weniger als die Hälfte
der nötigen Fläche.

**Die Lösung ist nicht Hochskalieren, sondern gleich groß erzeugen.**

| Weg | Ergebnis | Bewertung |
|---|---|---|
| **Nano Banana Pro, `resolution: 4k`, `2:3`** | ~2730 × 4096 px | ✅ **Empfohlen.** Direkt druckfähig, kein Upscale. Das Modell ist ausdrücklich auf Textwiedergabe ausgelegt — genau unsere Umlaut-Schwachstelle. |
| ChatGPT / DALL·E + KI-Upscaler 1,8× | 1838 × 2775 px | ⚠️ Notlösung |
| ChatGPT / DALL·E ohne Upscale | 1024 × 1536 px | ❌ Skript bricht ab |

> **Warum Hochskalieren hier besonders schlecht ist:** Auf diesen Covern steht
> der Titel **im Bild**. Buchstabenkanten sind exakt die Stelle, an der
> Upscaler Matsch produzieren — und der Titel ist das, was ein Käufer im
> Thumbnail zuerst ansieht. Wer 4K direkt erzeugt, umgeht das Problem, statt es
> zu reparieren.

**Seitenverhältnis immer `2:3`** (0,667) — für Band 2–5 liegt der Beschnitt
damit unter 1 %, für Band 1 bei 6,7 % (siehe oben). Jedes andere Verhältnis
kostet mehr Bildrand: die Band-5-Vorderseite (0,739) verliert seitlich 10,4 %.

`Scripts/build_cover.py` **bricht bei zu kleinen Bildern ab** — mit Absicht.
Eine Warnung reicht nicht: das Band-5-Skript hat gewarnt, und das Bild ist
trotzdem in den Druck gelaufen.

### Sicherheitszonen (Anteil am Panel, gilt für Vorder- UND Rückseite)

**Angaben als Anteil am erzeugten 2:3-Bild** — nicht am fertigen Panel. Das ist
der Wert, den man dem Bildmodell nennt.

| Zone | Band 2–5 (6 × 9) | Band 1 (5 × 8) |
|---|---|---|
| Text seitlich frei | **9 %** (zentrale 82 %) | **13 %** (zentrale **74 %**) |
| Text oben frei | 9 % | 9 % |
| Text unten frei | 9 % | 9 % |
| **Barcode (nur Rückseite)** | rechte **42 %** × untere **20 %** | rechte **46 %** × untere **22 %** |

Die Barcode-Zone bleibt **komplett frei von Text und Blickfang — und ohne
gemaltes Feld.**

### Warum diese Zahlen und nicht die KDP-Mindestwerte

KDP verlangt 0,25 Zoll (6,4 mm) Abstand zur Schnittkante. Genau darauf zu
zielen, ist zu knapp — das ist **nachgemessen, nicht befürchtet:**

> Der erste fertige Band-1-Umschlag hielt exakt die damals geforderten 8 %.
> Ergebnis im KDP-Previewer: „DAS FLÜSTERT" lag bei **6,6 mm** von der
> Schnittkante — 0,2 mm über der Grenze, optisch klebend. „Benjamin Krug" lag
> bei **2 bis 3 mm**, also darunter. Der Prompt hatte 6 % Höhe verlangt; das
> Modell lieferte 3,3 %.

Zwei Lehren:

1. **Bildmodelle unterschreiten die genannten Ränder.** Man muss mehr fordern,
   als man braucht. Die Werte oben zielen auf ~10 mm Abstand statt 6,4 mm.
2. **Prozentangaben allein wirken schlecht.** Immer eine anschauliche
   Gegenprobe danebenstellen — „so breit wie vier Großbuchstaben" statt nur
   „13 %" — und das Ganze als *„dieser Streifen wird abgeschnitten"*
   formulieren, nicht als Gestaltungswunsch.

### Wenn ein fertiges Bild zu knappe Ränder hat

**Nicht neu generieren — die Leinwand vergrößern.** Adobe Firefly Generative
Expand (oder ein vergleichbares Werkzeug) hängt oben Himmel und unten Boden an;
strukturlose Flächen bekommt ein Modell zuverlässig hin. Das geprüfte Bild und
sein geprüfter Text bleiben unangetastet, nur der Rahmen wächst.

Zielmaß: die Leinwand so erweitern, dass sie **exakt das Panel-Verhältnis**
trifft (Band 1: 0,621, Band 2–5: 0,662). Dann entfällt der Beschnitt ganz.
Beispiel Band 1: aus 2047 × 3072 wird 2150 × 3460 — Titelabstand steigt von
6,6 mm auf 12 mm, Autorname von ~2 mm auf ~15 mm.

### Buchrücken

Wird **vom Skript gesetzt, nie generiert** — es ist Text auf einer Fläche.
Breite = Seitenzahl × 0,002252 Zoll (weißes Papier).

| Band | Seiten | Rücken | davon nutzbar |
|---|---:|---:|---:|
| 1 | 186 | 10,6 mm | **7,5 mm** |
| 2 | 113 | 6,5 mm | 3,3 mm |
| 3 | 106 | 6,1 mm | 2,9 mm |
| 4 | 95 | 5,4 mm | **2,3 mm** |
| 5 | 104 | 5,9 mm | 2,8 mm |

Aufbau von oben nach unten: **Bandnummer** (Bernsteingold) · **Titel** (Kalkweiß)
· **DIE GEISTERSPÜRER** (Gold, klein) · **Benjamin Krug** (Kalkweiß).
Leserichtung **oben nach unten** — nachgemessen an den gedruckten Rücken von
Band 2 bis 5, alle vier laufen so.

**Band 1 ist mit 7,5 mm nutzbarer Höhe der einzige Rücken, auf dem alle vier
Zeilen bequem stehen** — er hat mehr als dreimal so viel Platz wie Band 4.
(186 Seiten im kleineren 5×8-Format ergeben den mit Abstand dicksten Rücken
der Reihe.)
Bei Band 4 (2,3 mm nutzbar) wird es eng; wenn nötig entfällt zuerst die
Reihenzeile, **nie die Bandnummer.** Im Regal ist sie das Einzige, was
beantwortet, ob es mehr davon gibt — und bisher trägt sie **kein einziger** Band.

---

## 3. Die vier Texte — auf jedem Cover, exakt so

```
1  Reihenzeile   DIE GEISTERSPÜRER · BAND N
2  Haupttitel    <Titel des Bandes>
3  Untertitel    Ein Grusel-Abenteuer für Kinder ab 10 Jahren
4  Autor         Benjamin Krug
```

- **Kein Siegel, kein Badge, kein Verlagslogo, keine Reihen-Vignette.** Es gibt
  keinen Verlag; Bildmodelle setzen kleinen Rundtext unlesbar. Band 2 ist der
  einzige Band mit Siegel — das entfällt.
- **Der Haupttitel ist der dominante Text.** Band 1 macht es umgekehrt (Reihe
  groß, Titel klein in Schreibschrift) — das wird angeglichen.
- Umlaut-Kontrolle: **GEISTERSPÜRER** mit Ü, **für** mit ü. Buchstabe für
  Buchstabe prüfen, nicht überfliegen.

### Farben

| Rolle | Hex |
|---|---|
| **Haupttitel** | **`#dfb057` Gold** (Glanzkante `#f0cb80`, Schattenkante `#d4a44a`) |
| Reihenzeile / Untertitel | `#9aa6b0` Stahlgrau — oder in Gold mitlaufend |
| Schattens Augen (Reihen-Akzent) | `#d4920b` Bernstein |
| Noras Hoodie | `#2a8a7a` Teal |
| Theos Bomberjacke | `#6b7a3a` Oliv |

> **★ Titelfarbe GOLD — Entscheidung vom 2026-08-05.**
> Der Wert oben ist aus den fertigen Vorderseiten von Band 2 (`#e1b162`) und
> Band 3 (`#ddae4c`) **gemessen**, nicht gesetzt — beide Bildmodelle haben von
> sich aus dasselbe warme Gold gewählt, und es steht den dunklen Motiven
> besser als Kalkweiß. Es greift außerdem Schattens Bernstein auf.
>
> **Band 1 ist die Ausnahme:** Er ist bereits mit kalkweißem Titel
> veröffentlicht und bleibt vorerst so. Nachziehen, wenn ohnehin ein
> Cover-Update ansteht — dafür allein lohnt kein Upload. Band 4 und 5 werden
> in Gold erzeugt.

**Teal, Oliv und Bernstein sind nicht dekorativ — sie sind die
Wiedererkennung der Reihe.** Auf dem Band-5-Cover fehlen alle drei (beide
Kinder braun, kein sichtbares Hundeauge); genau das wird beim Neubau behoben.

---

## 4. Reihen-Grammatik (aus Band 3, 4 und 5 abgelesen)

1. **Zwei Kinder und der Hund, von hinten**, im unteren Drittel. Gesichter sind
   nie zu sehen — auch nicht im Profil, auch nicht angeschnitten.
2. Sie **blicken in eine Öffnung hinein**: Tür, Tor, Tunnel, Spiegel, Fenster.
3. **Genau eine Lichtquelle** in der Bildmitte ist der Hingucker. Alles Licht im
   Bild kommt von dort.
4. **Schattens Auge** ist der einzige lebendige Punkt.
5. **Oberes Drittel bleibt ruhig** — dort steht der Titel.
6. **Nie ein klar erkennbarer Geist.** Silhouette, Andeutung, Hand — kein
   Gesicht. (Band 2 zeigt zwei Geister mit Gesichtern; das ist der Ausreißer.)
7. **Kein Blut, keine Fratze, keine Skelette.** „Kribbeln, kein Albtraum."
8. Alles führt zur Bildmitte.

### Farbwelt je Band — jeder Band muss sich im Thumbnail unterscheiden

| Band | Ort | dominant | Akzent |
|---|---|---|---|
| 1 | Altbau bei Nacht | Indigo / Violett | kaltes Blau (Fenster) + Bernstein |
| 2 | Alter Friedhof | Waldgrün / Nebelgrau | Mondweiß |
| 3 | Stillgelegte U-Bahn | Stahlblau | Grünlicht + Taschenlampe |
| 4 | Kaltes Zimmer, zugemauerte Tür | Blaugrau | **warmes Gold** (Türspalt) |
| 5 | Steingewölbe | warmes Braun-Schwarz | **kaltes Silbergrau** (Spiegel) |

---

## 5. Wiederverwendbare Prompt-Blöcke

Diese vier Blöcke stehen wörtlich in jedem Band-Prompt. Nur der Bandinhalt
dazwischen wechselt.

### Block A — Kopfblock (steht ganz oben, vor allem anderen)

Der Grund: beim ersten Band-5-Versuch standen die Cover-Texte erst bei 47 % des
Prompts. Das Modell hat vorher auf eigenen Kontext zurückgegriffen und
„DIE HERRENHAUS-DETEKTIVE" plus ein erfundenes Verlagslogo gemalt.

```
========================================
READ THIS BLOCK FIRST - IT OVERRIDES ANY EARLIER CONTEXT
========================================

This cover belongs to the German children's series "DIE GEISTERSPÜRER"
(The Ghost Trackers), for ages 10-12. It is NOT "Die Herrenhaus-Detektive"
and NOT any other series. Ignore any other book series, title, manor house
or branding from earlier in this conversation.

EXACTLY these four texts appear on the cover - no others, none invented:
  1. series line : DIE GEISTERSPÜRER · BAND <N>
  2. main title  : <TITEL>
  3. subtitle    : Ein Grusel-Abenteuer für Kinder ab 10 Jahren
  4. author      : Benjamin Krug

Forbidden anywhere: any publisher name, imprint or logo; any badge, seal,
sticker, ribbon, banner or emblem; any age roundel; any painted frame or
border around the artwork; any word not in the four texts above.
========================================
```

### Block B — Sicherheitsränder (der Block, der bisher fehlte)

Band 1 hat den Untertitel unterhalb der Sicherheitslinie stehen — er kann im
Druck angeschnitten werden.

```
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
```

### Block C — Figuren (unverändert in allen fünf Bänden)

```
THE THREE FIGURES - ALL SEEN FROM DIRECTLY BEHIND, in the lower third.
The viewer stands behind them and looks past their shoulders. We see the BACK
of their heads. Their faces are simply not in the picture - not in profile,
not in three-quarter view, not glimpsed. This is a fixed rule of the series.
They are NOT flat silhouettes: they are fully painted figures lit from the
front by the scene's single light source, so their clothing colours read
clearly even though they are seen from behind.

NORA (girl, 12) - straight shoulder-length MID-BROWN hair (not red, not
blonde). DARK TEAL zip-up hoodie (#2a8a7a), a clear blue-green. This is her
fixed series colour and must be plainly visible.

THEO (boy, 10) - smaller, half a step behind. Messy slightly curly DARK-BLOND
hair. Oversized MILITARY OLIVE-GREEN bomber jacket (#6b7a3a), a dull
yellow-green. His fixed series colour, plainly visible.

DO NOT SWAP THESE COLOURS: the GIRL wears TEAL, the BOY wears OLIVE. Readers
identify them by exactly this.

SCHATTEN (the dog) - medium-sized shaggy mixed-breed with dark, almost black
fur, a plain narrow LEATHER COLLAR (no harness, no chest straps, no vest).
Seen from behind and slightly to the side so that ONE eye is visible: a
LUMINOUS AMBER EYE (#d4920b), glowing from within. It is the single living
warm point of the cover and must stay visible at thumbnail size.
```

### Block D — Verbotsliste (am Ende jedes Prompts)

```
DO NOT INCLUDE: children's faces or any face in profile; a clearly rendered
ghost figure with a visible face; monsters, skeletons, bones, blood, gore,
scary grimaces; a third child or any additional person; publisher logos,
badges, seals, age roundels; a painted frame or border around the image;
modern elements, cars, phones, screens; neon colours; manga, anime or flat
cartoon style; any text beyond the four given lines.
```

### Block E — Rückseite, Barcode-Zone

```
BARCODE ZONE (CRITICAL): the BOTTOM-RIGHT of the back cover - the right 42%
of the width by the bottom 20% of the height - must stay calm, dark, empty
background: no text, no focal detail, no bright object.
Do NOT paint a grey, cream or white rectangle there, and do NOT paint a
barcode. The printer places the real barcode on top of the plain background.
(The Band 4 and Band 5 back covers each have a painted cream rectangle that
sits NEXT TO the real barcode position - that is the mistake this rule
prevents.)
```

---

## 6. Ablauf je Band

1. **Vorderseite** mit dem Band-Prompt erzeugen, 4–6 Varianten.
2. Beste wählen. **Texte Buchstabe für Buchstabe prüfen** — besonders
   `GEISTERSPÜRER` (Ü) und `für` (ü).
3. **Rückseite** mit dem Band-Rückseiten-Prompt erzeugen, passend zur gewählten
   Vorderseite (diese als Referenzbild anhängen).
4. **Beide Bilder hochskalieren** auf mindestens 1838 × 2775 px.
5. Ablegen als `BandN/Cover/Bilder/front_bandN.png` und `back_bandN.png`.
6. `py Scripts/build_cover.py N` — bricht bei zu kleinen Bildern ab.
7. **Kontrollbild ansehen:** liegt aller Text innerhalb der cyanen Linie? Ist das
   magentafarbene Barcode-Feld leer? Steht auf dem Rücken der richtige Titel?
8. **Thumbnail bei 150 px ansehen:** Titel, Hingucker und Bernsteinauge noch
   erkennbar?
9. Erst dann zu KDP.

> Schritt 7 ist nicht optional. Der falsch platzierte Barcode-Kasten in Band 4
> und 5 war auf jedem Bildschirm unsichtbar und nur mit eingezeichneten Linien
> zu sehen.
