# A0 · Prüfung Phase A — was hält, was war falsch, was ändert sich

> Stand 2026-10-12. Auftrag des Autors: *„Überarbeite Phase A nochmal sehr genau, begründe und
> hinterfrage deine Entscheidungen kritisch."*
>
> **Wie geprüft:** Jede Zahl, jedes Zitat und jede Stellenangabe in A1, A3, A5, A6 stichprobenartig
> gegen die Manuskripte nachgeschlagen. Band 1 aus der umgebauten Fassung (Branch `ccr-c33fc6fe-peyki0`), Band 2–5 aus
> `Manuskript_BandN_Komplett.md`. Wo ein Fund unsicher war, im Text nachgelesen statt aus dem Gedächtnis.
> Außerdem geprüft, ob die Schreibregeln S1–S6 mit den Build-Skripten zusammenpassen.

---

## 1. Ergebnis in einem Satz

Phase A ist **inhaltlich tragfähig**, hatte aber **sechs sachliche Fehler** — einer davon (S1) hätte
in Staffel 2 das gedruckte Buch beschädigt. Alle sind korrigiert. Dazu kommen drei Stellen, an denen
das **deutsche Original** selbst einen Fehler hat. Und der weitere Ablauf von Phase A wird umgestellt:
**Pilot früher, A7 kleiner, A2/A4 aus vorhandenen Unterlagen.**

---

## 2. Gefundene Fehler und Korrektur

| # | Wo | Fehler | Korrektur | Wie schlimm? |
|---|---|---|---|---|
| P1 | **Schreibregel S1/S4** (Plan + `Schreibstil_Ergaenzung_Staffel2.md`) | Markierung als `<!-- EN: … -->`-Kommentar im Kapiteltext. **Kein Build-Skript filtert HTML-Kommentare** (geprüft: kein `<!--` in `Scripts/*.py`). Der Kommentar wäre im DOCX/eBook/Taschenbuch **mitgedruckt** worden. | Hinweise stehen jetzt in einer Nebendatei `EN_Hinweise.md` je Band (Kapitel · Zitat · Art · Funktion). | **Hoch** — einziger Fehler mit Schaden am deutschen Produkt. Noch kein Kapitel betroffen (geprüft: kein `<!--` in `Staffel2/`). |
| P2 | **A1 E10, A6 F-B** | Beispiel *„sixteen degrees colder"* für B2 K1. 55 → 48 °F sind **7** °F. | *“Seven degrees colder.”* | Mittel — falsches Beispiel im verbindlichen Glossar wäre übernommen worden. |
| P3 | **A5 R30** | *“Had a daughter in Hanover. Never knew he died.”* — ohne Subjekt liest man „**er** wusste nicht, dass er starb". In B2 K14 steht im Original sogar *„Sie wusste nicht …"* | *“… She never knew he died.”* an beiden Stellen | Mittel — Bedeutungsfehler an einer emotionalen Stelle. |
| P4 | **A1 E9** | „Zweiter Stock kommt 20× vor" — A6 zählt 25. | 25, mit Quelle | Gering — Begründung stimmt trotzdem. |
| P5 | **Plan, Abschnitt „Stand"** | Doppelte, abgebrochene Zeile (`A6) → A2 Stimmen …`), veraltete Zahlen (42 statt 43 Register-Einträge; „Sprachwitze B1" statt B1–B5). | bereinigt | Gering. |
| P6 | **Selbsttest des Skripts** | Prüfte nur, ob *irgendein* Treffer kommt, nicht ob **jeder erwartete Ausdruck** gefunden wird. Den Fehler mit „Dritter Stock" am Satzanfang (A6, F29) hätte er nicht bemerkt. | Selbsttest prüft jetzt jeden erwarteten Ausdruck einzeln, auch „Dritter Stock" und den Genitiv „Frau Silbers". Gegenprobe: Mit dem alten Muster schlägt er fehl. | Mittel — ein Test, der nicht scheitern kann, ist kein Test. |

