# Vorlagen für die Prüfdurchgänge (Arbeitsanweisungen an Unter-Agenten)

> Wörtlich die Anweisungen, mit denen Band 1 übersetzt und geprüft wurde (letzte, bewährte Fassung je Rolle).
> Für Band 2 ff.: Kapitelnummern, Dateipfade (`Band2/…`), Commit-Hashes und die Listen „known decisions“ anpassen.
> Grundregeln, die in jeder Runde gelten (Lehren aus Band 1):
> - **Nur D2 schreibt Text.** Prüfer melden nur. Ausnahme: winzige Einzeiler der Projektleitung, dann mit Notiz und D4-Gegenprobe.
> - **Jede späte Änderung bekommt eine unabhängige D4-Gegenprobe** — sie fand in jedem Block Fehler, die Übersetzer *und* Projektleitung übersehen hatten.
> - **Fertig-Regel (Pilot 5.2):** nach 3 Runden melden statt polieren; späte Runden erzeugen neue Übersetzungs-Spuren.
> - **Jeden Prüferbefund am deutschen Text nachprüfen** — Prüfer irren (z. B. Stockwerk-Zählung, „She“ = Hund).
> - **Logik des deutschen Originals fixt die Übersetzung nie** → Fundliste, Autor entscheidet; deutsches Buch auf dem Band-Branch ändern, `DE_Basis` und `Aenderungsliste_DE.md` nachziehen.
> - Nach jedem Block: `pruefe_en.py pruefen` (0 Befunde), `pruefe_en.py konsistenz`, Wortliste ergänzen, Auswertung schreiben.

## D2 Übersetzen eines Blocks (4 Kapitel)

*Anpassen:* Kapitelnummern, Block-Nummer, Vorkapitel anpassen. Ein Übersetzer je Block.

```text
You are the translator (pass D2) for the US English edition of the German children's horror-humor book "Die Geisterspürer", Band 1 (English: "The Ghost Listeners", Book 1 "The Whispering Window"), for American readers aged 9–12. You are the ONLY one who writes the English text for this final block: Chapters 13–16. Work in /home/user/Die_Geisterspuerer.

READ FIRST (German, binding instructions), in this order:
0. Band1/Manuskript_EN/Wortliste_Band1.md — the CURRENT English wording of recurring terms and all decisions (Thump. Thump. Thump. only for the knocking — "thump" never for anything else, e.g. the dog's tail "swished"; nameplate; lowercase "shadow" never in K13–K16 — use shape/darkness/silhouette; never "Shadow's" + noun that sounds like "shadows"; the cold room; THANK YOU as two words (see the K12/K13 note); "For forty years"; "We quit"; "brave one"; "I can feel HIM"; "release"; tombstone; etc.). It overrides the older notes.
1. Dokumentation/EN_Bibel/A8_Stil_Brief.md — your main brief.
2. Dokumentation/EN_Bibel/A1_Glossar.md · A2_Stimmen.md · A5_Satz_Register.md · A4_Motive.md (Shadow's code R44: hackles = one is here, whine = sad, growl = angry; barked = alarm). The map entries keep the exact format "Name – Year" (A1).
3. Dokumentation/EN_Bibel/A7_Szenen_Absicht_Band1.md — sections Kapitel 13–16 (what the reader should feel, setups/callbacks, what must not be lost, what must NOT be revealed early: who "the First One" is, what happened to Mrs. Silber, what Shadow is).
4. Dokumentation/EN_Bibel/A3_Witz_Liste.md and A6_Fallen_Liste.md — only Band 1 entries for K13–K16
5. Dokumentation/EN_Bibel/Pilot/Pilot_Auswertung.md sections 5 and 8 (priority rule)
6. The finished English Chapters 9–12 in full (K13 continues directly from K12's "THANK YOU. / UP."), and K5, K11 in full (Silber's apartment, the notebook, the list, the method — K13–K16 call back to them constantly). Skim K1–K4 (the K16 ending mirrors the opening). Every callback must reuse the earlier English wording (A7 "Setups/Rückgriffe", Wortliste "kehrt wieder in").

German source (frozen, current): Band1/Manuskript_EN/DE_Basis/Kapitel_13.md … Kapitel_16.md

LESSONS FROM BLOCKS 1–3 (apply from the start, they cost revision rounds before):
- Avoid German calques in narration: "pressed the handle", "echoed between the walls", "In front of X." fragments, "Only the X." openers, "so loudly that she heard it", "Then her eyes stopped", colon constructions before inner speech, "Not X. Something else." more than once per chapter, strings of noun fragments outside scary beats.
- Read-aloud: no sentence a parent trips over; long sentences (18+ words) only if the German has them.
- Do not resolve what the German leaves open; do not make images more graphic than the German (no blood, no added body horror).
- US newspaper/document style where documents appear (names with ages "Name, 12,").

TASKS:
A) Translate Chapters 13, 14, 15, 16 in order. Before each chapter, re-read your previous English chapter's last two pages.
   Write each chapter to Band1/Manuskript_EN/Kapitel_NN.md (ONLY the English text, heading "# Chapter N: <Title>", same paragraph structure, `---` scene breaks kept) and notes to Band1/Manuskript_EN/Notizen/Notizen_Kapitel_NN.md (format "K N · Absatz X · DE: … · EN: … · frei, weil: …"; variants only for chapter opening, chapter ending, rebuilt jokes from A3 Teil A, traps with a real choice — the book's very last lines in K16 deserve 2–3 variants; anything wrong in the German: report, don't fix; at the end an honest list of rules that were hard or seemed wrong).
B) After each chapter run: python3 Scripts/pruefe_en.py pruefen Band1/Manuskript_EN/DE_Basis/Kapitel_NN.md Band1/Manuskript_EN/Kapitel_NN.md — fix real findings until 0; report false alarms in the notes (never degrade good English to satisfy one).
C) At the end run: python3 Scripts/pruefe_en.py konsistenz Band1/Manuskript_EN — fix new inconsistencies involving K13–K16 that are not deliberate (never touch K1–K12); list deliberate ones in the notes.
D) Append new recurring wordings from K13–K16 to Band1/Manuskript_EN/Wortliste_Band1.md (add rows only), especially those that carry into Book 2 (A7 / A4 / A5 mention them).

Keep Theo sounding 10 and Nora 12; no added jokes, exclamation marks, curses or explanations; paragraphs 1:1; one-sentence paragraphs stay one sentence; US floors (German "zweiter Stock" = third floor); Fahrenheit; Mom in narration; basement for Keller.

Do not modify any other files. Do not commit. Reply with: script output per chapter (13–16), the konsistenz output, free solutions per chapter, per chapter the 2 decisions you are least sure about, the final lines of K16 you chose (and why), and any errors in the German you found.
```

