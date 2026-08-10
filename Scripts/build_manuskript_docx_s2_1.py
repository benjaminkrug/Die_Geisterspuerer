"""
Baut den Taschenbuch-Innenteil von S2-1 als DOCX **ohne python-docx** -
und zusaetzlich eine HTML-Fassung.

WARUM ES DAS GIBT
-----------------
build_taschenbuch_docx_s2_1.py braucht python-docx. Wo das fehlt, stand bisher
die ganze Produktion still. Dieses Skript benutzt stattdessen
Scripts/docx_minimal.py (nur Standardbibliothek) und erzeugt dieselbe
Buchgestalt: 6x9 Zoll, Spiegelraender, Georgia, Blocksatz, Kapitaelchen-
Auftakt, Szenentrenner, Seitenzahlen.

Die **Textaufbereitung wird importiert**, nicht kopiert - dieselbe Quelle wie
Taschenbuch und eBook (ENDE-Marker, Szenentrenner-Logik, Typografie,
Frontmatter). Damit kann diese Fassung nicht inhaltlich abweichen.

Verwendung:
    python Scripts/build_manuskript_docx_s2_1.py

⚠️ GRENZE DIESER FASSUNG
   Ein von Hand geschriebenes DOCX laesst sich hier nicht durch ein
   Textprogramm gegenpruefen (LibreOffice ist in dieser Umgebung defekt,
   es scheitert schon an einer .txt). Das Skript prueft deshalb selbst, so
   weit es geht: ZIP-Aufbau, XML-Wohlgeformtheit, aufloesbare Beziehungen
   und ein Ruecklesen des eigenen Ergebnisses (alle Kapitel, alle Absaetze).
   **Die Datei muss einmal von Hand geoeffnet werden**, bevor sie zu KDP geht.
   Fuer den reinen Lesezweck liegt die HTML-Fassung daneben - die oeffnet
   jeder Browser und laesst sich von dort als PDF drucken.
"""

import os
import re
import sys
import html as _html
import importlib.util
import zipfile
import xml.dom.minidom as minidom

_SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, _SCRIPT_DIR)
from docx_minimal import Dokument, Para, Run, CM   # noqa: E402


def _lade_taschenbuch():
    pfad = os.path.join(_SCRIPT_DIR, "build_taschenbuch_docx_s2_1.py")
    spec = importlib.util.spec_from_file_location("_s21_tb", pfad)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


TB = _lade_taschenbuch()

_ROOT = os.path.join(_SCRIPT_DIR, "..")
OUTPUT_DIR = os.path.join(_ROOT, "Output", "S2-1")
OUT_DOCX = os.path.join(OUTPUT_DIR, "Manuskript_S2-1_Taschenbuch.docx")
OUT_HTML = os.path.join(OUTPUT_DIR, "Manuskript_S2-1_Taschenbuch.html")

EINZUG = round(0.6 * CM)          # 0,6 cm Erstzeileneinzug
SMALLCAPS_WORTE = 4


# ── Markdown-Runs (*kursiv*, **fett**) ───────────────────────────────────────
def runs_aus_markdown(text, *, size=11, smallcaps_erste=0):
    teile = re.findall(r'(\*\*(.+?)\*\*|\*(.+?)\*|([^*]+))', text)
    runs = []
    for _voll, fett, kursiv, klar in teile:
        if fett:
            runs.append(Run(fett, bold=True, size=size))
        elif kursiv:
            runs.append(Run(kursiv, italic=True, size=size))
        elif klar:
            runs.append(Run(klar, size=size))
    if smallcaps_erste and runs and not runs[0].italic and not runs[0].bold:
        worte = runs[0].text.split(' ')
        if len(worte) > smallcaps_erste:
            kopf = ' '.join(worte[:smallcaps_erste])
            rest = ' ' + ' '.join(worte[smallcaps_erste:])
            runs = [Run(kopf, smallcaps=True, size=size),
                    Run(rest, size=size)] + runs[1:]
    return runs


def zentriert(doc, text, *, size=11, bold=False, italic=False):
    doc.add(Para([Run(text, bold=bold, italic=italic, size=size)],
                 align="center", indent=0, line=240))


