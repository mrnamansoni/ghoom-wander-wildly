// Contact sheet of all SVGs for review: node sheet.mjs -> ../.impeccable/review/svg-sheet-*.png
import { chromium } from 'playwright';
import { readdirSync, readFileSync, mkdirSync, writeFileSync } from 'node:fs';
import path from 'node:path';
const here = path.dirname(new URL(import.meta.url).pathname);
const heroes = readdirSync(path.join(here, 'svg/hero')).sort();
const css = `<link rel="stylesheet" href="styles/fonts.css"><style>body{background:#000;margin:0;padding:16px;display:grid;grid-template-columns:1fr;gap:18px;width:720px}
div{border:1px solid #222}p{color:#8892A4;font:11px 'JetBrains Mono';margin:4px}</style>`;
const out = path.join(here, '..', '.impeccable', 'review'); mkdirSync(out, { recursive: true });
const b = await chromium.launch(); const pg = await b.newPage({ viewport: { width: 760, height: 900 }, deviceScaleFactor: 1.5 });
const chunks = [heroes.slice(0, 6), heroes.slice(6, 12), heroes.slice(12)];
for (const [i, ch] of chunks.entries()) {
  const html = css + ch.map(f => `<p>${f}</p><div>${readFileSync(path.join(here, 'svg/hero', f), 'utf8')}</div>`).join('');
  writeFileSync(path.join(here, '_sheet.html'), html); await pg.goto('file://' + path.join(here, '_sheet.html')); await pg.evaluate(() => document.fonts.ready); await pg.waitForTimeout(300);
  await pg.screenshot({ path: path.join(out, `svg-sheet-${i + 1}.png`), fullPage: true });
}
writeFileSync(path.join(here, '_sheet.html'), css + `<div style="width:700px">${readFileSync(path.join(here, 'svg/cover-map.svg'), 'utf8')}</div>`); await pg.goto('file://' + path.join(here, '_sheet.html'));
await pg.evaluate(() => document.fonts.ready); await pg.waitForTimeout(300);
await pg.screenshot({ path: path.join(out, 'svg-cover.png'), fullPage: true });
await b.close(); console.log('sheets done');