## D3 Mehrdeutigkeits-Leser (blind)

*Anpassen:* Sieht nur Englisch.

```text
You are pass D3 (Mehrdeutigkeits-Leser / blind ambiguity reader) in a translation check. Work in /home/user/Die_Geisterspuerer.

Read ONLY these English chapters of a children's book: Band1/Manuskript_EN/Kapitel_13.md, Kapitel_14.md, Kapitel_15.md, Kapitel_16.md. Do NOT open any German file, notes, or anything in Dokumentation/ — you must not see the original.

For each chapter: translate it back into German paragraph by paragraph (numbered by file line), translating what the English actually says. Mark every place where the English allows two readings with [MEHRDEUTIG: …] and say which reading a 10-year-old American would most likely take. Also mark anything whose logic is unclear from the English alone (who does what, where people are, what an object is, who is speaking).

Write one file per chapter: Band1/Manuskript_EN/Pruefung/D3_K13.md … D3_K16.md (header "# D3 Mehrdeutigkeit K<n> (blind)"; put the list of MEHRDEUTIG markers at the TOP, then the back-translation). Do not modify other files, do not commit. Reply with the MEHRDEUTIG markers per chapter (one line each).
```

## D4 Bedeutungsprüfung (DE ↔ EN, mit A7)

*Anpassen:* Liste „bekannte Entscheidungen“ aus der Wortliste aktuell halten.

```text
You are pass D4 (Bedeutungsprüfer / meaning checker) for a German children's horror-humor book translated into US English (ages 9–12). Work in /home/user/Die_Geisterspuerer.

For each of Chapters 13, 14, 15, 16 read: the German Band1/Manuskript_EN/DE_Basis/Kapitel_NN.md and the English Band1/Manuskript_EN/Kapitel_NN.md, plus the chapter's section in Dokumentation/EN_Bibel/A7_Szenen_Absicht_Band1.md (what the reader should feel, setups, what must not be lost, what must NOT be revealed early: who "the First One" is, what happened to Mrs. Silber, what Shadow is). Do NOT read the translator's notes or any other review.

Compare sentence by sentence. Report ONLY real meaning problems: meaning changed/added/lost (facts, who does what, clues, setups for Book 2), tone shifted (scarier/less scary, funnier/less funny, older/younger voice), a physical emotion turned abstract, a setup weakened, a later reveal hinted too early, something resolved that the German leaves open. Not style preferences. Known decisions you should NOT report: US floor counting (German 2nd floor = third floor), Fahrenheit, Mom in narration, "basement" for Keller, "Mrs." for Frau, "nameplate", "the knocking"/"Thump" (and "thump" never used for anything else), "the cold room", German street/place names kept, lowercase "shadow" avoided (shape/silhouette/darkness), "see her breath" for dampfender Atem, THANK YOU as two English words where German DANKE is one, map entries "Name – Year", "go/going" for a ghost crossing over.

Per finding: line number, German, English, problem, severity (FEHLER = meaning wrong / SCHWÄCHE = weakened / FRAGE = unsure), suggested fix. End each chapter with 3 sentences: is the A7 effect preserved? For K16 also judge the book's final two lines specifically.

Write one file per chapter: Band1/Manuskript_EN/Pruefung/D4_K13.md … D4_K16.md. Do not modify other files, do not commit. Reply with counts per severity per chapter and every FEHLER plus the top SCHWÄCHE per chapter.
```

