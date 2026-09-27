---
name: Wakflow Catalogue
description: A4 print catalogue for the Wakflow suite; each product is a spec sheet pinned to a live neon screen.
colors:
  void: "#000000"
  surface-1: "#0A0A0A"
  surface-2: "#111111"
  surface-3: "#161B22"
  surface-4: "#1C222B"
  signal-cyan: "#00C8FF"
  circuit-blue: "#4A90E2"
  ultraviolet: "#7B35C1"
  ai-violet: "#A56BE6"
  demo-orange: "#FF8A00"
  demo-amber: "#FFB347"
  proof-green: "#10B981"
  tick-green: "#34D399"
  problem-red: "#F87171"
  slate-grey: "#8892A4"
  ink: "#EEF3FA"
  ink-2: "#C9D3E0"
  hairline-cyan: "rgba(0, 200, 255, .12)"
  hairline-grey: "rgba(136, 146, 164, .22)"
  svg-line: "#262D38"
  svg-line-2: "#3A4250"
  cyan-deep: "#06303D"
  purple-deep: "#1E0F33"
  green-deep: "#062A20"
  orange-deep: "#2E1A05"
  red-deep: "#2E1414"
  blue-deep: "#0C1E33"
  button-ink: "#140A00"
typography:
  display:
    fontFamily: "Oxanium, sans-serif"
    fontSize: "46px"
    fontWeight: 800
    lineHeight: 1.04
    letterSpacing: "-0.015em"
  headline:
    fontFamily: "Oxanium, sans-serif"
    fontSize: "33px"
    fontWeight: 800
    lineHeight: 1.02
    letterSpacing: "-0.01em"
  title:
    fontFamily: "Oxanium, sans-serif"
    fontSize: "17px"
    fontWeight: 600
    lineHeight: 1.25
  numeral:
    fontFamily: "Oxanium, sans-serif"
    fontSize: "24px"
    fontWeight: 800
    lineHeight: 1.05
    letterSpacing: "-0.01em"
    fontFeature: "tnum"
  body:
    fontFamily: "DM Sans, sans-serif"
    fontSize: "10.5px"
    fontWeight: 400
    lineHeight: 1.45
    fontFeature: "tnum"
  body-strong:
    fontFamily: "DM Sans, sans-serif"
    fontSize: "11px"
    fontWeight: 600
    lineHeight: 1.3
  label:
    fontFamily: "JetBrains Mono, monospace"
    fontSize: "9px"
    fontWeight: 500
    lineHeight: 1
    letterSpacing: "0.16em"
rounded:
  tag: "4px"
  icon-sm: "11px"
  card: "14px"
  panel: "16px"
  panel-lg: "20px"
  pill: "999px"
spacing:
  page-top: "24px"
  page-bottom: "20px"
  page-x: "40px"
  grid-cell: "28px"
  gutter-sm: "8px"
  gutter: "16px"
  gutter-lg: "24px"
  flex-gap-max: "26px"
  flex-gap-lg-max: "64px"
components:
  button-demo:
    backgroundColor: "{colors.demo-orange}"
    textColor: "{colors.button-ink}"
    typography: "{typography.title}"
    rounded: "{rounded.pill}"
    padding: "9px 14px 9px 16px"
  button-demo-lg:
    backgroundColor: "{colors.demo-orange}"
    textColor: "{colors.button-ink}"
    rounded: "{rounded.pill}"
    padding: "13px 20px 13px 22px"
  chip-works-with:
    textColor: "{colors.ink-2}"
    rounded: "{rounded.pill}"
    padding: "4px 9px 4px 6px"
  flag-flagship:
    textColor: "{colors.demo-amber}"
    typography: "{typography.label}"
    rounded: "{rounded.pill}"
    padding: "4px 8px 3px 6px"
  tag-replaces:
    textColor: "{colors.problem-red}"
    typography: "{typography.label}"
    rounded: "{rounded.tag}"
    padding: "3px 6px 2px"
  icon-tile:
    backgroundColor: "{colors.surface-1}"
    rounded: "{rounded.card}"
    size: "52px"
  proof-panel:
    textColor: "{colors.slate-grey}"
    rounded: "{rounded.card}"
    padding: "10px 16px"
  legend-strip:
    backgroundColor: "{colors.surface-1}"
    rounded: "{rounded.card}"
    padding: "11px 12px 12px"
