---
name: Wakflow Catalogue
description: Light-edition A4 PDF catalogue for the Wakflow suite; white paper with a lavender wash, one product per page, drawn as clean vector datasheets.
colors:
  paper: "#FFFFFF"
  lavender-wash: "#F4F0FC"
  lavender-rule: "#EBE4F8"
  hairline: "#E2DAF2"
  ink: "#1C1836"
  body-ink: "#45415F"
  muted-ink: "#736E90"
  brand-purple: "#7B35C1"
  purple-tint: "#F1E9FB"
  demo-orange: "#FF8A00"
  button-ink: "#1C1300"
  flagship-amber: "#C26A00"
  flagship-amber-tint: "#FFF1DF"
  flag-pill-orange: "#E27A00"
  talk-teal: "#0784AD"
  talk-tint: "#E2F6FD"
  sell-blue: "#2A6CC2"
  sell-tint: "#E7F0FC"
  grow-green: "#0B8A5E"
  grow-tint: "#E3F7EF"
  run-slate: "#3D3A58"
  run-tint: "#ECEAF3"
  stroke-cyan: "#00C8FF"
  stroke-blue: "#4A90E2"
  stroke-green: "#10B981"
  stroke-red: "#F87171"
  drawing-line: "#E6E0F3"
  drawing-line-strong: "#CEC5E4"
  drawing-grey: "#6E6A8A"
typography:
  display:
    fontFamily: "Oxanium, DM Sans, sans-serif"
    fontSize: "44px"
    fontWeight: 800
    lineHeight: 1.07
    letterSpacing: "-0.015em"
  headline:
    fontFamily: "Oxanium, DM Sans, sans-serif"
    fontSize: "32px"
    fontWeight: 800
    lineHeight: 1.12
    letterSpacing: "-0.01em"
  product-title:
    fontFamily: "Oxanium, DM Sans, sans-serif"
    fontSize: "31px"
    fontWeight: 800
    lineHeight: 1.08
    letterSpacing: "-0.01em"
  numeral:
    fontFamily: "Oxanium, DM Sans, sans-serif"
    fontSize: "26px"
    fontWeight: 800
    lineHeight: 1.05
    fontFeature: "tnum"
  title:
    fontFamily: "DM Sans, sans-serif"
    fontSize: "17px"
    fontWeight: 700
    lineHeight: 1.3
  section:
    fontFamily: "Oxanium, DM Sans, sans-serif"
    fontSize: "15px"
    fontWeight: 700
    lineHeight: 1.2
  lead:
    fontFamily: "DM Sans, sans-serif"
    fontSize: "13.5px"
    fontWeight: 400
    lineHeight: 1.6
  body:
    fontFamily: "DM Sans, sans-serif"
    fontSize: "12px"
    fontWeight: 400
    lineHeight: 1.5
    fontFeature: "tnum"
  body-small:
    fontFamily: "DM Sans, sans-serif"
    fontSize: "11px"
    fontWeight: 400
    lineHeight: 1.4
  label:
    fontFamily: "DM Sans, sans-serif"
    fontSize: "11px"
    fontWeight: 600
    lineHeight: 1
  drawing-mono:
    fontFamily: "JetBrains Mono, monospace"
    fontSize: "9.72px"
    fontWeight: 500
    letterSpacing: "1.2px"
rounded:
  feature-dot: "2px"
  index-icon: "12px"
  product-icon: "16px"
  panel: "22px"
  pill: "999px"
spacing:
  page-x: "46px"
  page-top: "30px"
  page-bottom: "26px"
  head-gap: "26px"
  column-gap: "28px"
  gap-min: "14px"
  gap-max: "44px"
components:
  button-demo:
    backgroundColor: "{colors.demo-orange}"
    textColor: "{colors.button-ink}"
    rounded: "{rounded.pill}"
    padding: "12px 18px 12px 20px"
  button-demo-large:
    backgroundColor: "{colors.demo-orange}"
    textColor: "{colors.button-ink}"
    rounded: "{rounded.pill}"
    padding: "14px 22px 14px 24px"
  product-icon:
    backgroundColor: "{colors.paper}"
    rounded: "{rounded.product-icon}"
    size: "54px"
  index-icon:
    backgroundColor: "{colors.purple-tint}"
    textColor: "{colors.brand-purple}"
    rounded: "{rounded.index-icon}"
    size: "42px"
  new-pill:
    backgroundColor: "{colors.brand-purple}"
    textColor: "{colors.paper}"
    rounded: "{rounded.pill}"
    padding: "2px 6px 3px"
  flag-pill:
    backgroundColor: "{colors.flag-pill-orange}"
    textColor: "{colors.paper}"
    rounded: "{rounded.pill}"
    padding: "4px 8px"
  contact-panel:
    backgroundColor: "{colors.paper}"
    rounded: "{rounded.panel}"
    padding: "28px 30px"
