"""
Bringt das S2-1-Vollcover (Rueckseite + Buchruecken + Vorderseite als EIN Bild)
auf das exakte KDP-Druckmass und erzeugt das druckfertige PDF.

Buch:   Die Geisterspuerer · Die Gebundenen · Band 1 – "Der Gast, der blieb"
Format: 6 x 9 Zoll Taschenbuch, WEISSES Papier

Abgeleitet von build_cover_kdp_band5.py. Uebernommen: Seitenverhaeltnis-Pruefung,
Aufloesungs-Pruefung und die Buchruecken-Messung (die dort entstanden ist, weil
Band 5s erstes Vollcover einen dreimal zu breiten gemalten Ruecken hatte).

Verwendung:
    python Scripts/build_cover_kdp_s2_1.py --seiten 102
    python Scripts/build_cover_kdp_s2_1.py --seiten 102 "Pfad/zu/cover.png"


★ DER UNTERSCHIED ZU BAND 5: DIE SEITENZAHL IST PFLICHTARGUMENT

  Band 5 hatte PAGES = 104 fest im Skript — eine echte, abgelesene Zahl.
  Fuer S2-1 gibt es diese Zahl noch nicht: Das Taschenbuch-PDF ist ungebaut.
  Geschaetzt sind es ~102 Seiten (16.723 Woerter bei Ø 163,5 W/Seite, gemessen
  an Band 4 mit 164,2 und Band 5 mit 162,8).

  ‼️ Eine Schaetzung darf hier NICHT durchlaufen — aber nicht wegen der
  Millimeter: Zwei Seiten Differenz sind nur 0,11 mm Ruecken. Der Grund ist ein
  anderer und schwerer wiegender: **KDP prueft die Gesamtbreite des hochgeladenen
  Covers gegen die tatsaechliche Seitenzahl des hochgeladenen Manuskripts.**
  Stimmt beides nicht ueberein, wird das Cover abgelehnt — und die Schaetzung
  hier hat keine Fehlerspanne, weil sie aus nur zwei Datenpunkten (Band 4 und
  Band 5) stammt und stark davon abhaengt, wo die Kapitelumbrueche fallen. Bei
  16 statt 18 Kapiteln kann das mehrere Seiten ausmachen.

  Deshalb: kein Default. Ohne --seiten bricht das Skript ab und sagt, woher die
  Zahl kommt (aus dem fertigen Taschenbuch-PDF, nicht aus einer Rechnung).
"""

import os
import sys

try:
    import fitz  # PyMuPDF
except ImportError:
    print("!! PyMuPDF (fitz) ist nicht installiert — das Cover kann nicht gebaut werden.")
    print("   pip install pymupdf")
    sys.exit(2)

# ── KDP-Sollmass (6x9, weisses Papier) ────────────────────────────────────────
DPI          = 300
BLEED        = 0.125          # Beschnitt rundum (Zoll)
TRIM_W       = 6.0
TRIM_H       = 9.0
PAPER_FACTOR = 0.002252       # WEISSES Papier (creme waere 0.0025)

GESCHAETZTE_SEITEN = 102      # nur fuer die Fehlermeldung, NICHT als Default

RATIO_TOLERANCE = 0.01
SPINE_TOLERANCE = 0.006

_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
COVER_DIR = os.path.join(_ROOT, "Staffel2", "S2-1", "Cover")
DEFAULT_INPUT = os.path.join(COVER_DIR, "Bilder", "vollcover_s2_1.png")
OUTPUT_DIR = os.path.join(_ROOT, "Output", "S2-1")
OUTPUT_PDF = os.path.join(OUTPUT_DIR, "KDP_S2-1_Cover_Vollcover_300dpi.pdf")
OUTPUT_JPG = os.path.join(OUTPUT_DIR, "KDP_S2-1_Cover_Vollcover_300dpi.jpg")


def masse(pages: int) -> dict:
    spine_in = pages * PAPER_FACTOR
    cover_w_in = BLEED + TRIM_W + spine_in + TRIM_W + BLEED
    cover_h_in = BLEED + TRIM_H + BLEED
    return dict(
        spine_in=spine_in,
        cover_w_in=cover_w_in,
        cover_h_in=cover_h_in,
        w_px=round(cover_w_in * DPI),
        h_px=round(cover_h_in * DPI),
        ratio=(cover_w_in * DPI) / (cover_h_in * DPI),
        spine_fraction=spine_in / cover_w_in,
    )


