"""
Build a properly formatted DOCX for KDP eBook upload from Manuskript_Band5_Komplett.md.
Abgeleitet von build_ebook_docx_band4.py: echte Hyperlink+Bookmark-TOC statt
Word-Feld, QR-Code-Rezension, Widmung+Epigraph, apply_typography() fuer die
reine-ASCII-Manuskriptquelle.

Band-5-Sonderfaelle (Serienfinale):
  1. KEIN Teaser -- kein Nachfolgeband. Backmatter geht direkt von der
     Rezensions-Bitte zur Serienuebersicht (uebernommen aus
     build_taschenbuch_docx_band5.py, dort "mit dem Autor abgestimmt").
  2. Cross-Promo beginnt mit dem Geisterspuerer-SPIELBUCH (nicht mit
     Herrenhaus-Detektive wie bei Band 1-4) -- bewusste Reihenfolge, weil ein
     Leser direkt nach dem Serienfinale eher zu "dieselbe Geschichte, neu
     erlebt" greift als zu einer fremden Reihe.
  3. DREISTUFIGER ENDE-Marker statt der einfachen Band-1-4-Regex:
     **ENDE** (aus Kapitel_18.md selbst) + **ENDE BAND 5** + **ENDE DER
     ERSTEN STAFFEL** -- alle drei muessen weg, sonst landet z.B.
     "ENDE DER ERSTEN STAFFEL" als sichtbarer Fliesstext im Kindle-Buch.
     Regex 1:1 aus build_taschenbuch_docx_band5.py uebernommen (dort als
     "LANDMINE 2" dokumentiert), inklusive der Selbstpruefung am Ende von
     parse_and_build, die abbricht, falls doch ein ENDE-Rest uebrig bleibt.
"""

import os
import re
from docx import Document
from docx.shared import Pt, Cm, Emu, Inches
from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_BREAK
from docx.enum.section import WD_ORIENT
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

AUTHOR = "Benjamin Krug"
INPUT_FILE = os.path.join(os.path.dirname(__file__), "..", "Band5", "Manuskript", "Manuskript_Band5_Komplett.md")
OUTPUT_FILE = os.path.join(os.path.dirname(__file__), "..", "Output", "Band5", "KDP_Band5_eBook.docx")
QR_IMAGE = os.path.join(os.path.dirname(__file__), "..", "Band5", "Cover", "qr_rezension_band5.png")

# Widmung + Epigraph, wortgleich uebernommen aus build_manuskript_komplett_band5.py
# (dort die publizierte Quelle -- build_taschenbuch_docx_band5.py importiert von
# dort statt zu duplizieren, um Drift zu vermeiden; hier bewusst dieselbe Wahl).
WIDMUNG_ZEILEN = [
    "Für alle, die Angst haben, sie hätten etwas verpasst.",
    "Und für die, die sich trotzdem umdrehen.",
]
EPIGRAPH_ZEILEN = [
    "Der gefährlichste Geist ist nicht der, der etwas Böses will.",
    "Es ist der, der sich ganz sicher ist.",
]
EPIGRAPH_SOURCE = "aus dem Notizbuch von Margret Silber"


# ── Typografie: ASCII -> deutsche Anfuehrungszeichen/Gedankenstriche ─────────

def typo_quotes(text: str) -> str:
    out = []
    inside = False
    for idx, ch in enumerate(text):
        if ch == '"':
            if not inside:
                out.append('„')
                inside = True
            else:
                out.append('“')
                inside = False
        elif ch == "'":
            prev = text[idx - 1] if idx > 0 else ' '
            nxt = text[idx + 1] if idx + 1 < len(text) else ' '
            if prev.isalpha() and nxt.isalpha():
                out.append('’')
            elif prev.isalpha():
                out.append('’')
            else:
                out.append(ch)
        else:
            out.append(ch)
    return "".join(out)


def typo_dashes(text: str) -> str:
    text = re.sub(r'\s—\s', ' – ', text)
    text = re.sub(r'\s—', ' –', text)
    text = re.sub(r'—\s', '– ', text)
    return text


def apply_typography(text: str) -> str:
    text = typo_quotes(text)
    text = typo_dashes(text)
    return text


