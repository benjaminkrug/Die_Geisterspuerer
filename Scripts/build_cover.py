# -*- coding: utf-8 -*-
"""
Baut das KDP-Vollcover fuer EINEN Geisterspuerer-Band aus ZWEI Bildern
(Vorderseite + Rueckseite). Der Buchruecken wird berechnet und gezeichnet.

    py Scripts/build_cover.py 3
    py Scripts/build_cover.py 3 --front eigen.png --back eigen_back.png

WARUM ES DIESES SKRIPT GIBT
---------------------------
Band 1-4 wurden als EIN generiertes Bild gebaut und dann auf das KDP-Mass
gequetscht. Nachgemessen an den ausgelieferten Dateien:

    Band 3/4:  3410 x 2475 px  ->  eingepasst auf 3747 x 2775 px
               Verhaeltnis 1.378 statt 1.350  = 2 % horizontal gestaucht
               Hoehe 2475 statt 2775          = effektiv 267 statt 300 dpi

Beides ist im Druck. Dieses Skript macht beide Fehler unmoeglich:
  - Vorder- und Rueckseite werden PIXELGENAU an ihre KDP-Position gesetzt,
    nie verzerrt (immer proportional skaliert + mittig beschnitten).
  - Zu kleine Quellbilder fuehren zum ABBRUCH, nicht zu einer Warnung.
    (Das Band-5-Skript warnte nur -- und das Bild lief trotzdem durch.)

DER BUCHRUECKEN
---------------
Ruecken [Zoll] = Seitenzahl x 0.002252   (weisses Papier; creme = 0.0025)

Die Breite ist keine Design-Entscheidung. Sie ergibt sich aus der Seitenzahl,
und die Seitenzahl kommt aus dem KDP-Previewer -- NICHT aus einer Schaetzung.
Deshalb bricht das Skript ab, solange SEITEN_BESTAETIGT False ist.

Leserichtung: OBEN NACH UNTEN. Nachgemessen an den gedruckten Ruecken von
Band 2, 3, 4 und 5 -- alle vier laufen von oben nach unten. Massgeblich ist
das Regal, nicht die Konvention. (assemble_vollcover_band5.py drehte mit
rotate(90) andersherum; wer das kopiert, druckt den Ruecken auf dem Kopf.)

DAS SKRIPT PRUEFT SEINEN EIGENEN OUTPUT
---------------------------------------
Lehre aus dem Separator-Bug: ein Build, der nur "durchlaeuft", beweist nichts.
Am Ende wird das erzeugte PDF neu geoeffnet und vermessen, die Barcode-Zone
und der Beschnittrand werden auf Text/Details abgeklopft, und es faellt ein
KONTROLLBILD mit eingezeichneten Linien (Beschnitt / Trimm / Sicherheitsrand /
Barcode / Ruecken) sowie ein 150-px-Thumbnail an. Beides ansehen, bevor
irgendetwas zu KDP hochgeht.
"""
import argparse
import io
import os
import sys

import numpy as np
from PIL import Image, ImageDraw, ImageFont

# Buchtitel enthalten Umlaute ("Die Zugemauerte Tür") -- ohne das zeigt die
# Windows-Konsole "T?r" und der Ruecken-Check von Hand wird wertlos.
if hasattr(sys.stdout, "buffer"):
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")

# --------------------------------------------------------------------------
# KDP-KONSTANTEN (6 x 9 Zoll Taschenbuch)
# --------------------------------------------------------------------------
DPI = 300
BLEED = 0.125          # Anschnitt rundum, Zoll
TRIM_W, TRIM_H = 6.0, 9.0
PAPIER = {"weiss": 0.002252, "creme": 0.0025}

SAFE_TEXT = 0.25       # KDP: Textsicherheitsabstand zur Trimmkante, Zoll
SPINE_SAFE = 0.0625    # KDP: Freiraum je Ruecken-Seite, Zoll
BARCODE_W, BARCODE_H = 2.0, 1.2      # KDP-Barcode, Zoll
BARCODE_INSET = 0.25                 # Abstand von der Trimmkante, Zoll
MIN_SEITEN_RUECKENTEXT = 79          # darunter erlaubt KDP keinen Ruecken-Text

EBOOK_W, EBOOK_H = 1600, 2560        # KDP-eBook: 1:1.6, JPG oder TIFF

