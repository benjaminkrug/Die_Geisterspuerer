"""
Bringt das Band-4-Vollcover (Rueckseite + Buchruecken + Vorderseite als EIN Bild)
auf das exakte KDP-Druckmass und erzeugt das druckfertige PDF.

Buch: Die Geisterspuerer Band 4 – Die zugemauerte Tuer
Format: 6 x 9 Zoll Taschenbuch, 95 Seiten, WEISSES Papier
KDP-Vollcover-Sollmass:  12.468 x 9.250 Zoll = 3741 x 2775 px @ 300 dpi

Abgeleitet von build_cover_kdp_band3.py – einzige inhaltliche Aenderung: PAGES 107 -> 97
(=> schmalerer Buchruecken: 0.218 Zoll / 5.5 mm statt 0.241 Zoll).
Prueft Seitenverhaeltnis + Aufloesung des Eingabebildes und warnt vor
Verzerrung/Unschaerfe, bevor eingepasst wird.

Verwendung:
    py build_cover_kdp_band4.py                      # nimmt Standard-Eingabe
    py build_cover_kdp_band4.py "Pfad/zu/cover.png"  # eigenes Bild
"""

import os
import sys
import fitz  # PyMuPDF

# ── KDP-Sollmass Band 4 (6x9, 97 Seiten, weisses Papier) ──────────────────────
DPI        = 300
BLEED      = 0.125          # Beschnitt rundum (Zoll)
TRIM_W     = 6.0            # Buchbreite (Zoll)
TRIM_H     = 9.0            # Buchhoehe (Zoll)
PAGES      = 95
PAPER_FACTOR = 0.002252     # WEISSES Papier (creme waere 0.0025)

SPINE_IN   = PAGES * PAPER_FACTOR
COVER_W_IN = BLEED + TRIM_W + SPINE_IN + TRIM_W + BLEED   # 12.468
COVER_H_IN = BLEED + TRIM_H + BLEED                       # 9.250

TARGET_W_PX = round(COVER_W_IN * DPI)   # 3741
TARGET_H_PX = round(COVER_H_IN * DPI)   # 2775
TARGET_RATIO = TARGET_W_PX / TARGET_H_PX  # 1.3481

# ── Pfade ─────────────────────────────────────────────────────────────────────
_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DEFAULT_INPUT = os.path.join(_ROOT, "Band4", "Cover", "cover_1_gesammt.png")
OUTPUT_DIR = os.path.join(_ROOT, "Output", "Band4")
OUTPUT_PDF = os.path.join(OUTPUT_DIR, "KDP_Band4_Cover_Vollcover_300dpi.pdf")
OUTPUT_JPG = os.path.join(OUTPUT_DIR, "KDP_Band4_Cover_Vollcover_300dpi.jpg")

RATIO_TOLERANCE = 0.01   # ab dieser Abweichung wird gewarnt (Verzerrungsgefahr)


def load_pixmap(path):
    """Laedt JPG/PNG/PDF als Pixmap (erste Seite bei PDF)."""
    ext = os.path.splitext(path)[1].lower()
    if ext == ".pdf":
        doc = fitz.open(path)
        page = doc[0]
        zoom = max(TARGET_W_PX / page.rect.width, TARGET_H_PX / page.rect.height)
        pix = page.get_pixmap(matrix=fitz.Matrix(zoom, zoom))
        doc.close()
        return pix
    return fitz.Pixmap(path)


