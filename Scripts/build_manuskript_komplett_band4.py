"""
Baut das Gesamtmanuskript fuer Band 4 mit literarischer Frontmatter
(Widmung + Epigraph aus Frau Silbers Notizbuch) und sauberem Abschluss.

Abgeleitet von build_manuskript_komplett_band3.py.
Die Frontmatter-Elemente (Widmung, Epigraph) heben das Buch ueber ein
reines Zusammenkleben der Kapitel und schaffen ein Serien-Ritual.

Verwendung:
    python build_manuskript_komplett_band4.py
"""

import os
import re
from datetime import datetime

# ── Konfiguration ─────────────────────────────────────────────────────────────

BAND = 4
BAND_TITLE = "Die zugemauerte Tür"
AUTHOR = "Benjamin Krug"
SERIES = "Die Geisterspürer"

# ── Literarische Frontmatter (gewaehlt mit dem Autor, 2026-07-07) ──────────────

# Widmung – Thema Loslassen/Abschied (verbindet die Serie, kein Twist-Spoiler)
# Als Liste von Zeilen (jede Zeile wird eigenstaendig kursiv gesetzt).
WIDMUNG_ZEILEN = [
    "Für alle, die einmal jemanden gehen lassen mussten.",
    "Und für die, die gelernt haben, dass Erinnern nichts damit zu tun hat.",
]

# Epigraph – Thema Festhalten (trifft Fabers Wesen, kein Twist-Spoiler)
EPIGRAPH_ZEILEN = [
    "Die schwersten Geister sind nicht die zornigen.",
    "Es sind die, die etwas so sehr geliebt haben, dass sie es nicht mehr hergeben können.",
]
EPIGRAPH_SOURCE = "aus dem Notizbuch von Margret Silber"

# ── Pfade ─────────────────────────────────────────────────────────────────────

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MANUSKRIPT_DIR = os.path.join(ROOT, f"Band{BAND}", "Manuskript")
OUTPUT_PATH = os.path.join(MANUSKRIPT_DIR, f"Manuskript_Band{BAND}_Komplett.md")


def get_kapitel_files() -> list:
    files = []
    for fname in os.listdir(MANUSKRIPT_DIR):
        if re.match(r"Kapitel_\d+\.md$", fname):
            files.append(os.path.join(MANUSKRIPT_DIR, fname))
    files.sort(key=lambda p: int(re.search(r"Kapitel_(\d+)\.md$", p).group(1)))
    return files


def build() -> str:
    files = get_kapitel_files()
    print(f"Erstelle Manuskript fuer Band {BAND}: {BAND_TITLE}")
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
    parts.append("\n---\n\n")
    widmung_md = "\n\n".join(f"*{zeile}*" for zeile in WIDMUNG_ZEILEN)
    parts.append(widmung_md + "\n")

    # ── Epigraph ───────────────────────────────────────────────────────────
    parts.append("\n---\n\n")
    epi_lines = [f"> *{zeile}*" for zeile in EPIGRAPH_ZEILEN]
    epi_md = "\n>\n".join(epi_lines)
    parts.append(epi_md + f"\n>\n> — {EPIGRAPH_SOURCE}\n")

    # ── Kapitel ────────────────────────────────────────────────────────────
    for filepath in files:
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
    print(f"Woerter:     {word_count:,}")


if __name__ == "__main__":
    main()
