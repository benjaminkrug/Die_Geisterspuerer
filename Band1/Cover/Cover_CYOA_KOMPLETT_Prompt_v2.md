# Komplett-Prompt v2 — CYOA-Cover „Das Haus, das flüstert" (Bild + Text in einem)

> **Überarbeitung von** `Cover_CYOA_KOMPLETT_Prompt.md` nach Genre-/Wettbewerbsanalyse.
> **Für:** ChatGPT / GPT-4o / Nano Banana. **Sprache:** Deutsch+Englisch gemischt.
> **Methode:** Alles im Prompt (Text eingebrannt), wie bei Band 2.

---

## Was sich gegenüber v1 ändert und WARUM (kurz)

| Änderung v1 → v2 | Begründung (aus der Analyse) |
|---|---|
| „24 ENDEN" → **„23 ENDEN + 1 GEHEIMES ENDE"** | v1 widersprach dem Amazon-Titel (23). „Geheimes Ende" ist ein stärkerer Sammel-/Neugier-USP als eine bloße hohe Zahl. |
| Banner-Balken → **Badge/Siegel** (Stempel-Optik, in Bildstil integriert) | Der aufgeklebte gelbe Kasten war das schwächste, unprofessionellste Element. Top-Performer setzen den USP als gestaltetes Marken-Badge. |
| USP-Text **auf 1 Badge zusammengefasst** | v1 hatte 2 Bannerzeilen + Serientitel, die sich quetschten. Weniger Ebenen = jede wirkt stärker. |
| **Titel-Rendering gehärtet** (jeder Buchstabe voll, „flüstert" NICHT auflösen) | Auf dem echten Cover war „flüstert" zerfranst = Amateur-Marker. Die Nebel-Auflösung von v1 hat das begünstigt → gestrichen. |
| Thumbnail-Priorität geschärft (Reihenname + Titel + Zahl bei 200 px lesbar) | Amazon verkauft im Miniaturformat. |

---

## ✅ Vor jeder Generierung prüfen (häufigste Patzer)
1. Hochformat 1600×2560, NICHT quadratisch.
2. Genau **2 Kinder + 1 Hund**.
3. Umlaute: **GEISTERSPÜRER** (Ü), **flüstert** (ü) — niemals UE/UER.
4. USP-Badge sichtbar, **„23 ENDEN"** vollständig, **„+ 1 GEHEIMES ENDE"** lesbar.
5. „flüstert" ist SCHARF und vollständig — NICHT zerfasert/aufgelöst.
6. Kein Geist/Monster/Totenkopf/Blut. Nur „HILF" im Fenster.

---

# A) HAUPT-PROMPT (Bild + Text)

```
Erstelle ein hochauflösendes Buchcover im HOCHFORMAT, Seitenverhältnis 5:8 (1600 x 2560
Pixel, Breite KLEINER als Höhe). WICHTIG: Das Bild darf AUF KEINEN FALL quadratisch oder
querformatig sein — es ist ein stehendes Buchcover, deutlich höher als breit.

Es ist das Cover eines deutschen Kinder-Grusel-Entscheidungsbuchs ("du entscheidest, wie
die Geschichte weitergeht") für Kinder ab 10 Jahren. Zielwirkung: geheimnisvoll, spannend
und EINLADEND — Gänsehaut zum Kribbeln, NICHT bedrohlich oder albtraumhaft.

STIL:
Semi-realistische, malerische digitale Illustration (painterly digital illustration),
atmosphärisch und detailreich, wie ein hochwertiges, professionell verlegtes Kinderbuch-
Cover. NICHT fotorealistisch, NICHT Cartoon, NICHT Comic, NICHT Anime. Referenz-Gefühl:
die Stimmung britischer "Lockwood & Co"-Cover kombiniert mit dem warmen Farbkontrast guter
"Gänsehaut"-Cover.

KDP-SICHERHEITSZONE:
Halte rundum einen Sicherheitsabstand von mindestens 12-15 % zum Bildrand ein. KEIN Text
und keine wichtigen Bildelemente (Gesichter, der Hund, das Wort HILF) dürfen in dieser
Randzone liegen.

================ BILDAUFBAU (von unten nach oben) ================

PERSPEKTIVE: Nachtszene, frontale Ansicht, leicht aus der Untersicht (low angle), sodass
das Haus aufragt und die Kinder heldenhaft und mutig wirken.

VORDERGRUND — DIE FIGUREN (im unteren Drittel, GESICHTER GUT SICHTBAR):
Genau ZWEI Kinder und EIN Hund stehen frontal zum Betrachter auf nassem Kopfsteinpflaster.
Sie schauen den Betrachter direkt an, ihr Ausdruck sagt freundlich-herausfordernd
"Kommst du mit?". (GENAU zwei Kinder und ein Hund — keine weiteren Personen.)

- MÄDCHEN (12 Jahre, links): schulterlanges braunes Haar. Trägt einen petrol/türkisfarbenen
  Zip-Hoodie (Farbe #2a8a7a — die einzige kräftig gesättigte Kleidungsfarbe im Bild). In
  einer Hand hält sie eine eingeschaltete TASCHENLAMPE, deren warmes Licht ihr Gesicht und
  das ihres Bruders von schräg unten beleuchtet. Haltung: aufrecht, mutig, neugierig.

- JUNGE (10 Jahre, rechts, einen halben Schritt hinter dem Mädchen): einen Kopf kleiner,
  strubbelig-lockiges dunkelblondes Haar. Trägt eine zu große olivgrüne Bomberjacke. Eine
  Hand umklammert den Riemen seines Rucksacks. Gesichtsausdruck: ein bisschen nervös, aber
  mutig lächelnd.

- HUND (mittig VORNE zwischen den Kindern): mittelgroßer Mischling mit dunklem, fast
  schwarzem Fell. LEUCHTENDE BERNSTEINFARBENE AUGEN (#d4920b), die im Dunkeln glühen. Ohren
  gespitzt, Nackenfell leicht aufgestellt. Den Hund mit Rand-/Taschenlampenlicht anschneiden,
  sodass seine Silhouette klar erkennbar ist — niemals schwarz-auf-schwarz.

CYOA-BILDMETAPHER (subtil): Das nasse Kopfsteinpflaster vor den Kindern TEILT SICH IN EINE
Y-GABELUNG — ein Weg führt geradeaus zur Haustür, der andere biegt nach links in die
Dunkelheit ab. Natürlich wirkend. Leise Andeutung von "du entscheidest deinen Weg".

MITTELGRUND — DAS HAUS (füllt die obere Bildhälfte, ragt hinter den Kindern auf):
EIN altes deutsches Altbau-Wohnhaus (3 Stockwerke plus Dach, Baustil ca. 1890-1920).
Verwitterte grau-weiße Putzfassade mit feinen Rissen, hohe schmale Fenster.
- Erdgeschoss: dunkel.
- 1. Stock: EIN Fenster mit warmem, goldgelbem Licht (#d4920b) — Anker der Geborgenheit.
- 2. Stock (DER BLICKFANG): EIN Fenster leuchtet kalt bläulich-weiß (#c8dff5). Auf der
  beschlagenen Scheibe steht im Kondenswasser das Wort "HILF" — wie von einem Kinderfinger
  geschrieben. Dieses Fenster ist der hellste kalte Punkt im Bild.
- Haustür steht einen Spalt offen; dünner Nebel kriecht darunter hervor.

HINTERGRUND:
Tiefer Nachthimmel, Farbverlauf von Navy-Blau (#1a1a3e) zu Indigo-Lila (#2d1b4e). Blasser
Vollmond oben links, teils von Wolken verdeckt. Silhouetten von Nachbardächern.

================ LICHT & FARBEN ================

LICHT (warm + kalt gemischt, damit es einladend bleibt):
- Vollmond oben links: kühles Silberlicht (Grundstimmung).
- Warme Anker: Taschenlampe auf den Gesichtern, warmes Fenster im 1. Stock, Hundeaugen.
- Einziger kalter Akzent: das Geisterfenster im 2. Stock.
- Nasses Pflaster reflektiert Mondlicht. Wenig Nebel, hauptsächlich an der Tür.

FARBPALETTE:
Dominierend dunkles Navy/Indigo. Warme Bernstein-Akzente (#d4920b). Pop-Farbe Petrol/Türkis
(#2a8a7a) nur auf dem Hoodie des Mädchens. Kaltes Blau-Weiß (#c8dff5) nur für das
Geisterfenster. Der Warm-Kalt-Kontrast hält das Cover lebendig und einladend.

================ TYPOGRAFIE — direkt im Bild ================

ABSOLUT KRITISCHE REGELN FÜR ALLE TEXTE:
1. Alle deutschen Texte enthalten ECHTE Umlaute mit zwei Punkten (Ü, ü). NIEMALS "UE",
   "ue", "UER". Buchstabiere jedes Wort im Kopf, bevor du es zeichnest.
   - "GEISTERSPÜRER" = G-E-I-S-T-E-R-S-P-Ü-R-E-R
   - "flüstert" = f-l-ü-s-t-e-r-t
2. Jeder Buchstabe wird VOLLSTÄNDIG und SCHARF gerendert. KEINE zerfaserten, abgeschnittenen,
   verschmierten oder halb aufgelösten Buchstaben. Der Titel darf NICHT im Nebel „verlaufen".
3. Klassische, saubere Buchschrift (professioneller Verlags-Look). Kein handgekritzeltes,
   ungleichmäßiges Lettering.
4. Jeder Text muss lesbar bleiben, wenn das Cover auf 200 Pixel Breite (Thumbnail) verkleinert
   wird → lieber wenige, große, klare Worte.

Setze GENAU diese vier Textelemente, von oben nach unten:

(1) SERIENTITEL — ganz oben, im dunklen Himmel:
    Text exakt: DIE GEISTERSPÜRER
    Stil: große, hohe, FETTE klassische Versalien, ca. 80 % der Coverbreite. Farbe silber-
    weiß (#e0e8f0) mit deutlicher dunkler Navy-Kontur (#1a1a3e) und weichem Schatten. Perfekt
    lesbar auch im Thumbnail. Jeder Buchstabe vollständig und scharf.

(2) USP-BADGE — als gestaltetes rundes/ovales SIEGEL (wie ein Wachs-/Stempelsiegel oder eine
    Auszeichnungs-Plakette), NICHT als aufgeklebter rechteckiger Balken. Position: oben rechts,
    leicht schräg, teilweise vor dem Nachthimmel. Es sieht aus, als gehöre es zur Illustration
    (gemalt, mit Textur, leichtem Schatten), nicht wie ein nachträglicher Aufkleber.
    Farbe: warmes Bernstein/Gold (#d4920b) mit dunkler Navy-Schrift (#1a1a3e) für hohen
    Kontrast. Text im Badge, kompakt gestapelt:
      Groß und fett, oben:   23 ENDEN
      Klein darunter:        + 1 GEHEIMES ENDE
      Ganz klein, als Bogen: DU ENTSCHEIDEST
    Die Zahl „23" ist das größte Element im Badge und muss im Thumbnail klar lesbar sein.
    Das Badge fällt sofort als „Belohnung/Versprechen" ins Auge, nicht als Warnschild.

(3) BANDTITEL — unter den Figuren, im unteren Bilddrittel:
    Text exakt: Das Haus, das flüstert
    Stil: elegante, gut lesbare kursive Serifenschrift, helles Türkis (#7abfbf), etwa halb so
    groß wie der Serientitel, mit weichem Schatten. WICHTIG: „flüstert" wird VOLLSTÄNDIG und
    SCHARF geschrieben — die letzten Buchstaben lösen sich NICHT auf und verlaufen NICHT im
    Nebel. Alle Buchstaben klar und gleich deutlich.

(4) FUSSZEILE — ganz unten, über dem unteren Sicherheitsrand, EINE Zeile:
    Text exakt: Benjamin Krug · Grusel-Abenteuer zum Selbstentscheiden · ab 10 Jahren
    Stil: schlichte, gedämpft-weiße serifenlose Schrift (#c0c8d0), klein, dezent, leicht
    gesperrt. Richtet sich an Eltern.

================ STRIKTE VERBOTE ================
- KEIN weiterer Text als die vier Elemente oben plus "HILF" im Fenster.
- KEINE weiteren Personen, KEIN sichtbarer Geist, KEIN Monster, KEIN Totenkopf, KEIN Blut,
  KEINE Spinnweben-Klischees.
- KEIN rechteckiger aufgeklebter Banner-Balken — der USP ist ein gestaltetes Siegel/Badge.
- KEINE zerfaserten/aufgelösten Buchstaben; „flüstert" scharf und vollständig.
- NICHT quadratisch, NICHT querformat — striktes Hochformat 5:8.
- Genau 2 Kinder und 1 Hund. Umlaute NIEMALS als ae/oe/ue.
```

---

# B) NUR-TEXT-KORREKTUR (wenn das Bild gut ist, aber der Text Fehler hat)

```
Das Bild ist gut — ändere AUSSCHLIESSLICH den Text, lass Illustration, Komposition, Figuren,
Farben und Beleuchtung exakt unverändert. Korrigiere die Texte zu GENAU diesen Schreibweisen,
mit echten Umlauten (Ü/ü = Buchstabe mit zwei Punkten, niemals UE/ue), jeder Buchstabe
vollständig und scharf:

- Serientitel oben:     DIE GEISTERSPÜRER
- USP-Badge (Siegel):   23 ENDEN / + 1 GEHEIMES ENDE / DU ENTSCHEIDEST
- Bandtitel:            Das Haus, das flüstert   (VOLLSTÄNDIG, nicht im Nebel auflösen)
- Fußzeile:             Benjamin Krug · Grusel-Abenteuer zum Selbstentscheiden · ab 10 Jahren

Buchstabiere vor dem Zeichnen: G-E-I-S-T-E-R-S-P-Ü-R-E-R und f-l-ü-s-t-e-r-t.
Stelle sicher, dass „23 ENDEN" vollständig und im Thumbnail lesbar ist. Sonst nichts ändern.
```

---

# C) Stimmungs-Korrekturen (Feinschliff)

**Zu düster/gruselig:**
```
Behalte Komposition und Text, aber weniger düster: mehr warmes Taschenlampenlicht auf den
Gesichtern, helleres warmes Fenster im 1. Stock, weniger Nebel. Stimmung: "mysteriös und
spannend", NICHT "bedrohlich".
```

**Badge sieht aufgeklebt / wie Aufkleber aus:**
```
Behalte alles, aber gestalte das USP-Siegel oben rechts so, dass es zur gemalten Illustration
gehört: gleiche malerische Textur wie das übrige Bild, weicher Schlagschatten, leicht schräg,
als wäre es ins Bild integriert — NICHT wie ein flacher digitaler Aufkleber oder ein
rechteckiger Balken.
```

**„flüstert" ist zerfasert/unlesbar:**
```
Behalte alles, aber schreibe den Bandtitel „Das Haus, das flüstert" komplett neu: klassische
klare kursive Serifenschrift, JEDER Buchstabe vollständig, scharf und gleich deutlich. Das
Wort „flüstert" darf sich NICHT auflösen, verlaufen oder im Nebel verschwinden.
```

---

# D) Wichtiger Metadaten-Hinweis
Das Cover verspricht „23 ENDEN + 1 GEHEIMES ENDE". Der Amazon-Titel sagt aktuell nur
„23 Enden". → Damit Cover und Produktseite exakt übereinstimmen, den Amazon-Untertitel bei
Gelegenheit auf „…mit 23 Enden und 1 geheimen Ende…" ergänzen. Sonst entsteht dieselbe
Cover-vs-Titel-Diskrepanz wie bei der alten „24".
```
