# KDP-Texte — S2-5 „Der letzte Schlüssel“

> Vorlage: `S2-4/KDP_S2-4.md`. **Stand 02.11.: vollständig.** Abschnitt 6 entstand zuerst (Cover).
>
> ⚠️ Jede Tatsachenbehauptung und jedes Zitat ist einzeln gegen `Manuskript/Kapitel_*.md`
> geprüft (Memory „Verkaufstexte nie geprüft“). **Jede spätere Umformulierung ist ein neuer,
> ungeprüfter Text** — nach jeder Änderung die Beleglisten neu abgleichen.

---

## 1. KDP-Metadaten

| Feld | Wert |
|---|---|
| **Titel** | Der letzte Schlüssel |
| **Untertitel** | Dein Grusel-Abenteuer für Kinder ab 12 Jahre – eine spannende Geistergeschichte für Jungen und Mädchen |
| **Serientitel** | Die Geisterspürer – Die Gebundenen |
| **Serienband** | 5 |
| **Autor** | Benjamin Krug |
| **Preis** | Taschenbuch 12,99 € · eBook 4,99 € |
| **Umfang** | **109 Seiten** · 18 Kapitel · ca. 19.000 Wörter (Build 02.11., **ohne** Widmung/Epigraph) |
| **Format** | 6 × 9 Zoll, weißes Papier |
| **Dateien** | Inhalt `Output/S2-5/KDP_S2-5_Manuskript.pdf` · Umschlag `Output/S2-5/KDP_S2-5_Cover_Vollcover_300dpi.pdf` · eBook `Output/S2-5/KDP_S2-5_eBook.docx` + `Output/S2-5/KDP_S2-5_Cover_eBook_1600x2560.jpg` |

Untertitel und Preis unverändert vom Staffel-2-Standard (S2-1 bis S2-4 identisch). „ab 12 Jahre“ im
Untertitel ist die bestehende Formel der Reihe, nicht neu formuliert.

⚠️ Kommen Widmung/Epigraph noch dazu: Manuskript neu bauen, Seitenzahl neu ablesen, Cover mit
`py Scripts/build_cover_s2_5.py --seiten <neu> --final` neu bauen — **vor** dem Upload.

---

## 2. Serienbeschreibung (Amazon Series Page — Update für S2-5)

Die Seite existiert. **Erst nach Veröffentlichung von S2-5** um die letzte Zeile ergänzen (Regel seit
S2-1: nie einen Titel bewerben, den es noch nicht zu kaufen gibt):

```html
<b>Band 1:</b> Der Gast, der blieb<br>
<b>Band 2:</b> Die Uhr, die rückwärts läuft<br>
<b>Band 3:</b> Die Frau, die niemand gehen ließ<br>
<b>Band 4:</b> Der Park, der nicht vergisst<br>
<b>Band 5:</b> Der letzte Schlüssel<br>
```

Der Fließtext der Serienseite (`S2-1/KDP_S2-1.md` Abschnitt 2) bleibt. Er nennt „eine 5-teilige
Gruselreihe“ — stimmt jetzt genau.

---

## 3. Buchbeschreibung S2-5 (Amazon Product Page)

