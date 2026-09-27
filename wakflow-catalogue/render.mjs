// Prints dist/catalogue.html to dist/Wakflow-Catalogue-2026.pdf and writes dist/report.json
// with page overflow, font loading and minimum text size checks.
// Run: node render.mjs [--shots]   (--shots also saves a PNG of every page in .impeccable/review/)
import { chromium } from 'playwright';
import { writeFileSync, mkdirSync } from 'node:fs';
import { fileURLToPath, pathToFileURL } from 'node:url';
import path from 'node:path';

const here = path.dirname(fileURLToPath(import.meta.url));
const argHtml = process.argv.indexOf('--html');
const html = argHtml > 0 ? path.resolve(process.argv[argHtml + 1]) : path.join(here, 'dist', 'catalogue.html');
const checkOnly = process.argv.includes('--check-only');
const pdf = path.join(here, 'dist', 'Wakflow-Catalogue-2026.pdf');
const shots = process.argv.includes('--shots');

const FONTS = ['600 20px Oxanium', '700 20px Oxanium', '800 20px Oxanium',
  '400 12px "DM Sans"', '500 12px "DM Sans"', '600 12px "DM Sans"',
  '400 10px "JetBrains Mono"', '500 10px "JetBrains Mono"'];

const browser = await chromium.launch();
const page = await browser.newPage({ viewport: { width: 794, height: 1123 }, deviceScaleFactor: 2 });
await page.goto(pathToFileURL(html).href, { waitUntil: 'networkidle' });
await page.evaluate(async (fonts) => { await Promise.all(fonts.map((f) => document.fonts.load(f).catch(() => null))); await document.fonts.ready; }, FONTS);
await page.emulateMedia({ media: 'print' });

const report = await page.evaluate((fonts) => {
  // document.fonts.check() is true when no face matches at all, so require a loaded FontFace per family + weight.
  const faces = [...document.fonts].filter((f) => f.status === 'loaded');
  const missing = fonts.filter((spec) => {
    const [, weight, fam] = spec.match(/^(\d+) \S+ "?([^"]+)"?$/);
    return !faces.some((f) => f.family.replace(/["']/g, '') === fam && (f.weight === weight || f.weight.includes(' ')));
  });
  const pages = [...document.querySelectorAll('.page')];
  const overflows = [];
  pages.forEach((pg, i) => {
    const box = pg.getBoundingClientRect();
    let worst = 0;
    pg.querySelectorAll('*').forEach((el) => {
      if (el.closest('.bleed')) return;
      const r = el.getBoundingClientRect();
      if (r.width === 0 || r.height === 0) return;
      worst = Math.max(worst, r.bottom - box.bottom, r.right - box.right, box.left - r.left, box.top - r.top);
    });
    // text clipped inside fixed boxes
    pg.querySelectorAll('.fit').forEach((el) => {
      worst = Math.max(worst, el.scrollHeight - el.clientHeight - 1, el.scrollWidth - el.clientWidth - 1);
    });
    if (worst > 1) overflows.push({ page: i + 1, over_px: Math.round(worst) });
  });
  let minBody = 99, minBodyWhere = '', minLabel = 99, minLabelWhere = '';
  const walker = document.createTreeWalker(document.body, NodeFilter.SHOW_TEXT);
  while (walker.nextNode()) {
    const t = walker.currentNode;
    if (!t.textContent.trim()) continue;
    const el = t.parentElement;
    const cs = getComputedStyle(el);
    if (cs.display === 'none' || cs.visibility === 'hidden') continue;
    let px = parseFloat(cs.fontSize);
    const inSvg = el instanceof SVGElement;
    if (inSvg) { const m = el.getScreenCTM(); if (m) px *= Math.hypot(m.a, m.b); }
    const pt = px * 0.75;
    const isLabel = inSvg || /JetBrains/.test(cs.fontFamily) || el.closest('.micro');
    const where = `p${pages.indexOf(el.closest('.page')) + 1}: "${t.textContent.trim().slice(0, 30)}"`;
    if (isLabel) { if (pt < minLabel) { minLabel = pt; minLabelWhere = where; } }
    else if (pt < minBody) { minBody = pt; minBodyWhere = where; }
  }
  return { pages: pages.length, overflows, fonts_ok: missing.length === 0, fonts_missing: missing,
    min_body_pt: +minBody.toFixed(2), min_body_where: minBodyWhere,
    min_label_pt: +minLabel.toFixed(2), min_label_where: minLabelWhere };
}, FONTS);

if (checkOnly) { await browser.close(); console.log(JSON.stringify(report)); process.exit(0); }

if (shots) {
  const dir = path.join(here, '..', '.impeccable', 'review');
  mkdirSync(dir, { recursive: true });
  const n = report.pages;
  for (let i = 0; i < n; i++) {
    const el = (await page.$$('.page'))[i];
    await el.screenshot({ path: path.join(dir, `page-${String(i + 1).padStart(2, '0')}.png`) });
  }
}

await page.pdf({ path: pdf, preferCSSPageSize: true, printBackground: true });
await browser.close();
writeFileSync(path.join(here, 'dist', 'report.json'), JSON.stringify(report, null, 2));
console.log(JSON.stringify(report));
if (report.overflows.length || !report.fonts_ok) process.exitCode = 1;
