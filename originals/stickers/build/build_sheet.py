"""4x6 in sheet, N-up stacked edge-to-edge, short edge ticks marking each seam.
Usage: python3 build_sheet.py STICKER.pdf OUT.pdf
"""
import sys, io
from pypdf import PdfReader, PdfWriter, Transformation
from reportlab.pdfgen import canvas as rc

src, out = sys.argv[1], sys.argv[2]
st = PdfReader(src).pages[0]
sw, sh = float(st.mediabox.width), float(st.mediabox.height)
PW, PH = 288.0, 432.0  # 4 x 6 in
n = int(PH // sh)
gap = (PH - n * sh) / (n + 1)  # leftover height spread into equal gaps, top and bottom included
def ybot(i): return PH - gap * (i + 1) - sh * (i + 1)
x0 = (PW - sw) / 2

buf = io.BytesIO()
c = rc.Canvas(buf, pagesize=(PW, PH))
c.setLineWidth(0.25)
c.setStrokeGray(0.6)
T = 6  # tick length, pt
for i in range(1, n):  # tick at the middle of each gap, both page edges
    y = ybot(i - 1) - gap / 2
    c.line(0, y, T, y)
    c.line(PW - T, y, PW, y)
c.save(); buf.seek(0)
guides = PdfReader(buf).pages[0]

w = PdfWriter()
p = w.add_blank_page(width=PW, height=PH)
for i in range(n):
    p.merge_transformed_page(st, Transformation().translate(x0, ybot(i)))
p.merge_page(guides)
w.write(out)
print(out, f"{n}-up, gap {gap:.1f}pt")
