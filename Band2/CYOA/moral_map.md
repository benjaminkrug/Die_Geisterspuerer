# Moral Map — Die Geisterspuerer CYOA Band 2 „Der Friedhof ohne Namen"

Referenzdokument: Welches Thema lehrt welche Entscheidung?

**Grundregel:** Kein Thema wird direkt ausgesprochen. Die Lehre ergibt sich aus den KONSEQUENZEN der
Wahl. „Show, don't tell." (übernommen aus Band 1)

---

## Themen (Band-1-Set + Band-2-Schwerpunkte)

| # | Thema | Kurzformel |
|---|-------|-----------|
| 1 | Mut & Angst überwinden | Angst haben UND handeln = Mut |
| 2 | Freundschaft & Loyalität | Füreinander da sein, auch wenn es schwer wird |
| 3 | Kritisches Denken statt Gerüchte | Fakten prüfen, nicht der ersten Idee folgen |
| 4 | Verantwortung übernehmen | Nicht weglaufen, auch wenn es einfacher wäre |
| 6 | Kommunikation statt Geheimhaltung | Die RICHTIGEN Zuhörer / Sprecher finden |
| 10 | Richtig vs. Einfach | Das Richtige ist selten das Bequeme |
| 11 | Geduld zahlt sich aus | Manchmal muss man warten — manchmal darf man NICHT warten |
| 12 | Empathie ist stärker als Stärke | Zuhören befreit (Kern-USP der Reihe) |
| 13 | Jeder verdient erinnert zu werden | Auch die Namenlosen, auch nach 139 Jahren |
| 14 | Zusammen stärker als allein | Sackgassen beweisen es |
| 15 | Vertraue deinem Bauchgefühl | Schatten als Metapher für Intuition |
| **16** | **Der erste Plan ist nicht immer richtig** | **Noras Band-2-Bogen: erkennen, wenn die eigene Lösung scheitert** |
| **17** | **Schuld muss benannt werden** | **Vergessen schützt den Täter; nur das laute Aussprechen befreit** |

**Band-2-Kern:** #13 + #17 tragen den Twist. Brenners Namen *vorlesen* (Empathie, #12) reicht NICHT,
solange Voss' Schuld verschwiegen wird (#17). Das ist die bewusste Weiterentwicklung gegenüber Band 1,
wo Empathie allein genügte.

**Gestrichene Band-1-Themen in Band 2:** #5 (Vorurteile) und #7/#9 spielen hier keine tragende Rolle —
nicht erzwingen. #9 (Vergangenheit verstehen) steckt implizit in der ganzen Recherche, wird aber nicht
als Entscheidungs-Thema geführt.

---

## 13 Entscheidungen → Themen-Zuordnung

*(Abschnitte/Wahlen exakt aus `graph_v2.yaml`.)*

### Prolog

| Abschnitt | Wahl A / B / C | Primär | Sekundär | Subtile Umsetzung |
|-----------|----------------|--------|----------|--------------------|
| P5 | Gestalt folgen / Archiv / Kloß fragen | #15 Intuition | #3 Krit. Denken | Drei Haltungen: mutig dem Übernatürlichen folgen, kühl recherchieren, einem Erwachsenen vertrauen. Keine ist falsch. |

### Pfad A — „Dem Grauen folgen" (mutig)

| Abschnitt | Wahl A / B (/ C) | Primär | Sekundär | Subtile Umsetzung |
|-----------|------------------|--------|----------|--------------------|
| A3 | Bleiben (Schuppen) / Fliehen | #1 Mut & Angst | #10 Richtig vs. Einfach | Fliehen ist menschlich (EA4). Bleiben öffnet den Weg — mit Risiko (Schuppen-Falle). |
| A6 | Brenner ansprechen / zuhören / fliehen | #12 Empathie > Stärke | #1 Mut | Laut ansprechen scheitert (D1: „Reden ist nicht Zuhören"). Zuhören führt zum Twist. Fliehen = ehrlich (EA4). |
| A8 | Sofort vorlesen / Theo mitnehmen (Kapelle) | #16 Erster Plan ≠ richtig | #14 Zusammen stärker | Noras „wie bei Lina"-Plan scheitert spektakulär (EA3). Theo mitnehmen führt zum echten Fund (Johanns Zweig). |
| A11 | Kloß holen / allein weiter | #17 Schuld benennen | #4 Verantwortung | Allein „befreien" bleibt unvollständig (EA2). Den Zeugen Kloß holen = vollständige Lösung (EA1, Codewort NAME). |

### Pfad B — „Die Ermittlerin" (rational)

