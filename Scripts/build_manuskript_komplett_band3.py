"""
Baut das Gesamtmanuskript fuer Band 3 mit literarischer Frontmatter
(Widmung + Epigraph aus Frau Silbers Notizbuch) und sauberem Abschluss.

Erweiterte Version von build_manuskript_komplett.py speziell fuer Band 3.
Die Frontmatter-Elemente (Widmung, Epigraph) heben das Buch ueber ein
reines Zusammenkleben der Kapitel und schaffen ein Serien-Ritual.

Verwendung:
    python build_manuskript_komplett_band3.py
"""

import os
import re
from datetime import datetime

# ── Konfiguration ─────────────────────────────────────────────────────────────

BAND = 3
BAND_TITLE = "Schatten sieht mehr"
AUTHOR = "Benjamin Krug"
SERIES = "Die Geisterspürer"

# ── Literarische Frontmatter (gewaehlt mit dem Autor, 2026-06-10) ──────────────

# Widmung – Variante 1 (Thema: Zuhoeren – verbindet alle 5 Baende)
# Als Liste von Zeilen (jede Zeile wird eigenstaendig kursiv gesetzt).
WIDMUNG_ZEILEN = [
    "Für alle, denen einmal jemand richtig zugehört hat.",
    "Und für die, die noch darauf warten.",
]

# Epigraph – Variante A (Thema: Vergebung/Loslassen – kein Twist-Spoiler)
EPIGRAPH_ZEILEN = [
    "Nicht jeder Unruhige sucht die Wahrheit.",
    "Manche suchen nur die Erlaubnis, endlich aufzuhören.",
]
EPIGRAPH_SOURCE = "aus dem Notizbuch von Margret Silber"

# ── Pfade ─────────────────────────────────────────────────────────────────────

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MANUSKRIPT_DIR = os.path.join(ROOT, f"Band{BAND}", "Manuskript")
OUTPUT_PATH = os.path.join(MANUSKRIPT_DIR, f"Manuskript_Band{BAND}_Komplett.md")


def get_kapitel_files() -> list[str]:
    files = []
    for fname in os.listdir(MANUSKRIPT_DIR):
        if re.match(r"Kapitel_\d+\.md$", fname):
            files.append(os.path.join(MANUSKRIPT_DIR, fname))
    files.sort(key=lambda p: int(re.search(r"Kapitel_(\d+)\.md$", p).group(1)))
    return files


def build() -> str:
    files = get_kapitel_files()
    print(f"Erstelle Manuskript für Band {BAND}: {BAND_TITLE}")
    print(f"Gefundene Kapitel: {len(files)}")

    parts = []

    # ── Titelkopf ──────────────────────────────────────────────────────────
    parts.append(
        f"# {SERIES} – {BAND_TITLE}\n\n"
        f"**Band {BAND}**\n"
        f"Autor: {AUTHOR}\n"
        f"Stand: {datetime.now().strftime('%Y-%m-%d')}\n"
    )

    # ── Widmung ────────────────────────────────────────────────────────────
    # Jede Zeile als eigener kursiver Absatz (sauberes Markdown, kein Bruch).
    parts.append("\n---\n\n")
    widmung_md = "\n\n".join(f"*{zeile}*" for zeile in WIDMUNG_ZEILEN)
    parts.append(widmung_md + "\n")

    # ── Epigraph ───────────────────────────────────────────────────────────
    # Mehrzeiliges Blockquote, jede Zeile mit '> ' und kursiv, dann Quelle.
    parts.append("\n---\n\n")
    epi_lines = [f"> *{zeile}*" for zeile in EPIGRAPH_ZEILEN]
    epi_md = "\n>\n".join(epi_lines)          # Leerzeile zwischen den Zeilen, im Quote
    parts.append(epi_md + f"\n>\n> — {EPIGRAPH_SOURCE}\n")

    # ── Kapitel ────────────────────────────────────────────────────────────
    for i, filepath in enumerate(files):
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read().strip()
        parts.append("\n\n---\n\n")
        parts.append(content)

    # ── Abschluss ──────────────────────────────────────────────────────────
    parts.append(f"\n\n---\n\n**ENDE BAND {BAND}**\n\n---\n")

    return "".join(parts)


def main():
    text = build()
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(text)

    word_count = len(text.split())
    chapter_count = len(re.findall(r"\n# Kapitel ", text))
    print(f"\nGespeichert: {OUTPUT_PATH}")
    print(f"Kapitel:     {chapter_count}")
    print(f"Wörter:      {word_count:,}")


if __name__ == "__main__":
    main()