def create_styles(doc):
    style = doc.styles["Normal"]
    font = style.font
    font.name = "Georgia"
    font.size = Pt(11)
    pf = style.paragraph_format
    pf.space_before = Pt(0)
    pf.space_after = Pt(0)
    pf.line_spacing = 1.5
    pf.first_line_indent = Cm(0.7)
    pf.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY

    h1 = doc.styles["Heading 1"]
    h1.font.name = "Georgia"
    h1.font.size = Pt(16)
    h1.font.bold = True
    h1.font.italic = False
    h1.font.color.rgb = None
    h1pf = h1.paragraph_format
    h1pf.alignment = WD_ALIGN_PARAGRAPH.CENTER
    h1pf.first_line_indent = Cm(0)
    h1pf.space_before = Pt(0)
    h1pf.space_after = Pt(0)
    h1pf.keep_with_next = True


def add_page_break(doc):
    p = doc.add_paragraph()
    p.paragraph_format.first_line_indent = Cm(0)
    run = p.add_run()
    run.add_break(WD_BREAK.PAGE)


def add_blank_lines(doc, count=1):
    for _ in range(count):
        p = doc.add_paragraph()
        p.paragraph_format.first_line_indent = Cm(0)
        p.paragraph_format.space_before = Pt(0)
        p.paragraph_format.space_after = Pt(0)


def add_centered_text(doc, text, font_size=11, bold=False, italic=False):
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p.paragraph_format.first_line_indent = Cm(0)
    p.paragraph_format.space_before = Pt(0)
    p.paragraph_format.space_after = Pt(0)
    run = p.add_run(text)
    run.font.size = Pt(font_size)
    run.font.name = "Georgia"
    run.bold = bold
    run.italic = italic
    return p


def add_centered_image(doc, image_path, width_inches=1.6):
    if not os.path.isfile(image_path):
        print(f"  WARNUNG: Bild nicht gefunden, wird übersprungen: {image_path}")
        return None
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p.paragraph_format.first_line_indent = Cm(0)
    p.paragraph_format.space_before = Pt(0)
    p.paragraph_format.space_after = Pt(0)
    run = p.add_run()
    run.add_picture(image_path, width=Inches(width_inches))
    return p


def add_formatted_paragraph(doc, text, first_line_indent=True, alignment=None):
    p = doc.add_paragraph()
    if not first_line_indent:
        p.paragraph_format.first_line_indent = Cm(0)
    if alignment:
        p.alignment = alignment
        p.paragraph_format.first_line_indent = Cm(0)

    pattern = r'(\*\*(.+?)\*\*|\*(.+?)\*|([^*]+))'
    parts = re.findall(pattern, text)

    for full_match, bold_text, italic_text, plain_text in parts:
        if bold_text:
            run = p.add_run(bold_text)
            run.bold = True
            run.font.name = "Georgia"
            run.font.size = Pt(11)
        elif italic_text:
            run = p.add_run(italic_text)
            run.italic = True
            run.font.name = "Georgia"
            run.font.size = Pt(11)
        elif plain_text:
            run = p.add_run(plain_text)
            run.font.name = "Georgia"
            run.font.size = Pt(11)

    return p


def _add_bookmark(paragraph, bookmark_id, bookmark_name):
    start = OxmlElement("w:bookmarkStart")
    start.set(qn("w:id"), str(bookmark_id))
    start.set(qn("w:name"), bookmark_name)
    end = OxmlElement("w:bookmarkEnd")
    end.set(qn("w:id"), str(bookmark_id))
    paragraph._p.insert(0, start)
    paragraph._p.append(end)


def _add_internal_hyperlink(paragraph, text, anchor, font_size=12):
    hyperlink = OxmlElement("w:hyperlink")
    hyperlink.set(qn("w:anchor"), anchor)

    run = OxmlElement("w:r")
    rPr = OxmlElement("w:rPr")
    rFonts = OxmlElement("w:rFonts")
    rFonts.set(qn("w:ascii"), "Georgia")
    rFonts.set(qn("w:hAnsi"), "Georgia")
    rPr.append(rFonts)
    sz = OxmlElement("w:sz")
    sz.set(qn("w:val"), str(font_size * 2))
    rPr.append(sz)
    run.append(rPr)

    t = OxmlElement("w:t")
    t.set(qn("xml:space"), "preserve")
    t.text = text
    run.append(t)

    hyperlink.append(run)
    paragraph._p.append(hyperlink)


def _kapitel_nummer(title):
    m = re.search(r"Kapitel (\d+)", title)
    if not m:
        raise ValueError(f"Keine Kapitelnummer in Titel gefunden: {title!r}")
    return int(m.group(1))