# --------------------------------------------------------------------------
# REIHEN-STANDARD (gilt fuer alle fuenf Baende)
# --------------------------------------------------------------------------
REIHE = "DIE GEISTERSPÜRER"
AUTOR = "Benjamin Krug"

GOLD = (0xD4, 0x92, 0x0B)      # Schattens Bernstein - Reihen-Akzent
CREME = (0xE8, 0xE6, 0xE0)     # Kalkweiss - Titelfarbe der Reihe
STAHL = (0x9A, 0xA6, 0xB0)     # Stahlgrau - Reihenzeile

FONT_TITEL = r"C:\Windows\Fonts\georgiab.ttf"
FONT_KLEIN = r"C:\Windows\Fonts\georgia.ttf"
FONT_FALLBACK = [
    r"C:\Windows\Fonts\georgiab.ttf",
    r"C:\Windows\Fonts\constanb.ttf",
    r"C:\Windows\Fonts\timesbd.ttf",
    "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf",
]

# --------------------------------------------------------------------------
# DIE BAENDE
# --------------------------------------------------------------------------
# SEITEN            : echte Seitenzahl aus dem KDP-Previewer
# SEITEN_BESTAETIGT : False -> Abbruch. Schuetzt davor, dass eine Schaetzung
#                     in den Druck laeuft (Band 3 hatte 105 geschaetzt und nie
#                     ersetzt).
# ruecken_bg        : None = Farbe aus den Bildraendern messen (empfohlen).
#                     Eine feste RGB-Tupel-Angabe uebersteuert das.
# --------------------------------------------------------------------------
BAENDE = {
    # Band 1 lief bisher als 5 x 8 Zoll -- als einziger Band der Reihe.
    # Umgestellt auf 6 x 9 am 2026-08-04: 186 -> 152 Seiten (gemessen am neu
    # gebauten PDF, nicht geschaetzt). 'bestaetigt' bleibt False, bis die Zahl
    # aus dem KDP-Previewer gegengelesen ist -- LibreOffice und KDP koennen
    # sich um eine Seite unterscheiden, und davon haengt der Buchruecken ab.
    1: dict(titel="Das Haus, das flüstert",       seiten=152, bestaetigt=False,
            papier="weiss", ruecken_bg=None),
    2: dict(titel="Der Friedhof ohne Namen",      seiten=113, bestaetigt=True,
            papier="weiss", ruecken_bg=None),
    3: dict(titel="Schatten sieht mehr",          seiten=106, bestaetigt=True,
            papier="weiss", ruecken_bg=None),
    4: dict(titel="Die Zugemauerte Tür",          seiten=95,  bestaetigt=True,
            papier="weiss", ruecken_bg=None),
    5: dict(titel="Der Schleier",                 seiten=104, bestaetigt=True,
            papier="weiss", ruecken_bg=None),
}

_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# --------------------------------------------------------------------------
# Hilfsfunktionen
# --------------------------------------------------------------------------
def font(pfad, size):
    for p in [pfad] + FONT_FALLBACK:
        if p and os.path.exists(p):
            try:
                return ImageFont.truetype(p, size)
            except OSError:
                continue
    return ImageFont.load_default()


