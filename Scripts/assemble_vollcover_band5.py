"""
Setzt das KDP-Vollcover fuer Band 5 EXAKT zusammen:
Rueckseite | Buchruecken (berechnet) | Vorderseite  ->  3745 x 2775 px @ 300 dpi

WARUM ES DIESES SKRIPT GIBT
---------------------------
Buchruecken-Breite und die maximale Hoehe der Ruecken-Schrift sind KEINE
Design-Entscheidungen, sondern ergeben sich zwingend aus der Seitenzahl:

    Ruecken       = Seiten x 0.002252 Zoll   (weisses Papier)
    Text-Freiraum = 0.0625 Zoll je Seite     (KDP-Vorgabe)
    Textbreite    = Ruecken - 2 x Freiraum

Bei 104 Seiten sind das 5.9 mm Ruecken und nur 2.8 mm (32 px) nutzbare
Texthoehe. Von Hand oder per Bildgenerator wurde das dreimal in Folge
verfehlt (Ruecken 3.2x zu breit, Schrift 2.7x zu gross). Deshalb rechnet
und zeichnet dieses Skript den Ruecken selbst.

WAS ES TUT
----------
1. Findet im vorhandenen Vollcover den gemalten Ruecken-Balken
   (varianzaermste Spalte der Bildmitte) und schneidet links davon die
   RUECKSEITE, rechts davon die VORDERSEITE heraus.
2. Skaliert beide auf exakt 1837/1838 x 2775 px.
3. Zeichnet dazwischen einen 70 px breiten Ruecken in der Farbe des
   Originalbalkens und setzt den Ruecken-Text um 90 Grad gedreht,
   automatisch auf die erlaubte Hoehe begrenzt.
4. Speichert das Ergebnis als PNG -> danach build_cover_kdp_band5.py.

Verwendung:
    py Scripts/assemble_vollcover_band5.py
    py Scripts/assemble_vollcover_band5.py "Pfad/zum/vollcover.png"
"""

import os
import sys
from PIL import Image, ImageDraw, ImageFont
import numpy as np

# ── KDP-Sollmasse (identisch zu build_cover_kdp_band5.py) ────────────────────
DPI          = 300
BLEED        = 0.125
TRIM_W       = 6.0
TRIM_H       = 9.0
PAGES        = 104
PAPER_FACTOR = 0.002252        # weisses Papier
SPINE_MARGIN = 0.0625          # KDP: Freiraum je Seite neben Ruecken-Text

SPINE_IN   = PAGES * PAPER_FACTOR
COVER_W_IN = BLEED + TRIM_W + SPINE_IN + TRIM_W + BLEED
COVER_H_IN = BLEED + TRIM_H + BLEED

TARGET_W  = round(COVER_W_IN * DPI)          # 3745
TARGET_H  = round(COVER_H_IN * DPI)          # 2775
SPINE_PX  = round(SPINE_IN * DPI)            # 70
SIDE_W    = (TARGET_W - SPINE_PX) // 2       # 1837
TEXT_MAX  = round((SPINE_IN - 2 * SPINE_MARGIN) * DPI)   # 32

# ── Ruecken-Text ─────────────────────────────────────────────────────────────
SPINE_TEXT  = "Die Geisterspürer  ·  Der Schleier  ·  Benjamin Krug"
FONT_PATH   = r"C:\Windows\Fonts\georgia.ttf"
TEXT_COLOR  = (232, 230, 224)

_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DEFAULT_INPUT = os.path.join(_ROOT, "Band5", "Cover", "cover_V1_gesammt.png")
OUTPUT = os.path.join(_ROOT, "Band5", "Cover", "cover_KDP_assembled.png")


def finde_ruecken(img):
    """Gibt (x0, x1) des gemalten Ruecken-Balkens zurueck."""
    a = np.array(img.convert("RGB")).astype(float)
    w = a.shape[1]
    var = a.std(axis=0).mean(axis=1)
    lo, hi = int(w * 0.44), int(w * 0.56)
    v = var[lo:hi]
    flach = [i + lo for i, x in enumerate(v) if x < v.min() + 8]
    if not flach:
        raise SystemExit("FEHLER: Kein Ruecken-Balken gefunden.")
    return flach[0], flach[-1]


def ruecken_farbe(img, x0, x1):
    a = np.array(img.convert("RGB"))
    streifen = a[:, x0:x1 + 1].reshape(-1, 3)
    return tuple(int(c) for c in np.median(streifen, axis=0))