def add_table_of_contents(doc, chapter_titles):
    add_blank_lines(doc, 3)
    add_centered_text(doc, "Inhalt", font_size=18, bold=True)
    add_blank_lines(doc, 2)

    for title in chapter_titles:
        nummer = _kapitel_nummer(title)
        p = doc.add_paragraph()
        p.paragraph_format.first_line_indent = Cm(0)
        p.paragraph_format.space_after = Pt(6)
        _add_internal_hyperlink(p, title, f"kapitel_{nummer}", font_size=12)

    add_page_break(doc)


def add_front_matter(doc, chapter_titles):
    add_blank_lines(doc, 8)
    add_centered_text(doc, "Die Geisterspürer", font_size=18, bold=True)
    add_page_break(doc)

    add_blank_lines(doc, 5)
    add_centered_text(doc, "Die Geisterspürer", font_size=22, bold=True)
    add_blank_lines(doc, 1)
    add_centered_text(doc, "Der Schleier", font_size=16, italic=True)
    add_blank_lines(doc, 1)
    add_centered_text(doc, "Band 5", font_size=12)
    add_blank_lines(doc, 3)
    add_centered_text(doc, AUTHOR, font_size=12)
    add_page_break(doc)

    add_blank_lines(doc, 12)
    add_centered_text(doc, "Die Geisterspürer – Der Schleier", font_size=10, bold=True)
    add_centered_text(doc, "Band 5", font_size=10)
    add_blank_lines(doc, 1)
    add_centered_text(doc, f"© 2026 {AUTHOR}", font_size=9)
    add_centered_text(doc, "Alle Rechte vorbehalten.", font_size=9)
    add_blank_lines(doc, 1)
    p = add_centered_text(doc, "", font_size=9)
    run = p.add_run(
        "Dieses Buch ist ein Werk der Fiktion. Namen, Figuren, Orte und "
        "Ereignisse sind frei erfunden. Jede Ähnlichkeit mit tatsächlichen "
        "Personen, lebend oder tot, ist rein zufällig."
    )
    run.font.size = Pt(9)
    run.font.name = "Georgia"
    add_blank_lines(doc, 1)
    add_centered_text(doc, f"Umschlaggestaltung: {AUTHOR}", font_size=9)
    add_centered_text(doc, f"Satz und Layout: {AUTHOR}", font_size=9)
    add_blank_lines(doc, 1)
    add_centered_text(doc, "Erstausgabe 2026", font_size=9)
    add_centered_text(doc, "Independently published", font_size=9)

    # ── WIDMUNG (eigene Seite, zentriert, kursiv) ──────────────────────────
    add_page_break(doc)
    add_blank_lines(doc, 12)
    for zeile in WIDMUNG_ZEILEN:
        add_centered_text(doc, zeile, font_size=12, italic=True)
        add_blank_lines(doc, 1)

    # ── EPIGRAPH (eigene Seite, Silber-Notizbuch) ──────────────────────────
    add_page_break(doc)
    add_blank_lines(doc, 12)
    for zeile in EPIGRAPH_ZEILEN:
        add_centered_text(doc, zeile, font_size=12, italic=True)
        add_blank_lines(doc, 1)
    add_blank_lines(doc, 1)
    add_centered_text(doc, f"— {EPIGRAPH_SOURCE}", font_size=10, italic=True)

    add_page_break(doc)
    add_table_of_contents(doc, chapter_titles)


