"""
Build a properly formatted DOCX for KDP eBook upload from Manuskript_Band1_Komplett.md.
Handles: chapter headings, paragraphs with first-line indent, scene breaks,
italic/bold text, front matter, back matter.
"""

import os
import re
import sys
from docx import Document
from docx.shared import Pt, Cm, Emu
from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_BREAK
from docx.enum.section import WD_ORIENT
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import band1_anhang as anhang   # Leseprobe, Links, Band-2-Cover (gemeinsam mit dem Taschenbuch)

AUTHOR = "Benjamin Krug"
INPUT_FILE = os.path.join(os.path.dirname(__file__), "..", "Band1", "Manuskript", "Manuskript_Band1_Komplett.md")
OUTPUT_FILE = os.path.join(os.path.dirname(__file__), "..", "Output", "Band1", "KDP_Band1_eBook.docx")


def create_styles(doc):
    """Set up document styles for eBook formatting."""
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

    # Configure "Heading 1" so chapter titles are recognized by Kindle/KDP
    # for the auto-generated navigation TOC, while still looking like our
    # centered chapter headings. The key part is that chapters USE this style.
    h1 = doc.styles["Heading 1"]
    h1.font.name = "Georgia"
    h1.font.size = Pt(16)
    h1.font.bold = True
    h1.font.italic = False
    h1.font.color.rgb = None  # inherit (black) instead of the default blue
    h1pf = h1.paragraph_format
    h1pf.alignment = WD_ALIGN_PARAGRAPH.CENTER
    h1pf.first_line_indent = Cm(0)
    h1pf.space_before = Pt(0)
    h1pf.space_after = Pt(0)
    h1pf.keep_with_next = True


def add_page_break(doc):
    """Add a page break."""
    p = doc.add_paragraph()
    p.paragraph_format.first_line_indent = Cm(0)
    run = p.add_run()
    run.add_break(WD_BREAK.PAGE)


def add_blank_lines(doc, count=1):
    """Add empty paragraphs."""
    for _ in range(count):
        p = doc.add_paragraph()
        p.paragraph_format.first_line_indent = Cm(0)
        p.paragraph_format.space_before = Pt(0)
        p.paragraph_format.space_after = Pt(0)


def add_centered_text(doc, text, font_size=11, bold=False, italic=False):
    """Add a centered paragraph."""
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


def add_formatted_paragraph(doc, text, first_line_indent=True, alignment=None):
    """Add a paragraph with inline formatting (*italic*, **bold**)."""
    p = doc.add_paragraph()
    if not first_line_indent:
        p.paragraph_format.first_line_indent = Cm(0)
    if alignment:
        p.alignment = alignment
        p.paragraph_format.first_line_indent = Cm(0)

    # Parse inline markdown formatting
    # Handle **bold** and *italic*
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


def add_table_of_contents(doc):
    """Insert a real Word TOC field on its own page.

    KDP/Kindle reads this field (built from the Heading 1 chapter titles) and
    turns it into a clickable in-book table of contents. The field needs to be
    updated once in Word/LibreOffice (or by KDP on conversion) to fill in the
    page numbers, but the entries and links are generated automatically.
    """
    add_blank_lines(doc, 3)
    add_centered_text(doc, "Inhalt", font_size=18, bold=True)
    add_blank_lines(doc, 2)

    paragraph = doc.add_paragraph()
    paragraph.paragraph_format.first_line_indent = Cm(0)
    run = paragraph.add_run()

    # Build the TOC field: \o "1-1" = use Heading 1 only,
    # \h = hyperlinks, \z = hide tab leader/page no in web view, \u = outline level
    fld_begin = OxmlElement("w:fldChar")
    fld_begin.set(qn("w:fldCharType"), "begin")

    instr = OxmlElement("w:instrText")
    instr.set(qn("xml:space"), "preserve")
    instr.text = 'TOC \\o "1-1" \\h \\z \\u'

    fld_sep = OxmlElement("w:fldChar")
    fld_sep.set(qn("w:fldCharType"), "separate")

    # Placeholder text shown until the field is updated
    placeholder = OxmlElement("w:t")
    placeholder.text = "Inhaltsverzeichnis wird beim Öffnen aktualisiert."

    fld_end = OxmlElement("w:fldChar")
    fld_end.set(qn("w:fldCharType"), "end")

    r_elem = run._r
    r_elem.append(fld_begin)
    r_elem.append(instr)
    r_elem.append(fld_sep)
    r_elem.append(placeholder)
    r_elem.append(fld_end)

    # Tell Word to update fields automatically when the document is opened,
    # so the TOC and its links are populated without manual interaction.
    settings = doc.settings.element
    update_fields = settings.find(qn("w:updateFields"))
    if update_fields is None:
        update_fields = OxmlElement("w:updateFields")
        settings.append(update_fields)
    update_fields.set(qn("w:val"), "true")

    add_page_break(doc)


