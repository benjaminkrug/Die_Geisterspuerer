# -*- coding: utf-8 -*-
"""
Baut das KDP-Vollcover fuer Staffel 2, Band 5 ("Der letzte Schluessel") aus
Vorderseite + Rueckseite. Abgeleitet von build_cover_s2_4.py, verwendet
dieselben geprueften Funktionen aus build_cover.py.

    py Scripts/build_cover_s2_5.py --seiten 109 --final

★ SEITENZAHL IST GEMESSEN: 109 Seiten aus Output/S2-5/KDP_S2-5_Manuskript.pdf
  (Build 2026-11-02), OHNE Widmung/Epigraph. Kommen die noch dazu: Manuskript
  neu bauen, Seitenzahl neu ablesen, dieses Skript mit der neuen Zahl laufen
  lassen.

★ QUELLBILDER: vorderseite.jpg, aber rueckseite.png (gemischt, so geliefert).
"""
import argparse
import os
import sys

_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(_ROOT, "Scripts"))

from PIL import Image
import build_cover as bc  # geprueftes Basisskript, Funktionen wiederverwendet (wrappt stdout selbst)

TITEL = "Der letzte Schlüssel"
GEMESSENE_SEITEN = 109  # aus Output/S2-5/KDP_S2-5_Manuskript.pdf, OHNE Widmung/Epigraph
COVER_DIR = os.path.join(_ROOT, "Staffel2", "S2-5", "Cover")

TEXT_HELL = 170   # Graustufe, ab der ein Pixel als Schrift gilt (Schrift ~180-245, Grund ~5)


def textzeilen(arr, oben=0.20, unten=0.12):
    """Erste und letzte Pixelzeile mit Schrift: im oberen und im unteren Bildstreifen,
    mittlere 70 % der Breite. Die Szene in der Mitte wird bewusst nicht durchsucht."""
    import numpy as np
    g = np.asarray(Image.fromarray(arr).convert("L")) if not isinstance(arr, Image.Image) \
        else np.asarray(arr.convert("L"))
    h, w = g.shape
    mitte = g[:, int(0.15 * w):int(0.85 * w)] > TEXT_HELL
    zeilen = mitte.sum(axis=1) > 8
    top = np.nonzero(zeilen[:int(oben * h)])[0]
    bot = np.nonzero(zeilen[int((1 - unten) * h):])[0]
    return (int(top[0]) if top.size else None,
            int(bot[-1]) + int((1 - unten) * h) if bot.size else None)


def front_mit_textrand(pfad, w, h):
    """Vorderseite S2-5: Das Bildmodell hat die Reihenzeile 2,3 mm unter die
    Trimmkante gesetzt (verlangt waren 13 %). Statt neu zu generieren wird nach
    Reihenstandard die Leinwand vergroessert: Bild so weit verkleinern, dass
    oben und unten SAFE_TEXT frei bleibt, Rest mit gespiegeltem Bildrand fuellen.
    Links (Ruecken-Seite) buendig, damit die Fuellung rechts im Anschnitt liegt."""
    import numpy as np
    im = Image.open(pfad).convert("RGB")
    sw, sh = im.size
    top, bot = textzeilen(im)
    rand = (bc.BLEED + bc.SAFE_TEXT) * bc.DPI
    s_fill = max(w / sw, h / sh)
    s_text = (h - 2 * rand) / (bot - top)
    s = min(s_fill, s_text)
    nw, nh = round(sw * s), round(sh * s)
    arr = np.asarray(im.resize((nw, nh), Image.LANCZOS))
    # y-Versatz: Mitte des erlaubten Bereichs
    y_min, y_max = rand - top * s, (h - rand) - bot * s
    y0 = round((y_min + y_max) / 2) if s < s_fill else round((h - nh) / 2)
    pt, pb = max(0, y0), max(0, h - (y0 + nh))
    pr = max(0, w - nw)
    arr = np.pad(arr, ((pt, pb), (0, pr), (0, 0)), mode="reflect")
    arr = arr[max(0, -y0):max(0, -y0) + h, :w]
    sicht_oben = max(0, pt - bc.BLEED * bc.DPI)
    sicht_unten = max(0, pb - bc.BLEED * bc.DPI)
    sicht_rechts = max(0, pr - bc.BLEED * bc.DPI)
    print(f"  Vorderseite: Text {top}-{bot} px, Skalierung {s:.4f} statt {s_fill:.4f} "
          f"(Quellbild effektiv {sw / (nw / bc.DPI):.0f} dpi)")
    print(f"  Fuellung (gespiegelt): oben {pt}, unten {pb}, rechts {pr} px -- "
          f"davon sichtbar nach dem Schnitt: {sicht_oben:.0f} / {sicht_unten:.0f} / {sicht_rechts:.0f} px")
    return Image.fromarray(arr)


