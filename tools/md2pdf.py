#!/usr/bin/env python3
"""Minimal markdown -> PDF renderer with CJK (Chinese) support, using only Pillow.

Used by the /predict pipeline (step 7) to export the Simplified-Chinese
prediction as a PDF. Deliberately dependency-light: no reportlab / pandoc /
weasyprint required — just Pillow + a Noto Sans CJK font.

Usage:  python3 tools/md2pdf.py <input.md> <output.pdf>
"""
import sys, re, subprocess
from PIL import Image, ImageDraw, ImageFont

if len(sys.argv) != 3:
    sys.exit("usage: md2pdf.py <input.md> <output.pdf>")
SRC, OUT = sys.argv[1], sys.argv[2]

# --- locate a Simplified-Chinese-capable Noto Sans CJK face ---------------
CANDIDATES = [
    "/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc",
    "/usr/share/fonts/opentype/noto/NotoSansCJK-SC-Regular.otf",
    "/usr/share/fonts/truetype/noto/NotoSansCJK-Regular.ttc",
    "/System/Library/Fonts/PingFang.ttc",
]
BOLD_CANDIDATES = [
    "/usr/share/fonts/opentype/noto/NotoSansCJK-Bold.ttc",
    "/usr/share/fonts/opentype/noto/NotoSansCJK-SC-Bold.otf",
    "/usr/share/fonts/truetype/noto/NotoSansCJK-Bold.ttc",
]
def find_font(cands, fallback_query):
    for p in cands:
        try:
            open(p, "rb").close(); return p
        except OSError:
            continue
    try:  # ask fontconfig as a last resort
        out = subprocess.check_output(["fc-match", "-f", "%{file}", fallback_query], text=True)
        return out.strip() or None
    except Exception:
        return None
REG = find_font(CANDIDATES, "Noto Sans CJK SC")
BOLD = find_font(BOLD_CANDIDATES, "Noto Sans CJK SC:bold") or REG
if not REG:
    sys.exit("No CJK font found; install fonts-noto-cjk.")

def sc_index(path):
    """Find the Simplified-Chinese sub-face index in a .ttc (0 for plain .otf)."""
    if not path.endswith(".ttc"):
        return 0
    for i in range(16):
        try:
            if "SC" in ImageFont.truetype(path, 24, index=i).getname()[0] and "Mono" not in ImageFont.truetype(path, 24, index=i).getname()[0]:
                return i
        except Exception:
            break
    return 0
REG_IDX, BOLD_IDX = sc_index(REG), sc_index(BOLD)

# --- page geometry (A4 @ ~150 DPI) ----------------------------------------
W, H, MARGIN = 1240, 1754, 96
BG, FG, MUTED, ACCENT = (255, 255, 255), (23, 23, 23), (110, 110, 110), (176, 32, 40)
SIZES = {"h1": 40, "h2": 28, "body": 23, "small": 19}
_fc = {}
def font(kind, bold=False):
    key = (kind, bold)
    if key not in _fc:
        path, idx = (BOLD, BOLD_IDX) if bold else (REG, REG_IDX)
        _fc[key] = ImageFont.truetype(path, SIZES[kind], index=idx)
    return _fc[key]

# --- parse markdown into blocks -------------------------------------------
blocks = []
for raw in open(SRC, encoding="utf-8").read().splitlines():
    line = raw.rstrip()
    if not line.strip():                     blocks.append(("gap", ""))
    elif re.match(r"^#\s", line):            blocks.append(("h1", line[2:].strip()))
    elif re.match(r"^##\s", line):           blocks.append(("h2", line[3:].strip()))
    elif line.strip() == "---":              blocks.append(("hr", ""))
    elif re.match(r"^[-*]\s", line.strip()): blocks.append(("li", line.strip()[2:].strip()))
    else:                                    blocks.append(("p", line.strip()))

def segments(text):
    out = []
    for i, part in enumerate(re.split(r"\*\*", text)):
        part = part.replace("*", "")
        if part: out.append((part, i % 2 == 1))
    return out

def atomize(seg_text, bold):
    atoms, buf = [], ""
    def flush():
        nonlocal buf
        if buf: atoms.append((buf, bold)); buf = ""
    for ch in seg_text:
        if ch == " ":                 flush(); atoms.append((" ", bold))
        elif ord(ch) > 0x2E80:        flush(); atoms.append((ch, bold))
        else:                         buf += ch
    flush()
    return atoms

pages = []
img = Image.new("RGB", (W, H), BG); dr = ImageDraw.Draw(img); y = MARGIN
def newpage():
    global img, dr, y
    pages.append(img); img = Image.new("RGB", (W, H), BG); dr = ImageDraw.Draw(img); y = MARGIN
def ensure(h):
    global y
    if y + h > H - MARGIN: newpage()

def draw_wrapped(atoms, fkind, color, lh, x0=MARGIN, hang=0):
    global y
    line, cur, indent = [], 0, x0
    def flush(seg):
        global y
        ensure(lh); x = indent
        while seg and seg[0][0] == " ": seg.pop(0)
        for t, b, w in seg:
            dr.text((x, y), t, font=font(fkind, b), fill=color); x += w
        y += lh
    for t, b in atoms:
        w = dr.textlength(t, font=font(fkind, b))
        if indent + cur + w > W - MARGIN and line:
            flush(line[:]); line, cur, indent = [], 0, x0 + hang
        line.append((t, b, w)); cur += w
    if line: flush(line[:])

for typ, text in blocks:
    if typ == "gap":
        y += 10
    elif typ == "hr":
        ensure(30); y += 8; dr.line([(MARGIN, y), (W - MARGIN, y)], fill=(210, 210, 210), width=2); y += 18
    elif typ == "h1":
        y += 6; ensure(SIZES["h1"] + 20)
        draw_wrapped([a for s, b in segments(text) for a in atomize(s, True)], "h1", FG, SIZES["h1"] + 12)
        y += 6; dr.line([(MARGIN, y), (W - MARGIN, y)], fill=ACCENT, width=3); y += 20
    elif typ == "h2":
        y += 16; ensure(SIZES["h2"] + 16)
        draw_wrapped([a for s, b in segments(text) for a in atomize(s, True)], "h2", ACCENT, SIZES["h2"] + 12); y += 8
    elif typ == "li":
        ensure(SIZES["body"] + 10)
        dr.ellipse([MARGIN + 6, y + 12, MARGIN + 14, y + 20], fill=FG)
        draw_wrapped([a for s, b in segments(text) for a in atomize(s, b)], "body", FG, SIZES["body"] + 12, x0=MARGIN + 34); y += 6
    elif typ == "p":
        small = text.replace("*", "").startswith(("门槛备注", "Gate notes"))
        kind, color = ("small", MUTED) if small else ("body", FG)
        draw_wrapped([a for s, b in segments(text) for a in atomize(s, b)], kind, color, SIZES[kind] + 12); y += 4

pages.append(img)
pages[0].save(OUT, save_all=True, append_images=pages[1:], resolution=150.0)
print(f"wrote {OUT} ({len(pages)} page(s))")
