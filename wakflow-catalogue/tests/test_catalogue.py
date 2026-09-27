"""Catalogue checks. Run: python3 tests/test_catalogue.py [name ...]
Dark edition: WAKFLOW_THEME=dark python3 tests/test_catalogue.py"""
import json
import os
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DIST = ROOT / "dist"
DARK = os.environ.get("WAKFLOW_THEME") == "dark"
PDF = DIST / ("Wakflow-Catalogue-2026-Dark.pdf" if DARK else "Wakflow-Catalogue-2026.pdf")
REPORT = DIST / ("report-dark.json" if DARK else "report.json")
HTML = DIST / ("catalogue-dark.html" if DARK else "catalogue.html")
SVG = ROOT / "svg" / "dark" if DARK else ROOT / "svg"   # hero drawings and cover map for this edition

EXPECTED_PAGES = 22


def _report():
    return json.loads(REPORT.read_text())


# ---------- Task 1: pipeline ----------

def test_pdf_page_count():
    import pymupdf
    doc = pymupdf.open(PDF)
    assert doc.page_count == EXPECTED_PAGES, f"{doc.page_count} pages, want {EXPECTED_PAGES}"
    for i, page in enumerate(doc):
        w, h = page.rect.width, page.rect.height
        assert abs(w - 595.3) < 1.5 and abs(h - 841.9) < 1.5, f"page {i+1} is {w}x{h}, not A4"


def test_no_page_overflows():
    over = _report()["overflows"]
    assert over == [], f"content overflows: {over}"


def test_fonts_loaded():
    r = _report()
    assert r["fonts_ok"] is True, f"fonts not loaded: {r.get('fonts_missing')}"


def test_min_font_size():
    r = _report()
    assert r["min_body_pt"] >= 8.0, f"body text too small: {r['min_body_pt']}pt at {r['min_body_where']}"
    assert r["min_label_pt"] >= 7, f"label text too small: {r['min_label_pt']}pt at {r['min_label_where']}"


# ---------- Task 2: content ----------

sys.path.insert(0, str(ROOT / "content"))
OFFICIAL_NAMES = {
    "Wakflow AI Voice Calling Agent", "Wakflow WhatsApp Connect", "Wakflow Inbox", "Wakflow CRM",
    "Wakflow Automate", "Wakflow AI WhatsApp Agent", "Wakflow Lead Capture & CRM Sync",
    "Wakflow Instagram Automation", "Wakflow AI Carousel Studio", "Wakflow Bookings & Payment Follow-ups",
    "Wakflow WhatsApp Broadcasts", "Wakflow Cold Email Engine", "Wakflow Lead Finder",
    "Wakflow AI Video Factory", "Wakflow Care", "Wakflow Personal AI Assistant", "Wakflow Dashboard Websites",
}
NUM = re.compile(r"\d[\d,.]*\d%?|\d%?")


def _products():
    import yaml
    return yaml.safe_load((ROOT / "content" / "products.yaml").read_text())["products"]


def _site():
    import yaml
    return yaml.safe_load((ROOT / "content" / "site.yaml").read_text())


def _norm(s):
    return re.sub(r"\s+", " ", s.replace("**", ""))


def _numbers_in(s):
    return [n.rstrip(".,") for n in NUM.findall(s)]


def _num_in(n, src):
    """True when number n appears in src as a whole number (not as part of a longer one)."""
    return re.search(r"(?<![\d,.])" + re.escape(n) + r"(?![\d]|[,.]\d)", src) is not None


def test_all_products_present():
    ps = _products()
    names = [p["name"] for p in ps]
    assert len(names) == 17 and set(names) == OFFICIAL_NAMES, set(names) ^ OFFICIAL_NAMES
    assert [p["code"] for p in ps] == [f"{i:02d}" for i in range(1, 18)]
    assert sum(p.get("flagship", False) for p in ps) == 1


def test_proof_numbers_in_source():
    import partA
    bad = []
    for p in _products():
        src = _norm(partA.text(p["file"]))
        items = p["proof"]["items"]
        texts = [f"{i['n']} {i['l']}" for i in items] if p["proof"]["kind"] == "numbers" else list(items)
        for tx in texts:
            for n in _numbers_in(tx):
                if not _num_in(n, src):
                    bad.append((p["code"], n, tx))
    assert not bad, bad


