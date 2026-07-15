#!/usr/bin/env python3
"""
fix_anim_loop.py — Migrate Vue animation components from setInterval to setTimeout.

Why this exists:
    `setInterval` races with reset/clear timers when an animation loops
    back to step 0, causing the first step to fire twice. The recursive
    `setTimeout` pattern handles the end-of-loop reset cleanly.

What it does:
    Detects the pattern below in any `components/*.vue` file and rewrites
    it to use a recursive `playStep()` helper.

    BEFORE:
        let interval
        onMounted(() => {
          interval = setInterval(() => { ... }, 2000)
        })
        onUnmounted(() => clearInterval(interval))

    AFTER:
        let timerId = null
        const playStep = () => {
          if (activeStep.value < steps.length - 1) {
            timerId = setTimeout(() => { activeStep.value++; playStep() }, 2000)
          } else { /* end state */ }
        }
        onMounted(() => { timerId = setTimeout(playStep, 500) })
        onUnmounted(() => clearTimeout(timerId))

    Because every animation has different state-mutation logic, this
    script is conservative: it only flags components that still use
    `setInterval` and prints the file path for manual rewrite. It does
    NOT auto-rewrite — too easy to corrupt.

Usage:
    python scripts/fix_anim_loop.py [components_dir]
    (defaults to ../components)
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

INTERVAL_MARKER = "setInterval("


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[1])
    default = Path(__file__).resolve().parent.parent / "components"
    ap.add_argument("dir", type=Path, nargs="?", default=default)
    args = ap.parse_args()

    if not args.dir.is_dir():
        sys.exit(f"Not a directory: {args.dir}")

    flagged = []
    for vue in sorted(args.dir.rglob("*.vue")):
        if INTERVAL_MARKER in vue.read_text(encoding="utf-8"):
            flagged.append(vue)

    if not flagged:
        print("All animations use setTimeout. Good.")
        return

    print("Components still using setInterval (rewrite manually with recursive setTimeout):")
    for v in flagged:
        print(f"  - {v}")
    sys.exit(1)


if __name__ == "__main__":
    main()
