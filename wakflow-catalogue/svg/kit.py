"""Drawing kit shared by every catalogue SVG: brand colours, text, devices, bubbles, callouts.
All shapes are plain SVG strings so the output stays vector in the PDF."""
from html import escape

import os

THEME = os.environ.get("WAKFLOW_THEME", "light")  # "light" (default) or "dark" (the website's black + neon look)

BRAND = {
    "cyan": "#00C8FF", "blue": "#4A90E2", "purple": "#7B35C1",
    "orange": "#FF8A00", "orange2": "#FFB347", "green": "#10B981", "green2": "#34D399",
    "red": "#F87171", "white": "#FFFFFF",
}
if THEME == "dark":
    C = {
        **BRAND,
        # dark theme neutrals: the website's black, with cool grey lines
        "ink": "#EEF3FA", "grey": "#8892A4",
        "bg": "#000000", "bg1": "#0F1217", "bg2": "#12161C", "bg3": "#161B22", "bg4": "#1C222B",
        "line": "#262D38", "line2": "#3A4250",
        # deep tints of brand colours, used as fills behind brand-coloured strokes
        "cyanDeep": "#06303D", "purpleDeep": "#1E0F33", "greenDeep": "#062A20",
        "orangeDeep": "#2E1A05", "redDeep": "#2E1414", "blueDeep": "#0C1E33",
    }
    # Brand colours read well on black; only purple text needs a lighter partner.
    TEXT = {C["purple"]: "#B386EC"}
    BASE = "#0A0A0A"      # colour of the band the drawings sit on; mix() blends onto it
    LOGO = "logo-mark-dark.png"
else:
    C = {
        **BRAND,
        # light theme neutrals: white paper with a lavender cast
        "ink": "#1C1836", "grey": "#6E6A8A",
        "bg": "#FFFFFF", "bg1": "#FFFFFF", "bg2": "#F7F5FC", "bg3": "#F4F1FB", "bg4": "#ECE7F7",
        "line": "#E6E0F3", "line2": "#CEC5E4",
        # light tints of brand colours, used as fills behind brand-coloured strokes
        "cyanDeep": "#E4F8FF", "purpleDeep": "#F1E9FB", "greenDeep": "#E3F8EF",
        "orangeDeep": "#FFF2E0", "redDeep": "#FDECEC", "blueDeep": "#E7F0FC",
    }
    # Brand colours are too light for text on white; text drawn in a brand colour uses its darker partner.
    TEXT = {
        C["cyan"]: "#0784AD", C["blue"]: "#2A6CC2", C["purple"]: "#7B35C1", C["orange"]: "#B85E00",
        C["orange2"]: "#B85E00", C["green"]: "#0B8A5E", C["green2"]: "#0B8A5E", C["red"]: "#C93A3A",
    }
    BASE = "#FFFFFF"
    LOGO = "logo-mark.png"
LOGO_BG = "#0A0A0A" if THEME == "dark" else "#F4F0FC"  # the logo PNG is flattened onto this colour
SIZE = 1.08  # all drawing text is scaled up slightly for phone reading


def mix(color, opacity):
    """Solid colour equal to `color` at `opacity` over the page colour. PDFs render true transparency badly."""
    if opacity is None or color in (None, "none") or not color.startswith("#"):
        return color
    r, g, b = (int(color[i:i + 2], 16) for i in (1, 3, 5))
    br, bg_, bb = (int(BASE[i:i + 2], 16) for i in (1, 3, 5))
    m = lambda c, base: round(base + (c - base) * opacity)  # noqa: E731
    return f"#{m(r, br):02X}{m(g, bg_):02X}{m(b, bb):02X}"


DISPLAY, BODY, MONO = "Oxanium, DM Sans", "DM Sans", "JetBrains Mono"  # DM Sans supplies ₹, which Oxanium lacks