---

# Design System: Wakflow Catalogue

## Overview

**Creative North Star: "The Lavender Datasheet"**

The Wakflow catalogue is a 22-page A4 PDF (cover, platform intro, two index pages, seventeen product pages, back page) that a business owner is sent on WhatsApp and reads on a phone or prints. The light edition replaced the earlier black-and-neon catalogue at the owner's direction (27 Sep 2026): white with a shade of purple, far less content, no boxes, the demo button only on the first and last pages, and the owner's own WF logo. The website keeps its black world; the catalogue does not inherit it.

Each page is white paper with a lavender wash across its top: the wash carries the page head, the title and the product drawing, and the white below carries the reading content in open, unboxed lists separated by hairlines. Brand colours from the website survive only as solid strokes and small accents on light ground, each paired with a darker text partner so type in a brand colour stays readable on white. Purple is the house voice; orange appears only as the demo button and the flagship marker.

The world is built for PDF readers first. Every colour is solid, every drawing is flat vector, and nothing relies on transparency, shadow, blur or gradient to read. Depth is carried by the lavender wash against white, by hairline rules, and by colour-tinted icon plates.

**Key Characteristics:**
- White paper, lavender wash band on top, open unboxed content below
- Purple as the single house accent; six family accents with pale tints
- Oxanium for display and numerals, DM Sans for reading, JetBrains Mono only inside drawings
- Flat vector datasheet drawings with pin-label callouts
- Solid colours only: PDF-safe by rule and by test
- Orange demo pill on the cover and back page only

## Colors

A cool white-and-lavender paper system with one purple voice, family accents deepened for legibility on white, and brand neons kept for drawing strokes only.

### Primary
- **Wakflow Purple** (brand-purple): the house accent. Accent words in page titles and cover headline, "Wakflow" in product names, statistics, step numerals, journey discs, the footer link, the "New" feature pill, and the AI-agents family.
- **Purple Tint** (purple-tint): pale plate behind purple icons on the index and the purple family.

### Secondary
- **Demo Orange** (demo-orange) with **Button Ink** (button-ink): the "Book a free demo" pill, and nothing else in page CSS.
- **Flagship Amber** (flagship-amber, tint flagship-amber-tint): the flagship family accent, the "Our flagship product" flag, and the flagship package name. **Flag Pill Orange** (flag-pill-orange) fills the index "Flagship" pill.

### Tertiary: family accents
Each product family sets its own accent and tint on its pages (heading label, icon stroke, benefit ticks, feature dots, index rules and page numbers): Talk to customers **Talk Teal** (talk-teal / talk-tint), AI agents Wakflow Purple, Capture and sell **Sell Blue** (sell-blue / sell-tint), Grow **Grow Green** (grow-green / grow-tint), Run and protect **Run Slate** (run-slate / run-tint).

### Drawing palette
Drawings (svg/kit.py) stroke in the website's brand colours: **Signal Cyan** (stroke-cyan), **Circuit Blue** (stroke-blue), Wakflow Purple, Demo Orange (with light #FFB347), **Tick Green** (stroke-green, light #34D399), **Problem Red** (stroke-red). Fills behind those strokes are their pale tints (cyan #E4F8FF, purple #F1E9FB, green #E3F8EF, orange #FFF2E0, red #FDECEC, blue #E7F0FC). Text drawn in a brand colour is always swapped for its darker partner: cyan to #0784AD, blue to #2A6CC2, orange to #B85E00, green to #0B8A5E, red to #C93A3A; purple stays #7B35C1. Neutrals: drawing-line, drawing-line-strong, drawing-grey, and surfaces #F7F5FC / #F4F1FB / #ECE7F7.

