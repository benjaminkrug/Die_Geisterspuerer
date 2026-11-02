# Fundliste S2-5 „Der letzte Schlüssel" — Logik- und Qualitäts-Prüfplan

> **Stand:** 2026-11-02, nach Stimmen-Pass (Phase 4b), vor dem Bau.
> **Methode:** `Dokumentation/Logik_Pruefplan.md` (Durchgang A maschinell, B Lesen mit acht Fragen, C Fair Play)
> und `Dokumentation/Qualitaets_Pruefplan.md` (Teil A, F1 gemessen; F2 gelesen; Teil B vorgemerkt, weil Cover und
> KDP-Texte noch fehlen). Quelle: Einzelkapitel `Manuskript/Kapitel_01–18.md` (noch nicht kompiliert).
> **Noch nichts am Text geändert** — erst sammeln, dann entscheidet der Autor (Logik-Prüfplan Abschnitt 1.4).
>
> **Werkzeug:** Neu `Scripts/pruefe_logik_s2.py` (dünner Aufsatz auf `pruefe_logik.py`, alle Checks importiert,
> serienweiter Titel-Check jetzt inkl. Staffel 2). `Scripts/pruefe_qualitaet_s2.py` um S2-2 bis S2-5 ergänzt.

---

## Überblick

| Nr | Einstufung | Fund | Kap. | Fix (minimal) |
|---|---|---|---|---|
| L1 | 🟠 | Kapiteltitel „Was bleibt" gibt es schon: **Band 5 K18** | K18 | umbenennen **oder** bewusst als Klammer behalten — Autor |
| L2 | 🟠 | „hauchte Theo" 2× — nicht in der Liste der einfachen Sprechverben (CLAUDE.md) | K1 | 1 Wort je Stelle |
| L3 | 🟠 | Wörtlich gleicher Satz in zwei Folgekapiteln: „Er sah auf die Wand mit den Uhren." | K11/K12 | K12 umformulieren |
| L4 | 🟠 | K18: Schatten schläft nur — keine Reaktion (CLAUDE.md: mindestens eine pro Kapitel) | K18 | ein Satz |
| L5 | 🟡 | „Theo wusste es auch." (POV-Treffer) | K3 | — |
| L6 | 🟡 | Frieda kennt Grete und Ilse — nie ausdrücklich belegt | K12, K13 | — |
| L7 | 🟡 | Halder weiß, dass Konrad „in der Nacht im Frühjahr" starb | K14 | — |
| L8 | 🟡 | Die Kette ist am Ende von K14 draußen, in K15 wieder „unter dem Kragen" | K14/K15 | — |
| L9 | 🟡 | Wiederholte Sätze K4/K14 („nach getaner Arbeit nach Hause") und K12/K16 („wie eine Lampe …") | — | — |
| L10 | ⚪ | Skript meldet K6, K7, K13 „ohne Schatten-Reaktion" | — | Suchmuster zu eng |
| Q1 | 🟡 | K1 ist mit 1.462 W das längste Kapitel und liegt über dem Reihen-Schnitt | K1 | — |
| Q2 | ✅ | Einstieg, Leseprobe, tote Zonen, Entlastungsventil — alle im grünen Bereich, teils Reihen-Bestwert | — | — |
| Q3 | ⏳ | Teil B (Versprechen: Cover/Titel/Beschreibung gegen Buch) — erst prüfbar, wenn Cover und KDP-Text stehen | — | Merkpunkte unten |
| Q4 | ⏳ | A3: keine Leseprobe auf einen nächsten Band — darf **nicht** erfunden werden | Rahmen | Merkpunkt |

**Kein 🔴.** Stopp-Regel des Logik-Prüfplans (Abschnitt 8) wäre fast erreicht: vier 🟠, alle mit Ein-Wort- bis
Ein-Satz-Fix.

---

## Durchgang A — maschinell (`pruefe_logik_s2.py S2-5 --alle`)

