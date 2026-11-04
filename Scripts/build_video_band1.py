# -*- coding: utf-8 -*-
"""
Baut das 15-Sekunden-Werbevideo fuer "Das Haus, das fluestert" (Band 1, Staffel 1).
Skript und Begruendung: Dokumentation/Amazon_Ads_Video_Band1.md

    python Scripts/build_video_band1.py            # fertiges MP4
    python Scripts/build_video_band1.py --bild 4.2 # nur ein Einzelbild zur Kontrolle

Quellen: Band1/Cover/Bilder/video_fenster.png, video_fenster_klar.png, front_band1.jpg
Ausgabe: Output/Band1_Video/ (nicht in Git)

Kein Videogenerator: HILF ist eine Maske, durch die das Klarglas sichtbar wird. Text wird
gesetzt, nie generiert, damit jeder Buchstabe stimmt.
"""
import argparse
import os
import subprocess

import cv2
import numpy as np
from PIL import Image, ImageDraw, ImageFilter, ImageFont

_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BILDER = os.path.join(_ROOT, "Band1", "Cover", "Bilder")
OUT_DIR = os.path.join(_ROOT, "Output", "Band1_Video")

W, H = 1920, 1080
FPS = 30
DAUER = 15.0
OVER = 1.08  # Ueberstand fuer die Kamerafahrt auf der Scheibe

# Zeitplan in Sekunden, siehe Skript in der Dokumentation
T_HILF_FERTIG = 1.5
T_TEXT1 = (2.5, 5.0)
T_TEXT2 = (5.0, 8.0)
T_HAUS = (8.0, 8.6)      # Ueberblendung Scheibe -> Haus
T_FRAGE = (9.2, 11.4)
T_ENDE = (11.4, 11.65)   # Ueberblendung Haus -> Schlussbild

CREME = (242, 226, 184)
WEISS = (250, 246, 236)
GOLD = (223, 176, 87)

FONT_FETT = "C:/Windows/Fonts/georgiab.ttf"
FONT_NORMAL = "C:/Windows/Fonts/georgia.ttf"


def lade(name, groesse=None):
    im = Image.open(os.path.join(BILDER, name)).convert("RGB")
    if groesse:
        im = im.resize(groesse, Image.LANCZOS)
    return np.asarray(im).astype(np.float32) / 255.0


def weich(x):
    x = np.clip(x, 0.0, 1.0)
    return x * x * (3 - 2 * x)


def fenster(t, t0, t1, rand=0.25):
    """Deckkraft: ein- und ausblenden ueber rand Sekunden."""
    return weich((t - t0) / rand) * weich((t1 - t) / rand)


# ---------------------------------------------------------------- HILF-Maske

def buchstaben_pfade(cw, ch):
    """Striche wie mit dem Finger: leicht unregelmaessig, in Schreibreihenfolge."""
    s = OVER
    x0, y0, b, h = 345 * s, 185 * s, 118 * s, 300 * s
    luecke = 62 * s
    px = lambda i, fx, fy: (x0 + i * (b + luecke) + fx * b, y0 + fy * h)
    return [
        # H
        [px(0, 0.02, 0.00), px(0, 0.00, 0.50), px(0, 0.03, 1.00)],
        [px(0, 0.98, 0.02), px(0, 1.02, 0.52), px(0, 0.97, 0.99)],
        [px(0, 0.02, 0.50), px(0, 0.50, 0.47), px(0, 1.00, 0.49)],
        # I
        [px(1, 0.28, 0.01), px(1, 0.25, 0.50), px(1, 0.29, 1.00)],
        # L
        [px(1.72, 0.03, 0.00), px(1.72, 0.00, 0.55), px(1.72, 0.02, 0.98),
         px(1.72, 0.45, 0.99), px(1.72, 0.92, 0.97)],
        # F
        [px(2.72, 0.03, 0.01), px(2.72, 0.00, 0.50), px(2.72, 0.03, 1.00)],
        [px(2.72, 0.02, 0.02), px(2.72, 0.50, 0.00), px(2.72, 0.98, 0.03)],
        [px(2.72, 0.02, 0.47), px(2.72, 0.42, 0.45), px(2.72, 0.80, 0.47)],
    ]


def dicht(pfad, schritt=4.0):
    pts = []
    for (ax, ay), (bx, by) in zip(pfad, pfad[1:]):
        n = max(2, int(np.hypot(bx - ax, by - ay) / schritt))
        for i in range(n):
            f = i / n
            pts.append((ax + (bx - ax) * f, ay + (by - ay) * f))
    pts.append(pfad[-1])
    return pts


