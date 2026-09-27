"""Reads Part A source files: feature groups and counts, used by tests."""
import re
from pathlib import Path

SRC = Path(__file__).resolve().parent / "source"


def text(file):
    return (SRC / file).read_text()


def section(file, heading):
    t = text(file)
    m = re.search(rf"^### {re.escape(heading)}\s*$(.*?)(?=^### |\Z)", t, re.S | re.M)
    return m.group(1) if m else ""


def feature_groups(file):
    """[(group name, [feature names])] — a feature is a line starting with bold text (links excluded)."""
    out = []
    for block in re.split(r"^#### ", section(file, "Features"), flags=re.M)[1:]:
        name, _, body = block.partition("\n")
        items = re.findall(r"^\s*(?:- )?\*\*([^*\[][^*]*?)\*\*", body, re.M)
        out.append((name.strip(), [i.strip().rstrip(".") for i in items]))
    return out