| # | Check | Treffer | Bewertung |
|---|---|---|---|
| 1 | Doppelte Kapiteltitel serienweit | 3 | **„Was bleibt" B5K18 = S2-5K18 → L1.** („Der Keller" B1/B3 und „Was jetzt?" S2-3/S2-4 betreffen veröffentlichte Bände, nicht S2-5.) |
| 2 | Zeitangaben | 21 | **alle 21 im Kontext gegen die Zeitlinie geprüft — stimmen** („vor zwei Tagen" Marie = Tag 0; „gestern" in K9–K12 = Tag 1; „seit drei Monaten" = Mai–August; „dritte lange Fahrt in zwei Tagen" K14; „fester als gestern" K17) |
| 3 | Zahlen | 1 | „acht Uhr sieben" (K16) — stimmt mit Theos Handy überein |
| 4 | Sprechverben | 2 | „hauchte" 2× in K1 → **L2** |
| 5 | Verbotene Begriffe | 0 | — |
| 6 | POV | 1 | → **L5** |
| 7 | Schatten-Reaktion | 4 | K6/K7/K13 Fehltreffer (Schatten drückt sich an Frieda, liegt zwischen allen dreien, geht bei Fuß) → **L10**; K18 echt → **L4** |
| 8 | Wiederholte Sätze | 3 | 2 gewollt (L9), 1 Schlamperei → **L3** |
| 9 | Vierte Wand | 0 | — |
| 9 | Schlusssätze | 18 | alle 17 Cliffhanger + leises Schlussbild K18 ✅ |
| 10–12 | Echo / Pronomen / Tageszeit | 12 / 0 / 2 | Echo = Anaphern (gewollt); Tageszeit-Sprünge K5/K7 = Erinnerungen, keine Sprünge ⚪ |

## Durchgang B — Lesen mit acht Fragen

- **B1 Blocking:** Leine, Positionen und Türen K10–K16 nachgezeichnet (Nora an der Tür → tritt in K13 vor; Theo hält
  Schatten K10/K15, lässt in K16 los; Schlüsselbund auf der Schwelle K14). Stimmt.
- **B2 Wissen:** Jede Aussage hat eine Quelle (Nora: „Die hat er geholt. Heute Nacht." ← Friedas „um zwei"; Halder
  kennt Friedas Schloss-Trick, weil die Schublade unversehrt ist; Mamas Übergabe-Satz). Grenzfälle **L6, L7**.
- **B3 Ursache/Wirkung:** Konrads Schloss geht von **seinem** Ende auf (Ablösung), die 96 von **Halders** Ende
  (Aufziehen, Regel in K15 vorher ausgesprochen) — kein „weil jemand es sehr will". Halders Wende hat seit 3f einen
  rationalen Anker („Keine vierzig").
- **B4 Motivation:** Halder wartet den Tag über (K11, seit 3f begründet), holt die Kontrolluhr (Gewohnheit, K10/K13),
  entscheidet in K14 aus Reflex zuerst selbst — stimmig.
- **B5 Weltregeln:** Alle Regel-Sätze nebeneinandergelegt — Sichtbarkeit nur mit Halder (K4, K9, K10, K14, K15),
  Verblassen über Zeit (K9, K10, K14), Rückriss beim Verlassen (K4, K9, K13), zwei Enden (K15) inkl. Konrads K9-Satz
  (seit 02.11. regelkonform). **Kein Widerspruch.**
- **B6 Gegenstände:** Brief, Zeitungen, Kontrolluhr (Wand → Tasche K13 → Schulter K14 → behält K17), Reiseuhr,
  Kette (L8), Schlüsselbund, Stofftasche, Mütze (weg K4 → fehlt K9/K14 → wieder da nach der Ablösung). Lückenlos.
- **B7 Figurenstimme:** Theo 11, Frieda knapp, Halder ruhig, Mama warm; nach Punkt 4 keine zu runden Kindersätze
  mehr. Sprechverben → L2.
- **B8 Serien-Kontinuität:** gegen die Bücher geprüft (nicht gegen Pläne): Band 5 November („seit November leuchtet"),
  S2-2 Werkstatt-Inventar, S2-3 Feuer/Ilse/Standuhr, S2-4 Marie/Ampel. Hält.

## Durchgang C — Fair Play

- **Wächter → Ablösung (K14):** Hinweise K1 (nummerierte Kästen, Tore der Reihe nach), K2 („stempelt", „Es kommt
  immer einer", Blick den Weg hinunter), K9 (Übergabesatz, „bis einer kommt", „Um sechs kommt einer", „Dich hat
  keiner geschickt"), K10/K13 (Kontrolluhr auf kurz vor sechs, „als würde er auf etwas warten"). Alle vor K14. Für
  Kinder, die das Wort „Schichtablösung" nicht kennen, ist die Zahl der Hinweise angemessen — nicht zu viele. 🟡
- **Feuer → vierzig Minuten (K6/K12):** Kette S2-3 K12 → S2-5 K5 (Zeitungen ohne Uhrzeit) → K6 (Brief). ✅
- **Reiseuhr → Halders Uhr (K12/K15):** S2-2 K6 → S2-5 K6 (erinnert) → K12. ✅

---

## Die 🟠-Befunde im Einzelnen

### L1 · 🟠 · Kapiteltitel „Was bleibt" doppelt (Band 5 K18)
Der serienweite Check hat in Band 1/3 schon einmal einen echten Fehler gefunden („Der Keller"). Hier ist die
Dopplung **möglicherweise sinnvoll**: Beide sind das letzte Kapitel einer Staffel. Aber nichts in der Planung
dokumentiert das als Absicht — und im Inhaltsverzeichnis zweier Bände derselben Reihe wirkt es eher wie Versehen.
- **Option a — bewusst behalten** und als Klammer dokumentieren (Staffel 1 und 2 enden gleich benannt).
- **Option b — umbenennen**, z. B. „Einen echten." (der Kuchen-Zettel, das erste Bild des Kapitels) oder „Erster
  Schultag". ⚠️ Nicht „Vier Schläge" — bei Kindern doppeldeutig.

### L2 · 🟠 · „hauchte" (K1, 2×)
`"Was war das?", hauchte Theo.` · `"Vier", hauchte Theo. "Fünf."` — CLAUDE.md: nur einfache Sprechverben.
„flüsterte" geht nicht: K1 hat schon fünf „flüsterte" (Theos Flüster-Tic, Zwischenanalyse F1).
- Fix: `"Was war das?", fragte Theo leise.` · `"Vier", murmelte Theo. "Fünf."` (Echo auf sein „Eins, zwei, drei",
  murmelte Theo — dieselbe Zählung, dasselbe Verb).

### L3 · 🟠 · „Er sah auf die Wand mit den Uhren." in K11 und K12
Wortgleich, ein Kapitel auseinander.
- Fix K12: „Er sah an Frieda vorbei, an Theo vorbei, an den Regalen vorbei. **Bis zu den Uhren an der Wand.** Auf
  die runde, schwere Uhr …" — setzt die „vorbei"-Reihe fort, statt sie mit dem Wiederholungssatz abzubrechen.

### L4 · 🟠 · K18: Schatten ohne Reaktion
Er schläft im Sonnenstreifen — schönes Schlussbild, aber keine Reaktion. Der Epilog ist kein Grund, die
Serienregel auszusetzen, wenn ein Satz reicht.
- Fix: nach Theos „Das Codewort ist übrigens immer noch Kuchen.": „Schatten hob bei dem Wort ein Ohr, ohne die
  Augen aufzumachen." (Humor, Reaktion, und das Wort „Kuchen" bekommt einen dritten Zeugen.) Letzter Satz bleibt
  unberührt.

## Die 🟡-Befunde (stehen lassen, notiert)

- **L5:** Nora weiß, dass Theo es weiß — beide saßen in S2-3 K12 in Halders Küche. Schluss, kein POV-Bruch.
- **L6:** Frieda hat in S2-2 Gretes Befreiung beobachtet (S2-3 K7 Theo: „Sie hat die ganze Zeit zugesehen") und lebt
  in dem Haus, in dem Ilse als Geist war. Plausibel, ohne Beleg im Text.
- **L7:** Halder hat in S2-4 K16 nach den früheren Bewohnern gefragt. Plausibel.
- **L8:** Zwischen K14 und K15 liegt die Fahrt — dass er die Kette wieder einsteckt, braucht keinen Satz.
- **L9:** K4/K14 und K12/K16 sind bewusste Echos (Konrad geht „wie jemand, der nach getaner Arbeit nach Hause
  geht"; Halder erkennt in K16 das Leuchten von damals).
- **L10 (⚪):** `pruefe_logik.check_schatten` kennt „drückte sich gegen", „bei Fuß"/„neben seinem Bein", „lag
  zwischen" nicht. Bei Gelegenheit Muster erweitern (Regel 5) — nicht jetzt.

---

## Qualitäts-Prüfplan

### Teil A — gemessen (`pruefe_qualitaet_s2.py`, alle Bände nebeneinander)

| Kennzahl | Richtwert | S2-5 | Reihe |
|---|---|---|---|
| Wörter bis zur ersten Figurenrede | ≤ 150 | **12** ✅ | 32–151 |
| Wörter bis zum ersten Unheimlichen | ≤ 270 | **40** ✅ (gelesen: echter Grusel ab Schatten am Fenster, ~300 W — unkritisch) | 0–213 |
| Dialog K1 | ≥ 25 % | **46 %** ✅ | 26–49 % |
| Länge K1 | ≤ Ø Reihe | **1.462 W** 🟡 (Ø ~1.050) | 979–1.348 |
| Ø Kapitellänge | — | 1.057 W | 835–1.159 |
| Amazon-Leseprobe (~10 %) | ≥ 5 Signale | **1.913 W, 22 Signale** ✅ | 5–32 |

**Q1 (🟡):** K1 ist lang, aber er trägt zwei Szenen mit Haken (Schatten am Fenster um Mitternacht, die rüttelnden
Tore). Kürzen hieße eine der beiden schwächen. Qualitätsregel: im Zweifel stehen lassen.

### F1 — Struktur (gleiche Messung wie `pruefe_qualitaet.py`, auf alle Bände)

| Band | längste tote Zone | Schreck → Theo Ø | Schrecken ohne Theo |
|---|---|---|---|
| Band 1 | 321 W (K2) | 2,8 Abs. | 12 von 43 |
| Band 5 | 220 W (K11) | 3,9 | 12 von 22 |
| S2-2 | 514 W (K5) | 5,9 | 1 von 8 |
| S2-3 | 759 W (K3) | 4,8 | 3 von 9 |
| S2-4 | 233 W (K13) | 3,5 | 4 von 33 |
| **S2-5** | **159 W (K6)** ✅ Reihen-Bestwert | **1,8** ✅ Reihen-Bestwert | 4 von 9 (K4/K12 humorfrei geplant) |

### F2 — gelesen
- **Grusel:** Konkret und malbar (Tore der Reihe nach, der Faden aus der Schwelle, das Netz mit leeren Enden),
  Steigerung innerhalb der Szene (K1, K4, K10), nie Körperhorror. **Endet nach K10** — vom Autor bewusst so
  entschieden (emotionales statt gruseliges Finale).
- **Humor:** Kommt aus Theo (Angst und trotzdem weitermachen: „Ich red, wenn ich Angst hab"), Timing nach dem
  Schreck; zwei humorfreie Kapitel (K4, K12) wie geplant.
- **Herz:** stark — Konrad und Kalles Brötchen, Halder auf dem Boden („Ich hab's geschafft"), Frieda „Ich wollte
  wissen, ob du kommst", Theo „ich", Nora backt den Kuchen. Mit dem Geist fühlt man mit.

### Teil B — vorgemerkt für Cover und KDP-Text (Q3)
1. **Kein „gruseligster Band"** versprechen — der Grusel liegt in der ersten Hälfte; das Finale ist emotional.
2. **Beschreibungs-Tempo:** Ablösung, Aufziehen und Befreiung der Neunundneunzig **nicht** nennen (zweite Hälfte).
3. Als **Band 5 / Abschluss von Staffel 2** kennzeichnen — das Buch ist ohne die Vorbände nur halb lesbar.
4. Jede Aussage gegen das Buch prüfen (Memory „Verkaufstexte nie geprüft": 19 Faktenfehler in Staffel 1).

### A3 — Leseprobe auf den nächsten Band (Q4)
S2-5 ist das Staffelfinale, ein nächster Band existiert nicht. **Keine Leseprobe ins Buch** — in Band 1–4 waren sie
erfunden. Falls der Rahmen-Text einen „Ausblick" bekommt, nur mit echtem Text.
