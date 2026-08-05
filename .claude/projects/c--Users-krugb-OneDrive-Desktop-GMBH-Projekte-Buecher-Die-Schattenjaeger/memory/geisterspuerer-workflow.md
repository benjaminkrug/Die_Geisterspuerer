---
name: geisterspuerer-workflow
description: Stand und Schreib-Workflow der Buchreihe "Die Geisterspürer" (KDP, 5 Bände)
metadata:
  type: project
---

"Die Geisterspürer" — deutsche Kinder-Grusel-Reihe (10-12 J.), KDP-Selfpublishing, 5 Bände, Stadt Gravenstedt. Repo: Die_Schattenjaeger.

**Stand (2026-06-08):** Band 1 + Band 2 veröffentlicht (Manuskript + Cover fertig; Band 1 auch komplettes CYOA). Band 3 in Arbeit → siehe [[band3-konzept]]. Bände 4-5 nur geplant.

**Pro Band geplant (Buchkonzept/Codewort_System):** Band 3 "Schatten sieht mehr" (Vergeben), Band 4 "Die zugemauerte Tür" (Loslassen, Graven), Band 5 "Der Schleier" (Befreien, Finale). Serien-Codewörter ergeben Silbers Methode: ZUHÖREN, ERINNERN, VERGEBEN, LOSLASSEN, BEFREIEN.

**Dateistruktur:** `BandX/Story_Outline.md`, `BandX/Manuskript/Kapitel_NN.md`, `BandX/CYOA/`, `BandX/Cover/`. Build-Skripte in `Scripts/` (DOCX/EPUB/KDP-PDF, bandfähig). Output in `Output/` (gitignored).

**Schreib-Workflow für einen neuen Band:** (1) Story_Outline.md schreiben (4 Akte, Kapitel-für-Kapitel, oft mit Twist wie Band 2/3). (2) Kapitel einzeln schreiben — VORHER immer Dokumentation/Schreibstil_Regeln + Author_Info lesen. (3) Author_Info Kontinuitäts-Tracker ergänzen. (4) CYOA + 3 Codewörter. (5) Cover + KDP-Beschreibung + Build.

**Nicht-verhandelbare Stilregeln:** Er-Perspektive nah an Nora; Sätze max. 18 Wörter, kein Passiv; 35-45% Dialog; körperliche Emotionen; Schatten (Hund) mind. 1 Reaktion pro Kapitel; jedes Kapitel endet mit Cliffhanger; Grusel-Humor-Balance (Theo), Ausnahme bei Maximal-Ernst-Kapiteln; Geister sind traurig/gefangen, nie böse — Lösung durch Empathie. Details in CLAUDE.md + Dokumentation/.
