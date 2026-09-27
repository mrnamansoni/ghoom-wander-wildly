# Wakflow Product Catalogue (PDF)

The finished file is **`dist/Wakflow-Catalogue-2026.pdf`** — 22 A4 pages:
cover · platform intro · product list (2 pages) · one page per product (17) · back cover.

## Rebuild after a change

```bash
cd wakflow-catalogue
npm install            # once (Playwright + Chromium)
pip install jinja2 pyyaml segno pymupdf pillow fonttools brotli   # once
python3 svg/make_icons.py && python3 svg/make_heroes.py   # only if drawings changed
python3 fonts/make_static.py                              # only if font files changed
python3 build.py && node render.mjs
python3 review.py                  # renders every page as a PDF reader shows it
python3 tests/test_catalogue.py    # must end with 21/21 passed
```

`review.py` saves every page (rendered from the PDF itself, not the browser) into `../.impeccable/review/`.
Always check those images: browsers show effects that PDF readers turn into boxes.

## Where things live

| What | File |
|---|---|
| Product text (from Part A only) | `content/products.yaml` |
| Cover, intro, packages, back cover text | `content/site.yaml` |
| Page layouts | `templates/*.html.j2` |
| Colours, fonts, spacing | `styles/catalogue.css` |
| Product drawings (SVG) | `svg/make_heroes.py` → `svg/hero/` |
| Product icons | `svg/make_icons.py` → `svg/icons/` |
| Logo | `assets/logo-mark.png` (cropped from `assets/logo-original.webp`) |

## Design rules (light edition)

White pages with a lavender band, brand colours as solid colours only. No transparency, shadows, blur,
masks or gradient text — PDF readers draw those as boxes. The tests fail the build if any appear.
Product pages carry only: name, promise, drawing, 4 benefits, 8 key features. The demo button and
contact details are on the first and last pages only.

## Checks the build runs

Exactly 22 A4 pages · no page overflows · all three fonts loaded · no text below 8 pt (drawing labels 7 pt) ·
all 17 official names present · every proof number exists in the Part A source · key features come from Part A
or are marked as owner-provided · no internal software, server or client names · correct page numbers in the list ·
demo button only on first and last page · tappable links · no transparency in the PDF · no PDF-unsafe CSS ·
fonts embedded as real fonts · file under 4 MB.

Fonts (Oxanium, DM Sans, JetBrains Mono) are open source under the SIL Open Font License — see `fonts/OFL-*.txt`.
