"""
Calculate KDP cover dimensions and resize the cover PDF.
"""
import fitz  # PyMuPDF

# === KDP Cover Calculator ===
trim_w = 5.0   # inches
trim_h = 8.0   # inches
page_count = 200
bleed = 0.125  # inches on each outside edge

# Spine width: white paper = 0.002252 in/page, cream = 0.0025 in/page
spine_white = page_count * 0.002252
spine_cream = page_count * 0.0025

print("=== KDP Cover-Maße für 5x8 Zoll, 200 Seiten ===")
print()
print(f"Buchrücken (weißes Papier): {spine_white:.3f} in = {spine_white*25.4:.1f} mm")
print(f"Buchrücken (creme Papier):  {spine_cream:.3f} in = {spine_cream*25.4:.1f} mm")
print()

# Use white paper as default
spine = spine_white

cover_w = bleed + trim_w + spine + trim_w + bleed
cover_h = bleed + trim_h + bleed

print(f"Cover-Breite: {bleed} + {trim_w} + {spine:.3f} + {trim_w} + {bleed} = {cover_w:.3f} in = {cover_w*2.54:.1f} cm")
print(f"Cover-Höhe:   {bleed} + {trim_h} + {bleed} = {cover_h:.3f} in = {cover_h*2.54:.1f} cm")
print()

# At 300 DPI
px_w = int(cover_w * 300)
px_h = int(cover_h * 300)
print(f"Bei 300 DPI: {px_w} x {px_h} Pixel")
print()

# === Current PDF analysis ===
path = r"C:\Users\krugb\OneDrive\Desktop\GMBH\Projekte\Buecher\Die_Schattenjaeger\DIE Geisterspuerer.pdf"
doc = fitz.open(path)
page = doc[0]

current_w_in = page.rect.width / 72
current_h_in = page.rect.height / 72

print(f"=== Aktuelle PDF ===")
print(f"Seitenmaße: {current_w_in:.2f} x {current_h_in:.2f} in = {current_w_in*2.54:.1f} x {current_h_in*2.54:.1f} cm")
print(f"Skalierungsfaktor: {cover_w/current_w_in:.3f}x Breite, {cover_h/current_h_in:.3f}x Höhe")
print()

# === Resize PDF ===
print("=== Resize PDF ===")

# Target dimensions in points (72 pt = 1 in)
target_w_pt = cover_w * 72
target_h_pt = cover_h * 72

# Create new PDF with correct dimensions
new_doc = fitz.open()
new_page = new_doc.new_page(width=target_w_pt, height=target_h_pt)

# Place the old page content scaled to fit
src_rect = page.rect
dst_rect = fitz.Rect(0, 0, target_w_pt, target_h_pt)

# Insert the page as an image (renders and re-inserts)
# First render at high resolution
zoom = 300 / 72  # render at 300 DPI
mat = fitz.Matrix(zoom, zoom)
pix = page.get_pixmap(matrix=mat)
print(f"Gerendert bei 300 DPI: {pix.width} x {pix.height} px")

# Insert into new page
new_page.insert_image(dst_rect, pixmap=pix)

output_path = path.replace(".pdf", "_KDP.pdf")
new_doc.save(output_path, deflate=True, garbage=4)
new_doc.close()
doc.close()

import os
new_size = os.path.getsize(output_path) / (1024 * 1024)
print(f"Neue Datei: {output_path}")
print(f"Neue Größe: {new_size:.1f} MB")

# Verify
doc2 = fitz.open(output_path)
p = doc2[0]
print(f"Neue Maße: {p.rect.width/72:.2f} x {p.rect.height/72:.2f} in = {p.rect.width/72*2.54:.1f} x {p.rect.height/72*2.54:.1f} cm")
doc2.close()
