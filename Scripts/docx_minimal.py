"""
Minimaler DOCX-Schreiber ohne Fremdbibliotheken.

WARUM ES DAS GIBT
-----------------
Die Build-Skripte der Reihe brauchen `python-docx`. In manchen Umgebungen laesst
sich das nicht installieren (kein PyPI-Zugang) - und dann steht die ganze
Produktion still, obwohl LibreOffice fuer die PDF-Wandlung vorhanden ist.

Eine .docx ist aber nur ein ZIP mit XML darin, und `zipfile` steht in der
Standardbibliothek. Dieses Modul schreibt genau die OOXML-Teilmenge, die ein
Roman-Innenteil braucht: Seitenformat, Spiegelraender, Georgia, Blocksatz,
Zeilenabstand, Kapitaelchen, Kursiv/Fett, Seitenumbrueche und Seitenzahlen.

KEIN Ersatz fuer python-docx im Allgemeinen - nur fuer diesen einen Zweck.

Masseinheiten in OOXML:
    1 Zoll = 1440 Twips · 1 cm = 567 Twips · Schriftgrad in halben Punkten
    Zeilenabstand: 240 = einfach, also 360 = 1,5-fach
"""

import os
import zipfile
from xml.sax.saxutils import escape

ZOLL = 1440
CM = 567

NS = ('xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main" '
      'xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships"')


def _esc(t):
    return escape(t).replace('"', "&quot;")


class Run:
    def __init__(self, text, *, bold=False, italic=False, smallcaps=False,
                 size=11, font="Georgia", color=None):
        self.text, self.bold, self.italic = text, bold, italic
        self.smallcaps, self.size, self.font, self.color = smallcaps, size, font, color

    def xml(self):
        # ‼️ Die Reihenfolge ist NICHT frei: CT_RPr schreibt sie vor -
        #    rFonts, b, i, smallCaps, color, sz, szCs. Ein falsch sortiertes
        #    rPr laesst LibreOffice die Datei gar nicht erst oeffnen.
        p = [f'<w:rFonts w:ascii="{self.font}" w:hAnsi="{self.font}"/>']
        if self.bold:
            p.append('<w:b/>')
        if self.italic:
            p.append('<w:i/>')
        if self.smallcaps:
            p.append('<w:smallCaps/>')
        if self.color:
            p.append(f'<w:color w:val="{self.color}"/>')
        p.append(f'<w:sz w:val="{int(self.size*2)}"/>')
        p.append(f'<w:szCs w:val="{int(self.size*2)}"/>')
        return (f'<w:r><w:rPr>{"".join(p)}</w:rPr>'
                f'<w:t xml:space="preserve">{_esc(self.text)}</w:t></w:r>')


class Para:
    """Ein Absatz. align: left|center|both · indent/spacing in Twips."""

    def __init__(self, runs=None, *, align=None, indent=None, space_before=0,
                 space_after=0, line=360, page_break_before=False,
                 keep_with_next=False, style=None):
        self.runs = runs or []
        self.align, self.indent = align, indent
        self.space_before, self.space_after, self.line = space_before, space_after, line
        self.page_break_before, self.keep_with_next = page_break_before, keep_with_next
        self.style = style

    def xml(self):
        # ‼️ Wie bei Run: CT_PPr gibt die Reihenfolge vor -
        #    pStyle, keepNext, pageBreakBefore, widowControl, spacing, ind, jc.
        p = []
        if self.style:
            p.append(f'<w:pStyle w:val="{self.style}"/>')
        if self.keep_with_next:
            p.append('<w:keepNext/>')
        if self.page_break_before:
            p.append('<w:pageBreakBefore/>')
        p.append('<w:widowControl/>')
        p.append(f'<w:spacing w:before="{self.space_before}" '
                 f'w:after="{self.space_after}" '
                 f'w:line="{self.line}" w:lineRule="auto"/>')
        p.append(f'<w:ind w:firstLine="{self.indent if self.indent else 0}"/>')
        if self.align:
            p.append(f'<w:jc w:val="{self.align}"/>')
        return (f'<w:p><w:pPr>{"".join(p)}</w:pPr>'
                f'{"".join(r.xml() for r in self.runs)}</w:p>')


class SeitenzahlPara(Para):
    """Fussnotenzeile mit PAGE-Feld - Word/LibreOffice fuellen die Zahl selbst."""

    def xml(self):
        feld = (
            '<w:r><w:rPr><w:rFonts w:ascii="Georgia" w:hAnsi="Georgia"/>'
            '<w:sz w:val="20"/></w:rPr><w:fldChar w:fldCharType="begin"/></w:r>'
            '<w:r><w:instrText xml:space="preserve"> PAGE </w:instrText></w:r>'
            '<w:r><w:fldChar w:fldCharType="end"/></w:r>'
        )
        return ('<w:p><w:pPr>'
                '<w:spacing w:before="0" w:after="0" w:line="240" w:lineRule="auto"/>'
                '<w:ind w:firstLine="0"/>'
                '<w:jc w:val="center"/></w:pPr>'
                f'{feld}</w:p>')


