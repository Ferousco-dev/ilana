# BRAND

Visual identity for Ìlànà. Kept in the repository so contributors have one source of truth and
nobody re-invents the palette in a slide deck.

---

## The idea

Ìlànà means *process, method, the disciplined way a thing is done*. The mark should read as
**ordered passage**: something moving forward through stages that each have a threshold. Not a
gear, not a circuit board, not a robot. Those say "software". Ìlànà is about **discipline**, which
is older than software.

Two visual traditions to draw from, both Yoruba, both from the region the course is taught in:

- **Opon Ifá**, the divination tray: a circle with a carved geometric border, read as a structured
  field of knowledge.
- **Adire**, indigo resist-dyed cloth: repeating geometric grids, hand-drawn but rigorously
  ordered. Discipline expressed as pattern.

Plus the structural idea from the skill itself: **nine gates in sequence**.

---

## Palette

| Role | Name | Hex | Use |
| --- | --- | --- | --- |
| Primary | Ife Green | `#0B6E4F` | the mark, dark surfaces |
| Bright | Palm | `#2FBF71` | accents, active states, light-theme highlight |
| Deep | Forest | `#064A35` | shadow, depth in the gate sequence |
| Accent | Ochre | `#E8A33D` | the single highlighted element (the gate you are at) |
| Ink | Adire Indigo | `#1E2A4A` | text on light, alternate mark |
| Ground | Raffia | `#F4EDE2` | light background |
| Contrast | Terracotta | `#C1542D` | failure states, gate FAIL, sparingly |

**Ratio: roughly 70% green family, 20% ink, 10% ochre.** The ochre is the whole trick. One warm
element against a green field reads as African rather than generic tech-green, and it gives the eye
somewhere to land.

Avoid: teal-to-purple gradients, neon, glassmorphism, drop shadows, anything that looks like a
2021 SaaS logo.

---

## Files this repository expects

Drop generated assets here with these exact names and the README wires up automatically.

| File | Size | Background | Used in |
| --- | --- | --- | --- |
| `logo.svg` | vector | transparent | preferred everywhere |
| `logo.png` | 1024 x 1024 | transparent | fallback |
| `logo-dark.png` | 1024 x 1024 | transparent, lightened mark | GitHub dark theme |
| `banner.png` | 1280 x 400 | Ife Green or Raffia | README hero |
| `icon.png` | 512 x 512 | transparent | favicon, social preview |
| `social-preview.png` | 1280 x 640 | Ife Green | GitHub Open Graph card |

---

## Rules

1. **Legible at 24 pixels.** If the detail disappears in the favicon, the detail is decoration.
   Test it before committing.
2. **Works on both GitHub themes.** Either the mark survives on `#0d1117` and `#ffffff`, or ship
   `logo.svg` plus `logo-dark.png` and use a `<picture>` element.
3. **No text inside the mark.** The wordmark is separate, so the symbol can stand alone.
4. **Flat vector.** No gradients beyond a single two-stop, no bevels, no glow.
5. **The diacritic matters.** It is Ìlànà, with the grave accents. If a wordmark drops them it is
   spelling a different word.

## Typography

| Use | Face | Fallback |
| --- | --- | --- |
| Wordmark | a humanist sans with real diacritic support | Inter, Source Sans 3 |
| Body | system stack | |
| Code and gate output | a mono with clear `0`/`O` | JetBrains Mono, IBM Plex Mono |
