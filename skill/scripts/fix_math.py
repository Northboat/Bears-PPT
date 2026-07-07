#!/usr/bin/env python3
"""
fix_math.py — Convert LaTeX math notation to HTML-safe equivalents in slides.md.

Why this exists:
    Slidev's KaTeX renderer fails when `$...$` math is nested inside HTML
    blocks (<p>, <div>, <td>). The `$` characters survive as raw text,
    breaking the slide. This script flattens common math syntax to HTML
    tags + entities that render correctly in any context.

Usage:
    python scripts/fix_math.py [path/to/slides.md]
    (defaults to ../slides.md relative to this script)

Strategy:
    Two passes:
      1. Regex pass for parameterized constructs (A^T, A_1, A^{-1}, ...).
      2. Literal-string fallback pass for hard-to-regex sequences that
         appeared in the source paper.

    Both run idempotently — running twice produces the same output.

Coverage:
    LaTeX                      HTML
    ----------------------     ------------------------
    A^T, A^{-1}                A<sup>T</sup>, A<sup>-1</sup>
    A_1, A_{ij}                A<sub>1</sub>, A<sub>ij</sub>
    \\times                    &times;
    \\ne                       &ne;
    \\pmod p, (\\mod p)        (mod p)
    \\det(A)                   det(A)
    \\cdot                     ·
    $...$ / $$...$$            (delimiters stripped)
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

# (pattern, replacement) tuples applied in order.
# Patterns operate on the FULL file text; flags=re.DOTALL where multi-line.
REGEX_RULES: list[tuple[str, str]] = [
    # Superscripts: A^{...} → A<sup>...</sup>; A^T → A<sup>T</sup>
    (r"([A-Za-z0-9])\^\{([^}]+)\}", r"\1<sup>\2</sup>"),
    (r"([A-Za-z0-9])\^([A-Za-z0-9\-+]+)", r"\1<sup>\2</sup>"),
    # Subscripts: A_{...} → A<sub>...</sub>; A_1 → A<sub>1</sub>
    (r"([A-Za-z0-9])_\{([^}]+)\}", r"\1<sub>\2</sub>"),
    (r"([A-Za-z0-9])_([A-Za-z0-9]+)", r"\1<sub>\2</sub>"),
    # Common operators / functions
    (r"\\times", "&times;"),
    (r"\\ne(?![a-zA-Z])", "&ne;"),
    (r"\\le(?![a-zA-Z])", "&le;"),
    (r"\\ge(?![a-zA-Z])", "&ge;"),
    (r"\\cdot", "·"),
    (r"\\det", "det"),
    (r"\\pmod\s*\{?([^}\s]+)\}?", r"(mod \1)"),
    (r"\\bmod\s+", " mod "),
    # Strip remaining math delimiters (last, so the inner content is already converted).
    (r"\$\$([^$]+)\$\$", r"\1"),
    (r"\$([^$\n]+)\$", r"\1"),
]

# Verbatim string pairs — for sequences your regex pass missed.
# Add entries as needed; safe because str.replace is non-overlapping.
LITERAL_RULES: list[tuple[str, str]] = [
    # Examples (extend as the deck grows):
    # ("密文 c = A \\times t \\pmod p。", "密文 c = A &times; t (mod p)。"),
]


def transform(text: str) -> str:
    for pat, rep in REGEX_RULES:
        text = re.sub(pat, rep, text)
    for old, new in LITERAL_RULES:
        text = text.replace(old, new)
    return text


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[1])
    default = Path(__file__).resolve().parent.parent / "slides.md"
    ap.add_argument("path", type=Path, nargs="?", default=default,
                    help=f"Markdown file to rewrite (default: {default})")
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