def lade_und_einpassen(pfad, w, h, name, erlaube_unscharf=False):
    """Skaliert proportional bis die Flaeche gefuellt ist, dann mittiger Crop.

    Verzerrt NIE. Bricht ab, wenn das Quellbild zu klein ist -- genau das ist
    der Fehler, der in Band 1-4 gedruckt vorliegt.
    """
    if not os.path.exists(pfad):
        raise SystemExit(
            f"FEHLER: {name} nicht gefunden:\n  {pfad}\n"
            f"  Erwartet wird ein Bild von mindestens {w} x {h} px."
        )

    im = Image.open(pfad).convert("RGB")
    sw, sh = im.size

    # Effektive Aufloesung: wie viele dpi kommen im Druck wirklich an?
    eff_dpi = min(sw / (w / DPI), sh / (h / DPI))
    zu_klein = sw < w * 0.98 or sh < h * 0.98
    if zu_klein and not erlaube_unscharf:
        raise SystemExit(
            f"ABBRUCH: {name} ist zu klein.\n"
            f"  vorhanden : {sw} x {sh} px  (effektiv {eff_dpi:.0f} dpi)\n"
            f"  gebraucht : {w} x {h} px    (300 dpi)\n\n"
            f"  Ein Bildgenerator liefert hoechstens ~1024 x 1536 px. Das Bild\n"
            f"  muss VOR dem Cover-Bau hochskaliert werden (2x, Real-ESRGAN\n"
            f"  oder ein KI-Upscaler). Ohne das druckst du dieselbe Unschaerfe\n"
            f"  wie in Band 1-4 (dort effektiv 267 statt 300 dpi).\n\n"
            f"  Wenn du es trotzdem willst: --unscharf-erlauben"
        )
    if zu_klein:
        print(f"  !! {name}: nur {eff_dpi:.0f} dpi -- wird unscharf gedruckt.")

    scale = max(w / sw, h / sh)
    nw, nh = round(sw * scale), round(sh * scale)
    im = im.resize((nw, nh), Image.LANCZOS)

    # Wie viel faellt weg? Bei generierter Typografie ist das die Stelle,
    # an der Titel oder Autorname abgeschnitten werden.
    weg_x = (nw - w) / nw * 100
    weg_y = (nh - h) / nh * 100
    if weg_x > 1 or weg_y > 1:
        print(f"  {name}: Beschnitt {weg_x:.1f} % seitlich, {weg_y:.1f} % oben/unten "
              f"(Quelle {sw}x{sh}, Verhaeltnis {sw/sh:.3f} vs. Ziel {w/h:.3f})")
        if weg_x > 6 or weg_y > 6:
            print(f"     !! Viel Beschnitt. Im Kontrollbild pruefen, ob Text "
                  f"angeschnitten ist.")

    left, top = (nw - w) // 2, (nh - h) // 2
    return im.crop((left, top, left + w, top + h))


def randfarbe(panel, seite, tiefe=40):
    """Median-Farbe eines Bildrands -- fuer die Rueckenfarbe."""
    a = np.array(panel)
    streifen = a[:, -tiefe:] if seite == "rechts" else a[:, :tiefe]
    return tuple(int(c) for c in np.median(streifen.reshape(-1, 3), axis=0))


def zeichne_ruecken(w, h, bg, band, titel, seiten):
    """Setzt den Buchruecken: Bandnummer / Titel / Reihe / Autor.

    Aufbau waagerecht (Laenge = Buchhoehe), am Ende rotate(-90) -> der Text
    laeuft von OBEN NACH UNTEN. Nachgemessen an Band 2-5.
    """
    strip = Image.new("RGB", (h, w), bg)
    d = ImageDraw.Draw(strip)

    safe = round(SPINE_SAFE * DPI)
    nutzbar = w - 2 * safe

    if seiten < MIN_SEITEN_RUECKENTEXT:
        print(f"  !! {seiten} Seiten -- KDP erlaubt unter {MIN_SEITEN_RUECKENTEXT} "
              f"Seiten KEINEN Rueckentext. Ruecken bleibt leer.")
        return strip.rotate(-90, expand=True), []
    if nutzbar < 16:
        print(f"  !! Ruecken zu schmal fuer Text ({nutzbar} px nutzbar) -- bleibt leer.")
        return strip.rotate(-90, expand=True), []

    def setze(text, f, farbe, x_anteil):
        """Zeichnet mittig auf der Ruecken-BREITE, an x_anteil der Buchhoehe."""
        bb = d.textbbox((0, 0), text, font=f)
        tw, th = bb[2] - bb[0], bb[3] - bb[1]
        d.text((int(h * x_anteil) - tw / 2, (w - th) / 2 - bb[1]),
               text, font=f, fill=farbe)
        return tw

    def passend(text, pfad, anteil, max_laenge):
        """Groesste Schrift, die in Ruecken-Breite UND Laenge passt."""
        size = max(8, int(nutzbar * anteil))
        while size > 7:
            f = font(pfad, size)
            bb = d.textbbox((0, 0), text, font=f)
            if (bb[3] - bb[1]) <= nutzbar and (bb[2] - bb[0]) <= max_laenge:
                return f
            size -= 1
        return font(pfad, 8)

    # Reihenfolge von oben nach unten. Bandnummer zuerst -- im Regal ist sie
    # das Einzige, was "gibt es noch mehr davon?" beantwortet. Band 1-5 tragen
    # bisher KEINE Nummer am Ruecken.
    f_num = passend(str(band), FONT_TITEL, 0.80, h * 0.08)
    f_tit = passend(titel, FONT_TITEL, 0.62, h * 0.42)
    f_rei = passend(REIHE, FONT_KLEIN, 0.34, h * 0.30)
    f_aut = passend(AUTOR, FONT_KLEIN, 0.40, h * 0.20)

    setze(str(band), f_num, GOLD, 0.08)
    setze(titel, f_tit, CREME, 0.34)
    setze(REIHE, f_rei, GOLD, 0.66)
    setze(AUTOR, f_aut, CREME, 0.90)

    info = [f"Bandnummer {f_num.size} pt", f"Titel {f_tit.size} pt",
            f"Reihe {f_rei.size} pt", f"Autor {f_aut.size} pt"]
    return strip.rotate(-90, expand=True), info


