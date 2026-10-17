# A2 · Stimmen der Figuren — wie jede Figur auf Englisch klingt

> Phase A der englischen Ausgabe. Stand 2026-10-12.
> **Quelle:** `python3 Scripts/en_bibel_extrakt.py stimmen --band1 <umgebaute Fassung>` (wörtliche Rede
> aller fünf Bände, je Figur gezählt) plus gezieltes Nachlesen der Stellen.
>
> **Wozu:** Die Übersetzung (D2) und der US-Lektor (D5) prüfen jede Rede gegen diese Seite.
> Die häufigste Schwäche von KI-Übersetzungen ist, dass **alle Figuren gleich klingen** — glatt,
> erwachsen, etwas witziger als das Original. Diese Seite sagt für jede Figur, was sie ausmacht und was
> auf Englisch **nicht** passieren darf.

---

## 0. Messwerte und ihre Grenzen

| Figur | Reden | Wörter/Rede | Fragen | Ausrufe | ≤ 3 Wörter |
|---|---|---|---|---|---|
| Theo | 922 | 9,4 | 24 % | 1 % | 23 % |
| Nora | 839 | 9,0 | 15 % | 2 % | **34 %** |
| Frau Silber (v. a. B4) | 54 | **22,1** | 5 % | 0 % | 11 % |
| Mutter | 49 | 12,0 | **30 %** | 4 % | 26 % |
| Pawlik (B3) | 46 | **19,4** | 17 % | 0 % | 15 % |
| Kloß (B2) | 57 | 10,3 | 7 % | 0 % | 31 % |
| Graven (B5) | 48 | 10,8 | 10 % | 4 % | 27 % |
| Faber (B4) | 17 | 19,1 | 23 % | 0 % | 5 % |
| Frau Held (B4–B5) | 14 | 19,4 | 14 % | 0 % | 14 % |

