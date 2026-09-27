# Wakflow Product Catalogue PDF — Design Spec

**Date:** 2026-09-27 · **Owner:** Naman (Wakflow) · **Status:** waiting for owner review

## 1. Goal

A premium, 22-page A4 PDF catalogue of all 17 Wakflow products, in the Wakflow website brand (black + neon), with a custom SVG graphic on every product page. It is sent to Indian SME owners on WhatsApp and email, read mostly on phones, sometimes printed. Success = a non-technical owner can (a) see the whole suite in two pages, (b) understand any one product from its single page, and (c) knows how to book a demo.

## 2. What the owner said (fixed)

- A4 portrait. Intro page → product list with a one-to-two-line description (2 pages) → **one page per product** → contact on the back.
- Content comes from **Part A** of each product file only.
- Brand kept exactly: black #000/#0a0a0a/#111; cyan #00C8FF (main); blue #4A90E2; purple #7B35C1; orange #FF8A00→#FFB347 (actions); green #10B981/#34D399 (ticks); red #F87171 (problems); grey #8892A4 (body). Cyan→blue→purple gradient on headlines + orange gradient buttons.
- Fonts: Oxanium 600–800 (headings, numbers, buttons), DM Sans 400–600 (body), JetBrains Mono (small uppercase labels, wide tracking, `// 01 LABEL` style).
- Contact: **wakflow.com** and **+91 96253 30270**.
- Logo: owner will upload. Until then a text wordmark "WAKFLOW" in Oxanium stands in; swapping in the real logo is one file (`assets/logo.svg`).
- Layout: "mix of all three and choose best" (spec sheet + premium product box + live phone demo).

## 3. Assumptions (please correct if wrong)

1. There is a **cover page** before the intro page (so the intro page can explain the platform instead of only showing a title).
2. Products are ordered by **family** (the customer journey), not by file number, so the list tells a story. The flagship comes first. Page codes run 01–17 in this new order.
3. No prices are printed (Part A has none).
4. Products with no measured proof (Lead Finder, Cold Email, Carousel Studio, Video Factory) show "What you get on day one" instead of numbers.
5. Example chats/screens inside graphics are illustrations and carry a small "Example" tag. Every number printed as proof is copied exactly from Part A (as of 27 Sep 2026).
6. Underlying software names (n8n, Evolution, Chatwoot, Twenty, Hermes, LiveKit, etc.) never appear. Clients stay anonymous.

## 4. The fused design: "Spec sheet with a live screen"

One visual system, three borrowed strengths:

| From | What we keep |
|---|---|
| Tech spec sheet | Page rails with mono labels (`// 06 · AI AGENTS`), fine grid, feature "spec blocks", big measured numbers, "Connects to" row. Gives order and room for many features. |
| Live phone demo | Every product's hero graphic is its **screen at work** (chat, inbox, board, call, email, site) drawn in SVG, with thin leader lines pointing to 4–6 real features — the "pin labels" of the spec sheet. Makes each product instantly understood. |
| Premium product box | Soft neon halo behind each screen, a glowing product icon, and orange "Book a free demo" pill. Gives the gadget-on-a-shelf feel. |

### 4.1 Product page anatomy (every product, one A4 page)

```
┌ // 06 · AI AGENTS ─────────────────── WAKFLOW · 06/17 ┐  top rail (mono)
│ [icon] Wakflow AI WhatsApp Agent                       │  Oxanium 800, gradient
│ Your best salesperson, on WhatsApp, every hour of day  │  hero headline
│ sub-headline (2 lines, grey)                            │
│ ┌────────── HERO GRAPHIC (≈38% of page) ────────────┐  │  device screen SVG
│ │ callout ◀── [ screen at work ] ──▶ callout        │  │  + halo + leader lines
│ └───────────────────────────────────────────────────┘  │
│ THE PROBLEM (red)          │ WHAT YOU GET (green ticks)│  3 pains │ 4–6 benefits
│ ── FEATURE SPEC · 47 features in 8 groups ──────────── │
│ [group] [group] [group] [group]   (2–3 highlights each)│
│ ── PROOF ── 4,821 │ 14 sec │ 868 │ 600 ─────────────── │  big Oxanium numbers
│ Works with: (chips)   Replaces: WATI, Interakt…        │
│ [Book a free demo →]  wakflow.com · +91 96253 30270    │  orange pill
└────────────────────────────────────────────────────────┘
```

The feature spec shows **every feature group name** from Part A and the 2–3 strongest features in each, plus the real total ("47 features") so the reader knows the depth.

### 4.2 Other pages