def weiche_falz(canvas, x0, x1, bg, mm=3.0):
    """Blendet die Rueckenfarbe weich in beide Panels aus.

    KDP faltet mit +-1.6 mm Toleranz. Eine harte Farbkante zwischen Ruecken
    und Panel wandert dadurch sichtbar auf die Vorder- oder Rueckseite. Bei
    fast schwarzen Covern wie dieser Reihe faellt das sofort auf.
    """
    breite = int(mm / 25.4 * DPI)
    if breite < 2:
        return canvas
    h = canvas.height
    maske = Image.new("L", (breite, h), 0)
    md = ImageDraw.Draw(maske)
    for i in range(breite):
        md.line([(i, 0), (i, h)], fill=int(255 * (1 - i / breite)))

    flaeche = Image.new("RGB", (breite, h), bg)
    canvas.paste(flaeche, (x1 + 1, 0), maske)                    # rechts
    canvas.paste(flaeche, (x0 - breite, 0), maske.transpose(Image.FLIP_LEFT_RIGHT))
    return canvas


def tiefen_anheben(im, staerke=0.10):
    """Hebt die Schatten fuer den Druck an.

    KDP-Digitaldruck laeuft dunkler zu als der Bildschirm. Diese Reihe ist
    fast schwarz (Russschwarz #14100c, Indigo #1a1a3e) -- ohne Anhebung wird
    die untere Bildhaelfte im Druck ein schwarzer Klumpen.
    """
    if staerke <= 0:
        return im
    a = np.array(im).astype(np.float32) / 255.0
    a = a * (1 - staerke) + staerke * (a ** 0.55)     # nur Tiefen, Lichter bleiben
    return Image.fromarray((np.clip(a, 0, 1) * 255).astype(np.uint8))


# --------------------------------------------------------------------------
# Pruefungen am fertigen Bild
# --------------------------------------------------------------------------
def kantenenergie(bild_array):
    g = bild_array.mean(axis=2)
    return float(np.abs(np.diff(g, axis=0)).mean() + np.abs(np.diff(g, axis=1)).mean())


def pruefe_zonen(canvas, panel_w, spine_w):
    """Barcode-Feld und Beschnittrand abklopfen. Heuristisch -- das Kontrollbild
    bleibt die eigentliche Kontrolle."""
    a = np.array(canvas).astype(float)
    H, W, _ = a.shape
    warnungen = []

    # Barcode: unten rechts auf der RUECKSEITE (= linkes Panel, Rueckseite links)
    bx1 = round((BLEED + TRIM_W - BARCODE_INSET) * DPI)
    bx0 = bx1 - round(BARCODE_W * DPI)
    by1 = round((BLEED + TRIM_H - BARCODE_INSET) * DPI)
    by0 = by1 - round(BARCODE_H * DPI)
    zone = a[by0:by1, bx0:bx1]
    if kantenenergie(zone) > kantenenergie(a) * 1.3:
        warnungen.append(
            "BARCODE-ZONE (Rueckseite unten rechts, 2.0 x 1.2 Zoll) enthaelt viel "
            "Struktur -- moeglicherweise Text oder ein Blickfang. KDP druckt dort "
            "den Barcode darueber."
        )

    # Aeusserer Ring: Anschnitt + Textsicherheitsabstand
    ring = round((BLEED + SAFE_TEXT) * DPI)
    maske = np.ones((H, W), bool)
    maske[ring:H - ring, ring:W - ring] = False
    maske[:, panel_w - 20:panel_w + spine_w + 20] = False   # Ruecken ausklammern
    if maske.sum() and kantenenergie(a) > 0:
        rand = a[maske].reshape(-1, 1, 3)
        # Helle Pixel am Rand sind der Verdacht: heller Text im Beschnitt.
        hell = float((rand.mean(axis=2) > 200).mean())
        if hell > 0.02:
            warnungen.append(
                f"AEUSSERER RAND: {hell*100:.1f} % der Pixel im Beschnitt- und "
                f"Sicherheitsrand ({BLEED+SAFE_TEXT:.3f} Zoll) sind sehr hell. "
                f"Verdacht auf Text zu nah an der Kante -- im Kontrollbild pruefen."
            )
    return warnungen


