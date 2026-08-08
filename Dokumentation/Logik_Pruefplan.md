# Logik-Prüfplan — Fehler in einem FERTIGEN Buch finden

> **Zweck:** Ein bereits geschriebenes (auch veröffentlichtes) Buch auf **Logik-,
> Kontinuitäts- und Handwerksfehler** prüfen — und so beheben, dass **keine neuen
> entstehen.**
>
> **Nicht zu verwechseln mit:** `Spannungs_Pruefplan.md` (langweilig?) ·
> `Stimmen_Pruefplan.md` (klingt es nach KI?) · `Qualitaets_Pruefplan.md` (ist es gut?).
> Dieser Plan fragt nur: **Stimmt es?**
>
> **Werkzeug:** [`Scripts/pruefe_logik.py`](../Scripts/pruefe_logik.py) — führt Durchgang A
> automatisch aus. `py Scripts/pruefe_logik.py 1`
>
> **Reihenfolge:** Logik zuerst. Ein Satz, der gestrichen wird, weil er falsch ist, muss
> vorher nicht schön gemacht werden.

---

## 0. ★ DIE FÜNF GRUNDREGELN — vor jedem Durchgang lesen

Jede steht hier, weil der Fehler in diesem Projekt **real passiert ist**.

### Regel 1 — Ein Befund ist ein Verdacht, kein Fehler
Jeder Treffer wird **im Kontext gelesen**, bevor er zählt. Bei Band 5 waren von 31
maschinellen Treffern nur 9 echte Fehler — der Rest war Leitmotiv, Cliffhanger oder ein
Fehltreffer des Suchmusters.
**Wer nach Zahlen fixt statt nach Lesen, beschädigt das Buch.**

