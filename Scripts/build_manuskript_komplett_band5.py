"""
Baut das Gesamtmanuskript fuer Band 5 mit literarischer Frontmatter
(Widmung + Epigraph aus Frau Silbers Notizbuch) und sauberem Abschluss.

Abgeleitet von build_manuskript_komplett_band4.py.
Das Frontmatter-Ritual (Widmung + Epigraph) besteht seit Band 3 und
hebt das Buch ueber ein reines Zusammenkleben der Kapitel.

Band 5 ist das FINALE der Staffel 1. Der Abschluss-Marker ist deshalb
anders als bei Band 1-4: nicht nur "ENDE BAND 5", sondern das Ende der
Staffel. Der Staffel-2-Faden (Leuchtturm) bleibt in K18 stehen und wird
hier bewusst NICHT kommentiert - er soll wirken, nicht erklaert werden.

Verwendung:
    python Scripts/build_manuskript_komplett_band5.py

Pruefungen (brechen den Build ab, statt still Falsches zu bauen):
  - genau ERWARTETE_KAPITEL Dateien vorhanden, luckenlos ab 1
  - keine doppelten Kapiteltitel
  - jede Datei beginnt mit einem "# Kapitel N"-Kopf
  - KEIN "---" direkt vor einer Kapitelueberschrift  (siehe SEPARATOR-BUG)


★ SEPARATOR-BUG (gefunden 2026-07-17) — der Grund, warum dieses Skript
  anders baut als build_manuskript_komplett_band1..4.py:

  Die Downstream-Parser (build_taschenbuch_docx_band*.py UND build_ebook_docx.py)
  machen aus JEDER "---"-Zeile einen Szenentrenner:

      if line == '---':
          add_scene_break(doc)        # -> Leerzeile, zentriert "✦  ✦  ✦", Leerzeile

  Die Band-1..4-Skripte setzen aber ZUSAETZLICH ein "---" ZWISCHEN die Kapitel.
  Fuer den Parser ist das nicht von einem Szenentrenner unterscheidbar. Folge im
  gedruckten Buch:

      <letzter Satz des Kapitels = der Cliffhanger>
      ✦  ✦  ✦                 <- Fehl-Ornament
      <Seitenumbruch>
      Kapitel N+1

  Der Cliffhanger ist damit NICHT das Letzte auf der Seite — ein Ornament ist es.
  Das trifft genau das, worauf das ganze Buch gebaut ist (jedes Kapitel endet auf
  einem Cliffhanger). Real gemessen: Band 4 ist mit 15 solchen Fehl-Ornamenten
  in den Druck gegangen; Band 5 haette 17 gehabt.

  Fix hier an der Wurzel: "---" ist ueberladen (Szenentrenner UND Kapiteltrenner).
  Der Kapiteltrenner ist redundant — "# Kapitel N" markiert die Grenze bereits
  eindeutig, und KEIN Skript splittet auf "---" (geprueft). Also faellt er weg.
  Die Pruefung `pruefe_output()` haelt das dauerhaft fest.

  ⚠️ TODO Produktion: build_taschenbuch_docx_band5.py / eBook zusaetzlich defensiv
     machen — ein Szenentrenner direkt vor einer Kapitelueberschrift gehoert
     uebersprungen, egal was im Manuskript steht. Und: die ENDE-Strip-Regex aus
     Band 4 passt NICHT auf Band 5 (zusaetzliche Zeile "ENDE DER ERSTEN STAFFEL").
     Benoetigt:  re.sub(r'\\n\\n\\*\\*ENDE BAND 5\\*\\*\\n\\n\\*\\*ENDE DER ERSTEN STAFFEL\\*\\*\\n\\n---\\n*', '', body)
     Sonst landet "ENDE DER ERSTEN STAFFEL" als Fliesstext im Buch.
"""

import os
import re
import sys
from datetime import datetime

# ── Konfiguration ─────────────────────────────────────────────────────────────

BAND = 5
BAND_TITLE = "Der Schleier"
AUTHOR = "Benjamin Krug"
SERIES = "Die Geisterspürer"
ERWARTETE_KAPITEL = 18
IST_STAFFELFINALE = True

# ── Literarische Frontmatter ──────────────────────────────────────────────────
# ✅ VOM AUTOR FREIGEGEBEN 2026-07-17 (Benjamin Krug).
#
# Widmung: Thema "sich umdrehen / hinsehen" = das Herz von Band 5.
#   Bewusst NICHT das Band-4-Thema (gehen lassen / erinnern) wiederholen.
#   Kein Twist-Spoiler: sagt nicht, WER sich nicht umdreht.
#
#   ★ Zeile 1 ueberarbeitet 2026-07-17. Vorher: "Für alle, die sich nicht
#   umzudrehen trauen." Problem: eine Widmung wird VOR dem Buch gelesen, und
#   "sich nicht umdrehen" ist vorher eine leere Metapher — sie traegt erst
#   NACHHER. B3 ("denen einmal jemand richtig zugehört hat") und B4 ("die einmal
#   jemanden gehen lassen mussten") benennen dagegen eine Lebenserfahrung, die
#   man sofort erkennt, und werden beim Wiederlesen NOCH besser. Beides zu
#   koennen ist der Standard der Serie.
#   Jetzt: Zeile 1 = Gravens Diagnose in Klartext ("Sie haben Angst, dass Sie es
#   verpasst haben", K15) — sofort verstaendlich, universell. Zeile 2 haelt das
#   Bild des Buches und zahlt beim Wiederlesen aus.
WIDMUNG_ZEILEN = [
    "Für alle, die Angst haben, sie hätten etwas verpasst.",
    "Und für die, die sich trotzdem umdrehen.",
]

