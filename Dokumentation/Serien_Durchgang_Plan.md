# Serien-Durchgang — der finale Konsistenz-Durchgang über Staffel 1

> **Auftrag (2026-07-18):** Ein tiefer, vollständiger Durchgang durch alle fünf Bände.
> **Zwei Ziele gleichzeitig:**
> 1. **Staffel 1 abschließen** — *alle* groben Fehler finden und beheben. Kleine bewusst nicht.
> 2. **Fundament für Staffel 2** — die Welt vollständig erfassen, damit Band 6 auf gesichertem
>    Boden steht.
>
> **Warum ein eigener Plan:** Der [Logik-Prüfplan](Logik_Pruefplan.md) ist für **ein** Buch
> gebaut und optimiert auf **Effizienz** (Stichprobe, Stopp-Kriterien). Hier gilt das
> Gegenteil: fünf Bücher, und **Vollständigkeit schlägt Aufwand**. Die Werkzeuge des
> Logik-Prüfplans werden benutzt, seine Abbruchregeln sind **ausgesetzt**.

---

## 0. ★ Was „GROB" heißt — die Definition, ohne die der Durchgang nicht funktioniert

> **Der Test:** *Würde ein Kind, das die Reihe der Reihe nach liest, hier stolpern?*

**GROB ist ein Befund nur, wenn er in eine dieser fünf Klassen fällt:**

| | Klasse | Beispiel aus der Reihe |
|---|---|---|
| **G1** | **Widerspruch zu einem früheren Band** — der Leser erinnert sich | Ein befreiter Geist taucht wieder auf; eine Figur ist plötzlich anders alt |
| **G2** | **Bruch der eigenen Weltregeln** | Ein Toter verlässt Gravenstedt; ein Geist wird mit einer Methode befreit, die laut Kanon nicht funktioniert |
| **G3** | **Illusionsbruch** | „Wir haben **vier Bände** gebraucht" (Band 4, behoben) — Figur oder Erzähler spricht über die Bücher |
| **G4** | **Unbezahltes Setup** — der Leser wartet auf etwas, das nie kommt | Heinrich (B1, 12× erwähnt) wird nie aufgelöst |
| **G5** | **Figur handelt gegen ihre eigene Motivation** | Der Antagonist bremst seinen eigenen Plan (B5, behoben) |

**KLEIN ist alles andere — und wird NICHT behoben:**
Detailabweichungen, die niemand mitschreibt (Augenfarbe, Uhrzeit, Wetter) · Stil und Rhythmus ·
Wortwiederholungen · doppelte Kapiteltitel · alles, was nur beim Nebeneinanderlegen zweier
Bücher auffällt, nicht beim Lesen.

> ⚠️ **Grenzfall-Regel:** Wenn unklar ist, ob grob oder klein — **klein.** Bei fünf
> veröffentlichten Büchern ist jede Änderung ein Neu-Upload und ein neues Fehlerrisiko.

---

## 1. Die Struktur: zwei Durchgänge, nicht einer

**Das ist die wichtigste Abweichung vom Logik-Prüfplan.**

Einen Widerspruch zwischen Band 2 und Band 4 **kann man beim Lesen von Band 2 nicht
erkennen** — dafür müssen Band 4s Fakten schon auf dem Tisch liegen. Deshalb:

### DURCHGANG 1 — Erfassen (nicht urteilen)
Alle fünf Bände Kapitel für Kapitel lesen und in ein **festes Format** eintragen.
**In diesem Durchgang wird nichts bewertet und nichts geändert.** Wer beim Erfassen
urteilt, urteilt ohne die Hälfte der Daten.

### DURCHGANG 2 — Vergleichen und urteilen
Erst wenn alle fünf Bände erfasst sind: Fakten gegeneinanderlegen, Widersprüche
einstufen, dann die groben beheben.

---

## 2. DURCHGANG 1 — das Erfassungsformat

Pro Kapitel **sechs Felder**. Kurz halten — Stichworte, keine Sätze. Was nicht auffällt,
bleibt leer.

