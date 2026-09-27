# Wakflow Catalogue PDF Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build a 22-page A4 PDF catalogue of the 17 Wakflow products in the Wakflow black + neon brand, with a custom SVG graphic on every product page.

**Architecture:** Hand-curated Part A content lives in one YAML file. Jinja2 templates + one CSS file turn it into a single HTML document with one fixed-size `<section class="page">` per A4 page. Headless Chromium (Playwright) prints that HTML to PDF. Hero graphics are hand-authored inline SVG files, one per product.

**Tech Stack:** Python 3 + Jinja2 + PyYAML + segno (QR) + PyMuPDF (page checks), Node 22 + Playwright 1.56 (Chromium at `/opt/pw-browsers`), Google Fonts Oxanium / DM Sans / JetBrains Mono (OFL, stored locally).

**Spec:** `docs/superpowers/specs/2026-09-27-wakflow-catalogue-pdf-design.md`

## Global Constraints

- Page size A4 portrait, 210 × 297 mm, exactly 22 pages, one product per page.
- Colours exactly: bg `#000` / `#0a0a0a` / `#111`; cyan `#00C8FF`; blue `#4A90E2`; purple `#7B35C1`; orange `#FF8A00`→`#FFB347`; green `#10B981` / `#34D399`; red `#F87171`; grey text `#8892A4`.
- Fonts: Oxanium 600–800 headings/numbers/buttons; DM Sans 400–600 body; JetBrains Mono uppercase labels with wide tracking.
- Contact exactly: `wakflow.com` and `+91 96253 30270`.
- Text only from Part A of the product files. Proof numbers copied exactly. Official product names exactly.
- Never print: n8n, Evolution, Chatwoot, Twenty, Hermes, Baileys, LiveKit, Vobiz, MinIO, NCA, edge-tts, crm2, Naveen, any IP, any internal domain.
- Minimum body text 7.5 pt.
- Logo placeholder: text wordmark; real logo replaces `assets/logo.svg` without template changes.

## Review Focus

1. A long product name or long feature line pushes content past the page bottom → the overflow check must fail the build, not silently clip. (Task 1 test `test_no_page_overflows`.)
2. Web fonts fail to load and Chromium silently falls back to a system font → build must fail. (Task 1 test `test_fonts_loaded`.)
3. A proof number is mistyped while shortening copy (e.g. 91,907 → 91,970) → every number in `proof` must exist verbatim in that product's Part A. (Task 2 test `test_proof_numbers_in_source`.)
4. An internal software or client name slips into copy or into an SVG label → banned-word scan over the final HTML including SVG text. (Task 4 test `test_no_banned_words`.)
5. A product is missing or duplicated in the 17 → content test checks the exact 17 official names once each, and index page lists all 17 with correct page numbers. (Task 2 `test_all_products_present`, Task 4 `test_index_page_numbers`.)

---

### Task 1: Pipeline, fonts, brand tokens and page frame

**Files:**
- Create: `wakflow-catalogue/build.py`, `wakflow-catalogue/render.mjs`, `wakflow-catalogue/styles/catalogue.css`, `wakflow-catalogue/templates/base.html.j2`, `wakflow-catalogue/fonts/*.woff2` (+ `OFL.txt`), `wakflow-catalogue/assets/logo.svg`, `wakflow-catalogue/tests/test_catalogue.py`, `wakflow-catalogue/Makefile`

**Interfaces:**
- Produces: `build.py` → `dist/catalogue.html`; `node render.mjs` → `dist/Wakflow-Catalogue-2026.pdf` and `dist/report.json` = `{pages: int, overflows: [ {page:int, over_px:int} ], fonts_ok: bool, min_font_pt: float}`; CSS custom properties `--cyan --blue --purple --orange --orange-2 --green --green-2 --red --grey --bg --bg-1 --bg-2`, classes `.page`, `.rail`, `.mono-label`, `.grad-text`, `.btn`.

- [ ] Step 1: Write `tests/test_catalogue.py::test_pdf_page_count` (PDF opened with PyMuPDF has 22 pages, each 595×842 pt ±1), `test_no_page_overflows` (`report.json` overflows == []), `test_fonts_loaded` (`fonts_ok` is true), `test_min_font_size` (`min_font_pt` ≥ 7.5 for body text; mono micro-labels and SVG labels ≥ 6.5).
- [ ] Step 2: Run `python3 tests/test_catalogue.py` → fails (no dist).
- [ ] Step 3: Download the three font families (woff2, latin + latin-ext) into `fonts/`; write tokens + `@font-face` + `@page {size: A4; margin: 0}` + `.page {width:210mm; height:297mm; overflow:hidden; position:relative}` in CSS; `render.mjs` loads the HTML, waits for `document.fonts.ready`, checks `document.fonts.check('800 20px Oxanium')` etc., measures each `.page .page-inner` scrollHeight vs clientHeight, writes `report.json`, then `page.pdf({preferCSSPageSize:true, printBackground:true})`.
- [ ] Step 4: Temporary 22 empty frames → tests pass.
- [ ] Step 5: Commit.

