"""
Resize cover PDF to exact KDP dimensions with JPEG compression.
"""
import fitz
import os

# KDP dimensions for 5x8 trim, ~200 pages, white paper
cover_w_in = 10.700  # 0.125 + 5.0 + 0.450 + 5.0 + 0.125
cover_h_in = 8.250   # 0.125 + 8.0 + 0.125

# Points
cover_w_pt = cover_w_in * 72
cover_h_pt = cover_h_in * 72

# Open original
path = r"C:\Users\krugb\OneDrive\Desktop\GMBH\Projekte\Buecher\Die_Schattenjaeger\DIE Geisterspuerer.pdf"
doc = fitz.open(path)
page = doc[0]

# Render at 300 DPI
zoom = 300 / 72
mat = fitz.Matrix(zoom, zoom)
pix = page.get_pixmap(matrix=mat)
print(f"Gerendert: {pix.width} x {pix.height} px")

# Convert to JPEG bytes (quality 90 for good print quality)
jpeg_bytes = pix.tobytes("jpeg", jpg_quality=90)
print(f"JPEG Größe: {len(jpeg_bytes)/1024:.0f} KB")

# Create new PDF
new_doc = fitz.open()
new_page = new_doc.new_page(width=cover_w_pt, height=cover_h_pt)
dst_rect = fitz.Rect(0, 0, cover_w_pt, cover_h_pt)
new_page.insert_image(dst_rect, stream=jpeg_bytes)

output_path = path.replace(".pdf", "_KDP.pdf")
new_doc.save(output_path, deflate=True, garbage=4)
new_doc.close()
doc.close()

new_size = os.path.getsize(output_path)
print(f"\n=== Ergebnis ===")
print(f"Datei: DIE Geisterspuerer_KDP.pdf")
print(f"Größe: {new_size/1024/1024:.1f} MB (vorher: 6.5 MB)")
print(f"Maße: {cover_w_in:.3f} x {cover_h_in:.3f} in ({cover_w_in*2.54:.1f} x {cover_h_in*2.54:.1f} cm)")
print(f"Auflösung: 300 DPI")
print(f"\nHinweis: Original-Bilder sind nur 1024x1536 px.")
print(f"Für optimale Druckqualität bei 300 DPI bräuchten die")
print(f"Cover-Bilder mindestens 1575x2475 px pro Seite.")
