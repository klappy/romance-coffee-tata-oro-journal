"""4x6 in sheet, N-up stacked, with corner crop marks — same pattern as last session's sheet.
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
gap = (PH - n * sh) / (n + 1)
x0 = (PW - sw) / 2

buf = io.BytesIO()
c = rc.Canvas(buf, pagesize=(PW, PH))
c.setLineWidth(0.3)
L = 6
for i in range(n):
    y = PH - gap * (i + 1) - sh * (i + 1)
    for (cx, cy, dx, dy) in [(x0, y, -1, -1), (x0 + sw, y, 1, -1), (x0, y + sh, -1, 1), (x0 + sw, y + sh, 1, 1)]:
        c.line(cx + dx * 2, cy, cx + dx * (2 + L), cy)
        c.line(cx, cy + dy * 2, cx, cy + dy * (2 + L))
c.save(); buf.seek(0)
marks = PdfReader(buf).pages[0]

w = PdfWriter()
p = w.add_blank_page(width=PW, height=PH)
for i in range(n):
    y = PH - gap * (i + 1) - sh * (i + 1)
    p.merge_transformed_page(st, Transformation().translate(x0, y))
p.merge_page(marks)
w.write(out)
print(out, f"{n}-up, gap {gap:.1f}pt")
