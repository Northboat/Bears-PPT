#!/usr/bin/env python3
"""
replace_block.py — Replace a delimited section of slides.md.

Why this exists:
    When swapping a static diagram for an interactive Vue component
    (e.g. replacing a long ```mermaid``` block with `<MyAnim />`), you
    need a reproducible way to find the right span of text. Hand-editing
    risks dropping unrelated lines.

How it works:
    Match by START heading (## ...) and END heading. The matched span
    is `[start, end)` — the END heading itself is preserved.

Usage:
    python scripts/replace_block.py \\
        --start "## 协议流程图 (1/2)" \\
        --end   "## 协议流程图 (2/2)" \\
        --replacement-file new_block.md \\
        [path/to/slides.md]

    Or pass --replacement directly as a string:
    python scripts/replace_block.py \\
        --start "## 老标题" --end "## 下一节标题" \\
        --replacement "## 新标题\\n\\n<MyAnim />\\n\\n"

Safety:
    Refuses to run if --start matches more than once. Refuses to run if
    --start or --end is not found.
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path


def find_unique(text: str, marker: str) -> int:
    occurrences = [m.start() for m in re.finditer(re.escape(marker), text)]
    if not occurrences:
        sys.exit(f"Marker not found: {marker!r}")
    if len(occurrences) > 1:
        sys.exit(
            f"Marker {marker!r} matches {len(occurrences)} times "
            "— use a more specific string."
        )
    return occurrences[0]


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[1])
    default = Path(__file__).resolve().parent.parent / "slides.md"
    ap.add_argument("path", type=Path, nargs="?", default=default)
    ap.add_argument("--start", required=True, help="Section start marker (must be unique)")
    ap.add_argument("--end", required=True, help="Section end marker (must be unique)")
    g = ap.add_mutually_exclusive_group(required=True)
    g.add_argument("--replacement", help="Replacement text")
    g.add_argument("--replacement-file", type=Path, help="File containing replacement text")
    args = ap.parse_args()

    if not args.path.exists():
        sys.exit(f"Not found: {args.path}")

    text = args.path.read_text(encoding="utf-8")
    s = find_unique(text, args.start)
    e = find_unique(text, args.end)
    if e <= s:
        sys.exit("--end occurs before --start; check your markers.")

    replacement = (
        args.replacement_file.read_text(encoding="utf-8")
        if args.replacement_file
        else args.replacement.encode().decode("unicode_escape")  # allow \n in CLI
    )

    new_text = text[:s] + replacement + text[e:]
    args.path.write_text(new_text, encoding="utf-8")
    chars_removed = e - s
    print(f"Replaced {chars_removed} chars in {args.path}")


if __name__ == "__main__":
    main()