def kontrollbild(canvas, panel_w, spine_w, pfad):
    """Vollcover mit eingezeichneten KDP-Linien. Das ist das Bild, das man
    ansieht -- kein Skript kann beurteilen, ob ein Titel gut sitzt."""
    k = canvas.copy()
    d = ImageDraw.Draw(k)
    H, W = k.height, k.width
    b = round(BLEED * DPI)
    s = round((BLEED + SAFE_TEXT) * DPI)

    def kasten(x0, y0, x1, y1, farbe, br=4):
        d.rectangle([x0, y0, x1, y1], outline=farbe, width=br)

    kasten(b, b, W - b - 1, H - b - 1, (255, 0, 0))             # Trimmkante
    kasten(s, s, W - s - 1, H - s - 1, (0, 220, 255))           # Textsicherheit
    kasten(panel_w, 0, panel_w + spine_w - 1, H - 1, (255, 220, 0))   # Ruecken
    # Ruecken-Textsicherheit
    sp = round(SPINE_SAFE * DPI)
    kasten(panel_w + sp, 0, panel_w + spine_w - sp - 1, H - 1, (255, 120, 0), 2)

    bx1 = round((BLEED + TRIM_W - BARCODE_INSET) * DPI)
    bx0 = bx1 - round(BARCODE_W * DPI)
    by1 = round((BLEED + TRIM_H - BARCODE_INSET) * DPI)
    by0 = by1 - round(BARCODE_H * DPI)
    kasten(bx0, by0, bx1, by1, (255, 0, 255))                   # Barcode

    f = font(FONT_KLEIN, 34)
    legende = ["rot = Trimmkante (wird geschnitten)",
               "cyan = Textsicherheitsabstand 0.25 Zoll",
               "gelb = Buchruecken / orange = Ruecken-Textgrenze",
               "magenta = Barcode-Feld (bleibt frei)"]
    for i, t in enumerate(legende):
        d.text((b + 14, b + 14 + i * 44), t, font=f, fill=(255, 255, 255),
               stroke_width=3, stroke_fill=(0, 0, 0))
    k.save(pfad, quality=88)