def add_front_matter(doc, titel_liste=None):
    """Add title page, half-title, and copyright page."""
    # --- Half title ---
    add_blank_lines(doc, 8)
    add_centered_text(doc, "Die Geisterspürer", font_size=18, bold=True)
    add_page_break(doc)

    # --- Full title page ---
    add_blank_lines(doc, 5)
    add_centered_text(doc, "Die Geisterspürer", font_size=22, bold=True)
    add_blank_lines(doc, 1)
    add_centered_text(doc, "Das Haus, das flüstert", font_size=16, italic=True)
    add_blank_lines(doc, 1)
    add_centered_text(doc, "Band 1", font_size=12)
    add_blank_lines(doc, 3)
    add_centered_text(doc, AUTHOR, font_size=12)
    add_page_break(doc)

    # --- Copyright page ---
    add_blank_lines(doc, 12)
    add_centered_text(doc, "Die Geisterspürer – Das Haus, das flüstert", font_size=10, bold=True)
    add_centered_text(doc, "Band 1", font_size=10)
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
    add_page_break(doc)

    # --- Table of contents (fest, verlinkt; das Feld blieb ein Platzhalter) ---
    add_static_toc(doc, titel_liste)


def add_hyperlink(paragraph, url, text, font_size=11):
    """Klickbarer Link (Kindle oeffnet ihn im Browser). python-docx kann das nicht direkt."""
    r_id = paragraph.part.relate_to(
        url, "http://schemas.openxmlformats.org/officeDocument/2006/relationships/hyperlink",
        is_external=True)
    link = OxmlElement("w:hyperlink")
    link.set(qn("r:id"), r_id)
    run = OxmlElement("w:r")
    rpr = OxmlElement("w:rPr")
    for tag, val in (("w:rFonts", None), ("w:u", "single"), ("w:sz", str(font_size * 2))):
        el = OxmlElement(tag)
        if tag == "w:rFonts":
            el.set(qn("w:ascii"), "Georgia")
            el.set(qn("w:hAnsi"), "Georgia")
        else:
            el.set(qn("w:val"), val)
        rpr.append(el)
    run.append(rpr)
    t = OxmlElement("w:t")
    t.text = text
    run.append(t)
    link.append(run)
    paragraph._p.append(link)
    return link


def add_centered_link(doc, url, text, font_size=12):
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p.paragraph_format.first_line_indent = Cm(0)
    add_hyperlink(p, url, text, font_size)
    return p


def add_back_matter(doc):
    """Anhang (Schritt 1, Plan Band1/PLAN_Durchlesequote.md), gleiche Reihenfolge wie
    das Taschenbuch: Band 2 -> Rezensionsbitte -> Bandliste -> andere Buecher.
    Statt QR-Codes klickbare Links (auf dem Kindle ist ein QR-Code nutzlos).
    Die erfundene Leseprobe ("Heinrich M. - 1847", "vor drei Wochen") und
    "Erscheint 2026" sind ersetzt."""

    # --- 1. Bruecke zu Band 2 ---
    add_page_break(doc)
    add_blank_lines(doc, 2)
    add_centered_text(doc, "Wie geht es weiter?", font_size=16, bold=True)
    add_blank_lines(doc, 1)
    add_centered_text(doc, "Elf Kreise auf Frau Silbers Karte.", font_size=11)
    add_centered_text(doc, "Der nächste liegt am alten Friedhof.", font_size=11)
    add_blank_lines(doc, 1)
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p.paragraph_format.first_line_indent = Cm(0)
    p.add_run().add_picture(anhang.COVER_BAND2, width=Cm(6))
    add_blank_lines(doc, 1)
    add_centered_text(doc, "Die Geisterspürer · Band 2", font_size=11)
    add_centered_text(doc, anhang.BAND2_TITEL, font_size=14, italic=True)

    # --- 2. Leseprobe ---
    absaetze, _ = anhang.pruefe_leseprobe()
    add_page_break(doc)
    add_centered_text(doc, "Leseprobe aus Band 2", font_size=10, italic=True)
    p = add_centered_text(doc, anhang.BAND2_KAPITEL, font_size=16, bold=True)
    p.paragraph_format.space_before = Pt(10)
    p.paragraph_format.space_after = Pt(24)
    erster = True
    for a in absaetze:
        if a == anhang.SZENENWECHSEL:
            add_scene_break(doc)
            erster = True
            continue
        add_formatted_paragraph(doc, a, first_line_indent=not erster)
        erster = False

    # --- 3. Weiter zu Band 2 ---
    add_page_break(doc)
    add_blank_lines(doc, 3)
    add_centered_text(doc, "Wie es weitergeht, steht in", font_size=12)
    add_centered_text(doc, "Die Geisterspürer · Band 2", font_size=14, bold=True)
    add_centered_text(doc, anhang.BAND2_TITEL, font_size=14, italic=True)
    add_blank_lines(doc, 2)
    add_centered_link(doc, anhang.BAND2_URL, "Band 2 ansehen", font_size=14)
    add_blank_lines(doc, 2)
    add_centered_text(doc, "Für Eltern: Der Link führt zur Seite von Band 2 bei Amazon.", font_size=9, italic=True)

    # --- 4. Rezensions-Bitte ---
    add_page_break(doc)
    add_blank_lines(doc, 3)
    add_centered_text(doc, 'Hat dir „Das Haus, das flüstert“ gefallen?', font_size=14, bold=True)
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
    add_blank_lines(doc, 1)
    add_centered_link(doc, anhang.REZENSION_URL, "Jetzt bewerten", font_size=12)
    add_blank_lines(doc, 1)
    add_centered_text(doc, "Vielen Dank!", font_size=11)
    add_centered_text(doc, AUTHOR, font_size=11)

    # --- 5. Serien-Übersicht ---
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

    # --- 6. Andere Serien (gekuerzt) ---
    add_blank_lines(doc, 1)
    add_centered_text(doc, "* * *", font_size=11)
    add_blank_lines(doc, 1)
    add_centered_text(doc, "Mehr von Benjamin Krug:", font_size=13, bold=True)
    add_blank_lines(doc, 1)
    add_centered_text(doc, "Die Herrenhaus-Detektive", font_size=12, bold=True)
    add_centered_text(doc, "Detektivabenteuer ab 8 Jahren", font_size=10, italic=True)
    add_blank_lines(doc, 1)
    add_centered_text(doc, "Die Chrono-Agenten", font_size=12, bold=True)
    add_centered_text(doc, "Zeitreise-Abenteuer", font_size=10, italic=True)


