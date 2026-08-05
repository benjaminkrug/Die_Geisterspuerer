"""
Resize cover v2 PDF to exact KDP dimensions (5x8, ~200 pages, white paper).
"""
import fitz
import os

# KDP dimensions
cover_w_in = 10.700  # 0.125 + 5.0 + 0.450 + 5.0 + 0.125
cover_h_in = 8.250   # 0.125 + 8.0 + 0.125
target_w_px = int(cover_w_in * 300)  # 3210
target_h_px = int(cover_h_in * 300)  # 2475

cover_w_pt = cover_w_in * 72
cover_h_pt = cover_h_in * 72

path = r"C:\Users\krugb\OneDrive\Desktop\GMBH\Projekte\Buecher\Die_Schattenjaeger\Band1\Cover\Bilder\DIE Geisterspuerer_v2.pdf"
doc = fitz.open(path)
page = doc[0]

print(f"Original: {page.rect.width/72:.2f} x {page.rect.height/72:.2f} in")

zoom_x = target_w_px / page.rect.width
zoom_y = target_h_px / page.rect.height
mat = fitz.Matrix(zoom_x, zoom_y)

pix = page.get_pixmap(matrix=mat)
print(f"Gerendert: {pix.width} x {pix.height} px")

jpeg_bytes = pix.tobytes("jpeg", jpg_quality=95)

new_doc = fitz.open()
new_page = new_doc.new_page(width=cover_w_pt, height=cover_h_pt)
new_page.insert_image(fitz.Rect(0, 0, cover_w_pt, cover_h_pt), stream=jpeg_bytes)

output_path = os.path.join(r"C:\Users\krugb\OneDrive\Desktop\GMBH\Projekte\Buecher\Die_Schattenjaeger\Output\Band1\PDF", "DIE Geisterspuerer_v2_KDP.pdf")
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
print(f"\nDatei: DIE Geisterspuerer_v2_KDP.pdf")
