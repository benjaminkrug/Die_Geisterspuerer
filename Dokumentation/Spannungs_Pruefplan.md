# Spannungs-Prüfplan – „Es darf nie langweilig werden"

Anwendbar auf JEDES Kapitel (Band 3 und folgende). Ziel: Der Leser soll nie denken *„ah, das dauert jetzt"*. Auch ruhige Szenen (Recherche, Gespräch, Ausklang) müssen **fesselnd** sein — Spannung kommt nicht nur aus Action, sondern aus **offenen Fragen, Subtext und Vorwärtsdruck**.

> **Grundsatz:** Spannung = der Leser *will wissen, was als Nächstes kommt*. Das erreicht man auf zwei Arten: **Plot-Spannung** (was passiert?) und **Mikro-Spannung** (jeder Absatz endet mit einem winzigen Sog zum nächsten). Action-Kapitel haben Plot-Spannung gratis. Ruhige Kapitel müssen die Mikro-Spannung liefern.

---

## TEIL A – Messen (objektiv, vor dem Lesen)

Führe pro Kapitel diese Messung aus (Python-Snippet unten). Vier Zahlen, vier Schwellen:

| Kennzahl | Grün | Gelb (prüfen) | Rot (überarbeiten) |
|----------|------|---------------|--------------------|
| **Längster dialogfreier Block** | < 130 W | 130–180 W | > 180 W |
| **Dialog-Anteil** | 30–45 % | 20–30 % | < 20 % |
| **Sätze > 18 Wörter** | ≤ 3 | 4–6 | > 6 |
| **Wörter gesamt** | 950–1.300 | 1.300–1.500 | > 1.500 oder < 850 |

**Wichtig – Ausnahmen, die GELB/ROT erlauben:**
- **Action-Höhepunkt** (Einsturz, Flucht): Dialog darf < 20 % sein. Aber dialogfreie Blöcke trotzdem in kurze Sätze hacken (Tempo!).
- **Auflösungs-/Katharsis-Höhepunkt** (Befreiung): Dialog darf < 20 %, lange Sätze dürfen lyrisch fließen. Aber NUR im eigentlichen Auflösungsmoment, nicht drumherum.
- In ALLEN anderen Kapiteln gilt: ein dialogfreier Block > 180 W ist fast immer eine zähe Stelle → aufbrechen.

```python
import re
t = open('Band3/Manuskript/Kapitel_XX.md', encoding='utf-8').read()
paras = [p.strip() for p in t.split('\n\n') if p.strip() and not p.startswith('#') and p.strip()!='---']
streak=mx=0
for p in paras:
    if '"' not in p: streak+=len(p.split()); mx=max(mx,streak)
    else: streak=0
d=re.findall(r'"[^"]*"',t); dw=sum(len(x.split()) for x in d); w=len(t.split())
longs=[s for s in re.findall(r'[^.!?]+[.!?]',t) if len(s.split())>18]
print(f'Wörter {w} | Dialog {100*dw/w:.0f}% | Sätze>18W {len(longs)} | längster dialogfreier Block {mx}')
```

---

## TEIL B – Lesen mit 7 Spannungs-Fragen (subjektiv, pro Szene)

Lies jedes Kapitel Szene für Szene (Szene = zwischen zwei `---`). Stelle bei JEDER Szene diese 7 Fragen. Jedes „Nein" markiert eine Gefahrenstelle.

