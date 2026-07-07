# bears-ppt-skill

A self-contained, drop-in skill for building academic paper-share presentations using [Slidev](https://sli.dev/).

This skill captures the conventions, batch-processing scripts, and authoring workflow distilled from a real paper-share project. Any AI assistant or new contributor who reads `SKILL.md` can immediately begin authoring `slides.md` without prior context.

## Contents

```
bears-ppt-skill/
├── README.md                    ← you are here
├── SKILL.md                     ← the actual skill: read this first
├── pdf_text.sample.txt          ← example output of extract_pdf.py
└── scripts/                     ← batch helpers (idempotent, single-purpose)
    ├── extract_pdf.py           ← PDF → page-delimited plaintext
    ├── fix_math.py              ← LaTeX $...$ → HTML entities
    ├── fix_headings.py          ← strip "1. " / "①" prefixes
    ├── fix_tables.py            ← wrap <tr> in <tbody>
    ├── fix_anim_loop.py         ← detect setInterval in animations
    ├── normalize_spacing.py     ← unify mt-* values
    ├── academic_tone.py         ← lint promotional words
    └── replace_block.py         ← swap delimited section
```

## Quick start

1. **Copy this folder** into your Slidev project root, or drop the scripts into an existing `scripts/` directory.
2. **Read `SKILL.md`** end to end. It is the contract.
3. **Run the scripts** as part of your authoring loop:
   ```bash
   pip install pdfplumber
   python scripts/extract_pdf.py paper.pdf pdf_text.txt
   # ... draft slides.md by reading pdf_text.txt ...
   python scripts/fix_math.py
   python scripts/fix_headings.py
   python scripts/fix_tables.py
   python scripts/normalize_spacing.py --apply
   python scripts/academic_tone.py
   ```

## What this skill encodes

- **Slidev authoring conventions** — hard rules covering math rendering (incl. CSS-Grid matrix/formula layout), overflow handling, table markup, heading numbering, spacing scale, and Vue animation patterns. Each rule traces to a concrete bug.
- **Tone standard** — banned-word list (`恐怖`, `魔术`, `破局`, `完美`, etc.) + replacement vocabulary, suitable for academic narration rather than marketing pitch.
- **Authoring pipeline** — PDF → plaintext → distilled slides → batch fix-ups → lint → preview.
- **Manual-play animation pattern** — recursive `setTimeout`, control bar styling, opacity / sizing specs, drop-in for any new component.
- **Talk-script craft** — word-budget math, per-slide pacing, read-aloud register, page-by-page structure, self-check list. See SKILL.md §12.

## Adapting the skill

Each script is intentionally short (under 100 lines) so you can extend it for a new paper / new domain:

- New banned word? → `BANNED_PATTERNS` in `academic_tone.py`
- New LaTeX construct? → `REGEX_RULES` in `fix_math.py`
- New spacing rule? → `TARGETS` in `normalize_spacing.py`

Avoid building a "fix everything" mega-script. Composable single-purpose tools are easier to debug.

## License

Use freely. No attribution required.