def load_pixmap(path, m):
    ext = os.path.splitext(path)[1].lower()
    if ext == ".pdf":
        doc = fitz.open(path)
        page = doc[0]
        zoom = max(m['w_px'] / page.rect.width, m['h_px'] / page.rect.height)
        pix = page.get_pixmap(matrix=fitz.Matrix(zoom, zoom))
        doc.close()
        return pix
    return fitz.Pixmap(path)


def pruefe_buchruecken(path, m):
    """Misst die im Bild GEMALTE Buchruecken-Breite und vergleicht mit dem Soll.
    Der Ruecken ist die vertikal flachste Spalte der Bildmitte."""
    try:
        from PIL import Image
        import numpy as np
    except ImportError:
        return ["Buchruecken-Pruefung uebersprungen (Pillow/numpy fehlen). "
                "Das ist die Pruefung, die Band 5s dreimal zu breiten Ruecken "
                "gefunden hat — moeglichst nachholen."]

    a = np.array(Image.open(path).convert("RGB")).astype(float)
    h, w, _ = a.shape
    var = a.std(axis=0).mean(axis=1)
    lo, hi = int(w * 0.44), int(w * 0.56)
    v = var[lo:hi]
    flach = [i + lo for i, x in enumerate(v) if x < v.min() + 8]
    if not flach:
        return None

    ist_px = flach[-1] - flach[0] + 1
    ist_frac = ist_px / w
    soll_px = w * m['spine_fraction']
    mitte_ist = (flach[0] + flach[-1]) / 2
    versatz_px = abs(mitte_ist - w / 2)

    meldungen = []
    if abs(ist_frac - m['spine_fraction']) > SPINE_TOLERANCE:
        faktor = ist_frac / m['spine_fraction']
        meldungen.append(
            f"BUCHRUECKEN im Bild ist {faktor:.1f}x zu "
            f"{'breit' if faktor > 1 else 'schmal'}: gemalt {ist_px} px "
            f"({ist_frac*100:.2f} % der Breite), Soll ~{soll_px:.0f} px "
            f"({m['spine_fraction']*100:.2f} %). KDP faltet an der RECHNERISCHEN "
            f"Position – der Ruecken-Balken liefe sichtbar auf Vorder- und "
            f"Rueckseite weiter, der Rueckentext saesse nicht mittig."
        )
    if versatz_px > w * 0.005:
        meldungen.append(
            f"BUCHRUECKEN ist {versatz_px:.0f} px aus der Bildmitte versetzt "
            f"(Mitte bei x={mitte_ist:.0f}, Bildmitte x={w/2:.0f}). "
            f"Vorder- und Rueckseite werden dadurch ungleich breit."
        )
    return meldungen or None


def seiten_aus_argv():
    if "--seiten" in sys.argv:
        i = sys.argv.index("--seiten")
        if i + 1 < len(sys.argv):
            try:
                n = int(sys.argv[i + 1])
                if n > 0:
                    return n
            except ValueError:
                pass
    print("=" * 72)
    print("!! ABBRUCH — die Seitenzahl fehlt.")
    print("=" * 72)
    print("KDP prueft die Gesamtbreite des Covers gegen die tatsaechliche")
    print("Seitenzahl des Manuskripts. Stimmt beides nicht ueberein, wird das")
    print("Cover abgelehnt — und die Schaetzung unten hat keine Fehlerspanne.")
    print()
    print(f"Geschaetzt sind es ~{GESCHAETZTE_SEITEN} Seiten (16.723 Woerter bei")
    print("Ø 163,5 W/Seite). ‼️ Diese Schaetzung darf NICHT in den Druck.")
    print()
    print("Die echte Zahl steht im fertigen Taschenbuch-PDF:")
    print("    python Scripts/build_taschenbuch_docx_s2_1.py")
    print("Dann:")
    print(f"    python Scripts/build_cover_kdp_s2_1.py --seiten <echte Zahl>")
    sys.exit(1)


