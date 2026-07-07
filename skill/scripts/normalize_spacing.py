#!/usr/bin/env python3
"""
normalize_spacing.py — Enforce the deck-wide vertical-rhythm scale on slides.md.

Why this exists:
    Slides drift over time toward ad-hoc spacing values (mt-4, mt-8, mt-12)
    on roles where the convention is mt-6. This script normalizes those.

Convention (see skill.md §5.6):
    Container directly below an `## H2`               →  mt-6
    Bottom callout/summary <p> after a main block     →  mt-6
    Caption text under an icon/heading inside a card  →  mt-2
    Avoid mt-0, mt-8, mt-12 unless visually justified.

Strategy — opt-in, conservative:
    - Reports lines that mix mt-2 / mt-4 / mt-8 / mt-12 with grid/flex
      containers (high-confidence candidates for normalization).
    - With --apply, rewrites mt-8/mt-12 → mt-6 in those contexts.
    - mt-0 is reported but NOT rewritten (sometimes intentional).
    - Lines where mt-* appears inside a card's caption (`<p class="text-sm mt-2">`)
      are left alone.

Usage:
    python scripts/normalize_spacing.py [--apply] [path/to/slides.md]

    Without --apply  : dry-run, prints diff candidates.
    With --apply     : rewrites in place.
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

# Match a class attribute that contains both a layout container hint
# (grid|flex|justify-) and a margin-top value we want to normalize.
TARGETS = [
    (re.compile(r'(class="[^"]*\b(?:grid|flex|justify-)[^"]*\bmt-)8(\b[^"]*")'), r"\g<1>6\g<2>"),
    (re.compile(r'(class="[^"]*\b(?:grid|flex|justify-)[^"]*\bmt-)12(\b[^"]*")'), r"\g<1>6\g<2>"),
    # Bottom callout <p class="mt-4 ..."> patterns inside content slides
    (re.compile(r'(<p class="mt-)4(\s+text-sm[^"]*")'), r"\g<1>6\g<2>"),
]

# What to flag but not rewrite
WARN_PATTERNS = [
    (re.compile(r'class="[^"]*\bmt-0\b'), "mt-0 — verify intentional"),
]


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[1])
    default = Path(__file__).resolve().parent.parent / "slides.md"
    ap.add_argument("path", type=Path, nargs="?", default=default)
    ap.add_argument("--apply", action="store_true", help="Rewrite in place (default: dry-run)")
    args = ap.parse_args()

    if not args.path.exists():
        sys.exit(f"Not found: {args.path}")

    text = args.path.read_text(encoding="utf-8")
    lines = text.splitlines(keepends=True)

    changes = 0
    for i, line in enumerate(lines):
        new_line = line
        for pat, repl in TARGETS:
            new_line2, n = pat.subn(repl, new_line)
            if n:
                print(f"{args.path}:{i+1}: {line.rstrip()}")
                print(f"  →           {new_line2.rstrip()}")
                new_line = new_line2
                changes += n
        lines[i] = new_line
        for pat, msg in WARN_PATTERNS:
            if pat.search(line):
                print(f"{args.path}:{i+1}: {msg}")

    if changes == 0:
        print("No spacing inconsistencies detected.")
        return

    if args.apply:
        args.path.write_text("".join(lines), encoding="utf-8")
        print(f"\nApplied {changes} change(s).")
    else:
        print(f"\n{changes} change(s) would be applied. Re-run with --apply to commit.")


if __name__ == "__main__":
    main()
