"""
Baut das Gesamtmanuskript fuer Staffel 2, Band 1 ("Der Gast, der blieb").

Abgeleitet von build_manuskript_komplett_band5.py — bewusst NICHT neu erfunden.
Uebernommen werden alle Pruefungen, die dort aus echten Druckfehlern entstanden
sind (siehe SEPARATOR-BUG unten). Geaendert sind nur Pfade, Kapitelzahl und die
dreistufige Staffel-2-Kopfzeile.

Verwendung:
    python Scripts/build_manuskript_komplett_s2_1.py

Pruefungen (brechen den Build ab, statt still Falsches zu bauen):
  - genau ERWARTETE_KAPITEL Dateien vorhanden, luckenlos ab 1
  - keine doppelten Kapiteltitel
  - jede Datei beginnt mit einem "# Kapitel N - Titel"-Kopf
  - KEIN "---" direkt vor einer Kapitelueberschrift  (SEPARATOR-BUG)
  - jede Kapiteldatei liegt vollstaendig im Output


★ SEPARATOR-BUG (gefunden 2026-07-17 an Band 4/5) — gilt hier unveraendert:

  Die Downstream-Parser (build_taschenbuch_docx_band*.py UND build_ebook_docx.py)
  machen aus JEDER "---"-Zeile einen Szenentrenner. Die Band-1..4-Skripte setzten
  zusaetzlich ein "---" ZWISCHEN die Kapitel — fuer den Parser nicht von einem
  Szenentrenner unterscheidbar. Folge im gedruckten Buch:

      <Cliffhanger>
      ✦  ✦  ✦                 <- Fehl-Ornament
      <Seitenumbruch>
      Kapitel N+1

  Band 4 ist mit 15 solchen Fehl-Ornamenten in den Druck gegangen. Da JEDES
  Kapitel dieser Reihe auf einem Cliffhanger endet, trifft der Fehler genau das
  Konstruktionsprinzip des Buchs. Deshalb: kein "---" zwischen den Kapiteln.
  "# Kapitel N" markiert die Grenze bereits eindeutig.


⚠️ OFFEN — Frontmatter (Widmung + Epigraph)

  Seit Band 3 hat jeder Band eine Widmung und ein Epigraph, und beides ist in den
  Band-Skripten ausdruecklich als "VOM AUTOR FREIGEGEBEN" markiert. Fuer S2-1
  existiert bislang **kein freigegebener Text** — weder in PLAN_Staffel2.md noch
  in den S2-1-Dateien.

  Das Skript erfindet dafuer nichts. Solange die Listen leer sind, baut es das
  Manuskript OHNE Frontmatter und gibt eine deutliche Warnung aus. Sobald der
  Autor Texte freigegeben hat: hier eintragen und neu bauen — der Rest des Builds
  aendert sich nicht.


⚠️ TODO Produktion (uebernommen aus Band 5, gilt hier genauso)

  Ein spaeteres build_taschenbuch_docx_s2_1.py braucht:
  - defensives Ueberspringen eines Szenentrenners direkt vor einer
    Kapitelueberschrift, egal was im Manuskript steht
  - eine ENDE-Strip-Regex, die BEIDE Marker erwischt: das "**ENDE**" am Schluss
    von Kapitel 16 gehoert ins Buch, der Build-Marker darunter nicht:
        re.sub(r'\\n\\n---\\n\\n\\*\\*ENDE BAND 1 · DIE GEBUNDENEN\\*\\*\\n\\n---\\n*', '', body)
"""

import os
import re
import sys
from datetime import datetime

# ── Konfiguration ─────────────────────────────────────────────────────────────

BAND_LABEL = "S2-1"
BAND_NR = 1
BAND_TITLE = "Der Gast, der blieb"
AUTHOR = "Benjamin Krug"
SERIES = "Die Geisterspürer"
STAFFEL_TITLE = "Die Gebundenen"          # PLAN_Staffel2.md Abschnitt 10
ALTERSANGABE = "Ein Grusel-Abenteuer für Kinder ab 12 Jahren"
ERWARTETE_KAPITEL = 16

# ── Literarische Frontmatter ──────────────────────────────────────────────────
# ⚠️ LEER = NICHT FREIGEGEBEN. Siehe Kopfkommentar. Nicht selbst befuellen,
#    ohne dass der Autor den Text bestaetigt hat.
WIDMUNG_ZEILEN: list = []
EPIGRAPH_ZEILEN: list = []
EPIGRAPH_SOURCE = "aus dem Notizbuch von Margret Silber"

# ── Pfade ─────────────────────────────────────────────────────────────────────

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MANUSKRIPT_DIR = os.path.join(ROOT, "Staffel2", BAND_LABEL, "Manuskript")
OUTPUT_PATH = os.path.join(MANUSKRIPT_DIR, f"Manuskript_{BAND_LABEL}_Komplett.md")