| P7 | **A5 Satz-Register** (Commit 5cc553a, nachträglich gefunden) | Beim Einfügen von R44/R45 hat mein Bearbeitungs-Skript den Rest der Datei abgeschnitten: **R12–R43 waren gelöscht** (106 → 37 Zeilen). Gefunden hat es der Selbsttest des neuen Prüfskripts `pruefe_en.py` (verlangt ≥ 30 Register-Paare). | Datei aus dem vorigen Stand wiederhergestellt, R44/R45 wieder eingefügt (45 Einträge). Alle anderen Dateien des Commits per Zeilenzahl geprüft: nur A5 betroffen. | **Hoch** — wäre ohne Selbsttest erst beim Übersetzen aufgefallen. Lehre: Nach jeder Bearbeitung per Skript Zeilenzahl vorher/nachher vergleichen. |

**Ehrliche Einordnung:** P2 und P3 sind Flüchtigkeitsfehler beim Schreiben der Vorschläge. P1 ist ein
Denkfehler: Ich habe die Regel aus Sicht der Übersetzung entworfen und nicht geprüft, was die
Build-Kette mit dem Text macht. Daraus folgt eine Regel für den Rest von Phase A: **Jede Regel, die den
deutschen Text berührt, wird gegen die Build-Skripte geprüft.**

---

## 3. Fehler im deutschen Original (gefunden beim Gegenprüfen)

Die Übersetzung folgt dem Original. Was hier falsch ist, sollte **zuerst auf Deutsch** entschieden werden.
Vollständige Liste: `A3_Witz_Liste.md`, Abschnitt „Nebenfunde".

| Band | Stelle | Befund | Vorschlag |
|---|---|---|---|
| B2 | K1 | Wetter-App 13 → 9 Grad, dann *„Neun Grad kälter."* Es sind **vier**. Auch `Serien_Kanon.md` übernimmt „9 Grad kälter". | *„Vier Grad kälter."* — oder Endwert auf 4 Grad, wenn der Sturz drastisch sein soll |
| B5 | K5 (+ B3 K2) | Rückbezug auf Frau Held „im Sommer". **Nachgeprüft:** Frau Held fehlt im Roman Band 1 (auch in der Git-Geschichte), steht aber im **Spielbuch Band 1** (`Band1/CYOA`, Abschnitt 017: „Nachbarin im Erdgeschoss"). Die frühere Notiz „kommt in Band 1 nicht vor" war also zu grob. | Für Deutsch: hinnehmbar. **Für Englisch** wird es schlimmer, wenn das Spielbuch nicht übersetzt wird. Entscheidung offen (Abschnitt 6). |
| B2 | 8 Stellen | Tippfehler/Grammatik (Moos, Hängte, Zerfransen, hinterm Mauer, Gibt mir, Ich sieh, kein Gegenbeleg, Schlimmste) | wie in A3 gelistet |

---

## 4. Entscheidungen, die ich erneut hinterfragt habe — und warum sie bleiben (oder nicht)