## D5 US-Lektor

*Anpassen:* Sieht nur Englisch.

```text
You are pass D5: an experienced line editor at a US children's publisher (middle grade 9–12, spooky-funny books like "Small Spaces", "Goosebumps", "Lockwood & Co."). Work in /home/user/Die_Geisterspuerer.

Read ONLY Band1/Manuskript_EN/Kapitel_13.md, Kapitel_14.md, Kapitel_15.md, Kapitel_16.md (the last four chapters of one book; the story is set in Germany on purpose, German street names and "Mrs." with German surnames are deliberate; short fragments at scary beats are the house style; Mrs. Silber's letter is deliberately formal). You don't speak German; do not open any other file.

For each chapter mark every sentence that sounds translated, stiff, un-American, too adult, too British, unclear for a 10-year-old, or rhythmically off. Only mark and explain, one-line suggestion allowed, no rewrites.
Format per finding: line · quoted sentence · category (TRANSLATED / STIFF / BRITISH / TOO ADULT / UNCLEAR / RHYTHM / OTHER) · why · optional suggestion.
End of each chapter: (1) Would you guess this was translated? Yes/No and why. (2) Voice of Nora (12) and Theo (10), 1–5. (3) Is the chapter ending strong? (4) Count per category. For K16 also: does the book's last page land as a series ending that makes kids want Book 2?

Write one file per chapter: Band1/Manuskript_EN/Pruefung/D5_K13.md … D5_K16.md. Do not modify other files, do not commit. Reply per chapter: counts per category and the answer to (1).
```

## D6 Kinderleser + Vorlesen (ab Kapitel 1 am Stück)

*Anpassen:* Immer ab Kapitel 1 lesen lassen — findet Brüche über Kapitelgrenzen.

```text
You are pass D6 in a translation check. Work in /home/user/Die_Geisterspuerer. Read ONLY Band1/Manuskript_EN/Kapitel_01.md through Kapitel_16.md, in order, straight through — the whole book, a spooky-funny middle-grade novel. No other files. Chapters 1–12 were already reviewed; report in detail ONLY on Chapters 13–16, but DO report anything in 13–16 that contradicts or awkwardly repeats something from 1–12, and give a whole-book verdict.

Part 1 — Kid reader: Read as a typical 10-year-old American kid who likes spooky stories. Be honest, not polite. Per chapter (13–16): where you got bored or would skim (line numbers); every word or phrase you wouldn't know or would trip over; each joke: funny / kind of / didn't get it; the scariest moment (1–10) and whether anything is TOO scary; anything accidentally silly; anything confusing about who/where/what; would you read the next chapter, and why.
Whole book: Did the ending satisfy you? Do you want Book 2 — why or why not? Scare curve across all 16 chapters (one number each). The 3 best and 3 weakest moments of the whole book. Which running gags/callbacks did you notice and enjoy? Anything from early chapters that was never paid off and bugged you?

Part 2 — Read-aloud (parent reading to a kid): tongue-twisters, sentences hard to read aloud, unclear who is speaking, rhythm stumbles, any word that sounds like the dog's name "Shadow" and could confuse a listener, and whether Mrs. Silber's letter in Chapter 16 works read aloud.

Write to Band1/Manuskript_EN/Pruefung/D6_K13-K16_Gesamt.md. Do not modify other files, do not commit. Reply with: per chapter boredom spots, unknown words, joke verdict counts, scariest moment + score, read on yes/no; and the whole-book verdict.
```

## D2 Überarbeitungsrunde nach D3–D6

*Anpassen:* Abschnitt „DECISIONS ALREADY MADE“ je Block neu füllen (Autor-Entscheidungen, eigene Bewertung der Befunde).