# --- Festes, verlinktes Inhaltsverzeichnis (2026-10-14) ---------------------------------------
# Das Word-Feld oben enthält bis zur Aktualisierung nur den Platzhalter "Inhaltsverzeichnis wird
# beim Öffnen aktualisiert." Ob der KDP-Konverter Felder aktualisiert, ist nicht gesichert ->
# feste Einträge mit internen Links auf Textmarken an den Kapitelüberschriften.
_bm_id = [0]
_kapitel_nr = [0]


def add_bookmark(paragraph, name):
    _bm_id[0] += 1
    start = OxmlElement("w:bookmarkStart")
    start.set(qn("w:id"), str(_bm_id[0]))
    start.set(qn("w:name"), name)
    end = OxmlElement("w:bookmarkEnd")
    end.set(qn("w:id"), str(_bm_id[0]))
    paragraph._p.insert(0, start)
    paragraph._p.append(end)


def add_internal_link(paragraph, anchor, text, font_size=11):
    link = OxmlElement("w:hyperlink")
    link.set(qn("w:anchor"), anchor)
    run = OxmlElement("w:r")
    rpr = OxmlElement("w:rPr")
    fonts = OxmlElement("w:rFonts")
    fonts.set(qn("w:ascii"), "Georgia")
    fonts.set(qn("w:hAnsi"), "Georgia")
    size = OxmlElement("w:sz")
    size.set(qn("w:val"), str(font_size * 2))
    rpr.append(fonts)
    rpr.append(size)
    run.append(rpr)
    t = OxmlElement("w:t")
    t.set(qn("xml:space"), "preserve")
    t.text = text
    run.append(t)
    link.append(run)
    paragraph._p.append(link)


def add_static_toc(doc, titel_liste):
    add_blank_lines(doc, 3)
    add_centered_text(doc, "Inhalt", font_size=18, bold=True)
    add_blank_lines(doc, 2)
    for i, titel in enumerate(titel_liste, 1):
        p = doc.add_paragraph()
        p.paragraph_format.first_line_indent = Cm(0)
        p.alignment = WD_ALIGN_PARAGRAPH.LEFT
        add_internal_link(p, f"kapitel_{i:02d}", titel)


def add_chapter_heading(doc, title):
    """Add a chapter heading with page break.

    Uses the real "Heading 1" style so Kindle/KDP picks the chapter up for the
    auto-generated navigation TOC and the in-book TOC field resolves to it.
    """
    add_page_break(doc)
    add_blank_lines(doc, 3)
    p = doc.add_paragraph(title, style="Heading 1")
    # Ensure the run font matches our book look (style sets this too, but be safe)
    for run in p.runs:
        run.font.name = "Georgia"
        run.font.size = Pt(16)
        run.bold = True
    _kapitel_nr[0] += 1
    add_bookmark(p, f"kapitel_{_kapitel_nr[0]:02d}")
    add_blank_lines(doc, 2)