class Dokument:
    def __init__(self, *, breite_zoll=6.0, hoehe_zoll=9.0,
                 innen=0.875, aussen=0.625, oben=0.75, unten=0.75,
                 spiegelraender=True, seitenzahlen=True):
        self.paras = []
        self.b = round(breite_zoll * ZOLL)
        self.h = round(hoehe_zoll * ZOLL)
        self.mi, self.ma = round(innen * ZOLL), round(aussen * ZOLL)
        self.mo, self.mu = round(oben * ZOLL), round(unten * ZOLL)
        self.spiegel = spiegelraender
        self.seitenzahlen = seitenzahlen

    def add(self, para):
        self.paras.append(para)
        return para

    def leerzeile(self, n=1):
        for _ in range(n):
            self.add(Para([], indent=0, line=240))

    def seitenumbruch(self):
        self.add(Para([], indent=0, page_break_before=True))

    # ── Dateiteile ────────────────────────────────────────────────────────
    def _sect_pr(self):
        fuss = ('<w:footerReference w:type="default" r:id="rId2"/>'
                if self.seitenzahlen else '')
        return (
            f'<w:sectPr>{fuss}'
            f'<w:pgSz w:w="{self.b}" w:h="{self.h}"/>'
            f'<w:pgMar w:top="{self.mo}" w:right="{self.ma}" w:bottom="{self.mu}" '
            f'w:left="{self.mi}" w:header="0" w:footer="504" w:gutter="0"/>'
            f'<w:docGrid w:linePitch="360"/></w:sectPr>'
        )

    def _document_xml(self):
        koerper = "".join(p.xml() for p in self.paras)
        return (f'<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
                f'<w:document {NS}><w:body>{koerper}{self._sect_pr()}</w:body></w:document>')

    def _styles_xml(self):
        spiegel = '<w:mirrorMargins/>' if self.spiegel else ''
        return (
            '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
            f'<w:styles {NS}><w:docDefaults><w:rPrDefault><w:rPr>'
            '<w:rFonts w:ascii="Georgia" w:hAnsi="Georgia"/><w:sz w:val="22"/>'
            '</w:rPr></w:rPrDefault><w:pPrDefault><w:pPr>'
            '<w:jc w:val="both"/><w:spacing w:line="360" w:lineRule="auto"/>'
            '</w:pPr></w:pPrDefault></w:docDefaults>'
            '<w:style w:type="paragraph" w:default="1" w:styleId="Normal">'
            '<w:name w:val="Normal"/></w:style>'
            '<w:style w:type="paragraph" w:styleId="Heading1">'
            '<w:name w:val="heading 1"/><w:basedOn w:val="Normal"/>'
            '<w:pPr><w:outlineLvl w:val="0"/><w:jc w:val="center"/></w:pPr>'
            '<w:rPr><w:b/><w:sz w:val="28"/></w:rPr></w:style>'
            f'</w:styles>{spiegel}'.replace(f'</w:styles>{spiegel}', '</w:styles>')
        )

    def _settings_xml(self):
        spiegel = '<w:mirrorMargins/>' if self.spiegel else ''
        return ('<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
                f'<w:settings {NS}>{spiegel}'
                '<w:updateFields w:val="true"/></w:settings>')

    def _footer_xml(self):
        return ('<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
                f'<w:ftr {NS}>{SeitenzahlPara().xml()}</w:ftr>')

    def speichern(self, pfad):
        os.makedirs(os.path.dirname(os.path.abspath(pfad)), exist_ok=True)
        ct = ('<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
              '<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types">'
              '<Default Extension="rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/>'
              '<Default Extension="xml" ContentType="application/xml"/>'
              '<Override PartName="/word/document.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.document.main+xml"/>'
              '<Override PartName="/word/styles.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.styles+xml"/>'
              '<Override PartName="/word/settings.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.settings+xml"/>'
              '<Override PartName="/word/footer1.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.footer+xml"/>'
              '</Types>')
        rels = ('<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
                '<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">'
                '<Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/officeDocument" Target="word/document.xml"/>'
                '</Relationships>')
        drels = ('<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
                 '<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">'
                 '<Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/styles" Target="styles.xml"/>'
                 '<Relationship Id="rId2" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/footer" Target="footer1.xml"/>'
                 '<Relationship Id="rId3" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/settings" Target="settings.xml"/>'
                 '</Relationships>')

        with zipfile.ZipFile(pfad, "w", zipfile.ZIP_DEFLATED) as z:
            z.writestr("[Content_Types].xml", ct)
            z.writestr("_rels/.rels", rels)
            z.writestr("word/_rels/document.xml.rels", drels)
            z.writestr("word/document.xml", self._document_xml())
            z.writestr("word/styles.xml", self._styles_xml())
            z.writestr("word/settings.xml", self._settings_xml())
            z.writestr("word/footer1.xml", self._footer_xml())
        return pfad
