"""4x6 in sheet, N-up stacked edge-to-edge, one hairline cut guide between stickers.
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
top = PH - (PH - n * sh) / 2  # stack centered vertically, no gaps
x0 = (PW - sw) / 2

buf = io.BytesIO()
c = rc.Canvas(buf, pagesize=(PW, PH))
c.setLineWidth(0.25)
c.setStrokeGray(0.6)
for i in range(1, n):  # one line at each seam only
    y = top - sh * i
    c.line(0, y, PW, y)
c.save(); buf.seek(0)
guides = PdfReader(buf).pages[0]

w = PdfWriter()
p = w.add_blank_page(width=PW, height=PH)
for i in range(n):
    p.merge_transformed_page(st, Transformation().translate(x0, top - sh * (i + 1)))
p.merge_page(guides)
w.write(out)
print(out, f"{n}-up, {n-1} cut lines")
