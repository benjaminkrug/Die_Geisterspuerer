# -*- coding: utf-8 -*-
"""
Baut das KDP-Vollcover fuer Staffel 2, Band 1 ("Der Gast, der blieb") aus
Vorderseite + Rueckseite. Wiederverwendet die geprueften Funktionen aus
build_cover.py (Zuschnitt ohne Verzerrung, Ruecken zeichnen, weicher Falz,
Nachschaerfen, Tiefenanhebung, Selbstpruefung) statt sie zu duplizieren.

    py Scripts/build_cover_s2_1.py --seiten 102

★ DIE SEITENZAHL IST NUR GESCHAETZT (16.723 Woerter bei ~163,5 W/Seite).
  Ohne --schaetzung-freigeben bricht das Skript ab und baut NUR einen
  DRAFT-Ordner (Output/S2-1/Draft/), klar so benannt -- kein KDP-Upload-Pfad.
  Sobald das Taschenbuch-PDF gebaut ist und die echte Seitenzahl feststeht,
  --seiten <echte Zahl> --final setzen -> Output landet in Output/S2-1/.
"""
import argparse
import os
import sys

_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(_ROOT, "Scripts"))

from PIL import Image
import build_cover as bc  # geprueftes Basisskript, Funktionen wiederverwendet (wrappt stdout selbst)

TITEL = "Der Gast, der blieb"
GESCHAETZTE_SEITEN = 102
COVER_DIR = os.path.join(_ROOT, "Staffel2", "S2-1", "Cover")


def main():
    ap = argparse.ArgumentParser(description="KDP-Vollcover Staffel 2, Band 1")
    ap.add_argument("--front", default=os.path.join(COVER_DIR, "vorderseite.png"))
    ap.add_argument("--back", default=os.path.join(COVER_DIR, "rueckseite.png"))
    ap.add_argument("--seiten", type=int, default=GESCHAETZTE_SEITEN)
    ap.add_argument("--final", action="store_true",
                     help="ohne dieses Flag landet der Output in Output/S2-1/Draft/")
    ap.add_argument("--unscharf-erlauben", action="store_true", dest="unscharf")
    ap.add_argument("--schaerfe", type=int, default=60)
    ap.add_argument("--tiefen", type=float, default=0.10)
    args = ap.parse_args()

    ist_schaetzung = args.seiten == GESCHAETZTE_SEITEN
    final = args.final and not ist_schaetzung
    if args.final and ist_schaetzung:
        print("!! --final ignoriert: --seiten wurde nicht auf die echte, aus dem")
        print("   Taschenbuch-PDF abgelesene Zahl gesetzt. Es bleibt ein DRAFT.")
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
    print(f"KDP-Vollcover -- Die Geisterspuerer, Die Gebundenen, Band 1: {TITEL}")
    print("=" * 68)
    print(f"  Seiten     : {seiten} (weisses Papier, Faktor {faktor})"
          + ("   << GESCHAETZT, KEIN KDP-UPLOAD >>" if ist_schaetzung else ""))
    print(f"  Ruecken    : {spine_in:.3f} Zoll = {spine_in*25.4:.1f} mm = {spine_w} px")
    print(f"  Gesamt     : {TW} x {TH} px ({total_w_in:.3f} x {total_h_in:.3f} Zoll)")
    print()

    print("Quellbilder:")
    p_back = bc.lade_und_einpassen(args.back, panel_w, TH, "Rueckseite", args.unscharf)
    p_front = bc.lade_und_einpassen(args.front, panel_w, TH, "Vorderseite", args.unscharf)
    print()

    c1 = bc.randfarbe(p_back, "rechts")
    c2 = bc.randfarbe(p_front, "links")
    bg = tuple(int((a + b) / 2) for a, b in zip(c1, c2))
    print(f"  Ruecken-Hintergrundfarbe aus den Bildraendern gemessen: RGB{bg}")

    strip, info = bc.zeichne_ruecken(spine_w, TH, bg, "1", TITEL, seiten)
    if info:
        print("  Ruecken gesetzt: " + ", ".join(info))
    print()

    canvas = Image.new("RGB", (TW, TH), bg)
    canvas.paste(p_back, (0, 0))
    canvas.paste(p_front, (panel_w + spine_w, 0))
    canvas = bc.weiche_falz(canvas, panel_w, panel_w + spine_w - 1, bg)
    canvas.paste(strip, (panel_w, 0))

    warnungen = bc.pruefe_zonen(canvas, panel_w, spine_w, TRIM_W, TRIM_H)

    druck = bc.nachschaerfen(canvas, args.schaerfe)
    druck = bc.tiefen_anheben(druck, args.tiefen)

    out_dir = os.path.join(_ROOT, "Output", "S2-1") if final else \
        os.path.join(_ROOT, "Output", "S2-1", "Draft")
    os.makedirs(out_dir, exist_ok=True)
    prefix = "KDP_S2-1_Cover" if final else "DRAFT_S2-1_Cover"
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
        print("‼️  DRAFT -- NICHT fuer den KDP-Upload. Die Seitenzahl ist geschaetzt.")
        print("    Erst Taschenbuch-PDF bauen, echte Seitenzahl ablesen, dann:")
        print("    py Scripts/build_cover_s2_1.py --seiten <echt> --final")

    if warnungen:
        print()
        print("!! WARNUNGEN:")
        for w_ in warnungen:
            print("   - " + w_)


if __name__ == "__main__":
    main()