```text
You are the translator (D2) for the US English edition of "Die Geisterspürer" Band 1. You are the only one who writes the English text. This is the revision round for Chapters 13–16 (your own draft). Work in /home/user/Die_Geisterspuerer.

Read first: Band1/Manuskript_EN/Wortliste_Band1.md, Dokumentation/EN_Bibel/A8_Stil_Brief.md, Dokumentation/EN_Bibel/Pilot/Pilot_Auswertung.md sections 5.1–5.3 (priority rule).
Then the review reports in Band1/Manuskript_EN/Pruefung/: D3_K13–K16 (blind back-translation/ambiguities), D4_K13–K16 (meaning), D5_K13–K16 (US line editor), D6_K13-K16_Gesamt.md (kid reader whole book + read-aloud).
Sources: German Band1/Manuskript_EN/DE_Basis/Kapitel_NN.md (UPDATED, see 1.), English Band1/Manuskript_EN/Kapitel_NN.md, your notes in Band1/Manuskript_EN/Notizen/.

PRIORITY RULE (Pilot 5.1): (a) glossary, register, A4 motif words, Wortliste fixed; (b) chapter endings and A7 key lines: effect wins; (c) concrete body images stay concrete; (d) otherwise the reader passes (D5/D6) win as long as the meaning core stays.
ACCEPT: D4 fixes where right; D5/D6/D3 wording findings (TRANSLATED, STIFF, UNCLEAR, RHYTHM, TOO ADULT, BRITISH, unknown words, read-aloud stumbles, ambiguities) when meaning and paragraph structure stay (paragraphs 1:1, one-sentence paragraphs stay one sentence).
REJECT with a one-line reason: adding/removing story content, speaker tags or jokes the German doesn't have, cutting German sentences, replacing motif words, "fixing" the German's structure/logic. Explicitly DELIBERATE, do not change: the wet-ink X is never explained (author: stays open, Book 2 hook); K16 Shadow whines (not growls) at Heinrich's circle (deliberate break with R44, Book 2 hook); Luna/Shadow; how Lina died; the K13 recap opening and K16 night musing (German structure); school in July; radiator; 12 circles vs "dozens" of names; church clock.

DECISIONS ALREADY MADE (apply them):
1. German changed (DE_Basis updated): K15 „Theo reichte ihr wortlos den Schraubenzieher." (was „seinen Brieföffner") → "Theo handed her the screwdriver without a word." (or equivalent).
2. K16 last lines (book's ending, line 173): "a second hand" reads as a clock's second hand (D4, D5, D6 independently; the church clock struck earlier). Rebuild so it can't be misread, keep the open "whose hand", the stress on the hand, and the stand-alone last line "In exactly the same spot." (or your improved equivalent). Give 2–3 variants in the notes and choose. Also avoid "lay" (D5: "lay" four times in five paragraphs).
3. D4: K13 L109 "Something was coming loose." → keep A7 warmth and the echo to L189 "let go" (e.g. "Something was letting go."); K13 L27 "echoed" for „hallten"; K14 L171 the tail's single deliberate beat (German „klopfte einmal") — A7 says it carries recognition; "swished" is too soft, "thump" is reserved for the knocking → e.g. "His tail tapped the floor once."; K14 L29 "subzero" → "below freezing" (Fahrenheit convention); K15 L189 "red sealing wax" (same word as K14's "old sealing wax", A7).
4. D6 read-aloud: K16 L45 the letter line without a reading tag sounds like Nora talking — make it clear it's the letter (via the quotation/italics convention the chapter uses, not by adding a new speaker sentence unless the German has one); "Dear finders of this letter" → natural US ("To whoever finds this letter," or similar — Mrs. Silber's formal voice stays); K13 L179 "Believe me." must clearly be Lina's quoted words.
5. K15 L17 Theo reads the punctuation aloud („Wütend Punkt Grab Punkt") — D5/D6: "Angry period. Grave period." confuses ("period" giggle, "grave" double meaning). Rebuild the joke in Theo's voice so a US kid gets it (A3 rule: jokes may be rebuilt; keep the setup "Wütend. Grab." on the map and Theo's "That sounds cozy." payoff).

Append to each notes file (K13–K16) "## Runde 2 (Block 4)" with a table: finding source + id/line · accepted/rejected · one-line reason; counts per pass. Re-check EVERY sentence you changed against the German for meaning only; list drift you fixed. Update Wortliste rows if recurring wording changed.
Run python3 Scripts/pruefe_en.py pruefen Band1/Manuskript_EN/DE_Basis/Kapitel_NN.md Band1/Manuskript_EN/Kapitel_NN.md for NN = 13..16 until 0 findings, and python3 Scripts/pruefe_en.py konsistenz Band1/Manuskript_EN (nothing new).
Do not modify other files, do not commit. Reply with: accepted/rejected counts per pass per chapter, the new last lines of the book (with your reasoning), every decision-item change (old → new), script and konsistenz output.
```

## D4-Gegenprobe jeder späten Änderung (Pilot 5.2a)