def zeichne_ruecken(hoehe, farbe):
    """Baut den Ruecken-Streifen inkl. gedrehtem Text in erlaubter Groesse."""
    strip = Image.new("RGB", (SPINE_PX, hoehe), farbe)

    # Text waagerecht auf Hilfsbild zeichnen, dann drehen.
    # Schriftgroesse so waehlen, dass die HOEHE des Textes <= TEXT_MAX bleibt.
    size = TEXT_MAX
    font = None
    while size > 6:
        try:
            font = ImageFont.truetype(FONT_PATH, size)
        except OSError:
            font = ImageFont.load_default()
            break
        box = font.getbbox(SPINE_TEXT)
        if (box[3] - box[1]) <= TEXT_MAX:
            break
        size -= 1

    box = font.getbbox(SPINE_TEXT)
    tw, th = box[2] - box[0], box[3] - box[1]

    # Laenge begrenzen: Text darf hoechstens 70 % der Buchhoehe einnehmen
    max_len = int(hoehe * 0.70)
    while tw > max_len and size > 6:
        size -= 1
        font = ImageFont.truetype(FONT_PATH, size)
        box = font.getbbox(SPINE_TEXT)
        tw, th = box[2] - box[0], box[3] - box[1]

    hilf = Image.new("RGB", (tw + 4, th + 4), farbe)
    ImageDraw.Draw(hilf).text((2 - box[0], 2 - box[1]), SPINE_TEXT,
                              font=font, fill=TEXT_COLOR)
    hilf = hilf.rotate(90, expand=True)

    x = (SPINE_PX - hilf.width) // 2
    y = (hoehe - hilf.height) // 2
    strip.paste(hilf, (max(x, 0), y))
    return strip, size, th


def main():
    src_path = sys.argv[1] if len(sys.argv) > 1 else DEFAULT_INPUT
    if not os.path.exists(src_path):
        raise SystemExit(f"FEHLER: nicht gefunden: {src_path}")

    print("=" * 64)
    print("Vollcover ZUSAMMENSETZEN – Band 5 (Der Schleier)")
    print("=" * 64)
    print(f"Ziel      : {TARGET_W} x {TARGET_H} px @ {DPI} dpi")
    print(f"Ruecken   : {SPINE_PX} px ({SPINE_IN*25.4:.1f} mm) bei {PAGES} Seiten")
    print(f"Texthoehe : max {TEXT_MAX} px ({(SPINE_IN-2*SPINE_MARGIN)*25.4:.1f} mm) "
          f"– KDP verlangt {SPINE_MARGIN*25.4:.1f} mm Freiraum je Seite")
    print(f"Seiten    : je {SIDE_W} px breit")
    print()

    src = Image.open(src_path).convert("RGB")
    print(f"Eingabe: {os.path.basename(src_path)}  ({src.width} x {src.height})")

    x0, x1 = finde_ruecken(src)
    farbe = ruecken_farbe(src, x0, x1)
    print(f"  gemalter Ruecken gefunden: x={x0}..{x1} ({x1-x0+1} px), Farbe RGB{farbe}")

    back = src.crop((0, 0, x0, src.height)).resize((SIDE_W, TARGET_H), Image.LANCZOS)
    front = src.crop((x1 + 1, 0, src.width, src.height)).resize(
        (TARGET_W - SPINE_PX - SIDE_W, TARGET_H), Image.LANCZOS)
    print(f"  Rueckseite : {x0} px -> {back.width} px")
    print(f"  Vorderseite: {src.width-x1-1} px -> {front.width} px")

    strip, size, th = zeichne_ruecken(TARGET_H, farbe)
    print(f"  Ruecken neu gezeichnet: Schriftgrad {size} pt, Texthoehe {th} px "
          f"(erlaubt {TEXT_MAX})")

    out = Image.new("RGB", (TARGET_W, TARGET_H))
    out.paste(back, (0, 0))
    out.paste(strip, (SIDE_W, 0))
    out.paste(front, (SIDE_W + SPINE_PX, 0))
    out.save(OUTPUT)

    print()
    print("=" * 64)
    print(f"Gespeichert: {OUTPUT}")
    print(f"  {out.width} x {out.height} px")
    print()
    print("NAECHSTER SCHRITT:")
    print(f'  py Scripts/build_cover_kdp_band5.py "{OUTPUT}"')
    print("  -> muss jetzt OHNE Warnungen durchlaufen.")


if __name__ == "__main__":
    main()
