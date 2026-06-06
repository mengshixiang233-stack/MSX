# MSX research ppt

A Codex skill for building and revising high-level Chinese scientific defense PPT/PPTX decks.

This skill was reverse-extracted from the v11 tooth-loss cognition evidence-chain deck and preserves its narrative structure, layout constants, figure hierarchy, copywriting rules, and QA checks.

## When to use

Use this skill for:

- 科技奖答辩 PPT
- 科研答辩 PPT
- 医学科研结果汇报 PPT
- 机制研究 PPT
- 基金、课题、项目汇报 PPT

## Codex invocation

After installing the skill into `$CODEX_HOME/skills`, call it with:

```text
Use $msx-research-ppt to create/revise this research defense PPT.
```

Chinese example:

```text
调用 $msx-research-ppt，基于我的 docx 和实验图，制作 20 页左右中文科研答辩 PPT，保持 v11 evidence-chain 版式和 QA 标准。
```

## Package structure

```text
SKILL.md
agents/openai.yaml
examples/page-example.md
references/
  copywriting-style.md
  figure-hierarchy-and-cropping.md
  page-types-and-narrative.md
  qa-standard.md
  v11-layout-constants.md
scripts/
  audit_pptx.py
  extract_deck_profile.py
  v11_reference_builder.py
```

## Core workflow

1. Read project materials and classify each slide as background, problem, route, result, mechanism synthesis, output, or innovation.
2. Build a page plan before generation unless the user waives confirmation.
3. For result slides, prioritize one core finding and one dominant evidence figure.
4. Use v11 layout constants: flat left sidebar, Microsoft YaHei, 18 pt right bullets, 18 pt bottom takeaway, consistent rounded image frames.
5. Run `scripts/audit_pptx.py` and produce `qa_report.md` after generation.

## License

MIT License.
