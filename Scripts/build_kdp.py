"""
Build KDP-ready source markdown from Manuskript_Band1_Komplett.md
Adds front matter, back matter, replaces scene breaks, adds page breaks.
No fenced divs (:::) — they cause non-printable markers in KDP PDF.
"""
import re
import os

AUTHOR = "Benjamin Krug"
_SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
_PROJECT_ROOT = os.path.join(_SCRIPT_DIR, "..")

# Read the manuscript
with open(os.path.join(_PROJECT_ROOT, "Band1", "Manuskript", "Manuskript_Band1_Komplett.md"), "r", encoding="utf-8") as f:
    content = f.read()

# Strip the old header (lines 1-6: title, subtitle, word count, ---)
first_chapter = content.index("# Kapitel 1")
body = content[first_chapter:]

# Remove "ENDE BAND 1" and trailing ---
body = re.sub(r'\n---\n\n\*\*ENDE BAND 1\*\*\n\n---\n*', '', body)
body = re.sub(r'\n\*\*ENDE BAND 1\*\*\n*', '', body)

# Add \newpage before each chapter heading (except the first)
body = re.sub(r'\n# Kapitel ', '\n\\\\newpage\n\n# Kapitel ', body)
body = body.replace('\\newpage\n\n# Kapitel 1 ', '# Kapitel 1 ', 1)

# Replace scene breaks --- with centered asterisks (no div wrapper)
body = body.replace('\n---\n', '\n\n\\begin{center}\n* * *\n\\end{center}\n\n')

# Build front matter (pure LaTeX, no fenced divs)
front_matter = f"""---
title: "Das Haus, das flüstert"
subtitle: "Die Geisterspürer · Band 1"
author: "{AUTHOR}"
lang: de
---

\\newpage

\\begin{{center}}
\\vspace*{{4cm}}
{{\\Large Die Geisterspürer}}
\\end{{center}}

\\newpage

\\begin{{center}}
\\vspace*{{2cm}}
{{\\LARGE Die Geisterspürer}}

\\vspace{{0.5cm}}
{{\\Large Das Haus, das flüstert}}

\\vspace{{0.3cm}}
Band 1

\\vspace{{2cm}}
{AUTHOR}
\\end{{center}}

\\newpage

\\begin{{center}}
\\vspace*{{8cm}}
**Die Geisterspürer – Das Haus, das flüstert**

Band 1

\\vspace{{1cm}}

© 2026 {AUTHOR}

Alle Rechte vorbehalten.

\\vspace{{0.5cm}}

Dieses Buch ist ein Werk der Fiktion. Namen, Figuren, Orte und Ereignisse sind frei erfunden. Jede Ähnlichkeit mit tatsächlichen Personen, lebend oder tot, ist rein zufällig.

\\vspace{{0.5cm}}

Umschlaggestaltung: {AUTHOR}

Satz und Layout: {AUTHOR}

\\vspace{{0.5cm}}

Erstausgabe 2026

Independently published
\\end{{center}}

\\newpage

"""

# Build back matter (no fenced divs)
back_matter = f"""

\\newpage

## Weiterlesen?

### Band 2: Der Friedhof ohne Namen

Ein namenloser Grabstein. Ein Geist, der seit 180 Jahren zwischen den Gräbern steht. Und ein Geheimnis, das tiefer reicht als sechs Fuß unter der Erde.

Nora und Theo haben Lina befreit. Aber die Karte zeigt zehn weitere Markierungen — und der nächste Unruhige wartet auf dem alten Friedhof von Gravenstedt. Er ist nicht traurig. Er ist wütend. Und Schatten knurrt schon, bevor sie das Friedhofstor erreichen.

*Erscheint 2026*

\\vspace{{1cm}}

\\begin{{center}}
* * *
\\end{{center}}

## Die Geisterspürer — Alle Bände

**Band 1:** Das Haus, das flüstert

**Band 2:** Der Friedhof ohne Namen

**Band 3:** Schatten sieht mehr

**Band 4:** Die zugemauerte Tür

**Band 5:** Der Schleier

\\vspace{{1cm}}

\\begin{{center}}
* * *
\\end{{center}}

## Hat dir das Buch gefallen?

Dann freue ich mich über eine kurze Bewertung auf Amazon! Jede Rezension hilft anderen Leserinnen und Lesern, dieses Buch zu entdecken — und mir, weitere Bände zu schreiben.

Vielen Dank!

{AUTHOR}
"""

# Combine
full = front_matter + body + back_matter

# Write output
with open(os.path.join(_PROJECT_ROOT, "Output", "Band1", "KDP_Band1_Source.md"), "w", encoding="utf-8") as f:
    f.write(full)

print("Output/KDP_Band1_Source.md erstellt!")
print(f"Gesamtlänge: {len(full)} Zeichen")

chapters = re.findall(r'# Kapitel \d+', full)
print(f"Kapitel gefunden: {len(chapters)}")

breaks = full.count('* * *')
print(f"Szenetrenner: {breaks}")

newpages = full.count('\\newpage')
print(f"Seitenumbrüche: {newpages}")

# Verify
placeholders = re.findall(r'\[AUTORENNAME\]', full)
divs = re.findall(r'^:::', full, re.MULTILINE)
if placeholders:
    print(f"WARNUNG: {len(placeholders)} Platzhalter noch offen!")
else:
    print("Alle Platzhalter ersetzt.")
if divs:
    print(f"WARNUNG: {len(divs)} Fenced-Div-Marker gefunden!")
else:
    print("Keine Fenced-Div-Marker (sauber für KDP).")
