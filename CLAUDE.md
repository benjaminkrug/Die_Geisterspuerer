# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a **creative writing project** for a German children's book series titled **"Die Geisterspuerer"** (The Ghost Trackers). It is a self-publishing project targeting Amazon KDP. The repository contains planning documents, style guides, and story outlines — no source code.

- **Genre:** Horror/Suspense with Humor (Grusel-Humor) for children ages 10-12
- **Language:** All content is written in German
- **Planned scope:** 5-book series set in the fictional city of Gravenstedt
- **Parallel series:** Runs alongside "Die Herrenhaus-Detektive" (ages 8-10, crime/mystery, no supernatural elements)

## Repository Structure

```
Band1/ ... Band5/          — Per-book content (Manuskript/, CYOA/, Cover/)
Dokumentation/              — Series-wide guides
Scripts/                    — Shared build scripts
Output/Band1/ ... Band5/   — Generated files (in .gitignore)
```

## Key Documents

| File | Purpose |
|------|---------|
| `Dokumentation/Die_Geisterspuerer_Buchkonzept.md` | Series concept, market positioning, pricing, Amazon categories, cover direction |
| `Dokumentation/Die_Geisterspuerer_Author_Info.md` | Writing instructions, character profiles, continuity tracker, setting details |
| `Dokumentation/Schreibstil_Regeln_10_Jahre_Die_Geisterspuerer.md` | Detailed writing style rules for the target age group |
| `Band1/Story_Outline.md` | Band 1 chapter-by-chapter breakdown, 4-act structure, series arc (Bands 1-5) |

## Series Architecture

**Main characters:** Nora (12, rational older sister, POV character), Theo (10, sarcastic anxious brother), Schatten (dog, ghost detector — must appear in every chapter).

**Overarching mystery:** Gravenstedt was founded in 1823 by alchemist Alwin Graven, whose failed experiment trapped the dead in the city. A woman named Frau Silber freed ghosts for 40 years before disappearing. The children discover her apartment and continue her work.

**5-Book plan:** Each book focuses on a different ghost with escalating scare levels (3/10 to 8/10). Ghosts are sad/trapped people, never demonic — empathy and understanding free them, not fighting.

## Critical Writing Rules

When generating manuscript text, these rules from the style guides are **non-negotiable**:

- **Perspective:** Third person close to Nora (Er-/Sie-Perspektive). Only what Nora perceives.
- **Sentence length:** 10-15 words target, 18 words max. No passive voice.
- **Paragraphs:** 3-6 lines. Generous whitespace. Single-sentence paragraphs allowed for shock moments.
- **Dialog:** Minimum 35-45% per chapter. Short and snappy. Simple verbs only (sagte, fluesterte, rief, murmelte, zischte).
- **Emotions:** Always physical, never abstract. "Ihr Nackenhaare stellten sich auf" not "Sie fuehlte ein seltsames Gefuehl."
- **Horror-Humor balance:** After scary moments, humor within 1-2 paragraphs (usually from Theo). 2-3 exceptions per book are acceptable where dramatic pacing demands it.
- **Pacing:** Something must happen every 1-2 pages (scare, clue, surprise, humor).
- **Schatten (dog):** At least one reaction per chapter (growls, hackles, refuses room, pulls toward something, etc.).
- **Chapter endings:** Every chapter must end with a cliffhanger.
- **Chapter length:** Target 1,400-1,600 words — guideline, not a hard requirement. A chapter is done when it works, not when a number is reached. Minimum ~1,200 words (enough room for scene + dialog + atmosphere). Short chapters are better than padded ones.
- **Vocabulary:** Concrete, age-appropriate. Use "Erscheinung" not "Manifestation", "uebernatuerlich" not "paranormal", "Gestalt/Wesen" not "Entitaet".

## Content Boundaries

- No violence against children, no blood/decay/body horror
- Ghosts are sad, angry, or desperate — never evil or demonic
- Scares should tingle, not cause nightmares
- When in doubt: add humor

## Differentiation from Herrenhaus-Detektive

| Aspect | Herrenhaus-Detektive | Die Geisterspuerer |
|--------|----------------------|-------------------|
| Age group | 8-10 | 10-12 |
| Setting | Rural village (Eichenhain) | Large city (Gravenstedt) |
| Supernatural | No (rational explanations) | Yes (ghosts are real) |
| Team | 3 friends | 2 siblings + dog |
| Tone | Cozy mystery | Grusel with humor |
