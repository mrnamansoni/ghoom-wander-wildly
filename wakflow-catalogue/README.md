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
python3 build.py && node render.mjs --shots
python3 tests/test_catalogue.py    # must end with 16/16 passed
```

`--shots` also saves a PNG of every page into `../.impeccable/review/` for checking.

## Where things live

| What | File |
|---|---|
| Product text (from Part A only) | `content/products.yaml` |
| Cover, intro, packages, back cover text | `content/site.yaml` |
| Page layouts | `templates/*.html.j2` |
| Colours, fonts, spacing | `styles/catalogue.css` |
| Product drawings (SVG) | `svg/make_heroes.py` → `svg/hero/` |
| Product icons | `svg/make_icons.py` → `svg/icons/` |
| Logo | `assets/logo.svg` |

## Swapping in the real logo

Replace `assets/logo.svg` with your logo (SVG, wide format, white or brand colours on transparent) and rebuild.
If you only have a PNG, tell Claude — the templates switch from inline SVG to an image in two lines.

## Checks the build runs

Exactly 22 A4 pages · no page overflows · all three fonts loaded · no text below 7.5 pt (labels 6.5 pt) ·
all 17 official names present · every proof number exists in the Part A source · feature counts match source ·
no internal software, server or client names · correct page numbers in the list · contact on every product page ·
tappable WhatsApp, phone and website links (and list rows jump to their page) · fonts embedded as real fonts · file under 4 MB.

Fonts (Oxanium, DM Sans, JetBrains Mono) are open source under the SIL Open Font License — see `fonts/OFL-*.txt`.
