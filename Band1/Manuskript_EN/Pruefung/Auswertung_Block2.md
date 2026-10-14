# Auswertung Block 2 (Kapitel 5–8) — 2026-10-14

## Ergebnis

| Kap. | Runden | US-Lektor „übersetzt?" (letzte Runde) | TRANSLATED | Bedeutung FEHLER | Skript | Status |
|---|---|---|---|---|---|---|
| 5 | 2 | **nein**, knapp (R1: ja) | 11 → 5 | 0 (Gegenprobe R2 20/20 OK) | 0 | ✅ fertig |
| 6 | 3 | **ja, leicht** (R1 ja · R2 ja, leicht · R3 ja, leicht) | 6 → 5 → 8 | 0 (Gegenprobe R3: 1 SCHWÄCHE *empty* → *found no one in her apartment*) | 0 | ✅ fertig **mit Meldung** (s. u.) |
| 7 | 2 | **nein** (R1: leicht ja) | 3 → 3 | 0 | 0 | ✅ fertig |
| 8 | 2 (+1 Zeile R3) | **nein** (R1: leicht ja) | 4 → 2 | 0 (R2-SCHWÄCHE *vor Anspannung* → R3 behoben) | 0 | ✅ fertig |

Kinderleser (K1–K8 am Stück, Bericht nur K5–K8): würde weiterlesen; Grusel 7 · 5 · 5 · 7 von 10; K5 „bestes Kapitel bisher", K8 „stärkster Cliffhanger"; K6/K7 hängen etwas durch (Rückblicke, wenig Humor in K7 — beides wie im Deutschen).
Umfang: 5.936 Wörter Deutsch → 6.365 Englisch (+7 %). Absätze 1:1, keine Ein-Satz-Absätze verloren, Ausrufezeichen gleich, Dialoganteil ± 0,5 Punkte.
Einheitlichkeit (`pruefe_en.py konsistenz`): keine neue Abweichung durch K5–K8; eine gewollte (K5 *Not a growl. Not a whine.* ↔ K8 *No growling.*, in den Notizen begründet).

## Kapitel 6 — Meldung nach der Fertig-Regel (Pilot 5.2)

Nach drei Runden sagt der US-Lektor weiter „ja, leicht"; TRANSLATED stieg von 5 auf 8. **Bewertung:**
- **Die Runde-3-Änderungen werden selbst wieder angestrichen** (*Here, there was order.*, *Her heartbeat slowly went back to normal.*) — jeder frische Lektor findet neue Stellen. Das ist das Polieren im Kreis, vor dem der Pilot gewarnt hat; Zahl und Urteil schwanken mit dem Prüfer, nicht mit dem Text.
- Ein Großteil der übrigen Anstriche ist **Bau des deutschen Kapitels**: Rechercheszene mit Erklärsätzen, Zeitungstexte, Rückblicke, Noras Doppelabsatz, *„Wir brauchen 1974"* (bewusst so seit Korrektur A7), Netflix-Witz — fürs Englische gesperrt (keine Inhaltsänderung).
- Echte Verbesserungen aus R3 wurden übernommen: US-Zeitungsstil (*Margret Silber, 75,* statt *(75)* — auch vorlesbar), *of her own free will* statt zweimal *voluntarily*, Lehnübersetzungen.
Daher: **fertig**. Eine vierte Runde würde nach aller Erfahrung (Pilot, K2) ins Leere polieren.

## Was Block 2 am Verfahren und am Buch verändert hat

| Änderung | Auslöser |
|---|---|
| **Deutsches Buch korrigiert:** K6 Theo *„Was meinst du?"* (Folgefehler meiner Korrektur A6), K5 *Bücherstapel* statt *Bücherregal* — Commit d2badb5, eBook neu gebaut | drei bzw. zwei Prüfer unabhängig; Autor |
| K8-Wortspiel *Shadows leaped … / Shadow whined.* erlaubt (zweite Ausnahme neben K12), Skript angepasst | A7 + D4; D6: *dark shapes* klang nach Wesen; Autor |
| Skript ohne Fehlalarme: A1-Straßennamen (*Mühlenweg*), Kartenformat *Name – Jahr*, englisches *handy* | Übersetzer musste sonst gutes Englisch verschlechtern (*useful*) |
| A7/A3: veraltete Zitate (*vierzig Jahre lang –*, *seit drei Monaten*, *I'd like that on the record*) | Übersetzer |
| Wortliste: +37 Einträge aus K5–K8 | Pflege nach Block |

## Kritisch

- **Die Wortliste hat gewirkt:** K5 greift K2 wortgleich auf (Kratzer, kaltes Zimmer, Klingelschild), keine neuen Abweichungen. Ohne sie hätte der Übersetzer die veralteten Notizen gelesen.
- **Die unabhängige Gegenprobe bleibt nötig:** Sie fand zweimal eine Bedeutungsverschiebung, die der Übersetzer bei seiner eigenen Prüfung übersehen hatte (*stiff* ohne *vor Anspannung*, *empty* für *verlassen*).
- **Der Kinderleser zu K1–K8 am Stück** war besser als nur K5–K8: Er bemerkte Brüche über Kapitelgrenzen (*ghost dog*, Rückblicke). Für Block 3/4 beibehalten.
- **Deutsche Logik-Kleinigkeiten**, die Prüfer meldeten und die bewusst unverändert blieben: Mama geht nachmittags schlafen (K7), Werkzeug-Gespräch (K8), *seit gestern* (K7), schwarzweißes Foto von 2019 (K5), *„Aus dem Flur. Hinter ihnen."* (K5), Tagebuch-Datum 12. März ↔ Silber vermisst seit 14. März (K8, vermutlich gewollt). Sammlung in den Notizen K5–K8 (Abschnitt „Fehler im Original"). **Nur auf Wunsch** in die Fundliste — einzeln jeweils klein.
- **Alle Urteile sind KI-Urteile.** Echte US-Leser stehen weiter aus (E2-Anschreiben).

## Nächste Schritte

1. Block 3 (K9–K12): K9 aus dem Pilot auf den neuen Stand bringen (4 deutsche Änderungen, Regeln seit Block 1), dann K10–K12. K12 enthält das zweite *shadow*-Wortspiel.
2. Kinderleser wieder ab K1 am Stück.