```html
<b>Hinter einem alten Gleis rasseln im Morgengrauen die Rolltore. Eins nach dem anderen, genau nach den Nummern. Und die Reihe kommt näher.</b><br><br>

Nora (13) und Theo (11) sind nicht allein bei den leeren Lagerhallen. Ein Wächter macht dort seine Runde, grau und durchscheinend, und er schreit sie an: „Hier hat keiner was verloren!“ Schatten, ihr Hund, knurrt ihn nicht an. Er winselt.<br><br>

Dann steht Herr Halder am Bauzaun. Der freundliche Mann, der seit dreißig Jahren Geister in Schlösser sperrt, hat für diesen schon eine Falle gebaut. Denn er kennt so einen. „Älter als die anderen. Wütender. So einer wie damals.“<br><br>

Am Abend klingelt Frieda, Halders Tochter. In ihrer Tasche: alte Zeitungsausschnitte über ein Feuer, dreißig Jahre lang aufgehoben. Und ein grauer Umschlag der Feuerwehr, den ihr Vater nie geöffnet hat.<br><br>

<i>„Diesen lasse ich nicht los. Nicht noch einmal.“</i><br><br>

<b>Diesmal geht es nicht nur um einen Geist.</b> Es geht um den Mann, der ihn festhält – und um eine Frage, die er in dreißig Jahren keinem gestellt hat.<br><br>

<b>Das Finale der Gebundenen. Diesmal dreht Nora nicht um. Diesmal sieht sie hin.</b><br><br>

───<br><br>

<b>★ Für mutige Leser ab 12 Jahren</b><br>
<b>★ Kribbeln ja, Albträume nein</b> – Gänsehaut mit Sicherheitsnetz<br>
<b>★ Das Finale der Reihe</b> – die Wahrheit über das Feuer von Weißenbrück<br>
<b>★ 18 Kapitel</b> – fast jedes endet mit einem Cliffhanger<br>
<b>★ Gruselig UND lustig</b> – Theos Codewort für den Rückzug heißt „Kuchen“<br>
<b>★ Schatten ist alt geworden</b> – und trotzdem der Erste, der spürt, dass da draußen etwas ist<br><br>

<i>„Seit wann bist du der Vernünftige?“ – „Seit du aussiehst wie eine Zimmerpflanze, die einer vergessen hat zu gießen.“ – Nora und Theo beim Frühstück</i><br><br>

<b>Am stärksten mit den Bänden 1 bis 4 im Rücken</b> – das Wichtigste wird im Buch noch einmal erzählt.<br><br>

<b>Perfekt für Fans von Cornelia Funkes Gespensterjäger, Gänsehaut und Lockwood &amp; Co.</b>
```

### Warum so gebaut

- **Hook = die Szene, mit der das Buch beginnt** (K1 Ende): Tore nach Nummern, „Und die Reihe kam auf
  sie zu.“ Kein Versprechen, das erst später eingelöst wird.
- **Halder als Gegenspieler, nicht als Bösewicht:** „freundlicher Mann“ (K1 wörtlich) und sein eigenes
  Zitat. Das hält die Serienregel „Empathie statt Kampf“ auch im Verkaufstext.
- **Der Brief bleibt zu.** Sein Inhalt (23.20 Uhr, das Feuer war vor ihm da) ist der Twist des Bandes.
- **Ehrlich zum Einstieg:** S2-1 bis S2-4 versprechen „für sich lesbar“. Für das Finale wäre das
  übertrieben — Ilse, Marie, die Werkstatt setzen Vorwissen voraus. Deshalb „am stärksten mit den
  Bänden 1 bis 4“, plus der wahre Satz, dass das Wichtigste erzählt wird (K3 Weißenbrück, K5 Zeitungen).
- **Kein Superlativ:** kein „gruseligster“ oder „dunkelster Band“ — ab K10 gibt es keinen Grusel mehr.
- **„Theo hat für jeden Notfall ein Codewort“ verworfen:** Es gibt eines. Stattdessen das echte.

### Belegliste Buchbeschreibung (02.11.)