### Neutral
- **Paper** (paper): the page and the lower reading zone.
- **Lavender Wash** (lavender-wash): the top band on product and intro pages, the whole page on cover and back. This is "white with a shade of purple".
- **Lavender Rule** (lavender-rule): rules on the lavender cover and back pages, and the contact panel border.
- **Hairline** (hairline): header and footer rules, feature and index row dividers, QR frames.
- **Ink** (ink): headings, bold list heads, logo word.
- **Body Ink** (body-ink): body copy.
- **Muted Ink** (muted-ink): page numbers, footers, section asides, contact line.

### Named Rules
**The Solid Colour Rule.** Every colour in the PDF is a solid value. No rgba, opacity, color-mix, gradient text, box-shadow, text-shadow, blur, filter, mask or backdrop-filter in CSS; no opacity, radialGradient, filter or mask in SVG. PDF readers render transparency as boxes. When a softened colour is needed, pre-blend it over white with kit.py `mix()` and write the resulting hex. Enforced by `test_css_has_no_pdf_unsafe_effects`, `test_pdf_has_no_transparency` and `test_svgs_valid`.

**The Dark Partner Rule.** Brand neons are strokes and fills, never text on white. Any text drawn in a brand colour uses its darker partner from kit.py `TEXT`.

**The One Orange Rule.** Orange means "book a demo" or "flagship". The demo button appears only on the cover and the back page.

## Typography

**Display Font:** Oxanium (with DM Sans fallback, which also supplies the ₹ glyph Oxanium lacks)
**Body Font:** DM Sans
**Label/Mono Font:** JetBrains Mono, inside drawings only

**Character:** Oxanium's squared, engineered letterforms carry titles, numerals and buttons; DM Sans does all the reading at print-comfortable sizes with tabular figures.

### Hierarchy
- **Display** (800, 44px, 1.07): cover headline and the cover's product count.
- **Headline** (800, 32px, 1.12; 34px on the back page): intro, index and back page titles, with one accent phrase in Wakflow Purple.
- **Product title** (800, 31px, 1.08): "Wakflow" in purple, product name in ink.
- **Numeral** (800, 26px): intro statistics; step numerals on the back page at 34px; cover family counts at 22px.
- **Title** (DM Sans 700, 17px, 1.3): product headline under the title.
- **Section** (Oxanium 700, 15px): "What you get", "Key features" and similar; an aside in muted DM Sans 11.5px may follow on the same baseline. Index product names use the same step.
- **Lead** (13.5px, 1.6, max 660px): page intros; cover sub at 14px.
- **Body** (12px, 1.5): default; product sub at 12.5px; list descriptions 11.5px.
- **Body small / Label** (11px): feature descriptions, footers, head labels, captions. This is the floor.
- **Drawing mono** (500, 9px x SIZE 1.08, uppercase, 1.2 tracking): chip labels, window titles, "Example" tags inside drawings.

### Named Rules
**The Print Floor Rule.** Page body text never goes below 11px (8.25pt); drawing labels never below 7pt, after the kit's SIZE factor of 1.08. `test_min_font_size` checks the rendered PDF.

**The Mono Stays Drawn Rule.** JetBrains Mono uppercase is the voice of the illustrated product screens, not of the page. Page headings and labels are Oxanium or DM Sans in sentence case.

## Layout

Fixed A4 pages (210 x 297mm, zero page margin), inner padding 30px top, 46px sides, 26px bottom, laid out as a flex column so the footer sits at the bottom. Vertical breathing room between blocks comes from flexible gaps (min 14px, max 44px; 64px on the back page) so every page fills its sheet without overflow.

Product pages: a lavender showcase band bleeds edge to edge behind the head, title, headline, sub and full-width hero drawing; below, on white, a two-column benefits list (16px x 28px gap) and a two-column feature list, then the footer. Intro, index and back pages use three-column grids (journey, proof statistics, industries, steps) or single-column index rows (42px icon, text, page number). The cover and back page are lavender throughout.

Every page carries the same head (WF logo and wordmark, family or section label in accent, page number) over a hairline, and interior pages carry the same footer (catalogue name, wakflow.com in purple) over a hairline.

## Elevation & Depth

Completely flat. There are no shadows anywhere, by rule: box-shadow and blur are banned for PDF safety. Depth comes from three tonal moves only: the lavender wash band against white paper, pale family tints behind icons, and 1px hairline rules. Drawings are flat vector with 1 to 1.4px strokes; the kit's old `halo()` glow is a no-op in this edition.

