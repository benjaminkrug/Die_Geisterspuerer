"""
Kombiniert alle Kapitel eines Bandes zu einer einzigen Manuskript-Datei.
Verwendung:
    python build_manuskript_komplett.py          # erstellt Band2/Manuskript/Manuskript_Band2_Komplett.md
    python build_manuskript_komplett.py 1        # erstellt Band1/Manuskript/Manuskript_Band1_Komplett.md
    python build_manuskript_komplett.py 2        # Band 2
"""

import os
import sys
import re
from datetime import datetime

# ── Konfiguration ─────────────────────────────────────────────────────────────

BAND_TITLES = {
    1: "Das Haus, das flüstert",
    2: "Der Friedhof ohne Namen",
    3: "Schatten sieht mehr",
    4: "Die zugemauerte Tür",
    5: "Der Schleier",
}

AUTHOR = "Benjamin Krug"
SERIES = "Die Geisterspürer"

# ── Pfade ─────────────────────────────────────────────────────────────────────

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def get_kapitel_files(band: int) -> list[str]:
    """Gibt alle Kapitel-Dateien eines Bandes sortiert zurück."""
    manuskript_dir = os.path.join(ROOT, f"Band{band}", "Manuskript")
    if not os.path.isdir(manuskript_dir):
        raise FileNotFoundError(f"Verzeichnis nicht gefunden: {manuskript_dir}")

    files = []
    for fname in os.listdir(manuskript_dir):
        if re.match(r"Kapitel_\d+\.md$", fname):
            files.append(os.path.join(manuskript_dir, fname))

    # Sortierung nach Kapitelnummer
    files.sort(key=lambda p: int(re.search(r"Kapitel_(\d+)\.md$", p).group(1)))
    return files


def build_komplett(band: int) -> str:
    """Liest alle Kapitel und gibt den kombinierten Text zurück."""
    files = get_kapitel_files(band)
    title = BAND_TITLES.get(band, f"Band {band}")

    print(f"Erstelle Manuskript für Band {band}: {title}")
    print(f"Gefundene Kapitel: {len(files)}")
    for f in files:
        print(f"  {os.path.basename(f)}")

    sections = []

    # ── Kopfzeile ──────────────────────────────────────────────────────────
    header = f"""# {SERIES} – {title}

**Band {band}**
Autor: {AUTHOR}
Stand: {datetime.now().strftime("%Y-%m-%d")}

---

"""
    sections.append(header)

    # ── Kapitel ────────────────────────────────────────────────────────────
    for i, filepath in enumerate(files):
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read().strip()

        # Trennlinie zwischen Kapiteln (nicht nach dem letzten)
        if i > 0:
            sections.append("\n\n---\n\n")

        sections.append(content)

    # ── Abschluss ──────────────────────────────────────────────────────────
    sections.append(f"\n\n---\n\n**ENDE BAND {band}**\n\n---\n")

    return "".join(sections)


def main():
    band = int(sys.argv[1]) if len(sys.argv) > 1 else 2

    if band not in BAND_TITLES and band not in range(1, 6):
        print(f"Fehler: Band {band} nicht bekannt. Erlaubt: 1–5")
        sys.exit(1)

    output_path = os.path.join(ROOT, f"Band{band}", "Manuskript", f"Manuskript_Band{band}_Komplett.md")

    text = build_komplett(band)

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(text)

    # Statistik
    word_count = len(text.split())
    chapter_count = text.count("\n# Kapitel ")
    print(f"\nGespeichert: {output_path}")
    print(f"Kapitel:     {chapter_count}")
    print(f"Wörter:      {word_count:,}")
    print(f"Zeichen:     {len(text):,}")


if __name__ == "__main__":
    main()