| Aussage | Beleg |
|---|---|
| Rolltore, Morgengrauen, nach Nummern | K1 (siehe Abschnitt 6) |
| „Und die Reihe kommt näher.“ | K1: „Und die Reihe kam auf sie zu.“ (Umformung, nicht als Zitat gesetzt) |
| Nora (13), Theo (11) | Kontinuität S2-5 „Nora, 13“ / „Theo, 11“; identisch zu S2-1–S2-4 |
| Wächter, grau, durchscheinend, Runde | K2 / K4 (siehe Abschnitt 6) |
| schreit sie an | K2, Nora: „Er schreit uns an, Theo.“; K3, Halder: „Er schreit jede Nacht.“ |
| „Hier hat keiner was verloren!“ | K2, Wächter — wörtlich |
| knurrt ihn nicht an, winselt | K2: „Schatten winselte. Ein hoher, dünner Laut.“ Später knurrt er — das **Häuschen**, nicht den Mann: „Nicht den Mann“, sagte Nora. |
| Halder am Bauzaun | K3: „Halder stand am Bauzaun“ |
| freundlicher Mann, dreißig Jahre, Schlösser | K1 / K3 (siehe Abschnitt 6) |
| schon eine Falle gebaut | K4, Nora: „Eine Falle.“; K5: „Dein Vater hat ihm ein Schloss in die Türschwelle gebaut.“; K3: „Sie waren heute Nacht schon hier“ |
| „Älter als die anderen. Wütender. So einer wie damals.“ | K3, Halder — wörtlich |
| am Abend klingelt Frieda | K5: „Als es abends klingelte“ |
| Zeitungsausschnitte über ein Feuer, dreißig Jahre aufgehoben | K5: „Großbrand in der Weißenbrücker Altstadt“ / „Die hat er alle aufgehoben … Dreißig Jahre lang.“ |
| grauer Umschlag, Feuerwehr, nie geöffnet | K5: „grau geworden“, „Freiwillige Feuerwehr Weißenbrück“, „zugeklebt“; K6: „Warum hat er ihn nie aufgemacht?“ |
| „Diesen lasse ich nicht los. Nicht noch einmal.“ | K3, Halder — wörtlich |
| eine Frage, die er keinem gestellt hat | K3: „Haben Sie ihn gefragt?“ / „Ilse haben Sie auch nicht gefragt“; K13, Frieda: „Du hast nie einen gefragt“ (Thema, kein Ereignis verraten) |
| Nora dreht nicht um / sieht hin | K2 / K1 (siehe Abschnitt 6) |
| Finale der Reihe | Band 5 von 5 |
| die Wahrheit über das Feuer von Weißenbrück | K6 Brief, K12 Halders Wende — verrät nur, **dass** es eine gibt |
| 18 Kapitel, fast jedes mit Cliffhanger | 17 von 18 (K18 endet bewusst ohne; Cliffhanger-Register) |
| Codewort „Kuchen“, Rückzug | K1: „Codewort ist wieder Kuchen … Wenn einer Kuchen sagt, drehen wir um.“ |
| Schatten alt, spürt es zuerst | K1: „Er ist alt.“; nachts am Fenster („Er macht das seit einer Stunde“), bevor die Kinder etwas merken |
| Zimmerpflanzen-Dialog, beim Frühstück | K1, Nora und Theo — beide Zeilen wörtlich, direkt aufeinander folgend; Szene am Frühstückstisch („den Mund voller Rührei“) |

Beim Gegenlesen gefunden und ersetzt: Die erste Fassung schrieb „um sieben Uhr morgens“ hinter den
Dialog — die Uhrzeit steht nicht im Buch. Jetzt „beim Frühstück“ (belegt).

---

## 4. Backend-Keywords (7 Felder à 50 Zeichen)

1. `Geistergeschichte Kinder ab 12 Jahren Spukhaus` (46)
2. `Gänsehaut Bücher gruselig lustig Kinderbuch` (43)
3. `Gruselgeschichte ab 12 spannend Geist Hund` (42)
4. `Buch Mädchen Junge 12 13 Jahre Lesemuffel` (41)
5. `keine Albträume Serie Reihe Cliffhanger Kribbeln` (48)
6. `Halloween Geschenk Gespenst schaurig Geheimnis` (46)
7. `Geisterhaus Spuk gruselige Geschichten Kinder` (45)

Identisch zu S2-1 bis S2-4 (gleiche Zielgruppe, gleiche Suchwörter). Bewusst nicht: „Halder“,
„Wächter“, „Schlüssel“ — Titel und Beschreibung decken das ab.

---

## 5. Amazon-Kategorien (KDP)

1. Kinderbücher > Horror & Gruselgeschichten
2. Kinderbücher > Abenteuergeschichten > ab 12 Jahre
3. Kinderbücher > Fantasy & übernatürliche Geschichten

Identisch zu S2-1 bis S2-4.

---

## 6. Rückseitentext (gedrucktes Buch)

### Regeln, nach denen er gebaut ist (Qualitäts-Prüfplan Teil B)

- **Nur Ereignisse aus K1–K5.** Inhalt des Briefs, Konrads Ablösung, die Reiseuhr, das Ende: nichts.
- **Als Finale kenntlich**, ohne das Wort „Staffel“ (Regel seit S2-1).
- **Kein Superlativ**, den das Buch nicht hält („gruseligster Band“ o. ä.) — S2-5 hat ab K10 keinen
  Grusel mehr (vom Autor bewusst so entschieden).

### Pull-Quote

> „Diesen lasse ich nicht los. Nicht noch einmal.“

### Klappentext

