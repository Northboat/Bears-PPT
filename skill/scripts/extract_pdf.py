#!/usr/bin/env python3
"""
extract_pdf.py — Extract text from a PDF into a page-delimited plaintext file.

Output format (matches the existing pdf_text.txt convention):
    --- PAGE 0 ---
    <page-0 text>
    --- PAGE 1 ---
    <page-1 text>
    ...

Usage:
    pip install pdfplumber
    python scripts/extract_pdf.py input.pdf output.txt

Why this exists:
    A Slidev paper-share deck is built by reading a source PDF, distilling
    its sections, and rewriting them into slides.md. Having the PDF as flat
    text with page markers lets you grep / cite specific pages without
    repeatedly opening a PDF viewer.

Notes:
    - pdfplumber is preferred for academic papers (better column / equation
      handling than PyPDF2). pymupdf (`fitz`) is faster but sometimes
      mis-orders columns.
    - Text from scanned PDFs requires OCR (tesseract) and is out of scope.
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path


def extract(pdf_path: Path, out_path: Path) -> None:
    try:
        import pdfplumber
    except ImportError:
        sys.exit("pdfplumber not installed. Run: pip install pdfplumber")

    chunks: list[str] = []
    with pdfplumber.open(pdf_path) as pdf:
        for i, page in enumerate(pdf.pages):
            text = page.extract_text() or ""
            chunks.append(f"--- PAGE {i} ---\n{text}\n")

    out_path.write_text("\n".join(chunks), encoding="utf-8")
    print(f"Wrote {len(chunks)} pages → {out_path}")


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[1])
    ap.add_argument("pdf", type=Path, help="Source PDF file")
    ap.add_argument("out", type=Path, nargs="?", default=Path("pdf_text.txt"),
                    help="Output plaintext file (default: pdf_text.txt)")
    args = ap.parse_args()

    if not args.pdf.exists():
        sys.exit(f"PDF not found: {args.pdf}")
    extract(args.pdf, args.out)


if __name__ == "__main__":
    main()