class Doc:
    """Collects defs and body for one SVG file. `uid` prefixes every id (many SVGs share one HTML page)."""

    def __init__(self, uid, w, h):
        self.uid, self.w, self.h = uid, w, h
        self.defs, self.body, self._n = [], [], 0

    def id(self, name):
        return f"{self.uid}-{name}"

    def add(self, *parts):
        self.body.extend(parts)
        return self

    def radial(self, name, color, opacity=0.35):
        gid = self.id(name)
        self.defs.append(
            f'<radialGradient id="{gid}"><stop offset="0" stop-color="{color}" stop-opacity="{opacity}"/>'
            f'<stop offset="1" stop-color="{color}" stop-opacity="0"/></radialGradient>')
        return f"url(#{gid})"

    def linear(self, name, stops, x2=1, y2=0):
        gid = self.id(name)
        s = "".join(f'<stop offset="{o}" stop-color="{c}" stop-opacity="{a}"/>' for o, c, a in stops)
        self.defs.append(f'<linearGradient id="{gid}" x1="0" y1="0" x2="{x2}" y2="{y2}">{s}</linearGradient>')
        return f"url(#{gid})"

    def halo(self, *args, **kwargs):
        """Soft glows were a dark-theme device and need PDF transparency; the light theme has none."""
        return self

    def render(self):
        return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {self.w} {self.h}" '
                f'role="img" fill="none">'
                f'<defs>{"".join(self.defs)}</defs>{"".join(self.body)}</svg>\n')


# ---------- primitives ----------

def t(x, y, s, size=11, fill=C["ink"], family=BODY, weight=400, anchor="start", ls=None, opacity=None):
    extra = f' letter-spacing="{ls}"' if ls is not None else ""
    fill = mix(TEXT.get(fill, fill), opacity)
    return (f'<text x="{x}" y="{y}" font-family="{family}" font-size="{size * SIZE:.2f}" font-weight="{weight}" '
            f'fill="{fill}" text-anchor="{anchor}"{extra}>{escape(s)}</text>')


def mono(x, y, s, size=9, fill=C["grey"], anchor="start", weight=600):
    """Small drawing label: DM Sans, sentence case, never below 8pt on the page."""
    return t(x, y, s, max(size, 9.8), fill, BODY, weight, anchor)


def rect(x, y, w, h, r=6, fill=C["bg1"], stroke=C["line"], sw=1, opacity=None, dash=None):
    fill, stroke, o = mix(fill, opacity), mix(stroke, opacity), ""
    d = f' stroke-dasharray="{dash}"' if dash else ""
    st = f'stroke="{stroke}" stroke-width="{sw}"' if stroke else ""
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{fill}" {st}{o}{d}/>'


def line(x1, y1, x2, y2, stroke=C["line2"], sw=1, dash=None, opacity=None, cap="round"):
    d = f' stroke-dasharray="{dash}"' if dash else ""
    stroke, o = mix(stroke, opacity), ""
    return f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{stroke}" stroke-width="{sw}" stroke-linecap="{cap}"{d}{o}/>'


def path(d, stroke=C["cyan"], sw=1.2, fill="none", opacity=None, dash=None, join="round"):
    stroke, fill, o = mix(stroke, opacity), mix(fill, opacity), ""
    ds = f' stroke-dasharray="{dash}"' if dash else ""
    return (f'<path d="{d}" stroke="{stroke}" stroke-width="{sw}" fill="{fill}" '
            f'stroke-linecap="round" stroke-linejoin="{join}"{o}{ds}/>')


def circle(cx, cy, r, fill=C["cyan"], stroke=None, sw=1, opacity=None):
    fill, stroke, o = mix(fill, opacity), mix(stroke, opacity), ""
    st = f' stroke="{stroke}" stroke-width="{sw}"' if stroke else ""
    return f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{fill}"{st}{o}/>'


def bars(x, y, widths, h=5, gap=8, fill=C["line2"], r=2.5):
    """Placeholder text lines (for UI copy we do not want to invent)."""
    return "".join(rect(x, y + i * gap, w, h, r, fill, None) for i, w in enumerate(widths))


def tick(x, y, s=10, color=C["green2"], sw=1.6):
    return path(f"M{x} {y + s * .5} l{s * .35} {s * .35} l{s * .65} -{s * .75}", color, sw)


def chip(x, y, label, color=C["cyan"], size=9, pad=7, h=17, fill_opacity=0.14, text_fill=None):
    w = len(label) * max(size, 9.8) * SIZE * 0.56 + pad * 2
    return (f'<rect x="{x}" y="{y}" width="{w:.1f}" height="{h}" rx="{h / 2}" fill="{mix(color, fill_opacity)}" '
            f'stroke="{mix(color, .55)}" stroke-width=".8"/>'
            + mono(x + pad, y + h / 2 + size * .36, label, size, text_fill or color)), w