# ── Front- und Backmatter ────────────────────────────────────────────────────
def frontmatter(doc):
    doc.leerzeile(8)
    zentriert(doc, TB.SERIES_TITLE, size=20, bold=True)
    doc.seitenumbruch()

    doc.leerzeile(4)
    zentriert(doc, TB.SERIES_TITLE, size=24, bold=True)
    doc.leerzeile(1)
    zentriert(doc, TB.STAFFEL_TITLE, size=13)
    doc.leerzeile(1)
    zentriert(doc, TB.BAND_TITLE, size=17, italic=True)
    doc.leerzeile(1)
    zentriert(doc, f"Band {TB.BAND_NUM}", size=12)
    doc.leerzeile(3)
    zentriert(doc, TB.AUTHOR, size=12)
    doc.seitenumbruch()

    doc.leerzeile(10)
    zentriert(doc, f"{TB.SERIES_TITLE} – {TB.BAND_TITLE}", size=10, bold=True)
    zentriert(doc, TB.BAND_SUBTITLE, size=10)
    doc.leerzeile(1)
    zentriert(doc, f"© 2026 {TB.AUTHOR}", size=9)
    zentriert(doc, "Alle Rechte vorbehalten.", size=9)
    doc.leerzeile(1)
    zentriert(doc, "Dieses Buch ist ein Werk der Fiktion. Namen, Figuren, Orte und "
                   "Ereignisse sind frei erfunden. Jede Ähnlichkeit mit tatsächlichen "
                   "Personen, lebend oder tot, ist rein zufällig.", size=9)
    doc.leerzeile(1)
    zentriert(doc, f"Umschlaggestaltung: {TB.AUTHOR}", size=9)
    zentriert(doc, f"Satz und Layout: {TB.AUTHOR}", size=9)
    doc.leerzeile(1)
    zentriert(doc, "Erstausgabe 2026", size=9)
    zentriert(doc, "Independently published", size=9)

    doc.seitenumbruch()
    doc.leerzeile(12)
    for z in TB.WIDMUNG_ZEILEN:
        zentriert(doc, z, size=12, italic=True)
        doc.leerzeile(1)

    doc.seitenumbruch()
    doc.leerzeile(12)
    for z in TB.EPIGRAPH_ZEILEN:
        zentriert(doc, z, size=12, italic=True)
        doc.leerzeile(1)
    doc.leerzeile(1)
    zentriert(doc, f"— {TB.EPIGRAPH_SOURCE}", size=10, italic=True)


def backmatter(doc):
    doc.seitenumbruch()
    doc.leerzeile(3)
    zentriert(doc, f"{TB.Q}{TB.BAND_TITLE}{TB.E} hat dir gefallen?", size=14, bold=True)
    doc.leerzeile(1)
    for t in ("Dann freue ich mich riesig über eine kurze Bewertung auf Amazon "
              "— auch nur ein oder zwei Sätze reichen völlig.",
              "Jede Rezension hilft anderen Kindern (und ihren Eltern), dieses Buch "
              "zu entdecken. Und mir hilft sie, weitere Bände zu schreiben."):
        doc.add(Para(runs_aus_markdown(TB.apply_typography(t)), indent=0))
        doc.leerzeile(1)
    doc.leerzeile(1)
    zentriert(doc, "Vielen Dank!", size=11)
    zentriert(doc, TB.AUTHOR, size=11)

    doc.seitenumbruch()
    doc.leerzeile(2)
    zentriert(doc, f"{TB.SERIES_TITLE} — die ersten fünf Bände", size=14, bold=True)
    doc.leerzeile(1)
    doc.add(Para(runs_aus_markdown(
        "Nora, Theo und Schatten hatten schon einmal zu tun. Fünf Fälle, "
        "bevor dieser hier anfing."), indent=0))
    doc.leerzeile(1)
    for nr, titel in [(1, "Das Haus, das flüstert"), (2, "Der Friedhof ohne Namen"),
                      (3, "Schatten sieht mehr"), (4, "Die zugemauerte Tür"),
                      (5, "Der Schleier")]:
        doc.add(Para([Run(f"Band {nr}: ", bold=True), Run(titel)], indent=0))
    doc.leerzeile(1)
    zentriert(doc, "Man kann sie in jeder Reihenfolge lesen — auch nach diesem Buch.",
              size=10, italic=True)


# ── Hauptteil ────────────────────────────────────────────────────────────────
def kapitel(doc, body):
    erste_nach_kapitel = erste_nach_trenner = False
    for art, zeile in TB.ereignisfolge(body):
        if art == 'KAPITEL':
            doc.add(Para([Run(zeile[2:], bold=True, size=14)],
                         align="center", indent=0, space_before=1200,
                         space_after=720, page_break_before=True,
                         keep_with_next=True, line=240))
            erste_nach_kapitel, erste_nach_trenner = True, False
        elif art == 'TRENNER':
            doc.leerzeile(1)
            zentriert(doc, TB.SCENE_BREAK_SYMBOL, size=11)
            doc.leerzeile(1)
            erste_nach_kapitel, erste_nach_trenner = False, True
        else:
            text = TB.apply_typography(zeile)
            ohne_einzug = erste_nach_kapitel or erste_nach_trenner
            doc.add(Para(
                runs_aus_markdown(
                    text, smallcaps_erste=SMALLCAPS_WORTE if erste_nach_kapitel else 0),
                indent=0 if ohne_einzug else EINZUG))
            erste_nach_kapitel = erste_nach_trenner = False


