"""Catalogue checks. Run: python3 tests/test_catalogue.py [name ...]"""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DIST = ROOT / "dist"
PDF = DIST / "Wakflow-Catalogue-2026.pdf"
REPORT = DIST / "report.json"
HTML = DIST / "catalogue.html"

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
    assert r["min_body_pt"] >= 7.5, f"body text too small: {r['min_body_pt']}pt at {r['min_body_where']}"
    assert r["min_label_pt"] >= 6.5, f"label text too small: {r['min_label_pt']}pt at {r['min_label_where']}"


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
                if n not in src:
                    bad.append((p["code"], n, tx))
    site = _site()
    src0 = _norm(partA.text("00-wakflow-platform-overview.md"))
    for s in site["intro"]["stats"]:
        for n in _numbers_in(f"{s['n']} {s['l']}"):
            if n not in src0:
                bad.append(("intro", n, s["n"]))
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
    from kit import C
    allowed = {v.upper() for v in C.values()}
    slugs = [p["slug"] for p in _products()]
    files = [ROOT / "svg" / "hero" / f"{s}.svg" for s in slugs] + [ROOT / "svg" / "icons" / f"{s}.svg" for s in slugs]
    files += [ROOT / "svg" / "cover-map.svg"]
    bad = []
    for f in files:
        if not f.exists():
            bad.append((f.name, "missing"))
            continue
        txt = f.read_text()
        root = ET.fromstring(txt)
        if not root.get("viewBox") or root.get("width"):
            bad.append((f.name, "needs viewBox and no fixed width"))
        for hx in set(re.findall(r"#[0-9A-Fa-f]{6}\b", txt)):
            if hx.upper() not in allowed:
                bad.append((f.name, "off-brand colour", hx))
    assert not bad, bad


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