> Hinter einem alten Gleis, bei den leeren Lagerhallen, rasseln im Morgengrauen die Rolltore.
> Eins nach dem anderen, genau nach den Nummern. Ein Wächter macht seine Runde – grau,
> durchscheinend und wütend.
>
> Nora und Theo wissen, wer ihn dort festhalten will: Herr Halder, der freundliche Mann, der seit
> dreißig Jahren Geister in Schlösser sperrt. Denn dieser Geist erinnert ihn an einen anderen. An
> die Nacht, in der in Weißenbrück sechs Häuser brannten.
>
> Am Abend steht Frieda vor der Tür, Halders Tochter. Sie hat eine abgeschlossene Schublade ihres
> Vaters geöffnet. Darin: ein grauer Umschlag von der Feuerwehr. Dreißig Jahre alt – und noch
> immer zugeklebt.
>
> *„Wir möchten uns ordnungsgemäß anmelden.“ – Theo, zu einem Geist*
>
> Diesmal dreht Nora nicht um. Diesmal sieht sie hin. Das Finale der Gebundenen.

### Alterszeile

> Grusel-Abenteuer für mutige Leser ab 12 Jahren — Kribbeln ja, Albträume nein.

### Reihenzeile

> Band 5 und Finale der Gebundenen. Band 1 bis 4 sind bereits erschienen.

### Belegliste (02.11.)

| Aussage | Beleg |
|---|---|
| „Diesen lasse ich nicht los. Nicht noch einmal.“ | K3, letzte Zeile, Halder — wörtlich (im Buch durch „sagte er“ getrennt, eine Rede) |
| hinter einem alten Gleis | K1: „Die Lagerhallen lagen hinter einem alten Gleis.“ |
| leere Lagerhallen | K1 „Firma, die es nicht mehr gab“; K2 „zu den leeren Hallen“ |
| Morgengrauen | K1: Aufbruch halb sechs, „Himmel grau“, „im ersten Licht“ |
| Rolltore rasseln nach den Nummern | K1: „Ein Tor nach dem anderen, genau nach den Nummern.“ |
| Wächter, Runde | K4 „der Wächter“; K2 „Um halb sieben ist Rundgang“ |
| grau, durchscheinend | K2: „Grau und durchscheinend, wie Nebel vor einer Laterne.“ |
| wütend | K3, Halder: „Er ist wütend.“ |
| festhalten will | K3: „Diesen lasse ich nicht los.“ |
| freundlicher Mann, Geister in Schlösser | K1: „Ein freundlicher Mann mit einer Werkzeugtasche, der Geister in Schlösser sperrte.“ |
| seit dreißig Jahren | K3, Halder: „Ich mache das seit dreißig Jahren.“ |
| erinnert ihn an einen anderen | K3: „So einer wie damals.“ / „Wie bei dem Feuer?“ — keine Antwort |
| Weißenbrück, sechs Häuser, in der Nacht | K3 „Ein Feuer in derselben Nacht“; K5 Zeitung: „Feuer zerstört sechs Häuser.“ |
| am Abend, Frieda vor der Tür | K5: „Als es abends klingelte“ — Frieda |
| abgeschlossene Schublade geöffnet | K5: „In der untersten Schublade am Werktisch. Die war immer abgeschlossen.“ / „Er hat mir beigebracht, wie man Schlösser aufmacht“ |
| Darin: Umschlag | K5: „Er lag ganz unten. Unter allen Zeitungen.“ (die Zeitungen lagen in der Schublade) |
| grau, Feuerwehr | K5: „Er war grau geworden“ / „Freiwillige Feuerwehr Weißenbrück.“ |
| dreißig Jahre alt | K7: „Genau da, wo er dreißig Jahre gelegen hatte.“ |
| zugeklebt | K5: „die Lasche noch zugeklebt“ |
| „Wir möchten uns ordnungsgemäß anmelden.“ | K2, Theo zum Wächter — wörtlich, ein Satz aus seiner Rede |
| Nora dreht nicht um, sieht hin | K2: „Ich dreh nicht schon wieder um, bevor ich weiß, was in diesem Haus ist.“ K1: „Dann sehen wir hin.“ |
| Band 1 bis 4 erschienen | Autor 02.11.: S2-1 bis S2-4 live |

**Bewusst nicht im Text:** der Inhalt des Briefs (23.20 Uhr — der Twist), Konrads Name, die
Ablösung, Halders Reiseuhr, der Schluss. „Der letzte Fall“ verworfen: Der Plan hält einen
Staffel-3-Faden offen; „Finale der Gebundenen“ stimmt in jedem Fall. „Uhrmacher“ verworfen: steht
in S2-5 nicht, nur auf dem Wagen in S2-3 — „freundlicher Mann“ ist wörtlich K1.
