import os
import html

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "..", "info-card.svg")

# Same style colors as portrait
BG = "#0d1117"
BG2 = "#111722"
FRAME = "#30363d"
TITLE_TEXT = "#7d8590"
TEXT_COLOR = "#c9d1d9"
KEY_COLOR = "#39d353"
ACCENT_COLOR = "#22d3ee"

PAD = 20
TITLEBAR_H = 30
STATUS_H = 30
CANVAS_W = 1000
CANVAS_H = 875  # Matches the aspect/height of the portrait roughly

# Animation parameters
ROW_DUR = 0.2
STAGGER = 0.2

data = [
    ("Name", "Amit Singh Bisht"),
    ("Role", "B.Tech EE Student"),
    ("Education", "NIT Raipur"),
    ("Stack", "C++ | Python | JS | React | Node"),
    ("Projects", "EventSnap | IRON SIDE"),
    ("CP", "500+ problems"),
    ("Focus", "Systems | AI | Security"),
    ("Learning", "Agentic AI | ML")
]

lines = []
lines.append("amit@github:~$ neofetch")
lines.append("-----------------------")
lines.append("       ")
for k, v in data:
    # pad key to 9 chars for neat alignment
    padded_k = f"{k}:".ljust(11)
    lines.append(f"<key>{padded_k}</key> <val>{v}</val>")
lines.append("       ")
lines.append("amit@github:~$ _")

parts = []
parts.append(
    f'<svg xmlns="http://www.w3.org/2000/svg" width="{CANVAS_W}" height="{CANVAS_H}" '
    f'viewBox="0 0 {CANVAS_W} {CANVAS_H}" font-family="ui-monospace, SFMono-Regular, '
    f'Menlo, Consolas, monospace">'
)
parts.append('<defs>'
             f'<linearGradient id="bg" x1="0" y1="0" x2="0" y2="1">'
             f'<stop offset="0" stop-color="{BG2}"/><stop offset="1" stop-color="{BG}"/>'
             f'</linearGradient></defs>')

parts.append(f'<rect width="{CANVAS_W}" height="{CANVAS_H}" rx="12" fill="url(#bg)"/>')
parts.append(f'<rect x="0.5" y="0.5" width="{CANVAS_W-1}" height="{CANVAS_H-1}" rx="12" '
             f'fill="none" stroke="{FRAME}" stroke-width="1"/>')

parts.append(f'<line x1="0" y1="{TITLEBAR_H}" x2="{CANVAS_W}" y2="{TITLEBAR_H}" stroke="{FRAME}"/>')
for i, dotcol in enumerate(["#ff5f56", "#ffbd2e", "#27c93f"]):
    parts.append(f'<circle cx="{PAD + i*16}" cy="{TITLEBAR_H/2}" r="5" fill="{dotcol}"/>')
parts.append(f'<text x="{CANVAS_W/2}" y="{TITLEBAR_H/2 + 4}" fill="{TITLE_TEXT}" font-size="12" '
             f'text-anchor="middle">amit@github: ~$ ./info.sh</text>')

art_top = TITLEBAR_H + PAD * 2
font_size = 24
line_height = 36

for ry, raw_line in enumerate(lines):
    y = art_top + ry * line_height
    delay = ry * STAGGER
    
    if "<key>" in raw_line:
        key = raw_line.split("<key>")[1].split("</key>")[0]
        val = raw_line.split("<val>")[1].split("</val>")[0]
        text_content = f'<tspan fill="{KEY_COLOR}">{html.escape(key)}</tspan> <tspan fill="{TEXT_COLOR}">{html.escape(val)}</tspan>'
    else:
        text_content = html.escape(raw_line)

    text = f'<text xml:space="preserve" x="{PAD}" y="{y:.1f}" fill="{TEXT_COLOR}" font-size="{font_size}">{text_content}</text>'

    # Animation wipe
    parts.append(
        f'<clipPath id="r{ry}"><rect x="{PAD}" y="{y - font_size}" height="{line_height}" width="0">'
        f'<animate attributeName="width" from="0" to="{CANVAS_W}" begin="{delay:.3f}s" '
        f'dur="{ROW_DUR:.2f}s" fill="freeze"/></rect></clipPath>'
    )
    parts.append(f'<g clip-path="url(#r{ry})">{text}</g>')

parts.append("</svg>")
svg = "".join(parts)
with open(OUT, "w") as f:
    f.write(svg)
print("wrote", OUT, len(svg), "bytes")