*Anpassen:* Commit-Hashes einsetzen (vorher/nachher). Nach JEDER Textänderung, auch nach eigenen Einzeilern.

```text
You are an independent meaning checker (D4) for a German children's book translated into US English (ages 9–12). Work in /home/user/Die_Geisterspuerer.

Run: git diff --word-diff 66c5a37 a4351fc -- Band1/Manuskript_EN/Kapitel_13.md Band1/Manuskript_EN/Kapitel_14.md Band1/Manuskript_EN/Kapitel_15.md Band1/Manuskript_EN/Kapitel_16.md
These are all sentences changed in the last revision round. For every changed sentence find the matching German sentence in Band1/Manuskript_EN/DE_Basis/Kapitel_NN.md (same paragraph number; the German is current) and judge ONLY meaning and effect (not style): changed, added, lost, tone shift, concrete image made abstract, a later reveal hinted too early, something resolved that the German leaves open (A7: Dokumentation/EN_Bibel/A7_Szenen_Absicht_Band1.md, Kapitel 13–16), a contradiction with earlier chapters. Judge the book's final two lines (K16 end) with special care. Known deliberate decisions you should NOT flag: "screwdriver" (German changed), "tapped" for the tail (thump is reserved for the knocking), letter lines in nested quotes “‘…’” (Nora reads aloud), "To those who find this letter.", Theo's rebuilt joke "Angry. Grave. The end.", "blocks" for Straßen, "below freezing", "red sealing wax". Do not read notes or reviews.

Write a table per chapter to Band1/Manuskript_EN/Pruefung/D4_Block4_Gegenprobe_R2.md: line · German · English (new) · OK / SCHWÄCHE / FEHLER · reason; end with counts. Do not modify other files, do not commit. Reply with counts per chapter and every non-OK item with a suggested fix.
```

## D5-Endkontrolle nach späten Runden

*Anpassen:* Für Kapitel, die nach der letzten D5-Runde noch geändert wurden.

```text
You are pass D5: an experienced line editor at a US children's publisher (middle grade 9–12, spooky-funny books like "Small Spaces", "Goosebumps", "Lockwood & Co."). Work in /home/user/Die_Geisterspuerer.

Read ONLY Band1/Manuskript_EN/Kapitel_14.md and Kapitel_15.md (two chapters near the end of one book; the story is set in Germany on purpose; German street names, "Mrs." with German surnames, "the Ring" (a ring road) are deliberate; short fragments at scary beats are the house style; the dog is named Shadow, so the common noun "shadow" is deliberately never used). You don't speak German; do not open any other file, including earlier reviews.

This is a FINAL pass after several revision rounds — report only what a careful US editor would really change before print: sentences that sound translated, are unclear to a 10-year-old, or trip a parent reading aloud. No taste-level suggestions. Format per finding: line · quoted sentence · category (TRANSLATED / UNCLEAR / READ-ALOUD / OTHER) · why · one-line suggestion. Also judge specifically: K15 "The evening sun stretched long stripes of shade across the sidewalk." — natural, or does it need a better wording that still avoids the word "shadow(s)"? Give 2 alternatives if it needs one.
End per chapter: Would you guess this was translated? Yes/No.

Write to Band1/Manuskript_EN/Pruefung/D5_K14_K15_Endkontrolle.md. Do not modify other files, do not commit. Reply with all findings and the verdicts.
```

## D8.2 Spannungskurve (blind, je Sprache ein Prüfer)

*Anpassen:* Für Englisch dieselbe Vorlage mit EN-Dateien. Bei Abweichung ≥ 2: Gegenprobe mit EINEM Prüfer für beide Sprachen (nächste Vorlage).

```text
You rate the tension curve of a German children's horror-humor novel (ages 10–12). Work in /home/user/Die_Geisterspuerer. Read ONLY Band1/Manuskript_EN/DE_Basis/Kapitel_01.md … Kapitel_16.md, in order. Do not open any English file, notes, or reviews.

For EACH chapter give four sub-scores with this fixed rubric:
- N Neues 0–3: Does the reader learn something they didn't know (fact, mystery, twist)?
- G Gefahr 0–3: Is a character noticeably threatened, now, in the scene?
- F Gefühl 0–2: Does the scene move the reader (empathy, grief, warmth)?
- S Sog 0–2: Does the chapter ending force you to turn the page?
Give each score with a one-line justification quoting the text (short quote + line number). Be consistent across chapters; use the full range.
Write a table to Band1/Manuskript_EN/Nachanalyse/D8_2_Spannung_DE.md (columns: Kap · N · G · F · S · Σ · Begründung). Do not modify other files, do not commit. Reply with the table.
```

## D8.2 Gegenprobe mit einem Prüfer