# Epigraph: Thema "Gewissheit" = Gravens Kern (Überzeugung/Hybris/Verleugnung).
#   Steigert das Serien-Motiv sauber:
#     B3 = die Erlaubnis aufzuhören · B4 = die Liebe, die nicht hergibt
#     B5 = die Gewissheit, die nicht hinsieht
#   Kein Twist-Spoiler: benennt keine Figur und kein Ereignis.
EPIGRAPH_ZEILEN = [
    "Der gefährlichste Geist ist nicht der, der etwas Böses will.",
    "Es ist der, der sich ganz sicher ist.",
]
EPIGRAPH_SOURCE = "aus dem Notizbuch von Margret Silber"

# ── Pfade ─────────────────────────────────────────────────────────────────────

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MANUSKRIPT_DIR = os.path.join(ROOT, f"Band{BAND}", "Manuskript")
OUTPUT_PATH = os.path.join(MANUSKRIPT_DIR, f"Manuskript_Band{BAND}_Komplett.md")

KAPITEL_RE = re.compile(r"Kapitel_(\d+)\.md$")
KOPF_RE = re.compile(r"^#\s+Kapitel\s+(\d+)\s*[–-]\s*(.+)$")


def get_kapitel_files() -> list:
    files = []
    for fname in os.listdir(MANUSKRIPT_DIR):
        if KAPITEL_RE.match(fname):
            files.append(os.path.join(MANUSKRIPT_DIR, fname))
    files.sort(key=lambda p: int(KAPITEL_RE.search(p).group(1)))
    return files


def pruefe(files: list) -> list:
    """Gibt Fehlerliste zurueck. Leer = alles gut."""
    fehler = []

    nummern = [int(KAPITEL_RE.search(p).group(1)) for p in files]
    if len(files) != ERWARTETE_KAPITEL:
        fehler.append(
            f"{len(files)} Kapiteldateien gefunden, erwartet {ERWARTETE_KAPITEL}."
        )
    erwartet = list(range(1, len(files) + 1))
    if nummern != erwartet:
        fehlend = sorted(set(erwartet) - set(nummern))
        fehler.append(f"Kapitelnummern nicht lueckenlos. Fehlt/verschoben: {fehlend}")

    titel = {}
    for p in files:
        with open(p, "r", encoding="utf-8") as f:
            erste = f.readline().strip()
        m = KOPF_RE.match(erste)
        if not m:
            fehler.append(f"{os.path.basename(p)}: kein '# Kapitel N – Titel'-Kopf "
                          f"(gefunden: {erste!r})")
            continue
        nr_kopf, tit = int(m.group(1)), m.group(2).strip()
        nr_datei = int(KAPITEL_RE.search(p).group(1))
        if nr_kopf != nr_datei:
            fehler.append(
                f"{os.path.basename(p)}: Kopf sagt Kapitel {nr_kopf}, Datei sagt {nr_datei}."
            )
        if tit in titel:
            fehler.append(f"Doppelter Kapiteltitel {tit!r}: {titel[tit]} und "
                          f"{os.path.basename(p)}")
        titel[tit] = os.path.basename(p)

    return fehler


def pruefe_output(text: str) -> list:
    """Simuliert den Downstream-Parser auf dem fertigen Text.
    Faengt Fehler, die im Markdown unsichtbar sind und erst im PDF auffallen."""
    fehler = []

    m = re.search(r"^# Kapitel 1", text, re.MULTILINE)
    if not m:
        return ["'# Kapitel 1' nicht gefunden — Downstream-Parser wuerde abbrechen."]
    body = text[m.start():]

    # Ereignisfolge exakt wie build_taschenbuch_docx_band4.parse_and_build
    ereignisse = []
    for zeile in body.split("\n"):
        z = zeile.strip()
        if not z:
            continue
        if z.startswith("# Kapitel "):
            ereignisse.append(("KAPITEL", z))
        elif z == "---":
            ereignisse.append(("ORNAMENT", z))
        else:
            ereignisse.append(("TEXT", z))

    # ★ Der SEPARATOR-BUG: Ornament direkt vor einer Kapitelueberschrift
    for i in range(len(ereignisse) - 1):
        if ereignisse[i][0] == "ORNAMENT" and ereignisse[i + 1][0] == "KAPITEL":
            fehler.append(
                f"SEPARATOR-BUG: Fehl-Ornament direkt vor {ereignisse[i+1][1]!r} — "
                f"im Druck steht ein '✦ ✦ ✦' hinter dem Cliffhanger."
            )

    # Zwei Ornamente hintereinander = leerer Szenenblock
    for i in range(len(ereignisse) - 1):
        if ereignisse[i][0] == "ORNAMENT" and ereignisse[i + 1][0] == "ORNAMENT":
            fehler.append("Zwei '---' hintereinander — leerer Szenenblock.")

    # Kapitel darf nicht mit einem Ornament beginnen
    for i in range(len(ereignisse) - 1):
        if ereignisse[i][0] == "KAPITEL" and ereignisse[i + 1][0] == "ORNAMENT":
            fehler.append(f"Ornament direkt NACH {ereignisse[i][1]!r}.")

    return fehler


