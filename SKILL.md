---
name: msx-research-ppt
description: Generate or revise Chinese high-level scientific defense PPT/PPTX decks from科研项目 docx, experimental images, papers, old PPTs, or award/fund/report materials using the v11 evidence-chain narrative, layout constants, figure hierarchy, and QA standard reverse-extracted from the tooth-loss cognition deck. Use for 科技奖答辩PPT, 科研答辩PPT, 医学科研结果PPT, 机制研究PPT, 基金/课题汇报PPT, or when the user asks for a high-level academic defense deck rather than ordinary slide polishing.
---

# MSX research ppt

Use this skill to create or revise a **high-level Chinese scientific defense PPT**, not a generic presentation. The default output is a real `.pptx` deck with evidence-led slide structure, readable figures, and an explicit QA report.

This skill is based on the final v11 deck standard reverse-extracted from:

- `final_presentation_cn_v11_evidence_chain.pptx`
- `build_nature_paper2ppt.py`
- `qa_report.md`

When reproducing the style, do not invent a new visual system. Load the relevant references below and follow the constants and QA rules unless the user explicitly changes them.

## When To Use

Use when the user provides科研项目材料 and asks for:

- 中文科研答辩 PPT / 科技奖答辩 PPT / 医学科研结果 PPT
- 机制研究 PPT / 基金或课题汇报 PPT
- from docx, PDF, paper figures, old PPT, experimental images, image folders, tables, or manuscript text
- a deck organized by “科学问题—技术路线—核心结果—机制整合—创新意义”
- v11 证据链版, evidence-chain, 高水平学术汇报, or similar wording

Do not use this skill for marketing decks, casual courseware, poster design, or text-only polishing that does not require PPT generation/revision.

## Required Workflow

1. **Parse Inputs**
   - Read the docx/PDF/text/old PPT/image folders.
   - Extract: project title, background, scientific question, hypothesis, route, models, indicators, results, mechanism chain, innovation, future directions, available figures and figure meanings.
   - If an old deck or reference deck exists, inspect it with `scripts/extract_deck_profile.py` before designing.

2. **Build The Defense Narrative**
   - Default structure: cover, research background, existing evidence/gap, scientific question, route/design, core results, mechanism synthesis, paper/output support, innovation/future direction.
   - For mechanism projects, core-result slides must advance along a mechanism chain instead of listing results evenly.

3. **Classify Every Page**
   - Use one of: cover, background, problem, route, result, mechanism synthesis, output/achievement, innovation.
   - Page type determines title style, figure hierarchy, bottom takeaway function, and whether a right-side evidence rail is appropriate.

4. **Plan Before Writing PPT**
   - Before generating or refilling a deck, output a slide-by-slide plan and wait for user confirmation unless the user has explicitly waived confirmation.
   - Each planned slide must include: page number, page type, mechanism-chain position, suggested title, core finding, main evidence figure, secondary evidence/inset/backup decision, right-side bullets, bottom takeaway, crop/zoom needs, layout risks.

5. **Core Results Rule**
   - Each result slide must have **one core finding + one set of key evidence + one mechanism-chain position**.
   - Do not average-place all figures.
   - Main evidence must be large enough to read at presentation distance.
   - Dense or unreadable figures must be cropped, enlarged, split, or moved to backup/notes.

6. **Generate Or Refill PPT**
   - Prefer `python-pptx` for deterministic PPTX generation.
   - Use the v11 constants in `references/v11-layout-constants.md`.
   - Use the scripts in `scripts/` for profile extraction, crop/contact-sheet generation, and QA.

7. **Run QA And Revise**
   - Always produce a QA report.
   - QA must include package integrity, slide/media/notes count, bounds, overlap, source overlap, right-rail consistency, bullet style/spacing, takeaway font, rounded-corner radius, label alignment, and small-picture warnings.
   - Do not deliver a first draft with known high-severity defects.

## References To Load

- For extracted coordinates, colors, typography, slide dimensions, right rail, frame radius, sidebar, labels, and timeline: `references/v11-layout-constants.md`
- For narrative structure, page types, and mechanism-chain sequence: `references/page-types-and-narrative.md`
- For title/bullet/takeaway wording rules and examples: `references/copywriting-style.md`
- For figure selection, crop, inset, and backup decisions: `references/figure-hierarchy-and-cropping.md`
- For required QA checks and acceptable thresholds: `references/qa-standard.md`
- For a concrete page-level transformation example: `examples/page-example.md`

## Bundled Scripts

- `scripts/v11_reference_builder.py`: exact reference builder copied from the successful v11 tooth-loss cognition deck. Use as a reproducibility baseline and pattern source, not as a blind template for unrelated projects.
- `scripts/extract_deck_profile.py`: inspect a PPTX and emit slide size, text boxes, pictures, right rails, rounded rectangles, label bars, and fonts.
- `scripts/audit_pptx.py`: run object-level QA on a generated deck and write JSON/Markdown findings.

## Output Package

Create a minimal output package:

- `output/final_presentation_cn.pptx` or a user-specific filename
- `output/qa_report.md`
- `output/asset_manifest.md` when figures are extracted/cropped
- `output/assets/figures/` with selected/cropped figures
- optional `output/ppt_outline_cn.md` when helpful for traceability

## Non-Negotiables

- The deck is evidence-led; it is not a decorative template.
- Result slides do not average-display all data.
- Titles combine research content and key finding.
- Right-side bullets correspond to visible evidence and use native large round bullets.
- Bottom takeaways are full scientific sentences, not labels or repeated templates.
- Figures must be readable; crop or split rather than shrink.
- Sidebar, right rail, frame radius, label bars, page numbers, and takeaway bar remain consistent.
- Always run QA and report remaining limitations.