def add_scene_break(doc):
    """Add a scene break (centered asterisks)."""
    add_blank_lines(doc, 1)
    add_centered_text(doc, "* * *", font_size=11)
    add_blank_lines(doc, 1)


def parse_and_build(doc, content):
    """Parse markdown content and build the DOCX."""
    # Skip the header (title, subtitle, word count, ---)
    match = re.search(r'^# Kapitel 1', content, re.MULTILINE)
    if not match:
        raise ValueError("Could not find '# Kapitel 1' in manuscript")
    body = content[match.start():]

    # Remove ENDE BAND 1 and trailing ---
    body = re.sub(r'\n---\n\n\*\*ENDE BAND 1\*\*\n\n---\n*', '', body)
    body = re.sub(r'\n\*\*ENDE BAND 1\*\*\n*', '', body)
    # Schritt 1 (2026-10): Das Manuskript endet auf "---" + ENDE-Marker. Nach dem
    # Entfernen des Markers blieb das "---" stehen -> Ornament hinter dem letzten
    # Satz des Buches. Trenner am Textende immer entfernen.
    body = re.sub(r'(\n\s*---\s*)+$', '\n', body.rstrip() + '\n')

    # Split into lines
    lines = body.split('\n')

    def _naechste_zeile_ist_kapitel(start):
        """SEPARATOR-BUG-FIX (2026-07-18): schaut ueber Leerzeilen hinweg,
        ob als Naechstes eine Kapitelueberschrift kommt."""
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
            # Empty line - skip
            i += 1
            continue

        # Chapter heading
        if line.startswith('# Kapitel '):
            title = line[2:]  # Remove "# "
            add_chapter_heading(doc, title)
            is_first_para_after_heading = True
            i += 1
            continue

        # Scene break
        if line == '---':
            # ── SEPARATOR-BUG-FIX (2026-07-18) ────────────────────────────
            # Die Kompilier-Skripte setzen ein "---" ZWISCHEN die Kapitel.
            # Fuer diesen Parser ist das nicht von einem Szenentrenner zu
            # unterscheiden -> im Druck stand ein Ornament hinter JEDEM
            # Cliffhanger, dann erst der Seitenumbruch (Band 1: 17, B2: 14,
            # B3: 15, B4: 15 Stueck).
            # Ein Szenentrenner direkt vor einer Kapitelueberschrift ist
            # IMMER falsch -> ueberspringen.
            if _naechste_zeile_ist_kapitel(i + 1):
                i += 1
                continue
            add_scene_break(doc)
            is_first_para_after_break = True
            i += 1
            continue

        # Regular paragraph
        no_indent = is_first_para_after_heading or is_first_para_after_break
        add_formatted_paragraph(doc, line, first_line_indent=not no_indent)
        is_first_para_after_heading = False
        is_first_para_after_break = False
        i += 1


def main():
    import docx.enum.text

    # Read manuscript
    with open(INPUT_FILE, "r", encoding="utf-8") as f:
        content = f.read()

    # Create document
    doc = Document()

    # Set up page margins (for eBook, use standard margins)
    section = doc.sections[0]
    section.top_margin = Cm(2)
    section.bottom_margin = Cm(2)
    section.left_margin = Cm(2)
    section.right_margin = Cm(2)

    # Set up styles
    create_styles(doc)

    cp = doc.core_properties
    cp.title = "Die Geisterspürer – Das Haus, das flüstert (Band 1)"
    cp.author = cp.last_modified_by = AUTHOR
    cp.language = "de-DE"
    for el in doc.styles.element.iter(qn("w:lang")):
        el.set(qn("w:val"), "de-DE")
        el.set(qn("w:eastAsia"), "de-DE")

    # Build document
    titel_liste = [l[2:].strip() for l in content.split("\n") if l.startswith("# Kapitel ")]
    add_front_matter(doc, titel_liste)
    parse_and_build(doc, content)
    add_back_matter(doc)

    xml = doc.element.xml
    for i in range(1, len(titel_liste) + 1):
        if f'w:anchor="kapitel_{i:02d}"' not in xml or f'w:name="kapitel_{i:02d}"' not in xml:
            raise ValueError(f"Inhaltsverzeichnis: Link oder Textmarke für Kapitel {i} fehlt")
    if _kapitel_nr[0] != len(titel_liste):
        raise ValueError(f"{_kapitel_nr[0]} Überschriften, aber {len(titel_liste)} Einträge im Inhalt")

    # Save
    os.makedirs(os.path.dirname(os.path.abspath(OUTPUT_FILE)), exist_ok=True)  # Output/ ist nicht in git (frischer Klon)
    doc.save(OUTPUT_FILE)
    print(f"{OUTPUT_FILE} erstellt!")

    # Stats
    para_count = len(doc.paragraphs)
    print(f"Absätze: {para_count}")


if __name__ == "__main__":
    main()