---

# Design System: Wakflow Catalogue

## Overview

**Creative North Star: "The Lit Datasheet"**

Every page is an engineering datasheet printed on black: a product drawn working as a thin-stroke neon device, its features pinned to it with elbow leaders like pin labels, then the spec block, the measured proof and the way in. The world is the owner's pinned Wakflow web brand carried into print: pure black ground, a faint cyan graph-paper grid, soft violet and cyan halos bleeding in from the page corners, a cyan→blue→purple gradient reserved for names, and one warm orange pill that always means "book a demo".

Density is high but ordered. A4 at 96dpi (794×1123 CSS px) holds a rail, title block, hero screen, problem/benefit split, spec grid, proof panel and footer CTA on every product page, separated by 1px hairlines rather than boxes. Colour is semantic: cyan is the system, red is the customer's pain, green is measured proof and done, orange is the action, and each of six product families carries its own accent through icon tile, chips, spec rules and rail label.

The type voice has three registers: Oxanium for names and numbers (squared, technical, heavy), DM Sans for everything a reader reads, and JetBrains Mono uppercase "// LABEL" rails for every section label, measurement and caption.

**Key Characteristics:**
- Pure black page with a 28px cyan grid at 4.5% opacity, masked to fade through the middle.
- Radial neon halos (violet top-right, cyan left) behind every page; orange joins on flagship and back cover.
- Gradient text (cyan→blue→purple) on product names and the key phrase of each headline.
- "// LABEL" mono uppercase rails for all section labels, colour-coded by meaning.
- Products drawn as vector SVG devices (phone, window, bubbles, nodes) with pin-label callouts.
- Family accent (`--accent`) threads one hue through each product page.
- One orange gradient pill CTA per page, bottom right.

## Colors

A black-ground neon palette where every hue carries a fixed meaning.

### Primary
- **Signal Cyan** (signal-cyan): the system colour. Default label rails, hairlines (at 12%), grid (at 4.5%), the first stop of the brand gradient, journey step rings, back-cover step numerals, the Talk-to-customers family accent.
- **Circuit Blue** (circuit-blue): gradient midpoint; the Capture-and-sell family accent.
- **Ultraviolet** (ultraviolet): gradient end and the main halo hue (22–30% alpha radial glows).

### Secondary
- **Demo Orange → Demo Amber** (demo-orange → demo-amber, 95deg): the action gradient on every "Book a free demo" pill, with dark Button Ink text. Amber alone marks the flagship (flag pill, flagship accent, footer WhatsApp line, "Built for Indian businesses" label).

### Tertiary
- **Tick Green / Proof Green** (tick-green, proof-green): ticks, "// Proof" labels, the proof panel's border (tick-green at 28%) and wash (proof-green at 10% fading to cyan 4%). Grow family accent.
- **Problem Red** (problem-red): "// The problem" labels, pain-quote bullet dots with a 15% ring, the "Replaces" tag.
- **AI Violet** (ai-violet): the AI-agents family accent (a lighter ultraviolet for legibility on black).

### Neutral
- **Void** (void) page ground; **Surface 1–4** (surface-1 … surface-4) tile fills, device bodies and chat bubbles inside SVGs.
- **Ink** (ink): headlines, names, numerals, strong body. **Ink 2** (ink-2): leads, pain quotes, chip text; Run-and-protect family accent.
- **Slate Grey** (slate-grey): default body text and mono meta.
- **Hairline Cyan / Hairline Grey**: section rules and stat dividers in HTML. **SVG Line / Line 2**: opaque stroke greys inside the drawing kit.
- **Deep tints** (cyan-deep, purple-deep, green-deep, orange-deep, red-deep, blue-deep): fills placed behind a stroke of the same brand hue in SVG (e.g. the business-side chat bubble is cyan-deep with a cyan stroke).

### Named Rules
**The Meaning-Not-Mood Rule.** Red is only pain, green only proof or done, orange only the call to action. A hue never switches role between pages.