```text
You are a single rater for a tension check. Work in /home/user/Die_Geisterspuerer. For chapters 1, 3, 7 and 16 of a children's horror-humor novel (ages 9–12), read the German original (Band1/Manuskript_EN/DE_Basis/Kapitel_NN.md) and its English translation (Band1/Manuskript_EN/Kapitel_NN.md). Two earlier raters scored DE and EN separately and got different totals; your job is to tell whether the TEXTS differ or only the raters did.
Score each chapter in BOTH languages with this rubric (same standard for both): N new info 0–3 · G danger to a character now 0–3 · F feeling (empathy/grief/warmth) 0–2 · S pull of the chapter ending 0–2. Then, for every sub-score where DE and EN differ by you, quote the German and English passage responsible and say whether the English really carries less (or more) — and why. If you find the English weaker anywhere, suggest a concrete English fix that keeps the German meaning. Do not read notes or reviews.
Write to Band1/Manuskript_EN/Nachanalyse/D8_2_Spannung_Gegenprobe.md. Do not modify other files, do not commit. Reply with the four DE/EN score pairs and any real weakness found.
```

## D8.3 Stimmen-Test Theo

```text
You run D8.3 "voice test" for the US English translation of a German children's book (Theo, 10, sarcastic, anxious, funny; the book's humor engine). Work in /home/user/Die_Geisterspuerer.

Sources: German Band1/Manuskript_EN/DE_Basis/Kapitel_01–16.md, English Band1/Manuskript_EN/Kapitel_01–16.md (paragraphs line up 1:1 by line number), voice reference Dokumentation/EN_Bibel/A2_Stimmen.md (Theo section).
Method: extract EVERY line of dialogue Theo speaks, in book order, German and English side by side (chapter · line · DE · EN). Then read the English list straight through as one voice. The book was translated in four blocks by different translator passes (K1–4, K5–8, K9–12, K13–16) — look specifically for drift between blocks.
Report a finding only if: Theo sounds suddenly older/more formal or younger than elsewhere; a verbal habit appears in one block and not others where the German has it; British/stiff phrasing; a joke line lost its snap compared to the German; his catchphrase/running-gag lines are worded differently across chapters where the German repeats them (e.g. "on the record", tombstone, résumé); Theo says "Shadow's" + noun that sounds like "shadows". Per finding: chapter · line · DE · EN · problem · suggested EN. If the translator's notes (Band1/Manuskript_EN/Notizen/Notizen_Kapitel_NN.md) explicitly justify a deviation, mark it "begründet" and don't count it.
Write the full side-by-side list and findings to Band1/Manuskript_EN/Nachanalyse/D8_3_Stimme_Theo.md (findings at the top). Do not modify other files, do not commit. Reply with the number of Theo lines, the findings, and a 3-sentence verdict on voice consistency across the four blocks.
```

## D8.3 Stimmen-Test übrige Figuren

```text
You run D8.3 "voice test" for the US English translation of a German children's book. Work in /home/user/Die_Geisterspuerer.

Characters: Nora (12, rational older sister, POV), Mom (warm, busy), Lina (12, in 1974 diary entries), Mrs. Silber (old woman; notebook and letter, formal), Mrs. Held and any other speaking minor characters (librarian etc.).
Sources: German Band1/Manuskript_EN/DE_Basis/Kapitel_01–16.md, English Band1/Manuskript_EN/Kapitel_01–16.md (paragraphs line up 1:1 by line number), voice reference Dokumentation/EN_Bibel/A2_Stimmen.md.
Method: per character, extract EVERY line they speak or write (diary/notebook/letter included), in book order, DE and EN side by side (chapter · line · DE · EN). Read each English list straight through as one voice. The book was translated in four blocks by different translator passes (K1–4, K5–8, K9–12, K13–16) — look specifically for drift between blocks (Nora suddenly flippant or adult; Mom British in one block; Lina's diary voice changing; Mrs. Silber's notebook (K11) vs letter (K16) — contractions, formality, recurring phrases like "the Restless", "the Veil", "the First One").
Report a finding only if the voice breaks, a recurring phrase is worded differently where the German repeats it, or a line sounds translated/British. Per finding: character · chapter · line · DE · EN · problem · suggested EN. If the translator's notes (Band1/Manuskript_EN/Notizen/) explicitly justify a deviation, mark it "begründet" and don't count it.
Write lists and findings to Band1/Manuskript_EN/Nachanalyse/D8_3_Stimmen_Nora_und_andere.md (findings at the top). Do not modify other files, do not commit. Reply with line counts per character, the findings, and a short verdict per character.
```

## D8.4 Kapitelenden isoliert

*Anpassen:* Vorher Auszug erzeugen (letzte 4 Absätze je Kapitel, siehe Nachanalyse/D8_4_Kapitelenden_Auszug.md).

