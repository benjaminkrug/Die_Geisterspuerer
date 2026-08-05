# Graph-Skizze — CYOA Band 2 (Schritt 1a)

> **Zweck:** Topologie *vor* dem YAML visuell prüfen. Noch keine Texte, keine endgültigen IDs-Targets.
> Zu entscheiden: **(1) Twist-Pol-Variante a vs. b** · **(2) Gesamttopologie freigeben.**
> Quellen: `Plan_Band2_CYOA.md` §2–§6, `KANON.md`. Knotenzahl-Schätzung am Ende.

---

## Legende

- 🟦 Story · 🔶 Wahl (choice) · ⬛ Dead End (zurückblättern) · 🏁 Ende
- ⭐ = bestes Ende des Pfads (trägt Codewort) · 🔑 = Codewort-Vergabe
- `‼️` = unverzichtbarer Beat (`unique_event`): Twist, Theo-allein, Johanns Zweig, Schatten-Durchbruch, Kloß-Mut

---

## Prolog (gemeinsam) — P1–P5

```mermaid
flowchart TD
    P1[🟦 P1 Schatten bleibt am Tor stehen]
    P2[🟦 P2 Zwei Zonen · 9 Grad kälter · Stare]
    P3[🟦 P3 Der kippende Stein · Silhouette · '1887']
    P4[🟦 P4 Theo will weg · 'Schatten ist klüger']
    P5{🔶 P5 Entscheidung}
    P1-->P2-->P3-->P4-->P5
    P5-->|Der Gestalt folgen|A1
    P5-->|Erst Fakten · Archiv|B1
    P5-->|Kloß fragen|C1
```

---

## Pfad A — „Dem Grauen folgen" (mutig/übernatürlich)

```mermaid
flowchart TD
    A1[🟦 A1 Namenloser Teil · Kälte messen]
    A2[🟦 A2 'Stein mit dem Hund' · H.B. 1887]
    A3{🔶 A3 fliegender Grabstein — bleiben/fliehen?}
    A4[🟦 A4 Werkzeugschuppen · Tür fällt zu]
    A5[🟦 A5 1. Blechdose · 23 Namen + Johann · UV-Hinweis]
    A6{🔶 A6 Brenner erscheint — ansprechen / zuhören / fliehen}
    A7["‼️ A-TWIST: Brenner zeigt → Voss wirft Stein → zwei Geister"]
    A8{🔶 A8 sofort 'befreien' / Voss-Logik verstehen}
    A1-->A2-->A3
    A3-->|bleiben|A4
    A3-->|fliehen|EA4
    A4-->A5-->A6
    A6-->|laut ansprechen|D1
    A6-->|zuhören|A7
    A6-->|fliehen|EA4
    A7-->A8
    A8-->|sofort vorlesen → Scheitern|A9scheiter
    A8-->|Theo mitnehmen · Kapelle|A10kapelle
    A9scheiter["🟦 A-Scheitern: Vorlesen macht Voss stärker"]-->EA3
    A10kapelle["‼️ A-Kapelle: Theo allein (POV nora_aussen) · Johanns Zweig · Schatten-Durchbruch"]
    A10kapelle-->A11[🟦 A11 Erkenntnis: Kloß muss Voss anklagen]
    A11-->A12{🔶 A12 Kloß holen / allein weiter}
    A12-->|Kloß|EA1
    A12-->|allein|EA2
    D1((⬛ D1 'Reden ist nicht Zuhören' →A6))
```

**A-Enden:** EA1 ⭐🔑 NAME „Der Zeuge spricht" · EA2 „Schattens Wache" (B3-Hook) · EA3 „Allein zu mutig" (Scheitern) · EA4 „Nacht-Flucht".

---

## Pfad B — „Die Ermittlerin" (rational/Recherche)

```mermaid
flowchart TD
    B1[🟦 B1 Stadtarchiv · Sektion-C-Seiten herausgerissen · H.B. + G. Voss]
    B2["🟦 B2 Grusel-Anker: Strich durch 'Voss' auf dem Foto · Silber-Spur"]
    B3{🔶 B3 Voss-Spur weiter / zurück zum Friedhof-Schuppen}
    B4[🟦 B4 Schuppen · 1. Dose · Buch-Hinweis]
    B5["‼️ B-TWIST: Aktenlogik → Poltergeist passt zu Voss, Brenner ist Opfer"]
    B6{🔶 B6 Registerbüro (Beweis) / direkt Kapelle (riskant)}
    B7["🟦 B7 Unterird. Registerbüro · Protokoll 1886 · Voss-Notiz"]
    B1-->B2-->B3
    B3-->|Voss-Spur|B5
    B3-->|Friedhof|B4
    B4-->B5-->B6
    B6-->|Beweise|B7
    B6-->|Eile|D4
    B7-->EB1
    D4((⬛ D4 'Zu viel Eile' →B6))
    B5-.->|ohne Handeln|D3((⬛ D3 'Wissen ohne Handeln' →B3))
```

