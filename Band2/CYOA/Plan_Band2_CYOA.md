# Plan — Die Geisterspürer Band 2 CYOA
## "Der Friedhof ohne Namen" — Entscheidungsbuch

> Strategiedokument. Noch kein Graph, noch keine Texte.
> Architektur-Entscheidung: **Time Cave wie Band 1**, **kanontreu** zum linearen Manuskript (Handlung/Figuren/Twist — *nicht* Typografie, s. §1a).
> Status: **Rev. 3** — Stil-Philosophie auf den **v3-Stand von Band 1** umgestellt (s. §0a + §7).
> Die numerischen Qualitätsziele aus `Qualitaets_Analyse.md` (Wortzahl/Dialog-Quote als Soll) sind
> **verworfen**; maßgeblich ist `Band1/CYOA/v2/STIL_REFERENZ.md`. Bewährte Rev.-2-Entscheidungen
> (Kanontreue, POV `nora_aussen`, Twist = Johanns Zweig, Codewörter, Pfad C zuerst) bleiben unverändert.

---

## 0. Was diesem Plan zugrunde liegt (analysierte Quellen)

| Quelle | Was ich daraus übernehme |
|--------|--------------------------|
| `Band1/CYOA/v2/graph_v2.yaml` | Time-Cave-Struktur, ID-Konventionen (P/A/B/C/D/E), Datei-Layout, Konvergenz-Regel |
| `Band1/CYOA/frontmatter.md` | "HALT!"-Seite, Regeln, Codewort-Hinweis — wird für Band 2 adaptiert |
| `Band1/CYOA/v2/STIL_REFERENZ.md` | **Maßgebliche Stil-Philosophie (v3)**: Anti-KI-Muster, Rhythmus, konkrete Details, *kein* Wortzahl-Ziel. Überschreibt `Qualitaets_Analyse.md`. |
| `Band1/CYOA/v2/KANON.md` | Vorbild für die zu erstellende `Band2/CYOA/KANON.md` (Faktenblatt gegen Widersprüche). |
| `Band1/CYOA/Qualitaets_Analyse.md` | Nur noch als **Diagnose-Beispiel** genutzt: zeigt, *welche* Abschnitte zu dünn wurden — die numerischen Soll-Werte daraus sind **verworfen** (s. §0a). |
| `Band1/CYOA/v2/endings/E07.md` | Ending-Format inkl. Codewort-Box (🔑 …) |
| `Band2/Story_Outline.md` | **Kanon**: Brenner/Voss, Kloß, Akt-Struktur, Twist, Orte, Schatten-Verhalten |
| `Band2/Manuskript/` (15 Kap.) | Tonfall, Dialoge, konkrete Szenen — Steinbruch für CYOA-Szenen |
| `Dokumentation/Codewort_System.md` | Band 2 Serien-Wort = **ERINNERN**, 3 Codewörter, Geheim-Ending-Regeln |
| `Scripts/build_cyoa_taschenbuch_v3.py` + `validate_graph_v2.py` | Build- & Validierungs-Pipeline, die wir 1:1 weiternutzen |

---

## 0a. Stil-Philosophie (Rev. 3 — die wichtigste Korrektur)

**Was sich gegenüber Rev. 2 ändert und warum:**
Rev. 2 zog seine Qualitätsziele aus `Qualitaets_Analyse.md` (Ø 300–350 Wörter, Enden ≥ 300 W,
Dialog 35–45 %). Genau diese „mehr Wörter / mehr Quote"-Logik hat Band 1 bei der v3-Überarbeitung
als **Ursache** des maschinellen Eindrucks erkannt. `STIL_REFERENZ.md` sagt wörtlich:
*„Kein Wortzahl-Ziel. Aufgefüllter Text war Teil des KI-Problems."* → Rev. 3 stellt um.

**Die maßgeblichen Regeln (aus `Band1/CYOA/v2/STIL_REFERENZ.md`):**
1. **Kein Wortzahl-Ziel.** Ein Abschnitt ist fertig, wenn er funktioniert. Kurz & dicht schlägt lang & aufgefüllt.
2. **Verbotene KI-Muster** (hart): „Nicht X, sondern Y", Dreier-Fragment-Listen, Adverb-Echos nach Punkt, Wort-Wiederholung als Pseudo-Tiefe, Gefühls-Treppen, erklärender Schluss-Doppelsatz.
3. **Satzrhythmus mischen.** Kein Dauer-Stakkato. Lange, sich windende Sätze machen die kurzen erst scharf.
4. **Emotionen körperlich zeigen,** nie etikettieren. Ein Gefühl pro Moment, voll ausgespielt.
5. **Pro Abschnitt ≥ 1 konkretes, eigenwilliges Detail** (der stärkste Anti-KI-Hebel).
6. **Anti-Recycling:** wortgleiche Bausteine über Abschnitte variieren — der Leser geht mehrere Pfade und *bemerkt* Wiederholungen.

