# Schreibstil — Ergänzung für Staffel 2 (und alle neuen Texte)

> Angelegt 2026-10-12. Ergänzt `Schreibstil_Regeln_10_Jahre_Die_Geisterspuerer.md`, ersetzt nichts.
> `PLAN_Staffel2.md`, Abschnitt 1a, sah diese Datei für die Deltas von Staffel 2 vor.
>
> **Inhalt bisher:** übersetzungsfreundlich schreiben. Die **Tonalitäts-Deltas** von Staffel 2
> (älteres Nora-Alter, dunklere Grundstimmung, Grusel 6→9) stehen weiterhin in
> `Staffel2/PLAN_Staffel2.md`, Abschnitt 8, und werden hier nicht doppelt geführt.

---

## Übersetzungsfreundlich schreiben

**Warum:** Die Reihe soll auch auf Englisch erscheinen (`Internationalisierung_Vorgehensplan.md`).
Was beim Schreiben markiert wird, muss beim Übersetzen nicht gesucht werden — und wird seltener falsch.

**Grundsatz:** Deutsch ist der Hauptmarkt. **Keine dieser Regeln darf den deutschen Text flacher
machen.** Deshalb heißt es fast überall *markieren*, nicht *vermeiden*.
**Im Zweifel: deutsch schreiben und markieren.**

| # | Regel | So geht's | Beispiel aus dem Bestand |
|---|---|---|---|
| S1 | **Sprachwitze markieren**, nicht verbieten | Eine Zeile in `EN_Hinweise.md` im Manuskript-Ordner des Bandes: `K4 · „Kondenswasser schreibt …" · Wortwitz · Entlastung nach Schreck` — **nicht** als Kommentar im Kapiteltext (siehe unten) | B1 K4: *„Kondenswasser schreibt keine deutschen Wörter!"* |
| S2 | **Wiederkehrende Sätze ins Satz-Register** | Wer einen Satz bewusst wiederholt (Zitat, Motto, Running Gag), trägt ihn in `EN_Bibel/A5_Satz_Register.md` ein und verwendet ihn danach **wörtlich gleich** | Silbers Notizbuch-Motti B3–B5; *„Der Erste ist nicht im Tunnel."* (7× über 3 Bände) |
| S3 | **Stockwerke, Maße, Schulklassen nur, wenn die Handlung sie braucht** | Sonst *oben, unten, ein paar Schritte, eiskalt* — auf Deutsch oft sogar bildhafter | B1: *„zehn Grad"*, *„dreißig Kilo"*; Stockwerke zählen in den USA anders |
| S4 | **Kulturbezüge so, dass sie sich selbst erklären** — oder markieren | Ebenfalls eine Zeile in `EN_Hinweise.md`: `K6 · „wie bei einem Adventskalender" · Kulturbezug` | S2-1 K6: klopfte dreimal, *„wie bei einem Adventskalender"* |
| S5 | **Rätsel, Hinweise, Codewörter nie an deutsche Buchstaben binden** | Keine Anfangsbuchstaben-, Anagramm-, Reim- oder Schreibweisen-Rätsel. Begriffe sind übertragbar, Buchstaben nicht. | Bisher eingehalten: SCHLÜSSEL/KARTE/STIMME sind Begriffe |
| S6 | **Szenen-Absicht mitschreiben** | Im Cliffhanger-Register je Kapitel eine Zeile: *Was soll der Leser fühlen?* | `Cliffhanger_Register_S2-1.md` — eine Spalte mehr |

**Was diese Regeln nicht sind:** kein Verbot von Redewendungen, Witzen oder deutschen Orten. Die
Reihe spielt in Deutschland und soll so klingen.

**Prüfung:** Keine neue Pflichtprüfung. Das Übersetzungs-Skript (`Scripts/en_bibel_extrakt.py`, A11)
liest später `EN_Hinweise.md` ein.

**Warum eine eigene Datei statt `<!-- -->`-Kommentaren im Text** (geändert 2026-10-12): Die
Build-Skripte (`build_ebook_docx*.py`, `build_taschenbuch_docx*.py`) filtern HTML-Kommentare **nicht**.
Ein Kommentar im Kapiteltext würde im gedruckten Buch und im eBook stehen. Die Build-Skripte
umzubauen hieße, über ein Dutzend Skripte anzufassen, die heute funktionieren. Eine Nebendatei kostet
genauso wenige Sekunden und kann nichts kaputt machen. Nachteil: Die Zeile kann vom Text „wegdriften",
wenn ein Satz umgeschrieben wird — deshalb das Zitat mit aufschreiben, nicht nur die Kapitelnummer.
