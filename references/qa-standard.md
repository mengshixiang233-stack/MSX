# QA Standard

Every generated deck must include `qa_report.md`.

## Required Checks

Package:

- PPTX zip integrity: `testzip() == None`
- target slide count correct
- embedded media count reasonable
- notes slides preserved when notes are generated
- no placeholder tokens (`lorem`, `undefined`, `nan`, `xxxx`)

Geometry:

- shape outside slide bounds: 0
- source text overlaps pictures: 0
- body content does not collide with subtitle area
- bottom takeaway does not overlap body/source/pictures
- right rail x/width consistent across result pages
- left sidebar position consistent
- label bars align to image frame top-left
- all image/content rounded frames use actual corner radius `0.06 in`

Text:

- right bullets use native large round bullet `●`
- hand-typed `·` bullet count: 0
- bullet run starts with one leading space
- right-bullet font: Microsoft YaHei 18 pt
- bottom takeaway font: Microsoft YaHei 18 pt
- manual lines of only 1-3 Chinese characters should be 0 except intentional labels/table headers
- page titles should not be generic section labels
- takeaways should not be repeated templates

Figures:

- no result-slide picture under readability threshold unless it is a deliberate icon/label
- source labels do not overlap images
- main evidence figure is visually dominant
- dense figures are cropped/split/moved to backup
- axis labels, group names, trends, and significance markers are preserved where relevant

## Scripts

Use `scripts/audit_pptx.py` after generation:

```bash
python scripts/audit_pptx.py path/to/deck.pptx --json output/qa_audit.json --markdown output/qa_report.md
```

Use `scripts/extract_deck_profile.py` to inspect an old/reference deck:

```bash
python scripts/extract_deck_profile.py path/to/deck.pptx --json output/deck_profile.json
```

## Known Limitations

Object-level QA cannot replace a full rendered preview when Office/LibreOffice is unavailable. If a reliable renderer exists, additionally export slide previews and visually inspect at slide-sorter scale.