class Maske:
    def __init__(self, cw, ch):
        self.cw, self.ch = cw, ch
        rng = np.random.default_rng(7)
        self.pfade = [dicht(p) for p in buchstaben_pfade(cw, ch)]
        self.gesamt = sum(len(p) for p in self.pfade)
        grob = rng.random((ch // 6, cw // 6)).astype(np.float32)
        self.rausch = cv2.GaussianBlur(cv2.resize(grob, (cw, ch), interpolation=cv2.INTER_CUBIC), (0, 0), 2.5)
        self.rausch = (self.rausch - self.rausch.min()) / (np.ptp(self.rausch) + 1e-6)
        self.fertig = None

    def bei(self, t):
        fort = 0.16 + 0.84 * weich(t / T_HILF_FERTIG)
        if fort >= 0.999 and self.fertig is not None:
            return self.fertig
        n = int(self.gesamt * fort)
        leer = np.zeros((self.ch, self.cw), np.uint8)
        for p in self.pfade:
            if n <= 0:
                break
            teil = np.array(p[:n], np.float32)
            n -= len(p)
            if len(teil) >= 2:
                cv2.polylines(leer, [(teil * 8).astype(np.int32)], False, 255,
                              thickness=int(30 * OVER), lineType=cv2.LINE_AA, shift=3)
        m = cv2.GaussianBlur(leer.astype(np.float32) / 255.0, (0, 0), 5.0)
        m = np.clip((m + (self.rausch - 0.5) * 0.28 - 0.42) / 0.20, 0, 1)
        m = m * m * (3 - 2 * m)
        if fort >= 0.999:
            self.fertig = m
        return m


# ---------------------------------------------------------------- Buch

def buch_rgba(hoehe, kippen=0.055):
    """Buch als Objekt: Vorderseite leicht gedreht, Ruecken links. Liefert RGBA float."""
    im = Image.open(os.path.join(BILDER, "front_band1.jpg")).convert("RGB")
    cw, ch = im.size
    breite = int(ch * 0.625)
    links = (cw - breite) // 2
    im = im.crop((links, 0, links + breite, ch))
    b = int(hoehe * 0.625)
    cover = np.asarray(im.resize((b * 2, hoehe * 2), Image.LANCZOS)).astype(np.float32) / 255.0
    ruecken = int(hoehe * 0.026)
    gw, gh = b + ruecken + 40, hoehe + 40
    y = int(hoehe * kippen)
    z = np.array([[ruecken + 20, 20], [gw - 20, 20 + y], [gw - 20, gh - 20 - y], [ruecken + 20, gh - 20]], np.float32)
    q = np.array([[0, 0], [b * 2, 0], [b * 2, hoehe * 2], [0, hoehe * 2]], np.float32)
    M = cv2.getPerspectiveTransform(q, z)
    bild = cv2.warpPerspective(cover, M, (gw, gh), flags=cv2.INTER_AREA)
    alpha = cv2.warpPerspective(np.ones(cover.shape[:2], np.float32), M, (gw, gh), flags=cv2.INTER_LINEAR)

    # Ruecken: dunkle Kante mit gedrucktem Farbton
    leer = np.zeros((gh, gw, 3), np.uint8)
    pts = np.array([[20, 20 + int(y * 1.3)], [ruecken + 20, 20], [ruecken + 20, gh - 20], [20, gh - 20 - int(y * 1.3)]], np.int32)
    cv2.fillConvexPoly(leer, pts, (30, 36, 62), lineType=cv2.LINE_AA)
    r_a = cv2.fillConvexPoly(np.zeros((gh, gw), np.uint8), pts, 255, lineType=cv2.LINE_AA).astype(np.float32) / 255.0
    bild = bild * alpha[..., None] + (leer.astype(np.float32) / 255.0) * (1 - alpha[..., None])
    a = np.maximum(alpha, r_a)

    # Licht: sanfte Kante am Falz
    verlauf = np.clip((np.arange(gw) - ruecken - 20) / 14.0, 0, 1).astype(np.float32)
    bild = bild * (0.84 + 0.16 * verlauf)[None, :, None]
    return np.dstack([bild, a])


def setze(ziel, rgba, x, y, schatten=0.55):
    h, w = rgba.shape[:2]
    if schatten:
        a = np.zeros(ziel.shape[:2], np.float32)
        y1, x1 = min(y + h, a.shape[0]), min(x + w, a.shape[1])
        a[y:y1, x:x1] = rgba[:y1 - y, :x1 - x, 3]
        a = cv2.GaussianBlur(np.roll(a, -16, axis=1), (0, 0), 26) * schatten
        ziel[...] = ziel * (1 - a[..., None])
    y1, x1 = min(y + h, ziel.shape[0]), min(x + w, ziel.shape[1])
    teil = rgba[:y1 - y, :x1 - x]
    al = teil[..., 3:4]
    ziel[y:y1, x:x1] = ziel[y:y1, x:x1] * (1 - al) + teil[..., :3] * al


# ---------------------------------------------------------------- Text

def font(pfad, g):
    return ImageFont.truetype(pfad, g)


def textebene(zeilen, x, y, schleier=True):
    """zeilen: Liste aus (Text, Fontpfad, Groesse, Farbe, Abstand danach). RGBA float."""
    bild = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(bild)
    yy, breite = y, 0
    lagen = []
    for text, pfad, g, farbe, abstand in zeilen:
        f = font(pfad, g)
        lagen.append((text, f, farbe, yy))
        breite = max(breite, d.textlength(text, font=f))
        yy += g + abstand
    schatten = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    ds = ImageDraw.Draw(schatten)
    for text, f, _, ty in lagen:
        ds.text((x + 2, ty + 3), text, font=f, fill=(0, 0, 0, 220))
    schatten = schatten.filter(ImageFilter.GaussianBlur(5))
    for text, f, farbe, ty in lagen:
        d.text((x, ty), text, font=f, fill=farbe + (255,))
    ges = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    if schleier:
        s = Image.new("L", (W, H), 0)
        ImageDraw.Draw(s).rounded_rectangle((x - 40, y - 24, x + breite + 40, yy + 8), 40, fill=125)
        s = s.filter(ImageFilter.GaussianBlur(64))
        ges = Image.merge("RGBA", (Image.new("L", (W, H), 12), Image.new("L", (W, H), 18),
                                   Image.new("L", (W, H), 30), s))
    ges = Image.alpha_composite(Image.alpha_composite(ges, schatten), bild)
    return np.asarray(ges).astype(np.float32) / 255.0


def auflegen(ziel, ebene, deck):
    if deck <= 0:
        return
    a = ebene[..., 3:4] * deck
    ziel[...] = ziel * (1 - a) + ebene[..., :3] * a


# ---------------------------------------------------------------- Szenen

class Video:
    def __init__(self):
        cw, ch = int(W * OVER), int(H * OVER)
        self.cw, self.ch = cw, ch
        self.fog = lade("video_fenster.png", (cw, ch))
        klar = lade("video_fenster_klar.png", (cw, ch))
        self.klar = klar
        self.maske = Maske(cw, ch)

        buch = buch_rgba(int(760 * OVER))
        by = int(968 * OVER) - buch.shape[0]
        bx = int(1215 * OVER)
        self.buch_pos = (bx, by)
        self.buch = buch

        # Cover fuer die Kamerafahrt
        self.cover = np.asarray(Image.open(os.path.join(BILDER, "front_band1.jpg")).convert("RGB")).astype(np.float32) / 255.0

        # Schlussbild
        yy, xx = np.mgrid[0:H, 0:W].astype(np.float32)
        nacht = np.array([0.045, 0.055, 0.095], np.float32)
        warm = np.array([0.55, 0.33, 0.13], np.float32)
        glut = np.exp(-(((xx - 1340) / 800) ** 2 + ((yy - 560) / 640) ** 2))[..., None]
        rng = np.random.default_rng(3)
        korn = rng.normal(0, 0.006, (H, W, 1)).astype(np.float32)
        self.ende_grund = nacht + warm * glut * 0.85 + korn
        self.ende_buch = buch_rgba(900, kippen=0.05)

        self.t1 = textebene([("Kribbeln ja, Albträume nein.", FONT_FETT, 62, WEISS, 22),
                             ("Grusel mit Humor ab 10", FONT_NORMAL, 42, CREME, 0)], 300, 640)
        self.t2 = textebene([("Kondenswasser schreibt", FONT_FETT, 58, WEISS, 14),
                             ("keine deutschen Wörter!", FONT_FETT, 58, WEISS, 22),
                             ("Theo, 10", FONT_NORMAL, 36, CREME, 0)], 300, 616)
        self.t3 = textebene([("Wer dann?", FONT_FETT, 92, WEISS, 0)], 150, 110)
        self.t4 = textebene([("Ein Geschenk", FONT_FETT, 84, WEISS, 18),
                             ("für mutige Leser", FONT_FETT, 84, WEISS, 40),
                             ("Band 1 von 5", FONT_NORMAL, 48, GOLD, 0)], 170, 370, schleier=False)

    def scheibe(self, t):
        m = self.maske.bei(t)[..., None]
        bild = self.fog * (1 - m) + self.klar * m
        bild = bild.copy()
        ohne = bild.copy()
        setze(bild, self.buch, *self.buch_pos)
        weg = float(weich((t - 7.6) / 0.4))
        bild = bild * (1 - weg) + ohne * weg
        # langsamer Push-in auf die Scheibe
        z = 1.0 + 0.035 * weich(t / 8.0)
        bw, bh = W / z, H / z
        cx, cy = self.cw * 0.48, self.ch * 0.5
        M = np.array([[W / bw, 0, -(cx - bw / 2) * W / bw], [0, H / bh, -(cy - bh / 2) * H / bh]], np.float32)
        return cv2.warpAffine(bild, M, (W, H), flags=cv2.INTER_LINEAR)

    def haus(self, t):
        a = (1190, 1632, 640.0)
        b = (1093, 1560, 2186.0)
        c = (1093, 2315, 2186.0)
        if t < 9.9:
            x = np.clip((t - 8.0) / 1.9, 0, 1)
            f = 1 - (1 - x) ** 3
            cw = a[2] ** (1 - f) * b[2] ** f
            g = (cw - a[2]) / (b[2] - a[2])
            cx, cy = a[0] + (b[0] - a[0]) * g, a[1] + (b[1] - a[1]) * g
        else:
            f = weich((t - 9.9) / 1.6)
            cx, cy, cw = [b[i] + (c[i] - b[i]) * f for i in range(3)]
        ch = cw * H / W
        s = W / cw
        M = np.array([[s, 0, -(cx - cw / 2) * s], [0, s, -(cy - ch / 2) * s]], np.float32)
        return cv2.warpAffine(self.cover, M, (W, H), flags=cv2.INTER_AREA if s < 1 else cv2.INTER_CUBIC,
                              borderMode=cv2.BORDER_REPLICATE)

    def ende(self, t):
        bild = self.ende_grund.copy()
        setze(bild, self.ende_buch, 1090, 70, schatten=0.5)
        auflegen(bild, self.t4, weich((t - 11.7) / 0.35))
        return bild

    def bild(self, t):
        if t < T_HAUS[1]:
            f = self.scheibe(t)
            auflegen(f, self.t1, fenster(t, *T_TEXT1))
            auflegen(f, self.t2, fenster(t, *T_TEXT2))
            if t > T_HAUS[0]:
                x = float(weich((t - T_HAUS[0]) / (T_HAUS[1] - T_HAUS[0])))
                f = f * (1 - x) + self.haus(t) * x
        elif t < T_ENDE[1]:
            f = self.haus(t)
            if t > T_ENDE[0]:
                x = float(weich((t - T_ENDE[0]) / (T_ENDE[1] - T_ENDE[0])))
                f = f * (1 - x) + self.ende(t) * x
        else:
            f = self.ende(t)
        if T_FRAGE[0] < t < T_FRAGE[1]:
            f = f.copy()
            auflegen(f, self.t3, fenster(t, *T_FRAGE))
        return np.clip(f, 0, 1)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--bild", type=float, help="nur das Bild zu dieser Sekunde als PNG ausgeben")
    args = ap.parse_args()
    os.makedirs(OUT_DIR, exist_ok=True)
    v = Video()

    if args.bild is not None:
        f = (v.bild(args.bild) * 255).astype(np.uint8)
        pfad = os.path.join(OUT_DIR, f"bild_{args.bild:05.2f}.png")
        Image.fromarray(f).save(pfad)
        print(pfad)
        return

    pfad = os.path.join(OUT_DIR, "Band1_Video_v1.mp4")
    kmd = ["ffmpeg", "-y", "-v", "error",
           "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{W}x{H}", "-r", str(FPS), "-i", "-",
           "-f", "lavfi", "-t", str(DAUER), "-i", "anoisesrc=c=brown:a=0.012:r=48000,lowpass=f=500,aformat=channel_layouts=stereo",
           "-c:v", "libx264", "-profile:v", "main", "-preset", "slow", "-crf", "18", "-pix_fmt", "yuv420p",
           "-c:a", "aac", "-b:a", "128k", "-shortest", "-movflags", "+faststart", pfad]
    p = subprocess.Popen(kmd, stdin=subprocess.PIPE)
    n = int(DAUER * FPS)
    for i in range(n):
        f = (v.bild(i / FPS) * 255 + 0.5).astype(np.uint8)
        p.stdin.write(f.tobytes())
        if i % 60 == 0:
            print(f"  {i}/{n}", flush=True)
    p.stdin.close()
    p.wait()
    print("fertig:", pfad)


if __name__ == "__main__":
    main()
