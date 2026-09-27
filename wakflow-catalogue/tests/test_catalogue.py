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
