# Arbeitsplan — Band 5 "Der Schleier" (FINALE Staffel 1)

## Die Geisterspürer, Band 5 (Linear-Manuskript)

> Dieser Plan beschreibt **nur das Schreiben des Buchs** (Manuskript, 18 Kapitel).
> Cover und Publishing folgen NACH dem fertigen Manuskript.
>
> ⚠️ **PRÄZISIERUNG 2026-07-17 (vom Autor bestätigt):** Hier stand *„Cover, CYOA, Publishing
> folgen wie bei Band 1–4"* — missverständlich. Der Stand:
> **Die CYOA ist NICHT eingestellt, sondern nachgelagert.** Das **lineare Buch verkauft sich
> deutlich besser**, darum hat es Vorrang. CYOA fertig: **Band 1** (111 Dateien, eigene
> Skripte, eigene Ads-Kampagne), teilweise **Band 2** (18). **Band 3, 4 und 5 stehen aus**
> (Ordner angelegt, leer).
> **→ Für Band 5 gilt: linear zuerst und vollständig. CYOA später — kein Blocker.**
>
> Vorgehen: identisch zum bewährten **Band-4-Prozess** ([../Band4/PLAN_Band4.md](../Band4/PLAN_Band4.md)) —
> Continuity → Outline → Szenenplanung (+ Setup/Payoff-Tracker + Cliffhanger-Register
> parallel) → Kapitel → Kompilieren.
>
> **Besonderheit Band 5:** Es ist das **Finale der ganzen Staffel** und muss zwei
> Dinge gleichzeitig leisten: (1) das 200-Jahre-Graven-Rätsel vollständig auflösen,
> (2) den leisen Übergang zu Staffel 2 legen — siehe [../Staffel2/PLAN_Staffel2.md](../Staffel2/PLAN_Staffel2.md),
> **Abschnitt 4 (unbedingt VOR dem Outlinen lesen).**

---

## 0. Kurzfassung (TL;DR)

- **Was:** Band-5-Manuskript, **18 Kapitel**, ~20.000–23.000 Wörter (Finale, etwas länger als B4 ~15.900–19.100; nicht aufblähen).
- **Titel (steht):** "Der Schleier" · **Grusel-Level:** 8/10 (höchster der Serie) · **Serien-Thema (Vorschlag):** FRIEDEN / ABSCHIED (Freigabe offen).
- **Was Band 5 auflöst:** Alwin Graven / "der Erste" — der Ursprung von allem. Das Finale.
- **Was Band 5 säen muss:** GENAU EINEN leisen Staffel-2-Faden (kein Cliffhanger, der das Finale beschädigt). Details unten + Staffel-2-Plan.
- **Status:** Konzept-Kern (Abschnitt 4) **ENTSCHIEDEN** (User 2026-07-15) inkl. Graven-Mechanik-Profil. Nur Restpunkte offen (Abschnitt 8). **Nächster Schritt: Phase 1 (Continuity).**

---

## 1. Warum dieser Plan so aussieht (Begründung)

Der Band-4-Prozess hat funktioniert (16 Kapitel, alle Tracker, saubere Twist-Fairness).
Band 5 übernimmt ihn **1:1**. Dieselben Dateitypen:

```
Band5/
  PLAN_Band5.md                  ← dieses Dokument
  Kontinuitaet_Band5.md          ← Continuity-Tracker (Stand nach Band 4 einpflegen)
  Story_Outline.md               ← Dramaturgie, 18 Kap.
  Detaillierte_Szenenplanung.md  ← Szene 1–4 pro Kapitel
  Setup_Payoff_Tracker.md        ← Tschechow-Tabelle (erbt offene Fäden aus B1–4)
  Cliffhanger_Register.md        ← Muster-Kontrolle über alle 18
  Manuskript/
    Kapitel_01.md … Kapitel_18.md
    Manuskript_Band5_Komplett.md
Scripts/
  build_manuskript_komplett_band5.py  ← aus Band-4-Skript ableiten
```

**Einziger echter Unterschied zu Band 4:** Band 5 schließt **alle** Serien-Fäden statt
einen Fall aufzumachen. Der `Setup_Payoff_Tracker` erbt deshalb die offenen Fäden aus
Band 1–4 (Abschnitt 2) und muss am Ende **restlos leer** sein — außer dem einen
bewusst gesetzten Staffel-2-Faden.

---

## 2. Inhaltliche Ausgangslage (steht fest — aus Band 4 verifiziert)

Aus [../Band4/Story_Outline.md](../Band4/Story_Outline.md) (K15/K16 + "Verbindungen zur Gesamtserie") und dem Band-4-Finale:

**Serien-Fakten (nicht verhandelbar):**
- Titel Band 5: **"Der Schleier"** · Grusel **8/10** · Finale: Graven / "der Erste".
- Karten-Stand: **4 von 12 durchgestrichen** (Lina, Brenner/Voss, Marlene, Faber). **8 offen.**
- Der **rote GRAVEN-Kreis glüht jetzt von selbst** — stärker als alle Markierungen.
- Gründer/Geheimnis: **Alwin Graven**, Alchemist, gründete Gravenstedt **1823**. Sein
  krankes Kind → er versuchte die Grenze Leben/Tod zu öffnen → Experiment scheiterte →
  die Toten können Gravenstedt seither nicht verlassen. (Kanon `Buchkonzept.md`.)

**Der Zustand, in dem Band 5 startet (aus B4-Finale):**
1. **Silber ist erlöst und weitergegangen** — lebend befreit, dann freiwillig gegangen
   (hoffnungsvoll, kein Tod). **NICHT mehr verfügbar als Figur** (nur Hinterlassenes /
   Erinnerung). Sie hat den Kindern die Aufgabe endgültig übergeben.
2. **Silbers letzte Warnung an Nora (B4 K15):** *"Der Erste hat euch gesehen. Er wird
   kommen. Nicht zu einem Ort auf der Karte. Zu EUCH. Passt auf Schatten auf — er weiß,
   was ihr noch nicht wisst."* → **Zwei Pflicht-Payoffs für Band 5:** Graven kommt zu
   IHNEN; und **Schatten trägt ein Geheimnis.**
3. **Der fremd vervollständigte Satz (B4 K16):** *"Der Erste ist nicht im Tunnel. Er ist
   — schon wach. Und er kennt eure Namen."* (Handschrift, die NICHT Silbers ist.)
4. **Erster Graven-Kontakt geschah bereits (B4 K11–12):** Graven rief Noras Namen; sagte
   *"Du bist wie er, Kind."* → **Payoff-Pflicht:** Was heißt "wie er"? (→ Noras Versuchung, Abschnitt 4.)
5. **Schatten gehört jetzt den Kindern** (Silbers letztes Geschenk); er hat gewählt zu
   bleiben. Sein **hartes, neues Knurren** richtet sich am Ende von B4 aus dem Fenster
   **in die Stadt hinaus.**