### Regel 2 — Nach JEDEM Fix prüfen, was er anderswo bricht
Ein Fix in Akt 3 von Band 5 („Rücken zum Glas") zerstörte das Blocking in Kapitel 10 **und**
kippte in Kapitel 13 eine Prämisse samt Payoff in Kapitel 15.
**Ein Fix ist erst fertig, wenn seine Umgebung geprüft ist.**

### Regel 3 — Der Fix selbst kann ein Fehler sein
Ein K04-Fix verdoppelte **wortwörtlich** eine Formulierung aus einem K01-Fix desselben
Durchgangs. Ein geplanter Ersatz („Magen wurde zu Stein") hätte „Magen" auf 3× gebracht —
ein Muster *verstärkt*, während eines entfernt wird.
**Jede neue Formulierung gegen das ganze Buch prüfen, bevor sie bleibt.**

### Regel 4 — Ein Fix kann einen Altfehler freilegen
Nach dem Entfernen eines Füllsatzes stand in K13 eine **vorher schon vorhandene** Doppelung
nackt da — der Füller hatte sie verdeckt.
**Nach jedem Fix den ganzen Absatz neu lesen, nicht nur die Zeile.**

### ★ Regel 5 — Das Prüfwerkzeug hat auch Fehler
Beim ersten Lauf gegen Band 1 meldete das Skript 6 verbotene Begriffe — **4 davon waren
Substring-Treffer**: „Leiche" matchte „g*leiche*n" und „sch*leiche*nd". Und 20 verdächtige
Sprechverben, von denen ~15 normale Handlungsverben waren („Nora presste die Lippen
zusammen").
**Bevor man einem Treffer glaubt, prüft man das Suchmuster.** Ein falsch positives
Werkzeug kostet mehr Zeit als gar keines — und verführt zu Änderungen an heilem Text.

> ### ⚠️ Die Minimal-Regel
> **Die kleinste Änderung, die den Fehler behebt.** Nicht die schönste.
> Rangfolge: (1) ein Wort · (2) einen Satz ändern · (3) einen Satz streichen ·
> (4) einen Satz ergänzen · (5) einen Absatz umbauen.
> **Stufe 5 nur, wenn 1–4 den Fehler nachweislich nicht beheben.**

---

## 1. Vorbereitung

1. **★ Git-Stand sauber machen.** `git status` — alles committen oder stashen. Am Ende
   zeigt `git diff` **jede einzelne geänderte Zeile**. Das ist das stärkste Sicherheitsnetz
   dieses Plans; ohne sauberen Ausgangsstand funktioniert es nicht.
2. **★ Quelle bestimmen — welche Datei ist die publizierte Wahrheit?**
   Kapiteldateien gegen das Komplett-Manuskript vergleichen.
   ⚠️ Bei **Band 2 wichen 13 von 15 Kapiteln ab** — das gedruckte Buch folgte dem
   *Komplett*-Manuskript, die Kapiteldateien waren veraltet. Wer die falsche Quelle
   bearbeitet, ändert Text, den niemand liest — oder dreht Veröffentlichtes zurück.
3. **★ Stichprobe zuerst (Aufwandsschätzung).** Drei Kapitel nach Durchgang B lesen —
   Anfang, Mitte, Ende. Ergibt das **0–1 echte Fehler**, lohnt der volle Durchgang meist
   nicht. Ergibt es **3+ pro Kapitel**, ist mit erheblichem Aufwand zu rechnen — dann
   vorher entscheiden, ob sich das für ein veröffentlichtes Buch lohnt.
4. **Befundliste anlegen** (Abschnitt 6). **Nichts ändern, solange geprüft wird.**
   Erst alle Befunde sammeln, dann entscheiden, dann fixen.

---

## 2. Durchgang A — Maschinell (`pruefe_logik.py`)

```
py Scripts/pruefe_logik.py <band>          # Checks 1-9
py Scripts/pruefe_logik.py <band> --alle   # zusätzlich die rauschanfälligen 10-12
```

> ### ★ Die wichtigste Regel des Skripts: Erzählertext ≠ Dialog
> Fast alle Checks laufen **nur auf dem Erzählertext**. Figuren dürfen alles sagen —
> falsche Grammatik, Vermutungen über andere, Wiederholungen. Beim ersten Testlauf war der
> einzige POV-Treffer in Band 1 eine **Dialogzeile** und damit kein Fehler.

**Gemessene Trefferquote an Band 1** (18 Kap., 27.320 W) — nach der Werkzeugkorrektur:

| # | Check | Treffer | Wert |
|---|---|---|---|
| 1 | **Doppelte Kapiteltitel (serienweit)** | 1 | 🟢 **echter Fund** — „Der Keller" in B1 *und* B3 |
| 2 | Zeitangaben | 6 | 🟢 hoch — häufigster Fehler der Reihe |
| 3 | Zahlen, die zusammenpassen müssen | 8 | 🟢 hoch — 12 Markierungen / 11 Geister rechnen |
| 4 | Verdächtige Sprechverben | 3 | 🟡 mittel (vor der Korrektur: 20) |
| 5 | Verbotene Begriffe | 0 | 🟢 sauber (vor der Korrektur: 6 Fehltreffer) |
| 6 | POV-Bruch | 0 | 🟢 Band 1 ist POV-sauber |
| 7 | Kapitel ohne Schatten-Reaktion | 0 | 🟢 alle 18 erfüllt |
| 8 | Wörtlich wiederholte Sätze | 2 | 🟡 prüfen, ob Callback oder Schlamperei |
| 9 | Kapitel-Schlusssätze | 18 | ⚪ zur Beurteilung, kein Fehler an sich |
| 10 | **Wort-Echo** | 9 | 🔴 **wertlos** — alle 9 waren bewusste Anapher |
| 11 | Pronomen-Ambiguität | 0 | ⚪ billig, selten |
| 12 | Tageszeit-Sprünge | 0 | ⚪ billig, selten |

**Konsequenz:** Checks 1–3 zuerst, sie tragen den Ertrag. Check 10 nur bei konkretem
Verdacht — er zeigt bei sauberer Prosa fast nur Stilmittel an und **verführt dazu, gute
Sätze zu zerstören**.

---

## 3. Durchgang B — Lesen mit acht Fragen

Maschinen finden keine Logikfehler. Dieser Durchgang schon. **Kapitel für Kapitel**, mit der
Kontinuitätsdatei daneben.

### B1 — Blocking *(häufigste Fehlerquelle)*
> Wer steht wo, wer sieht wen an, wer hält was?

Bei jedem Szenenwechsel mitzeichnen. Diese Fehler entstehen fast immer beim **Überarbeiten**.
Konkret: Kann die Figur das sehen? Hat sie die Hand frei? Ist sie überhaupt im Raum?

### B2 — Wissen
> Woher weiß die Figur das?

Für jede Aussage: gesagt bekommen (wo?), gesehen (wo?), oder erfunden? In Band 5 stand
*„Nora begriff, dass er es seit zweihundert Jahren nicht ausgesprochen hatte"* — **das konnte
sie nicht wissen.**

### B3 — Ursache und Wirkung
> Passiert das, *weil* vorher etwas passiert ist — oder weil die Handlung es braucht?

Verbotenes Muster: etwas hört auf, **weil jemand es sehr will**. Willenskraft ist keine
Mechanik.

### B4 — Motivation
> Würde diese Figur laut ihrer **eigenen** Motivation so reagieren?

In Band 5 sagte der Antagonist „Nein, warte —", als sein *eigener Plan* aufging.

### B5 — Weltregeln
> Hält sich die Mechanik an ihre eigenen Regeln?

Alle Sätze sammeln, die eine Regel behaupten („Er kann nicht …", „Nur wenn …"), und
**untereinander legen**. In Band 5 widersprachen sich zwei über zwei Kapitel hinweg —
sichtbar erst nebeneinander.

### ★ B6 — Gegenstände und Aussehen
> Wo ist das Ding gerade?

Taschenlampe, Karte, Notizbuch, Schlüssel, Rucksack: mitverfolgen. Wer etwas abgelegt hat,
kann es zwei Seiten später nicht benutzen. Dasselbe für Kleidung, Verletzungen, Wetter und
Tageszeit — was etabliert ist, bleibt, bis es explizit geändert wird.

### ★ B7 — Figurenstimme
> Klingt der Satz nach dieser Figur?

Theo ist **zehn**. Ein Wort wie „letztlich" oder ein verschachtelter Nebensatz ist bei ihm
ein Fehler, auch wenn er inhaltlich stimmt. Gegenprobe: Repliken abdecken und raten, wer
spricht. Wer das nicht kann, hat ein Stimmproblem.

### ★ B8 — Serien-Kontinuität *(nur ab Band 2)*
> Widerspricht das einem früheren Band?

Prüfen: Figurenalter und Zeitlinie · bereits befreite Geister (sie können nicht
zurückkehren) · etablierte Regeln der Welt · Wohnorte, Namen, Verwandtschaften.
**Gegen die früheren Bände prüfen, nicht gegen die Erinnerung.**

---

## 4. Durchgang C — Fair Play (nur bei Rätsel/Twist)

Alle Hinweise auflisten, mit Kapitelnummer. **Regel: Eine Auflösung in Kapitel N darf nur
Hinweise nutzen, die in Kapiteln ≤ N stehen.**
Gegenprobe: Kann ein aufmerksames Kind es vorher ahnen? Nein → Hinweis fehlt.
Offensichtlich → ein Hinweis zu viel.

---

## 5. Bewertung — ist es wirklich ein Fehler?

Nur 🔴 und 🟠 werden geändert.

| | Bedeutung | Vorgehen |
|---|---|---|
| 🔴 **Fehler** | Widerspruch, faktisch falsch, Regelbruch | **fixen** |
| 🟠 **Schwäche** | nicht falsch, aber verwirrend | fixen, **wenn** minimal möglich |
| 🟡 **Absicht** | wirkt wie ein Fehler, ist gewollt (Leitmotiv, Callback, Figurensprache) | **stehen lassen + notieren**, damit es beim nächsten Durchgang nicht erneut auffällt |
| ⚪ **Fehltreffer** | Suchmuster hat danebengegriffen | verwerfen — **und das Muster korrigieren** (Regel 5) |

**Die Beweislast liegt beim Fixen.** Wer nicht begründen kann, *warum* es ein Fehler ist,
lässt es stehen. Im Zweifel: 🟡.

---

## 6. Befundliste (Vorlage)

| # | Kap. | Zitat | Fehlerart | Einstufung | Begründung | Fix (minimal) | Regel 2 geprüft | Status |
|---|------|-------|-----------|-----------|------------|---------------|-----------------|--------|
| 1 | | | Zeitlinie / Blocking / Wissen / … | 🔴🟠🟡⚪ | | | ✓ | offen |

---

## 7. Fix-Durchgang — die Sicherheitsschleife

**Pro Befund, in dieser Reihenfolge. Keine Abkürzung.**

1. **Minimalen Fix formulieren** (Rangfolge Abschnitt 0).
2. **Regel 3:** Neue Formulierung gegen das **ganze Buch** suchen. Kommt sie schon vor?
   Verstärkt sie ein Muster?
3. **Fix einbauen.**
4. **Regel 4:** Den **ganzen Absatz** neu lesen.
5. **Regel 2:** Umgebung prüfen —
   - Absatz davor und danach
   - bei Blocking-Änderungen: das ganze Kapitel
   - bei Mechanik-/Regeländerungen: **alle** Kapitel, die dieselbe Regel erwähnen
   - bei Namen/Fakten: alle Vorkommen im Buch
6. **Abhaken**, mit Notiz, was geprüft wurde.

### ★ Abschlussprüfung (nicht überspringen)

1. **`git diff` Zeile für Zeile lesen.** Jede geänderte Zeile muss einem Befund in der
   Liste entsprechen. Findet sich eine Änderung ohne Befund — zurücknehmen.
2. **`pruefe_logik.py` erneut laufen lassen.** Neue Treffer, die vorher nicht da waren,
   sind mit hoher Wahrscheinlichkeit **selbst verursacht**.
3. **Kapitel-Schlusssätze vergleichen** — alle unverändert? Cliffhanger sind tabu.
4. **Setup/Payoff-Anker** noch vorhanden (falls ein Tracker existiert)?
5. **Wortzahl-Differenz plausibel?** Ein Logik-Pass ändert **wenige Dutzend** Wörter, nicht
   Hunderte. Große Differenz = zu viel angefasst.
6. **★ Am fertigen Artefakt prüfen, nicht im Manuskript.** Lehre aus der
   Band-1–4-Nachbesserung: Fehler im Bauprozess sind im Markdown unsichtbar und nur im
   fertigen DOCX/PDF zu sehen — so kam der `**ENDE**`-Marker ans Licht, der bis in den
   Druck durchschlug.

---

## 8. Wann dieser Plan gestoppt wird

- **Stichprobe ergibt 0–1 echte Fehler** → das Buch ist in Ordnung. Aufhören.
- **20 Befunde, keiner 🔴** → aufhören.
- **Fixes bedingen sich gegenseitig** (A braucht B braucht C) → stoppen und die Kette als
  Ganzes bewerten, statt weiterzukorrigieren.
- **Ein Fehler wäre nur durch großen Umbau zu beheben** → **notieren, nicht ausführen.**
  Bei einem veröffentlichten Buch ist ein großer Umbau fast nie Aufwand und Risiko wert.

---

## 9. Bekannte 🟡-Befunde (nicht erneut melden)

> Hier eintragen, was geprüft und als Absicht eingestuft wurde — sonst prüft man es beim
> nächsten Durchgang wieder.

| Band | Stelle | Warum kein Fehler |
|---|---|---|
| 1 | „einen Moment — einen einzigen, kurzen Moment", „vorbei … vorbei … vorbei" u. a. | Bewusste Anapher, Stilmittel (Check 10) |
| 5 | „Zum ersten Mal seit zweihundert Jahren" (mehrfach) | Tragendes Leitmotiv, trägt den Payoff |
| 5 | K1/K8 „hielt alles ein bisschen zu fest" (fast wortgleich) | Callback: K1 benennt das Verhalten, K8 liefert den Grund |
| S2-1 | K12 „Bei einem Menschen hört man auf zu ziehen" — Analogie statt Ableitung | Durchgang C 2026-08-08: Der letzte Schritt der Auflösung ist bewusst weich. Das Buch flaggt es selbst durch Theo („klingt wie ein Poster im Klassenzimmer"); K10 hat die Richtung („sanft, nicht mit Gewalt") gerade vorgeführt, die Form bleibt Überraschung. Ein härterer Hinweis wäre nach der Gegenprobe **ein Hinweis zu viel**. |
| S2-1 | Das Schloss bleibt nach Herberts Befreiung kalt (K13/K15/K16), obwohl K12 die Kälte mit „es gehört zu ihm" erklärt | Kein Widerspruch, sondern Konstruktion: Noras Deutung ist wahr, aber unvollständig — die Kälte kommt vom **Erbauer**, nicht vom Gehaltenen. K13 und K15 markieren die Abweichung ausdrücklich. Trägt den Staffel-Haken. |