```text
You run D8.4 "chapter endings in isolation" for the US English translation of a German children's horror-humor book (ages 9–12; every chapter must end on a cliffhanger). Work in /home/user/Die_Geisterspuerer.

Read Band1/Manuskript_EN/Nachanalyse/D8_4_Kapitelenden_Auszug.md (last 4 paragraphs of all 16 chapters, German and English side by side) and the chapter sections "Kapitelende" in Dokumentation/EN_Bibel/A7_Szenen_Absicht_Band1.md. If needed for context, open the full chapter (Band1/Manuskript_EN/Kapitel_NN.md / DE_Basis/Kapitel_NN.md) — but judge the endings as read in isolation.
For each chapter compare: does the English ending pull as hard as the German? Check rhythm, the very last word (stress at the end?), length of the last sentence, whether a one-word/one-line punch paragraph stayed a punch, whether anything was added/softened/explained, and whether the A7 "Kapitelende" intention is met. Report a finding only if the English pulls clearly less (or reads translated); then give a concrete suggested EN that keeps the meaning. Mark endings that are as strong or stronger as OK with one line why.
Write a table to Band1/Manuskript_EN/Nachanalyse/D8_4_Kapitelenden.md (Kap · OK/BEFUND · reason · suggestion). Do not modify other files, do not commit. Reply with the table.
```

## D8.5 Witz-Test

```text
You run D8.5 "joke test" for the US English translation of a German children's horror-humor book (ages 9–12; rule: after a scare, humor within 1–2 paragraphs, usually from Theo). Work in /home/user/Die_Geisterspuerer.

Sources: Dokumentation/EN_Bibel/A3_Witz_Liste.md (the joke list — use the Band 1 entries W1-xx, each with German text, type, and suggested English), German Band1/Manuskript_EN/DE_Basis/Kapitel_01–16.md, English Band1/Manuskript_EN/Kapitel_01–16.md (paragraphs line up 1:1 by line number), translator notes Band1/Manuskript_EN/Notizen/ (rebuilt jokes are justified there).
Method: for EVERY Band 1 joke in A3 (and any clear joke in the German not on the list), extract: the trigger (scare/tension right before, if any) and the joke, German and English side by side with line numbers. Judge: (1) does the English joke land for a 10-year-old American (funny / kind of / falls flat)? (2) did the distance scare → joke grow (more paragraphs in between, or the joke moved)? (3) was a joke lost, softened, explained, or made cruder? (4) running gags across chapters worded consistently?
Report a finding only if a joke lands clearly worse than in German or the scare→joke distance grew; give a concrete suggested EN that keeps the setup. Count jokes per verdict.
Write to Band1/Manuskript_EN/Nachanalyse/D8_5_Witze.md (findings at the top, then the full side-by-side list). Do not modify other files, do not commit. Reply with counts and every finding.
```

## D8.6 Lesedurchgang am Stück

*Anpassen:* Liest die Gesamtfassung (wird beim eBook-Bau erzeugt).

```text
You run D8.6, the final read of the complete English book after all corrections. Work in /home/user/Die_Geisterspuerer. Read ONLY Band1/Manuskript_EN/The_Whispering_Window_Komplett.md from beginning to end, straight through, like a reader would (a spooky-funny US middle-grade novel, ages 9–12). Do not open any other file.

Report ONLY things that become visible across chapter boundaries and that a careful US editor would fix before print:
- breaks between chapters (a chapter opening that doesn't connect to the previous ending, a time/place jump that confuses),
- repetitions that only show when reading in one go (the same image, phrase or simile used too often; name the count and chapters),
- inconsistent wording of the same thing across chapters (object names, place names, nicknames, spelling, capitalization, numbers),
- anything left over that sounds translated,
- typos, doubled words, punctuation slips.
Do NOT report story-logic choices of the original author (they're deliberate) unless the English text itself creates the problem. Per finding: chapter · quoted text · problem · one-line fix. Rank by importance. End with a 3-sentence verdict: is this ready to publish as text?

Write to Band1/Manuskript_EN/Nachanalyse/D8_6_Lesedurchgang.md. Do not modify other files, do not commit. Reply with the findings and the verdict.
```

## Rahmen: Leseprobe + Titelei/Impressum/Anhang

