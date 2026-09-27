"""Builds dist/catalogue.html from content/*.yaml, svg/ and templates/.
Run: python3 build.py && node render.mjs
Dark edition: python3 build.py --theme dark && node render.mjs --theme dark  (writes catalogue-dark.html)
"""
import re
import sys
from pathlib import Path

import yaml
from jinja2 import Environment, FileSystemLoader, StrictUndefined
from markupsafe import Markup

ROOT = Path(__file__).resolve().parent
DIST = ROOT / "dist"


def load_yaml(name):
    path = ROOT / "content" / name
    return yaml.safe_load(path.read_text()) if path.exists() else None


THEME = "dark" if "--theme" in sys.argv and sys.argv[sys.argv.index("--theme") + 1] == "dark" else "light"


def svg(name, cls=""):
    """Inline an SVG file from svg/ (without the XML prolog). The dark edition uses svg/dark/ where it exists."""
    dark = ROOT / "svg" / "dark" / f"{name}.svg"
    text = (dark if THEME == "dark" and dark.exists() else ROOT / "svg" / f"{name}.svg").read_text()
    text = re.sub(r"<\?xml.*?\?>\s*", "", text)
    if cls:
        text = text.replace("<svg", f'<svg class="{cls}"', 1)
    return Markup(text)


def asset(name):
    """Inline a file from assets/ (the logo lives here; replace assets/logo.svg with the real one)."""
    text = (ROOT / "assets" / name).read_text()
    return Markup(re.sub(r"<\?xml.*?\?>\s*", "", text))


def qr(data, color="#000000"):
    """QR code as inline SVG path."""
    import segno
    import io
    buf = io.BytesIO()
    code = segno.make(data, error="m")
    code.save(buf, kind="svg", dark=color, light="#FFFFFF", border=4,
              xmldecl=False, svgns=True, nl=False, scale=1)
    w, h = code.symbol_size(border=4)
    out = buf.getvalue().decode()
    out = re.sub(r'\swidth="\d+"\sheight="\d+"', f' viewBox="0 0 {w} {h}"', out, count=1)
    return Markup(out.replace("<svg", '<svg class="qr"', 1))


def fmt_code(n):
    return f"{int(n):02d}"


def build():
    env = Environment(loader=FileSystemLoader(ROOT / "templates"), undefined=StrictUndefined,
                      autoescape=True, trim_blocks=True, lstrip_blocks=True)
    env.globals.update(svg=svg, qr=qr, asset=asset, fmt_code=fmt_code)
    products = load_yaml("products.yaml") or {"products": []}
    site = load_yaml("site.yaml") or {}
    by_code = {p["code"]: p for p in products["products"]}
    families = {f["id"]: f for f in site.get("families", [])}
    html = env.get_template("catalogue.html.j2").render(
        products=products["products"], by_code=by_code, site=site, families=families, total=len(by_code),
        theme=THEME)
    DIST.mkdir(exist_ok=True)
    out = DIST / ("catalogue-dark.html" if THEME == "dark" else "catalogue.html")
    out.write_text(html)
    print(f"built {out} ({len(html) // 1024} KB)")


if __name__ == "__main__":
    build()
