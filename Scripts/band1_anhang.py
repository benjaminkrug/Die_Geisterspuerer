"""
Gemeinsame Daten fuer den Anhang von Band 1 (Taschenbuch UND eBook).

Schritt 1 des Plans Band1/PLAN_Durchlesequote.md. Vorher stand der Inhalt doppelt in
build_taschenbuch_docx.py und build_ebook_docx.py und lief auseinander: Das Taschenbuch
hatte die echte Leseprobe, das eBook eine erfundene (mit "Heinrich M. - 1847",
"vor drei Wochen" und "Erscheint 2026").

★ Die Leseprobe wird NICHT abgetippt, sondern beim Bau aus
  Band2/Manuskript/Manuskript_Band2_Komplett.md gelesen (das ist die publizierte Wahrheit,
  NICHT die Kapitel-Dateien von Band 2, die sind veraltet, s. TODO_Nachbesserung).
  Jeder Absatz wird gegen die Quelle geprueft. Weicht etwas ab, bricht der Bau ab.

Aufruf zur Kontrolle:
    py Scripts/band1_anhang.py
"""
import os
import re
import sys

_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

BAND2_QUELLE = os.path.join(_ROOT, "Band2", "Manuskript", "Manuskript_Band2_Komplett.md")
BAND2_TITEL = "Der Friedhof ohne Namen"
BAND2_KAPITEL = "Kapitel 1 – Guten Morgen, Friedhof"

# ASINs der Taschenbuecher (wie Scripts/build_qr_rezension.py)
BAND1_ASIN = "B0GNZVXDDJ"
BAND2_ASIN = "B0GV8R8QJ6"

# --------------------------------------------------------------------------
# Wohin fuehren QR-Code und Link "weiter zu Band 2"?
# --------------------------------------------------------------------------
# ★ ENTSCHIEDEN 2026-10-17 (Autor): KEINE eigene Domain, der Code fuehrt direkt zu
#   Amazon. Nicht erneut vorschlagen. Die Scan-Zaehlung aus Plan Abschnitt 8 entfaellt.
# Solange es die eigene Domain nicht gibt (Plan, Abschnitt 8), fuehrt der Code
# direkt auf Amazon. Das funktioniert, aber die Scans lassen sich NICHT zaehlen.
# Sobald die Weiterleitung steht: hier eintragen, z. B.
#     WEITERLEITUNG_BAND2 = "https://geisterspuerer.de/band2"
# dann `py Scripts/build_qr_rezension.py --force` und beide Buecher neu bauen.
WEITERLEITUNG_BAND2 = None

BAND2_URL = WEITERLEITUNG_BAND2 or f"https://www.amazon.de/dp/{BAND2_ASIN}"
REZENSION_URL = f"https://www.amazon.de/review/create-review?asin={BAND1_ASIN}"

QR_BAND2 = os.path.join(_ROOT, "Band1", "Cover", "qr_weiter_band2.png")
QR_REZENSION = os.path.join(_ROOT, "Band1", "Cover", "qr_rezension_band1.png")
COVER_BAND2 = os.path.join(_ROOT, "Band1", "Cover", "band2_vorderseite_leseprobe.jpg")

# --------------------------------------------------------------------------
# Leseprobe: Anfang von Band 2, Kapitel 1, bis zum ersten Haken
# --------------------------------------------------------------------------
# Ende: Schatten bleibt vor dem Tor sitzen. Das ist auch der Haken des
# Band-2-Klappentexts ("Vier Pfoten auf dem Gehsteig").
# NICHT weiter bis "Er würde warten.": Danach sagt Theo "Er ist noch nie..." /
# Nora "War er nicht." In Band 1 hat sich Schatten aber schon geweigert (Kap. 2,
# kaltes Zimmer; Kap. 5 sagt es ausdruecklich). Direkt nach Band 1 gelesen faellt das auf.
LESEPROBE_ENDE = ("Schatten saß auf dem Gehsteig. Vier Pfoten fest auf dem Pflaster. "
                  "Er war keinen Millimeter durch das Tor getreten.")

# Bewusst AUSGELASSEN (Logikpruefung 2026-10-10): Der Satz sagt, dass man von der
# Strasse aus nur Baeume sieht. In Band 1, Kap. 15 sehen die Kinder aber von der
# anderen Strassenseite Grabsteine und eine Gestalt. Direkt hintereinander gelesen
# faellt der Widerspruch auf. Ohne den Absatz liest sich die Stelle glatt:
# "Das ist groß", sagte Theo. -> Nora schob das Tor auf.
LESEPROBE_AUSLASSEN = (
    "Er hatte recht. Von der Straße aus sah man nur die Bäume",
)

