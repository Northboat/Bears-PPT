#!/usr/bin/env python3
"""
fix_headings.py — Strip manual numeric prefixes from slide headings.

Why this exists:
    Slidev's <Toc> component auto-numbers headings. Manually-numbered
    headings ("# 1. 研究背景") render as "1. 1. 研究背景" in the TOC,
    a duplicate-number bug. This script normalizes headings to plain titles.

What it removes:
    # 1. Title           →  # Title
    # 12.  Title         →  # Title          (extra spaces tolerated)
    ## 1.2 Subtitle      →  ## Subtitle      (multi-level numbering)
    ## ① Section         →  ## Section       (Chinese circled numerals)
    ## (一) Section      →  ## Section       (Chinese parenthetical numerals)

What it preserves:
    Headings that contain numbers as part of the actual title text, e.g.
    "## 协议流程图 (1/2)" — the parenthetical (1/2) is content, not a prefix.

Usage:
    python scripts/fix_headings.py [path/to/slides.md]
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

# Heading line: ^(#+) <prefix><title>$
# Prefix patterns to strip (only at the start of the heading text):
PREFIX_PATTERNS = [
    r"\d+(?:\.\d+)*\.?\s+",                        # "1. ", "1.2 ", "12. "
    r"[①②③④⑤⑥⑦⑧⑨⑩⑪⑫⑬⑭⑮⑯⑰⑱⑲⑳]\s*",  # circled digits
    r"[一二三四五六七八九十]+[、.\)]\s*",            # 一、 二. 三)
    r"\([一二三四五六七八九十\d]+\)\s*",             # (一) (1)
]

HEADING_RE = re.compile(r"^(#{1,6})\s+(.*)$", re.MULTILINE)
PREFIX_RE = re.compile("|".join(PREFIX_PATTERNS))


def strip_prefix(title: str) -> str:
    m = PREFIX_RE.match(title)
    return title[m.end():] if m else title


def transform(text: str) -> str:
    def repl(m: re.Match) -> str:
        hashes, title = m.group(1), m.group(2)
        return f"{hashes} {strip_prefix(title)}"
    return HEADING_RE.sub(repl, text)


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[1])
    default = Path(__file__).resolve().parent.parent / "slides.md"
    ap.add_argument("path", type=Path, nargs="?", default=default)
    args = ap.parse_args()

    if not args.path.exists():
        sys.exit(f"Not found: {args.path}")

    original = args.path.read_text(encoding="utf-8")
    updated = transform(original)
    if updated == original:
        print("No changes.")
        return
    args.path.write_text(updated, encoding="utf-8")
    print(f"Rewrote {args.path}")


if __name__ == "__main__":
    main()