### Task 2: Content — `content/products.yaml` + `content/site.yaml`

**Files:**
- Create: `wakflow-catalogue/content/products.yaml`, `wakflow-catalogue/content/site.yaml`, `wakflow-catalogue/content/source/` (copy of the 18 Part A files, for tests)

**Interfaces:**
- Produces: each product = `{code: "01".."17", slug, file: "16-personal-ai-assistant.md", name, family, flagship: bool, list_desc, headline, sub, replaces?, pains: [{q, a}] x3, benefits: [{t, d}] 4–6, feature_total: int, feature_groups: [{name, items: [str] 2–3}], proof: {kind: "numbers"|"dayone", items: [{n, l}] 3–4 | [str]}, proof_note?, works_with: [code], cta}`. `site.yaml` = cover, intro (pains, steps, stats), families, back cover.

- [ ] Step 1: Tests `test_all_products_present` (17 unique official names equal the README list), `test_proof_numbers_in_source` (every digit group in `proof.items[].n` appears in the product's Part A text), `test_feature_totals` (feature_total equals the count of bold feature lines under `### Features` in source, and every `feature_groups[].name` is a `####` heading in source), `test_works_with_codes_valid`.
- [ ] Step 2: Run → fail.
- [ ] Step 3: Write the YAML from Part A (order and graphics per spec §4.3).
- [ ] Step 4: Run → pass. Commit.

### Task 3: Graphics — icons, cover system map, 17 hero SVGs

**Files:**
- Create: `wakflow-catalogue/svg/icons/<slug>.svg` (17), `wakflow-catalogue/svg/hero/<slug>.svg` (17), `wakflow-catalogue/svg/cover-map.svg`, `wakflow-catalogue/svg/journey.svg`

**Interfaces:**
- Produces: SVG files with `viewBox` set, no fixed width/height, brand colours only, text in Oxanium/DM Sans/JetBrains Mono, "EXAMPLE" tag on illustrated chats/screens. `build.py` inlines them with `svg(name)` helper.

- [ ] Step 1: Test `test_svgs_valid` (each file parses as XML, has viewBox, uses only brand colours + white/black/greys + rgba of brand colours).
- [ ] Step 2: Draw each graphic per spec §4.3; render a contact sheet `dist/svg-sheet.png` for review.
- [ ] Step 3: Tests pass. Commit.

### Task 4: Page templates — cover, intro, index ×2, product, back cover

**Files:**
- Create: `wakflow-catalogue/templates/{cover,intro,index,product,back}.html.j2`
- Modify: `wakflow-catalogue/styles/catalogue.css`, `wakflow-catalogue/build.py`

**Interfaces:**
- Consumes: Task 1 tokens/classes, Task 2 data, Task 3 `svg()` helper.
- Produces: final `dist/catalogue.html` with 22 `.page` sections in spec order; QR SVGs via `segno` for `https://wa.me/919625330270` and `https://wakflow.com`.

- [ ] Step 1: Tests `test_no_banned_words` (Global Constraints list, case-insensitive, over HTML incl. SVG), `test_index_page_numbers` (index rows link to page n = 4 + code), `test_contact_printed` (both contact strings on back cover and on every product page footer).
- [ ] Step 2: Build templates, run pipeline, all Task 1 + 4 tests pass.
- [ ] Step 3: Visual pass: rasterise all 22 pages (PyMuPDF, 110 dpi) into `.impeccable/review/`, inspect, fix in one batch, re-check once.
- [ ] Step 4: Commit.

### Task 5: Finish — detector, independent review, DESIGN.md, delivery

- [ ] Step 1: `impeccable detect --json wakflow-catalogue/dist/catalogue.html`; fix mechanical findings.
- [ ] Step 2: Spawn `impeccable-finish-reviewer` with spec, direction contract, page images; apply its material fixes once; verdict round.
- [ ] Step 3: Spawn `impeccable-documenter` → `DESIGN.md` + `.impeccable/design.json`.
- [ ] Step 4: Superpowers verification-before-completion: re-run all tests fresh, read output.
- [ ] Step 5: Commit PDF + source, push `claude/gallant-faraday-gi4hc9`, open draft PR, send PDF to owner.