### 1. Der Haken-Test (offene Fragen)
**Trägt der Leser am Ende dieser Szene mindestens eine unbeantwortete Frage weiter?**
- Gut: „Wer hat den Hund erkannt? Warum?" / „Wessen Fußspur führt nur rein, nicht raus?"
- Schlecht: Eine Szene, die nur Information *abschließt*, ohne eine neue Frage zu öffnen.
- **Fix:** Am Szenenende einen Mini-Hook setzen (eine Frage, ein Widerspruch, ein „aber").

### 2. Der Vorwärts-Test (kein Stillstand)
**Bewegt sich etwas — körperlich, emotional oder im Wissen der Figuren?**
- Gefahr bei: Beschreibungs-Strecken (Raum betreten, Weg gehen), Recherche-Blöcken, „und dann erklärte X".
- **Fix:** Statt eine Information *zu liefern*, lass sie *entdeckt* werden (Reaktion in Echtzeit: „Und?" – „Warte." – „Oh.").

### 3. Der „Das dauert"-Test (dialogfreie Blöcke)
**Gibt es einen Absatz-Block über ~180 Wörter ohne Dialog oder ohne Reaktion?**
- Das ist DIE Stelle, wo der Leser aussteigt. (Siehe Messung Teil A.)
- **Fix:** Eine Figur hineinreagieren lassen (ein Halbsatz Theo, ein Schatten-Beat), oder den Block in kürzere, gehackte Absätze mit Weißraum teilen.
- **⚠️ WICHTIG — gegen die Absatz-Zerteilung gegenlesen:** Ein „dialogfreier Block" ist NICHT automatisch zäh. 155 Wörter in 13 kurzen Ein-Satz-Absätzen (z. B. eine Grusel-Sequenz: „Ein Geräusch." / „Es läutete." / „Stille.") lesen sich **rasend schnell** — der Weißraum treibt. Dieselben 155 Wörter in 2 langen Absätzen sind zäh. → Erst prüfen, OB der Block aus langen Absätzen besteht. Nur dann ist er ein Problem. (Beispiel: K5 Signal-Sequenz — hoher Block-Wert, aber spannend, weil zerhackt.)

### 4. Der Schatten-Test (lebendiger Anker)
**Reagiert Schatten in dieser Szene — oder fehlt er auffällig?**
- Schatten ist das eingebaute Spannungswerkzeug: Eine Schatten-Reaktion lädt JEDE ruhige Szene mit Unheimlichkeit auf.
- **Fix:** In einer faden Szene einen kleinen Schatten-Beat setzen (Ohren, Knurren, starrt in eine Richtung).

### 5. Der Subtext-Test (nicht alles aussprechen)
**Wird hier etwas gezeigt statt erklärt — gibt es eine Lücke, die der Leser selbst füllt?**
- Gut: „Das war das Schlimmste — Theo, der nichts sagte." (Der Leser schließt: es ist ernst.)
- Schlecht: „Nora hatte Angst und war besorgt um Theo." (Nichts zu füllen = langweilig.)
- **Fix:** Eine erklärte Emotion durch eine körperliche Geste + Auslassung ersetzen.

### 6. Der Satz-Rhythmus-Test (kein Trott)
**Wechseln kurze und lange Sätze — oder reihen sich gleichlange Sätze aneinander?**
- Monotoner Rhythmus liest sich zäh, selbst bei spannendem Inhalt.
- In Spannungs-/Action-Momenten: kurze, harte Sätze. Ein-Wort-Absätze. (Siehe Teil A, „Sätze > 18 W".)
- **Fix:** Lange Schachtelsätze an Höhepunkten brechen. Einen Ein-Satz- oder Ein-Wort-Absatz einbauen.

### 7. Der Cliffhanger-Test (Pflicht am Kapitelende)
**Endet das Kapitel mit einem Sog, der zum Weiterlesen zwingt?**
- Das letzte Bild muss eine Frage, eine Drohung oder eine Umkehrung sein.
- **Fix:** Wenn der letzte Absatz „beruhigt", einen Schlusshaken ergänzen (Band 3 K16: „rührte sich der Erste").

---

## TEIL C – Die „Langeweile-Killer" (konkrete Werkzeuge)

Wenn eine Szene den Test nicht besteht, wähle den passenden Killer:

1. **Frage statt Antwort.** Beende den Absatz mit einer Unbekannten, nicht mit einer Auflösung.
2. **Reaktion einbauen.** Beschreibung → Dialog: lass eine Figur live darauf reagieren („Was?" / „Das kann nicht sein.").
3. **Verknappen.** Das schnellste Mittel gegen „das dauert": streichen. Jeder Satz, der nichts Neues bringt (kein Bild, keine Info, keine Emotion, kein Humor), fliegt raus.
4. **Sinnliches Detail statt Adjektiv-Kette.** Ein konkreter Geruch/ein Geräusch (Geruch nach nassem Stein, ein einzelner Tropfen) zieht mehr als „der dunkle, unheimliche Flur".
5. **Schatten als Verstärker.** Ein Hund-Beat macht aus Kulisse Bedrohung.
6. **Theo als Ventil + Tempo.** Ein kurzer Theo-Einwurf bricht Beschreibungs-Trott und hält Leser bei der Stange — außer in den 2–3 bewusst humorlosen Maximal-Ernst-Szenen.
7. **Den Einsatz nennen.** Warum ist das wichtig? Wenn unklar ist, was die Figuren zu verlieren haben, wird es zäh. Ein Satz, der die Konsequenz benennt, schafft Spannung.
8. **Vorausdeutung (sparsam).** Ein „Sie hätte genauer hinhören sollen" zieht den Leser vorwärts — aber max. 1× pro Kapitel, sonst Masche.

---

## TEIL D – Pro-Kapitel-Arbeitsblatt (Vorlage)

Für jedes Kapitel ausfüllen:

```
KAPITEL __ – Titel
Messung: Wörter ___ | Dialog ___% | Sätze>18W ___ | längster dialogfreier Block ___
→ Ampel: 🟢 / 🟡 / 🔴   (mit Ausnahme-Begründung falls Action/Katharsis)

Szenen-Check (pro --- Abschnitt):
Szene 1: Haken? __ Vorwärts? __ kein zäher Block? __ Schatten? __ Subtext? __ Rhythmus? __
Szene 2: ...
(Jedes "Nein" notieren + Killer aus Teil C zuordnen)

Schwächste Stelle im Kapitel: ____________________
Konkreter Fix: ____________________

Cliffhanger stark genug? __
Spannungs-Score /10: __   (vorher → nachher)
```

---

## ⚠️ Methodik-Hinweis zum Absatz-Schluss-Test (Teil E, Regel 3)

Der Test muss **gelesen**, nicht automatisch gezählt werden. Sog entsteht oft aus **Kontext/Bedeutung**, nicht aus Oberflächen-Markern (Fragezeichen, Schlüsselwörter). Beispiel: „Und da war sie." hat keinen Marker, ist aber bei einer Geist-Erscheinung der stärkste Hook überhaupt. Eine automatische Marker-Zählung stuft solche Sätze fälschlich als „neutral" ein und ist daher wertlos. → Immer selbst lesen und fragen: *Will ich nach diesem Satz weiterlesen?*

---

## TEIL E – Die 3 Goldenen Regeln (wenn du nur 30 Sekunden hast)

1. **Jede Szene öffnet eine Frage oder dreht eine Schraube.** Sonst streichen oder umbauen.
2. **Kein dialogfreier Block über ~180 Wörter** (außer Action/Katharsis) — reaktion rein oder zerteilen.
3. **Jeder Absatz zieht zum nächsten.** Lies den letzten Satz jedes Absatzes: Will man weiterlesen? Wenn nein → Haken nachrüsten.

---

## Referenz: Was bei Band 3 funktioniert hat (Positiv-Beispiele)

- **Ruhige Szene spannend gemacht:** K3 (Archiv) — Recherche wird zur Entdeckung, jeder Fund eskaliert („Ein Kind." → „mit dem Jungen darin").
- **Mikro-Spannung in Dialog:** K7 — „Eine Taschenlampe." / „Und?" / Nora hält inne. (Fund wird *enthüllt*, nicht beschrieben.)
- **Subtext:** K2 — „Das war das Schlimmste — Theo, der nichts sagte."
- **Sinnliches Detail:** K10 — „Manche Buchstaben waren tiefer als andere. Als hätte er es nachgezogen, damit es nicht verschwindet."
- **Stille als Spannung (kein Stillstand):** K8 — Nora redet, das Echo läuft mechanisch weiter = verstörender als jede Action.
- **Cliffhanger-Umkehrung:** Jedes Kapitel endet mit Frage/Drohung (K5 „die Stimme einer Frau", K16 „rührte sich der Erste").