| Abschnitt | Wahl A / B (/ C) | Primär | Sekundär | Subtile Umsetzung |
|-----------|------------------|--------|----------|--------------------|
| B2 | Im Archiv vertiefen (→B4) / zum Schuppen (→B3) | #3 Krit. Denken | #1 Mut | Zwei gleichwertige Recherche-Wege zum Twist: Voss' Akte (kühl) oder die Blechdose im Feld. Beide münden in B5 (begründeter Twist). |
| B3 | Fund zusammensetzen (handeln) / nur forschen | #4 Verantwortung | #3 Krit. Denken | Schuppen-Weg: Blechdose mit Johann-Eintrag. Nur forschen ohne Handeln befreit niemanden (D3). |
| B5 | Beweise sammeln / vorsichtig / sofort Kapelle | #11 Geduld | #10 Richtig vs. Einfach | Beweise (Registerbüro) = Lösung (EB1, AKTE). Zu vorsichtig = zurück (D4). Eile zur Kapelle scheitert (EB3). |
| B7 | Kloß zum Reden / selbst weitermachen / bei Beweisen belassen | #17 Schuld benennen | #4 Verantwortung | Beweise allein reichen nicht — jemand muss sie laut machen (EB1). Selbst Silbers Methode fortführen = Hüterin-Weg (EB4). Nichts tun = halbe Wahrheit (EB2). |

### Pfad C — „Kloß vertrauen" (sozial, geplant stärkster Pfad)

| Abschnitt | Wahl A / B | Primär | Sekundär | Subtile Umsetzung |
|-----------|------------|--------|----------|--------------------|
| C2 | Kloß glauben & abwarten / anlügen & heimlich | #6 Kommunikation | #4 Verantwortung | Kloß anlügen isoliert (D5). Vertrauen öffnet sein Geständnis. (Wahl erst nach dem Kennenlernen in C1.) |
| C4 | Kloß zum Reden bewegen / allein versuchen | #17 Schuld benennen | #14 Zusammen stärker | Allein bleibt Teilerfolg (EC3). Kloß überzeugen führt zum stärksten Ende. |
| C7 | Vor den Baggern (5 Uhr) / zögern | #11 Geduld | #1 Mut | „Manchmal darf man NICHT warten": Zögern = die Bagger zerstören Sektion C (EC4). Handeln rettet es. |
| C8 | 47 Namen gemeinsam vorlesen / Kloß Tafel aufhängen | #13 Jeder verdient Erinnerung | #2 Freundschaft | Beide befreien Brenner. Vorlesen = epischer Mut-Moment (EC1, STIMME). Tafel = warmer, leiser Ausklang (EC2). |

---

## 4 Sackgassen → Themen

| Sackgasse | Weg | Thema | Lehre |
|-----------|-----|-------|-------|
| D1 | A6→D1 | #12 Empathie > Stärke | Reden ist nicht Zuhören. Brenner braucht jemanden, der FÜHLT, nicht anschreit. |
| D3 | B3→D3 | #4 Verantwortung | Wissen ohne Handeln befreit niemanden. Recherche ist erst der Anfang. |
| D4 | B5→D4 | #11 Geduld / #10 Richtig vs. Einfach | Zu viel Eile macht es schlimmer — Voss vor den Beweisen anzugehen scheitert. |
| D5 | C1→D5 | #6 Kommunikation | Lügen isoliert; Vertrauen verbindet. Ohne Kloß' Geständnis fehlt der Schlüssel. |

---

## Themen-Verteilung (Übersicht)

| Thema | Primär | Sekundär | Sackgassen | Gesamt |
|-------|--------|----------|------------|--------|
| #1 Mut & Angst | A3 | A6, B2, C7 | — | 4x |
| #2 Freundschaft | — | C8 | — | 1x |
| #3 Krit. Denken | B2 | P5, B3 | — | 3x |
| #4 Verantwortung | B3 | A11, C1, B7 | D3 | 5x |
| #6 Kommunikation | C1 | B7 | D5 | 3x |
| #10 Richtig vs. Einfach | — | A3, B5 | D4 | 3x |
| #11 Geduld | B5, C7 | — | D4 | 3x |
| #12 Empathie > Stärke | A6 | — | D1 | 2x |
| #13 Jeder verdient Erinnerung | C8 | — | — | 1x (USP durchzieht alles) |
| #14 Zusammen stärker | — | A8, C4 | — | 2x |
| #15 Intuition | P5 | — | — | 1x (Schatten durchzieht alles) |
| #16 Erster Plan ≠ richtig | A8 | — | — | 1x (Noras Bogen, trägt Akt 3) |
| #17 Schuld benennen | A11, B7, C4 | — | — | 3x (Twist-Kern) |

**Bewertung der Verteilung:** Kein Thema über 4x, der Twist-Kern (#17) sitzt bewusst auf allen drei
Pfaden (A11/B7/C4) — das ist gewollt, weil jeder Pfad zur selben Erkenntnis führen muss (Plan §5).
#13 und #15 erscheinen nur 1x als *Entscheidung*, durchziehen aber als USP/Schatten jeden Abschnitt.

---

## Qualitätsprüfung (Checkliste, aus Band 1 übernommen)

- [ ] Jede Entscheidung hat mindestens 1 zugeordnetes Thema
- [ ] Kein Thema wird direkt ausgesprochen („Die Moral ist…")
- [ ] Die Lehre ergibt sich aus den KONSEQUENZEN der Wahl
- [ ] Sackgassen lehren, ohne zu bestrafen
- [ ] Themen-Verteilung ausgewogen (kein Thema dominiert)
- [ ] Schatten sinnvoll präsent ODER bewusst abwesend (STIL_REFERENZ §4 — keine erzwungene Quote)
- [ ] Humor nach jedem Grusel — außer im bewussten Tiefpunkt (A-Scheitern / Theo-allein)