| Entscheidung | Einwand | Ergebnis | Begründung |
|---|---|---|---|
| **E1 *The Ghost Listeners*** | Vor der Marktanalyse A10 festgelegt — das ist die falsche Reihenfolge. | **bleibt**, A10 macht vor dem Cover eine Gegenprobe | Der Titel folgt aus dem Inhalt (Zuhören befreit), nicht aus dem Markt. Die Titelsuche wurde gemacht. Was fehlt, ist nur die Gegenprobe gegen Amazon.com-Suchergebnisse und Kategorien. Die kostet nichts und kann den Titel noch kippen, bevor Geld in ein Cover fließt. |
| **E2 *The Whispering Window*** | Das Fenster *schreibt*, es flüstert nicht. | **bleibt** | Der deutsche Titel sagt selbst „flüstert", und das Haus *klopft* und *schreibt*. „Flüstern" ist dort schon bildhaft gemeint. Alternativen wie *Words on the Window* verlieren den Grusel-Klang. Gegenprobe in A10 wie bei E1. |
| **E8 *Mrs.* statt *Ms.*** | *Ms.* ist im US-Englisch die neutrale Form. | **bleibt**, Begründung ergänzt | Alle Frauen mit Anrede sind alt oder historisch: Silber, Held, die Geistfrau Weber, Linas Lehrerin Kettner (1974). *Mrs.* passt zu ihnen. **Neue Regel:** junge Frauen in Staffel 2 → *Ms.* |
| **R33 *FOR MOM. I'M NOT MAD.*** | *mad* heißt britisch „verrückt". Ein Objekt (*at you*) wäre klarer. | **bleibt, ohne Objekt** | In B3 K13 sagt Nora, der Satz sei an niemanden gerichtet. *at you* würde genau das zerstören. *mad* klingt nach Kind; die Ausgabe ist US. |
| **R5 *Angry. Grave.*** | *grave* heißt auch „ernst". | **bleibt, Pilot prüft** | Im Kontext (Notiz zu einem Toten) liegt „Grab" nahe, und Theos Witz F17 (*“Angry period. Grave period.”*) braucht genau diese zwei Wörter. Wenn Prüfer D4 es als „ernst" liest, kommt *Angry. Buried.* in Frage — dann muss F17 neu gebaut werden. |
| **W3-08 *darn* (Pawlik)** | *darn* klingt nach Kind oder Oma, nicht nach knurrigem Alten. | **geändert → *blasted*** | Genauso harmlos für 9–12, passt zur Figur. Glossar: Kinder *darn*, alte Leute *blasted*. |
| **Witz-Zählung ≈ 280** | Band 1 wurde genauer gezählt als Band 2–5 und ist länger. Die Zahlen sehen aus, als würde der Humor abnehmen. | **Zahlen bleiben, Warnung ergänzt** | Pro 1.000 Wörter: 4,7 / 3,4 / 2,7 / 1,7 / 2,2. Der Rückgang ist teils echt (höhere Gruselstufe), teils Zählweise. Für die Übersetzung zählen nur Umbauten und Neuerfindungen, und die sind vollständig. **Keine Aussage über „zu wenig Humor in Band 4" ableiten.** |
| **Band-1-Grundlage = nicht gemergter Branch** | Wenn Band 1 noch geändert wird, verschieben sich Stellenangaben. | **bleibt, Risiko benannt** | Alle Einträge nennen Kapitel, nicht Zeilen, und zitieren den Satz. So bleiben sie auch nach kleinen Änderungen auffindbar. Vor der Übersetzung von Band 1 einmal das Skript neu laufen lassen. |
| **Englische Vorschläge allgemein** | Sie stammen von einer KI ohne Muttersprachler-Prüfung und klingen vielleicht nur plausibel. | **bleibt — das ist die bekannte Grenze des Plans** | Deshalb heißt es „Englisch vorläufig bis Pilot". Die Prüfung machen D4 (Bedeutung), D5 (US-Lektor ohne Deutsch) und die Lesegruppen (E2). Ein menschlicher Muttersprachler bleibt die stärkste fehlende Prüfung (Plan Abschnitt 8; Autor: ohne Lektorat). |

---

## 5. Umstellung des weiteren Ablaufs von Phase A

**Bisher:** A2 → A4 → A11 → A7–A10 → Pilot.
**Neu:** A2 + A4 (aus vorhandenen Unterlagen) → A8 Stil-Brief → A11 EN-Prüfungen → **Pilot (K1 + K9)** →
A7 und A9 für die restlichen Kapitel → A10 vor dem Cover.

