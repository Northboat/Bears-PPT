#!/usr/bin/env python3
"""
fix_tables.py — Wrap raw <tr> rows inside <tbody> in slides.md.

Why this exists:
    Vue's template compiler emits a warning "<tr> cannot be child of <table>"
    when a raw HTML table omits <tbody>. Browsers auto-insert <tbody> at
    runtime, but Vue's compile-time parser does not, causing hydration
    warnings and potential mis-rendering.

What it does:
    Detects <table>...</table> blocks that contain <tr> directly (no
    <tbody>/<thead>/<tfoot>) and wraps the rows in <tbody>...</tbody>.

    <table>             →   <table>
      <tr>...</tr>            <tbody>
      <tr>...</tr>              <tr>...</tr>
    </table>                    <tr>...</tr>
                              </tbody>
                            </table>

Idempotency:
    Tables that already contain <tbody>/<thead>/<tfoot> are left untouched.

Usage:
    python scripts/fix_tables.py [path/to/slides.md]
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

TABLE_RE = re.compile(r"(<table\b[^>]*>)(.*?)(</table>)", re.DOTALL | re.IGNORECASE)
HAS_BODY_RE = re.compile(r"<(tbody|thead|tfoot)\b", re.IGNORECASE)


def wrap_rows(inner: str) -> str:
    """Wrap loose <tr>...</tr> rows inside a <tbody>."""
    if HAS_BODY_RE.search(inner):
        return inner  # already structured

    # Find the leading whitespace before the first <tr> to preserve indent.
    m = re.search(r"\s*<tr\b", inner, re.IGNORECASE)
    if not m:
        return inner
    head, body = inner[:m.start()], inner[m.start():]

    # Indent body by 2 extra spaces; trim trailing whitespace before </table>.
    indent = re.match(r"\s*", body).group(0)
    body_stripped = body.rstrip()
    indented = re.sub(r"\n", "\n  ", body_stripped)

    return f"{head}{indent}<tbody>{indented}\n  </tbody>\n"


def transform(text: str) -> str:
    return TABLE_RE.sub(
        lambda m: f"{m.group(1)}{wrap_rows(m.group(2))}{m.group(3)}",
        text,
    )


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