def textabstand_pruefen(canvas, x0, x1, name):
    """Misst am FERTIGEN Vollcover den Abstand der Schrift zur Trimmkante.
    Grund: pruefe_zonen() mittelt ueber den ganzen Rand und hat die 2,3 mm der
    ersten S2-5-Vorderseite nicht gemeldet."""
    top, bot = textzeilen(canvas.crop((x0, 0, x1, canvas.height)))
    trim = bc.BLEED * bc.DPI
    o = (top - trim) / bc.DPI * 25.4
    u = (canvas.height - trim - bot) / bc.DPI * 25.4
    soll = bc.SAFE_TEXT * 25.4
    ok = o >= soll - 0.1 and u >= soll - 0.1
    print(f"  {name}: Schrift {o:.1f} mm unter / {u:.1f} mm ueber der Trimmkante "
          f"(Soll >= {soll:.1f} mm) -- {'ok' if ok else 'ZU NAH'}")
    return None if ok else f"{name}: Schrift zu nah an der Trimmkante ({o:.1f} / {u:.1f} mm)."


def main():
    ap = argparse.ArgumentParser(description="KDP-Vollcover Staffel 2, Band 5")
    ap.add_argument("--front", default=os.path.join(COVER_DIR, "vorderseite.jpg"))
    ap.add_argument("--back", default=os.path.join(COVER_DIR, "rueckseite.png"))
    ap.add_argument("--seiten", type=int, default=GEMESSENE_SEITEN)
    ap.add_argument("--final", action="store_true",
                     help="ohne dieses Flag landet der Output in Output/S2-5/Draft/")
    ap.add_argument("--unscharf-erlauben", action="store_true", dest="unscharf")
    ap.add_argument("--schaerfe", type=int, default=60)
    ap.add_argument("--tiefen", type=float, default=0.10)
    args = ap.parse_args()

    veraltet_moeglich = args.seiten == GEMESSENE_SEITEN
    final = args.final
    if args.final and veraltet_moeglich:
        print("⚠️  --final mit der zuletzt gemessenen Seitenzahl (109) -- diese gilt nur,")
        print("    solange Widmung/Epigraph noch nicht freigegeben sind. Falls seitdem")
        print("    freigegeben und neu gebaut wurde: Taschenbuch-PDF neu pruefen, echte")
        print("    Seitenzahl neu ablesen, dann erst hier eintragen.")
        print()

    TRIM_W, TRIM_H = bc.FORMATE["6x9"]
    faktor = bc.PAPIER["weiss"]
    seiten = args.seiten
    spine_in = seiten * faktor
    total_w_in = 2 * (TRIM_W + bc.BLEED) + spine_in
    total_h_in = TRIM_H + 2 * bc.BLEED
    TW, TH = round(total_w_in * bc.DPI), round(total_h_in * bc.DPI)
    panel_w = round((TRIM_W + bc.BLEED) * bc.DPI)
    spine_w = TW - 2 * panel_w

    print("=" * 68)
    print(f"KDP-Vollcover -- Die Geisterspuerer, Die Gebundenen, Band 5: {TITEL}")
    print("=" * 68)
    print(f"  Seiten     : {seiten} (weisses Papier, Faktor {faktor})"
          + ("   << aus dem echten Taschenbuch-PDF, OHNE Frontmatter >>"
             if veraltet_moeglich else ""))
    print(f"  Ruecken    : {spine_in:.3f} Zoll = {spine_in*25.4:.1f} mm = {spine_w} px")
    print(f"  Gesamt     : {TW} x {TH} px ({total_w_in:.3f} x {total_h_in:.3f} Zoll)")
    print()

    print("Quellbilder:")
    p_back = bc.lade_und_einpassen(args.back, panel_w, TH, "Rueckseite", args.unscharf)
    bc.lade_und_einpassen(args.front, panel_w, TH, "Vorderseite", args.unscharf)  # nur Aufloesungspruefung
    p_front = front_mit_textrand(args.front, panel_w, TH)
    print()

    c1 = bc.randfarbe(p_back, "rechts")
    c2 = bc.randfarbe(p_front, "links")
    bg = tuple(int((a + b) / 2) for a, b in zip(c1, c2))
    print(f"  Ruecken-Hintergrundfarbe aus den Bildraendern gemessen: RGB{bg}")

    # erzwingen=True wie bei S2-2 bis S2-4: bewusste Entscheidung fuer
    # Bandnummer+Titel statt eines leeren Rueckens (S2-4 so bei KDP durchgegangen).
    strip, info = bc.zeichne_ruecken(spine_w, TH, bg, "5", TITEL, seiten, erzwingen=True)
    if info:
        print("  Ruecken gesetzt: " + ", ".join(info))
    print()

    canvas = Image.new("RGB", (TW, TH), bg)
    canvas.paste(p_back, (0, 0))
    canvas.paste(p_front, (panel_w + spine_w, 0))
    canvas = bc.weiche_falz(canvas, panel_w, panel_w + spine_w - 1, bg)
    canvas.paste(strip, (panel_w, 0))

    warnungen = bc.pruefe_zonen(canvas, panel_w, spine_w, TRIM_W, TRIM_H)
    print("Textabstand am fertigen Vollcover:")
    for x0, x1, name in [(0, panel_w, "Rueckseite"), (panel_w + spine_w, TW, "Vorderseite")]:
        w_ = textabstand_pruefen(canvas, x0, x1, name)
        if w_:
            warnungen.append(w_)
    print()

    druck = bc.nachschaerfen(canvas, args.schaerfe)
    druck = bc.tiefen_anheben(druck, args.tiefen)

    out_dir = os.path.join(_ROOT, "Output", "S2-5") if final else \
        os.path.join(_ROOT, "Output", "S2-5", "Draft")
    os.makedirs(out_dir, exist_ok=True)
    prefix = "KDP_S2-5_Cover" if final else "DRAFT_S2-5_Cover"
    p_pdf = os.path.join(out_dir, f"{prefix}_Vollcover_300dpi.pdf")
    p_jpg = os.path.join(out_dir, f"{prefix}_Vollcover_300dpi.jpg")
    p_ctl = os.path.join(out_dir, f"{prefix}_KONTROLLE.jpg")
    p_thm = os.path.join(out_dir, f"{prefix}_thumbnail_150.png")
    p_ebk = os.path.join(out_dir, f"{prefix}_eBook_1600x2560.jpg")

    druck.save(p_jpg, quality=95, dpi=(bc.DPI, bc.DPI))
    import img2pdf
    with open(p_pdf, "wb") as f:
        f.write(img2pdf.convert(p_jpg, layout_fun=img2pdf.get_layout_fun(
            (img2pdf.in_to_pt(total_w_in), img2pdf.in_to_pt(total_h_in)))))

    ebook_src = Image.open(args.front).convert("RGB")
    sw, sh = ebook_src.size
    sc = max(bc.EBOOK_W / sw, bc.EBOOK_H / sh)
    ebook_src = ebook_src.resize((round(sw * sc), round(sh * sc)), Image.LANCZOS)
    l, t = (ebook_src.width - bc.EBOOK_W) // 2, (ebook_src.height - bc.EBOOK_H) // 2
    ebook_src.crop((l, t, l + bc.EBOOK_W, t + bc.EBOOK_H)).save(p_ebk, quality=95)

    bc.kontrollbild(druck, panel_w, spine_w, TRIM_W, TRIM_H, p_ctl)
    thumb = druck.crop((panel_w + spine_w, 0, TW, TH))
    thumb.resize((150, round(150 * TH / panel_w)), Image.LANCZOS).save(p_thm)

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
        print(f"  PDF misst {ist_w:.3f} x {ist_h:.3f} Zoll -- korrekt.")

    print()
    print("=" * 68)
    for pfad, was in [(p_pdf, "Vollcover PDF"),
                       (p_jpg, "Vollcover JPG"),
                       (p_ebk, "eBook-Cover (JPG, 1:1.6)"),
                       (p_ctl, "KONTROLLBILD -- ANSEHEN, mit KDP-Linien"),
                       (p_thm, "Thumbnail 150 -- ANSEHEN")]:
        print(f"  {was}\n    {pfad}")

    if not final:
        print()
        print("‼️  DRAFT -- NICHT fuer den KDP-Upload. --final nicht gesetzt.")
        print("    py Scripts/build_cover_s2_5.py --seiten 109 --final")

    if warnungen:
        print()
        print("!! WARNUNGEN:")
        for w_ in warnungen:
            print("   - " + w_)


if __name__ == "__main__":
    main()
