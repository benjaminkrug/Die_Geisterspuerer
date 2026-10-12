# Vorgehensplan — Englische Ausgabe der Geisterspürer

> **Fassung 2, 2026-10-12.** Ersetzt Fassung 1 vom selben Tag.
> **Schwerpunkt dieser Fassung: eine bessere Übersetzung.** Fassung 1 hat vor allem geregelt,
> *wann* Geld ausgegeben wird. Fassung 2 regelt zusätzlich, *wie* die Übersetzung so gut wird,
> dass niemand merkt, dass es eine ist.
>
> Baut auf `Internationalisierung_Analyse.md` auf und ersetzt deren Abschnitt 7.
> Berücksichtigt den Umbau von Band 1 (Branch `ccr-c33fc6fe-peyki0`).
>
> ⚠️ Kosten und Termine sind Schätzungen. Was mit **[prüfen]** markiert ist, muss vor der
> Entscheidung bestätigt werden.

---

## 0. Kurzfassung

**Was sich gegenüber Fassung 1 ändert:**

| | Fassung 1 | Fassung 2 |
|---|---|---|
| Wer prüft die KI-Übersetzung? | **Ein** englischer Lektor (liest nur Englisch) | **Zwei Rollen:** ein **zweisprachiger Übersetzer** vergleicht mit dem deutschen Original, danach ein **englischer Kinderbuch-Lektor** für Klang und Kinder-Tauglichkeit |
| Wie wird der Weg gewählt? | Probe-Lektorat Kap. 1 | **Blinder Probe-Vergleich** an zwei Textstellen: KI + Überarbeitung **gegen** komplett menschliche Übersetzung. Bewerter wissen nicht, was was ist. |
| Vorbereitung | Glossar + Stil-Brief | **Übersetzungs-Bibel:** Glossar, Stimmen der Figuren, Witz-Liste, Motiv-Liste, Satz-Register über alle 5 Bände, Fallen-Liste |
| KI-Übersetzung | Ein Durchgang pro Kapitel | **Vier Durchgänge** (verstehen → übersetzen → rückübersetzen und vergleichen → Konsistenz) mit dem ganzen Buch im Blick |
| Lernen | – | **Änderungsquote** pro Kapitel messen; jede Korrektur fließt in die Bibel; Aufwand für spätere Bände sinkt messbar |
| Kosten B1+B2 | ca. 1.750–3.450 € | **ca. 3.800–6.200 €** |

**Die wichtigste Einzelentscheidung:** Ein Lektor, der kein Deutsch kann, findet keine
**Bedeutungsfehler** — er sieht nur, ob der englische Satz gut klingt. Ein schön klingender
falscher Satz rutscht durch. Deshalb braucht es eine Person, die **beide Sprachen** liest.

---

## 1. Was heißt „gute Übersetzung" bei dieser Reihe?

Ohne Maßstab kann man nicht prüfen. Fünf Kriterien, jedes mit einem Prüfer:

| # | Kriterium | Woran man es merkt | Wer prüft |
|---|---|---|---|
| Q1 | **Bedeutung stimmt** | Keine Information verloren, verdreht oder dazuerfunden. Hinweise (Setups) und Auflösungen (Payoffs) sitzen an derselben Stelle. | Zweisprachiger Überarbeiter + Rückübersetzung (Claude) |
| Q2 | **Klingt wie ein US-Kinderbuch** | Kein „übersetzt"-Gefühl. Ein US-Lektor würde nicht merken, dass es ein Original auf Deutsch gab. | Englischer Kinderbuch-Lektor |
| Q3 | **Ton und Rhythmus bleiben** | Grusel → Witz innerhalb 1–2 Absätzen. Kurze Schock-Absätze bleiben kurz. Theo ist witzig, Nora ist sachlich. Kapitelenden ziehen. | Lektor + Kinder-Testleser |
| Q4 | **Konsistent** | Namen, Begriffe, wiederkehrende Sätze identisch — innerhalb des Bandes **und über alle 5 Bände**. | Prüfskript (Claude) |
| Q5 | **Lesbar für 9–12** | Lesbarkeitswert im Zielbereich (Flesch-Kincaid ca. Klasse 4–6 [prüfen an US-Vergleichstiteln]), keine Wörter, die Kinder nicht kennen. | Prüfskript + Testleser |

**Wichtig:** Q1 und Q2 widersprechen sich manchmal. Wörtlich = Q1 gut, Q2 schlecht. Frei = umgekehrt.
**Regel für die Reihe:** Bei Handlung, Hinweisen und Fakten gewinnt Q1. Bei Witzen, Redewendungen
und Rhythmus gewinnt Q2 — *die Wirkung* muss gleich sein, nicht die Wörter.

