"""
Bringt das Band-5-Vollcover (Rueckseite + Buchruecken + Vorderseite als EIN Bild)
auf das exakte KDP-Druckmass und erzeugt das druckfertige PDF.

Buch: Die Geisterspuerer Band 5 – Der Schleier
Format: 6 x 9 Zoll Taschenbuch, 104 Seiten, WEISSES Papier
KDP-Vollcover-Sollmass:  12.484 x 9.250 Zoll = 3745 x 2775 px @ 300 dpi

Abgeleitet von build_cover_kdp_band4.py. Aenderungen:
  - PAGES 97 -> 104  (=> Buchruecken 0.234 Zoll / 5.9 mm statt 0.218 Zoll)
  - Pfade Band4 -> Band5
  - ★ NEU: Buchruecken-Pruefung (pruefe_buchruecken).

★ WARUM DIE BUCHRUECKEN-PRUEFUNG NEU IST
  Das Band-4-Skript prueft nur Seitenverhaeltnis und Aufloesung des Gesamtbilds.
  Es prueft NICHT, ob der im Bild GEMALTE Buchruecken so breit ist, wie KDP ihn
  erwartet. Beim ersten Band-5-Vollcover war er **dreimal zu breit** (5.84 % der
  Bildbreite statt 1.88 %). Folge im Druck: KDP faltet an der rechnerischen
  Position — mitten in die dunkle Rueckenflaeche hinein. Der Ruecken-Balken
  liefe dann sichtbar auf Vorder- und Rueckseite weiter, und der Rueckentext
  saesse nicht mittig auf dem Ruecken.
  Diese Pruefung misst die flache (varianzarme) Spalte in der Bildmitte und
  vergleicht sie mit dem Sollwert.

Verwendung:
    py Scripts/build_cover_kdp_band5.py                      # Standard-Eingabe
    py Scripts/build_cover_kdp_band5.py "Pfad/zu/cover.png"  # eigenes Bild
"""

import os
import sys
import fitz  # PyMuPDF

# ── KDP-Sollmass Band 5 (6x9, 104 Seiten, weisses Papier) ─────────────────────
DPI        = 300
BLEED      = 0.125          # Beschnitt rundum (Zoll)
TRIM_W     = 6.0            # Buchbreite (Zoll)
TRIM_H     = 9.0            # Buchhoehe (Zoll)
PAGES      = 104
PAPER_FACTOR = 0.002252     # WEISSES Papier (creme waere 0.0025)

SPINE_IN   = PAGES * PAPER_FACTOR                         # 0.2342
COVER_W_IN = BLEED + TRIM_W + SPINE_IN + TRIM_W + BLEED   # 12.484
COVER_H_IN = BLEED + TRIM_H + BLEED                       # 9.250

TARGET_W_PX = round(COVER_W_IN * DPI)     # 3745
TARGET_H_PX = round(COVER_H_IN * DPI)     # 2775
TARGET_RATIO = TARGET_W_PX / TARGET_H_PX  # 1.3495

SPINE_FRACTION = SPINE_IN / COVER_W_IN    # 0.0188 = 1.88 % der Breite

# ── Pfade ─────────────────────────────────────────────────────────────────────
_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DEFAULT_INPUT = os.path.join(_ROOT, "Band5", "Cover", "cover_V1_gesammt.png")
OUTPUT_DIR = os.path.join(_ROOT, "Output", "Band5")
OUTPUT_PDF = os.path.join(OUTPUT_DIR, "KDP_Band5_Cover_Vollcover_300dpi.pdf")
OUTPUT_JPG = os.path.join(OUTPUT_DIR, "KDP_Band5_Cover_Vollcover_300dpi.jpg")

RATIO_TOLERANCE = 0.01    # ab dieser Abweichung wird gewarnt (Verzerrungsgefahr)
SPINE_TOLERANCE = 0.006   # +-0.6 Prozentpunkte Rueckenbreite


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


def pruefe_buchruecken(path):
    """★ Misst die im Bild gemalte Buchruecken-Breite und vergleicht mit dem Soll.

    Der Buchruecken ist die vertikal FLACHESTE Spalte der Bildmitte (eine
    gleichmaessige Farbflaeche hat kaum vertikale Streuung). Gibt einen
    Warntext zurueck oder None.
    """
    try:
        from PIL import Image
        import numpy as np
    except ImportError:
        return None  # Pruefung optional – ohne Pillow/numpy einfach ueberspringen

    a = np.array(Image.open(path).convert("RGB")).astype(float)
    h, w, _ = a.shape
    var = a.std(axis=0).mean(axis=1)          # vertikale Streuung je Spalte
    lo, hi = int(w * 0.44), int(w * 0.56)     # nur die Bildmitte betrachten
    v = var[lo:hi]
    flach = [i + lo for i, x in enumerate(v) if x < v.min() + 8]
    if not flach:
        return None

    ist_px = flach[-1] - flach[0] + 1
    ist_frac = ist_px / w
    soll_px = w * SPINE_FRACTION
    mitte_ist = (flach[0] + flach[-1]) / 2
    versatz_px = abs(mitte_ist - w / 2)

    meldungen = []
    if abs(ist_frac - SPINE_FRACTION) > SPINE_TOLERANCE:
        faktor = ist_frac / SPINE_FRACTION
        meldungen.append(
            f"BUCHRUECKEN im Bild ist {faktor:.1f}x zu "
            f"{'breit' if faktor > 1 else 'schmal'}: gemalt {ist_px} px "
            f"({ist_frac*100:.2f} % der Breite), Soll ~{soll_px:.0f} px "
            f"({SPINE_FRACTION*100:.2f} %). KDP faltet an der RECHNERISCHEN "
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


def main():
    in_path = sys.argv[1] if len(sys.argv) > 1 else DEFAULT_INPUT
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    if not os.path.exists(in_path):
        print(f"FEHLER: Eingabebild nicht gefunden: {in_path}")
        sys.exit(1)

    print("=" * 64)
    print("KDP-Vollcover Band 5 – Der Schleier")
    print("=" * 64)
    print(f"Sollmass: {TARGET_W_PX} x {TARGET_H_PX} px  "
          f"({COVER_W_IN:.3f} x {COVER_H_IN:.3f} Zoll @ {DPI} dpi)")
    print(f"Buchruecken: {SPINE_IN:.3f} Zoll ({SPINE_IN*25.4:.1f} mm) bei "
          f"{PAGES} Seiten, weisses Papier")
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

    spine_msgs = pruefe_buchruecken(in_path)
    if spine_msgs:
        warnings.extend(spine_msgs)

    if warnings:
        print("!! WARNUNGEN:")
        for w_ in warnings:
            print("   - " + w_)
        print()
    else:
        print("OK: Verhaeltnis, Aufloesung und Buchruecken passen – "
              "verlustfreie Einpassung.")
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
        print("ACHTUNG: Es gab Warnungen (siehe oben). Das PDF ist masslich korrekt")
        print("fuer KDP, aber NICHT unbedingt druckreif. Warnungen zuerst beheben.")
        print()
        print(">> AUSSERDEM MANUELL PRUEFEN (kann kein Skript):")
        print("   Steht auf dem BUCHRUECKEN der richtige Titel?")
        print("   Band 5 muss 'Der Schleier' heissen - im ersten Entwurf stand")
        print("   dort faelschlich 'Die Zugemauerte Tuer' (= Band 4).")


if __name__ == "__main__":
    main()