def test_feature_totals():
    import partA
    bad = []
    for p in _products():
        groups = dict(partA.feature_groups(p["file"]))
        total = sum(len(v) for v in groups.values())
        if p["feature_total"] != total:
            bad.append((p["code"], "total", p["feature_total"], total))
        shown = [g["name"] for g in p["feature_groups"]]
        if shown != list(groups):
            bad.append((p["code"], "groups", shown, list(groups)))
        for g in p["feature_groups"]:
            for it in g["items"]:
                src = it["src"] if isinstance(it, dict) else it
                if src not in groups.get(g["name"], []):
                    bad.append((p["code"], g["name"], src))
    assert not bad, bad


def test_works_with_codes_valid():
    codes = {p["code"] for p in _products()}
    for p in _products():
        ww = p["works_with"]
        assert 3 <= len(ww) <= 7 and set(ww) <= codes and p["code"] not in ww, (p["code"], ww)


# ---------- Task 3: graphics ----------

def test_svgs_valid():
    import xml.etree.ElementTree as ET
    sys.path.insert(0, str(ROOT / "svg"))
    slugs = [p["slug"] for p in _products()]
    files = [SVG / "hero" / f"{s}.svg" for s in slugs] + [ROOT / "svg" / "icons" / f"{s}.svg" for s in slugs]
    files += [SVG / "cover-map.svg"]
    bad = []
    for f in files:
        if not f.exists():
            bad.append((f.name, "missing"))
            continue
        txt = f.read_text()
        root = ET.fromstring(txt)
        if not root.get("viewBox") or root.get("width"):
            bad.append((f.name, "needs viewBox and no fixed width"))
        for unsafe in ("opacity", "radialGradient", "filter", "mask"):
            if unsafe in txt:
                bad.append((f.name, "PDF-unsafe", unsafe))
    assert not bad, bad


# ---------- Task 4: pages ----------

BANNED_CI = ["n8n", "chatwoot", "baileys", "livekit", "vobiz", "minio", "edge-tts", "nca toolkit", "crm2",
             "naveen", "hermes agent", "evolution api", "gemini live", "tripwaley.in", "ghoomosasteme.in"]
BANNED_CS = [r"\bEvolution\b", r"\bTwenty\b", r"\bHermes\b", r"\bNCA\b"]


def _html():
    return HTML.read_text()


def _sections():
    return re.findall(r'<section (?:id="[^"]*" )?class="page ([^"]*)"([^>]*)>(.*?)</section>', _html(), re.S)


def test_no_banned_words():
    html = _html()
    low = html.lower()
    hits = [w for w in BANNED_CI if w in low]
    hits += [p for p in BANNED_CS if re.search(p, html)]
    hits += re.findall(r"\b\d{1,3}(?:\.\d{1,3}){3}\b", html)
    assert not hits, hits


def test_index_page_numbers():
    secs = _sections()
    assert len(secs) == EXPECTED_PAGES, len(secs)
    rows = re.findall(r'class="idx-row[^"]*" data-code="(\d+)" data-page="(\d+)"', _html())
    assert len(rows) == 17, rows
    for code, pg in rows:
        n = int(pg)
        assert n == 4 + int(code), (code, pg)
        cls, attrs, _ = secs[n - 1]
        assert "product" in cls and f'data-code="{code}"' in attrs, (code, n, cls, attrs)


def test_contact_printed():
    secs = _sections()
    cover, back = secs[0][2], secs[-1][2]
    assert "wakflow.com" in cover and "+91 96253 30270" in cover
    assert "wakflow.com" in back and "+91 96253 30270" in back


# ---------- Final review fixes ----------

def test_proof_matcher_rejects_substrings():
    src = "11,476 customers, 868 alerts, 4,821 chats, 0.91 seconds, 85% answered"
    for good in ("11,476", "868", "4,821", "0.91", "85%"):
        assert _num_in(good, src), good
    for bad in ("1,476", "11,47", "86", "4,82", "0.9", "91"):
        assert not _num_in(bad, src), bad


def test_font_check_catches_missing_stylesheet():
    """Rendering a copy whose stylesheet has no @font-face must report fonts_ok false."""
    import shutil
    import subprocess
    css = (ROOT / "styles" / "catalogue.css").read_text().replace('@import url("fonts.css");', "")
    (ROOT / "styles" / "_nofonts.css").write_text(css)
    html = HTML.read_text().replace("../styles/catalogue.css", "../styles/_nofonts.css")
    probe = DIST / "_nofonts.html"
    probe.write_text(html)
    try:
        out = subprocess.run(["node", str(ROOT / "render.mjs"), "--html", str(probe), "--check-only"],
                             capture_output=True, text=True, cwd=ROOT)
        rep = json.loads(out.stdout.strip().splitlines()[-1])
        assert rep["fonts_ok"] is False, rep
    finally:
        probe.unlink(missing_ok=True)
        (ROOT / "styles" / "_nofonts.css").unlink(missing_ok=True)


