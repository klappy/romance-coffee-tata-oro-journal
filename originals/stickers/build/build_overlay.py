"""Build the date/lot stickers by overlaying onto the ORIGINAL sticker PDF,
so the barcode, fonts and layout are byte-for-byte the original.
Usage: python3 build_overlay.py ORIGINAL.pdf BEST_BY OUTDIR
"""
import sys, io
from pypdf import PdfReader, PdfWriter, Transformation
from reportlab.pdfgen import canvas as rc
from reportlab.lib.units import inch
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

pdfmetrics.registerFont(TTFont("LS", "/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf"))
pdfmetrics.registerFont(TTFont("LSB", "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf"))

orig_path, best_by, outdir = sys.argv[1], sys.argv[2], sys.argv[3]
LOT = "260723-01"
orig = PdfReader(orig_path).pages[0]
W, H0 = float(orig.mediabox.width), float(orig.mediabox.height)  # 271.44 x 81

def overlay(size, draw):
    buf = io.BytesIO()
    c = rc.Canvas(buf, pagesize=size)
    draw(c)
    c.save()
    buf.seek(0)
    return PdfReader(buf).pages[0]

# Variant 1 — same size; original text ends at y≈9pt from bottom, add one line below it
def d1(c):
    c.setFont("LSB", 5.6)
    c.drawString(118.2, 3.2, f"BEST BY {best_by} · LOT {LOT}")
w = PdfWriter()
p = w.add_blank_page(width=W, height=H0)
p.merge_page(orig)
p.merge_page(overlay((W, H0), d1))
w.write(f"{outdir}/sticker-D1-{best_by}.pdf")

# Variant 2 — 0.25 in taller; original sits at the top, bold date line below
H = H0 + 0.25 * inch
def d2(c):
    c.setFont("LSB", 14)
    c.drawString(17.7, 5.5, f"BEST BY {best_by}")
    c.setFont("LS", 5.6)
    c.drawRightString(W - 10, 6.5, f"LOT {LOT} · ROASTED 07-23-2026")
w = PdfWriter()
p = w.add_blank_page(width=W, height=H)
p.merge_transformed_page(orig, Transformation().translate(0, H - H0))
p.merge_page(overlay((W, H), d2))
w.write(f"{outdir}/sticker-D2-{best_by}.pdf")
print("ok")
