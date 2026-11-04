# -*- coding: utf-8 -*-
"""
Baut das 15-Sekunden-Werbevideo fuer "Das Haus, das fluestert" (Band 1, Staffel 1).
Skript und Begruendung: Dokumentation/Amazon_Ads_Video_Band1.md

    python Scripts/build_video_band1.py              # fertiges MP4
    python Scripts/build_video_band1.py --bild 4.2   # nur ein Einzelbild zur Kontrolle

Quellen: Band1/Cover/Bilder/video_fenster.png, video_fenster_klar.png, front_band1.jpg
Ausgabe: Output/Band1_Video/ (nicht in Git)

Kein Videogenerator: HILF ist eine Maske, durch die das Klarglas sichtbar wird. Nora, Theo und
Schatten werden per GrabCut vom Haus getrennt, damit die Kamerafahrt Tiefe bekommt. Text wird
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
VERSION = "v2"

W, H = 1920, 1080
FPS = 30
DAUER = 15.0
OVER = 1.08  # Ueberstand fuer die Kamerafahrt auf der Scheibe

# Zeitplan in Sekunden, siehe Skript in der Dokumentation
T_HILF_FERTIG = 1.5
T_TEXT1 = (2.5, 5.0)
T_TEXT2 = (5.0, 8.0)
T_HAUS = (8.0, 8.6)      # Ueberblendung Scheibe -> Haus
T_FRAGE = (9.2, 11.1)
T_ENDE = (11.4, 11.65)   # Ueberblendung Haus -> Schlussbild

CREME = (242, 226, 184)
WEISS = (250, 246, 236)
GOLD = (223, 176, 87)

FONT_FETT = "C:/Windows/Fonts/georgiab.ttf"
FONT_NORMAL = "C:/Windows/Fonts/georgia.ttf"

COVER_FENSTER = (1133, 1590)  # blaues Fenster im Cover, Pixel in front_band1.jpg
TIEFE = 0.075                 # Figuren bewegen sich bei der Fahrt um diesen Anteil staerker


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


def rausch(rng, h, w, teiler, sigma):
    """Weiches Rauschen im Bereich 0..1."""
    grob = rng.random((max(2, h // teiler), max(2, w // teiler))).astype(np.float32)
    n = cv2.GaussianBlur(cv2.resize(grob, (w, h), interpolation=cv2.INTER_CUBIC), (0, 0), sigma)
    return (n - n.min()) / (np.ptp(n) + 1e-6)


# ---------------------------------------------------------------- HILF-Maske

def buchstaben_pfade():
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
        self.pfade = [dicht(p) for p in buchstaben_pfade()]
        self.gesamt = sum(len(p) for p in self.pfade)
        self.rausch = rausch(np.random.default_rng(7), ch, cw, 6, 2.5)
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


def perlen(m, cw, ch):
    """Kleine Tropfen entlang der Buchstabenkanten. Liefert RGBA float."""
    rng = np.random.default_rng(11)
    ys, xs = np.nonzero((m > 0.15) & (m < 0.7))
    wahl = rng.choice(len(xs), 110, replace=False)
    a = Image.new("L", (cw, ch), 0)
    d = ImageDraw.Draw(a)
    for i in wahl:
        r = rng.uniform(1.6, 4.2)
        d.ellipse((xs[i] - r, ys[i] - r, xs[i] + r, ys[i] + r), fill=int(rng.uniform(120, 210)))
    al = np.asarray(a.filter(ImageFilter.GaussianBlur(0.8))).astype(np.float32) / 255.0
    return np.dstack([np.full((ch, cw, 3), (0.86, 0.93, 1.0), np.float32), al])


# ---------------------------------------------------------------- Buch

def buch_rgba(hoehe, kippen=0.055):
    """Buch als Objekt, Vorderseite leicht gedreht, Ruecken links.
    Liefert RGBA float und die Lage des blauen Fensters im Buchbild."""
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

    fx = (COVER_FENSTER[0] - links) / breite * b * 2
    fy = COVER_FENSTER[1] / ch * hoehe * 2
    wx, wy = cv2.perspectiveTransform(np.array([[[fx, fy]]], np.float32), M)[0, 0]

    leer = np.zeros((gh, gw, 3), np.uint8)
    pts = np.array([[20, 20 + int(y * 1.3)], [ruecken + 20, 20], [ruecken + 20, gh - 20], [20, gh - 20 - int(y * 1.3)]], np.int32)
    cv2.fillConvexPoly(leer, pts, (30, 36, 62), lineType=cv2.LINE_AA)
    r_a = cv2.fillConvexPoly(np.zeros((gh, gw), np.uint8), pts, 255, lineType=cv2.LINE_AA).astype(np.float32) / 255.0
    bild = bild * alpha[..., None] + (leer.astype(np.float32) / 255.0) * (1 - alpha[..., None])
    a = np.maximum(alpha, r_a)

    verlauf = np.clip((np.arange(gw) - ruecken - 20) / 14.0, 0, 1).astype(np.float32)
    bild = bild * (0.84 + 0.16 * verlauf)[None, :, None]
    return np.dstack([bild, a]), (float(wx), float(wy))


def ebene_auf_leinwand(rgba, x, y, cw, ch):
    leer = np.zeros((ch, cw, 4), np.float32)
    h, w = rgba.shape[:2]
    y1, x1 = min(y + h, ch), min(x + w, cw)
    leer[y:y1, x:x1] = rgba[:y1 - y, :x1 - x]
    return leer


def schatten_von(ebene, versatz=-16, sigma=26, staerke=0.55):
    a = np.roll(ebene[..., 3], versatz, axis=1)
    return cv2.GaussianBlur(a, (0, 0), sigma) * staerke


def glut(cw, ch, x, y, sigma, farbe):
    yy, xx = np.mgrid[0:ch, 0:cw].astype(np.float32)
    g = np.exp(-(((xx - x) / sigma) ** 2 + ((yy - y) / sigma) ** 2))
    return g[..., None] * np.array(farbe, np.float32)


# ---------------------------------------------------------------- Figuren

def figuren_maske(cover):
    """Trennt Nora, Theo und Schatten vom Haus (GrabCut mit Umrissen aus dem Cover)."""
    hoehe, breite = cover.shape[:2]
    y0 = 1750
    s = 0.35
    roi = (cover[y0:] * 255).astype(np.uint8)
    kl = cv2.resize(roi, None, fx=s, fy=s, interpolation=cv2.INTER_AREA)
    bgr = kl[..., ::-1].copy()
    h, w = kl.shape[:2]
    m = np.full((h, w), cv2.GC_PR_BGD, np.uint8)

    def poly(pts, wert):
        p = np.array([[(x * 1.63, y * 1.63 - y0) for x, y in pts]], np.float32) * s
        cv2.fillPoly(m, [p.astype(np.int32)], wert)

    poly([(290, 1200), (380, 1130), (500, 1200), (560, 1500), (570, 1999), (130, 1999), (150, 1500)], cv2.GC_PR_FGD)
    poly([(330, 1250), (460, 1250), (510, 1550), (480, 1950), (220, 1950), (190, 1560)], cv2.GC_FGD)
    poly([(640, 1360), (750, 1360), (760, 1500), (830, 1800), (880, 1999), (480, 1999), (570, 1700)], cv2.GC_PR_FGD)
    poly([(640, 1420), (700, 1420), (720, 1650), (760, 1950), (600, 1950), (610, 1650)], cv2.GC_FGD)
    poly([(900, 1240), (1080, 1240), (1190, 1560), (1170, 1999), (810, 1999), (800, 1560)], cv2.GC_PR_FGD)
    poly([(930, 1300), (1040, 1300), (1140, 1560), (1100, 1950), (880, 1950), (850, 1560)], cv2.GC_FGD)
    m[: int((1100 * 1.63 - y0) * s)] = cv2.GC_BGD

    cv2.grabCut(bgr, m, None, np.zeros((1, 65)), np.zeros((1, 65)), 6, cv2.GC_INIT_WITH_MASK)
    fg = ((m == cv2.GC_FGD) | (m == cv2.GC_PR_FGD)).astype(np.uint8)
    _, lab, st, _ = cv2.connectedComponentsWithStats(fg)
    gross = 1 + np.argsort(st[1:, cv2.CC_STAT_AREA])[-3:]
    fg = np.isin(lab, gross).astype(np.float32)
    fg = cv2.morphologyEx(fg, cv2.MORPH_CLOSE, np.ones((9, 9)))
    fg = cv2.dilate(fg, cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5)))
    voll = cv2.resize(fg, (breite, hoehe - y0), interpolation=cv2.INTER_LINEAR)
    voll = cv2.GaussianBlur(voll, (0, 0), 2.2)
    aus = np.zeros((hoehe, breite), np.float32)
    aus[y0:] = voll
    return aus


def hintergrund_fuellen(cover, maske):
    """Fuellt die Flaeche hinter den Figuren, die bei der Fahrt sichtbar wird."""
    s = 0.25
    kl = cv2.resize((cover * 255).astype(np.uint8), None, fx=s, fy=s, interpolation=cv2.INTER_AREA)
    mk = cv2.resize(maske, (kl.shape[1], kl.shape[0]), interpolation=cv2.INTER_AREA)
    mk = cv2.dilate((mk > 0.05).astype(np.uint8) * 255, cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (17, 17)))
    gefuellt = cv2.inpaint(kl[..., ::-1].copy(), mk, 9, cv2.INPAINT_TELEA)[..., ::-1]
    gr = cv2.resize(gefuellt, (cover.shape[1], cover.shape[0]), interpolation=cv2.INTER_CUBIC).astype(np.float32) / 255.0
    groesser = cv2.resize(mk, (cover.shape[1], cover.shape[0]), interpolation=cv2.INTER_LINEAR).astype(np.float32) / 255.0
    a = cv2.GaussianBlur(groesser, (0, 0), 8)[..., None]
    return cover * (1 - a) + gr * a


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


def auflegen(ziel, ebene, deck, anstieg=0):
    """Text blendet ein und steigt dabei um wenige Pixel."""
    if deck <= 0:
        return
    e = np.roll(ebene, anstieg, axis=0) if anstieg else ebene
    a = e[..., 3:4] * deck
    ziel[...] = ziel * (1 - a) + e[..., :3] * a


# ---------------------------------------------------------------- Szenen

class Video:
    def __init__(self):
        cw, ch = int(W * OVER), int(H * OVER)
        self.cw, self.ch = cw, ch
        rng = np.random.default_rng(5)

        # Scheibe
        self.fog = lade("video_fenster.png", (cw, ch))
        self.klar = lade("video_fenster_klar.png", (cw, ch))
        self.maske = Maske(cw, ch)
        self.perlen = perlen(self.maske.bei(99.0), cw, ch)

        sx, sy = cw / 1672.0, ch / 941.0
        glas = np.zeros((ch, cw), np.float32)
        cv2.fillPoly(glas, [np.array([[232 * sx, 100 * sy], [1490 * sx, 45 * sy], [1490 * sx, 815 * sy],
                                      [225 * sx, 775 * sy]], np.int32)], 1.0)
        self.glas = cv2.GaussianBlur(glas, (0, 0), 14)
        self.gx, self.gy = np.meshgrid(np.arange(cw, dtype=np.float32), np.arange(ch, dtype=np.float32))
        self.n1 = rausch(rng, ch, cw, 60, 30) - 0.5
        self.n2 = rausch(rng, ch, cw, 60, 30) - 0.5

        # Buch auf der Fensterbank
        buch, (wx, wy) = buch_rgba(int(760 * OVER))
        by = int(968 * OVER) - buch.shape[0]
        bx = int(1215 * OVER)
        self.buch = ebene_auf_leinwand(buch, bx, by, cw, ch)
        schatten = schatten_von(self.buch)
        kante = np.zeros((ch, cw), np.float32)
        cv2.ellipse(kante, (bx + buch.shape[1] // 2, by + buch.shape[0] - 26), (buch.shape[1] // 2, 16), 0, 0, 360, 1.0, -1)
        self.buch_schatten = np.clip(schatten + cv2.GaussianBlur(kante, (0, 0), 9) * 0.6, 0, 0.85)
        self.buch_glut = glut(cw, ch, bx + wx, by + wy, 46, (0.30, 0.46, 0.75))

        # Haus in zwei Ebenen
        self.cover = lade("front_band1.jpg")
        self.fg_a = figuren_maske(self.cover)
        self.bg = hintergrund_fuellen(self.cover, self.fg_a)
        c = self.cover
        warm = ((c[..., 0] > 0.55) & (c[..., 0] - c[..., 2] > 0.25)).astype(np.float32)
        warm[2150:] = 0
        self.warm = cv2.GaussianBlur(warm, (0, 0), 3)
        blau = ((c[..., 2] > 0.5) & (c[..., 2] > c[..., 0] + 0.05)).astype(np.float32)
        ziel = np.zeros_like(blau)
        ziel[1450:1730, 1060:1210] = 1
        self.blau = cv2.GaussianBlur(blau * ziel, (0, 0), 6)
        kh, kw = c.shape[0] // 8, c.shape[1] // 8
        self.f1 = cv2.resize(rausch(rng, kh, kw, 12, 6) - 0.5, (c.shape[1], c.shape[0]))
        self.f2 = cv2.resize(rausch(rng, kh, kw, 12, 6) - 0.5, (c.shape[1], c.shape[0]))
        self.nebel1 = rausch(rng, H, W * 2, 90, 40)
        self.nebel2 = rausch(rng, H, W * 2, 60, 28)
        self.xx, self.yy = np.meshgrid(np.arange(W, dtype=np.float32), np.arange(H, dtype=np.float32))

        # Schlussbild
        yy, xx = np.mgrid[0:H, 0:W].astype(np.float32)
        nacht = np.array([0.045, 0.055, 0.095], np.float32)
        warmton = np.array([0.55, 0.33, 0.13], np.float32)
        g = np.exp(-(((xx - 1340) / 800) ** 2 + ((yy - 560) / 640) ** 2))[..., None]
        korn = rng.normal(0, 0.006, (H, W, 1)).astype(np.float32)
        grund = nacht + warmton * g * 0.85 + korn
        eb, (ex, ey) = buch_rgba(900, kippen=0.05)
        ebene = ebene_auf_leinwand(eb, 1090, 70, W, H)
        schatten = schatten_von(ebene, staerke=0.5)[..., None]
        self.ende_bild = grund * (1 - schatten)
        al = ebene[..., 3:4]
        self.ende_bild = self.ende_bild * (1 - al) + ebene[..., :3] * al
        self.ende_glut = glut(W, H, 1090 + ex, 70 + ey, 40, (0.28, 0.42, 0.70))
        self.funken = [(rng.uniform(780, 1900), rng.uniform(0, H), rng.uniform(8, 26), rng.uniform(1.2, 2.8),
                        rng.uniform(0, 6.28)) for _ in range(26)]

        # Filmkorn, wiederverwendet
        self.korn = [rng.normal(0, 0.007, (H, W, 1)).astype(np.float32) for _ in range(6)]

        self.t1 = textebene([("Kribbeln ja, Albträume nein.", FONT_FETT, 62, WEISS, 22),
                             ("Grusel mit Humor ab 10", FONT_NORMAL, 42, CREME, 0)], 300, 640)
        self.t2 = textebene([("Kondenswasser schreibt", FONT_FETT, 58, WEISS, 14),
                             ("keine deutschen Wörter!", FONT_FETT, 58, WEISS, 22),
                             ("Theo, 10", FONT_NORMAL, 36, CREME, 0)], 300, 616)
        self.t3 = textebene([("Wer dann?", FONT_FETT, 92, WEISS, 0)], 150, 110)
        self.t4 = textebene([("Ein Geschenk", FONT_FETT, 84, WEISS, 18),
                             ("für mutige Leser", FONT_FETT, 84, WEISS, 40),
                             ("Band 1 von 5", FONT_NORMAL, 48, GOLD, 0)], 170, 370, schleier=False)

    # -- Scheibe -------------------------------------------------------
    def scheibe(self, t):
        w = 0.5 * t
        co, si = float(np.cos(w)), float(np.sin(w))
        dx = (self.n1 * co + self.n2 * si) * 26 * self.glas
        dy = (self.n2 * co - self.n1 * si) * 26 * self.glas
        fog = cv2.remap(self.fog, self.gx + dx, self.gy + dy, cv2.INTER_LINEAR, borderMode=cv2.BORDER_REFLECT)
        hell = 1 + (self.n2 * si + self.n1 * co) * 0.12 * self.glas
        fog = fog * hell[..., None]

        m = self.maske.bei(t)
        mm = m[..., None]
        bild = fog * (1 - mm) + self.klar * mm
        # nasse Kante der Buchstaben
        e = cv2.GaussianBlur(m, (0, 0), 2.2)
        licht = (np.roll(np.roll(e, 3, axis=0), 3, axis=1) - e) * 0.30
        bild = bild + licht[..., None]
        if t > 1.2:
            perl = self.perlen[..., 3:4] * float(weich((t - 1.2) / 0.6))
            bild = bild * (1 - perl) + self.perlen[..., :3] * perl

        # Buch
        weg = float(weich((t - 7.6) / 0.4))
        sch = self.buch_schatten[..., None] * (1 - weg)
        bild = bild * (1 - sch)
        al = self.buch[..., 3:4] * (1 - weg)
        puls = float(np.exp(-((t - 1.1) / 0.45) ** 2) + 0.22 * (1 + np.sin(t * 2.2)) / 2)
        buch = self.buch[..., :3] + self.buch_glut * puls
        bild = bild * (1 - al) + buch * al

        # langsamer Push-in auf die Scheibe
        z = 1.0 + 0.035 * weich(t / 8.0)
        bw, bh = W / z, H / z
        cx, cy = self.cw * 0.48, self.ch * 0.5
        M = np.array([[W / bw, 0, -(cx - bw / 2) * W / bw], [0, H / bh, -(cy - bh / 2) * H / bh]], np.float32)
        return cv2.warpAffine(bild, M, (W, H), flags=cv2.INTER_LINEAR)

    # -- Haus ----------------------------------------------------------
    def kamera(self, t):
        a = (1190, 1632, 640.0)
        b = (1093, 1560, 2186.0)
        c = (1093, 2315, 2186.0)
        if t < 9.9:
            x = np.clip((t - 8.0) / 1.9, 0, 1)
            f = 1 - (1 - x) ** 3
            cw = a[2] ** (1 - f) * b[2] ** f
            g = (cw - a[2]) / (b[2] - a[2])
            return a[0] + (b[0] - a[0]) * g, a[1] + (b[1] - a[1]) * g, cw
        f = weich((t - 9.9) / 1.6)
        return b[0], b[1] + (c[1] - b[1]) * f, b[2]

    def haus(self, t):
        cx, cy, cw = (float(v) for v in self.kamera(t))
        ch = cw * H / W
        s = W / cw
        M = np.array([[s, 0, -(cx - cw / 2) * s], [0, s, -(cy - ch / 2) * s]], np.float32)
        fl = cv2.INTER_AREA if s < 1 else cv2.INTER_CUBIC
        rand = cv2.BORDER_REPLICATE
        bg = cv2.warpAffine(self.bg, M, (W, H), flags=fl, borderMode=rand)
        # Stehen die Figuren fast wieder am Originalplatz, zeigt das echte Cover mehr als die Fuellung
        zurueck = float(weich(1 - (2315 - cy) * TIEFE / 22))
        if zurueck > 0:
            bg = bg * (1 - zurueck) + cv2.warpAffine(self.cover, M, (W, H), flags=fl, borderMode=rand) * zurueck

        # Fenster flackern unabhaengig voneinander, das blaue atmet
        w = cv2.warpAffine(self.warm, M, (W, H), flags=cv2.INTER_LINEAR)
        n = cv2.warpAffine(self.f1 * float(np.cos(t * 3.1)) + self.f2 * float(np.sin(t * 4.3)), M, (W, H), flags=cv2.INTER_LINEAR)
        bg = bg * (1 + (w * n * 0.9)[..., None])
        bl = cv2.warpAffine(self.blau, M, (W, H), flags=cv2.INTER_LINEAR)
        bg = bg * (1 + (bl * 0.16 * float(np.sin(t * 2.4)))[..., None])

        # Zeile im Bild -> Hoehe im Cover
        szene = cy + (self.yy - H / 2) / s

        # Pflaster glitzert
        pflaster = weich((szene - 2560) / 120)
        if pflaster.max() > 0.01:
            dx = np.sin(self.yy / 7.0 + t * 6.0) * 3.5 * pflaster
            bg = cv2.remap(bg, self.xx + dx, self.yy, cv2.INTER_LINEAR, borderMode=cv2.BORDER_REPLICATE)

        # Nebel hinter den Figuren
        lage = int((t * 46) % W)
        nb = self.nebel1[:, lage:lage + W]
        boden = weich((szene - 1950) / 620) * weich((3150 - szene) / 200)
        a = np.clip((nb - 0.35) * 1.5, 0, 1) * boden * 0.42
        bg = bg * (1 - a[..., None]) + np.array((0.50, 0.58, 0.72), np.float32) * a[..., None]

        # Figuren eilen der Kamera voraus: das erzeugt die Tiefe
        versatz = (2315 - cy) * TIEFE
        M2 = M.copy()
        M2[1, 2] += versatz * s
        fa = cv2.warpAffine(self.fg_a, M2, (W, H), flags=cv2.INTER_LINEAR)
        if fa.max() > 0.01:
            fg = cv2.warpAffine(self.cover, M2, (W, H), flags=fl, borderMode=rand)
            bg = bg * (1 - fa[..., None]) + fg * fa[..., None]

        # duenner Schleier vor den Figuren
        lage2 = int((W - t * 74) % W)
        nv = self.nebel2[:, lage2:lage2 + W]
        a2 = np.clip((nv - 0.45) * 1.4, 0, 1) * weich((szene - 2500) / 500) * 0.22
        return bg * (1 - a2[..., None]) + np.array((0.55, 0.62, 0.76), np.float32) * a2[..., None]

    # -- Schluss -------------------------------------------------------
    def ende(self, t):
        bild = self.ende_bild + self.ende_glut * float(0.24 * (1 + np.sin(t * 2.2)))
        z = 1.0 + 0.03 * weich((t - 11.4) / 3.6)
        M = np.array([[z, 0, -(z - 1) * 1340], [0, z, -(z - 1) * 540]], np.float32)
        bild = cv2.warpAffine(bild, M, (W, H), flags=cv2.INTER_LINEAR, borderMode=cv2.BORDER_REPLICATE)

        # warme Lichtpartikel
        schicht = np.zeros((H, W), np.float32)
        for x, y, v, r, ph in self.funken:
            yy = (y - t * v) % H
            xx = x + np.sin(t * 0.6 + ph) * 14
            hell = 0.55 + 0.45 * np.sin(t * 1.3 + ph)
            cv2.circle(schicht, (int(xx), int(yy)), int(r + 0.5), float(hell), -1, cv2.LINE_AA)
        schicht = cv2.GaussianBlur(schicht, (0, 0), 1.6)
        bild = bild + schicht[..., None] * np.array((0.55, 0.40, 0.20), np.float32)

        d = weich((t - 11.7) / 0.35)
        auflegen(bild, self.t4, d, int((1 - d) * 16))
        return bild

    def bild(self, t):
        if t < T_HAUS[1]:
            f = self.scheibe(t)
            for e, (a, b) in ((self.t1, T_TEXT1), (self.t2, T_TEXT2)):
                d = fenster(t, a, b)
                auflegen(f, e, d, int((1 - weich((t - a) / 0.3)) * 14))
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
            auflegen(f, self.t3, fenster(t, *T_FRAGE), int((1 - weich((t - T_FRAGE[0]) / 0.3)) * 14))
        f = f + self.korn[int(t * FPS) % len(self.korn)]
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

    pfad = os.path.join(OUT_DIR, f"Band1_Video_{VERSION}.mp4")
    kmd = ["ffmpeg", "-y", "-v", "error",
           "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{W}x{H}", "-r", str(FPS), "-i", "-",
           "-f", "lavfi", "-t", str(DAUER), "-i", "anoisesrc=c=brown:a=0.012:r=48000,lowpass=f=500,aformat=channel_layouts=stereo",
           "-c:v", "libx264", "-profile:v", "main", "-preset", "slow", "-crf", "19", "-pix_fmt", "yuv420p",
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