def main():
    pages = seiten_aus_argv()
    m = masse(pages)

    bilder = [a for a in sys.argv[1:]
              if not a.startswith("--") and not a.isdigit()]
    in_path = bilder[0] if bilder else DEFAULT_INPUT

    os.makedirs(OUTPUT_DIR, exist_ok=True)

    print("=" * 72)
    print("KDP-Vollcover — Die Gebundenen · Band 1 – Der Gast, der blieb")
    print("=" * 72)
    print(f"Sollmass: {m['w_px']} x {m['h_px']} px  "
          f"({m['cover_w_in']:.3f} x {m['cover_h_in']:.3f} Zoll @ {DPI} dpi)")
    print(f"Buchruecken: {m['spine_in']:.4f} Zoll ({m['spine_in']*25.4:.2f} mm) "
          f"bei {pages} Seiten, weisses Papier")
    if pages == GESCHAETZTE_SEITEN:
        print(f"⚠️  {pages} ist die GESCHAETZTE Zahl. Stammt sie wirklich aus dem")
        print( "    fertigen PDF? Wenn nicht: erst bauen, dann ablesen.")
    print()

    if not os.path.exists(in_path):
        print(f"FEHLER: Eingabebild nicht gefunden: {in_path}")
        print(f"        Erwartet wird das VOLLCOVER (Rueck + Ruecken + Vorderseite).")
        sys.exit(1)

    pix = load_pixmap(in_path, m)
    src_ratio = pix.width / pix.height
    print(f"Eingabe: {os.path.basename(in_path)}")
    print(f"  {pix.width} x {pix.height} px | Verhaeltnis {src_ratio:.4f} | @300dpi = "
          f"{pix.width/DPI:.2f} x {pix.height/DPI:.2f} Zoll")
    print()

    warnungen = []
    if abs(src_ratio - m['ratio']) > RATIO_TOLERANCE:
        warnungen.append(
            f"SEITENVERHAELTNIS weicht ab: {src_ratio:.4f} vs. Ziel {m['ratio']:.4f}. "
            f"Das Bild wird beim Einpassen VERZERRT. Besser im Verhaeltnis "
            f"{m['ratio']:.3f} ({m['w_px']}x{m['h_px']} px) neu erzeugen."
        )
    if pix.width < m['w_px'] or pix.height < m['h_px']:
        eff_dpi = min(pix.width / m['cover_w_in'], pix.height / m['cover_h_in'])
        warnungen.append(
            f"AUFLOESUNG zu niedrig: effektiv ~{eff_dpi:.0f} dpi (Soll 300). "
            f"Bild mit {m['w_px']}x{m['h_px']} px erzeugen."
        )
    spine_msgs = pruefe_buchruecken(in_path, m)
    if spine_msgs:
        warnungen.extend(spine_msgs)

    if warnungen:
        print("!! WARNUNGEN:")
        for w_ in warnungen:
            print("   - " + w_)
        print()
    else:
        print("OK: Verhaeltnis, Aufloesung und Buchruecken passen.")
        print()

    if (pix.width, pix.height) != (m['w_px'], m['h_px']):
        tmp = fitz.open()
        p = tmp.new_page(width=pix.width, height=pix.height)
        p.insert_image(fitz.Rect(0, 0, pix.width, pix.height), pixmap=pix)
        pix = p.get_pixmap(matrix=fitz.Matrix(m['w_px'] / pix.width,
                                              m['h_px'] / pix.height))
        tmp.close()

    print(f"Eingepasst auf: {pix.width} x {pix.height} px")

    jpeg_bytes = pix.tobytes("jpeg", jpg_quality=95)
    with open(OUTPUT_JPG, "wb") as f:
        f.write(jpeg_bytes)

    out = fitz.open()
    page = out.new_page(width=m['cover_w_in'] * 72, height=m['cover_h_in'] * 72)
    page.insert_image(fitz.Rect(0, 0, m['cover_w_in'] * 72, m['cover_h_in'] * 72),
                      stream=jpeg_bytes)
    out.save(OUTPUT_PDF, deflate=True, garbage=4)
    out.close()

    print(f"PDF : {OUTPUT_PDF}")
    print(f"JPG : {OUTPUT_JPG}")
    print()
    print("⚠️  Jetzt das Kontrollbild ansehen — nicht optional:")
    print("    Text innerhalb der Sicherheitslinie? Barcode-Feld leer?")
    print("    Rueckentitel richtig? Gemalter Ruecken so breit wie der rechnerische?")
    print("⚠️  Und den 150-px-Thumbnail: Titel, Tuerspalt, Bernsteinauge UND")
    print("    die Zeile 'DIE GEBUNDENEN · BAND 1' noch erkennbar?")


if __name__ == "__main__":
    main()
