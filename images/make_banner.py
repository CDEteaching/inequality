import sys
from PIL import Image, ImageDraw, ImageFont

photo_path, font_dir, out_path = sys.argv[1], sys.argv[2], sys.argv[3]
W, H = 2400, 900
PANEL = 1180          # navy quote panel width
FADE = 340            # soft transition into photo
NAVY = (0, 58, 112)   # #003A70
ORANGE = (229, 77, 35)  # #E54D23

src = Image.open(photo_path).convert("RGB")
# crop band: tower tops to blue tarp roofs
pw = W - PANEL + FADE
ratio = pw / H
cw = src.width
ch = int(cw / ratio)
y0 = 1010
photo = src.crop((0, y0, cw, y0 + ch)).resize((pw, H), Image.LANCZOS)

img = Image.new("RGB", (W, H), NAVY)
img.paste(photo, (PANEL - FADE, 0))

# horizontal fade from navy into photo
mask = Image.new("L", (FADE, H))
md = ImageDraw.Draw(mask)
for x in range(FADE):
    a = int(255 * (1 - x / FADE) ** 0.8)
    md.line([(x, 0), (x, H)], fill=a)
img.paste(Image.new("RGB", (FADE, H), NAVY), (PANEL - FADE, 0), mask)

d = ImageDraw.Draw(img)
f = lambda n, s: ImageFont.truetype(f"{font_dir}/roboto-{n}.ttf", s)
qmark, quote, attr, small, credit = f("700-normal", 220), f("300-italic", 86), f("700-normal", 44), f("400-normal", 34), f("400-normal", 24)

L = 130
d.text((L - 10, 70), "“", font=qmark, fill=ORANGE)
d.multiline_text((L, 300), "…the defining\nchallenge of our time.", font=quote, fill="white", spacing=22)
d.line([(L, 590), (L + 90, 590)], fill=ORANGE, width=6)
d.text((L, 625), "Barack Obama, 2013", font=attr, fill="white")
d.text((L, 685), "on rising inequality and declining mobility", font=small, fill=(205, 215, 230))

c = "Photo: Zoshua Colah / Unsplash  ·  Byculla, Mumbai"
tw = d.textlength(c, font=credit)
d.rectangle([(W - tw - 44, H - 54), (W, H)], fill=(0, 0, 0))
d.text((W - tw - 28, H - 44), c, font=credit, fill=(235, 235, 235))

img.save(out_path, quality=88, optimize=True, progressive=True)
print(img.size)
