"""
Resize cover PDF to exact KDP dimensions, optimized file size.
"""
import fitz
import os

# KDP dimensions for 5x8 trim, ~200 pages, white paper
cover_w_in = 10.700
cover_h_in = 8.250
target_w_px = int(cover_w_in * 300)  # 3210
target_h_px = int(cover_h_in * 300)  # 2475

# Points
cover_w_pt = cover_w_in * 72
cover_h_pt = cover_h_in * 72

# Open original
path = r"C:\Users\krugb\OneDrive\Desktop\GMBH\Projekte\Buecher\Die_Schattenjaeger\DIE Geisterspuerer.pdf"
doc = fitz.open(path)
page = doc[0]

# Calculate zoom to get exactly target pixels
# Original is 2398 x 1856 pt
zoom_x = target_w_px / page.rect.width
zoom_y = target_h_px / page.rect.height
mat = fitz.Matrix(zoom_x, zoom_y)

pix = page.get_pixmap(matrix=mat)
print(f"Gerendert: {pix.width} x {pix.height} px (Ziel: {target_w_px} x {target_h_px})")

# Convert to JPEG (quality 95 for print)
jpeg_bytes = pix.tobytes("jpeg", jpg_quality=95)
print(f"JPEG: {len(jpeg_bytes)/1024:.0f} KB")

# Create new PDF with correct dimensions
new_doc = fitz.open()
new_page = new_doc.new_page(width=cover_w_pt, height=cover_h_pt)
new_page.insert_image(fitz.Rect(0, 0, cover_w_pt, cover_h_pt), stream=jpeg_bytes)

output_path = path.replace(".pdf", "_KDP.pdf")
new_doc.save(output_path, deflate=True, garbage=4)
new_doc.close()
doc.close()

orig_size = os.path.getsize(path)
new_size = os.path.getsize(output_path)

print(f"\n=== Ergebnis ===")
print(f"Original:  {orig_size/1024/1024:.1f} MB")
print(f"KDP-Cover: {new_size/1024/1024:.1f} MB ({cover_w_in:.1f} x {cover_h_in:.1f} in)")
print(f"Reduktion: {(1 - new_size/orig_size)*100:.0f}%")
print(f"Pixel:     {target_w_px} x {target_h_px} @ 300 DPI")
print(f"\nDatei: DIE Geisterspuerer_KDP.pdf")