def add_back_matter(doc):
    """Rezensions-Bitte -> KEIN Teaser (Serienfinale) -> Serienuebersicht ->
    Cross-Promo (Spielbuch zuerst). Struktur 1:1 aus
    build_taschenbuch_docx_band5.py uebernommen."""
    add_page_break(doc)

    # --- 1. Rezensions-Bitte ---
    add_blank_lines(doc, 3)
    add_centered_text(doc, 'Hat dir „Der Schleier“ gefallen?', font_size=14, bold=True)
    add_blank_lines(doc, 1)
    add_formatted_paragraph(
        doc,
        "Dann freue ich mich riesig über eine kurze Bewertung auf Amazon "
        "— auch nur ein oder zwei Sätze reichen völlig.",
        first_line_indent=False,
    )
    add_blank_lines(doc, 1)
    add_formatted_paragraph(
        doc,
        "Jede Rezension hilft anderen Kindern (und ihren Eltern), dieses Buch "
        "zu entdecken. Und mir hilft sie, weitere Bände zu schreiben.",
        first_line_indent=False,
    )
    add_blank_lines(doc, 2)

    add_centered_text(doc, "Einfach den Code scannen und eine Bewertung dalassen:", font_size=11, italic=True)
    add_blank_lines(doc, 1)
    add_centered_image(doc, QR_IMAGE, width_inches=1.6)
    add_blank_lines(doc, 1)
    add_centered_text(doc, "(Handykamera auf den Code halten – der Link öffnet sich von selbst.)", font_size=9, italic=True)

    add_blank_lines(doc, 2)
    add_centered_text(doc, "Vielen Dank!", font_size=11)
    add_centered_text(doc, AUTHOR, font_size=11)

    # --- 2. KEIN TEASER — Band 5 ist der letzte Band der Staffel. ---
    # Wie im Taschenbuch bewusst leer gelassen: kein Staffel-2-Teaser (Staffel 2
    # ist noch nicht geschrieben -- genau der Fehler, der Band 3/4 vorher
    # unterlaufen ist). Direkt weiter zur Serienuebersicht.

    # --- 3. Serien-Übersicht ---
    add_page_break(doc)
    add_blank_lines(doc, 2)
    add_centered_text(doc, "Die Geisterspürer — Alle Bände", font_size=14, bold=True)
    add_blank_lines(doc, 1)

    for band_num, title in [
        (1, "Das Haus, das flüstert"),
        (2, "Der Friedhof ohne Namen"),
        (3, "Schatten sieht mehr"),
        (4, "Die zugemauerte Tür"),
        (5, "Der Schleier"),
    ]:
        add_formatted_paragraph(
            doc,
            f"**Band {band_num}:** {title}",
            first_line_indent=False,
        )

    # --- 4. Cross-Verweis: Spielbuch zuerst (Band-5-spezifisch) ---
    add_blank_lines(doc, 1)
    add_centered_text(doc, "* * *", font_size=11)
    add_blank_lines(doc, 1)
    add_centered_text(doc, f"Mehr spannende Abenteuer von {AUTHOR}:", font_size=14, bold=True)
    add_blank_lines(doc, 1)

    # (1) Geisterspürer als Spielbuch
    add_centered_text(doc, "Die Geisterspürer – als Spielbuch", font_size=13, bold=True)
    add_blank_lines(doc, 1)
    add_formatted_paragraph(
        doc,
        "Du kennst die Geschichte. Aber was wäre passiert, wenn Nora damals "
        "nicht in den Keller gegangen wäre?",
        first_line_indent=False,
    )
    add_formatted_paragraph(
        doc,
        "In „Das Haus, das flüstert – Grusel-Spielbuch“ entscheidest du an jedem "
        "Wendepunkt selbst. Folgst du dem Hund die Treppe hinauf? Gehst du nachts "
        "in den Keller? Liest du das Tagebuch allein — oder mit Theo?",
        first_line_indent=False,
    )
    add_formatted_paragraph(
        doc,
        "24 verschiedene Enden. Und ein geheimes, das nur die Mutigsten finden.",
        first_line_indent=False,
    )
    add_blank_lines(doc, 1)
    add_centered_text(doc, "Grusel-Spielbuch ab 10 Jahren.", font_size=11, italic=True)

    # (2) Herrenhaus-Detektive
    add_blank_lines(doc, 2)
    add_centered_text(doc, "Die Herrenhaus-Detektive", font_size=13, bold=True)
    add_blank_lines(doc, 1)
    add_formatted_paragraph(
        doc,
        "Niemand darf das alte Herrenhaus betreten. Aber Jonas, Mila und Ben "
        "finden einen Schlüssel — und hinter der verschlossenen Tür wartet ein "
        "Geheimnis, das seit dreißig Jahren niemand lüften durfte.",
        first_line_indent=False,
    )
    add_blank_lines(doc, 1)
    add_centered_text(doc, "Spannendes Detektivabenteuer ab 8 Jahren.", font_size=11, italic=True)

    # (3) Herrenhaus-Detektive als Spielbuch
    add_blank_lines(doc, 2)
    add_centered_text(doc, "Die Herrenhaus-Detektive – als Spielbuch", font_size=13, bold=True)
    add_blank_lines(doc, 1)
    add_formatted_paragraph(
        doc,
        "Zwei Fälle, in denen du selbst ermittelst: „Das verbotene Herrenhaus“ "
        "und „Das Geheimnis des Brunnens“.",
        first_line_indent=False,
    )
    add_formatted_paragraph(
        doc,
        "Welcher Spur folgst du zuerst? Wem glaubst du? Jede Entscheidung führt "
        "dich auf einem anderen Weg durch den Fall — und zu einem anderen Ende.",
        first_line_indent=False,
    )
    add_blank_lines(doc, 1)
    add_centered_text(doc, "Detektiv-Spielbücher ab 8 Jahren.", font_size=11, italic=True)


