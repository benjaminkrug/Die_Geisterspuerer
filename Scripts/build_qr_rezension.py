"""
Erzeugt die Rezensions-QR-Codes fuer alle Baende der Geisterspuerer-Reihe.

Jeder Code fuehrt DIREKT auf das Amazon-Bewertungsformular des jeweiligen Bandes
(nicht nur auf die Produktseite) — genauso wie der bereits gedruckte Band-1-Code.

★ JEDER erzeugte Code wird nach dem Schreiben mit OpenCV WIEDER EINGELESEN und
  gegen die Soll-URL geprueft. Ein QR-Code, der im gedruckten Buch ins Leere
  fuehrt, waere nicht mehr korrigierbar — deshalb hier keine Annahme, sondern
  eine Messung.

Verwendung:
    py Scripts/build_qr_rezension.py
"""

import os
import sys

import qrcode
import cv2

_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# ASINs der Taschenbuch-Ausgaben (vom Autor 2026-07-18)
ASIN = {
    1: "B0GNZVXDDJ",   # Das Haus, das fluestert   (bereits gedruckt)
    2: "B0GV8R8QJ6",   # Der Friedhof ohne Namen
    3: "B0H4VQHBLX",   # Schatten sieht mehr
    4: "B0H869XC17",   # Die zugemauerte Tuer
    5: "B0H9DJF3T9",   # Der Schleier
}

URL_MUSTER = "https://www.amazon.de/review/create-review?asin={asin}"


def pfad(band: int) -> str:
    return os.path.join(_ROOT, f"Band{band}", "Cover", f"qr_rezension_band{band}.png")


def erzeuge(band: int, ueberschreiben: bool = False) -> bool:
    ziel = pfad(band)
    soll_url = URL_MUSTER.format(asin=ASIN[band])

    if os.path.exists(ziel) and not ueberschreiben:
        ist = dekodiere(ziel)
        if ist == soll_url:
            print(f"  Band {band}: existiert bereits und stimmt — unveraendert")
            return True
        print(f"  Band {band}: existiert, enthaelt aber {ist!r} statt {soll_url!r}")
        return False

    os.makedirs(os.path.dirname(ziel), exist_ok=True)

    qr = qrcode.QRCode(
        version=None,
        error_correction=qrcode.constants.ERROR_CORRECT_M,  # 15 % Fehlertoleranz
        box_size=12,
        border=4,          # KDP/Print: stiller Rand ist Pflicht, sonst unscannbar
    )
    qr.add_data(soll_url)
    qr.make(fit=True)
    bild = qr.make_image(fill_color="black", back_color="white")
    bild.save(ziel)

    # ── Gegenprobe: Datei wieder einlesen und dekodieren ──────────────────
    ist = dekodiere(ziel)
    if ist != soll_url:
        print(f"  Band {band}: !! GEGENPROBE FEHLGESCHLAGEN")
        print(f"             erwartet: {soll_url}")
        print(f"             gelesen : {ist!r}")
        return False

    from PIL import Image
    w, h = Image.open(ziel).size
    print(f"  Band {band}: erzeugt + gegengelesen OK  ({w}x{h} px)  {soll_url}")
    return True


def dekodiere(png_pfad: str):
    img = cv2.imread(png_pfad)
    if img is None:
        return None
    data, _, _ = cv2.QRCodeDetector().detectAndDecode(img)
    return data or None


def main():
    ueberschreiben = "--force" in sys.argv
    print("=" * 70)
    print("Rezensions-QR-Codes — Die Geisterspuerer")
    print("=" * 70)
    ok = True
    for band in sorted(ASIN):
        if not erzeuge(band, ueberschreiben):
            ok = False
    print()
    if ok:
        print("Alle QR-Codes vorhanden und verifiziert.")
    else:
        print("!! Mindestens ein Code stimmt nicht — siehe oben.")
        sys.exit(1)


if __name__ == "__main__":
    main()
