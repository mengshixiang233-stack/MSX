# V11 Layout Constants

These constants were reverse-extracted from `build_nature_paper2ppt.py` and verified against `final_presentation_cn_v11_evidence_chain.pptx`.

## Canvas And Grid

| Item | Value |
|---|---:|
| Slide size | 16:9 widescreen |
| Width | `13.333333 in` |
| Height | `7.5 in` |
| Sidebar width | `1.46 in` |
| Main left x | `1.76 in` |
| Main right x | `12.93 in` |
| Main content width | `11.17 in` |
| Body top | `1.42 in` |
| Title y | `0.32 in` |
| Title height | `0.42 in` |
| Title divider y | `0.89 in` |
| Subtitle y | `0.95 in` |
| Page number | bottom-right, near `x=12.55, y=7.16` |

Main body content should start no higher than `1.42 in`, except intentionally designed section/cover elements. This prevents collision with the subtitle area.

## Colors

| Token | RGB | Hex | Use |
|---|---|---|---|
| `NAVY` | `08,35,78` | `#083578` | title, active sidebar, label bars, key lines |
| `BLUE` | `16,6A,B7` | `#166AB7` | secondary accent |
| `PANEL` | `FF,FF,FF` | `#FFFFFF` | figure/content panel fill |
| `LINE` | `B8,C7,DB` | `#B8C7DB` | frame line |
| `TEXT` | `15,25,3A` | `#15253A` | main body text |
| `MUTED` | `64,72,83` | `#647283` | source/caption |
| `TAKEAWAY_FILL` | `F4,F8,FD` | `#F4F8FD` | bottom takeaway bar |
| `SLIDE_BG` | `FB,FD,FF` | `#FBFDFF` | page background |
| `SIDEBAR_BG` | `F1,F5,FA` | `#F1F5FA` | sidebar background |

## Typography

| Region | Font | Size | Weight | Line spacing |
|---|---|---:|---|---:|
| Main title | Microsoft YaHei | 27 pt | bold | 1.3 |
| Subtitle | Microsoft YaHei | 13.5 pt | regular | 1.3 |
| Sidebar item | Microsoft YaHei | 15.2 pt | regular | 1.3 |
| Right-side bullet | Microsoft YaHei | 18 pt | regular | ~1.25-1.3 |
| Bottom takeaway | Microsoft YaHei | 18 pt | regular | 1.3 |
| Figure label bar | Microsoft YaHei | 8.8 pt | regular | 1.3 |
| Source | Microsoft YaHei | 7.5 pt | regular | 1.3 |
| Timeline card | Microsoft YaHei | 8.2-9.6 pt | regular | ~1.08 |

Do not bold explanatory text outside titles unless a specific local design reason exists.

## Sidebar

Sections are fixed:

1. 研究背景
2. 科学问题
3. 技术路线
4. 核心结果
5. 创新意义

Active section uses a full-width navy rectangle. Inactive sections use navy text on pale background with thin divider lines. Do not include `机制整合` as a separate sidebar item.

## Right Evidence Rail

| Item | Value |
|---|---:|
| x | `8.55 in` |
| y | `1.46 in` |
| width | `4.25 in` |
| normal height | `4.35 in` |
| bullet size | `18 pt` |
| bullet style | native PPT large round bullet, char `●` |
| bullet text prefix | one leading space after bullet |

No blue mini-title or horizontal rule above the right bullets. Do not use hand-typed `·`.

## Figure Frames And Labels

| Item | Value |
|---|---:|
| Frame shape | rounded rectangle |
| Frame fill | white |
| Frame line | `#B8C7DB`, about `0.75 pt` |
| Actual corner radius | `0.06 in` |
| Inner padding | `0.06 in` |
| Label bar height | `0.28 in` |
| Label bar width | `min(frame width, 2.55 in)` |
| Label bar fill | `#083578` |
| Label text inset | x `+0.07`, y `+0.04` |

Blue label bars align exactly with the image frame top-left. Frames in a group should share y/x grid lines whenever possible.

## Bottom Takeaway

| Item | Value |
|---|---:|
| x | `LEFT - 0.08 = 1.68 in` |
| y | usually `6.36 in` |
| width | about `11.03 in` |
| height | `0.56 in` |
| font | Microsoft YaHei 18 pt |
| alignment | center, vertically middle |
| corner radius | `0.06 in` |

Do not allow source labels, pictures, or body content to overlap the takeaway bar.

## Common Result-Page Geometry

Default result page:

- Left evidence area: `x=1.76`, `y=1.42`, `w≈6.58`, `h≈4.58`
- Right rail: `x=8.55`, `y=1.46`, `w=4.25`, `h=4.35`
- Source: bottom-left above takeaway, typically y `6.00-6.17`, size `7.5 pt`

Mechanism synthesis page:

- Figure can expand beyond normal left evidence area.
- V11 used central mechanism figure around `x=1.96`, `y=1.32`, `w=10.78`, `h=4.55`; inserted picture itself was about `7.87 x 4.43 in`.
- Ordinary right bullet rail may be removed.
- Add mechanism-chain chips near y `5.72`.

Outcome/timeline page:

- Replace dense tables with a horizontal timeline.
- Use alternating small rounded cards with year, mechanism node, and contribution claim.