SZENENWECHSEL = "---"


def _typo_quotes(absatz):
    """Band 2 ist reines ASCII. Paarweise: erstes " -> „, zweites -> “.
    Darf NUR auf Band-2-Text laufen (Band 1 ist schon typografisch, s. Fehler 3)."""
    if "„" in absatz or "“" in absatz:
        raise ValueError(f"Absatz ist schon typografisch, Quelle geaendert? {absatz[:50]}")
    if absatz.count('"') % 2:
        raise ValueError(f"Ungerade Zahl von Anführungszeichen: {absatz[:60]}")
    teile = absatz.split('"')
    aus = teile[0]
    for i, teil in enumerate(teile[1:]):
        aus += ("„" if i % 2 == 0 else "“") + teil
    return aus


def _quellabsaetze():
    with open(BAND2_QUELLE, encoding="utf-8") as f:
        text = f.read()
    m = re.search(r"^# " + re.escape(BAND2_KAPITEL) + r"\s*$", text, re.MULTILINE)
    if not m:
        raise ValueError(f"'{BAND2_KAPITEL}' nicht in {BAND2_QUELLE} gefunden")
    rest = text[m.end():]
    ende = re.search(r"^# Kapitel ", rest, re.MULTILINE)
    kapitel = rest[: ende.start()] if ende else rest
    return [z.strip() for z in kapitel.split("\n") if z.strip()]


def leseprobe():
    """Liste der Absaetze; SZENENWECHSEL steht fuer einen Szenentrenner.
    Bricht ab, wenn die Quelle nicht mehr zur Erwartung passt."""
    absaetze = []
    ausgelassen = []
    for z in _quellabsaetze():
        if any(z.startswith(a) for a in LESEPROBE_AUSLASSEN):
            ausgelassen.append(z)
            continue
        absaetze.append(SZENENWECHSEL if z == "---" else _typo_quotes(z))
        if z == LESEPROBE_ENDE:
            break
    else:
        raise ValueError(f"Leseprobe-Ende '{LESEPROBE_ENDE}' nicht gefunden")
    if len(ausgelassen) != len(LESEPROBE_AUSLASSEN):
        raise ValueError(f"Auszulassende Absaetze nicht alle gefunden: {ausgelassen}")
    if absaetze[0] == SZENENWECHSEL or absaetze[-1] == SZENENWECHSEL:
        raise ValueError("Leseprobe beginnt oder endet mit einem Szenentrenner")
    return absaetze


def pruefe_leseprobe():
    """Kontrolle (a) des Plans: Jeder Absatz steht woertlich in Band 2
    (nach Rueckwandlung der Anfuehrungszeichen). Gibt (absaetze, woerter) zurueck."""
    with open(BAND2_QUELLE, encoding="utf-8") as f:
        quelle = set(z.strip() for z in f.read().split("\n"))
    absaetze = leseprobe()
    for a in absaetze:
        if a == SZENENWECHSEL:
            continue
        roh = a.replace("„", '"').replace("“", '"')
        if roh not in quelle:
            raise ValueError(f"Nicht woertlich in Band 2: {a[:70]}")
        if a.count("„") != a.count("“"):
            raise ValueError(f"Anführungszeichen unausgeglichen: {a[:70]}")
    woerter = sum(len(a.split()) for a in absaetze if a != SZENENWECHSEL)
    return absaetze, woerter


if __name__ == "__main__":
    try:
        absaetze, woerter = pruefe_leseprobe()
    except ValueError as e:
        print("FEHLER:", e)
        sys.exit(1)
    n = sum(1 for a in absaetze if a != SZENENWECHSEL)
    print(f"Leseprobe: {n} Absaetze, {woerter} Woerter, woertlich aus Band 2 ✓")
    print(f"Erster Absatz : {absaetze[0]}")
    print(f"Letzter Absatz: {absaetze[-1]}")
    print(f"Weiter-Link   : {BAND2_URL}")
    if not WEITERLEITUNG_BAND2:
        print("  !! Noch keine eigene Domain: Link geht direkt auf Amazon, Scans nicht zaehlbar.")
