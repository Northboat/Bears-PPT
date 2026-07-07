# Slidev Presentation Skill — bears-ppt-skill

A self-contained guide for any AI assistant or new contributor to immediately start authoring an academic paper-share Slidev deck without prior context. Read this once, then begin working on the target project's `slides.md`.

This skill was distilled from a real paper-share project. Its rules trace to concrete bugs and revisions, not theoretical best practices.

---

## 1. What This Skill Is For

Building a [Slidev](https://sli.dev/) presentation deck — a Vue-based framework that turns a single Markdown file into an interactive slide show — for **academic paper-share use cases**. The original deck on which this skill was authored shared:

> *A Novel RFID Authentication Protocol Based on a Block-Order-Modulus Variable Matrix Encryption Algorithm* (IEEE TIFS, 2025)

The tone is **academic, not promotional**. See §6.

The skill applies generally to any "convert an academic paper into a 30-slide deck" task.

## 2. Expected Project Layout

This skill assumes a Slidev project with the following structure (paths used in scripts default to this layout):

```
your-slidev-project/
├── slides.md                                            ← ★ MAIN EDIT TARGET ★
├── pdf_text.txt                                         ← page-delimited PDF text (produced by extract_pdf.py)
├── components/                                          ← auto-imported Vue components
│   ├── *.vue
├── scripts/                                             ← batch helpers from this skill
│   ├── extract_pdf.py
│   ├── fix_math.py
│   ├── fix_headings.py
│   ├── fix_tables.py
│   ├── fix_anim_loop.py
│   ├── normalize_spacing.py
│   ├── academic_tone.py
│   └── replace_block.py
├── public/                                              ← static assets, e.g. /xdu.jpg
└── package.json
```

**The deck being edited is `slides.md`** at the project root. Scripts default to operating on `../slides.md` relative to the `scripts/` folder.

## 3. Common Commands

Run from inside the project root:

```bash
npm install                           # first-time setup
npm run dev                           # dev server at http://localhost:3030 with HMR
npm run build                         # static build
npm run export                        # PDF
npx slidev export --format pptx       # PPTX
```

If the dev server reports `Port 3030 is already in use`:
```bash
lsof -ti:3030 | xargs kill -9
```

## 4. Editing Workflow

1. **Read `slides.md` before editing.** Use line-anchored `Edit` calls; never blindly rewrite. Slides are separated by `---` lines, so you can locate a slide by its index (1-based, counting frontmatter as page 1).
2. **Rely on HMR.** After editing `slides.md` or any `components/*.vue`, do *not* restart Vite. HMR handles markdown, Vue SFC, and CSS changes cleanly. Only kill/restart on explicit user request or port conflict.
3. **Keep edits minimal and surgical.** Don't refactor untouched slides. Don't reformat unrelated markup.
4. **Verify visually.** When the change is significant, suggest the user reload `localhost:3030` and navigate to the affected pages. For text-only changes, no verification needed.
5. **For tone-related rewrites**, after editing run `python scripts/academic_tone.py` (or the equivalent grep):
   ```
   Grep pattern="恐怖|魔术|破局|无懈可击|完美|彻底|金贵|致命|惊人|爆炸|洗牌|掠影|！" path=slides.md
   ```
   No matches expected.

## 5. Slidev Authoring Conventions (HARD RULES)

These rules were learned from real bugs. Violating them produces broken output.

### 5.1 Math inside HTML — never use KaTeX `$…$` inside HTML tags
KaTeX `$p$` / `$$ … $$` does **not** render when nested inside `<p>`, `<div>`, `<td>`, etc. — it stays as raw `$` text on the slide.

✅ Use HTML tags + entities: `A<sup>T</sup>`, `A<sub>1</sub>`, `&times;`, `&ne;`, `(mod p)`, `det(A)`.
❌ Don't write `$A^T$` or `$$c = A \times t$$` inside `<div class="…">`.

KaTeX is fine in plain markdown paragraphs *outside* HTML blocks.

### 5.1a Rendering matrices and aligned formula lists — use CSS Grid, not `<br>` + `&nbsp;`
Stacking formulas with `<br>` and trying to align columns with `&nbsp;` always looks crooked because monospace and proportional widths drift. Use CSS Grid for **two things**:

**(a) An inline 2&times;2 / m&times;n matrix with vertical bars:**
```html
<span class="matrix">
  <span>a</span><span>b</span>
  <span>c</span><span>d</span>
</span>

<style scoped>
.matrix {
  display: inline-grid;
  grid-template-columns: repeat(2, 1.4em);
  grid-auto-rows: 1.4em;
  align-items: center;
  justify-items: center;
  padding: 0 0.5em;
  border-left: 2px solid currentColor;
  border-right: 2px solid currentColor;
  font-style: italic;
  font-size: 1.1em;
}
</style>
```
Adjust `repeat(N, …)` for an N-column matrix. The two solid bars on the sides give the visual "matrix bracket" effect without needing actual brackets.

**(b) A list of aligned formulas (e.g. `P₁ = …`, `P₂ = …`, … in two columns):**
```html
<div class="font-mono p-grid">
  <span>P<sub>1</sub> = (a+d)(e+h)</span>
  <span>P<sub>2</sub> = (c+d) · e</span>
  <span>P<sub>3</sub> = a · (f−h)</span>
  <span>P<sub>4</sub> = d · (g−e)</span>
  ...
</div>

<style scoped>
.p-grid {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 2px 12px;
}
</style>
```
Each formula sits in its own grid cell, so the `=` signs in column 1 align perfectly with the `=` signs in column 2 — no manual padding. If you have an odd number of formulas, add an empty `<span></span>` to keep the grid balanced.

**Style hygiene for inline math:**
- Use a real minus sign `−` (U+2212), not the ASCII hyphen `-`
- Use the middle dot `·` for multiplication when adjacent letters might run together (`a·e` not `ae`)
- Color the multiplication operands (e.g., `<b class="text-red-600">a·e</b>`) when you want the audience to *count* operations — turns "a wall of formulas" into a visually scannable diagram

### 5.2 Constrain overflow on long content
The slide canvas has a fixed height. Long `<Toc>` lists or tall mermaid diagrams clip or bleed off-screen.

✅ Wrap with `<div class="max-h-[300px] overflow-y-auto pr-2">`.
✅ For mermaid blocks specifically, also append `transform scale-90 origin-top` to the wrapper:
```html
<div class="mt-6 text-sm max-h-[300px] overflow-y-auto pr-2 transform scale-90 origin-top">
```

### 5.3 Mermaid container needs both top margin AND inner padding
Mermaid SVG renders flush with its container. `mt-6` alone leaves it cramped against the heading; `p-2` inside is too tight.

✅ `<div class="flex justify-center mt-6"><div class="bg-gray-100 dark:bg-gray-800 p-4 rounded-lg shadow-md w-3/4 transform scale-90 origin-top"> … mermaid … </div></div>`

### 5.4 No manual heading numbering
Slidev's TOC component auto-numbers. If you write `## 1. 研究背景`, the TOC outputs `1. 1. 研究背景`.

✅ `## 研究背景`
❌ `## 1. 研究背景`

### 5.5 HTML tables MUST wrap rows in `<tbody>`
Vue's template compiler emits `<tr> cannot be child of <table>` warnings and may cause hydration errors. Browsers auto-insert `<tbody>` at runtime, but Vue's compile-time parser does not.

✅
```html
<table>
  <tbody>
    <tr><td>…</td></tr>
  </tbody>
</table>
```
❌ `<table><tr>…</tr></table>`

### 5.6 Vertical-rhythm spacing scale
Use a consistent scale across slides; ad-hoc values (`mt-2`, `mt-4`, `mt-8`, `mt-12` mixed) look uneven.

| Role | Class |
|---|---|
| Container directly below `## H2` title | `mt-6` |
| Bottom callout/summary `<p>` after a main block | `mt-6` (or `mt-2` only when preceding block is a tall scale-90 mermaid/animation) |
| Caption text under an icon/heading inside a card | `mt-2` |
| **Avoid** | `mt-0`, `mt-8`, `mt-12` unless visually justified |

### 5.7 Vue animation components — recursive `setTimeout`, not `setInterval`
Step-by-step animations in `components/*.vue` must not use `setInterval`: it races with reset/clear timers when looping back to start, causing the first step to fire twice.

✅ Pattern:
```js
let timerId = null
const playStep = () => {
  if (activeStep.value < steps.length - 1) {
    timerId = setTimeout(() => { activeStep.value++; playStep() }, 2000)
  } else { /* end state */ }
}
onUnmounted(() => clearTimeout(timerId))
```

### 5.8 Animations are manual-play with subtle controls
The user does NOT want auto-loop animations. Both `CryptoAnim.vue` and `ProtocolAnim.vue` follow this pattern — copy it for any new animation:

- Initial state: paused at first frame (CryptoAnim) or empty (ProtocolAnim)
- Bottom-right control bar: play / pause / replay buttons + `current/total` step counter
- Visually subtle: `bg-black/20` baseline → `bg-black/50` on hover, `opacity-40` → `opacity-100` on hover, ~20px button hit areas, `w-3 h-3` SVG icons, `text-[10px]` counter
- Wrap in `backdrop-blur-sm rounded-full border border-gray-600/30` for a glass-pill look

## 6. Tone & Wording Standard (HARD RULE)

This is an **academic paper-share, not a marketing pitch**. The user explicitly required removing all promotional/emotional wording.

### Words and patterns to avoid
| Banned | Why |
|---|---|
| 恐怖、惊人、爆炸、致命、金贵 | Emotional intensity |
| 魔术、破局、洗牌、掠影 | Metaphorical / informal |
| 完美、无懈可击、彻底 | Absolutist hype |
| 巧妙、大幅、锐减、落地、危机 | Promotional verbs |
| Trailing `！` (full-width exclamation) | Tonal noise |

### Replace with
- **提出 / 引入 / 构造 / 完成更新 / 形成闭环 / 节省率达到 / 难以承载 / 显著负担**
- Neutral declarative sentences. Passive/objective voice where appropriate.

### Keep verbatim
- All numerical results: `44.44%`, `99.59%`, `99.9%`, `n=18`
- All proper nouns: `AM`, `SUEO`, `DBLTKM`, `Winograd`, `BAN`, `RFID`
- All formulas and code

### Section cover subtitles
Describe content; don't advertise. ✅ `存储与计算复杂度对比`  ❌ `惊人的存储优化率`.

### Emojis
Allowed **only as small visual icons inside cards** (❌ ⚠️ 💡 🔢 🔄 🔀 📉). Never in body prose, never as bullet decorations.

## 7. Quick Reference: Slidev Frontmatter & Layouts in This Deck

```yaml
---
theme: seriph
background: /xdu.jpg
class: 'text-center'
lineNumbers: false
transition: fade-out
css: unocss
---
```

Per-slide frontmatter (between `---` separators):
```
---
layout: center
class: text-center
---
```

`layout: center` is used for chapter cover slides. Default layout is used for content.

## 8. When Asked to Add a New Slide

1. Add `---` separator at the insertion point in `slides.md`.
2. Start with `## Title` (no manual number).
3. Wrap structured content in UnoCSS grids (`grid grid-cols-2 gap-4 mt-6`).
4. Apply §5.6 spacing.
5. Use `<sub>`/`<sup>`/HTML entities for math (§5.1).
6. If long, wrap in overflow container (§5.2).
7. Use academic tone (§6).

## 9. When Asked to Add a New Animation Component

1. Create `components/MyAnim.vue`.
2. Use `<script setup>`, recursive `setTimeout` (§5.7).
3. Add the manual-play control bar from §5.8 (copy CSS/markup from a reference component such as `CryptoAnim.vue`).
4. Reference in `slides.md` as `<MyAnim />` — auto-imported, no `import` needed.

## 10. Don't Touch (Without Explicit Request)

- `node_modules/`
- `package-lock.json`
- Anything explicitly marked as legacy in the host project.

## 11. Authoring Pipeline & Batch Helpers (`scripts/`)

A typical paper-share deck goes through this pipeline:

```
PDF source ──► extract_pdf.py  ──► pdf_text.txt  ──► (human distills) ──► slides.md
                                                                             │
                                                                             ▼
                                                                  ┌──────────────────────┐
                                                                  │  Batch fix-up loop   │
                                                                  │  (run as needed)     │
                                                                  ├──────────────────────┤
                                                                  │  fix_math.py         │  LaTeX → HTML entities
                                                                  │  fix_headings.py     │  strip manual numbers
                                                                  │  fix_tables.py       │  add <tbody>
                                                                  │  fix_anim_loop.py    │  flag setInterval
                                                                  │  normalize_spacing   │  unify mt-* values
                                                                  └──────────────────────┘
                                                                             │
                                                                             ▼
                                                                  academic_tone.py  (lint)
                                                                             │
                                                                             ▼
                                                                       npm run dev
```

### 11.1 PDF extraction

```bash
pip install pdfplumber
python scripts/extract_pdf.py path/to/paper.pdf pdf_text.txt
```

Produces a flat text file with `--- PAGE N ---` markers. Use `grep "term" pdf_text.txt` or `grep -A 5 "PAGE 7" pdf_text.txt` to cite specific paper pages while drafting slides. See `pdf_text.sample.txt` (shipped with this skill) for an example output.

If `pdfplumber` mis-orders columns or drops equations, fall back to:
```bash
pdftotext -layout source.pdf pdf_text.txt   # macOS: brew install poppler
```

### 11.2 The fix-up scripts

All scripts live under `scripts/` and operate on `slides.md` (or `components/`) by default. They are **idempotent** — safe to run multiple times.

| Script | Purpose | When to run |
|---|---|---|
| `fix_math.py` | Convert `A^T`, `\\times`, `$...$` to `<sup>T</sup>`, `&times;`, plain text | After pasting equations from the PDF |
| `fix_headings.py` | Strip `# 1.` / `## ①` prefixes that break TOC | After importing an outline |
| `fix_tables.py` | Wrap `<tr>` in `<tbody>` | After authoring raw HTML tables |
| `fix_anim_loop.py` | Detect `setInterval` in `components/*.vue` (manual rewrite hint) | After adding a new animation |
| `normalize_spacing.py` | Rewrite `mt-8`/`mt-12` → `mt-6` on grid/flex containers; warn on `mt-0` | Before review; use `--apply` to commit |
| `academic_tone.py` | Lint for promotional words; exits 1 if any found | As a pre-commit gate |
| `replace_block.py` | Swap a section delimited by two unique heading markers | When replacing a static diagram with a Vue component |

### 11.3 Quick recipes

**Replace a static mermaid diagram with a Vue component:**
```bash
python scripts/replace_block.py \
  --start "## 协议流程图 (1/2)：查询与上行认证" \
  --end   "## 协议流程图 (2/2)" \
  --replacement-file new_section.md
```

**Pre-commit sanity sweep:**
```bash
python scripts/fix_math.py && \
python scripts/fix_headings.py && \
python scripts/fix_tables.py && \
python scripts/normalize_spacing.py --apply && \
python scripts/academic_tone.py
```
A clean run prints `No changes.` for each fixer and `Tone check passed.` at the end.

### 11.4 Extending the helpers

- New banned word? Add a `(regex, reason)` tuple to `BANNED_PATTERNS` in `academic_tone.py`.
- New LaTeX construct? Add a `(pattern, replacement)` tuple to `REGEX_RULES` in `fix_math.py`.
- New spacing rule? Add a regex pair to `TARGETS` in `normalize_spacing.py`.

Keep each helper single-purpose. **Do NOT** create a "fix everything" mega-script — small composable tools are easier to reason about and debug than a monolith.

## 12. Writing the Talk Script (`talk_script.md`)

When the user asks for "a script I can read aloud" / "30 分钟报告稿" / similar, the goal is a **printable, page-by-page narration** the speaker can read verbatim while clicking through the deck. Generate it as `talk_script.md` at the project root.

### 12.1 Time-to-words math (Mandarin Chinese)

A relaxed academic delivery is **~200 Chinese characters per minute**. Multiply target minutes × 200 to get the target word budget:

| Target | Words | Notes |
|---|---|---|
| 15 min | ~3,000 | tight; cut every page to its core sentence |
| 30 min | ~6,000 | comfortable; allows examples + one digression per algorithm |
| 45 min | ~9,000 | room for Q&A asides and live equation walk-throughs |

Always tally roughly per section as you draft so the total lands within ±10% of the budget.

### 12.2 Per-slide budget

Distribute time roughly proportional to information density:

| Slide kind | Time | Words |
|---|---|---|
| Cover slide | 1 min | ~200 |
| Section divider (`layout: center`) | 15–20 sec | ~50 |
| Background / motivation page | 1.5–2 min | ~350 |
| Algorithm explanation (the meat) | 2–2.5 min | ~450–500 |
| Protocol step diagram | 2 min | ~400 |
| Performance / results page | 1.5–2 min | ~350 |
| Conclusion page | 2 min | ~400 |
| Thank-you / Q&A page | 30 sec | ~80 |

### 12.3 Voice and register — read-aloud style

- **First-person plural inclusive**: "我们先看…", "我们再回到主线". Pulls the audience along; reads naturally aloud.
- **Imperative pointers**: "看页面左边的红框", "数一下绿色加粗的乘号" — explicit references to what's on screen so the speaker isn't blindly reciting and the audience knows where to look.
- **Demonstrative resolution**: "这个数字", "这一段", "这条性质" — connect successive sentences instead of repeating nouns. Repeating "AM 算法" three times in two sentences sounds robotic.
- **Conversational connectives**: "那么…", "其实…", "也就是说…", "那退而求其次…", "OK，回到主线". These are the verbal hinges of natural Chinese speech.
- **Avoid written-only grammar**: drop "之", "其", "故", "亦", "诸如" — they don't sound right out loud. Replace with "的", "它", "所以", "也", "比如".
- **No long compound sentences**: cap at ~25 characters per breath. Break with "，" or full stop. If a sentence runs longer than two lines on screen, split it.

### 12.4 Per-page structure pattern

Each page in the script should follow this rhythm:

1. **One-line topic statement** — what this slide is about, in plain words.
2. **Walk-through of the visual** — explicitly map narration to layout: "页面分成左右两栏…", "上面这个公式…".
3. **Concrete example or number** — the audience remembers numbers, not abstractions. ("99.59%", "n=18", "8 次乘法 → 7 次乘法").
4. **Why-it-matters tag** — connect back to the bigger story before the page-turn cue.
5. **Page-turn cue** — `【翻页】` (or whatever symbol). Always end the page with one.

Avoid summarizing the whole slide twice (once at the start, once at the end). Pick one place.

### 12.5 Markup conventions for the script file

```markdown
## 第 N 页 · <slide title>（约 X 分钟）

<narration in plain prose paragraphs>

`【翻页】`
```

Use the literal page numbers from the rendered Slidev deck (cover = page 1, section dividers count). This lets the speaker glance at the side display and cross-reference instantly.

Other useful markers in the body:
- `（停顿）` — explicit micro-pause, useful before a punchline number or after a complex equation.
- `【可省略】` … `【/可省略】` — wrap optional asides that can be cut if running over time.
- `> 备注：…` — a sentence that's notes-only and should NOT be read aloud (e.g., "this is the page where you click the play button").

### 12.6 Handle hard pages explicitly

Some pages are harder to narrate than others. Plan for them:

- **Long equation pages** (e.g., the `S_traditional` formula): do NOT read every term. Instead say "我们看它的形式：里面有一项是 X，再加上一项 Y，关键是它**关于 N 是阶乘求和**" — describe the *shape* of the equation, not the symbols.
- **Animation pages** (`<CryptoAnim />`, `<ProtocolAnim />`): tell the speaker to click play and narrate over the animation. Reference the steps by number, not by reading every label.
- **BAN logic / formal proof pages**: do NOT read the symbol soup aloud. Say "推理过程的具体符号大家可以课后看，要点是…" and summarize the conclusion. Save 60+ seconds.
- **Mermaid sequence diagrams**: walk through steps in order, but at most one sentence per step. Don't get stuck.

### 12.7 Closing the talk

The last content page (the conclusions slide) deserves a structured close:

1. Restate the 3 contributions in one sentence each — mirrors what's on the slide.
2. **One personal evaluation sentence** — the audience wants to know what *you* think, not just what the paper says. ("我个人的评价是…", "这篇论文的价值不在于发明了新工具，而在于把已有的工具组合得很恰当").
3. End with "我的分享到这里" or equivalent — clear handoff to Q&A.

Don't put all of these on the thank-you slide. The thank-you slide gets ~30 seconds: thank, invite questions, sit down.

### 12.8 Self-check before delivering the script

- [ ] Total word count within ±10% of the target?
- [ ] Every page ends with `【翻页】`?
- [ ] No `$...$` LaTeX in narration (the speaker can't pronounce those — write `A 的 T 次方` or `A 转置`)?
- [ ] Every reference to a slide element (左边、绿色框、第三行) actually exists on that page?
- [ ] No "perfect/incredible/amazing" hype words leaked from the academic-tone rule (§6)?
- [ ] A bottom note section listing time-cutting options if Q&A overruns?

A good script reads like it was written *by* the speaker, not *for* an actor. When in doubt, read a paragraph aloud yourself — if it sounds like a press release, rewrite.

---

**You are now ready to edit `slides.md`. Read the relevant slide section, apply the conventions above, and use HMR to ship changes incrementally.**