### Named Rules
**The No-Box Rule.** Page content is not boxed. Lists are open rows separated by hairlines; benefits hang on a tick, features on a 7px square dot. The only framed shapes on the page are icon plates, QR codes, the contact panel on the back page, and the product screens drawn inside illustrations.

## Shapes

Soft geometric. Icon plates are rounded squares (16px at 54px on product pages, 12px at 42px on the index); pills are fully round (demo button, "New", "Flagship"); list markers are 7px squares with 2px corners; intro journey steps sit on 30px purple discs. The cover family strip uses a 3px accent top rule per family; the index uses a 2px accent rule under each family name. Drawings use 6 to 10px rounded rectangles, 22px-corner phones, and elbow leaders ending in a ringed dot for callouts.

## Components

### Buttons
- **Shape:** full pill (999px).
- **Demo button:** solid Demo Orange with Button Ink text, Oxanium 700 13px, trailing 14px arrow drawn as a stroked SVG path. Large variant on the back page at 15px.
- **Placement:** cover and back page only; never on product or index pages.
- **States:** none; this is print. Buttons are live links to WhatsApp.

### Chips
- **New pill:** white on Wakflow Purple, DM Sans 700 9.5px, after a feature name the owner added.
- **Flagship pill:** white on Flag Pill Orange with a star, on the index.
- **Drawing chips:** pale tint fill, pre-mixed stroke, mono uppercase label in the dark partner colour.

### Cards / Containers
- **Product icon plate:** 54px, white fill, 1.5px family-accent border, 16px corners, 28px line icon in accent.
- **Index icon plate:** 42px, family tint fill, no border, 12px corners, 22px icon in accent.
- **Contact panel (back page only):** white on lavender, 1.5px Lavender Rule border, 22px corners, 28px x 30px padding; holds phone number, web address, large demo button and two 112px QR codes.

### Navigation
- **Page head:** logo (22px mark, 15px Oxanium 800 uppercase wordmark with 0.06em tracking; 44px / 26px on the cover), right-aligned label in family accent (DM Sans 600 11px) and page number (Oxanium 700 12px, muted).
- **Index rows:** every product row links to its page; page number in family accent.
- **Footer:** muted catalogue name, purple wakflow.com link.

### Lists
- **Benefits:** two columns; family-accent circled tick, bold ink head (13px), body description (11.5px).
- **Features:** two columns between hairlines; 7px accent square dot, bold head (12px), description (11px).
- **Packages (back page):** two columns of name/best-for rows between Lavender Rule hairlines; flagship name in amber with a star.

### Datasheet Drawing (signature)
Each product page carries one full-width vector hero drawn with svg/kit.py: a product screen (phone or window) in white with lavender neutrals, tinted brand-colour highlights, and pin-label callouts (ringed dot, elbow leader, DM Sans 600 label with a grey sub-line) on either side. Placeholder bars stand in for UI copy that would otherwise be invented, and an "Example" tag marks every screen as illustrative. The cover carries the system map: seventeen product nodes on a ring around the WF mark.

## Do's and Don'ts

### Do:
- **Do** use solid colours only; pre-blend softened colours over white with `mix()` and write the hex.
- **Do** keep the lavender wash on the top band (or the whole page on cover and back) and white for the reading zone.
- **Do** swap brand-colour text for its darker partner from kit.py `TEXT`.
- **Do** keep page body text at 11px or larger and drawing labels at 7pt or larger.
- **Do** review pages rendered from the PDF by MuPDF (`python3 wakflow-catalogue/review.py`, output in .impeccable/review/), never browser screenshots.
- **Do** use the owner's WF logo beside the WAKFLOW wordmark on every page head.
- **Do** set one accent phrase per title in Wakflow Purple.

### Don't:
- **Don't** use rgba, opacity, color-mix, gradients on text, box-shadow, text-shadow, blur, filters or masks; PDF readers render them as boxes.
- **Don't** put content in boxes or cards; use open rows and hairlines.
- **Don't** place the demo button anywhere but the cover and the back page.
- **Don't** bring back the website's black background or neon glows into the catalogue.
- **Don't** set text in raw cyan, blue, orange, green or red on white.
- **Don't** add content back to product pages beyond title, headline, sub, drawing, benefits and key features.
