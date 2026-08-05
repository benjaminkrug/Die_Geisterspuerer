"""
Check cover file dimensions, resolution, and KDP compliance.

Supports PDF, PNG, JPG/JPEG files.
Usage: python check_cover.py [file_path]
       Without argument: checks all cover files in the current directory.
"""
import sys
import os
from pathlib import Path

# KDP target dimensions
KDP_EBOOK_W, KDP_EBOOK_H = 1600, 2560  # Amazon recommended ideal
KDP_FRONT_W, KDP_FRONT_H = 1575, 2475  # 5.25x8.25 in @ 300 DPI (with bleed)
KDP_SPREAD_W, KDP_SPREAD_H = 3210, 2475  # Full spread: front + spine + back

BASE_DIR = Path(r"C:\Users\krugb\OneDrive\Desktop\GMBH\Projekte\Buecher\Die_Schattenjaeger\Band1\Cover\Bilder")


def check_pdf(path):
    """Check PDF cover: page dimensions, embedded images, DPI."""
    try:
        import fitz
    except ImportError:
        print("PyMuPDF nicht installiert. Installiere mit: pip install PyMuPDF")
        return

    doc = fitz.open(str(path))
    file_size_mb = os.path.getsize(path) / (1024 * 1024)
    print(f"  Dateigroesse: {file_size_mb:.1f} MB")

    for i, page in enumerate(doc):
        rect = page.rect
        w_in = rect.width / 72
        h_in = rect.height / 72
        w_cm = w_in * 2.54
        h_cm = h_in * 2.54
        print(f"  Seite {i+1}: {rect.width:.0f} x {rect.height:.0f} pt = {w_in:.2f} x {h_in:.2f} in = {w_cm:.1f} x {h_cm:.1f} cm")

        images = page.get_images()
        print(f"  Eingebettete Bilder: {len(images)}")
        for img in images:
            xref = img[0]
            base_image = doc.extract_image(xref)
            w = base_image["width"]
            h = base_image["height"]
            size_kb = len(base_image["image"]) / 1024
            ext = base_image["ext"]
            dpi_w = w / w_in if w_in > 0 else 0
            dpi_h = h / h_in if h_in > 0 else 0
            print(f"    Bild: {w}x{h} px, {size_kb:.0f} KB, Format: {ext}, ~{dpi_w:.0f} DPI")

            # KDP compliance check
            check_kdp_compliance(w, h, "PDF-Bild")

    doc.close()


def check_image(path):
    """Check image file (PNG/JPG): dimensions, DPI, KDP compliance."""
    try:
        from PIL import Image
    except ImportError:
        print("  Pillow nicht installiert. Installiere mit: pip install Pillow")
        return

    file_size_mb = os.path.getsize(path) / (1024 * 1024)
    print(f"  Dateigroesse: {file_size_mb:.1f} MB")

    img = Image.open(str(path))
    w, h = img.size
    print(f"  Pixel: {w} x {h} px")
    print(f"  Seitenverhaeltnis: {w/h:.3f} (Ziel 2:3 = {2/3:.3f}, eBook = {1600/2560:.3f})")

    dpi = img.info.get("dpi", (None, None))
    if dpi[0]:
        print(f"  DPI: {dpi[0]:.0f} x {dpi[1]:.0f}")
        w_in = w / dpi[0]
        h_in = h / dpi[1]
        print(f"  Druckgroesse bei DPI: {w_in:.2f} x {h_in:.2f} in = {w_in*2.54:.1f} x {h_in*2.54:.1f} cm")
    else:
        print(f"  DPI: nicht eingebettet")
        print(f"  Bei 300 DPI: {w/300:.2f} x {h/300:.2f} in = {w/300*2.54:.1f} x {h/300*2.54:.1f} cm")

    img.close()
    check_kdp_compliance(w, h, "Bild")


def check_kdp_compliance(w, h, label):
    """Check pixel dimensions against KDP targets."""
    print(f"\n  --- KDP-Kompatibilitaet ({label}: {w}x{h} px) ---")

    # Check against eBook
    ebook_ok = w >= KDP_EBOOK_W and h >= KDP_EBOOK_H
    status = "OK" if ebook_ok else "ZU KLEIN"
    print(f"  eBook-Cover (1600x2560):     [{status}] {'Passt!' if ebook_ok else f'Fehlt: {max(0, KDP_EBOOK_W-w)}x{max(0, KDP_EBOOK_H-h)} px'}")

    # Check against front cover with bleed
    front_ok = w >= KDP_FRONT_W and h >= KDP_FRONT_H
    status = "OK" if front_ok else "ZU KLEIN"
    print(f"  TB-Frontcover (1575x2475):   [{status}] {'Passt!' if front_ok else f'Fehlt: {max(0, KDP_FRONT_W-w)}x{max(0, KDP_FRONT_H-h)} px'}")

    # Check against full spread
    spread_ok = w >= KDP_SPREAD_W and h >= KDP_SPREAD_H
    status = "OK" if spread_ok else "ZU KLEIN"
    print(f"  TB-Vollumschlag (3210x2475):  [{status}] {'Passt!' if spread_ok else f'Fehlt: {max(0, KDP_SPREAD_W-w)}x{max(0, KDP_SPREAD_H-h)} px'}")

    # Upscale recommendation
    if not ebook_ok or not front_ok:
        max_needed_w = max(KDP_EBOOK_W, KDP_FRONT_W)
        max_needed_h = max(KDP_EBOOK_H, KDP_FRONT_H)
        scale = max(max_needed_w / w, max_needed_h / h)
        print(f"  Empfehlung: Upscale um Faktor {scale:.2f}x (z.B. mit Magnific AI oder letsenhance.io)")

    # DPI at print size (5x8 trim)
    dpi_at_print = min(w / 5.25, h / 8.25)
    status = "OK" if dpi_at_print >= 300 else "UNTER 300"
    print(f"  DPI bei 5.25x8.25in Druck:   [{status}] ~{dpi_at_print:.0f} DPI")


def find_cover_files():
    """Find all cover-related files in the project directory."""
    patterns = ["*cover*", "*Cover*", "*COVER*", "DIE_Geisterspuerer_v*", "DIE Geisterspuerer*"]
    extensions = {".pdf", ".png", ".jpg", ".jpeg", ".tiff"}
    found = set()
    for pattern in patterns:
        for f in BASE_DIR.glob(pattern):
            if f.suffix.lower() in extensions and f.is_file():
                found.add(f)
    return sorted(found)


def main():
    if len(sys.argv) > 1:
        # Check specific file
        path = Path(sys.argv[1])
        if not path.is_absolute():
            path = BASE_DIR / path
        files = [path]
    else:
        # Find all cover files
        files = find_cover_files()
        if not files:
            print("Keine Cover-Dateien gefunden.")
            return
        print(f"Gefundene Cover-Dateien: {len(files)}\n")

    for path in files:
        if not path.exists():
            print(f"FEHLER: Datei nicht gefunden: {path}")
            continue

        print(f"{'='*60}")
        print(f"DATEI: {path.name}")
        print(f"{'='*60}")

        ext = path.suffix.lower()
        if ext == ".pdf":
            check_pdf(path)
        elif ext in (".png", ".jpg", ".jpeg", ".tiff"):
            check_image(path)
        else:
            print(f"  Nicht unterstuetztes Format: {ext}")

        print()


if __name__ == "__main__":
    main()