| Page | Content |
|---|---|
| 1 Cover | Wordmark, "Product Catalogue 2026", headline "One system for every message, every lead and every follow-up.", large SVG: the Wakflow core with 17 product nodes wired around it, grouped by family colour. |
| 2 Intro | `// 00 THE PLATFORM`: 4 pains → 6-step "How it works" journey diagram (customer gets in touch → AI answers → lead saved → human takes over → follow-ups run → you stay in control) → "We run our own businesses on Wakflow" with 6 measured numbers (GSM + Tripwaley). |
| 3–4 Product list | 17 products in 6 families, each row: page code, icon, official name, 1–2 line description (from the overview's Products table), page number. Flagship highlighted with orange star. |
| 5–21 | One product per page (order below). |
| 22 Back cover | Final call to action ("Stop running your business across apps that don't talk to each other."), 3 steps to start, wakflow.com, +91 96253 30270, two QR codes (WhatsApp chat + website). |

### 4.3 Product order, graphic and proof per page

| Page code | Product (official name) | Family | Hero graphic (SVG) | Proof / day one |
|---|---|---|---|---|
| 01 ⭐ | Wakflow Personal AI Assistant | Flagship | Phone chat: 7:30 am morning briefing, approve/deny buttons, voice note | 51 of 53 runs; 21 of 21 daily checks; 3 real problems found in week one; 27 of 27 leads confirmed |
| 02 | Wakflow WhatsApp Connect | Talk to customers | QR scan → many numbers → hub wired to Inbox, AI, CRM, Automations | 91,907 messages; 21,396 contacts; 15,967 in 30 days; 5 numbers |
| 03 | Wakflow Inbox | Talk to customers | 3-pane shared inbox, channel icons, owners, statuses | 20,407 conversations; 320,557 messages; 10 team members; 2,760 notes |
| 04 | Wakflow Instagram Automation | Talk to customers | Reel with "price?" comments → auto reply → DM carousel → number → call | 454 IG customers (440 with phone); 216 leads in June; 637 interactions in 44 h |
| 05 | Wakflow Dashboard Websites | Talk to customers | Website + dashboard panel, "Save → Live" | 53 packages / 195 prices; 214 enquiries; PageSpeed 92 / 100; 94 pages |
| 06 | Wakflow AI WhatsApp Agent | AI agents | Hinglish sales chat with photos, "typing…", hand-over alert | 4,821 conversations; 14 s reply; 868 hand-overs; 600 chats for a furniture retailer |
| 07 | Wakflow AI Voice Calling Agent | AI agents | Call screen with waveform + timeline (lead → call in ~1 min → WhatsApp sent → callback → score) | 68 calls, 85% answered; 0.91 s first word; 82/100 quality; ~2 min talk |
| 08 | Wakflow CRM | Capture & sell | Pipeline board with source-tagged lead cards + "My follow-ups today" | 11,476 + 3,023 records; only 63 typed by hand; 11,781 tasks; 27-person team |
| 09 | Wakflow Lead Capture & CRM Sync | Capture & sell | Sources → cleaner ("+91 98…", "098…", "98…" → one) → CRM + task; GREEN/AMBER/RED audit lamp | 27 of 27 leads, zero lost; 10,746 from WhatsApp; 454 from Instagram; 288 in 30 days |
| 10 | Wakflow Bookings & Payment Follow-ups | Capture & sell | Booking timeline (hold → advance → reminder → balance → invoice) + receipt | 366 confirmed bookings; 6 live web bookings; branded PDF invoice; checked every morning |
| 11 | Wakflow WhatsApp Broadcasts | Capture & sell | One message fanning into many different wordings, human-paced gaps, replies returning | 199 contacts → 188 sent → 27 new leads (about 1 in 7) |
| 12 | Wakflow Lead Finder | Grow | Chat prompt "50 marketing heads at real estate firms in Pune" → verified result table | Day one list |
| 13 | Wakflow Cold Email Engine | Grow | 7-week sending ramp + inbox-not-spam meter + WhatsApp reply alert | Day one list |
| 14 | Wakflow AI Carousel Studio | Grow | Topic in chat → 3 slide versions → approve ✓ → "Post now" | Day one list |
| 15 | Wakflow AI Video Factory | Grow | Vertical film strip: script → voice → scenes → captions → publish | Day one list |
| 16 | Wakflow Automate | Run & protect | Node flow: trigger → AI decides → human approval → actions; recipe chips | 88 built / 33 running; 27 of 27 leads; 15,967 messages |
| 17 | Wakflow Care | Run & protect | Heartbeat line + shield + backup calendar of green ticks | 11 nightly backups in a row (7 databases); 21 checks in 21 days; 1,370 records restored; 13 full-system backups |

## 5. How it is built

- `wakflow-catalogue/` in this repo.
- `content/products.yaml` — hand-picked Part A text per product (headline, sub, pains, benefits, feature groups + highlights, feature count, proof, works-with, replaces). Text copied from Part A, only shortened, never changed in meaning.
- `svg/*.svg` — one hand-drawn hero graphic per product + cover system map + icons.
- `templates/*.html.j2` + `styles/catalogue.css` — Jinja2 templates, CSS `@page { size: A4 }`, one `<section class="page">` per page.
- `fonts/` — Oxanium, DM Sans, JetBrains Mono (open-source OFL fonts, embedded).
- `build.py` → `dist/catalogue.html`; `render.mjs` (Playwright + Chromium) → `dist/Wakflow-Catalogue-2026.pdf`.
- QR codes made with `segno` (open source).

## 6. Checks before delivery

1. PDF has exactly 22 pages; no page overflows (automatic check of every page's content height).
2. Banned-word scan on the output: no underlying software names, no internal names, no client names.
3. Every proof number in the PDF matches the Part A source text (automatic check).
4. Visual review of every page as an image; fix, re-check once.
5. Impeccable detector + independent finish review.
6. Text stays readable on a phone: body text never below 7.5 pt.

## 7. Out of scope

Website build (next project), printing-ink optimisation (the brand is black; a white print version can be made later), Part B internal content.