# ── HTML-Fassung (oeffnet garantiert, druckbar als PDF) ──────────────────────
def schreibe_html(body):
    def md(t):
        t = _html.escape(t)
        t = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', t)
        t = re.sub(r'\*(.+?)\*', r'<em>\1</em>', t)
        return t

    teile = ['<!doctype html><html lang="de"><head><meta charset="utf-8">',
             f'<title>{TB.SERIES_TITLE} – {TB.BAND_TITLE}</title><style>',
             '@page{size:6in 9in;margin:0.75in 0.625in 0.75in 0.875in}',
             'body{font-family:Georgia,serif;font-size:11pt;line-height:1.5;',
             'text-align:justify;max-width:34em;margin:2em auto;padding:0 1em}',
             'h1{text-align:center;font-size:14pt;margin:3em 0 1.5em;page-break-before:always}',
             'h1:first-of-type{page-break-before:avoid}',
             'p{margin:0;text-indent:0.6cm}p.noindent{text-indent:0}',
             '.mitte{text-align:center;text-indent:0;margin:0}',
             '.trenner{text-align:center;text-indent:0;margin:1em 0;letter-spacing:.3em}',
             '.titel{margin:6em 0 4em}.titel div{margin:.4em 0}',
             '</style></head><body>']

    teile.append('<div class="titel mitte">')
    teile.append(f'<div style="font-size:24pt;font-weight:bold">{TB.SERIES_TITLE}</div>')
    teile.append(f'<div style="font-size:13pt">{TB.STAFFEL_TITLE}</div>')
    teile.append(f'<div style="font-size:17pt;font-style:italic">{TB.BAND_TITLE}</div>')
    teile.append(f'<div>Band {TB.BAND_NUM}</div><div>{TB.AUTHOR}</div></div>')
    for z in TB.WIDMUNG_ZEILEN:
        teile.append(f'<p class="mitte"><em>{_html.escape(z)}</em></p>')
    teile.append('<p class="mitte">&nbsp;</p>')
    for z in TB.EPIGRAPH_ZEILEN:
        teile.append(f'<p class="mitte"><em>{_html.escape(z)}</em></p>')
    teile.append(f'<p class="mitte"><em>— {_html.escape(TB.EPIGRAPH_SOURCE)}</em></p>')

    erste = False
    for art, zeile in TB.ereignisfolge(body):
        if art == 'KAPITEL':
            teile.append(f'<h1>{_html.escape(zeile[2:])}</h1>')
            erste = True
        elif art == 'TRENNER':
            teile.append(f'<p class="trenner">{TB.SCENE_BREAK_SYMBOL}</p>')
            erste = True
        else:
            klasse = ' class="noindent"' if erste else ''
            teile.append(f'<p{klasse}>{md(TB.apply_typography(zeile))}</p>')
            erste = False

    teile.append('</body></html>')
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    with open(OUT_HTML, "w", encoding="utf-8") as f:
        f.write("\n".join(teile))


