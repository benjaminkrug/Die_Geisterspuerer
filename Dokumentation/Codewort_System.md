# Codewort-System — Die Geisterspuerer CYOA (Serien-Architektur)

## Konzept

Jeder Band hat **3 Codewörter**, versteckt in den 3 besten Endings (eines pro Hauptpfad). Die Wörter sind organisch in den Text eingebettet — nicht als Rätsel, sondern als bedeutungsvolle Sätze, die beim Wiederlesen auffallen.

Wer alle 3 Codewörter eines Bandes sammelt, findet am Buchende einen Hinweis, der zu einem **Geheim-Ending** führt. Das Geheim-Ending enthält ein **Serien-Codewort**, das über alle 5 Bände gesammelt wird.

---

## Band 1 — Das Haus, das flüstert

### 3 Codewörter

| Pfad | Bestes Ending | Codewort | Versteck im Text |
|------|---------------|----------|-----------------|
| A | E7 (Die neue Hüterin) | **SCHLÜSSEL** | Silbers Brief: "Der Schlüssel liegt nicht im Schloss, sondern im Zuhören." |
| B | E16 (Schatten und Stein) | **KARTE** | Helds Notizbuch: "Auf der Karte sind zwölf Punkte. Zwölf Stimmen. Wer sie alle hört, versteht." |
| C | E23 (Mamas Frage) | **STIMME** | Mama: "Jede Stimme verdient, gehört zu werden. Auch die leisen." |

### Kombination

Am Buchende (nach dem letzten Ending, vor Backmatter):

> *Du hast drei besondere Wörter gefunden?*
> *Verbinde sie: Was brauchst du, um alle zwölf Geister zu befreien?*
> *Den SCHLÜSSEL zum Zuhören, die KARTE der Unruhigen und eine STIMME, die nicht aufgibt.*
> *Gehe zu Abschnitt 300.*

### Geheim-Ending (Abschnitt 300 / E24 "Das Versprechen")

- Nora steht vor Silbers Karte, alle 12 Markierungen leuchtend
- Schatten legt sich neben sie, Kopf auf Pfoten
- Nora spürt: Silber ist nicht verschwunden — sie wartet
- Nora legt die Hand auf die Karte: "Ich komme. Alle zwölf."
- **Serien-Codewort Band 1:** ZUHÖREN

---

## Serien-Arc über 5 Bände

| Band | Titel | 3 Codewörter | Geheim-Ending Serien-Wort | Thema |
|------|-------|-------------|--------------------------|-------|
| 1 | Das Haus, das flüstert | SCHLÜSSEL + KARTE + STIMME | **ZUHÖREN** | Empathie |
| 2 | Der Friedhof ohne Namen | (offen) | **ERINNERN** | Vergangenheit |
| 3 | Schatten sieht mehr | (offen) | **VERGEBEN** | Vergebung |
| 4 | Die zugemauerte Tür | (offen) | **LOSLASSEN** | Abschied |
| 5 | Der Schleier | (offen) | **BEFREIEN** | Erlösung |

### Band 5: Finales Serien-Ending

Am Ende von Band 5 CYOA:

> *Du hast fünf Bände lang zugehört. Fünf Wörter gesammelt.*
> *ZUHÖREN. ERINNERN. VERGEBEN. LOSLASSEN. BEFREIEN.*
> *Das ist Silbers Methode. Die vollständige Methode.*
> *Gehe zu Abschnitt 500.*

**Abschnitt 500:** Nora steht vor Gravens Grab. Die vollständige Methode. Alle 12 Geister befreit. Graven selbst — nicht besiegt, sondern verstanden. Silber erscheint. "Danke." Gravenstedt ist frei.

---

## Implementierungs-Regeln

1. **Codewörter sind KURSIV und GROSS** im Text: *SCHLÜSSEL*, *KARTE*, *STIMME*
2. Sie stehen in einem Satz, der auch ohne Codewort-Wissen Sinn ergibt
3. Sie werden von einer Figur ausgesprochen oder gedacht (nie vom Erzähler)
4. Der Hinweis am Buchende ist optisch abgesetzt (Kasten oder kursiv)
5. Das Geheim-Ending ist das LETZTE Ending im Buch (höchste Abschnittnummer)
6. Es enthält den stärksten Serien-Hook aller Endings

## Vergleich mit Herrenhaus-Detektive

| Aspekt | Herrenhaus | Geisterspürer |
|--------|-----------|---------------|
| Codewörter pro Band | 4 | 3 |
| Versteck | Im Text versteckt | Im Text versteckt |
| Kombination | Wörter = Ortsname | Wörter = Methode |
| Geheim-Ending | Bonus-Szene | Serien-Arc + Antagonist |
| Serien-System | Nein (pro Band) | Ja (5 Bände → finales Ending) |
| Schwierigkeit | Mittel | Hoch (3 Pfade = 3 Durchspielungen) |