```
## B<n> K<nr> — <Titel>

FAKTEN     neue Welt-/Figuren-/Ortsfakten (mit Kurzzitat)
REGELN     Sätze, die behaupten, wie die Welt funktioniert ("kann nicht", "nur wenn")
ZEIT       Zeitangaben, Jahreszeit, Abstände
WISSEN     was Nora/Theo hier NEU erfahren
SETUP/PAYOFF  gepflanzt: … | eingelöst: …
VERDACHT   alles, was sich falsch anfühlt — NICHT bewerten, nur notieren
```

**Warum genau diese sechs:** Sie decken die fünf Grob-Klassen ab. FAKTEN und ZEIT finden G1,
REGELN findet G2, WISSEN findet G2/G5, SETUP/PAYOFF findet G4, VERDACHT fängt G3 und G5.

**Maschinelle Vorarbeit pro Kapitel** (spart die Hälfte der Zeit):
`py Scripts/pruefe_logik.py <band>` liefert Zeitangaben, Zahlen, Namen, Regelsätze und die
Vierte-Wand-Kandidaten schon vorsortiert. Das Lesen muss dann nur noch verifizieren und
ergänzen, was Muster nicht sehen.

---

## 3. DURCHGANG 2 — die sechs Vergleiche

Erst nach vollständiger Erfassung. Jeder Vergleich zielt auf eine Grob-Klasse.

| # | Vergleich | Findet |
|---|---|---|
| **V1** | **Faktentabelle** — jede Figur, jeder Ort über alle 5 Bände nebeneinander | G1 |
| **V2** | **Regeltabelle** — alle REGELN-Einträge untereinander legen | G2 |
| **V3** | **Zeitstrahl** — alle ZEIT-Einträge auf eine Linie | G1 |
| **V4** | **Wissensstand** — was weiß Nora am Ende jedes Bandes? Weiß sie im nächsten mehr/weniger? | G2, G5 |
| **V5** | **Setup/Payoff-Bilanz** — jedes Setup ohne Payoff ist ein G4-Kandidat | G4 |
| **V6** | **Verdachtsliste** — alle VERDACHT-Einträge durchgehen, jetzt mit vollem Kontext | G3, G5 |

---

## 4. Vollständigkeit — die Abbruchregeln sind ausgesetzt

> Der Logik-Prüfplan sagt: *„20 Befunde, keiner 🔴 → aufhören"* und *„Stichprobe zuerst"*.
> **Beides gilt hier NICHT.** Der Auftrag lautet „alle groben Fehler", und man weiß erst am
> Ende, ob man alle hat.

**Fortschritt wird sichtbar geführt** — ein Kapitel gilt erst als erledigt, wenn alle sechs
Felder bearbeitet sind (auch wenn sie leer bleiben):

| Band | Kapitel | erfasst | Befunde | Stand |
|---|---|---|---|---|
| 1 | 18 | ☑ **18/18** | 6 behoben | gebaut, **186 S.**, bereit zum Upload |
| 2 | 15 | ☑ **15/15** | 2 behoben, 2 bewusst offen | gebaut, **113 S.** · ⚠️ **nur `Manuskript_Band2_Komplett.md` lesen** — 13 der 15 Kapiteldateien sind veraltet |
| 3 | 16 | ☑ **16/16** | 1 behoben | gebaut, **106 S.**, Cover passt (`PAGES=106`) |
| 4 | 16 | ☑ **16/16** | 2 behoben (**7.+8. vierte Wand**) | gebaut, **95 S.**, Cover passt |
| 5 | 18 | ☑ **18/18** | **0** — sauber | unverändert, kein Neubau nötig |
| | **83** | **☑ 83/83** | **12 behoben** | Bände 1–4 neu gebaut, bereit |