**Wie belastbar?** Das Skript erkennt den Sprecher am Begleitsatz (*sagte Theo*). Steht keiner da, nimmt es
den Wechsel im Hin und Her an. Rund **20 % der Reden** bleiben ohne Zuordnung. Stichproben zeigten
Fehlzuordnungen; die gröbste ist behoben (Silber wird in B4 nur „Silber" genannt und war zuerst Faber zugeschlagen).
Einzelne Fehler bleiben. Für Nora und
Theo sind die Zahlen wegen der Menge stabil. Für die Nebenfiguren sind es **Tendenzen**, keine Werte —
bei ihnen zählt das Nachlesen mehr als die Zahl.

**Drei Befunde, die für die ganze Übersetzung gelten:**
1. **Ausrufezeichen sind selten** (1–4 %). Die Reihe macht Spannung mit kurzen Sätzen, nicht mit „!".
   → Die Übersetzung **fügt keine Ausrufezeichen hinzu**. Prüfskript A11 zählt sie je Kapitel DE ↔ EN.
2. **Niemand flucht.** *Verdammt* kommt in fünf Bänden **genau einmal** vor (Pawlik, B3 K13 → *blasted*).
   → Kein *damn*, *hell*, *crap*, *sucks*. *Oh my God* nur, wenn das Original es sagt (Eltern-Rezensionen in den USA).
3. **Nora und Theo werden über die Reihe älter.** Theos Reden: B1 im Schnitt 7,8 Wörter, B4 15,0. Noras:
   8,4 → 12,6. → Band 1 auf Englisch **nicht** an Band 4 angleichen. Die Kinder in Band 1 klingen jünger.

---

## 1. Nora (12) — die Kontrolle

**Was sie ausmacht (belegt):**
- **Kurz.** Jede dritte Rede hat höchstens drei Wörter. Häufigste Anfänge: *Ja.* · *Ich weiß.* · *Theo.*
- *„Theo."* als ganzer Satz ist eine **Warnung** oder ein **Stopp** — kein Anruf.
- Rational, erklärt weg: *„Quatsch. Das ist ein Altbau. Die sehen alle so aus."* · *„Es gibt eine Erklärung."* (R26)
- Zu Erwachsenen höflich und vorsichtig, mit *Sie* und Gedankenstrich-Zögern:
  *„Entschuldigung. Wir wollten fragen — die alte U-Bahn da unten …"*
- Wenig Fragen (15 %). Sie **sagt**, was zu tun ist: *„Wir helfen ihr. Jetzt. Heute Nacht."*
- In B4/B5 längere, ernste Sätze. Sie bleibt aber sachlich, nie pathetisch.

**Auf Englisch:**
| Regel | Beispiel |
|---|---|
| Kurze Antworten bleiben kurz. *Ich weiß.* = *I know.* — nicht *I'm aware* oder *I know that.* | *„Ja." → “Yeah.”* (zu Theo) · *“Yes.”* (zu Erwachsenen) |
| *„Theo."* bleibt ein Wort mit Punkt. Kein *“Theo, stop.”* | *“Theo.”* |
| Kein Sarkasmus. Der gehört Theo. Nora ist genervt, nicht witzig. | *„Quatsch."* → **“Oh, come on.”** (Pilot entschieden: *That's silly* klang für den US-Lektor nach Lehrerin, D5 K1 #5) |
| Zu Erwachsenen: *Excuse me*, *Mr./Mrs.*, ganze Sätze. Das ersetzt das deutsche *Sie* (F27). | *“Excuse me. We wanted to ask — the old subway down there …”* |

**Gefahr bei der KI-Übersetzung:** Nora wird zur kühlen Erzählerin mit Erwachsenenwortschatz
(*rational explanation*, *logically*). Sie ist zwölf. Sie sagt *There's an explanation.*, nicht *There's a logical explanation for this.*

---

## 2. Theo (10) — der Angsthase mit dem Mundwerk

**Was er ausmacht (belegt):**
- Redet am meisten (922 Reden), fragt am meisten (24 %).
- Witz durch **Übertreibung und Filmvergleich**: *„Das ist der Teil im Film, wo alle sterben."* ·
  *„Das ist Kapitel eins von* Wir hätten zu Hause bleiben sollen*."* · *„Andere Kinder gehen nach Hause
  und spielen Videospiele. Wir ermitteln in Geisterfällen."*
- **Alltag als Maßstab:** *„Ich halte es ja nicht mal beim Zahnarzt im Wartezimmer aus."*
- Feste Sprüche (Register R40–R42): *Ich sag ja nur.* · *Weißt du, was komisch ist?* · *Ich will ja nichts sagen …*
- **Schaltet den Witz ab**, wenn es ernst wird — und der Text sagt es: *„Mach schon", sagte Theo. Kein Witz diesmal.*
- Ab B3 lange, kluge Reden in Schlüsselmomenten (B4 K10: *„Er räumt uns ein, Stück für Stück, bis wir
  auch nur noch Sachen auf einem Regal sind, mit einem Schild davor."*).
- Redet mit Schatten wie mit einem Menschen (B3 K7).

**Auf Englisch:**
| Regel | Beispiel |
|---|---|
| **Witz so lang wie im Original.** Nicht ausbauen, keine zweite Pointe anhängen. | *“This is the part in the movie where everybody dies.”* |
| Wortschatz eines Zehnjährigen. Kein *ironically*, *technically*, *literally* als Füllwort. | |
| Sprüche R40–R42 **immer gleich**. | *Just saying.* · *You know what's weird?* · *I'm not saying anything, but …* |
| *Kein Witz diesmal*-Stellen: Theo klingt dort schlicht. | *“Hurry up,” Theo said. No joke this time.* |
| Filmtitel-Witze: Titel erfinden, kursiv, im Stil eines US-Horrorfilms. | *“This is chapter one of* We Should Have Stayed Home*.”* |

**Gefahr bei der KI-Übersetzung:** Theo wird zum Sitcom-Kind mit Pointen im Sekundentakt
(*“Oh great. Just great.”* an jeder Ecke). Im Original ist er **ängstlich zuerst, witzig als Abwehr**.
Prüfung D5 fragt bei jeder Theo-Pointe: *Steht die im Original?*

---

## 3. Die Mutter — „Mom"

**Was sie ausmacht:** Hat **keinen Vornamen** (Kanon). Fragt viel (30 %), ist die Einzige mit
Ausrufen (*„Und? Platz! Hohe Decken! Charme!"*). Müde vom Schichtdienst, liebevoll, merkt nichts vom
Übernatürlichen. Redensarten einer Erwachsenen: *„um Himmels willen"*. In B4 K16 der eine lange, weise
Absatz über ihre Mutter (Register R17 *Loslassen heißt nicht vergessen*).

**Auf Englisch (geändert nach Pilot):** Kinder **und Erzähltext** sagen **Mom** — auch dort, wo das Original *ihre Mutter* schreibt. *their mother* nur ausnahmsweise, wenn ein Satz sonst unklar wird. **Warum geändert:** Die erste Fassung dieser Regel (Wechsel wie im Original) war im Pilot das **auffälligste Übersetzungszeichen** überhaupt (D5 K1: „single biggest giveaway", ~11× *their mother* in einem Kapitel). Im Deutschen ist *ihre Mutter* neutral, im US-Kinderbuch klingt *their mother* kühl und fern. Die Regel widersprach außerdem dem Glossar A1 (*Mom* in Anrede **und** Erzählung). Alte Fassung: das Original wechselt
(74× *Mama*, 71× *Mutter*); den Wechsel beibehalten. *um Himmels willen* → *for heaven's sake*.
Ihre Ausrufe **dürfen** bleiben — sie ist die eine Figur, die so redet.

**Gefahr:** Ein Vorname rutscht hinein (Planungsunterlagen nannten sie „Sarah"). **Nie.**

---

## 4. Lina Vogt (Tagebuch, 1974, 12 Jahre)

**Was sie ausmacht:** Datierte Einträge (*„17. September."*), kurze Sätze, Wiederholung als Gefühl:
*„Ich habe Angst. Ich habe richtige Angst. Niemand glaubt mir."* Alltag zuerst (Mathe, Frau Kettner,
Hanna, ihr Hund Luna), dann das kalte Zimmer. Lila Tinte, *„weil das meine Lieblingsfarbe ist"*.

**Auf Englisch:**
- Datum US-Stil: *September 17.* (nicht *17 September*).
- Kurze Sätze, Wiederholung behalten: *“I'm scared. I'm really scared. Nobody believes me.”* (R27)
- **Kein Wort, das es 1974 nicht gab** und kein heutiger Jugendslang: kein *like* als Füllwort, kein
  *awesome*, *cool* nur sparsam, kein *OMG*. Auch kein gespieltes 70er-Slang (*far out*, *groovy*) —
  das wäre Verkleidung. Schlicht schreiben, dann klingt es zeitlos.
- *Mama* im Tagebuch → **Mom** (ein Kind von 1974 in einer US-Ausgabe). *Oma* → **Grandma**.

---

## 5. Margret Silber — geschriebene und gesprochene Stimme

**Was sie ausmacht:** In B1–B3 nur Notizbuch und Brief; in **B4** spricht sie (54 Reden) — mit den **längsten
Reden der Reihe** (Ø 22 Wörter), fast ohne Fragen. Sie erklärt, sie fragt nicht. **Vollständige, ruhige Sätze**, Merksätze
mit Wiederholung: *„Die Unruhigen brauchen jemanden, der ihre Geschichte versteht. Nicht nur kennt.
Versteht."* (R3). Knappe Fall-Notizen: *„Anna Berger, 1923. Ertrunken im Kanal. Wollte nur, dass
jemand ihren Namen kennt. Drei Nächte."* Gesprochen (B4 K15): *„Nein, Kind. Ich bin so müde. Vierzig Jahre müde."*

**Auf Englisch:**
- Im Notizbuch und Brief **keine Kurzformen**: *I am*, *do not*, *it is*. Das unterscheidet sie
  sofort von den Kindern (Register R2: *If you are reading this, I am no longer here.*).
- Fall-Notizen im Telegrammstil lassen: *“Anna Berger, 1923. Drowned in the canal. Only wanted someone to know her name. Three nights.”*
- **Gesprochen (B4)** ist sie wärmer, aber ebenso vollständig: Kurzformen sparsam, nie Slang.
- *Kind* (Anrede) → **child**. Klingt im Englischen altmodisch — gewollt; Faber benutzt es auch.
- Nora liest vor: deutsche Anführung im Zitat *„‚…'"* → US *“‘…’”*.

---

## 6. Frau Held — die Nachbarin (ab B4 tragend)

**Was sie ausmacht:** Lange Sätze, mit *und* aneinandergereiht (Ø 19 Wörter), wie jemand, der gern
erzählt. Klatsch-Ton: **„die Silber"** (Artikel vor dem Nachnamen). Rhetorische Fragen: *„Das ist die
Frage, nicht wahr."* · *„Erklärt mir das mal, ihr Klugen."* Nennt Nora *Kind*.

**Auf Englisch:**
- *„die Silber"* → **Silber** ohne *Mrs.* — die einzige erlaubte Ausnahme von Glossar E8. Das Weglassen
  der Anrede macht im Englischen dasselbe wie der Artikel im Deutschen: vertraut, ein bisschen respektlos.
- Lange *and*-Ketten **nicht** in kurze Sätze zerhacken. Ihr Redefluss ist ihre Stimme.
- *ihr Klugen* → *you smart ones* oder *smarty-pants* — Pilot entscheidet.

---

## 7. Erwachsene Nebenfiguren

| Figur | Band | Was sie ausmacht | Auf Englisch |
|---|---|---|---|
| **Kloß** (Friedhofsverwalter) | B2 | Amtlich, stockend, mit Gedankenstrichen: *„die Aufzeichnungen aus dieser Zeit sind — lückenhaft."* Fast keine Umgangssprache. Schuldbewusst. | Wenige Kurzformen, Amtswörter **einfach** halten (*records*, *spotty*). Die Pausen (— und …) behalten. |
| **Pawlik** (alter U-Bahn-Mann) | B3 | Längste Reden der Reihe (Ø 19 Wörter), Beichte in Schüben. Umgangssprache (*hab*, *geh*), Wiederholung: *„Ich geh da nicht rein. Nie wieder."* · *„Ich hab gedacht, einmal macht nichts."* | Kurzformen, schlichter Arbeiter-Ton: *“I figured once wouldn't hurt.”* Fluch: *blasted* (A1). **Kein** Dialekt, kein *ain't*. |
| **Faber** (der Sammler, Geist) | B4 | Lange, fast poetische Sätze, *„verstehst du"*, *„Kind"*. Paradoxe: *„Ich habe sie weggeliebt."* | *you see* · *child*. Die Neuschöpfung **behalten**: *“I loved them away.”* — nicht glätten zu *I wore them out with love*. |
| **Graven** (der Erste) | B5 | **Ruhig, knapp, überlegen.** Befehle ohne Bitte: *„Morgen. Bring den Hund."* Herablassend freundlich: *„Ihr seid Kinder. Kinder versuchen es immer."* Nie laut. | **Keine Kurzformen** (er ist von 1823). Keine Bösewicht-Theatralik, kein Lachen, kein *foolish children*. Je ruhiger, desto unheimlicher (Motto R10: *der sich ganz sicher ist*). |

---

## 8. Geister ohne Stimme

Die meisten Geister sprechen nicht — sie **schreiben** (Kondenswasser, Tinte, Ritzung) oder klopfen.
Das ist im Glossar (E11, Großbuchstaben) und im Satz-Register geregelt. Regel für A2: **Geisterschrift
bekommt nie Satzzeichen, die das Original nicht hat**, und nie mehr Wörter.

---

## 9. Nebenfund im Original

| Band | Stelle | Befund |
|---|---|---|
| B4 | K16 (Kapitel_16.md Z. 51) | Szenentrenner `---` **mitten im Gespräch**: zwischen Theos Frage *„Hat's funktioniert?"* und Mamas Antwort *„Nein …"*. Wenn Absicht (Pause): im Satzbild ungewöhnlich, Leser denken an einen Ortswechsel. Wenn Versehen: entfernen. [prüfen] — Die Übersetzung übernimmt das Original. |

---

## 10. Wie diese Seite benutzt wird

- **D2 (Übersetzen):** Diese Seite steht im Stil-Brief (A8) als Anhang.
- **D5 (US-Lektor):** prüft je Kapitel drei Reden pro Hauptfigur gegen die Regeln oben.
- **A11 (Prüfskript):** misst Ausrufezeichen, Flüche, Kurzformen bei Silber/Graven, Länge von Noras und
  Theos Reden DE ↔ EN je Band.
- **Pilot (K1, K9):** entscheidet die mit „Pilot entscheidet" markierten Fälle und trägt sie hier ein.