**Offene Fäden, die Band 5 auflösen MUSS (Erbe aus B1–B4):**
- **A. Graven / "der Erste" selbst** — wer er heute ist, was er will, wie er aufgelöst wird. (Das Finale.)
- **B. Der "Schleier"** — was er ist, wie er geschlossen/geheilt wird.
- **C. Die 8 verbleibenden Markierungen / gefangenen Geister** — ihr Schicksal.
- **D. Schattens Geheimnis** — "er weiß, was ihr noch nicht wisst"; **plus** die noch
  offenen B-Fäden: *Schatten altert nicht* + *Friedhofs-Verweigerung (B2: "hat auf dem
  Friedhof etwas gesehen, geht seither nicht mehr hin")*. → **ENTSCHIEDEN (User 2026-07-15):
  Band 5 löst Schatten VOLLSTÄNDIG auf.** Nichts bleibt für Staffel 2 offen (Konzept-Regel 7).
- **E. "Hütet euch vor dem Ersten. Er ist nicht wie die anderen"** (Silbers Brief, B1) —
  muss eingelöst werden: Graven IST gefährlicher/aktiver als jeder bisherige Geist.

---

## 3. Qualitäts-/Konsistenz-Regeln (übernommen, nicht neu erfunden)

Aus [../CLAUDE.md](../CLAUDE.md), [../Dokumentation/Schreibstil_Regeln_10_Jahre_Die_Geisterspuerer.md](../Dokumentation/Schreibstil_Regeln_10_Jahre_Die_Geisterspuerer.md),
[../Dokumentation/Die_Geisterspuerer_Author_Info.md](../Dokumentation/Die_Geisterspuerer_Author_Info.md) und [../Dokumentation/Spannungs_Pruefplan.md](../Dokumentation/Spannungs_Pruefplan.md):

- **Perspektive:** 3. Person nah an Nora. Nur, was Nora wahrnimmt.
- **Kapitellänge real:** ~1.150–1.300 Wörter (wie Band 4). Kapitel ist fertig, wenn es funktioniert, nicht bei einer Zahl.
- **Sätze** max. 18 Wörter, kein Passiv. **Absätze** 3–6 Zeilen, viel Weißraum. Ein-Wort-Zeilen in Schock-/Schlüsselmomenten.
- **Dialog** ≥ 35–45 % (Atmosphäre-/Maximal-Ernst-Kapitel dürfen ~23 %, dann Nachbar dialogreich).
- **Emotionen körperlich** — nie abstrakt.
- **Grusel-Humor-Balance:** nach Grusel binnen 1–2 Absätzen Humor (Theo) — **Ausnahme im Finale: mehr Maximal-Ernst-Momente erlaubt** (Graven-Konfrontation), aber Theo bleibt Ventil; das Buch darf nie hoffnungslos werden.
- **Schatten:** mind. 1 Reaktion pro Kapitel (Pflicht). Im Finale ist Schatten zentraler als je → leicht.
- **Cliffhanger** am Kapitelende (Pflicht); nächstes Kapitel löst ihn DIREKT auf.
- **Umlaute:** echte Umlaute (ä/ö/ü/ß).
- **⚠️ Ghost-Regel bleibt HEILIG — auch im Finale (wichtigste Regel des Buchs):** Graven
  ist **gefährlicher und aktiver** als jeder bisherige Geist (löst "nicht wie die
  anderen" ein) — aber er bleibt **ein trauernder Mensch, kein Dämon.** Aufgelöst wird
  er durch **Empathie/Verstehen, NIE durch Kampf/Überlisten/Bannen.** Das ist die
  Serien-These, jetzt auf ihren Ursprung angewandt. Kein Blut, kein Body-Horror, kein
  Kind kommt zu dauerhaftem Schaden. "Kribbeln ja, Albträume nein" gilt auch bei 8/10 —
  die Gefahr kommt aus **Einsatz und Ausmaß** (die ganze Stadt), nicht aus Grausamkeit.
- **Grusel-Eskalation der Serie:** 3 → 4 → 6 → 7 → **8/10.** Spürbar größer als Band 4:
  von EINEM Raum (B4) auf die **ganze Stadt** (Geisternacht).

---

## 4. Konzept-Fundament (weitgehend ENTSCHIEDEN — Stand 2026-07-15)

> **Verriegelt (User-Freigaben 2026-07-15):** Graven-Kern A1 (leere Tür / Kind längst
> hinüber — mitentschieden durch das Echo-Kind), das **Echo-Kind**, die **Fear-first-Struktur**,
> **Sarah bleibt raus**, Schatten **voll auflösen**, Noras Versuchung = **Hebel B** ("nie
> wieder loslassen", konkret verankert), plus die Grusel-Mechanik-Upgrades unten.
> Plus **Graven-Mechanik-Profil** (Warum-jetzt, Schatten-Anker, Psychologie/Stimme/Regeln),
> **Instrument von 1823** als Objekt, **18 Kapitel.** **Noch offen (Abschnitt 8):** Vaterfrage,
> Schatten-Wortlaut, Thema/Codewort, Geisternacht-Datum. Ab hier ist alles Kanon für die Outline.

### Prämisse (Ein-Absatz-Fassung)

Graven wartet nicht mehr — er **kommt zu den Kindern.** **Warum jetzt, nach 200 Jahren?**
Weil Silber (40 Jahre) und die Kinder (4 befreite Geister) die gefangenen Toten entfernt
haben — genau die "Ankermasse", die den Schleier stabil hielt. **Ihre eigene Heldentat hat
ihn so weit geschwächt, dass Graven in *dieser* Geisternacht sein Fenster bekommt** (bitterer
Preis, kanontreu zu Silbers "der Schleier wird dünner"). **Warum ausgerechnet die Kinder?**
Sie haben **Schatten** — den **lebenden Anker** des Schleiers (den Hund der Gründungstragödie,
vom Schleier gehalten wie die Toten, nur lebend). Graven **braucht Schatten**, um den Riss zu
vollenden. Auf die Geisternacht zu will Graven tun, wofür er 1823 die Grenze öffnete: zu
seinem toten Kind **hindurch** — er will den Schleier mit dem **Instrument von 1823**
(Schleier-Apparat/-Spiegel, sein Signatur-Objekt) **ganz aufreißen.** Das wäre die
Katastrophe: die Grenze kollabiert, und **die Lebenden werden ins graue Dazwischen gezogen —
zuerst Theo und Schatten** (gefangen wie Silber hinter Fabers Tür, nur stadtweit). **Was
Graven in Wahrheit festhält (der Twist, Makro-Spiegel zu Fabers leerem Medaillon):** nicht
sein Kind — nur dessen **Echo.** Das Kind hat vor langer Zeit selbst **losgelassen** und ist
friedlich hinübergegangen. Zurück blieb ein **Nachhall im Schleier**: eine kindsgroße
Gestalt, die durch die Stadt geht, immer dieselben Bewegungen wiederholt, nach Graven ruft —
aber leer ist (siehe Echo-Kind, unten). Graven merkt nicht, dass er nur ein Echo umklammert.
**Nur Graven konnte nicht loslassen.** Aufgelöst wird er nicht im Kampf: Die Kinder erreichen
in der Geisternacht seinen **Ursprungsort von 1823** und wenden dort — **verwoben, nicht
abgehakt** — alles an, was sie in vier Bänden lernten (Zuhören → Erinnern → Vergeben →
Loslassen). Schlussstein ist **Noras Wahl** — sie widersteht Gravens Versuchung, selbst nie
mehr loszulassen, und zeigt ihm die Wahrheit des Echos. Graven lässt los. Das Echo darf
endlich ruhen. Der Schleier reißt nicht — er **heilt.** Die Geisternacht wird die **große
Erlösung:** alle wartenden Toten gehen hinüber (**Lina aus Band 1 unter ihnen** — Leser-Payoff),
die 8 Markierungen löschen sich, die Karte ist vollendet. Graven findet Frieden. Schatten
wird frei. Die Stadt ist frei — und trägt fortan eine **Narbe** (leiser Staffel-2-Faden,
Abschnitt 5).

### ⚠️ Konzept-Regeln (verbindlich)

1. **Graven bleibt ein Mensch (Ghost-Regel im Finale).** Gefährlicher, aktiver, "nicht
   wie die anderen" — aber am Ende ein Vater in Trauer, kein Monster. Empathie löst,
   nicht Gewalt. (Non-negotiable, Abschnitt 3.)
2. **Neuer Mechanismus, nicht Band-4-Wiederholung.** Band 4 = ein Kind (Theo) ZEIGT dem
   Geist das Loslassen durch Opfer. Band 5 = die **POV-Heldin Nora** wird in **Versuchung**
   geführt, selbst festzuhalten, und wählt anders. Der Klimax ist **körperlich und aktiv**
   (Wettlauf, reißender Schleier, echte Gefahr), aber die vier Serien-Methoden werden
   **organisch verwoben** — NICHT als vier getaktete Puzzle-Stufen (kein Videospiel-Boss;
   sonst Schematismus, den B1–4 vermieden). Anderer Mechanismus, andere Figur, aktiv statt
   nur gedacht. Reframing gegen B4: B4 = etwas *hergeben*, das man hält; B5 = ein *Ende
   annehmen*, das man nicht ändern kann.
3. **Die 8 Geister werden nicht "abgehakt".** Kollektive Erlösung durch die Schleier-Heilung
   (Massen-Abschied, Lina dabei). Emotionaler Payoff, keine 8 Mini-Wiederholungen.
4. **Das Echo-Kind bleibt tragisch, nie dämonisch (Ghost-Regel gilt auch für IT).** Es ist
   kein Monster und kein Gegner — es ist die traurigste Sache im Buch: ein leerer Nachhall.
   Der Grusel entsteht aus dem **Uncanny** (ein hohles, wiederholendes Kind, das dich ansieht,
   ohne dich zu sehen), nicht aus Bosheit. Es "jagt" niemanden; es wiederholt nur.
5. **Fear-first (Upgrade B).** Graven wird in Akt 1–2 **erst unheimlich/bedrohlich** aufgebaut
   (Versprechen "nicht wie die anderen" einlösen); die tragische Wahrheit kippt erst in Akt 3
   die Angst in Mitleid. Nicht früh humanisieren.
6. **Konkreter Showdown-Ort (Upgrade C).** Die Stadt darf ausdünnen, aber der Höhepunkt
   spielt an **einem** Ort: Gravens Ground Zero von 1823. Keine diffuse Stadt-Nebel-Kulisse.
7. **Schattens Geheimnis: VOLL auflösen (User-Entscheidung 2026-07-15) — und plotnotwendig.**
   Band 5 klärt Schatten **restlos** — inkl. "*warum altert er nicht*" + Friedhofs-Verweigerung
   (B2) + Silbers Warnung "er weiß, was ihr noch nicht wisst". Schatten ist **schleier-gebunden:**
   der Hund der Gründungstragödie, vom Schleier gehalten wie die Toten, nur lebend (deshalb
   200 J. / kein Altern / Geist-Sinn; Friedhofs-Verweigerung = er sah dort Graven/das Kind).
   **Er ist der LEBENDE ANKER des Schleiers — und genau deshalb braucht Graven ihn, um den
   Riss zu vollenden. DAS ist der Grund, warum Graven zu den Kindern kommt** (macht Schattens
   Auflösung strukturell unverzichtbar, nicht bloß ein Reveal). Wenn der Schleier am Ende
   **heilt, wird Schatten frei = wieder ein normaler Hund**, der endlich altern und zu einer
   Familie gehören darf. Bittersüß, hoffnungsvoll, **kein Tod** (lebt weiter, für Staffel 2 als
   normaler, alternder Hund). "Nicht magisch"-Regel: er hatte nie Kräfte — er war *gehalten*,
   wie die Geister. **Nichts von Schatten bleibt für Staffel 2 offen** (die soll eigenständig
   sein, NEUE Geheimnisse — siehe [../Staffel2/PLAN_Staffel2.md](../Staffel2/PLAN_Staffel2.md)). → Der leise Staffel-2-Faden
   (Abschnitt 5) ist deshalb NICHT Schatten, sondern die "Leuchtturm"-Narbe.

### Der Antagonist: ALWIN GRAVEN — Profil (analog zum Sammler-Profil aus B4)

> Diese Schicht fehlte dem Plan zuerst (Story + Thema stark, Antagonisten-Mechanik dünn).
> B4 hatte sie über das Sammler-Profil. Hier nachgezogen (User-Freigabe 2026-07-15).

**Psychologie — und warum er NICHT "Faber, nur größer" ist (Abgrenzungs-Tests):**
- **Faber (B4):** *Angst vor der Leere* → hortet **alles** (nach außen, panisch, wahllos).
- **Marlene (B3):** *Schuld* → Selbstbestrafung (nach innen, passiv).
- **GRAVEN:** *Überzeugung / Hybris / Verleugnung* → opfert **alles für das EINE** (ruhig,
  gewiss, aktiv). Er hortet nicht und bestraft sich nicht — er **weigert sich, eine Realität
  anzunehmen**, und beugt eine ganze Stadt diesem einen Willen. Er glaubte 1823, den Tod
  befehligen zu können — **und glaubt es immer noch.** Das ist eine eigene, dritte Psychologie
  (Hybris statt Angst/Schuld) → kein Recycling.

**Stimme (bisher undefiniert — jetzt festgelegt):** ruhig, höflich, vernünftig, fast **sanft** —
**nie tobend.** Der gruseligste Typ ist der, der überzeugt ist, recht zu haben. Er spricht mit
Nora wie zu einer **Gleichgesinnten** ("du bist wie ich, Kind") — das macht die Versuchung
gefährlich und zahlt "Du bist wie er" (B4) ein. Kontrast zum Echo-Kind (leer/wortlos) und zu
Theo (nervös/witzig).

**Regeln & Grenzen (gegen "vage Allmacht" — Wachpunkt 12 hiermit gelöst):**
- **Er ist an den Schleier gebunden.** Voll handeln kann er **nur in der Geisternacht** (dünnster
  Schleier). Vorher nur "durchsickern": Kälte, Stimme, das Echo-Kind bewegen, Orte "falsch"
  machen, die 8 regen. → erklärt, warum er die Kinder nicht sofort greift (die Uhr hat Zähne).
- **Er braucht Schatten** (lebender Anker) für den Riss — deshalb kommt er zu den Kindern.
- **Was er NICHT kann:** die Lebenden direkt töten/nehmen, **bis der Riss vollendet ist.** Die
  Gefahr ist das drohende Aufreißen (Theo/Schatten würden ins Dazwischen gezogen), nicht ein
  greifender Monster-Angriff. (Hält "Kribbeln, nicht Albträume.")
- **Die Uhr:** die Geisternacht als **Datum** (Feinbau: ein konkretes Kalender-/Gründungsdatum).

**Signatur-Objekt (Serien-Muster — jeder Geist hat eins):** ✅ **das Instrument von 1823** —
der Schleier-Apparat/-Spiegel, mit dem Graven die Grenze öffnete. Es steht am **Ground Zero**
und gibt dem Showdown einen physischen Fokus (passt zum Titel "Der Schleier"). **Durch das
Instrument + Gravens zerbrochene Worte + das Echo-Kind wird 1823 ENTDECKT** (Nora-POV,
"entdecken statt vortragen" — kein Geschichts-Referat). Am Ende, beim Loslassen, wird das
Instrument still/dunkel (Äquivalent zu Fabers fallendem Medaillon).

### Die Entscheidungen im Einzelnen

**E1 — Gravens Ziel?** ✅ → **Den Schleier auf der Geisternacht ganz aufreißen, um zu seinem
Kind zu gelangen.** Menschlichste Motivation (Trauer), ins Katastrophale skaliert.

**E2 — Der Twist?** ✅ → **Das Kind ist längst hinüber; Graven hält nur dessen Echo**
(Echo-Kind, E8). Makro-Spiegel zu Fabers leerem Medaillon.

**E3 — Wie wird Graven aufgelöst?** ✅ → **Empathie + aktiver Klimax (vier Methoden VERWOBEN,
nicht getaktet) + Noras Wahl** als Schlussstein, nicht Kampf. Zahlt "Du bist wie er" aus.

**E4 — Noras Versuchung?** ✅ → **Ja, Hebel B: "nie wieder jemanden loslassen müssen".**
Das ist *wörtlich* Gravens eigener Fehler → tightester "Du bist wie er"-Spiegel, trifft
universell, braucht keine neue Backstory, **schützt Band 4** (holt Silber NICHT literal
zurück — benennt nur die Angst). Konkret verankert an: dem frischen Silber-Verlust (als
Wunde, nicht als Angebot) + der gerade erfahrenen Wahrheit, dass sie **Schatten** eines
Tages verlieren wird (er ist jetzt sterblich, Regel 7) + Mama. Nora kommt an ihren
dunkelsten Punkt (ihr Kanon-Makel "hält zu fest" — früh gesät) und wählt trotzdem das
Loslassen. *(Vaterfrage als optionaler Verstärker noch offen, Abschnitt 8.)*

**E5 — Die 8 Geister + Schleier?** ✅ → **Kollektive Erlösung durch Schleier-Heilung** (Regel 3),
Lina dabei. Karte danach vollständig.

**E6 — Struktur?** ✅ (User 2026-07-15) → **18 Kapitel, 4 Akte.** Das Finale trägt deutlich
mehr als B4 (Fear-first + Echo-Kind + Graven-Backstory + Versuchung + Klimax + Massen-Abschied
+ Schatten-Auflösung) — 16 wäre gedrängt. 18 gibt Luft (wie B1). Akt-Split: 4 / 5 / 4 / 5.

**E7 — Serien-Thema/Codewort?** ⏳ → Vorschlag **FRIEDEN** / Alt. ABSCHIED. (Abschnitt 8.)

**E10 — Graven-Mechanik & Objekt?** ✅ (User 2026-07-15) → komplettes Paket: Warum jetzt (die
Kinder schwächten den Schleier), warum sie/Schatten (lebender Anker), Psychologie (Überzeugung/
Hybris), Stimme, Regeln, Signatur-Objekt (Instrument von 1823). Details im **Graven-Profil** oben.

**E8 — Echo-Kind?** ✅ (User 2026-07-15) → Graven hält einen **leeren Schleier-Nachhall**
seines Kindes: kindsgroß, wiederholt dieselben Bewegungen, ruft nach ihm, sieht die Kinder
an, ohne sie zu sehen. Kein Monster, kein Gegner — **tragisch, nicht dämonisch** (Regel 4).
Gibt dem Twist ein sichtbares Grusel-Bild (Uncanny) und verkörpert das "leere Medaillon"
im Stadt-Maßstab. Erster Anblick in Akt 1 als **Bedrohung/Rätsel** (Fear-first), wahre
Natur (leer) erst in Akt 3.

**E9 — Sarah (Mutter)?** ✅ → **Bleibt raus** (ahnungslos wie B1–4). Fokus auf
Nora/Theo/Schatten + Graven, kein Faden zu viel.

### Der Grusel (8/10) — wie er entsteht

- **Fear-first + Echo-Kind (Regel 4+5):** Graven und das Echo-Kind sind in Akt 1–2 echt
  unheimlich (Uncanny, unberechenbar) — die Angst kommt zuerst, das Mitleid spät.
- **Konkreter Ort (Regel 6):** Höhepunkt an Gravens Ground Zero (1823), nicht diffuse Stadt.
  Die Stadt dünnt aus, aber der Schrecken bleibt eng und greifbar.
- **Konkreter, persönlicher Einsatz:** Reißt der Schleier ganz, kollabiert die Grenze und die
  **Lebenden werden ins graue Dazwischen gezogen — zuerst Theo und Schatten** (nicht die
  abstrakte "Stadt"). Gefangen wie Silber hinter Fabers Tür, nur stadtweit. Frightening,
  konkret, ohne Blut/Ekel — die Uhr hat damit echte Zähne.
- **Sicherheitsnetz franst — und heilt (Upgrade E):** In der Geisternacht **versagt
  Schattens Warnen** (er ist selbst schleier-gebunden, es zerrt an ihm), sichere Orte werden
  unsicher, Theos Witze bleiben ihm im Hals stecken → Peak-Dread. Am Ende alles
  wiederhergestellt (Schatten frei, Theo lacht) → Peak-Relief. Kontrollierte Eskalation,
  keine Dauerbedrohung.
- **Grenzen bleiben:** kein Blut, kein Body-Horror, kein Kind zu dauerhaftem Schaden;
  Ausgang ist Erlösung. "Kribbeln ja, Albträume nein" auch bei 8/10.

### Vier-Akt-Bogen (18 Kapitel, Split 4/5/4/5 — Feinbau in Story_Outline.md)

- **Akt 1 (K1–4) — Er kommt zu ihnen.** Direkt an B4-Cliffhanger an. Graven erreicht
  Zuhause/Stadt (sickert durch: Kälte, Stimme); erste Sichtungen des **Echo-Kindes als
  Bedrohung/Rätsel** (noch nicht verstanden, nur unheimlich). Die **Geisternacht** naht
  (Datum als Uhr). Gravens **Regeln** etablieren (er kann noch nicht voll handeln → warum er
  sie nicht greift). Noras Makel früh zeigen: nach dem Silber-Verlust **klammert sie**
  (überbehütet Theo, lässt Schatten nicht aus den Augen). **Schattens Warnen beginnt zu
  versagen** (es zerrt an ihm).
- **Akt 2 (K5–9) — Was in der Stadt umgeht.** Ermittlung steigert die Angst (Graven bleibt
  bedrohlich, NICHT früh humanisiert). Was ist das Echo-Kind? **Warum braucht Graven gerade
  Schatten?** → erste Enthüllung: Schatten ist der **lebende Anker** (Payoff Silber-Warnung).
  **Warum jetzt:** die Kinder begreifen, dass ihr eigenes Befreien den Schleier geschwächt hat
  (bitterer Preis). Die Stadt dünnt aus, die 8 regen sich. Akt-Ende: erste Ahnung, dass das
  Kind-Ding **leer** ist — erster Riss Richtung Tragik.
- **Akt 3 (K10–13) — Die Wahrheit / Nora ist wie er.** Der **Kipp-Moment:** am/über das
  **Instrument von 1823** + Gravens zerbrochene Worte wird die Wahrheit *entdeckt* (Kind hat
  losgelassen, das Echo ist alles, was blieb) — Angst wird Mitleid. Graven konfrontiert Nora
  ruhig als "Gleichgesinnte", bietet die **Versuchung** (E4). Ihr dunkelster Punkt — sie wankt
  echt. Tiefpunkt: Graven **beginnt das Aufreißen**, Geisternacht, Sicherheitsnetz voll
  zerrissen; **Theo/Schatten drohen ins Dazwischen gezogen zu werden** (8/10).
- **Akt 4 (K14–18) — Der Schleier.** Wettlauf zu Gravens **Ground Zero** unter der Uhr. In
  **einer durchgehenden, gefährlichen Konfrontation** wenden die Kinder das Gelernte
  **verwoben** an (Theo *hört zu*, als Graven "tobt"; eine *Erinnerung*; Graven muss sich
  *vergeben*; **Loslassen** als Schlussstein) — **Theo trägt einen Schlüsselmoment** (wie B4).
  **Noras Wahl:** sie widersteht der Versuchung und zeigt Graven die Wahrheit des Echos. Graven
  lässt los, das Instrument wird still, das Echo darf ruhen, der Schleier **heilt.**
  Massen-Abschied (**Lina dabei**), 8 Markierungen löschen sich. **Schatten wird frei**
  (normaler Hund). Sicherheitsnetz wiederhergestellt (Theo lacht). Ausklang + **EIN leiser
  Staffel-2-Faden** (Leuchtturm-Narbe).

---

## 5. ⚠️ Staffel-2-Brücke — was Band 5 mitliefern MUSS

> Aus [../Staffel2/PLAN_Staffel2.md](../Staffel2/PLAN_Staffel2.md), Abschnitt 4. Beim Outlinen von Anfang an mitdenken —
> nachträglich einzubauen ist teuer.

1. **Graven vollständig auflösen** — kein Rest-Antagonist, keine Fortsetzungs-Schuld. ✅ (E1–E3 tun das.)
2. **Neuer Schleier-Zustand: "geheilt, aber vernarbt".** Nicht einfach "weg". Die geheilte
   Narbe macht Gravenstedt zu einer **dünnen Stelle / einem Leuchtturm** — das ist der
   Mechanismus, der Staffel 2 (Geister von außerhalb / der "Anti-Silber") erst ermöglicht.
   → Beim Finale so formulieren, dass der Schleier heilt, aber eine Spur bleibt.
3. **Die alte 12er-Karte abschließen** (E5: alle 8 frei → Karte vollständig). Staffel 2 = neue Landkarte.
4. **GENAU EINEN leisen Faden pflanzen — KEIN Cliffhanger.** Das Finale muss sich
   abgeschlossen anfühlen. **⚠️ NICHT mehr Schatten** (der ist voll aufgelöst,
   Konzept-Regel 7). Kandidaten (einen wählen bei der Outline):
   - Der **geheilte Schleier hinterlässt eine Narbe** — Gravenstedt ist jetzt eine dünne
     Stelle / ein "Leuchtturm". Das Schlussbild deutet an, dass die Heilung die Stadt
     *sichtbar* gemacht hat für etwas/jemanden draußen. (Direkter Einstieg in den
     Staffel-2-Mechanismus.)
   - Ein **lebender Fremder**, der die Kinder am Rand beobachtet (der spätere Anti-Silber, unbenannt).
   - Ein **einzelnes neues Flackern** in der geheilten Stadt — nicht auf der alten Karte.
   > Empfehlung: **Leuchtturm-Narbe** als Haupt-Seed (zahlt den Staffel-2-Mechanismus direkt
   > ein), ggf. als letztes Bild mit einem einzelnen neuen Flackern. NUR EINER trägt — kein
   > Feuerwerk, und er darf die Graven-Auflösung nicht relativieren.

---

## 6. Konkrete Arbeitsschritte (Phasen — wie Band 4)

- **Phase 0 — Konzept-Entscheidungen:** ✅ **weitgehend ERLEDIGT (User 2026-07-15).** E1–E5,
  E8, E9 entschieden + Grusel-Upgrades (Echo-Kind, Fear-first, Ground-Zero, vier Methoden,
  Sicherheitsnetz, Theo/Lina) + Graven-Mechanik-Profil + Instrument 1823 + 18 Kapitel. Nur
  Restpunkte offen (Abschnitt 8): Vaterfrage, Schatten-Wortlaut, Codewort, Geisternacht-Datum.
  Abschnitt 4 ist ab jetzt Kanon.
- **Phase 1 — Continuity:** ✅ **ERLEDIGT (2026-07-15).** `Band5/Kontinuitaet_Band5.md`
  angelegt (Format wie B4): Stil-Merkblatt, Grusel 8/10, Figuren-Stand nach B4, **volles
  Graven-Profil + Echo-Kind + Instrument**, Eigennamen/Fakten, "Was die Kinder wissen / noch
  nicht wissen", Gegenstände, 7 zu prüfende Widersprüche, offene Fäden, leere Gerüste
  (Zeitlinie/Akt-Fortschritt/Dialog-Bilanz). **★ Kern-Knoten gelöst:** "Kind ging hinüber"
  vs. "Tote können die Stadt nicht verlassen" → *hinüber = über den Schleier (Frieden), wie
  jede Befreiung*; das Kind war der erste Fall, der loslassen konnte, während Graven festhielt.
  Kein Widerspruch. Nächster Schritt: Phase 2 (Outline).
- **Phase 2 — Story_Outline.md:** ✅ **ERLEDIGT (2026-07-15).** Alle 18 Kapitel (Kernszene/
  Schatten/Humor/Cliffhanger-Typ/Wort-Ziel), Buchkonzept, großer Twist, **eigener MECHANIK-/
  PHYSIK-Abschnitt** (Anti-Story-Fehler), Eskalations-Marker, Übersichtstabelle (~22.050 W),
  Serien-Verbindungen, Twist-Logik (4 Methoden verwoben, faire Hinweise), offene Outline-
  Entscheidungen, Wachpunkte, Checkliste. **★ Selbstprüfung fand & schloss 3 Story-Löcher:**
  (1) Schatten kann die Stadt nicht verlassen (sonst "warum nicht wegbringen?"); (2) Sarah =
  Nachtschicht (sonst "wo ist Mama?"); (3) Heilung befreit alle 8, weil Graven die Wurzel ist
  (schützt "jeder Geist eigene Methode"-Regel). Plus: Spiegel früher geseedet, Anti-B4-
  Wiederholung (kein Objekt-Geschenk im Klimax), Humor-Cluster-Wachpunkt. Nächster Schritt:
  Phase 3 (Szenenplanung + Tracker).
- **Phase 3 — Szenenplanung + Tracker:** ✅ **ERLEDIGT (2026-07-16).** Alle drei Dateien:
  `Setup_Payoff_Tracker.md` (10 geerbte B1–4-Fäden + 19 neue Setups, alle gemappt; 2 Twist-
  Ketten fair-play-geprüft; nur B18/Staffel-2 offen), `Cliffhanger_Register.md` (18 Cliffhanger,
  **Häufung K11–14 durch Um-Typisierung behoben**, keine 2 gleichen in Folge), `Detaillierte_
  Szenenplanung.md` (Szene 1–4/Kap. + alle 17 Übergänge geprüft, lösen sofort auf).
  **★ Re-Review (Score 9,0→~9,4) fand & fixte 3 Doc-Konsistenz-/Handwerks-Punkte:** (1) Outline-
  Übersichtstabelle an die neuen Cliffhanger-Typen synchronisiert; (2) Recherche-Kapitel-Warnung
  (K5/K6/K3/K8 = Langeweile-Risiko → eskalierende Funde + Live-Dialog); (3) K11 dialogreich halten
  (bricht das K10/K12-Maximal-Ernst-Cluster). Nächster Schritt: Phase 4 (Kapitel schreiben).
- **Phase 4 — Kapitel schreiben (1→18).** 🔄 IN ARBEIT. Nach JEDEM Kapitel: Continuity +
  Setup/Payoff + Cliffhanger-Register updaten, `Spannungs_Pruefplan` anwenden (Messung), Fixes.
  Vierer-Review nach jedem Akt.
  - ✅ **Akt 1 (K1–4) GESCHRIEBEN & überarbeitet (2026-07-16).** Manuskript/Kapitel_01–04.md,
    3.567 W. Review-Score 7,5→~8,5: Kapitel waren zu kurz + zu viele lange Sätze → ausgebaut
    (Dialog-Beats, faire Hinweise, Continuity-Fix Notizbuch) + Sätze gebrochen (0–1 >18W/Kap.).
    Cliffhanger BILD/STIMME/AKTION/DIALOG, alle Übergänge lösen sofort auf. Fear-first gewahrt.
    Offener Wachpunkt Akt 2: Dialog-Kurve anheben, Recherche-K5/K6 = eskalierende Funde.
  - ✅ **Akt 2 (K5–9) GESCHRIEBEN & überarbeitet (2026-07-16).** Kapitel_05–09.md, ~4.290 W.
    Review-Score 7,5→~8,7. Dialog-Kurve 29/43/28/28/35 % (Akt-1-Wachpunkt erfüllt). Beide
    Enthüllungen erarbeitet statt verkündet; Fear-first bis K9 gehalten. **Behoben:** Zeitlinien-
    fehler "zwei Jahre" (K6+K9), Logik-Widerspruch Echo-spricht-mit-Theo (→ Graven bewegt es),
    "keuchte", K8-Dialog 21→28 %, lange Sätze. **Plus:** "Warum nicht den Hund wegbringen?"
    wird in K9 auf der Seite widerlegt (Ortsschild-Szene). Doc-Fix: "Ankermasse"-Kollision raus.
  - ✅ **Akt 3 (K10–13) GESCHRIEBEN & überarbeitet (2026-07-16).** Kapitel_10–13.md, ~3.900 W.
    Review-Score 7,5→~8,8. Dialog 19/29/26/43 %. Der Kipp-Moment sitzt: der Spiegel wiederholt
    1823, die Kinder sehen, wie das Kind loslässt — **und Graven dreht sich nicht um** (er steht
    mit dem Rücken zum Glas, hat nie hingesehen → erklärt 200 J. Verleugnung, setzt K15).
    **Behoben:** eigene Kausalitäts-Wachregel verletzt (K13 "Willenskraft stoppt den Riss" →
    jetzt: der Hund blieb stehen); Graven-Telepathie (nicht in seinen Regeln); erfundener
    Nachname "Nora Weber"; "keuchte" (3. Mal); K10-Dialog 13→19 %; 7 Sätze ≥24 W gebrochen.
  - ✅ **Akt 4 (K14–18) GESCHRIEBEN & überarbeitet (2026-07-16) — ★ MANUSKRIPT KOMPLETT.**
    Kapitel_14–18.md, ~4.700 W. Review-Score 7,5→~8,8. Dialog 37/43/37/15/31 %.
    **Der Klimax läuft darauf hinaus, einen Mann dazu zu bringen, sich umzudrehen** (Payoff
    des K10-Setups). Vier Methoden verwoben: Theo *hört* (K14) → Graven *sieht hin* + Theos
    Vergeben-Beat, Name "Emilie" (K15) → Nora *macht Loslassen vor*, öffnet die Hand am
    Halsband (K16). Mechanik 4 exakt: Schatten erreicht den Spiegel im Moment des Loslassens
    → Heilung statt Riss. Anti-B4-Regel gehalten (kein Objekt-Geschenk). Lina & Co. **warten
    drüben** (kein Wiederbeleben). Schatten frei/sterblich, kein Tod. EIN leiser Faden in K18.
    **Behoben:** Echo verschwand in K14 ganz (hätte K16 den Schlussbeat genommen); K17 nur
    8 % Dialog; 43 Sätze >18 W (längster 39 → jetzt 27).
- **★ BAND 5 KOMPLETT: 18/18 Kapitel, ~17.000 Wörter** (im realen B4-Bereich ~15.900).

- **✅ Phase 4b — STIMMEN-PASS (Anti-Formel) — DURCHGEFÜHRT & ABGESCHLOSSEN 2026-07-17.**
  Ergebnis (alle Werte /1.000 W, Benchmark Band 1):
  „Und"-Erzähler **8,59 → 2,54** (B1 2,26 ✅) · „Und dann" **2,40 → 0,83** · „Zum ersten Mal"
  **1,40 → 0,59** · Kurz-Absätze **11,5 % → 9,4 %** · „nie vergessen" **4 → 1** ·
  „das Schlimmste" (Erzähler) 3 → 2 · Sätze >18 W 46 → 42. Dialog unangetastet (Tabu).
  **Regel E bestanden:** alle 18 Cliffhanger + alle Payoff-Anker (K15 „Emilie", K16 „Geh,
  Emilie" / „Er sah nicht dem Hund nach" / „Zum ersten Mal seit zweihundert Jahren",
  K17 „Da bist du ja") nachweislich intakt.
  **Zwei Ziele bewusst NICHT verfolgt** (begründet, nicht übersehen — Details Prüfplan A. 10):
  1. „Zum ersten Mal" bleibt über B1-Dichte — es ist Band 5s **tragendes Leitmotiv**; der
     zentrale Payoff (K16) und der Schlusssatz (K17) bestehen wörtlich daraus.
  2. **Dialog 31 % ist KEIN Defekt.** Band 1 hat exakt dasselbe Profil (12 von 18 Kapiteln
     unter 35 %, Spanne 18–58 %). Der Ausreißer ist Band 4 (46 %). „Nachbessern" hätte Band 5
     von der Benchmark **weg** gezogen. Ziel aus dem Plan gestrichen.
  **Bester Fund des Passes:** K15 „…und Nora begriff, dass er es seit zweihundert Jahren nicht
  ausgesprochen hatte" — Erkenntnis-Formel + Leitmotiv-Dichte **und ein echter Erzählfehler**
  (Nora kann das gar nicht wissen). → „…und es klang, als hätte er es zweihundert Jahre nicht
  mehr in den Mund genommen." **Formel-Marker zeigen oft echte Fehler an, nicht nur Stil.**
  → **Nächster Schritt: Phase 5.** Vorher empfohlen: menschlicher Read (dafür war der Pass da).

  <details><summary>Ausgangsbefund (historisch)</summary>

  Werkzeug:
  [../Dokumentation/Stimmen_Pruefplan.md](../Dokumentation/Stimmen_Pruefplan.md) (serienweit, neu 2026-07-16).
  **Muss VOR Phase 5 laufen** (sonst Rebuild) **und VOR dem User-Read** (damit der Mensch
  seine Aufmerksamkeit nicht an mechanischem Rauschen verbraucht).
  **Warum überhaupt:** Nicht die kurzen Sätze wirken maschinell (Band 1 ist mit 4,8 W/Satz
  noch kürzer und liest sich handgeschrieben) — sondern die **Formel-Dichte**. Und die
  **driftet monoton über die Serie**: „Und"-Satzanfänge pro 1.000 W = B1 **4,4** → B4 8,5 →
  **B5 13,2**. Band 5 hat 3× die Band-1-Dichte.
  **Band-5-Befund (Startpunkt, Details im Prüfplan Abschnitt 10):** „Und"-Anfang 224 (Ziel
  80–100) · dramatische Kurz-Absätze 147 = 11,5 % (Ziel 7–8 %) · „Zum ersten Mal" 23 (Ziel
  7–12) · „Und dann" 41 (Ziel 10–15) · „Nora begriff/verstand" ~8 (Ziel ≤2) · „das
  Schlimmste" 7 (Ziel ≤2) · Dialog 31 % (Ziel 35 %).
  **Kern-Regeln:** Benchmark = Band 1, **nicht auf null optimieren** · marker-weise durchs
  ganze Buch, nicht kapitelweise (Dichte ist nur global sichtbar) · Varianz-Pflicht beim
  Fixen (streichen/verschmelzen/umbauen/behalten mischen, sonst neues Muster) · **Tabu:**
  Cliffhanger-Zeilen, Dialog, Mechanik-/Kanon-Sätze · **danach BEIDE Prüfpläne neu messen**
  (Verschmelzen erzeugt lange Sätze!) + Setup/Payoff- und Cliffhanger-Register gegenlesen.

  </details>

- **✅ Phase 5 — Kompilieren: ERLEDIGT 2026-07-17, danach überarbeitet.**
  [../Scripts/build_manuskript_komplett_band5.py](../Scripts/build_manuskript_komplett_band5.py)
  → `Band5/Manuskript/Manuskript_Band5_Komplett.md` (18/18 Kapitel, **16.956 W Fließtext**).
  **Verifiziert:** alle 18 Quellkapitel wortwörtlich enthalten · Reihenfolge 1–18 · Umlaute
  intakt · Abschluss „ENDE BAND 5 / ENDE DER ERSTEN STAFFEL".

  ### ★★ SEPARATOR-BUG — betrifft BAND 1–4, nicht nur Band 5
  Beim Überarbeiten von Phase 5 gefunden. Die Downstream-Parser
  (`build_taschenbuch_docx_band*.py` **und** `build_ebook_docx.py`) machen aus **jeder**
  `---`-Zeile einen Szenentrenner (`add_scene_break` → zentriertes „✦ ✦ ✦"). Die
  Build-Skripte von Band 1–4 setzen aber **zusätzlich ein `---` zwischen die Kapitel**.
  Für den Parser ist das nicht unterscheidbar. Ergebnis im gedruckten Buch:

  > \<Cliffhanger — der letzte Satz des Kapitels\>
  > **✦ ✦ ✦**  ← Fehl-Ornament
  > \<Seitenumbruch\> → Kapitel N+1

  **Der Cliffhanger ist damit nicht das Letzte auf der Seite — ein Ornament ist es.** Das
  trifft genau die Mechanik, auf der die ganze Reihe gebaut ist (jedes Kapitel endet auf
  einem Cliffhanger). **Real gemessen: Band 4 ist mit 15 solchen Fehl-Ornamenten in den
  Druck gegangen**, Band 5 hätte 17 gehabt.

  **Fix an der Wurzel (in Band 5 eingebaut):** `---` war überladen — Szenentrenner *und*
  Kapiteltrenner. Der Kapiteltrenner ist **redundant** (`# Kapitel N` markiert die Grenze
  eindeutig) und **kein Skript splittet auf `---`** (geprüft). Also fällt er weg. Echte
  Szenentrenner: 108 → **90** (= die 18 Fehl-Trenner raus, kein echter verloren).

  **→ TODO Band 1–4:** beim nächsten Nachdruck/Update dieselbe Zeile entfernen
  (`parts.append("\n\n---\n\n")` → `parts.append("\n\n")`) und neu bauen. **Kein Textfehler,
  reine Typografie — aber es kostet jeden Cliffhanger seine Wirkung.**

  ### Weitere Änderungen an Phase 5
  - **Der Build bricht ab, statt still Falsches zu bauen.** Geprüft werden Kapitelzahl,
    lückenlose Nummerierung, Kopf-vs-Dateiname, **Titel-Eindeutigkeit** (weil bei B5 real ein
    Duplikat auftrat: „Weniger schwer" = B4 K15 → umbenannt „Die offene Hand") und **die
    Struktur des fertigen Outputs** (`pruefe_output` simuliert den Downstream-Parser und
    fängt Fehl-Ornamente, Doppel-Trenner, Ornament nach Kapitelkopf). Gegengetestet: alte
    Bauweise → 17 Fehler erkannt; fehlendes Kapitel → Build bricht ab, schreibt nichts.
  - **Wortzahl korrigiert: 17.317 → 16.956.** `len(text.split())` zählte `---`, `>` und
    `**ENDE BAND 5**` als Wörter (~2 % zu viel). Diese Zahl wandert in KDP-Metadaten und
    Planung — sie muss stimmen. Neu: `zaehle_woerter()`, konsistent mit den Prüfplan-Skripten.
  - **⚠️ TODO Produktion:** `build_taschenbuch_docx_band5.py` (noch nicht abgeleitet) braucht
    zwei Dinge: (1) defensiv einen Szenentrenner **vor** einer Kapitelüberschrift überspringen,
    egal was im Manuskript steht; (2) **die ENDE-Strip-Regex aus B4 passt NICHT** — Band 5 hat
    die Extrazeile „ENDE DER ERSTEN STAFFEL". Ohne Anpassung landet sie als Fließtext im Buch.
    Exakte Regex steht im Kopf des Build-Skripts.

  ### ✅ Frontmatter — VOM AUTOR FREIGEGEBEN 2026-07-17
  Konstanten `WIDMUNG_ZEILEN` / `EPIGRAPH_ZEILEN` oben im Skript (Änderung: ändern + neu bauen).
  - **Widmung:** *„Für alle, die Angst haben, sie hätten etwas verpasst. / Und für die, die
    sich trotzdem umdrehen."*
    **Zeile 1 überarbeitet** (vorher: *„die sich nicht umzudrehen trauen"*). Grund: eine
    Widmung wird **vor** dem Buch gelesen, und „sich nicht umdrehen" ist vorher eine leere
    Metapher. B3 („denen einmal jemand richtig zugehört hat") und B4 („die einmal jemanden
    gehen lassen mussten") benennen eine sofort erkennbare Lebenserfahrung **und** werden beim
    Wiederlesen besser. Beides zu können ist der Serienstandard. Neue Zeile 1 = Gravens
    Diagnose in Klartext (K15: „Sie haben Angst, dass Sie es verpasst haben").
  - **Epigraph:** *„Der gefährlichste Geist ist nicht der, der etwas Böses will. / Es ist der,
    der sich ganz sicher ist."* Gravens Kern = Gewissheit, nicht Bosheit. Steigert das
    Serien-Motiv (B3 = die Erlaubnis aufzuhören · B4 = die Liebe, die nicht hergibt ·
    B5 = die Gewissheit, die nicht hinsieht) **und formuliert nebenbei die Ghost-Regel der
    Reihe als Motto.** Silber kannte „den Ersten" (ihre Notiz in K6) — die Quelle stimmt.
    Kein Twist-Spoiler.
- **✅ Phase 6 — ABSCHLUSS-PRÜFUNG: BESTANDEN 2026-07-17. Manuskript inhaltlich fertig.**
  Volles Protokoll: [Setup_Payoff_Tracker.md](Setup_Payoff_Tracker.md), Abschnitt „Phase 6".
  - **Alle 10 Erb-Fäden aus B1–4 wörtlich am Text nachgewiesen** (nicht nur „geplant").
    Tabelle B: B1–B17 eingelöst, **nur B18 (Leuchtturm) bewusst offen** — wie vorgesehen.
  - **Ghost-Regel gewahrt:** keine verbotenen Begriffe. Der einzige „Monster"-Treffer (K2)
    *formuliert* die Regel: *„Es war nicht gruselig, wie ein Monster gruselig ist."*
  - **Staffel-2-Brücke: alle vier Pflichten (A–D) erfüllt** — bei (D) sogar besser als geplant
    (Plan wollte Schatten knurren lassen; das Buch löst die Spannung auf und zeigt das Licht
    über den Köpfen der Figuren).
  - Schatten in **18/18 Kapiteln mit echter Reaktion** · Sprechverben sauber · Silber nicht
    zurückgeholt · Lina & Co. nicht wiederbelebt · Schatten stirbt nicht · Content-Grenzen
    gewahrt · Zeitlinie „vier Monate" endgültig korrekt.
  - **★ Phase 6 wurde nachgeprüft (2026-07-17) und enthielt drei EIGENE Prüffehler — keine
    Buchfehler.** (1) „Tabelle B eingelöst" war eine Behauptung, keine Prüfung → nachgeholt,
    alle bestätigt. (2) Der Schatten-Check war untauglich („Schatten" heißt auch *shadow*;
    Erwähnung ≠ Reaktion) → streng neu geprüft. (3) **„Grusel 8/10" hatte ich stillschweigend
    übersprungen** → ehrliche Antwort: **nicht messbar** (Band 1 mit 3/10 hat die höchste
    Kälte-Dichte der Reihe, Band 4 mehr „Angst"-Wörter als Band 5 — Vokabeln zählen misst
    keine Angst). **Alle 6 geplanten Grusel-Upgrades sind aber nachweislich verbaut**; ob es
    als 8/10 wirkt, entscheidet der Autoren-Read.
  - **★ Prozess-Fund (kein Buchfehler):** Das Cliffhanger-Register hat eine Blindstelle — es
    typisiert nach Inhalt, prüft aber nie die **Form** des Schlusssatzes. K09–K13 enden alle
    fünf auf gesprochener Zeile. **Bewusst nicht geändert** (B1–B3 haben mit 8–9 gleichförmigen
    Enden am Stück längere Läufe; die Form folgt dem Inhalt; die fünf Zeilen sind Spitzenklasse).
    Für Band 6 ff. im Register vermerkt.
  - **~~Offene Entscheidung: CYOA-Codewort~~ — ★ GESTRICHEN 2026-07-17, war ein Irrtum.**
    Das Codewort ist **ausschließlich ein CYOA-Bauteil**: laut
    [../Dokumentation/Codewort_System.md](../Dokumentation/Codewort_System.md) versteckt jeder
    Band **3 Codewörter in seinen 3 besten Endings** (z. B. B1: E7/E16/E23) → Geheim-Ending
    (Abschnitt 300). **Ein lineares Buch hat ein Ende, keine 23.** Für Band 5 linear gibt es
    also nichts zu platzieren und nichts zu entscheiden.
    **→ Phase 6 hat KEINE offenen Punkte.** (Falls je eine Band-5-CYOA entsteht: FRIEDEN hat
    keinen Textanker (0×), LOSLASSEN ist schon B4 — dann wäre HEIMWEG der Kandidat.)

  <details><summary>Ursprüngliche Prüfliste</summary>

  `Setup_Payoff_Tracker` restlos leer (außer Staffel-2-Faden)?
  Alle Erb-Fäden aus B1–4 aufgelöst? Cliffhanger-Muster ok? Grusel 8/10 spürbar? Ghost-Regel
  gewahrt (Graven kein Dämon)? **Staffel-2-Brücke (Abschnitt 5) erfüllt?** Codewort platzierbar?

  </details>

- **★ BAND 5 IST FERTIG.** Manuskript 18/18, 16.932 W, kompiliert, alle Prüfungen bestanden.
  Offen bis zur Veröffentlichung:
  1. ✅ **Frontmatter — freigegeben 2026-07-17.**
  2. ✅ **Taschenbuch gebaut 2026-07-17.**
     [../Scripts/build_taschenbuch_docx_band5.py](../Scripts/build_taschenbuch_docx_band5.py)
     → `Output/Band5/KDP_Band5_Manuskript.docx` + `.pdf` — **104 Seiten** (B4: 97), 6×9 Zoll.
     **Am fertigen DOCX verifiziert** (nicht am Skript): 18/18 Kapitel · **0 Fehl-Ornamente** ·
     87 echte Szenentrenner · **kein ENDE-Marker im Buch** · deutsche Anführungszeichen ·
     Kapitälchen-Auftakt.
     **Vier Abweichungen zu B1–4, jede begründet im Dateikopf des Skripts:**
     (1) defensiver Skip für Trenner vor Kapitelüberschrift · (2) ENDE-Regex für Band 5s zweite
     Zeile · (3) **Frontmatter wird importiert statt kopiert** (B1–4 definierten sie in ZWEI
     Dateien — Divergenzrisiko zwischen Manuskript und Druck) · (4) kein Teaser.
     **★ Beim Prüfen des fertigen DOCX zusätzlich gefunden:** `Kapitel_18.md` endet mit dem
     Marker `**ENDE**`, der bis in den Druck durchschlug — direkt vor die Rezensions-Bitte.
     **Kein gedrucktes Geisterspürer-Buch hat ein alleinstehendes „ENDE"** (Band 1 hat den
     Marker auch im Manuskript, aber nicht im Druck; B2–B4 gar nicht). Jetzt abgefangen.
     **Lehre: das Skript zu prüfen reicht nicht — man muss das Artefakt prüfen.**
  3. 🔄 **Cover — Bilder da, drei Korrekturen offen.**
     ✅ Vorderseiten-Prompt + Rückseiten-Prompt + Klappentext geschrieben
     ([Cover/Prompts/](Cover/Prompts/), [Cover/Klappentext_Band5.md](Cover/Klappentext_Band5.md))
     ✅ `Scripts/build_cover_kdp_band5.py` fertig (aus B4 abgeleitet, **PAGES 97→104**,
     **neu: Buchrücken-Prüfung**) — läuft, erzeugt `Output/Band5/KDP_Band5_Cover_Vollcover_300dpi.{pdf,jpg}`
     in exakt 3745 × 2775 px.
     ✅ **COVER FERTIG & HOCHGELADEN (2026-07-18).** Vom Autor korrigiert und in der
     KDP-Vorschau geprüft — dort passt es. Der Rückentitel „Der Schleier" ist verifiziert
     (V1 hatte fälschlich „Die Zugemauerte Tür" = Band 4).
     *Die Restwarnungen meines Skripts (Rückenbreite, 268 dpi, 2 % Stauchung) haben sich in
     der KDP-Vorschau als unkritisch erwiesen — die Vorschau ist die maßgebliche Instanz.*
     🔧 Nebenprodukt: [../Scripts/assemble_vollcover_band5.py](../Scripts/assemble_vollcover_band5.py)
     setzt ein Vollcover exakt zusammen (Rücken + Rückentext aus der Seitenzahl berechnet).
     Für Band 5 nicht mehr gebraucht — **aber nützlich für die Band-1–4-Nachbesserung
     und Band 6.**
  4. ✅ **Klappentext fertig** ([Cover/Klappentext_Band5.md](Cover/Klappentext_Band5.md)) —
     3 Fassungen, alle Behauptungen gegen das Manuskript geprüft, Spoiler-Kontrolle bestanden.
  5. ✅ **KDP-Metadaten fertig 2026-07-18** —
     [../Dokumentation/KDP_Beschreibungen.md](../Dokumentation/KDP_Beschreibungen.md),
     Abschnitt „Buchbeschreibung Band 5". Enthält: Titel · Untertitel (wortgleich B3/B4,
     102 Zeichen) · Serientitel/-band · Preis 10,99 / 4,99 · HTML-Beschreibung (2.811 von
     4.000 Zeichen) · 7 Backend-Keywords (alle ≤ 50 geprüft) · 3 Kategorien.
     **Alle KDP-Feldgrenzen programmatisch verifiziert.**
     **★ Keywords bleiben UNVERÄNDERT zu Band 4 — bewusste Entscheidung, ausführlich begründet
     in der Datei:** Datenlage unverändert (Helium-10 2026-06-11) · Band-5-Motive
     (Spiegel/Schleier/Gewölbe/Geisternacht) haben ~0 Volumen — **zum dritten Mal dasselbe
     Muster** nach B3 (U-Bahn) und B4 (Tür/Uhr) · „Geisterhaus" (12.563) passt bei B5 sachlich
     am besten von allen Bänden · Serien-Konsistenz stärkt das Amazon-Cluster.
     **Zusätzlich vorgeschlagen:** Serienbeschreibung um „Die Reihe ist abgeschlossen"
     ergänzen (eigenes Verkaufsargument — Eltern kaufen ungern in unfertige Reihen).
  5. ⚠️ **Offene Autorenentscheidung:** Die Teaser-Seite ist leer (Band 5 hat keinen Nachfolger).
     Kandidaten im Skript kommentiert. Backmatter ist auch ohne vollständig: Rezensions-Bitte →
     Serienübersicht → Cross-Werbung (Herrenhaus-Detektive, Chrono-Agenten).
  6. **Entscheidung Band 1–4 Neu-Build** (Separator-Bug — Geschäftsentscheidung)

  ### ★ Zwei gedruckte Altlasten in ALLEN vier verkauften Bänden
  **→ Vollständige Arbeitsliste: [../Dokumentation/TODO_Nachbesserung_Band1-4.md](../Dokumentation/TODO_Nachbesserung_Band1-4.md)**
  **Entscheidung 2026-07-17: ZURÜCKGESTELLT — erst Band 5 fertig und veröffentlicht.**
  Band 5 ist von beidem nicht betroffen; nichts davon blockiert hier etwas.

  | | Fehl-Ornamente | Leseprobe real/gedruckt |
  |---|---|---|
  | Band 1 | 17 | **0 / 32** 🔴 |
  | Band 2 | 14 | 9 / 24 |
  | Band 3 | 15 | 1 / 16 |
  | Band 4 | 15 | 0 / 12 |
  | **Band 5** | **0** ✅ | — |

  **CYOA:** nachgelagert, nicht gestrichen — lineares Buch zuerst (s. Präzisierung oben).

---

## 7. Risiken & Wachpunkte (finale-spezifisch)

1. **Ton-Falle "8/10".** Höchster Grusel der Serie — aber "Kribbeln ja, Albträume nein"
   bleibt. Gefahr über Ausmaß/Einsatz (ganze Stadt, Zeitdruck), NIE über Bösartigkeit/Body-Horror.
2. **Graven als Dämon (größtes Risiko).** Die Versuchung, den Finale-Gegner "böse" zu machen,
   ist groß. Widerstehen: Graven ist der traurigste Geist, nicht der bösartigste. Sonst
   bricht die Serien-These im entscheidenden Moment.
3. **Band-4-Wiederholung (Loslassen).** Graven "muss loslassen" klingt wie Faber. Differenzieren
   über **Mechanismus** (Nora wählt, statt ein Kind zeigt) und **Maßstab** (Stadt statt Zimmer,
   das Kind ist schon fort). Twist-Logik-Block muss das belegen.
4. **Finale-Überladung.** Band 5 erbt viele Fäden (Abschnitt 2) UND löst jetzt Schatten
   voll auf. Der `Setup_Payoff_Tracker` muss am Ende restlos leer sein — bis auf den EINEN
   Leuchtturm-Faden. Priorisieren: Graven-Kern + Echo-Kind + Noras Bogen tragen; Neben-Fäden
   dienen ihnen, nicht umgekehrt.
5. **Das Finale beschädigen mit einem Staffel-2-Cliffhanger.** Nur EIN leiser Faden (Abschnitt 5).
   Das Buch muss sich als Abschluss anfühlen — die 5-teilige Reihe soll als Einheit verkaufbar sein.
6. **Die 8 Geister schematisch abarbeiten.** Konzept-Regel 3: kollektive Erlösung, kein Fließband.
7. **Silber fehlt als Figur.** Sie ist weg (B4). Führung nur über Hinterlassenes/Erinnerung —
   NICHT als lebende Helferin zurückholen (auch nicht durch Gravens Angebot, das Nora ablehnt).
8. **Fear-first verwässern (Regel 5).** Nicht der Versuchung erliegen, Graven früh sympathisch
   zu machen. Akt 1–2 = Angst; Mitleid erst Akt 3. Sonst verpufft "nicht wie die anderen".
9. **Echo-Kind kippt zum Monster (Regel 4).** Es darf nie angreifen/böse wirken — nur
   wiederholen. Grusel aus Uncanny, nicht aus Bedrohung. Sensibel für 10–12: verstörend, nicht traumatisch.
10. **Vier-Methoden-Klimax wird zur Checkliste.** Gelöst über Regel 2 (verwoben statt
    getaktet), aber beim Schreiben streng halten: die Methoden fließen in EINE Konfrontation,
    kein "jetzt Punkt 3 abhaken". Jeder Beat kostet etwas; Theo trägt einen.
11. **Exposition statt Entdeckung.** Gravens Geschichte (1823) über das **Instrument**, das
    Echo-Kind und Gravens zerbrochene Worte ERLEBEN lassen — kein Geschichts-Referat (Nora-POV,
    "entdecken statt vortragen" — Band-4-Lektion).
12. **Gravens Regeln.** ✅ Im **Graven-Profil** festgelegt (schleier-gebunden, voll erst in der
    Geisternacht, braucht Schatten, kann Lebende erst nach dem Riss nehmen). Beim Schreiben
    konsequent einhalten — nicht versehentlich früher allmächtig machen.

---

## 8. Offene Restpunkte (klein — vor bzw. während der Outline)

Der Konzept-Kern (Abschnitt 4) inkl. Graven-Mechanik, Objekt (Instrument 1823) und Struktur
(18 Kap.) ist entschieden. Offen sind nur noch Feinschliffe:

1. **Vaterfrage (Hebel-Verstärker):** War der Vater je als *verstorben* gedacht? Falls ja,
   wird die Versuchung (E4) noch schärfer (totes Kind ↔ toter Vater, exakter Spiegel) —
   dann abwägen. Falls nein: bleibt bei Hebel B wie in E4, kein Handlungsbedarf.
2. **Schatten-Erklärung (Art):** Kern steht (schleier-gebundener Anker, Regel 7). Nur die
   konkrete Ausformulierung/den genauen Wortlaut bei der Outline freigeben.
3. **E7 (Thema/Codewort):** FRIEDEN (Vorschlag) / ABSCHIED / anderes.
4. **Geisternacht-Datum:** konkretes Kalender-/Gründungsdatum als Uhr (bei der Outline setzen).
5. **Staffel-2-Faden:** Vorschlag = Leuchtturm-Narbe (Abschnitt 5, Punkt 4). Bestätigen oder wählen.

> Keiner dieser Punkte blockiert den Start von Phase 1 (Continuity). Sie können bei der
> Outline (Phase 2) fixiert werden.

---

## 9. Was dieser Plan bewusst NICHT enthält

Cover, Klappentext, KDP-Setup, Keywords, A+ Content, CYOA (Codewort/Verzweigungen/Endings),
Illustrationen. Diese folgen — wie bei Band 1–4 — erst NACH dem fertigen Linear-Manuskript.

---

*Erstellt 2026-07-15. Konzept-Kern entschieden (User 2026-07-15) — Restpunkte Abschnitt 8. Nächster Schritt: Phase 1 (Continuity).*