> **★ Lehre aus Band 4 — die Suche ist immer enger als die Sprache.**
> Der Vierte-Wand-Fix galt als vollständig (6 Stellen, Skript meldete 0). Beim **Lesen** kam
> eine siebte ans Licht: *„seit Band drei"* — Singular statt Plural, Zahlwort statt Ziffer.
> Das ist der **dritte** Fall derselben Art (vorher: Groß-/Kleinschreibung; fehlende
> Wortgrenze bei `\bLeiche`, die „gleichen" traf).
> **Konsequenz:** Ein grüner Skript-Lauf beweist nur, dass das *Muster* nichts findet — nicht,
> dass nichts da ist. Der Lese-Durchgang ist nicht optional.
> ⚠️ **Und: den Vierte-Wand-Check nur gegen das MANUSKRIPT laufen lassen, nie gegen das PDF** —
> der Autoren-Nachspann sagt legitim „weitere Bände" und die Reihenübersicht „Alle Bände".

**Maschinelle Vorprüfung (1a) ist für alle fünf Bände abgeschlossen** — V1 Fakten, V2 Weltregeln,
V3 Zeitstrahl, V4 Wissensstand, V5 Setup/Payoff. Ergebnisse und Grenzen stehen im
[Serien-Kanon](Serien_Kanon.md), Abschnitt 6. Was jetzt noch läuft, ist **ausschließlich 1b**,
der Lese-Durchgang.

**Befunde Band 1** (alle im Kanon Abschnitt 7 mit Begründung): Heinrich-Daten 11×,
Mutter-Beruf 2×, Karte in K13 vorweggenommen 2×, Bellen K08, „Zum ersten Mal" K08.

> **★ Zwei Lehren aus Band 1, die für die restlichen vier Bände gelten:**
> 1. **Im Zweifel ersatzlos streichen statt umformulieren.** Ein Ersatztext behauptet etwas
>    Neues — und kann einen größeren Fehler einbauen als der, den er behebt.
> 2. **Die belanglose Stelle anpassen, nicht die bedeutungstragende.** Bei einem Widerspruch
>    zuerst prüfen, welche der beiden Stellen im Buch Arbeit leistet (Rückbezüge? Steigerung?).
>    Die andere ändern.

**Reihenfolge: 1 → 2 → 3 → 4 → 5.** In Leserichtung, weil G1 (Widerspruch zu einem früheren
Band) nur so entsteht, wie ein Leser ihn erlebt.

---

## 5. Beheben — mit den Regeln, die schon stehen

Für jeden Fix gelten **unverändert** die fünf Grundregeln und die Sicherheitsschleife aus
[Logik_Pruefplan.md](Logik_Pruefplan.md), Abschnitt 0 und 7:
Befund ist Verdacht · nach jedem Fix die Umgebung prüfen · der Fix selbst kann ein Fehler
sein · ein Fix kann einen Altfehler freilegen · das Werkzeug hat auch Fehler ·
**kleinste Änderung, die den Fehler behebt**.

**Zusätzlich für diesen Durchgang:**
- **Erst alle Befunde sammeln, dann in EINEM Rutsch beheben.** Nicht band-weise fixen —
  sonst ändert man Band 2 und merkt bei Band 4, dass die Änderung falsch war.
- **Pro Band einmal neu bauen und hochladen**, nicht mehrfach.
- **Seitenzahl nach jedem Neu-Bau prüfen** — ändert sie sich, muss das Cover nachgezogen
  werden (`build_cover_kdp_band*.py`).

---

## 6. Das zweite Ergebnis: der Staffel-2-Boden

Der Durchgang füllt [Serien_Kanon.md](Serien_Kanon.md) vollständig. **Was dort am Ende
stehen muss, damit Staffel 2 sicher darauf bauen kann:**

- **Weltregeln** — vollständig, mit Belegstelle, inklusive der Grenzen („Tote können die
  Stadt nicht verlassen", „hinüber ≠ weggehen")
- **Figurenblätter** — Alter, Aussehen, Sprechweise, was sie wissen, was sie NICHT wissen
- **Ortsverzeichnis** — jeder benannte Ort mit Band-Referenz
- **Zeitstrahl** — Juli bis November, jedes Ereignis eingeordnet
- **Die zwölf Markierungen** — wer, wo, wann, wodurch befreit
- **★ Offene Fäden** — alles, was nie aufgelöst wurde. Für Staffel 2 ist diese Liste
  **wertvoller als der Rest**: Jeder offene Faden ist entweder ein Geschenk (Aufhänger) oder
  eine Falle (der Leser erwartet noch eine Antwort).
- **★ Was NICHT im Buch steht** — Namen und Fakten, die nur in Planungsdateien existieren.
  *(Bereits gefunden: die Mutter heißt in keinem Buch „Sarah"; der Vater kommt nicht vor.)*

---

## 7. Ehrlicher Aufwand

**83 Kapitel, ~95.000 Wörter.** Mit maschineller Vorarbeit realistisch **8–14 Stunden**,
verteilbar über mehrere Sitzungen — Bandgrenzen sind natürliche Pausen, weil Durchgang 1
band-weise läuft.

**Was der Durchgang NICHT leisten kann:**
- Er findet keine Fehler, die kein Muster und kein aufmerksamer Leser sieht.
- Er beweist nicht, dass **keine** groben Fehler mehr da sind — er beweist, dass keiner mehr
  **gefunden wurde**. Der Unterschied gehört ins Ergebnis geschrieben.
- Er verbessert die Bücher nicht literarisch. Dafür sind Spannungs-, Stimmen- und
  Qualitäts-Prüfplan da.

---

## 8. Abschluss

Der Durchgang ist fertig, wenn:
1. alle 83 Kapitel erfasst sind (Tabelle in Abschnitt 4 vollständig abgehakt),
2. alle sechs Vergleiche aus Abschnitt 3 durchgeführt sind,
3. jeder Befund eingestuft ist (grob/klein) **mit Begründung**,
4. alle groben behoben und die betroffenen Bände neu gebaut sind,
5. `Serien_Kanon.md` die Punkte aus Abschnitt 6 vollständig enthält,
6. **im Kanon steht, was geprüft wurde und was nicht** — kein ✅ ohne durchgeführte Prüfung.

---

## ✅ ABGESCHLOSSEN 2026-07-18 — Ergebnis

**Alle 83 Kapitel gelesen. 11 grobe Fehler behoben, alle in `Serien_Kanon.md` §7 mit
Ist/Neu und Begründung dokumentiert.**

| Band | Behobene Fehler | Seiten (bereit) |
|---|---|---|
| 1 | Heinrich-Daten ×? · Mutter-Beruf ×2 · Karte in K13 vorweggenommen ×2 · Bellen · „Zum ersten Mal" | **186** |
| 2 | Anruf mit noch nicht gefundener Karte · „67 Jahre" → 37 | **113** |
| 3 | unbezahltes Setup (leuchtende Markierungen) | **106** |
| 4 | 7.+8. Bruch der vierten Wand („seit Band drei" · „seit dem ersten Band") | **95** |
| 5 | **keiner** — sauber | unverändert |

**Jeder Eingriff war eine Streichung oder ein Ein-Wort-Tausch** — keine neu erfundenen Sätze.
Jeder wurde am **fertigen Druck-PDF** verifiziert (Leerraum normalisiert), Seitenzahlen
geprüft, Cover-Passung bestätigt.

**Bewusst NICHT behoben** (in §7b mit Begründung): „Morgen"↔„letzten Monat" (B1→2),
H.B.-Kartenbezug (B2), „drei Monate" eingefroren (B1–3), Graven „nie ein Mensch" (B4→5,
gewollter Figuren-Irrtum), sowie mehrere Detail-Grenzfälle.

**Was der Durchgang für Staffel 2 hinterlässt:** `Serien_Kanon.md` ist von ~3.500 auf
~5.900 Wörter gewachsen — vollständige Figurenblätter (inkl. Voss, Marlene, Faber, Graven),
das **Erscheinungs-Repertoire** (fehlte ganz), ein 14-Zeilen-**Ortsverzeichnis**, die
**Echo-Weltregel**, und die Liste der nie erzählten Karteneinträge als Stoffvorrat.

**Drei methodische Lehren** (alle im Kanon/Skript verankert):
1. *Die Suche ist enger als die Sprache* — 3× hat ein zu enges Muster einen echten Fehler
   verdeckt (Groß/klein · Wortgrenze · Singular/Plural). Der Lese-Durchgang ist nicht optional.
2. *Im Zweifel streichen statt ersetzen* — ein Ersatztext kann einen größeren Fehler einbauen.
3. *Eine als unsicher markierte Aussage einer fehlbaren Figur ist ein Erzählmittel* — nur ein
   **Erzähler**-Widerspruch ist ein G1.

> **Ehrlichkeitsklausel (aus Abschnitt 7):** Bewiesen ist nicht, dass **keine** groben Fehler
> mehr existieren — bewiesen ist, dass beim vollständigen Lesen aller 83 Kapitel **keiner mehr
> gefunden wurde**. Fehler, die weder Muster noch aufmerksamer Leser sehen, kann auch dieser
> Durchgang nicht ausschließen.

**Offen:** Bände 1–4 bei KDP hochladen (die neu gebauten Innenteile). Band 5 unverändert.