**The One Accent Per Product Rule.** Each product page resolves `--accent` from its family (flagship amber, talk cyan, AI violet, sell blue, grow green, run ink-2) and uses it for the icon tile, spec-rule underlines, spec bullets, chips and the rail label, never more.

**The Deep-Tint Fill Rule.** In SVG, a brand-coloured stroke sits on its matching deep tint, never on a lighter tint of itself.

## Typography

**Display Font:** Oxanium (with sans-serif)
**Body Font:** DM Sans (with sans-serif)
**Label/Mono Font:** JetBrains Mono (with monospace)

**Character:** Oxanium's squared heavy forms make names and numbers read as instrument readouts; DM Sans keeps the reading copy plain and friendly for non-technical owners; JetBrains Mono supplies the datasheet margin voice. All fonts are self-hosted woff2 subsets under OFL. Numerals are tabular throughout.

### Hierarchy
- **Display** (800, 46px, 1.04, -0.015em): cover headline only; back cover uses 38px, intro 30px, index 34px/28px at the same weight.
- **Headline** (800, 33px, 1.02): product name, set in the brand gradient, under a 12px 600 Oxanium "WAKFLOW" brand line tracked at 0.28em that is the first word of the product's own name.
- **Title** (600–700, 11–17px, 1.2–1.3): product one-line headline (17px), spec group heads (10.5px, accent underline), step and package names (12–13px), CTA line (12px).
- **Numeral** (800, 22–40px, ~1.05): feature counts (30px), proof stats (23–24px), legend counts (22px), cover total (40px), phone number (34px).
- **Body** (400, 10.5px, 1.45): default; leads rise to 12–13px in Ink 2. Spec items and captions 10px. Max measure about 560–690px.
- **Label** (500, 9px, 0.12–0.18em, uppercase): "// LABEL" rails, running rail, footer, meta, chip codes, captions.

### Named Rules
**The Print Floor Rule.** Body text never below 10px (7.5pt); labels never below 9px. In SVG, the smallest label is 9 units, which renders at about 0.98 scale on the page.

**The Gradient-Is-A-Name Rule.** The cyan→blue→purple gradient text goes on product names and the key phrase of a headline ("One system", "answer, sell, book and follow up", "wakflow.com"), one span per heading. It is the owner's brand device, not decoration to spread.

**The Slash Voice Rule.** Every section label is JetBrains Mono uppercase prefixed "// ", coloured by meaning (cyan default, red problem, green proof, amber built-for). An `em` inside a label drops to grey for the qualifier.

## Layout

Fixed A4 portrait pages (210×297mm, 794×1123 CSS px), zero page margin, printed with exact colour. Each page is a flex column with 24px top, 20px bottom and 40px side padding. Inner pages open with a three-column rail (section label in accent / logo centred / "Product catalogue 2026" with the page number) over a cyan hairline, and close with a mono footer rail or the CTA block, both pushed down with `margin-top: auto`.

Vertical rhythm between sections comes from flexible spacers that grow to at most 26px (64px on the intro and back cover, capped at 30px on the intro), so each page fills its height without overflow. Content blocks use CSS grid: title block `auto 1fr auto`; problem/benefit split 232px + 1fr at 24px gap; spec grid in 3, 4 or 5 columns depending on group count; proof stats in 3 or 4 columns divided by grey hairlines; journey in 6 columns joined by a 2px gradient line.

The product hero figure bleeds 4px past the text column and the cover map 30px, so drawings feel larger than the text frame.

## Elevation & Depth

Depth is light, not shadow. Surfaces are flat black; separation comes from hairlines, faint tinted washes (8–12% of a hue fading to transparent) and radial glows. Glow is part of the world: page halos, icon-tile halos, SVG node halos and the demo pill's orange under-glow.

### Shadow Vocabulary
- **Demo glow** (`box-shadow: 0 6px 18px -6px rgba(255, 138, 0, .55)`): under every orange pill.
- **Accent halo** (`box-shadow: 0 0 28px -8px color-mix(in srgb, var(--accent) 60%, transparent)`): product icon tile.
- **Signal ring** (`box-shadow: 0 0 0 3px rgba(248, 113, 113, .15)`): the red pain dot.
- **Page halos** (radial gradients, 380–520px ellipses, 9–30% alpha): violet upper right, cyan left; flagship swaps in orange; cover centres violet and cyan behind the system map.

