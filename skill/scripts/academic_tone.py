#!/usr/bin/env python3
"""
academic_tone.py — Lint slides.md for promotional/emotional wording.

Why this exists:
    A paper-share deck must read as a neutral academic narrative, not a
    marketing pitch. Words like "恐怖", "魔术", "破局", "完美", trailing
    "！", and similar tonal noise have a habit of slipping in during
    drafting. This script reports any that remain so they can be rewritten
    by hand.

This is a LINTER, not an auto-rewriter:
    Tone fixes need human judgment ("巧妙引入" → what?). Reporting them
    line-by-line is far safer than blind substitution.

Usage:
    python scripts/academic_tone.py [path/to/slides.md]
    Exit code 1 if any banned word is found, 0 otherwise. Useful in CI.

Extending:
    Edit BANNED_PATTERNS below. Each is a regex; provide an explanation
    in the comment so contributors understand WHY a word is banned.
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

BANNED_PATTERNS: list[tuple[str, str]] = [
    # Emotional intensifiers
    (r"恐怖|惊人|爆炸|致命|金贵", "emotional intensity"),
    # Metaphorical / informal
    (r"魔术|破局|洗牌|掠影", "metaphorical / informal"),
    # Absolutist hype
    (r"完美|无懈可击|彻底", "absolutist hype"),
    # Promotional verbs
    (r"巧妙|大幅|锐减|落地|危机", "promotional verbs"),
    # Tonal noise
    (r"！", "full-width exclamation mark"),
]


def lint(path: Path) -> int:
    text = path.read_text(encoding="utf-8")
    hits = 0
    for i, line in enumerate(text.splitlines(), 1):
        for pattern, reason in BANNED_PATTERNS:
            for m in re.finditer(pattern, line):
                print(f"{path}:{i}: {m.group(0)!r}  ({reason})")
                print(f"    {line.strip()}")
                hits += 1
    return hits


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[1])
    default = Path(__file__).resolve().parent.parent / "slides.md"
    ap.add_argument("path", type=Path, nargs="?", default=default)
    args = ap.parse_args()

    if not args.path.exists():
        sys.exit(f"Not found: {args.path}")

    hits = lint(args.path)
    if hits:
        print(f"\n{hits} banned word(s) found. Rewrite by hand using neutral language.")
        sys.exit(1)
    print("Tone check passed.")


if __name__ == "__main__":
    main()