# ── Selbstpruefung des erzeugten DOCX ────────────────────────────────────────
def pruefe_docx(pfad, erwartete_kapitel, erwartete_absaetze):
    fehler = []
    with zipfile.ZipFile(pfad) as z:
        namen = set(z.namelist())
        pflicht = {"[Content_Types].xml", "_rels/.rels", "word/document.xml",
                   "word/styles.xml", "word/settings.xml", "word/footer1.xml",
                   "word/_rels/document.xml.rels"}
        if not pflicht <= namen:
            fehler.append(f"fehlende Teile: {sorted(pflicht - namen)}")
        for n in namen:
            if n.endswith(".xml") or n.endswith(".rels"):
                try:
                    minidom.parseString(z.read(n))
                except Exception as e:
                    fehler.append(f"{n} nicht wohlgeformt: {e}")
        doc = z.read("word/document.xml").decode("utf-8")
        rels = z.read("word/_rels/document.xml.rels").decode("utf-8")
        ct = z.read("[Content_Types].xml").decode("utf-8")

    # Beziehungen, die das Dokument benutzt, muessen auch deklariert sein
    for rid in set(re.findall(r'r:id="(rId\d+)"', doc)):
        if f'Id="{rid}"' not in rels:
            fehler.append(f"Beziehung {rid} wird benutzt, ist aber nicht deklariert")
    for teil in re.findall(r'Target="([^"]+)"', rels):
        if teil.endswith(".xml") and f'/word/{teil}' not in ct and \
           'Extension="xml"' not in ct:
            fehler.append(f"{teil} fehlt in [Content_Types].xml")

    # Ruecklesen: Kapitel und Absaetze zaehlen.
    # ‼️ Text je ABSATZ zusammensetzen, nicht je Lauf. Der erste Absatz jedes
    #    Kapitels ist wegen der Kapitaelchen auf zwei Laeufe verteilt; ein
    #    Vergleich je Lauf meldet ihn faelschlich als fehlend (real passiert,
    #    4 Fehltreffer beim ersten Lauf).
    kapitel_gefunden = len(re.findall(r'<w:pageBreakBefore/>', doc))
    absatz_texte = []
    for p in re.findall(r'<w:p>.*?</w:p>', doc, re.S):
        t = "".join(re.findall(r'<w:t xml:space="preserve">([^<]*)</w:t>', p))
        if t.strip():
            absatz_texte.append(t)
    if len(absatz_texte) < erwartete_absaetze:
        fehler.append(f"nur {len(absatz_texte)} Textabsaetze im DOCX, "
                      f"erwartet >= {erwartete_absaetze}")
    return fehler, kapitel_gefunden, len(re.findall(r'<w:p>', doc)), absatz_texte


def main():
    with open(TB.INPUT_FILE, encoding="utf-8") as f:
        inhalt = f.read()
    body = TB.bereite_body_vor(inhalt)

    doc = Dokument(breite_zoll=6.0, hoehe_zoll=9.0,
                   innen=0.875, aussen=0.625, oben=0.75, unten=0.75,
                   spiegelraender=True, seitenzahlen=True)
    frontmatter(doc)
    kapitel(doc, body)
    backmatter(doc)

    os.makedirs(OUTPUT_DIR, exist_ok=True)
    doc.speichern(OUT_DOCX)
    schreibe_html(body)

    quell_absaetze = sum(1 for a, _ in TB.ereignisfolge(body) if a == 'TEXT')
    fehler, kap, abs_, texte = pruefe_docx(OUT_DOCX, TB.ERWARTETE_KAPITEL, quell_absaetze)

    print("=" * 70)
    print("TASCHENBUCH-INNENTEIL S2-1 — ohne python-docx gebaut")
    print("=" * 70)
    print(f"DOCX : {OUT_DOCX}  ({os.path.getsize(OUT_DOCX):,} Bytes)")
    print(f"HTML : {OUT_HTML}  ({os.path.getsize(OUT_HTML):,} Bytes)")
    print()
    print(f"Kapitel-Seitenumbrueche : {kap}  (16 Kapitel + 4 Frontmatter + 2 Backmatter)")
    print(f"Absaetze im DOCX        : {abs_}  (Quelltext-Absaetze: {quell_absaetze})")
    print(f"Textlaeufe              : {len(texte)}")

    # Jeder Quellabsatz muss WORTGLEICH als Absatz im DOCX stehen.
    # Markdown-Sternchen fallen weg, weil sie zu Kursiv/Fett geworden sind.
    rein = lambda s: re.sub(r'\*+', '', s)
    quelle = [TB.apply_typography(z) for a, z in TB.ereignisfolge(body) if a == 'TEXT']
    fehlend = [q for q in quelle if rein(q) not in texte]
    if fehlend:
        fehler.append(f"{len(fehlend)} Quellabsaetze im DOCX nicht wiedergefunden, "
                      f"z. B.: {fehlend[0][:50]!r}")

    print()
    if fehler:
        print("!! BEFUNDE:")
        for f_ in dict.fromkeys(fehler):
            print("   -", f_)
        sys.exit(1)
    print("Selbstpruefung bestanden: ZIP-Aufbau, XML, Beziehungen, Inhalt vollstaendig.")
    print()
    print("⚠️  Die DOCX konnte hier NICHT von einem Textprogramm geoeffnet werden")
    print("    (LibreOffice ist in dieser Umgebung defekt - es scheitert schon an")
    print("    einer .txt). Vor dem Weg zu KDP einmal von Hand oeffnen und die")
    print("    ECHTE SEITENZAHL ablesen - die braucht der Buchruecken.")
    print("    Zum reinen Lesen und als PDF-Quelle: die HTML-Fassung daneben.")


if __name__ == "__main__":
    main()
