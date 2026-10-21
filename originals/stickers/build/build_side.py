"""Side-of-bag sticker: date + lot only, for bags that already carry the barcode sticker.
Sticker 2 x 0.75 in; 4x6 sheet = 2 columns x 8 rows, edge-to-edge, short edge ticks per seam.
Usage: python3 build_side.py BEST_BY OUTDIR
"""
import sys
from reportlab.pdfgen import canvas as rc
from reportlab.lib.units import inch
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

pdfmetrics.registerFont(TTFont("LS", "/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf"))
pdfmetrics.registerFont(TTFont("LSB", "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf"))

best_by, outdir = sys.argv[1], sys.argv[2]
LOT, ROASTED = "260723-01", "07-23-2026"
SW, SH = 2.0 * inch, 0.75 * inch

def draw_sticker(c, x, y):
    c.setFont("LSB", 12.5)
    c.drawString(x + 8, y + SH - 21, f"BEST BY {best_by}")
    c.setFont("LS", 7)
    c.drawString(x + 8, y + 11, f"LOT {LOT} · ROASTED {ROASTED}")

# single sticker
c = rc.Canvas(f"{outdir}/sticker-side-bestby-{best_by}.pdf", pagesize=(SW, SH))
draw_sticker(c, 0, 0)
c.save()

# 4x6 sheet, 2 cols x 8 rows
PW, PH = 4 * inch, 6 * inch
cols, rows = 2, int(PH // SH)
c = rc.Canvas(f"{outdir}/sheet-4x6-side-bestby-{best_by}.pdf", pagesize=(PW, PH))
for r in range(rows):
    for k in range(cols):
        draw_sticker(c, k * SW, PH - (r + 1) * SH)
c.setLineWidth(0.25); c.setStrokeGray(0.6)
T = 6  # tick length, pt
c.line(SW, 0, SW, T); c.line(SW, PH - T, SW, PH)
for r in range(1, rows):
    y = PH - r * SH
    c.line(0, y, T, y); c.line(PW - T, y, PW, y)
c.save()
print(f"{cols}x{rows} = {cols*rows} per sheet")