def zaehle_woerter(text: str) -> int:
    """Echte Fliesstext-Woerter. len(text.split()) zaehlt '---', '>' und
    '**ENDE BAND 5**' als Woerter und meldet ~2 % zu viel — diese Zahl wandert
    aber in KDP-Metadaten und Planung, also muss sie stimmen."""
    clean = re.sub(r"^\s*(---|>.*|#.*|\*\*ENDE.*)$", "", text, flags=re.MULTILINE)
    return len(re.findall(r"[A-Za-zÄÖÜäöüßéèêëàâîôûçœ']+", clean))


def build(files: list) -> str:
    parts = []

    # ── Titelkopf ──────────────────────────────────────────────────────────
    parts.append(
        f"# {SERIES} – {BAND_TITLE}\n\n"
        f"**Band {BAND}**"
        + (" — Finale Staffel 1\n" if IST_STAFFELFINALE else "\n")
        + f"Autor: {AUTHOR}\n"
        f"Stand: {datetime.now().strftime('%Y-%m-%d')}\n"
    )

    # ── Widmung ────────────────────────────────────────────────────────────
    parts.append("\n---\n\n")
    parts.append("\n\n".join(f"*{z}*" for z in WIDMUNG_ZEILEN) + "\n")

    # ── Epigraph ───────────────────────────────────────────────────────────
    parts.append("\n---\n\n")
    epi = "\n>\n".join(f"> *{z}*" for z in EPIGRAPH_ZEILEN)
    parts.append(epi + f"\n>\n> — {EPIGRAPH_SOURCE}\n")

    # ── Kapitel ────────────────────────────────────────────────────────────
    # ⚠️ KEIN "---" zwischen den Kapiteln! Siehe SEPARATOR-BUG oben.
    # Die Ueberschrift "# Kapitel N" markiert die Grenze bereits eindeutig.
    for filepath in files:
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read().strip()
        parts.append("\n\n")
        parts.append(content)

    # ── Abschluss ──────────────────────────────────────────────────────────
    if IST_STAFFELFINALE:
        parts.append(f"\n\n---\n\n**ENDE BAND {BAND}**\n\n"
                     f"**ENDE DER ERSTEN STAFFEL**\n\n---\n")
    else:
        parts.append(f"\n\n---\n\n**ENDE BAND {BAND}**\n\n---\n")

    return "".join(parts)


def main():
    print(f"Erstelle Manuskript fuer Band {BAND}: {BAND_TITLE}")
    files = get_kapitel_files()
    print(f"Gefundene Kapitel: {len(files)}")

    fehler = pruefe(files)
    if fehler:
        print("\n!! BUILD ABGEBROCHEN — Manuskript nicht geschrieben:")
        for f in fehler:
            print(f"   - {f}")
        sys.exit(1)
    print("Pruefung: ok (Anzahl, Nummerierung, Koepfe, Titel-Eindeutigkeit)")

    text = build(files)

    # ── Output pruefen, BEVOR geschrieben wird ─────────────────────────────
    fehler = pruefe_output(text)
    chapter_count = len(re.findall(r"\n# Kapitel ", text))
    if chapter_count != ERWARTETE_KAPITEL:
        fehler.append(f"{chapter_count} Kapitelkoepfe im Output, "
                      f"erwartet {ERWARTETE_KAPITEL}.")
    for f_ in files:
        with open(f_, "r", encoding="utf-8") as fh:
            if fh.read().strip() not in text:
                fehler.append(f"{os.path.basename(f_)} nicht vollstaendig im Output.")
    if fehler:
        print("\n!! BUILD ABGEBROCHEN — Manuskript nicht geschrieben:")
        for e in dict.fromkeys(fehler):
            print(f"   - {e}")
        sys.exit(1)
    print("Output-Pruefung: ok (Struktur, keine Fehl-Ornamente, Kapitel vollstaendig)")

    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(text)

    print(f"\nGespeichert: {OUTPUT_PATH}")
    print(f"Kapitel:     {chapter_count}")
    print(f"Woerter:     {zaehle_woerter(text):,} (Fliesstext, ohne Markdown-Marker)")


if __name__ == "__main__":
    main()