def test_pdf_has_tappable_links():
    import pymupdf
    doc = pymupdf.open(PDF)
    back = [l.get("uri", "") for l in doc[-1].get_links()]
    for want in ("https://wa.me/919625330270", "tel:+919625330270", "https://wakflow.com"):
        assert any(u.startswith(want) for u in back), (want, back)
    idx = [l for pg in (doc[2], doc[3]) for l in pg.get_links() if l.get("kind") in (pymupdf.LINK_GOTO, pymupdf.LINK_NAMED)]
    assert len(idx) >= 17, len(idx)


def test_demo_button_only_on_first_and_last_page():
    import pymupdf
    doc = pymupdf.open(PDF)
    pages = [i + 1 for i, pg in enumerate(doc)
             if any(l.get("uri", "").startswith("https://wa.me/") for l in pg.get_links())
             or "free demo" in pg.get_text().lower()]
    assert pages == [1, EXPECTED_PAGES], pages


def test_fonts_embedded_as_real_fonts():
    import pymupdf
    doc = pymupdf.open(PDF)
    kinds = {f[2] for pg in doc for f in pg.get_fonts()}
    assert "Type3" not in kinds, kinds
    assert PDF.stat().st_size < 4_000_000, PDF.stat().st_size


# ---------- Redesign: PDF-safe rendering + owner content ----------

def test_css_has_no_pdf_unsafe_effects():
    css = (ROOT / "styles" / "catalogue.css").read_text() + (ROOT / "styles" / "dark.css").read_text()
    for bad in ("background-clip", "box-shadow", "mask-image", "filter:", "backdrop-filter", "rgba(", "opacity:",
                "color-mix", "text-shadow", "features in total"):
        assert bad not in css, bad


def test_pdf_has_no_transparency():
    """Transparency groups and alpha graphics states render as boxes in many PDF readers."""
    import pymupdf
    doc = pymupdf.open(PDF)
    bad = []
    for x in range(1, doc.xref_length()):
        obj = doc.xref_object(x, compressed=True)
        if "/ExtGState" in obj or "/Type/ExtGState" in obj or ("/ca " in obj or "/CA " in obj):
            for m in re.finditer(r"/(ca|CA)\s*([0-9.]+)", obj):
                if float(m.group(2)) < 0.999:
                    bad.append((x, m.group(0)))
            if re.search(r"/SMask\s*<<", obj):
                bad.append((x, "SMask"))
        if re.search(r"/SMask\s+\d+\s+0\s+R", obj):
            bad.append((x, "image soft mask"))
    assert not bad, bad[:10]


def test_key_features_from_source_or_owner():
    import partA
    bad = []
    for p in _products():
        kf = p["key_features"]
        if not 6 <= len(kf) <= 8:
            bad.append((p["code"], "count", len(kf)))
        names = {n for _, items in partA.feature_groups(p["file"]) for n in items}
        for k in kf:
            if isinstance(k, dict) and k.get("owner"):
                continue
            src = k["src"] if isinstance(k, dict) else k
            if src not in names:
                bad.append((p["code"], src))
    assert not bad, bad


def test_owner_requested_features_present():
    by = {p["slug"]: p for p in _products()}
    inbox = " ".join(str(k) for k in by["inbox"]["key_features"]).lower()
    assert "unlimited whatsapp numbers" in inbox and "same time" in inbox
    ig = " ".join(str(k) for k in by["instagram-automation"]["key_features"]).lower()
    assert "personalised" in ig and "comment" in ig


def test_product_pages_are_short_and_readable():
    """Reading text (outside the drawings) stays short enough for a phone; body text >= 8.25pt."""
    for cls, attrs, body in _sections():
        if "product" not in cls:
            continue
        text = re.sub(r"<svg.*?</svg>", " ", body, flags=re.S)
        words = len(re.sub(r"<[^>]+>", " ", text).split())
        assert words <= 165, (attrs, words)
    assert _report()["min_body_pt"] >= 8.25


def test_no_page_codes_that_clash_with_page_numbers():
    txt = (SVG / "cover-map.svg").read_text()
    codes = re.findall(r">(\d\d)</text>", txt)
    assert not codes, codes


if __name__ == "__main__":
    names = sys.argv[1:] or [n for n in dict(globals()) if n.startswith("test_")]
    failed = 0
    for n in names:
        try:
            globals()[n]()
            print(f"PASS {n}")
        except Exception as e:  # noqa: BLE001
            failed += 1
            print(f"FAIL {n}: {type(e).__name__}: {e}")
    print(f"--- {len(names) - failed}/{len(names)} passed")
    sys.exit(1 if failed else 0)