### Named Rules
**The Light-Not-Lift Rule.** Nothing casts a directional drop shadow. Elements glow from their own hue or sit on a tinted wash.

## Shapes

Soft technical geometry. Pills (999px) for every button, chip, flag and SVG chip; 14px rounded cards for icon tiles, proof panels, legend strip and flagship rows; 16px for the hero frame and intro proof; 20px for the back-cover contact panel; 11px for small index icon tiles; 4px only on the "Replaces" tag. Rules are 1px hairlines; bullets are small circles (pains) or 4×1.5px accent dashes (spec items). SVG devices use 22px phone corners and 10px window corners, 0.8–1.2 stroke weights.

## Components

### Buttons
- **Shape:** full pill (999px).
- **Primary (demo):** orange→amber gradient, Button Ink text, Oxanium 700 11px, trailing 13px stroke arrow, demo glow. Large variant 14px on the back cover. One per page, bottom right with the mono contact line beneath.
- **States:** print artifact; no hover or focus states exist.

### Chips
- **Works-with chip:** pill, 1px border at 38% of the target product's family accent over an 8% wash, 12px product icon, mono 9px code, DM Sans 10px name in Ink 2.
- **Flagship flag:** pill, amber mono 9px uppercase with a star, amber 50% border on orange 10% wash.
- **Replaces tag:** 4px-radius red mono tag followed by the replaced tools in grey.

### Cards / Containers
- **Proof panel:** 14px radius, green 28% border, green→cyan→transparent 100deg wash, green "// label", Oxanium numerals over grey captions.
- **Icon tile:** 52px square, 14px radius, accent 55% border, radial accent 22% glow on Surface 1.
- **Legend strip / back contact panel:** hairline-divided cells on translucent Surface 1; the contact panel carries a cyan→violet wash and a 30% cyan border.

### Navigation
- **Logo:** `wakflow-catalogue/assets/logo.svg` is a placeholder wordmark (gradient-stroked W tile plus Oxanium 800 WAKFLOW) until the owner uploads the real logo; swap the file, not the layouts (30px tall on the cover, 24px on the back, 15px in the rail).
- **Running rail:** mono 9px uppercase, accent left label, centred 15px logo, page number in Ink. Index rows map each product to its page with code, icon tile, name, description and a large Oxanium page number.

### Pin-Label Callout (signature)
A hollow 3.2r dot with a solid 1.3r core on the device, a 0.9 stroke elbow leader at 70% opacity, and an 11px DM Sans 600 label in Ink with an optional 9.5px grey sub-line. This is how features attach to the live screen.

### Neon Device Kit (signature)
Phones, windows, chat bubbles (customer side Surface 4, business side cyan-deep with cyan stroke), system nodes with an 8% halo ring, audio waves, mono chips and an "Example" tag on illustrative screens, all emitted as plain vector SVG so the PDF stays sharp.

## Do's and Don'ts

### Do:
- **Do** keep every page on the black ground with the masked 28px cyan grid and at least one radial halo.
- **Do** put gradient text on the product name and one key headline phrase, never across whole paragraphs.
- **Do** label every section with a "// " JetBrains Mono uppercase rail at 9px, coloured by meaning.
- **Do** hold body copy at 10px or larger and labels at 9px or larger; SVG labels at 9 units or larger.
- **Do** draw products as thin-stroke vector devices with pin-label callouts, and tag illustrative screens "Example".
- **Do** use only measured, dated proof numbers in the green proof panel.
- **Do** end each page with a single orange demo pill and the wakflow.com / phone contact line.

### Don't:
- **Don't** use orange for anything but the call to action and the flagship marker.
- **Don't** use red outside pain quotes, problem labels and the "Replaces" tag.
- **Don't** add directional drop shadows; depth is glow and tinted washes.
- **Don't** place a brand-coloured stroke on anything but its deep tint in SVG.
- **Don't** invent UI copy inside device screens; use placeholder bars.