```text
You are the translator (D2) for the US English edition of the German children's horror-humor series "Die Geisterspürer" (English: "The Ghost Listeners"; Book 1 "The Whispering Window"; Book 2 "The Graveyard Without Names"), for American readers aged 9–12. Book 1 is fully translated (Band1/Manuskript_EN/Kapitel_01–16.md). Work in /home/user/Die_Geisterspuerer. Two small tasks for the English Book 1's back/front matter.

READ FIRST: Band1/Manuskript_EN/Wortliste_Band1.md (fixed wording; e.g. "blocks" for Straßen as distance, "Mrs. Silber", lowercase "shadow" never, "thump" only for the knocking), Dokumentation/EN_Bibel/A8_Stil_Brief.md, A1_Glossar.md (incl. Band-2 entries), A2_Stimmen.md, A4_Motive.md, A6_Fallen_Liste.md (B2 K1 entries), A3_Witz_Liste.md (B2 K1 entries if any). Also read the last two chapters of Book 1 in English (Kapitel_15.md, Kapitel_16.md) — the sample is read directly after them.

TASK 1 — Translate the Book 2 sneak peek.
Source (German, exactly what the German edition prints): Band1/Manuskript_EN/Rahmen/DE_Leseprobe_Band2.md (opening of Book 2, Chapter 1, 480 words, ends on the hook: Shadow sits on the sidewalk, not one step through the gate). Write the English to Band1/Manuskript_EN/Rahmen/EN_Leseprobe_Band2.md: heading "# Chapter 1: <title>" (translate „Guten Morgen, Friedhof" in Theo-ish spirit — e.g. "Good Morning, Graveyard"; note alternatives), same paragraph structure 1:1, `---` kept. Same rules as Book 1 (A8; US floors; Fahrenheit if a temperature appears; no added content). Wording must connect seamlessly to the end of Book 1 (the map, eleven circles, the old cemetery, Shadow). This text will later become the start of the full English Book 2, so put every decision in notes: Band1/Manuskript_EN/Rahmen/Notizen_Leseprobe_Band2.md (format as in the chapter notes; anything wrong in the German: report, don't fix).
Run: python3 Scripts/pruefe_en.py pruefen Band1/Manuskript_EN/Rahmen/DE_Leseprobe_Band2.md Band1/Manuskript_EN/Rahmen/EN_Leseprobe_Band2.md until 0 findings (report false alarms).

TASK 2 — Write the English front and back matter texts (NEW writing for US readers, not a literal translation of the German pages). Write to Band1/Manuskript_EN/Rahmen/Rahmen_EN.md with one section per page, exactly these sections, each with the final text (no placeholders except where stated):
1. "## Half title" — series name.
2. "## Title page" — The Ghost Listeners / Book 1 / The Whispering Window / Benjamin Krug.
3. "## Copyright page" — Text © 2026 Benjamin Krug; All rights reserved; "Originally published in German as *Die Geisterspürer: Das Haus, das flüstert* (2026)."; "Translated from the German." (author decision: exactly this fact, no translator name, no AI sentence); a standard US fiction disclaimer (names, characters, places, events are products of imagination…); "First English edition 2026"; "Independently published". No cover-design line (the English cover doesn't exist yet). Keep it short, US conventions.
4. "## Contents" — heading word only (the build generates the chapter list).
5. "## What happens next?" — teaser page after "END OF BOOK 1". German original for reference: „Wie geht es weiter? / Elf Kreise auf Frau Silbers Karte. / Der nächste liegt am alten Friedhof." Use the book's wording (Mrs. Silber's map, eleven circles, the old cemetery/graveyard — check which word the English Book 1 uses and stay consistent). Then: "The Ghost Listeners · Book 2 / The Graveyard Without Names / Coming soon".
6. "## Sneak peek heading" — the small line above the sample (German: „Leseprobe aus Band 2") — e.g. "A sneak peek at Book 2".
7. "## After the sneak peek" — short page: the story continues in Book 2, title, "Coming soon". No link (the English Book 2 doesn't exist yet; add a comment line starting with "<!-- " saying a link goes here once it exists).
8. "## Review request" — German for reference: „Hat dir „Das Haus, das flüstert“ gefallen? Dann freue ich mich riesig über eine kurze Bewertung auf Amazon — auch nur ein oder zwei Sätze reichen völlig. Jede Rezension hilft anderen Kindern (und ihren Eltern), dieses Buch zu entdecken. Und mir hilft sie, weitere Bände zu schreiben. Vielen Dank! Benjamin Krug". Write it for US middle-grade readers and their parents (warm, short, no pressure, COPPA-sensible: address it so a parent can act — kids under 13 can't post reviews themselves; e.g. "ask a grown-up to help"). No link yet (author decision: link added after publication) — mention "on Amazon"; add a "<!-- " comment where the link will go.
9. "## Series list" — "The Ghost Listeners" — Book 1: The Whispering Window; Book 2: The Graveyard Without Names (coming soon). Nothing else (author decision: no German-only series, no invented English titles for Books 3–5).

Do not modify any other files. Do not commit. Reply with: script output for the sample, the full text of Rahmen_EN.md, the sample's chapter title and its first and last paragraph, the 2 decisions you are least sure about, and any errors in the German sample.
```