def button(x, y, w, h, label, kind="orange", uid="b", size=10):
    # orange belongs to the catalogue's one real call to action, so buttons inside drawings are purple
    fill = {"orange": C["purple"], "green": C["green"], "ghost": C["bg3"]}[kind]
    stroke = {"orange": C["purple"], "green": C["green"], "ghost": C["line2"]}[kind]
    col = C["white"] if kind in ("orange", "green") else C["ink"]
    return (rect(x, y, w, h, h / 2, fill, stroke, .8)
            + t(x + w / 2, y + h / 2 + size * .36, label, size, col, DISPLAY, 700, "middle"))


# ---------- devices ----------

def phone(x, y, w=150, h=280, glow=None):
    s = rect(x, y, w, h, 22, C["bg1"], C["line2"], 1.2)
    s += rect(x + 5, y + 5, w - 10, h - 10, 18, C["bg"], None)
    s += rect(x + w / 2 - 22, y + 11, 44, 7, 3.5, C["bg4"], None)
    if glow:
        s = path(f"M{x + 22} {y} H{x + w - 22}", glow, 1.4, opacity=.9) + s
    return s


def window(x, y, w, h, title="", dots=True):
    s = rect(x, y, w, h, 10, C["bg1"], C["line2"], 1.2)
    s += line(x, y + 22, x + w, y + 22, C["line"], 1)
    if dots:
        for i, c in enumerate((C["red"], C["orange2"], C["green2"])):
            s += circle(x + 14 + i * 11, y + 11, 3, c, opacity=.8)
    if title:
        s += mono(x + w / 2, y + 14.8, title, 9, C["grey"], "middle")
    return s


def bubble(x, y, w, h, side="in", fill=None, stroke=None, r=10):
    """Chat bubble box; `side` in = customer (left, neutral), out = business (right, tinted)."""
    if side == "in":
        fill, stroke = fill or C["bg4"], stroke or C["line2"]
    else:
        fill, stroke = fill or C["cyanDeep"], stroke or C["cyan"]
    return rect(x, y, w, h, r, fill, stroke, .8)


def wave(x, y, w, h, n=28, color=C["cyan"], seed=3, sw=1.6):
    import math
    out = []
    step = w / n
    for i in range(n):
        a = abs(math.sin(i * 0.9 + seed) * math.cos(i * 0.37 + seed * .5))
        hh = max(2, a * h)
        out.append(line(x + i * step, y - hh / 2, x + i * step, y + hh / 2, color, sw))
    return "".join(out)


# ---------- callouts (datasheet pin labels) ----------

def callout(px, py, lx, ly, label, side="left", color=C["cyan"], sub=None):
    """Dot on the device at (px,py), elbow leader to (lx,ly), label beyond it."""
    elbow_x = lx + (14 if side == "left" else -14)
    s = circle(px, py, 3.2, C["bg"], color, 1.4)
    s += circle(px, py, 1.3, color)
    s += path(f"M{px} {py} L{elbow_x} {ly} L{lx} {ly}", color, .9, opacity=.7)
    anchor = "end" if side == "left" else "start"
    tx = lx - 5 if side == "left" else lx + 5
    s += t(tx, ly + 3.8, label, 11, C["ink"], BODY, 600, anchor)
    if sub:
        s += t(tx, ly + 17, sub, 9.5, C["grey"], BODY, 400, anchor)
    return s


def example_tag(x, y):
    return (rect(x, y, 72, 18, 9, C["bg"], C["line2"], .8)
            + mono(x + 36, y + 13, "Example", 9, C["grey"], "middle"))


def arrow(x1, y1, x2, y2, color=C["cyan"], sw=1.2, dash=None, head=5, opacity=None):
    import math
    ang = math.atan2(y2 - y1, x2 - x1)
    hx1 = x2 - head * math.cos(ang - .5)
    hy1 = y2 - head * math.sin(ang - .5)
    hx2 = x2 - head * math.cos(ang + .5)
    hy2 = y2 - head * math.sin(ang + .5)
    return (line(x1, y1, x2, y2, color, sw, dash, opacity)
            + path(f"M{hx1:.1f} {hy1:.1f} L{x2} {y2} L{hx2:.1f} {hy2:.1f}", color, sw, opacity=opacity))


def node(cx, cy, r, label, color=C["cyan"], sub=None, size=10.5):
    s = circle(cx, cy, r + 6, color, opacity=.08)
    s += circle(cx, cy, r, C["bg1"], color, 1.2)
    s += t(cx, cy + size * .36, label, size, C["ink"], DISPLAY, 700, "middle")
    if sub:
        s += mono(cx, cy + r + 15, sub, 9, C["grey"], "middle")
    return s