| Änderung | Begründung | Gegenargument |
|---|---|---|
| **Pilot vor A7/A9/A10** | Der Pilot beantwortet die wichtigste offene Frage: *Hilft die Bibel überhaupt?* A9 (US-Zielwerte) und A10 (Markt) ändern an der Übersetzung von K1 und K9 nichts. Wenn der Pilot zeigt, dass die Bibel anders aufgebaut sein muss, war die Arbeit an A7–A10 für alle Kapitel umsonst. | Ohne A9 fehlen dem Pilot die US-Vergleichswerte für D8.1. → Für den Pilot reichen die deutschen Werte als Bezug (Gleichwertigkeit DE ↔ EN). A9 kommt danach. |
| **A7 kleiner** | Kapitelpläne gibt es schon: `Story_Outline.md` (B1–B3), `Cliffhanger_Register.md` + `Detaillierte_Szenenplanung.md` (B4–B5). A7 wird **daraus herausgezogen**, je Kapitel eine Zeile „Leser soll fühlen" + Kapitelende. Der Autor prüft nur Band 1 vollständig, B2–B5 stichprobenartig. | Die Pläne können vom fertigen Text abweichen. → Bei Abweichung gilt der Text; A7 notiert die Abweichung. |
| **A2/A4 aus Skript + gezieltem Nachlesen** | Beim Lesen für A3 hätte ich Stimmen und Motive gleich mitsammeln sollen — das war ein Planungsfehler. Jetzt: Dialogsätze je Figur per Skript herausziehen, Motive per Suchwort (Klopfen, metallisch, Bernstein, Kondenswasser, lila Tinte). | Ein Skript erfasst den *Ton* nicht. → Das Skript liefert die Belege, die Beschreibung des Tons schreibe ich aus den Belegen. |
| **A9 nur Kennzahlen** | Aus Leseproben werden **nur Zahlen** gemessen (Satzlänge, Dialoganteil, Absatzlänge). Kein fremder Text kommt ins Repository (Urheberrecht). | Leseproben sind kurz (meist Kap. 1–2) und nicht für das ganze Buch typisch. → Werte als Korridor lesen, nicht als Ziel. |

---

## 6. Was der Autor entscheiden sollte (nicht dringend, vor der Übersetzung von Band 2 bzw. 5)

1. **B2 K1 „Neun Grad kälter"** — auf Deutsch zu „Vier Grad kälter" korrigieren? (Ändert eine
   veröffentlichte Ausgabe; ein Satz, weit unter der 10-%-Grenze von KDP.)
2. **Frau Held** — im Roman Band 1 (umgebaute Fassung) mit einer kurzen Begegnung im Treppenhaus
   einführen? Dann stimmen B3 K2 und B5 K5 für alle Leser, und die englische Ausgabe braucht das Spielbuch nicht.
3. **Tippfehler Band 2** — die 8 Stellen auf Deutsch korrigieren? (Angeboten, noch nicht freigegeben.)

Bis dahin übersetzt die englische Fassung **so, wie das Original es meint** (z. B. *Seven degrees
colder*), und die Abweichung steht im Bericht D8.

---

## 7. Was diese Prüfung selbst nicht leistet

- **Stichprobe, keine Vollprüfung.** Alle Zahlen in den Bilanzen und alle Register-Einträge mit
  Stellenangabe sind nachgeschlagen. Die 226 „übertragbaren" Witze aus Teil B sind **nicht** einzeln
  nachgeprüft — dort kann ein Fehler keinen Schaden anrichten, weil sie ohnehin nur übersetzt werden.
- **Kein Englisch-Muttersprachler** hat irgendetwas davon gesehen (siehe Abschnitt 4, letzte Zeile).
- **Die Titel sind nicht markenrechtlich geprüft**, nur gegen Buchtitel. Buchtitel sind in den USA in
  der Regel nicht schützbar, Reihentitel unter Umständen schon. Die A10-Gegenprobe sucht deshalb auch
  im US-Markenregister (USPTO) nach *Ghost Listeners*.