**Wortzahl wird Diagnose, nicht Ziel:** Der Report dient nur dazu, *verdächtig* dünne Abschnitte
(Richtwert < ~130 W) zu **finden** — die dann *geprüft* werden („fehlt hier eine Szene / ein Beat?"),
**nicht** mechanisch aufgefüllt. Siehe §7 (neu) und §0b (Werkzeuge).

---

## 0b. Werkzeug-Dateien VOR dem Schreiben (in Rev. 2 gefehlt)

Der wahre Qualitätshebel von Band 1 waren nicht die Metriken, sondern zwei Steuer-Dokumente. Band 2
bekommt sie ebenfalls — **bevor** Prosa entsteht:

| Datei | Zweck | Quelle |
|-------|-------|--------|
| `Band2/CYOA/KANON.md` | Faktenblatt aus dem Manuskript: Brenner (1820–1887), Voss (1810–1888), Johann (*1851 †1853), 47 Namen, Kloß' Urgroßvater, zwei Friedhofs-Zonen, Schatten-Verhalten, Frau-Silber-Spur. Verhindert Widersprüche über alle Abschnitte. | Vorbild `Band1/CYOA/v2/KANON.md` |
| `Band2/CYOA/STIL_REFERENZ.md` | §0a + Band-2-spezifische Anti-Recycling-Listen (s. §7). | adaptiert von Band 1 |
| `Band2/CYOA/moral_map.md` | Lektion je Dead End / Ende. | wie Band 1 |

---

## 1. Die zentrale Design-Spannung (und wie der Plan sie löst)

**Das Problem, das ich offen benenne:**
Time Cave lebt von *divergierenden* Pfaden, die kaum konvergieren. Die Story von Band 2 hat aber einen **zwingenden Twist**: Brenner allein zu befreien funktioniert *nicht* — Voss muss von jemandem mit Verantwortung (Kloß) entlarvt werden. Eine reine Verzweigung würde entweder den Twist verwässern oder lauter "falsche" Pfade erzeugen.

**Die Lösung — "Time Cave mit einem Erkenntnis-Pol":**
- Die 3 Pfade (A/B/C) divergieren in **Akt 1–2** ganz normal wie in Band 1 (verschiedene Wege, den Friedhof zu erforschen).
- Sie führen aber alle zu **derselben Erkenntnis** ("Es sind zwei Geister, Voss ist das Problem") — jeder Pfad erreicht sie *anders* und *zu anderem Preis*. Das ist **keine** Konvergenz der Abschnitte (die bleiben getrennt, Time-Cave-konform), sondern eine **thematische Konvergenz**.
- Ab dem Twist verzweigt jeder Pfad erneut in **eigene** Enden. Brenner-Befreiung gelingt nur, wenn der Leser auf seinem Pfad die "Voss-zuerst"-Logik trifft. Wer das verpasst, landet bei einem ehrlichen, aber unvollständigen Ende (wie E5/E8/E22 in Band 1).
- **Regel bleibt:** Pfade konvergieren nicht in den Abschnitten. Einzig erlaubter Brückenpunkt analog Band 1 (C→A/B) ist hier **C→Kloß-Strang**, weil Kloß die Pflicht-Figur des Twists ist.

**Warum das die richtige Wahl ist:** Es erhält volle Band-1-Konsistenz (Pipeline, Codewörter, Optik), respektiert den Kanon und macht den Twist trotzdem zur dramatischen Achse statt zur Einbahnstraße.

**⚠️ Offene Graph-Frage (in Schritt 1a zu entscheiden, Rev. 3):**
Auf Prosa-Ebene ist „thematische Konvergenz" elegant — auf YAML-Ebene erzwingt sie eine harte Wahl:
- **(a) Drei getrennte Twist-Abschnitte** (A-Twist / B-Twist / C-Twist), gleicher *Kern*, bewusst
  *verschiedene Inszenierung*. Hält Time-Cave sauber (0 Konvergenz, Validator grün). **Preis:** Recycling-Gefahr
  — die drei Abschnitte müssen aktiv unterschiedlich geschrieben werden (Anti-Recycling-Liste, §7).
- **(b) Ein gemeinsamer Konvergenz-Twist.** Garantiert identischen Twist, spart Schreibarbeit. **Preis:**
  bricht die Time-Cave-Regel (zweiter Konvergenzpunkt neben C→Kloß), Validator wirft Warnung, Pfad-Identität verwässert.

→ **Vorgehen:** In Schritt 1a beide Varianten als kleine Mermaid-Skizze gegenüberstellen, dann festlegen.
Bis dahin ist dieser Punkt **nicht** entschieden (Rev. 2 hatte ihn fälschlich als gelöst markiert).

---

## 1a. Was "kanontreu" heißt — und was NICHT (geklärt nach Manuskript-Abgleich)

Beim Abgleich mit dem fertigen linearen Manuskript (Kap. 1 & 11) sind zwei Punkte aufgefallen, die der erste Plan falsch/unscharf hatte:

**Typografie — bewusste Ausnahme vom Kanon:**
Das lineare Band-2-Manuskript nutzt **gerade Anführungszeichen** (`"Theo!"`). Band 1 CYOA und der Validator (`analyze_quality.py`, Punkt 6) erwarten **Guillemets** (`»Theo!«`).
→ **Festlegung:** Das CYOA nutzt **Guillemets »…«** wie Band 1 CYOA. "Kanontreu" gilt für **Handlung, Figuren, Twist, Orte** — *nicht* für Satzzeichen. So bleibt die interaktive Reihe in sich konsistent und der Validator grün.

**Perspektive — harte Regel, betrifft den Theo-Höhepunkt:**
CLAUDE.md: *"Dritte Person nah an Nora. Nur was Nora wahrnimmt."* Das Manuskript löst die Theo-allein-Szene mustergültig: **Nora steht draußen am Kapellenfenster** und nimmt nur Fragmente wahr (Geräusche, Theos Gesicht im Spalt). Theos Erlebnis wird *danach* von ihm erzählt, nie aus seinem Kopf.
→ **Festlegung:** Im Graph erhält jeder Theo-allein-Abschnitt die Notiz `pov: nora_aussen`. Verhindert einen späteren Schreibfehler, der die Serien-Regel bräche.

---

## 2. Die drei Pfade (Spiegel von Band 1, an Band-2-Kanon angepasst)

Band 1: A=übernatürlich folgen, B=logisch ermitteln, C=Familie/Mama.
Band 2 spiegelt diese **Leser-Haltungen**, nutzt aber Band-2-Figuren:

| Pfad | Band-2-Name | Leser-Haltung | Einstieg | Kanon-Anker |
|------|-------------|---------------|----------|-------------|
| **A** | "Dem Grauen folgen" | mutig / übernatürlich | Nora folgt der grauen Gestalt (Brenner) in den namenlosen Teil | Kap. 3, 7, 9–11 |
| **B** | "Die Ermittlerin" | rational / Recherche | Stadtarchiv, Friedhofsbücher, das Foto mit durchgestrichenem Namen | Kap. 4, 12 |
| **C** | "Kloß vertrauen" | sozial / Erwachsene einbeziehen | Direkt zu Herrn Kloß; er wird vom Hindernis zum Verbündeten | Kap. 2, 6, 13 |

**Begründung der Zuordnung:**
- A entspricht der "Schatten folgen"-Energie von Band 1 — nur dass **Schatten hier ausfällt** (verweigert den Friedhof). Das ist der frischeste Pfad: Nora muss *ohne* ihr Frühwarnsystem mutig sein. Kanon-Detail aus Outline.
- B nutzt die Recherche-Stärke, die in Band 1 (Pfad B) am schwächsten umgesetzt war → hier gezielt besser machen.
- C war in Band 1 qualitativ der **stärkste** Pfad (Werte 8–10). Kloß als emotionaler Erwachsener ist das Band-2-Äquivalent zu Mama. Diesen Pfad bewusst als Highlight planen.

---

## 3. Prolog (gemeinsam, P1–P5)

Direkt am Kanon (Outline Kap. 1). Endet im 3-fachen Wahlpunkt.

| ID | Titel | Inhalt | Typ |
|----|-------|--------|-----|
| P1 | "Schatten bleibt stehen" | Friedhofstor, heller Morgen. Schatten knurrt, weigert sich einzutreten. | story |
| P2 | "Zwei Zonen" | Vorderer Teil gepflegt, hinterer namenlos & 5° kälter. Vögel fliegen auf. | story |
| P3 | "Der kippende Stein" | Ein Grabstein kippt ohne Wind. Dunkle Silhouette zwischen den Steinen. | story |
| P4 | "Theo will weg" | Theos Witz ("Schatten ist klüger als wir beide"). Spannung: bleiben oder gehen? | story |
| P5 | **Entscheidung** | 3 Wege. | **choice → A1 / B1 / C1** |

P5-Wahl (Wording im Stil von Band-1-P5):
- *"Da war eine Gestalt. Folge ihr in den hinteren Teil → A1"*
- *"Erst Fakten. Wer liegt hier? Geh ins Stadtarchiv → B1"*
- *"Herr Kloß weiß mehr, als er sagt. Frag ihn → C1"*

**Frau-Silber-Spur auf allen Pfaden (Serien-Faden, Punkt aus Rev. 2):**
Damit kein Leser den Serien-Faden verpasst, taucht der Hinweis *"vor drei Monaten hat schon jemand diese Namen gesucht"* (= Frau Silber) auf **allen drei Pfaden** mindestens einmal auf — nicht nur im Archiv (B):
- **A:** in der ersten Blechdose ein Zettel in fremder, neuerer Handschrift.
- **B:** die Archivarin sagt es direkt (Kanon Kap. 4).
- **C:** Kloß erwähnt eine Frau, die "vor einer Weile" nach dem hinteren Teil fragte.

---

## 4. Akt- & Pfad-Struktur (Time Cave)

Jeder Pfad durchläuft: **Erkundung → erster Geist-Kontakt → der Twist (2 Geister) → Verzweigung in Enden.**

### Pfad A — "Dem Grauen folgen" (~12–14 Abschnitte)
1. A1–A4 Erkundung: namenloser Teil, Kälte messen, "H.B. 1887"-Grab, fliegender Grabstein (Kap. 3).
2. A5–A7 Werkzeugschuppen: eingesperrt, **erste Blechdose**, 23 Namen + "Johann" (Kap. 5).
3. **A8 Wahl:** Brenner ansprechen / zuhören & beobachten / fliehen.
4. A9–A11 **Twist-Pol:** Brenner erscheint (still, zeigt) → Voss schmeißt Stein → Nora erkennt: zwei Geister (Kap. 7). *Dead End D1, wenn Brenner laut konfrontiert wird ("Reden ist nicht Zuhören", Lektion gespiegelt von Band 1).*
5. **A12 Wahl:** sofort befreien (→ Scheitern-Strang, Kap. 9–10) / Voss-Logik verstehen (→ gute Enden).
6. Enden EA1–EA4 (s. Abschnitt 6).

### Pfad B — "Die Ermittlerin" (~11–13 Abschnitte)
> **Gezielte Verbesserung:** In Band 1 war Pfad B der schwächste (3 kritische Abschnitte, zu trocken — Recherche allein gruselt nicht). Band 2 gibt B **eigene physische Horror-Anker**, die nur dort vorkommen, damit B kein "langweiliger Logikpfad" ist.
1. B1–B3 Stadtarchiv: herausgerissene Seiten, "H.B." + "G. Voss", Archivarin-Hinweis auf Frau Silber (Kap. 4).
2. B4 **Wahl:** weiter forschen (Voss-Spur) / zurück zum Friedhof (Schuppen).
3. B5–B7 **B-exklusiver Grusel-Anker 1:** das **Foto, auf dem nachträglich ein Name durchgestrichen erscheint** (Kap. 4 Cliffhanger — der Strich war nicht auf dem Original). Recherche bekommt so einen übernatürlichen Schauer.
4. **B8 Twist-Pol** (Johanns-Zweig-Logik aus §5, hier über Aktenfund): der Poltergeist passt zu Voss, nicht zu "H.B." — Brenner ist Opfer.
5. **B9 Wahl:** Beweise im **unterirdischen Registerbüro** sammeln (Kap. 13 — **B-exklusiver Gruselort:** Gaslicht-Halter, Akten von 1887, klaustrophobisch) / direkt zur Kapelle (riskant → Dead End D4 "Zu viel Eile").
6. Enden EB1–EB3.

### Pfad C — "Kloß vertrauen" (~13–15 Abschnitte, geplant als stärkster Pfad)
1. C1–C2 Kloß schwitzt, Sperrung, 3-Tage-Frist (Bagger Donnerstag). Doppelschatten im Fenster (Kap. 2).
2. **C3 Wahl:** Kloß glauben & abwarten / heimlich selbst forschen.
3. C4–C6 Kloß gesteht die Voss-Geschichte (Urgroßvater = Komplize, Kap. 6).
4. **C7 Twist-Pol:** Mit Kloß' Wissen wird klar: zwei Geister, Voss lebt vom Schweigen.
5. **C8 Wahl:** Kloß zum Reden bewegen / es allein versuchen (→ schwächeres Ende).
6. C9–C11 Unterirdisches Registerbüro, Original-Protokoll (Kap. 13).
7. **Brücke C→Kloß-Finale** (einziger erlaubter Konvergenzpunkt): Kloß spricht Voss' Schuld laut aus (Kap. 14).
8. Enden EC1–EC4 (inkl. das emotional stärkste + Codewort).

### Dead Ends (Lektionen, kein "Game Over")
| ID | Pfad | Lektion | Zurück zu |
|----|------|---------|-----------|
| D1 | A | "Reden ist nicht Zuhören" (Brenner laut anschreien) | A8 |
| D2 | A | **"Theo nicht zurücklassen"** (allein in die Kapelle → man verpasst die Johanns-Zweig-Szene) | A12 |
| D3 | B | "Wissen ohne Handeln befreit niemanden" | B4 |
| D4 | B | "Zu viel Eile macht es schlimmer" (Voss vor Beweisen) | B9 |
| D5 | C | "Lügen isoliert" (Kloß anlügen) | C3 |

---

## 5. Der Twist im interaktiven Format (kritischer Punkt — Rev. 2)

**Korrektur gegenüber Rev. 1:** Der erste Plan reduzierte den Twist auf *"es sind zwei Geister"*. Der Manuskript-Abgleich (Kap. 11) zeigt: der wahre emotionale Hebel ist **Johanns Zweig** — das zusammengebundene Kindergrab-Bündel in der zweiten Blechdose — und die Erkenntnis, dass **Vorlesen allein nicht reicht, solange Voss da ist**. Außerdem spricht im Manuskript *Theo*, nicht Nora, die Lösung aus ("Wir brauchen jemanden, der Voss' Schuld laut ausspricht → Kloß"). Das ist die stärkste Szene des Buchs — sie muss in den Graph.

**Der neu definierte Twist-Pol (auf jedem Pfad ein Pflicht-Abschnitt):**
- **Inhaltlicher Kern:** nicht "2 Geister erkannt", sondern **"Johanns Zweig gefunden + verstanden: Vorlesen reicht nicht, Voss muss angeklagt werden"**. Konkreter, emotionaler, und macht den "Kloß muss reden"-Mechanismus *zwingend* statt behauptet.
- Twist-Pol-Abschnitte: **A-Twist** (A9–A11) / **B-Twist** (B8) / **C-Twist** (C7). Nicht umgehbar für die guten Enden.
- Wer ihn umgeht (sofort "Brenner befreien"), landet im **Scheitern-Strang** (Kap. 9–10 "Alles wird schlimmer") → bitter, aber nie böse. Interaktive Umsetzung von Noras falschem Plan.

**Theo-allein-in-der-Kapelle (Kap. 11) als belohnter Höhepunkt:**
- Schlüssel-Abschnitt auf **Pfad A und C** — erreichbar nur, wenn der Leser vorher Theo *mitnimmt* / das Risiko eingeht (verzweigt aus A12 bzw. C8).
- **POV bleibt bei Nora draußen am Fenster** (`pov: nora_aussen`, s. §1a) — exakt wie im Manuskript.
- Inhalt: zweite Blechdose, **Johanns Zweig**, Theo bleibt strategisch regungslos, Brenner stellt sich zwischen Theo und Voss.

**Der Schatten-Durchbruch (neuer Belohnungs-Beat, aus Kap. 11):**
- Band-2-Sonderregel war bisher nur *"Schatten bleibt außerhalb"*. Das Manuskript hat einen stärkeren Moment: am Höhepunkt **zerreißt Schatten die Leine und springt über den Zaun** — der eine Augenblick, in dem er den Friedhof doch betritt, um Theo zu erreichen.
- **Graph-Beat `schatten_durchbruch`:** wird nur auf den besten Pfaden ausgelöst (Theo-Rettung in A & C). Macht das Schatten-Mysterium *aktiv* statt zur bloßen Abwesenheits-Notiz — und ist ein emotionaler Payoff, der zum Band-3-Hook (warum verweigert er den Friedhof?) führt.
- Auf den Scheiter-/Fluchtpfaden bleibt Schatten draußen — der Durchbruch ist die Belohnung fürs Durchhalten.

---

## 6. Enden-Liste (13 + 1 Geheim) — *festgeschrieben*

> **Designprinzip (Rev. 3):** **13 vollwertige Enden** als echte, befriedigende Szenen — *nicht* als kurze Abbinder. Die Lehre aus Band 1: dort gab es 24 Enden, aber viele waren dünn und „SCHWACH". Ursache war jedoch **nicht** „zu wenige Wörter", sondern **fehlende Szene** (kein Beat, keine Sensorik, kein echter Cliffhanger). → Ziel ist daher **Vollständigkeit der Szene**, *kein* Wortzahl-Minimum (vgl. §0a). Ein Ende ist fertig, wenn es den Pfad emotional schließt und (beim ⭐) das Codewort organisch trägt. Markiert mit ⭐ = bestes Ending des Pfads (trägt Codewort).
>
> **⚠️ Zwei-Gipfel-Regel (festgelegt nach Pfad C, Schritt 4):** Der vorletzte Abschnitt (z. B. C8) trägt den
> **Voss-Bann** = *Spannungs*-Gipfel (Angst → Erleichterung). Das ⭐-Ende (EC1/EA1/EB1) trägt den **Brenner/Johann-Frieden**
> = *Trauer/Wärme*-Gipfel (die 47 Namen, „zwei Jahre und fünf Monate", Brenners lautloses „Danke", Codewort).
> Das sind **zwei verschiedene Gefühle** — das Ende schwächt also nicht ab, es wechselt die Tonart. Manuskript trennt
> das bewusst (Kap. 13 Voss / Kap. 14 Brenner). → **Enden NIE als „und dann lasen sie noch die Namen" bauen**, sondern
> als eigenen emotionalen Gipfel. Voss im vorletzten Abschnitt **ganz** auflösen, damit der warme Beat rein bleibt.

| ID | Titel | Pfad | Ausgang | Codewort |
|----|-------|------|---------|----------|
| EA1 ⭐ | "Der Zeuge spricht" | A | Voss entlarvt, Brenner & Johann befreit, mit Theo | **NAME** |
| EA2 | "Schattens Wache" | A | befreit, aber Schatten-Rätsel offen (Band-3-Hook) | — |
| EA3 | "Allein zu mutig" | A | Scheitern, Brenner bleibt (Kap.-10-Variante) | — |
| EA4 | "Nacht-Flucht" | A | Abbruch, minimaler Hook | — |
| EB1 ⭐ | "Aktenzeichen Voss" | B | über Beweise gelöst, rational-warm | **AKTE** |
| EB2 | "Die halbe Wahrheit" | B | Beweise ja, Befreiung unvollständig | — |
| EB3 | "Zu nah an Voss" | B | Eile-Scheitern | — |
| EC1 ⭐ | "47 und ein kleiner Name" | C | Kloß' Mutmoment, vollständige Befreiung (Kap. 14) | **STIMME** |
| EC2 | "Die Gedenktafel" | C | befreit, Kloß hängt Tafel auf, warm | — |
| EC3 | "Ohne Kloß" | C | allein versucht, Teilerfolg | — |
| EC4 | "Zu spät" | C | Bagger kommen, bittersüß | — |
| E-GEHEIM | "Nicht alleine" | — | Geheim-Ending, Serien-Wort **ERINNERN** | (benötigt NAME+AKTE+STIMME) |

**Codewort-System (kanonisch, Doku-konform):**
- 3 Codewörter: **NAME** (A) · **AKTE** (B) · **STIMME** (C) → kombiniert zum Serien-Wort **ERINNERN**.
- Thema Band 2 = "Vergangenheit/Erinnern" → passt perfekt zu Brenners vergessenen Namen.
- Geheim-Ending-Hinweis am Buchende, Stil wie Band 1 (Kasten/kursiv), führt zu höchster Abschnittsnummer.
- *Begründung NAME/AKTE/STIMME:* alle drei sind im Text organisch unterbringbar (Brenner will Namen; Voss-Akte; jemand muss die Stimme erheben) und ergeben zusammen "sich an Namen erinnern" = ERINNERN.

---

## 7. Qualitäts-Lehren aus Band 1 (Rev. 3 — Ursachen statt Metriken)

Band 1 hatte messbare Schwächen — aber die **Zahlen waren Symptome, nicht Ursachen**. Rev. 3 zielt
auf die Ursachen. Die alte Metrik-Tabelle (Ø 300–350 W, Dialog 35–45 %, Enden ≥ 300 W) ist **gestrichen**.

| Band-1-Schwäche | Eigentliche Ursache | Maßnahme Band 2 |
|-----------------|---------------------|-----------------|
| Abschnitte „SCHWACH/KRITISCH" | fehlender **Beat** (keine Szene, nur Übergang) | Jeder Abschnitt hat *ein* konkretes Ereignis (Schreck, Hinweis, Wahl, Humor). Wenn keiner da ist → Abschnitt streichen/zusammenlegen, nicht strecken. |
| Maschineller Ton | wiederkehrende Satzmuster, Recycling | §0a-Regeln + Anti-Recycling-Liste (unten) bei *jedem* Abschnitt prüfen. |
| Pfad B = schwach (Recherche gruselt nicht) | Logik ohne Körper/Sensorik | B bekommt **eigene physische Grusel-Anker** (durchgestrichener Name im Foto, unterirdisches Registerbüro) — s. §4. |
| Dünne Enden | fehlende Szene, nicht zu wenig Text | Enden als vollwertige Szenen (§6) — Vollständigkeit, kein Wortzahl-Soll. |

**Schatten-Regel Band 2 (verfeinert — KEINE 100 %-Quote):**
Schatten ist außerhalb des Friedhofs und damit *spürbar abwesend* — das ist ein **Stilmittel**, kein
Defizit. `STIL_REFERENZ` warnt explizit vor dem „sprechenden Kuscheltier". Daher:
- Schatten-Reaktionen **variieren** (Mauer, Jaulen, Warten, Schnüffeln, Unruhe) und werden **sparsam &
  bedeutungsvoll** gesetzt, nicht reflexhaft in jeden Abschnitt gestopft.
- In reinen Innen-/Recherche-Szenen darf seine *Abwesenheit* thematisiert werden (Nora vermisst ihr
  Frühwarnsystem) statt einer erzwungenen Außen-Mention.
- Der **Schatten-Durchbruch** (Kap. 11, §5) ist dadurch ein echter Payoff statt Routine.

**Anti-Recycling-Liste Band 2** (in `STIL_REFERENZ.md` führen, beim Schreiben aktiv variieren):
„Schatten an der Mauer", „Kloß schwitzt", „grau und still / Kopf gesenkt" (Brenner), „schwarz, größer
als ein Mensch" (Voss), „roch nach altem Papier", „47 Namen". Diese kehren über viele Abschnitte wieder
— Formulierung jedes Mal frisch.

**Validierung (Rev. 3 — Werkzeug, kein Richter):**
⚠️ **Falle:** `Scripts/validate_graph_v2.py` ist hart auf Band 1 verdrahtet (Graph-Pfad *und*
Report-Output `Band1/CYOA/`, Zeilen ~858/872). Ein naiver „Pfad umstellen"-Lauf würde die
**Band-1-Qualitätsanalyse überschreiben.** → Daher in Schritt 1c **forken** zu
`validate_graph_v2_band2.py` mit eigenem Graph- *und* Output-Pfad. Genutzt für:
- **Graph-Integrität** (Pass/Fail): keine toten Links, alle Enden erreichbar, Codewort-Erreichbarkeit (§9 1c).
- **Diagnose** (kein Pass/Fail): Wortzahl/Dialog/Schatten-Mention nur als **Hinweisliste**. Ein
  „SCHWACH"-Flag löst eine *manuelle Prüfung gegen die §0a-Checkliste* aus — nicht automatisches Auffüllen.
- **Score entschärfen:** die `_calculate_score`-Wortzahl-Boni (250–400 = +2 etc.) neutralisieren,
  damit kurze dichte Abschnitte nicht fälschlich „SCHWACH/KRITISCH" werden (Rev.-3-Linie, §0a).

---

## 8. Datei- & Ordnerstruktur (analog Band 1)

```
Band2/CYOA/
├── Plan_Band2_CYOA.md          (dieses Dokument)
├── KANON.md                    (Faktenblatt aus Manuskript — Schritt 0.5)
├── STIL_REFERENZ.md            (v3-Stil + Anti-Recycling-Liste — Schritt 0.5)
├── graph_skizze.md             (Mermaid-Verzweigung zur Freigabe — Schritt 1a)
├── frontmatter.md              (adaptierte "HALT!"-Seite)
├── graph_v2.yaml               (Single Source of Truth — Schritt 1b)
├── moral_map.md                (Lektionen je Dead End / Ende)
├── prolog/        P01.md … P05.md
├── pfad_a/        A01.md …
├── pfad_b/        B01.md …
├── pfad_c/        C01.md …
├── dead_ends/     D01.md … D05.md
├── endings/       EA1.md … EC4.md, E_geheim.md
└── Illustrationen/ (später, Prompts separat)
```

**Build:** `Scripts/build_cyoa_taschenbuch_v3.py` wird zu `..._band2.py` kopiert; nur `V2_DIR`, `FRONTMATTER_FILE`, `OUTPUT_DIR`, `ILLUSTRATION_MAP` ändern sich. Kein neuer Pipeline-Code nötig.

---

## 9. Arbeitsschritte (Reihenfolge & Freigabe-Punkte)

| Schritt | Ergebnis | Freigabe? |
|---------|----------|-----------|
| **0** | Dieses Planungsdokument (Rev. 3) | ✅ erledigt |
| **0.5** | `KANON.md` (Faktenblatt aus Manuskript) + `STIL_REFERENZ.md` (Band 2, mit Anti-Recycling-Liste). Schnell, faktenziehen. | ✅ kurz prüfen |
| **1a** | **Verzweigungs-Skizze** (Mermaid, alle ~60 Knoten) inkl. **beider Twist-Pol-Varianten** (§1) zur visuellen Prüfung. Noch kein YAML. | ✅ **Topologie + Twist-Pol freigeben** ← **nächster Bauschritt** |
| **1b** | Aus der freigegebenen Skizze: `graph_v2.yaml` komplett (IDs, Targets, Enden, Codewörter, `unique_event` für Schlüsselbeats). | ✅ prüfen |
| **1c** | **Validator forken** → `Scripts/validate_graph_v2_band2.py` (Band-2-Graph-Pfad **und** Band-2-Output-Pfad, damit Band-1-Reports nicht überschrieben werden; Wortzahl-Score entschärft, s. §7). Lauf: erreichbar / keine toten Links / **jedes ⭐-Ende + Geheim-Ende von P5 aus erreichbar** (Codewort-Checkliste). | ✅ grün (Graph-Integrität) |
| 2 | `frontmatter.md` + `moral_map.md` | ✅ |
| 3 | Prolog P1–P5 schreiben → QA-Check | ✅ Ton-Probe |
| 4 | Pfad C (stärkster, als Qualitäts-Benchmark) | ✅ |
| 5 | Pfad A, Pfad B | — |
| 6 | Dead Ends + alle Enden + Geheim-Ending | — |
| 7 | Gesamt-QA (`validate` + `analyze`), Codewort-Konsistenz | ✅ |
| 8 | Build-Script Band 2 + Test-Export docx | ✅ |
| 9 | Illustrations-Prompts (analog Band 1) | optional |

---

## 9a. Bewusst verworfene Ideen (damit sie nicht wiederkommen)

Geprüft und **absichtlich nicht** übernommen — würden das Buch nicht besser machen:
- **Sterne-Bewertung der Enden** (wie Herrenhaus): Das Codewort-System erfüllt die "manche Enden sind besser"-Funktion bereits. Eine zweite Wertungsebene wäre Doppelung und Ballast.
- **Mehr als ~65 Abschnitte:** Band 1 (122 Abschnitte) belegt, dass zusätzliche Abschnitte die Qualität verdünnen. Tiefe statt Menge.
- **Zusätzliche Pfad-Konvergenzen** über den einen erlaubten Punkt (C→Kloß-Finale) hinaus: würde die Time-Cave-Struktur aufweichen.
- **Eigene CYOA-Nebenfiguren/Orte** (lockere Variante): bewusst verworfen zugunsten strikter Kanontreue.

---

## 10. Status der Entscheidungen (vor Schritt 1)

| # | Punkt | Status |
|---|-------|--------|
| 1 | Architektur Time Cave | ✅ entschieden |
| 2 | Strikt kanontreu (Handlung/Figuren) | ✅ entschieden |
| 3 | Typografie **Guillemets »…«** | ✅ entschieden (Rev. 2, §1a) |
| 4 | Twist = **Johanns Zweig** + Schatten-Durchbruch | ✅ entschieden (Rev. 2, §5) |
| 5 | **13 Enden** als vollwertige Szenen (kein Wortzahl-Soll) | ✅ festgeschrieben (§6, Rev. 3) |
| 6 | Codewörter **NAME / AKTE / STIMME → ERINNERN** | ✅ entschieden |
| 7 | Abschnitts-Gesamtzahl: **48** laut Graph (Tiefe statt Menge) — unter Richtwert, gesund | ✅ fixiert nach Schritt 1b (Graph) |
| 8 | POV-Regel `nora_aussen` für Theo-Szenen | ✅ entschieden (§1a) |
| 9 | **Stil = v3 / STIL_REFERENZ**, kein Wortzahl-Ziel; Validator = Werkzeug | ✅ entschieden (Rev. 3, §0a/§7) |
| 10 | Werkzeug-Dateien `KANON.md` + `STIL_REFERENZ.md` + `moral_map.md` vor Prosa | ✅ als Schritt 0.5 (§0b/§9) |

**Alle Entscheidungen getroffen. Plan (Rev. 3) ist abgenommen.**

### Codewort-Festlegung (Detail für die Enden)

| Pfad | Bestes Ende | Codewort | Beispielsatz (final beim Schreiben justierbar) |
|------|-------------|----------|-----------------------------------------------|
| A | EA1 "Der Zeuge spricht" | *NAME* | »Jeder Mensch hat einen NAMEN verdient — auch nach 139 Jahren.« (Kanon: 139, nicht 137) |
| B | EB1 "Aktenzeichen Voss" | *AKTE* | »Die AKTE lügt nicht. Sie erinnert sich, wenn niemand sonst es tut.« |
| C | EC1 "47 und ein kleiner Name" | *STIMME* | »Es braucht nur eine STIMME, die laut ausspricht, was alle vergessen wollten.« |
| → Geheim | E-GEHEIM "Nicht alleine" | Serien-Wort **ERINNERN** | (höchste Abschnittsnummer, stärkster Serien-Hook) |

> **Nächste Schritte (Rev. 3, geschärft):**
> 1. **Schritt 0.5** — `KANON.md` + `STIL_REFERENZ.md` aus dem Manuskript ziehen (schnell, faktenbasiert).
> 2. **Schritt 1a** — `graph_skizze.md`: Mermaid-Verzweigung aller Knoten **inkl. beider Twist-Pol-Varianten**
>    (§1). → **Freigabe von Topologie + Twist-Pol.** Noch kein YAML.
> 3. **Schritt 1b** — `graph_v2.yaml` aus der freigegebenen Skizze (inkl. `unique_event` für Schlüsselbeats:
>    Theo-allein, Johanns Zweig, Schatten-Durchbruch). Danach finale Abschnittszahl fixieren (§10 #7).
> 4. **Schritt 1c** — Validator forken (`validate_graph_v2_band2.py`, eigener Output-Pfad) + Codewort-Erreichbarkeit prüfen.
>
> Sag „los", dann starte ich mit Schritt 0.5, danach lege ich dir die Skizze (1a) zur Freigabe vor.