# --------------------------------------------------------------------------
def main():
    ap = argparse.ArgumentParser(description="KDP-Vollcover fuer Die Geisterspuerer")
    ap.add_argument("band", type=int, choices=sorted(BAENDE))
    ap.add_argument("--front")
    ap.add_argument("--back")
    ap.add_argument("--seiten", type=int, help="Seitenzahl uebersteuern (Testlauf)")
    ap.add_argument("--unscharf-erlauben", action="store_true",
                    dest="unscharf", help="zu kleine Quellbilder zulassen")
    ap.add_argument("--tiefen", type=float, default=0.10,
                    help="Schattenanhebung fuer den Druck, 0 = aus (Vorgabe 0.10)")
    args = ap.parse_args()

    band = args.band
    cfg = BAENDE[band]
    cover_dir = os.path.join(_ROOT, f"Band{band}", "Cover", "Bilder")
    front = args.front or os.path.join(cover_dir, f"front_band{band}.png")
    back = args.back or os.path.join(cover_dir, f"back_band{band}.png")

    seiten = args.seiten or cfg["seiten"]
    if seiten is None:
        raise SystemExit(
            f"ABBRUCH: Fuer Band {band} ist keine Seitenzahl hinterlegt.\n"
            f"  Die Rueckenbreite ergibt sich zwingend aus der Seitenzahl.\n"
            f"  Echte Zahl aus dem KDP-Previewer in BAENDE[{band}]['seiten']\n"
            f"  eintragen und ['bestaetigt'] = True setzen."
        )
    if not cfg["bestaetigt"] and not args.seiten:
        raise SystemExit(
            f"ABBRUCH: BAENDE[{band}]['bestaetigt'] ist False -- die Seitenzahl\n"
            f"  {seiten} ist noch nicht gegen den KDP-Previewer geprueft.\n"
            f"  (Band 3 hatte eine Schaetzung, die nie ersetzt wurde.)\n"
            f"  Testlauf trotzdem: --seiten {seiten}"
        )

    faktor = PAPIER[cfg["papier"]]
    spine_in = seiten * faktor
    total_w_in = 2 * (TRIM_W + BLEED) + spine_in
    total_h_in = TRIM_H + 2 * BLEED
    TW, TH = round(total_w_in * DPI), round(total_h_in * DPI)
    panel_w = round((TRIM_W + BLEED) * DPI)
    spine_w = TW - 2 * panel_w

    print("=" * 68)
    print(f"KDP-Vollcover  --  Die Geisterspuerer, Band {band}: {cfg['titel']}")
    print("=" * 68)
    print(f"  Seiten     : {seiten} ({cfg['papier']}es Papier, Faktor {faktor})"
          + ("" if cfg["bestaetigt"] else "   << NICHT BESTAETIGT (Testlauf) >>"))
    print(f"  Ruecken    : {spine_in:.3f} Zoll = {spine_in*25.4:.1f} mm = {spine_w} px")
    print(f"  Gesamt     : {TW} x {TH} px ({total_w_in:.3f} x {total_h_in:.3f} Zoll)")
    print(f"  Panel je   : {panel_w} x {TH} px")
    print()

    print("Quellbilder:")
    p_back = lade_und_einpassen(back, panel_w, TH, "Rueckseite", args.unscharf)
    p_front = lade_und_einpassen(front, panel_w, TH, "Vorderseite", args.unscharf)
    print()

    bg = cfg["ruecken_bg"]
    if bg is None:
        c1 = randfarbe(p_back, "rechts")
        c2 = randfarbe(p_front, "links")
        bg = tuple(int((a + b) / 2) for a, b in zip(c1, c2))
        print(f"  Rueckenfarbe aus den Bildraendern gemessen: RGB{bg}")
    else:
        print(f"  Rueckenfarbe fest vorgegeben: RGB{bg}")

    strip, info = zeichne_ruecken(spine_w, TH, bg, band, cfg["titel"], seiten)
    if info:
        print("  Ruecken gesetzt: " + ", ".join(info))
        print(f"  (nutzbare Breite {spine_w - 2*round(SPINE_SAFE*DPI)} px "
              f"= {(spine_in - 2*SPINE_SAFE)*25.4:.1f} mm)")
    print()

    canvas = Image.new("RGB", (TW, TH), bg)
    canvas.paste(p_back, (0, 0))
    canvas.paste(p_front, (panel_w + spine_w, 0))
    canvas = weiche_falz(canvas, panel_w, panel_w + spine_w - 1, bg)
    canvas.paste(strip, (panel_w, 0))

    warnungen = pruefe_zonen(canvas, panel_w, spine_w)

    druck = tiefen_anheben(canvas, args.tiefen)
    if args.tiefen > 0:
        print(f"  Tiefen fuer den Druck um {args.tiefen*100:.0f} % angehoben "
              f"(--tiefen 0 schaltet das ab).")

    # Eigener Ordner: Output/BandN/ enthaelt die Dateien der VERKAUFTEN Auflage.
    # Die duerfen nicht ueberschrieben werden, solange die Neufassung nicht
    # freigegeben ist -- sonst ist die Vorlage des laufenden Produkts weg.
    out_dir = os.path.join(_ROOT, "Output", f"Band{band}", "Cover_neu")
    os.makedirs(out_dir, exist_ok=True)
    p_pdf = os.path.join(out_dir, f"KDP_Band{band}_Cover_Vollcover_300dpi.pdf")
    p_jpg = os.path.join(out_dir, f"KDP_Band{band}_Cover_Vollcover_300dpi.jpg")
    p_ctl = os.path.join(out_dir, f"KDP_Band{band}_Cover_KONTROLLE.jpg")
    p_thm = os.path.join(out_dir, f"KDP_Band{band}_Cover_thumbnail_150.png")
    p_ebk = os.path.join(out_dir, f"KDP_Band{band}_Cover_eBook_1600x2560.jpg")

    druck.save(p_jpg, quality=95, dpi=(DPI, DPI))
    import img2pdf
    with open(p_pdf, "wb") as f:
        f.write(img2pdf.convert(p_jpg, layout_fun=img2pdf.get_layout_fun(
            (img2pdf.in_to_pt(total_w_in), img2pdf.in_to_pt(total_h_in)))))

    # eBook: 1:1.6 statt 1:1.5 -> ANDERER Beschnitt, nicht bloss kleiner.
    # Und: JPG, nicht PNG -- KDP nimmt fuer eBook-Cover nur JPEG oder TIFF.
    # Ohne Tiefenanhebung, das ist ein Bildschirm-Cover.
    ebook_src = Image.open(front).convert("RGB")
    sw, sh = ebook_src.size
    sc = max(EBOOK_W / sw, EBOOK_H / sh)
    ebook_src = ebook_src.resize((round(sw * sc), round(sh * sc)), Image.LANCZOS)
    l, t = (ebook_src.width - EBOOK_W) // 2, (ebook_src.height - EBOOK_H) // 2
    ebook_src.crop((l, t, l + EBOOK_W, t + EBOOK_H)).save(p_ebk, quality=95)

    kontrollbild(druck, panel_w, spine_w, p_ctl)
    thumb = druck.crop((panel_w + spine_w, 0, TW, TH))
    thumb.resize((150, round(150 * TH / panel_w)), Image.LANCZOS).save(p_thm)

    # ---- Selbstpruefung am erzeugten Artefakt -----------------------------
    print()
    print("Selbstpruefung am fertigen PDF:")
    import fitz
    doc = fitz.open(p_pdf)
    r = doc[0].rect
    doc.close()
    ist_w, ist_h = r.width / 72, r.height / 72
    if abs(ist_w - total_w_in) > 0.005 or abs(ist_h - total_h_in) > 0.005:
        warnungen.append(f"PDF-MASS falsch: {ist_w:.3f} x {ist_h:.3f} Zoll statt "
                         f"{total_w_in:.3f} x {total_h_in:.3f}.")
    else:
        print(f"  PDF misst {ist_w:.3f} x {ist_h:.3f} Zoll = {ist_w*DPI:.0f} x "
              f"{ist_h*DPI:.0f} px @ {DPI} dpi -- korrekt.")

    kontrolle = Image.open(p_jpg)
    if kontrolle.size != (TW, TH):
        warnungen.append(f"JPG-MASS falsch: {kontrolle.size} statt ({TW}, {TH}).")
    else:
        print(f"  JPG misst {TW} x {TH} px -- korrekt, unverzerrt.")

    print()
    print("=" * 68)
    for pfad, was in [(p_pdf, "Vollcover PDF  -> KDP-Upload Taschenbuch"),
                      (p_jpg, "Vollcover JPG  -> Kontrolle"),
                      (p_ebk, "eBook-Cover    -> KDP-Upload eBook (JPG, 1:1.6)"),
                      (p_ctl, "KONTROLLBILD   -> ANSEHEN, mit KDP-Linien"),
                      (p_thm, "Thumbnail 150  -> ANSEHEN, Amazon-Groesse")]:
        print(f"  {was}\n    {pfad}")

    if warnungen:
        print()
        print("!! WARNUNGEN:")
        for w in warnungen:
            print("   - " + w)

    print()
    print("VON HAND PRUEFEN (kann kein Skript):")
    print(f"  1. Kontrollbild: liegt Text innerhalb der CYANEN Linie?")
    print(f"  2. Kontrollbild: ist das MAGENTA Barcode-Feld ruhig und leer?")
    print(f"  3. Ruecken: steht dort '{cfg['titel']}' -- der Titel von Band {band}?")
    print(f"     (Beim ersten Band-5-Entwurf stand dort 'Die Zugemauerte Tuer'.)")
    print(f"  4. Thumbnail: Titel und Hingucker bei 150 px noch erkennbar?")
    print(f"  5. KDP-Previewer: Ruecken mittig, nichts Wichtiges im Anschnitt?")


if __name__ == "__main__":
    main()