def add_chapter_heading(doc, title):
    add_page_break(doc)
    add_blank_lines(doc, 3)
    p = doc.add_paragraph(title, style="Heading 1")
    for run in p.runs:
        run.font.name = "Georgia"
        run.font.size = Pt(16)
        run.bold = True
    nummer = _kapitel_nummer(title)
    _add_bookmark(p, nummer, f"kapitel_{nummer}")
    add_blank_lines(doc, 2)


def add_scene_break(doc):
    add_blank_lines(doc, 1)
    add_centered_text(doc, "* * *", font_size=11)
    add_blank_lines(doc, 1)


def parse_and_build(doc, content):
    match = re.search(r'^# Kapitel 1', content, re.MULTILINE)
    if not match:
        raise ValueError("Could not find '# Kapitel 1' in manuscript")
    body = content[match.start():]

    # ── LANDMINE 2 (Band 5 hat eine ZWEITE ENDE-Zeile) ────────────────────
    # 1:1 aus build_taschenbuch_docx_band5.py uebernommen. Die einfache
    # Band-1-4-Regex traefe "ENDE DER ERSTEN STAFFEL" nicht -> wuerde als
    # sichtbarer Fliesstext im Kindle-Buch landen.
    body = re.sub(
        r'\n+---\n+\*\*ENDE BAND 5\*\*\n+\*\*ENDE DER ERSTEN STAFFEL\*\*\n+---\n*',
        '', body)
    body = re.sub(r'\n+\*\*ENDE (BAND 5|DER ERSTEN STAFFEL)\*\*\n*', '', body)

    # ── Und der Marker AUS Kapitel 18 selbst ──────────────────────────────
    # Kapitel_18.md endet mit "**ENDE**" -- ein Manuskript-Marker, kein
    # Buchinhalt. Nur die exakte Marker-Zeile, niemals das Wort "Ende" im
    # Fliesstext.
    body = re.sub(r'(?m)^\s*\*\*ENDE\*\*\s*$\n?', '', body)

    # Selbstpruefung: kein ENDE-Rest darf uebrig sein, sonst Abbruch statt
    # stillem Falschbau (gleiche Pruefung wie im Taschenbuch-Skript).
    rest = [z for z in body.split('\n')
            if re.fullmatch(r'\s*\*{0,2}ENDE[^*]*\*{0,2}\s*', z)]
    if rest:
        raise ValueError(
            f"ENDE-Marker nicht sauber entfernt, wuerde im Buch landen: {rest!r} "
            f"(Landmine 2 — Regex pruefen.)"
        )

    lines = body.split('\n')

    def _naechste_zeile_ist_kapitel(start):
        j = start
        while j < len(lines) and not lines[j].strip():
            j += 1
        return j < len(lines) and lines[j].strip().startswith('# Kapitel ')

    is_first_para_after_heading = False
    is_first_para_after_break = False
    i = 0

    while i < len(lines):
        line = lines[i].strip()

        if not line:
            i += 1
            continue

        if line.startswith('# Kapitel '):
            title = line[2:]
            add_chapter_heading(doc, title)
            is_first_para_after_heading = True
            i += 1
            continue

        if line == '---':
            if _naechste_zeile_ist_kapitel(i + 1):
                i += 1
                continue
            add_scene_break(doc)
            is_first_para_after_break = True
            i += 1
            continue

        no_indent = is_first_para_after_heading or is_first_para_after_break
        text = apply_typography(line)
        add_formatted_paragraph(doc, text, first_line_indent=not no_indent)
        is_first_para_after_heading = False
        is_first_para_after_break = False
        i += 1


def main():
    with open(INPUT_FILE, "r", encoding="utf-8") as f:
        content = f.read()

    chapter_titles = re.findall(r"^# (Kapitel \d+.*)$", content, re.MULTILINE)
    if not chapter_titles:
        raise ValueError("Keine Kapitelueberschriften im Manuskript gefunden")

    doc = Document()

    section = doc.sections[0]
    section.top_margin = Cm(2)
    section.bottom_margin = Cm(2)
    section.left_margin = Cm(2)
    section.right_margin = Cm(2)

    create_styles(doc)

    add_front_matter(doc, chapter_titles)
    parse_and_build(doc, content)
    add_back_matter(doc)

    doc.save(OUTPUT_FILE)
    print(f"{OUTPUT_FILE} erstellt!")

    para_count = len(doc.paragraphs)
    print(f"Absätze: {para_count}")


if __name__ == "__main__":
    main()
