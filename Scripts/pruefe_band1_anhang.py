"""
Prueft die GEBAUTEN Band-1-Dateien (Taschenbuch- und eBook-DOCX), nicht die Skripte.
Schritt 1 des Plans Band1/PLAN_Durchlesequote.md, Kontrollen (a)-(e).

    py Scripts/build_qr_rezension.py
    py Scripts/build_taschenbuch_docx.py
    py Scripts/build_ebook_docx.py
    py Scripts/pruefe_band1_anhang.py

Exit-Code 0 nur, wenn beide Dateien hochladbar sind.
"""
import hashlib
import os
import re
import sys
import zipfile

from docx import Document

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import band1_anhang as anhang  # noqa: E402

_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TASCHENBUCH = os.path.join(_ROOT, "Output", "Band1", "KDP_Band1_Manuskript.docx")
EBOOK = os.path.join(_ROOT, "Output", "Band1", "KDP_Band1_eBook.docx")
ORNAMENTE = {"✦  ✦  ✦", "* * *"}

fehler = []
hinweise = []


def check(ok, text):
    print(("  ✓ " if ok else "  ✗ ") + text)
    if not ok:
        fehler.append(text)


def absaetze(pfad):
    return [p.text.strip() for p in Document(pfad).paragraphs if p.text.strip()]


def md5(daten):
    return hashlib.md5(daten).hexdigest()


def pruefe_gemeinsam(name, pfad):
    print(f"\n{name}: {os.path.relpath(pfad, _ROOT)}")
    if not os.path.isfile(pfad):
        check(False, "Datei fehlt -- erst bauen")
        return None
    voll = absaetze(pfad)
    text = "\n".join(voll)

    # (a) Leseprobe: vollstaendig, in Reihenfolge, woertlich aus Band 2
    soll, woerter = anhang.pruefe_leseprobe()
    soll_text = [a for a in soll if a != anhang.SZENENWECHSEL]
    try:
        start = voll.index(soll_text[0])
        ist = [a for a in voll[start:start + len(soll)] if a not in ORNAMENTE]
        check(ist == soll_text, f"(a) Leseprobe: {len(soll_text)} Absaetze / {woerter} Woerter, "
                                f"woertlich aus Band 2 und in Reihenfolge")
    except ValueError:
        check(False, "(a) Leseprobe nicht gefunden")
    check(not any(a.startswith(anhang.LESEPROBE_AUSLASSEN) for a in voll),
          "(a) ausgelassener Absatz (Baeume/Kastanien) steht nicht im Buch")

    # (b) Reste der alten, erfundenen Leseprobe
    alt = [s for s in ("Erscheint 2026", "Heinrich M.", "vor drei Wochen", "überall erhältlich")
           if s in text]
    check(not alt, f"(b) keine Reste der alten Leseprobe {alt or ''}")

    # (d) Anfuehrungszeichen
    auf, zu, ascii_ = text.count("„"), text.count("“"), text.count('"')
    doppelt = re.findall(r"„[^“\n]*„", text)
    check(auf == zu and ascii_ == 0 and not doppelt,
          f"(d) Anführungszeichen: „ {auf} / “ {zu} / gerade {ascii_} / doppelt öffnend {len(doppelt)}")

    # (e) Fehl-Ornamente: vor einer Kapitelueberschrift oder am Buchende
    vor_kapitel = [voll[i + 1][:30] for i, p in enumerate(voll[:-1])
                   if p in ORNAMENTE and voll[i + 1].startswith("Kapitel ")]
    ende = voll.index("Wie geht es weiter?")
    am_ende = voll[ende - 1] in ORNAMENTE
    check(not vor_kapitel and not am_ende,
          f"(e) Fehl-Ornamente: vor Kapiteln {len(vor_kapitel)}, am Buchende {int(am_ende)}")

    # Seit 2026-10-14 steht jeder Kapiteltitel zusaetzlich im festen Inhaltsverzeichnis (eBook)
    # -> verschiedene Titel zaehlen, und jeder darf hoechstens zweimal vorkommen.
    kapitel = [p for p in voll if re.match(r"Kapitel \d+ – ", p)]
    titel = set(kapitel)
    check(len(titel) == 17 and all(kapitel.count(k) <= 2 for k in titel),
          f"16 Kapitel + Leseprobe-Kapitel ({len(titel)} verschiedene Ueberschriften)")
    return voll


def pruefe_taschenbuch():
    if pruefe_gemeinsam("TASCHENBUCH", TASCHENBUCH) is None:
        return
    # (c) QR-Codes: die eingebetteten Bilder muessen exakt die geprueften Dateien sein
    with zipfile.ZipFile(TASCHENBUCH) as z:
        bilder = {md5(z.read(n)) for n in z.namelist() if n.startswith("word/media/")}
    for name, pfad, url in (("weiter zu Band 2", anhang.QR_BAND2, anhang.BAND2_URL),
                            ("Rezension", anhang.QR_REZENSION, anhang.REZENSION_URL)):
        if not os.path.isfile(pfad):
            check(False, f"(c) QR {name}: {os.path.relpath(pfad, _ROOT)} fehlt "
                         f"(Buch wurde mit --entwurf gebaut, NICHT hochladen)")
            continue
        with open(pfad, "rb") as f:
            check(md5(f.read()) in bilder, f"(c) QR {name}: eingebettet = {os.path.basename(pfad)}")
        try:
            import cv2
            data, _, _ = cv2.QRCodeDetector().detectAndDecode(cv2.imread(pfad))
            check(data == url, f"(c) QR {name} dekodiert: {data}")
        except ImportError:
            hinweise.append(f"QR {name}: OpenCV fehlt, Inhalt nicht dekodiert")
    if not anhang.WEITERLEITUNG_BAND2:
        hinweise.append("Noch keine eigene Domain: der Band-2-Code fuehrt direkt zu Amazon, "
                        "Scans sind nicht zaehlbar")


def pruefe_ebook():
    if pruefe_gemeinsam("EBOOK", EBOOK) is None:
        return
    with zipfile.ZipFile(EBOOK) as z:
        rels = z.read("word/_rels/document.xml.rels").decode("utf-8")
    ziele = set(re.findall(r'Target="(https?://[^"]+)"[^>]*TargetMode="External"', rels))
    check(anhang.BAND2_URL in ziele, f"(c) Link weiter zu Band 2: {anhang.BAND2_URL}")
    check(anhang.REZENSION_URL in ziele, f"(c) Link Rezension: {anhang.REZENSION_URL}")


if __name__ == "__main__":
    pruefe_taschenbuch()
    pruefe_ebook()
    for h in hinweise:
        print(f"\n  ! {h}")
    print("\n" + ("ALLES BESTANDEN -- hochladbar." if not fehler
                  else f"{len(fehler)} FEHLER -- nicht hochladen."))
    sys.exit(1 if fehler else 0)