def main():
    in_path = sys.argv[1] if len(sys.argv) > 1 else DEFAULT_INPUT
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    if not os.path.exists(in_path):
        print(f"FEHLER: Eingabebild nicht gefunden: {in_path}")
        sys.exit(1)

    print("=" * 64)
    print("KDP-Vollcover Band 4 – Die zugemauerte Tuer")
    print("=" * 64)
    print(f"Sollmass: {TARGET_W_PX} x {TARGET_H_PX} px  "
          f"({COVER_W_IN:.3f} x {COVER_H_IN:.3f} Zoll @ {DPI} dpi)")
    print(f"Buchruecken: {SPINE_IN:.3f} Zoll ({SPINE_IN*25.4:.1f} mm) bei {PAGES} Seiten, weisses Papier")
    print()

    pix = load_pixmap(in_path)
    src_ratio = pix.width / pix.height
    print(f"Eingabe: {os.path.basename(in_path)}")
    print(f"  {pix.width} x {pix.height} px | Verhaeltnis {src_ratio:.4f} | @300dpi = "
          f"{pix.width/DPI:.2f} x {pix.height/DPI:.2f} Zoll")
    print()

    warnings = []

    if abs(src_ratio - TARGET_RATIO) > RATIO_TOLERANCE:
        warnings.append(
            f"SEITENVERHAELTNIS weicht ab: {src_ratio:.4f} vs. Ziel {TARGET_RATIO:.4f}. "
            f"Das Bild wird beim Einpassen VERZERRT (gestaucht/gestreckt). "
            f"Fuer perfekte Qualitaet das Bild im Verhaeltnis {TARGET_RATIO:.3f} "
            f"({TARGET_W_PX}x{TARGET_H_PX}px) neu erzeugen."
        )

    if pix.width < TARGET_W_PX or pix.height < TARGET_H_PX:
        eff_dpi = min(pix.width / COVER_W_IN, pix.height / COVER_H_IN)
        warnings.append(
            f"AUFLOESUNG zu niedrig: effektiv ~{eff_dpi:.0f} dpi (Soll 300). "
            f"Das Bild wird hochskaliert und kann im Druck unscharf wirken. "
            f"KDP empfiehlt mind. 300 dpi -> Bild mit {TARGET_W_PX}x{TARGET_H_PX}px erzeugen."
        )

    if warnings:
        print("!! WARNUNGEN:")
        for w in warnings:
            print("   - " + w)
        print()
    else:
        print("OK: Verhaeltnis und Aufloesung passen – verlustfreie Einpassung.")
        print()

    if (pix.width, pix.height) != (TARGET_W_PX, TARGET_H_PX):
        tmp = fitz.open()
        p = tmp.new_page(width=pix.width, height=pix.height)
        p.insert_image(fitz.Rect(0, 0, pix.width, pix.height), pixmap=pix)
        zoom_x = TARGET_W_PX / pix.width
        zoom_y = TARGET_H_PX / pix.height
        pix = p.get_pixmap(matrix=fitz.Matrix(zoom_x, zoom_y))
        tmp.close()

    print(f"Eingepasst auf: {pix.width} x {pix.height} px")

    jpeg_bytes = pix.tobytes("jpeg", jpg_quality=95)
    with open(OUTPUT_JPG, "wb") as f:
        f.write(jpeg_bytes)

    cover_w_pt = COVER_W_IN * 72
    cover_h_pt = COVER_H_IN * 72
    out = fitz.open()
    page = out.new_page(width=cover_w_pt, height=cover_h_pt)
    page.insert_image(fitz.Rect(0, 0, cover_w_pt, cover_h_pt), stream=jpeg_bytes)
    out.save(OUTPUT_PDF, deflate=True, garbage=4)
    out.close()

    chk = fitz.open(OUTPUT_PDF)
    r = chk[0].rect
    chk.close()
    print()
    print("=" * 64)
    print("ERGEBNIS")
    print("=" * 64)
    print(f"PDF: {OUTPUT_PDF}")
    print(f"  {r.width:.1f} x {r.height:.1f} pt = {r.width/72:.3f} x {r.height/72:.3f} Zoll "
          f"= {r.width/72*300:.0f} x {r.height/72*300:.0f} px @ 300 dpi")
    print(f"  Dateigroesse: {os.path.getsize(OUTPUT_PDF)/1024/1024:.1f} MB")
    print(f"JPG (Kontrolle): {OUTPUT_JPG}")
    if warnings:
        print()
        print("ACHTUNG: Es gab Warnungen (siehe oben). PDF ist masslich korrekt fuer KDP,")
        print("aber fuer beste Druckqualitaet das Bild neu erzeugen (Verhaeltnis/Aufloesung).")


if __name__ == "__main__":
    main()
