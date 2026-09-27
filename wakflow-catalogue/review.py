"""Renders every page of the finished PDF with MuPDF (a real PDF reader, not the browser)
into ../.impeccable/review/page-NN.png, plus side-by-side pairs, for visual review.
Run: python3 review.py [dpi]"""
import sys
from pathlib import Path

import pymupdf
from PIL import Image

ROOT = Path(__file__).resolve().parent
OUT = ROOT.parent / ".impeccable" / "review"


def main(dpi=110):
    OUT.mkdir(parents=True, exist_ok=True)
    for old in OUT.glob("*.png"):
        old.unlink()
    doc = pymupdf.open(ROOT / "dist" / "Wakflow-Catalogue-2026.pdf")
    files = []
    for i, page in enumerate(doc):
        f = OUT / f"page-{i + 1:02d}.png"
        page.get_pixmap(dpi=dpi).save(f)
        files.append(f)
    for k in range(0, len(files), 2):
        ims = [Image.open(f) for f in files[k:k + 2]]
        pair = Image.new("RGB", (sum(i.width for i in ims) + 16, ims[0].height), (60, 60, 60))
        x = 0
        for im in ims:
            pair.paste(im, (x, 0))
            x += im.width + 16
        pair.save(OUT / f"pair-{k // 2 + 1:02d}.png")
    print(f"{len(files)} pages rendered from the PDF into {OUT}")


if __name__ == "__main__":
    main(int(sys.argv[1]) if len(sys.argv) > 1 else 110)
