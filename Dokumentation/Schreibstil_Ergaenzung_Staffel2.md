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
| S1 | **Sprachwitze markieren**, nicht verbieten | Kommentar direkt über dem Absatz: `<!-- EN: Wortwitz, Funktion: Entlastung nach Schreck -->` | B1 K4: *„Kondenswasser schreibt keine deutschen Wörter!"* |
| S2 | **Wiederkehrende Sätze ins Satz-Register** | Wer einen Satz bewusst wiederholt (Zitat, Motto, Running Gag), trägt ihn in `EN_Bibel/A5_Satz_Register.md` ein und verwendet ihn danach **wörtlich gleich** | Silbers Notizbuch-Motti B3–B5; *„Der Erste ist nicht im Tunnel."* (7× über 3 Bände) |
| S3 | **Stockwerke, Maße, Schulklassen nur, wenn die Handlung sie braucht** | Sonst *oben, unten, ein paar Schritte, eiskalt* — auf Deutsch oft sogar bildhafter | B1: *„zehn Grad"*, *„dreißig Kilo"*; Stockwerke zählen in den USA anders |
| S4 | **Kulturbezüge so, dass sie sich selbst erklären** — oder markieren | `<!-- EN: Kulturbezug -->` | S2-1 K6: klopfte dreimal, *„wie bei einem Adventskalender"* |
| S5 | **Rätsel, Hinweise, Codewörter nie an deutsche Buchstaben binden** | Keine Anfangsbuchstaben-, Anagramm-, Reim- oder Schreibweisen-Rätsel. Begriffe sind übertragbar, Buchstaben nicht. | Bisher eingehalten: SCHLÜSSEL/KARTE/STIMME sind Begriffe |
| S6 | **Szenen-Absicht mitschreiben** | Im Cliffhanger-Register je Kapitel eine Zeile: *Was soll der Leser fühlen?* | `Cliffhanger_Register_S2-1.md` — eine Spalte mehr |

**Was diese Regeln nicht sind:** kein Verbot von Redewendungen, Witzen oder deutschen Orten. Die
Reihe spielt in Deutschland und soll so klingen.

**Prüfung:** Keine neue Pflichtprüfung. Das Übersetzungs-Skript (`Scripts/en_bibel_extrakt.py`, A11)
sammelt die `EN:`-Markierungen später ein.