**B-Enden:** EB1 ⭐🔑 AKTE „Aktenzeichen Voss" · EB2 „Die halbe Wahrheit" (unvollständig) · EB3 „Zu nah an Voss" (Eile-Scheitern).

> ⚠️ **Frage B:** Erreicht Pfad B den emotionalen Twist-Kern (Johanns Zweig) überhaupt, oder löst B den Fall
> „kühler" über Akten? Im Plan ist B der Recherche-Pfad — Vorschlag: B erreicht den Twist **über das
> Protokoll** (Voss' Schuld dokumentiert), Johanns Zweig bleibt A/C vorbehalten. Das gibt den Pfaden Profil.

---

## Pfad C — „Kloß vertrauen" (sozial/Erwachsene) — geplanter stärkster Pfad

```mermaid
flowchart TD
    C1[🟦 C1 Kloß schwitzt · 3-Tage-Frist · Doppelschatten im Fenster]
    C2{🔶 C2 Kloß glauben & abwarten / heimlich selbst forschen}
    C3[🟦 C3 Kloß' Geständnis · Urgroßvater August Kloß · Voss-Story]
    C4["‼️ C-TWIST: Mit Kloß' Wissen klar — zwei Geister, Voss lebt vom Schweigen"]
    C5{🔶 C5 Kloß zum Reden bewegen / allein versuchen}
    C6["🟦 C6 Registerbüro · Original-Protokoll (mit Kloß)"]
    C7["‼️ C-Kapelle: Theo allein / Johanns Zweig / Schatten-Durchbruch (POV nora_aussen)"]
    C8["‼️ BRÜCKE C→Kloß-Finale: Kloß spricht Voss' Schuld laut aus (Kap.13/14)"]
    C1-->C2
    C2-->|abwarten|C3
    C2-->|heimlich|D5((⬛ D5 'Lügen isoliert' →C2))
    C3-->C4-->C5
    C5-->|Kloß überzeugen|C6
    C5-->|allein|EC3
    C6-->C7-->C8
    C8-->EC1
    C8-.->|Bagger zu früh|EC4
    C3-.->|Kloß-Tafel-Variante|EC2
```

**C-Enden:** EC1 ⭐🔑 STIMME „47 und ein kleiner Name" · EC2 „Die Gedenktafel" · EC3 „Ohne Kloß" (Teilerfolg) · EC4 „Zu spät" (bittersüß).

---

## Geheim-Ende (Codewort-System)

```mermaid
flowchart LR
    EA1[🏁 EA1 🔑 NAME]-->G
    EB1[🏁 EB1 🔑 AKTE]-->G
    EC1[🏁 EC1 🔑 STIMME]-->G
    G[["🏁 E-GEHEIM 'Nicht alleine' · Serien-Wort ERINNERN · höchste Abschnittsnr."]]
```

NAME + AKTE + STIMME → **ERINNERN**. Geheim-Ende-Hinweis am Buchende (Kasten/kursiv), führt zur höchsten Nummer.

---

# DIE ENTSCHEIDUNG: Twist-Pol Variante a vs. b

Der Twist-Kern („zwei Geister · Vorlesen reicht nicht · Voss muss angeklagt werden") muss laut Plan auf
**allen** Pfaden vorkommen. Im Graph oben ist er als **A7 / B5 / C4** modelliert. Das ist **Variante a**.

### Variante a — drei getrennte Twist-Abschnitte (oben gezeichnet)

```mermaid
flowchart TD
    A6{A6}-->A7[‼️ A-TWIST · Brenner zeigt, Voss wirft]
    B3{B3}-->B5[‼️ B-TWIST · Aktenlogik]
    C3-->C4[‼️ C-TWIST · Kloß' Wissen]
    A7-->A8{...A-Enden}
    B5-->B6{...B-Enden}
    C4-->C5{...C-Enden}
```

- ✅ **Time-Cave bleibt sauber** — 0 zusätzliche Konvergenz, Validator grün.
- ✅ Jeder Pfad erlebt den Twist **in seiner eigenen Sprache** (mutig / kühl / sozial) → starke Pfad-Identität.
- ⚠️ **Preis:** 3 Abschnitte mit gleichem *Kern* → Recycling-Gefahr. Gegenmittel: Anti-Recycling-Liste
  (STIL_REFERENZ §5), bewusst verschiedene Inszenierung. Mehr Schreibarbeit (3 statt 1).

### Variante b — ein gemeinsamer Konvergenz-Twist

```mermaid
flowchart TD
    A6{A6}-->T
    B3{B3}-->T
    C3-->T[‼️ T-TWIST · gemeinsam für alle Pfade]
    T-->A8{zurück A-Enden}
    T-->B6{zurück B-Enden}
    T-->C5{zurück C-Enden}
```

- ✅ Twist garantiert **identisch**, nur **1 Abschnitt** zu schreiben, kein Recycling.
- ⚠️ **Preis:** **zweiter Konvergenzpunkt** (neben C→Kloß-Finale) → bricht die selbst gesetzte Time-Cave-Regel,
  **Validator wirft Konvergenz-Warnung**, und nach dem gemeinsamen T muss man die Leser sauber auf ihren
  Pfad **zurücksortieren** (T braucht 3 Ausgänge je nach Herkunft → unschön / fehleranfällig im Buchformat,
  weil der Leser nur „weiter mit Nr. X" liest und nicht weiß, „woher" er kam).

### Mein Argument (Empfehlung)

**Variante a.** Begründung, die das Buch besser macht — nicht nur die Regel erfüllt:
1. In einem **gedruckten** CYOA ist Rück-Sortierung nach einem Konvergenzknoten praktisch unmöglich
   (kein Zustand, nur „weiter mit Nr. X"). Variante b müsste den Twist faktisch doch dreifach ausgeben.
2. Die **Pfad-Identität** (A mutig / B kühl / C sozial) ist der Mehrwert eines Mehrpfad-Buchs. Genau am
   Twist — dem Höhepunkt — ist identischer Text die größte verschenkte Chance.
3. Das Recycling-Risiko ist **beherrschbar** (Liste + Manuskript hat schon drei verschiedene Inszenierungen
   vorgezeichnet: Brenner zeigt [Kap. 7], Aktenlogik [Kap. 12], Kloß' Geständnis [Kap. 6/13]).

---

# Zweite Architektur-Frage: Theo-allein / Johanns Zweig — auf welchen Pfaden?

Das ist der **emotionale Höhepunkt** (Kap. 11). Im Manuskript passiert er **einmal**. Im CYOA-Graph oben
ist er auf **A (A10) und C (C7)** — **nicht** auf B.

- **Pro (A+C):** Beide sind „am Friedhof handelnde" Pfade; der Beat ist die Belohnung fürs Risiko (Theo
  mitnehmen). B ist der Recherche-/Distanz-Pfad → dort wirkt er aufgesetzt.
- **Risiko:** Wieder ein Beat, der auf 2 Pfaden steht → Recycling. Gegenmittel: in A aus dem „Folgen"
  heraus, in C aus „mit Kloß" heraus — verschiedene Vorläufe, gleicher Kern-Fund.
- **Alternative (zu entscheiden):** Johanns Zweig **nur auf C** (dem stärksten Pfad), A erreicht den
  Twist über Brenners Zeigen ohne den Zweig. Spart einen Doppel-Beat, schwächt aber A emotional.

> Vorschlag: **A + C** behalten (wie gezeichnet), Recycling über Vorlauf-Variation lösen.

---

# Knotenzahl-Schätzung (fällt erst hier, nicht vorab)

| Block | Knoten |
|------|--------|
| Prolog P1–P5 | 5 |
| Pfad A (A1–A12 inkl. Scheiter/Kapelle-Zweig) | ~13 |
| Pfad B (B1–B7) | ~8 |
| Pfad C (C1–C8) | ~9 |
| Dead Ends D1, D3, D4, D5 | 4 |
| Enden EA1–4, EB1–3, EC1–4 | 11 |
| Geheim-Ende | 1 |
| **Summe** | **~51** |

→ Liegt unter dem Richtwert 55–65 → **gesund** (Tiefe statt Menge, Plan §9a). Reserve für 2–3
Zwischen-Abschnitte vorhanden, falls ein Übergang zu gedrängt wirkt. **Finale Zahl nach 1b.**

---

# Offene Punkte für deine Freigabe (1a)

1. **Twist-Pol: Variante a** (3 getrennte) — bestätigen?
2. **Theo-allein/Johanns Zweig auf A+C** (nicht B) — bestätigen?
3. **Pfad B erreicht Twist über Akten/Protokoll** (ohne Johanns Zweig) — ok?
4. **Topologie insgesamt** (Wahlpunkte/Enden-Zuordnung oben) — Einwände?
5. Klein-Klär (aus KANON): **UV-Lampe = aus Silbers Wohnung** · **„M. Silber" im CYOA erwähnen ja/nein** —
   jetzt oder im Schreibschritt?