ENDE_MARKER = f"**ENDE BAND {BAND_NR} · {STAFFEL_TITLE.upper()}**"

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


def pruefe_cliffhanger(files: list, text: str) -> list:
    """Jedes Kapitel dieser Reihe endet auf einem Cliffhanger. Diese Pruefung
    stellt sicher, dass der letzte Satz jedes Kapitels im Output UNMITTELBAR
    vor der naechsten Kapitelueberschrift steht — nichts darf sich dazwischen
    schieben."""
    fehler = []
    for i, p in enumerate(files[:-1]):
        with open(p, "r", encoding="utf-8") as f:
            letzte = [z.strip() for z in f.read().strip().split("\n") if z.strip()][-1]
        naechste_nr = int(KAPITEL_RE.search(files[i + 1]).group(1))
        muster = re.escape(letzte) + r"\s*\n\s*\n# Kapitel " + str(naechste_nr)
        if not re.search(muster, text):
            fehler.append(
                f"Kapitel {i+1}: Schlusszeile {letzte[:40]!r} steht nicht direkt "
                f"vor '# Kapitel {naechste_nr}'."
            )
    return fehler


def zaehle_woerter(text: str) -> int:
    """Echte Fliesstext-Woerter. len(text.split()) zaehlt '---', '>' und
    '**ENDE ...**' als Woerter und meldet ~2 % zu viel — diese Zahl wandert
    aber in KDP-Metadaten und Planung, also muss sie stimmen."""
    clean = re.sub(r"^\s*(---|>.*|#.*|\*\*ENDE.*)$", "", text, flags=re.MULTILINE)
    return len(re.findall(r"[A-Za-zÄÖÜäöüßéèêëàâîôûçœ']+", clean))


def build(files: list) -> str:
    parts = []

    # ── Titelkopf (dreistufige Staffel-2-Kopfzeile, PLAN Abschnitt 10) ──────
    parts.append(
        f"# {SERIES} – {BAND_TITLE}\n\n"
        f"**{STAFFEL_TITLE} · Band {BAND_NR}**\n"
        f"{ALTERSANGABE}\n"
        f"Autor: {AUTHOR}\n"
        f"Stand: {datetime.now().strftime('%Y-%m-%d')}\n"
    )

    # ── Widmung ────────────────────────────────────────────────────────────
    if WIDMUNG_ZEILEN:
        parts.append("\n---\n\n")
        parts.append("\n\n".join(f"*{z}*" for z in WIDMUNG_ZEILEN) + "\n")

    # ── Epigraph ───────────────────────────────────────────────────────────
    if EPIGRAPH_ZEILEN:
        parts.append("\n---\n\n")
        epi = "\n>\n".join(f"> *{z}*" for z in EPIGRAPH_ZEILEN)
        parts.append(epi + f"\n>\n> — {EPIGRAPH_SOURCE}\n")

    # ── Kapitel ────────────────────────────────────────────────────────────
    # ⚠️ KEIN "---" zwischen den Kapiteln! Siehe SEPARATOR-BUG oben.
    for filepath in files:
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read().strip()
        parts.append("\n\n")
        parts.append(content)

    # ── Abschluss ──────────────────────────────────────────────────────────
    # Kapitel 16 traegt bereits ein "**ENDE**" (Ende der Geschichte).
    # Der Marker hier ist der Buch-Marker — genau wie bei Band 1-5.
    parts.append(f"\n\n---\n\n{ENDE_MARKER}\n\n---\n")

    return "".join(parts)


def main():
    print(f"Erstelle Manuskript fuer {BAND_LABEL}: {BAND_TITLE}")
    print(f"  {SERIES} · {STAFFEL_TITLE} · Band {BAND_NR}")
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
    fehler += pruefe_cliffhanger(files, text)
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
    print("Output-Pruefung: ok (Struktur, keine Fehl-Ornamente, "
          "Cliffhanger unmittelbar vor Kapitelgrenze, Kapitel vollstaendig)")

    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(text)

    print(f"\nGespeichert: {OUTPUT_PATH}")
    print(f"Kapitel:     {chapter_count}")
    print(f"Woerter:     {zaehle_woerter(text):,} (Fliesstext, ohne Markdown-Marker)")

    if not WIDMUNG_ZEILEN or not EPIGRAPH_ZEILEN:
        fehlt = []
        if not WIDMUNG_ZEILEN:
            fehlt.append("Widmung")
        if not EPIGRAPH_ZEILEN:
            fehlt.append("Epigraph")
        print(f"\n⚠️  OHNE FRONTMATTER GEBAUT — es fehlt: {', '.join(fehlt)}.")
        print("    Band 3, 4 und 5 haben beides. Der Text muss vom Autor")
        print("    freigegeben werden; das Skript erfindet ihn nicht.")
        print("    Nach Freigabe oben eintragen und neu bauen.")


if __name__ == "__main__":
    main()