---

## 2. Warum Übersetzungen bei dieser Reihe schiefgehen können — konkrete Fallen aus Band 1

Diese Liste zeigt, dass „gut übersetzen" hier mehr ist als Sprachkenntnis. Sie wird in Phase A
für alle Bände vervollständigt.

| # | Stelle (Band 1, neue Fassung) | Falle | Lösungsrichtung |
|---|---|---|---|
| F1 | Kap. 4: *„Kondenswasser schreibt keine deutschen Wörter!"* | Der Witz bezieht sich auf die **Sprache selbst**. „German words" wäre im Englischen absurd. | „Condensation doesn't **spell**!" o. ä. — Witz neu bauen |
| F2 | Wörter im Kondenswasser: HILF · HIER · VERGISS NICHT · TAGEBUCH · LIES · BITTE · DANKE · OBEN | Müssen kurz, kindlich, mit dem Finger schreibbar sein. Kap. 12 hat **vier Wörter auf vier Fenstern**. | HELP · HERE · DON'T FORGET · DIARY · READ · PLEASE · THANK YOU · UP — Länge und Wirkung prüfen |
| F3 | Kap. 3: *„Es gibt eine Erklärung"* + Theo: *„Du sagst das jetzt zum dritten Mal"* | Der Witz funktioniert nur, wenn der Satz **dreimal gleich** übersetzt ist. | Satz-Register (Abschnitt 3, B5) |
| F4 | *„Klopf. Klopf. Klopf. Pause."* (Kap. 2, 3, 11) | Rhythmus-Motiv, kehrt gesteigert wieder. | „Knock. Knock. Knock. Pause." — überall identisch |
| F5 | Kap. 12: *„Einen Schatten. Aber nicht unseren Schatten."* | Hundename = normales Wort. | Im Englischen sogar besser: „A shadow. But not our Shadow." — **Großschreibung konsequent** |
| F6 | Kap. 1: *„Altbau heißt alt. Alt heißt gruselig."* | „Altbau" gibt es im Englischen nicht. | „Old house means old. Old means haunted." |
| F7 | Kap. 6: *„Mikrofiche." – „Gesundheit."* | Funktioniert **wörtlich** („Bless you."). | Beispiel, dass nicht alles umgebaut werden muss — Überarbeiter darf nicht „überübersetzen" |
| F8 | Kap. 2/3: *„zehn Grad"*, *„dreißig Kilo"*, *„drei mal vier Meter"* | US-Kinder denken in °F, Pfund, Fuß. | Zahlen meist durch Bild ersetzen („the temperature dropped like a stone"), Rest umrechnen |
| F9 | Kap. 9: Linas Tagebuch (1974, 12 Jahre) | Stimme eines Mädchens **von 1974** — kein moderner Slang. | Eigener Stimm-Eintrag in der Bibel |
| F10 | Frau Silbers Notizbuch und Brief | Ältere, ruhige Erwachsenenstimme. Wird in **Band 4 und 5 zitiert** (*„Bei Lina … hatte Verstehen den Geist gehen lassen"*). | Satz-Register über alle Bände, sonst stimmt das Zitat in Band 4 nicht |
| F11 | *„Frau Silber"*, *„Frau Kettner"*, *„Frau Held"* | „Frau" behalten (Flair) oder „Mrs." (verständlich)? | Entscheidung im Glossar, dann **überall gleich** |
| F12 | Kap. 3: *„Das hört man wahrscheinlich in Hamburg."* | Ortsbezug. Bleibt, weil die Reihe in Deutschland spielt — aber US-Kinder kennen Hamburg kaum. | Überarbeiter entscheidet; Regel: deutsche Orte nur, wo sie ohne Erklärung funktionieren |

---

## 3. Der Plan auf einen Blick

```
PHASE A  Übersetzungs-Bibel (Okt–Nov 2026)                    0 €   ┐ parallel
PHASE B  Deutsche Fassung Band 1 festmachen (Okt–Nov 2026)     –    ┘
   ◆ PRÜFPUNKT 1 (ca. Mitte Jan 2027): Wirkt der Umbau in DE?
PHASE C  Blinder Probe-Vergleich + Team wählen (Dez–Feb)    ~0,6–1 T€
PHASE D  Band 1 übersetzen — der Qualitäts-Maßstab (Feb–Apr)
PHASE E  Band 2 übersetzen — mit gelernter Bibel (Apr–Mai)
PHASE F  Produktion EN (parallel)
PHASE G  Launch B1 (Juni) + B2 (Juli 2027)
   ◆ PRÜFPUNKT 2 (ca. Ende Aug 2027): Trägt Englisch? Wie hoch ist die Änderungsquote?
PHASE H  Band 3–5 — Aufwand je nach Änderungsquote (Sept 2027 – Jan 2028)
```

**Zeitplan-Änderung gegenüber Fassung 1:** Das gründlichere Verfahren kostet etwa **6–8 Wochen**.
Die Halloween-Saison 2027 wird damit **nur mit Band 1 + 2** erreicht, nicht mit der ganzen Reihe.
Begründung und Gegenargument in Abschnitt 8.2.

---

## 4. Phasen im Detail

### Phase A — Die Übersetzungs-Bibel (Okt–Nov 2026, 0 €)

Eine Übersetzung ist nur so gut wie das, was der Übersetzer über das Buch **weiß**. Die Reihe hat
dafür schon viel Material (`Serien_Kanon.md`, `Stimmen_Pruefplan.md`, `Setup_Payoff_Tracker.md`,
`Cliffhanger_Register.md`). Daraus wird **eine** englische Arbeitsgrundlage.

| # | Teil der Bibel | Inhalt | Warum |
|---|---|---|---|
| A1 | **Glossar** | Reihentitel, Bandtitel, Namen, Orte, feste Begriffe (*die Unruhigen, der Schleier, der Erste, Hüterin*), Codewörter — je mit Entscheidung und Begründung | Q4. Spätere Änderung = teuer. |
| A2 | **Stimmen** | Für Nora, Theo, Mama, Lina (1974), Frau Silber, Frau Held: wie sprechen sie? Satzlänge, Lieblingswörter, was sie **nie** sagen würden. Je 3 Beispielsätze DE → EN | Q3. Stimmen sind das Erste, was in Übersetzungen verloren geht. |
| A3 | **Witz-Liste** | Jeder Theo-Witz in Band 1 mit **Funktion** (Entlastung nach Grusel? Charakter? Callback?) und Typ (übertragbar / umbauen / ersetzen) | Q2/Q3. Der Überarbeiter weiß, *wozu* der Witz da ist, und kann gleichwertig ersetzen. |
| A4 | **Motiv-Liste** | Wiederkehrende Bilder und Laute: Klopfen, metallischer Geschmack, Bernsteinaugen, Kondenswasser, lila Tinte, Schattens Signale (Fell, Knurren, Winseln) | Q4. Motive müssen gleich klingen, damit Leser sie wiedererkennen. |
| A5 | **Satz-Register** | Alle Sätze, die **wörtlich wiederkehren** — im Band und über Bände (Silbers Notizbuch, „Es gibt eine Erklärung", Codewörter, Briefzitate). Englische Fassung wird **einmal** festgelegt. | Q1/Q4. Siehe F3, F10. |
| A6 | **Fallen-Liste** | Abschnitt 2, für alle 5 Bände vervollständigt | Q1/Q2 |
| A7 | **Szenen-Absicht** | Pro Kapitel 3–5 Zeilen: Was muss das Kapitel beim Leser auslösen? (Schreck, Lachen, Hinweis, Rührung) + das Kapitelende | Q3. Der Überarbeiter kann frei formulieren, ohne die Wirkung zu verlieren. |
| A8 | **Stil-Brief EN** | Die Stilregeln der Reihe für Englisch: „said"-Regel, Satzlänge nach Lesbarkeit statt Wortzahl, Absatzlänge, Anführungszeichen, US-Schreibweise | Q2/Q5 |
| A9 | **US-Vergleichstexte** | 3–5 erfolgreiche US-Middle-Grade-Grusel-Titel: Lesbarkeitswerte, Dialoganteil, typische Formulierungen | Q2/Q5. Gibt dem Prüfskript echte Zielwerte statt geschätzter. |
| A10 | **Titelprüfung + US-Marktanalyse** | wie Fassung 1 | Markt, nicht Übersetzung — bleibt aber in A, weil kostenlos |

**Ergebnis:** `Dokumentation/EN_Bibel/` (Glossar, Stimmen, Witze, Motive, Register, Fallen, Absichten, Stil-Brief)
und `Dokumentation/EN_Marktanalyse_USA.md`.

**Wer:** Claude erstellt alles. **Autor entscheidet** Glossar (A1) und prüft die Szenen-Absichten (A7) —
nur der Autor weiß sicher, was eine Szene soll.

### Phase B — Deutsche Fassung festmachen (Okt–Nov 2026)

Unverändert aus Fassung 1: 11 Fehler beheben, Testleser DE, KDP-Frage, Upload.
**Neu:** Danach wird Band 1 DE für die Übersetzung **eingefroren**. Spätere deutsche Änderungen
kommen in eine Änderungsliste und werden gezielt nachgezogen.

### ◆ Prüfpunkt 1 — Wirkt der Umbau? (ca. Mitte Jan 2027)

Unverändert aus Fassung 1: weiter, wenn B1→B2 (DE) **≥ 30 %** oder **+10 Prozentpunkte**;
Stopp bei unverändert **< 20 %**. Phase A ist in jedem Fall nicht verloren.

### Phase C — Blinder Probe-Vergleich und Team wählen (Dez 2026 – Feb 2027)

Das ist der **Kern der Überarbeitung**. Statt zu raten, welcher Weg die bessere Übersetzung liefert,
wird es an echtem Text gemessen.

**C1 — Zwei Probestellen** (zusammen ca. 2.500 Wörter):
- **Kap. 1 komplett** (~1.550 W): Theos Humor, Atmosphäre, Einstieg — hier entscheidet sich der Kauf (Leseprobe!).
- **Kap. 9, Tagebuch-Teil** (~1.000 W): Linas 1974-Stimme, Gefühl, Grusel. Die schwerste Stelle des Buches.

**C2 — Kandidaten suchen** (Autor, Claude schreibt die Ausschreibung):
- **Rolle 1 — Zweisprachiger Überarbeiter:** Literaturübersetzer DE→EN, Muttersprache Englisch,
  Erfahrung mit Kinder-/Jugendbuch. Verbände und Verzeichnisse [prüfen: z. B. ATA, ALTA, Society of
  Authors Translators Association, Reedsy-Übersetzer].
- **Rolle 2 — Kinderbuch-Lektor:** US-Muttersprachler, Middle Grade, idealerweise Spooky/Horror.

**C3 — Drei Fassungen derselben Probestellen:**

| Fassung | Wie entsteht sie | Was sie testet |
|---|---|---|
| **X** | KI-Entwurf (Claude, mit Bibel) → **Überarbeiter-Kandidat 1** überarbeitet frei gegen das Original | Weg „KI + Profi" |
| **Y** | KI-Entwurf → **Überarbeiter-Kandidat 2** | Unterschied zwischen Personen |
| **Z** | **Ein Übersetzer übersetzt ohne KI**, nur mit Bibel | Weg „komplett menschlich" (Analyse Option A) |

**C4 — Blinde Bewertung:**
- **Lektor-Kandidaten** (Rolle 2) bekommen X, Y, Z ohne Hinweis, wie sie entstanden sind, und
  bewerten nach Q2, Q3, Q5 mit einem festen Bogen (Claude erstellt ihn).
- **Claude** bewertet Q1 per Rückübersetzung: Wo weicht der Sinn vom Original ab?
- **Wenn möglich: 3–5 englischsprachige Kinder** lesen die drei Fassungen von Kap. 1 und sagen,
  welche sie weiterlesen wollen.

**C5 — Entscheidung (Autor)** nach diesem Schema:

| Ergebnis | Weg für das ganze Projekt |
|---|---|
| X oder Y **gleich gut** wie Z (oder besser) | **KI + Überarbeiter** — der beste der beiden wird genommen |
| Z **klar besser** (Lektoren und Kinder bevorzugen Z deutlich) | **Komplett menschliche Übersetzung**, KI nur für Konsistenz-Prüfung — teurer, aber die bessere Übersetzung ist der Zweck dieser Fassung |
| Alle drei schwach | Kandidaten waren falsch → neue suchen, **nicht** mit schwachem Team starten |

**C6 — Verträge:** Festpreis pro Band, Termine, Query-Runde inklusive, **vollständige Übertragung aller
Nutzungsrechte** (Buy-out). Übersetzer im Impressum nennen. [prüfen: Rechtslage, falls der Übersetzer
in Deutschland sitzt — dort gibt es einen gesetzlichen Anspruch auf angemessene Vergütung]

### Phase D — Band 1 übersetzen: der Qualitäts-Maßstab (Feb – Apr 2027)

Band 1 ist der Einstieg und die Leseprobe. Hier wird **nicht** gespart.

**D1 — KI-Entwurf in vier Durchgängen** (Claude, gilt nur für den Weg „KI + Überarbeiter"):

```
Durchgang 1  VERSTEHEN    Ganzes Buch lesen. Pro Kapitel Abgleich mit Szenen-Absicht (A7):
                          Wo sind Witze, Hinweise, Motive, Register-Sätze?
Durchgang 2  ÜBERSETZEN   Kapitelweise, mit dem GANZEN Buch und der Bibel im Kontext.
                          Bei jeder freien Lösung: Randnotiz „frei, weil …"
Durchgang 3  RÜCKPRÜFEN   Englisch → Deutsch zurückübersetzen und mit dem Original
                          vergleichen. Jede Abweichung: gewollt (Randnotiz) oder Fehler?
Durchgang 4  KONSISTENZ   Prüfskript: Glossar, Register-Sätze, Motive, Schatten je Kapitel,
                          Kapitelenden, Lesbarkeit je Kapitel gegen US-Zielwerte (A9)
```

Die Randnotizen gehen **mit** an den Überarbeiter. Er sieht so, wo die KI bewusst frei war und
wo sie unsicher war.

**D2 — Überarbeitung gegen das Original** (Rolle 1): Satz für Satz mit dem deutschen Text daneben.
**Darf frei umformulieren** — ausdrücklich im Auftrag, damit der KI-Satzbau nicht stehen bleibt
(siehe Abschnitt 8.3).

**D3 — Query-Runde:** Der Überarbeiter sammelt Fragen („Soll das unheimlich oder lustig sein?").
Claude beantwortet aus Bibel und Kanon, **Autor** entscheidet bei Absichtsfragen.
Ziel: eine Runde pro Band, nicht laufende Einzel-Mails.

**D4 — Lektorat** (Rolle 2): Nur Englisch lesen, wie ein US-Leser. Q2, Q3, Q5.
**Kommentiert, schreibt nicht um.** Der Überarbeiter setzt die Kommentare um — so bleibt
**eine** Stimme im Buch (siehe 8.4).

**D5 — Englische Testleser:** 3–5 Kinder 9–12, Fragebogen wie im deutschen Testleser-Bogen
(wo aufgehört, welche Stelle lustig, welche gruselig, welche langweilig). **Plus Vorlese-Test:**
Ein Elternteil liest Kap. 1 laut vor — holprige Sätze fallen beim Vorlesen sofort auf.

**D6 — Korrektorat** (dritte Person oder ein zweiter, getrennter Durchgang).

**D7 — Lernschleife:** Jede Korrektur aus D2–D6 wird einsortiert (Glossar? Stimme? Witz? Grammatik?)
und **in die Bibel übernommen**. Claude misst die **Änderungsquote**: Anteil der Sätze, die der
Überarbeiter geändert hat — pro Kapitel und gesamt.

### Phase E — Band 2: mit gelernter Bibel (Apr – Mai 2027)

Gleicher Ablauf wie D, ohne Testleser. **Erwartung:** Die Änderungsquote sinkt gegenüber Band 1,
weil die Bibel jetzt die Korrekturen aus Band 1 enthält.
**Wenn sie nicht sinkt:** Ursache klären, bevor Band 3–5 beauftragt werden (Abschnitt 8.6).

### Phase F — Produktion (parallel zu D/E)

Unverändert aus Fassung 1: Build-Skripte mit Sprache, Cover EN, Anhang mit Leseprobe B2 EN und
QR auf Amazon.com, KDP-Texte **neu geschrieben** (nicht übersetzt), A+ Content.
**Neu:** Der Überarbeiter liest Klappentext und Leseprobe gegen — dort entscheidet sich der Kauf.

### Phase G — Launch (Juni/Juli 2027)

B1 im Juni, B2 im Juli. Rezensionen sammeln, kleine Ads. KI-Hinweis bei KDP: Wenn der Weg
„KI + Überarbeiter" gewählt wurde → **„Übersetzung: KI-generiert" angeben**, auch nach Überarbeitung
[prüfen: aktueller KDP-Wortlaut].

### ◆ Prüfpunkt 2 — Trägt Englisch? (ca. Ende Aug 2027)

Wie Fassung 1 (Durchlesequote EN, Rezensionen, Ads) — **plus ein Qualitätssignal:**
Wird in Rezensionen die Übersetzung erwähnt? Ein einziges „feels translated" ist ein Warnsignal,
das vor Band 3 behoben werden muss.

### Phase H — Band 3–5: Aufwand nach Änderungsquote (Sept 2027 – Jan 2028)

| Änderungsquote Band 2 | Verfahren Band 3–5 |
|---|---|
| **niedrig** (Überarbeiter ändert weniger als jeden 5. Satz) | KI-Entwurf + Überarbeiter + Korrektorat. Lektorat nur stichprobenartig (1. und letztes Drittel). |
| **mittel** | Volles Verfahren wie Band 2 |
| **hoch** (mehr als jeden 3. Satz) | Prüfen, ob für Band 3–5 der Weg „komplett menschlich" günstiger **und** besser ist |

Die Schwellen sind Startwerte; nach Band 1 und 2 mit echten Zahlen neu setzen.

---

## 5. Wer macht was

| Aufgabe | Claude | Autor | Überarbeiter (zweisprachig) | Lektor (US) |
|---|---|---|---|---|
| Übersetzungs-Bibel | erstellt | entscheidet Glossar, prüft Absichten | ergänzt in D2 | – |
| KI-Entwurf + Rückprüfung + Prüfskript | ✅ | – | – | – |
| Überarbeitung gegen Original | – | – | ✅ **verantwortet die Stimme** | – |
| Query-Antworten | aus Kanon | bei Absicht | fragt | – |
| Lektorat (Klang, Kinder) | – | – | setzt um | ✅ kommentiert |
| Probe-Vergleich auswerten | Q1, Bogen | **entscheidet** | Kandidat | bewertet blind |
| Testleser EN finden | Fragebogen | ✅ | – | evtl. Kontakte |
| Verträge, Zahlungen, KDP, Ads | Vorbereitung | ✅ | – | – |

---

## 6. Kosten (Schätzung — Angebote einholen)

| Posten | B1 + B2 (~41.000 W) | B3–B5 (~50.500 W) |
|---|---|---|
| Phase A (Bibel, Marktanalyse) | 0 € | – |
| Probe-Vergleich (3 Fassungen à ~2.500 W + 2–3 Bewertungen) | ca. 600–1.000 € | – |
| Überarbeitung gegen Original (ca. 0,05–0,08 €/W) [prüfen] | ca. 2.050–3.300 € | ca. 1.500–4.000 €* |
| Lektorat (ca. 0,02–0,03 €/W, nur Kommentare) | ca. 800–1.250 € | ca. 0–1.500 €* |
| Korrektorat | ca. 300–500 € | ca. 400–700 € |
| Testleser EN | ca. 50–150 € | – |
| **Summe ohne Ads** | **ca. 3.800–6.200 €** | **ca. 1.900–6.200 €*** |
| *zum Vergleich:* komplett menschliche Übersetzung (ca. 0,10–0,15 €/W) | ca. 4.100–6.150 € + Lektorat | ca. 5.050–7.600 € + Lektorat |

\* je nach Änderungsquote (Phase H).

**Ehrliche Einordnung:** Für Band 1 + 2 liegt der Weg „KI + Überarbeiter" **nicht mehr deutlich
billiger** als eine komplett menschliche Übersetzung. Der Vorteil liegt in der **Geschwindigkeit**,
in der **Konsistenz über 5 Bände** (Prüfskript, Register) und darin, dass die Kosten bei Band 3–5
sinken können. Deshalb ist der Probe-Vergleich (C) so wichtig: Er entscheidet nach Qualität, nicht
nach Preis.

**Was muss verkauft werden?** Grob ~3 $ Tantieme pro Exemplar (Taschenbuch $9.99 oder E-Book $3.99,
Werte [prüfen]). ~5.000 € für B1+B2 entsprechen **etwa 1.800 verkauften Exemplaren**, Ads noch nicht
eingerechnet. Zum Vergleich: Band 1 DE hat in 71 Tagen 636 Exemplare verkauft. **Die englische
Ausgabe ist eine Investition über 1–2 Jahre, kein schneller Gewinn.**

---

## 7. Begründung der wichtigsten Entscheidungen

| Entscheidung | Begründung |
|---|---|
| **Zweisprachiger Überarbeiter statt nur US-Lektor** | Nur wer das Original liest, findet Bedeutungsfehler (Q1). Ein Hinweis, der falsch übersetzt ist, zerstört eine Auflösung drei Kapitel später — das merkt ein rein englischer Lektor nicht. |
| **Zusätzlich US-Kinderbuch-Lektor** | Übersetzer sind oft sehr gut in Treue, nicht unbedingt im Gefühl für 10-Jährige in den USA (Q2, Q5). Zwei Blickwinkel, zwei Personen. |
| **Blinder Probe-Vergleich mit menschlicher Übersetzung** | Die Frage „KI + Mensch oder nur Mensch?" ist eine Qualitätsfrage. Sie lässt sich nur am Text beantworten, nicht am Preis und nicht durch meine Einschätzung (siehe 8.1). |
| **Probe an Kap. 1 und Kap. 9** | Kap. 1 = Kaufentscheidung (Leseprobe). Kap. 9 = schwierigste Stimme (Lina 1974) und Gefühl. Wer beides kann, kann das Buch. |
| **Übersetzungs-Bibel** | Die Reihe lebt von Stimmen, Witzen und Motiven über 5 Bände. Ohne schriftliche Grundlage entscheidet jeder Beteiligte jedes Mal neu — und unterschiedlich. |
| **Vier KI-Durchgänge mit ganzem Buch im Blick** | Kapitelweise isoliert übersetzt, gehen Rückgriffe verloren (Klopfen in Kap. 11, Tagebuch in Kap. 13). Die Rückübersetzung findet Sinnfehler, bevor ein Mensch dafür bezahlt wird. |
| **Lektor kommentiert, Überarbeiter schreibt** | Eine Stimme im Buch. Wenn zwei Personen umschreiben, klingt das Buch wie zwei Bücher. |
| **Änderungsquote messen** | Macht Qualität und Aufwand sichtbar. Ohne Zahl kann man nicht entscheiden, wie viel Prüfung Band 3–5 brauchen. |
| **Band 1 ohne Sparen** | Band 1 ist der Einstieg und die Leseprobe. Ein Fehler hier kostet die ganze Reihe; ein Fehler in Band 4 kostet einen Band. |

---

## 8. Kritische Hinterfragung

### 8.1 „Ist Claude hier neutral?"

**Nein.** Claude würde den KI-Entwurf schreiben und schlägt einen Weg vor, in dem dieser Entwurf
vorkommt. **Deshalb** enthält der Plan Fassung Z (komplett menschlich) im blinden Vergleich und eine
klare Regel, wann Z gewinnt. Die Bewertung machen Lektoren und Kinder, nicht Claude. Claude bewertet
nur Q1 per Rückübersetzung — und das auch für Fassung Z, also gegen das eigene Interesse.

### 8.2 „Lohnt sich die Verzögerung? Halloween 2027 nur mit zwei Bänden."

**Gegenargument:** Fassung 1 hätte die ganze Reihe zu Halloween 2027 geschafft. Jetzt sind es nur
Band 1 + 2. Eine Saison ist ein Jahr.

**Prüfung:** Zwei Bände zur Saison sind als **Einstieg** ausreichend — wer B1+B2 im Oktober kauft,
kauft B3–B5 im Winter. Eine schnellere, schlechtere Übersetzung würde dagegen dauerhaft schaden:
Erste Rezensionen bleiben für immer stehen, und „schlecht übersetzt" ist bei Eltern ein
Ausschlussgrund. **Ergebnis:** Verzögerung akzeptiert. Wenn der Probe-Vergleich früh fertig ist,
kann Phase D vorgezogen werden.

### 8.3 „Macht ein KI-Entwurf die Übersetzung nicht sogar schlechter?"

**Ernstzunehmendes Gegenargument.** Wer einen fertigen Entwurf überarbeitet, bleibt oft näher an
dessen Satzbau, als er es beim freien Übersetzen täte. Das Ergebnis kann korrekt, aber flach
klingen — genau das „übersetzt"-Gefühl, das wir vermeiden wollen.

**Gegenmaßnahmen im Plan:**
1. Der blinde Vergleich mit Fassung Z misst genau diesen Effekt.
2. Der Auftrag an den Überarbeiter erlaubt **ausdrücklich** freies Umschreiben.
3. Der Lektor liest ohne Original und merkt Flachheit, unabhängig davon, woher sie kommt.

**Restrisiko:** Zwei Probestellen sind eine kleine Stichprobe. Deshalb bleibt die Änderungsquote
nach Band 1 ein zweiter Prüfpunkt.

### 8.4 „Mehr Beteiligte = bessere Übersetzung?"

**Nicht automatisch.** Ab einer gewissen Zahl von Prüfern entsteht ein Kompromiss-Text ohne Stimme.
**Regel im Plan:** Es gibt genau **eine** Person mit Schreibrecht am englischen Text (der Überarbeiter).
Alle anderen kommentieren. Der Autor entscheidet nur bei Absichtsfragen, nicht bei Formulierungen.

### 8.5 „Kann der Autor die Entscheidungen überhaupt treffen, ohne Englisch zu beurteilen?"

Teilweise nicht. Darum stützen sich alle Qualitätsentscheidungen auf **externe, blinde** Urteile
(Lektor, Kinder) und auf **Zahlen** (Änderungsquote, Rückübersetzungs-Abweichungen). Der Autor
entscheidet, was er beurteilen kann: Absichten, Budget, Personen.

### 8.6 „Ist die Änderungsquote ein gutes Maß?"

**Nur bedingt.** Ein Überarbeiter, der viel ändert, kann gründlich sein **oder** seinen eigenen Stil
durchsetzen. Ein Überarbeiter, der wenig ändert, kann einen guten Entwurf haben **oder** nachlässig sein.
**Deshalb:** Die Quote wird nie allein gelesen, sondern zusammen mit dem Lektor-Urteil und der
Rückübersetzung. Sie ist ein Hinweis, kein Urteil.

### 8.7 „Lohnt sich das überhaupt wirtschaftlich?"

**Offen.** Abschnitt 6 rechnet ~1.800 Exemplare für B1+B2 bis zur Kostendeckung, ohne Ads.
Der US-Markt ist größer als der deutsche, aber wir starten ohne Rezensionen und Bekanntheit.
**Dieser Plan macht die Übersetzung besser — er macht sie nicht billiger.** Ob der Autor dieses Geld
ausgeben will, ist eine Entscheidung, die dieser Plan nicht abnehmen kann. Die Prüfpunkte begrenzen
das Risiko: Vor Prüfpunkt 1 fließt kein Geld, vor Prüfpunkt 2 nur für zwei Bände.

### 8.8 „Warum nicht gleich nur menschlich übersetzen, wenn es kaum teurer ist?"

**Gutes Argument**, und es ist in C5 als mögliches Ergebnis eingebaut. Gegen eine Festlegung ohne Test
spricht: (a) Wir wissen nicht, ob der menschliche Weg hier wirklich besser ist; (b) eine einzelne
Person ohne Bibel und Prüfskript übersieht leicht Konsistenz über 5 Bände. **Auch bei Weg Z** bleiben
Bibel, Prüfskript und Lektorat — sie machen jede Übersetzung besser, egal wer sie schreibt.

### 8.9 Was ich am Plan beim Hinterfragen geändert habe

1. **Lektor kommentiert nur** — zuerst durften beide Rollen umschreiben. Geändert wegen 8.4.
2. **Fassung Z in den Vergleich aufgenommen** — zuerst sollten nur zwei KI-Überarbeitungen verglichen
   werden. Das hätte die Grundfrage (KI-Entwurf ja oder nein) gar nicht beantwortet.
3. **Kap. 9 als zweite Probe** — zuerst nur Kap. 1. Kap. 1 ist zu leicht, um Übersetzer zu unterscheiden;
   die Tagebuch-Stimme trennt gute von sehr guten.
4. **Kosten ehrlich verglichen** — in Fassung 1 wirkte der KI-Weg deutlich billiger. Mit
   zweisprachiger Überarbeitung schrumpft der Unterschied; das steht jetzt offen in Abschnitt 6.
5. **Vorlese-Test** ergänzt — billig, und er findet holprige Sätze, die stille Leser überlesen.

---

## 9. Offene Fragen an den Autor

| # | Frage | Wofür |
|---|---|---|
| 9.1 | Ist ein Budget von **ca. 3.800–6.200 €** für Band 1 + 2 (ohne Ads) denkbar? Wenn nein: wie viel? | Abschnitt 6. Bei kleinerem Budget gilt Fassung 1 (nur ein Lektor) — mit bekanntem Qualitätsrisiko. |
| 9.2 | Wie sicher ist Ihr Englisch? | Wer führt die Gespräche mit Überarbeiter und Lektor? |
| 9.3 | Kennen Sie englischsprachige Familien mit Kindern 9–12? | C4, D5 |
| 9.4 | Sollen Sie im Impressum als Autor **und** der Übersetzer genannt werden? | Vertrag C6 |
| 9.5 | Vorrang bei Zeitknappheit: Staffel 2 oder Englisch? | Gesamtplanung |
| 9.6 | „Frau Silber" oder „Mrs. Silber"? (Muss nicht jetzt entschieden werden — Vorschlag kommt in A1.) | Glossar |

---

## Nächster konkreter Schritt

**Phase A starten**, in dieser Reihenfolge: **A1 Glossar** (Entscheidungsvorlage für den Autor) →
**A5 Satz-Register** und **A6 Fallen-Liste** (brauchen alle 5 Bände, darum früh) → A2–A4, A7–A9 →
A10 Marktanalyse.
