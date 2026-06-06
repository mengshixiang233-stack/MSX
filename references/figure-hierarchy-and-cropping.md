# Figure Hierarchy And Cropping

Result slides are evidence pages, not image galleries.

## Evidence Hierarchy

Each result slide should contain:

1. One dominant visual evidence block.
2. Optional one or two smaller insets only if they sharpen the claim.
3. Right-side evidence bullets mapped to the dominant visual/insets.
4. A bottom takeaway that states the mechanism role of the evidence.

Do not preserve every panel when doing so makes the figure unreadable.

## Main Figure Rules

- The main evidence should usually occupy 55-75% of the usable visual area.
- Axis labels, group names, trends, representative images, and significance marks should be readable at presentation distance.
- If the full figure is too dense, crop to the panels that prove the slide’s core finding.
- Preserve scientific context: do not crop away required axes, group labels, legends, or significance bars.
- Original experimental data must not be redrawn unless values are explicitly available and the user approves recreation.

## Secondary Evidence

Secondary figures may be:

- a small inset,
- a cropped panel,
- a note/source/backup item,
- or omitted from the main slide and described in speaker notes.

Use secondary evidence only when it makes the main claim more trustworthy. Do not add it to fill space.

## Backup Page Decisions

Move a figure/panel to backup or notes when:

- it repeats evidence already shown,
- it becomes too small after placement,
- its labels/significance cannot be read,
- it distracts from the main finding,
- or it only verifies an experimental premise.

V11 examples:

- General-state/body-weight evidence was not displayed as equal-weight evidence on the main MWM result slide.
- Behavior panels were not repeated on the p38/NF-κB molecular slide.
- Dense HT22 figure was cropped to the functional/ROS evidence.
- Juvenile MWM was cropped to platform-statistics evidence and used as an inset.

## Crop Manifest

Every crop should be recorded in `asset_manifest.md`:

| Field | Meaning |
|---|---|
| slide | destination slide |
| asset label | what the crop shows |
| copied file | local crop path |
| role / quality note | source panel and why it was cropped |

## Contact Sheet

Generate a contact sheet of selected/cropped figures before final deck delivery. Use it to catch:

- wrong crop,
- missing panel labels,
- unreadable text,
- blank images,
- duplicated assets,
- excessive whitespace.
