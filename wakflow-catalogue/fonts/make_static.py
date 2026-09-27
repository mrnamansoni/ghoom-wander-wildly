"""Turns the variable Google Fonts files into one static font per weight, so Chromium embeds them
in the PDF as real fonts (not Type3 outlines). Rewrites styles/fonts.css to point at fonts/static/.
Run once after changing fonts: python3 fonts/make_static.py"""
import re
from pathlib import Path

from fontTools.ttLib import TTFont
from fontTools.varLib.instancer import instantiateVariableFont

HERE = Path(__file__).resolve().parent
CSS = HERE.parent / "styles" / "fonts.css"
OUT = HERE / "static"


def main():
    OUT.mkdir(exist_ok=True)
    css = CSS.read_text()
    blocks = re.findall(r"/\* ([\w-]+) \*/\n(@font-face \{.*?\})", css, re.S)
    faces = []
    for subset, block in blocks:
        family = re.search(r"font-family: '([^']+)'", block).group(1)
        style = re.search(r"font-style: (\w+)", block).group(1)
        weight = int(re.search(r"font-weight: (\d+)", block).group(1))
        src = re.search(r"url\(\.\./fonts/(?:static/)?([^)]+)\)", block).group(1)
        name = f"{family.replace(' ', '')}-{weight}{'i' if style == 'italic' else ''}-{subset}.woff2"
        target = OUT / name
        if not target.exists():
            source = HERE / src if (HERE / src).exists() else OUT / src
            font = TTFont(source)
            if "fvar" in font:
                axes = {a.axisTag for a in font["fvar"].axes}
                limits = {}
                if "wght" in axes:
                    limits["wght"] = weight
                if "opsz" in axes:
                    limits["opsz"] = 14
                font = instantiateVariableFont(font, limits, updateFontNames=False)
            font.flavor = "woff2"
            font.save(target)
        faces.append(f"/* {subset} */\n" + re.sub(r"url\([^)]+\)", f"url(../fonts/static/{name})", block))
    CSS.write_text("\n".join(faces) + "\n")
    print(f"{len(faces)} static faces in {OUT}")


if __name__ == "__main__":
    main()
