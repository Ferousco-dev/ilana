# LOGO PROMPTS

Ready to paste into an image generator. Concept A is the recommended one.
Palette and rules: `BRAND.md`.

---

## A. The Gate Sequence  (recommended)

> Flat vector logo mark, perfectly square, transparent background. A sequence of five nested
> pointed-arch gateways receding into depth, viewed straight on, like looking down a colonnade.
> Each arch is a clean geometric outline of even stroke weight. The outermost arch is deep forest
> green #064A35, and each successive arch is a lighter green, ending on bright palm green #2FBF71
> at the innermost. The innermost arch is filled solid with warm ochre #E8A33D, glowing like a
> doorway with light behind it. The vertical posts of each arch carry a subtle repeating notched
> pattern inspired by carved Yoruba house posts and adire indigo cloth geometry: small triangles
> and horizontal bars, no more than three notches per post. Strictly symmetrical about the vertical
> axis. Minimal, confident, architectural. No text, no letters, no gradient meshes, no drop shadows,
> no 3D bevel, no glow effects. Bold enough to remain legible at 24 pixels. Style of a modern
> open-source project logo, in the tradition of Adinkra and adire geometry rather than Silicon
> Valley tech iconography.

**Negative prompt:** `text, letters, words, watermark, gear, cog, circuit board, robot, brain, chip, 3D render, photorealistic, glossy, bevel, drop shadow, neon, purple, teal gradient, busy detail, gradient mesh`

---

## B. The Opon Ifá Cycle

> Flat vector logo mark, perfectly square, transparent background. A bold circular ring in deep
> green #0B6E4F whose outer edge carries a carved geometric border of alternating triangles and
> short bars, evoking the incised rim of a Yoruba Opon Ifá divination tray. Inside the ring, four
> thick arrows chase each other clockwise, forming a continuous closed loop with clean mitred
> corners, in bright palm green #2FBF71. Exactly one of the four arrows is warm ochre #E8A33D. At
> the centre of the loop, a small solid square in adire indigo #1E2A4A. Everything strictly
> geometric, even stroke weight, four-fold rotational symmetry apart from the single ochre arrow.
> Minimal, ceremonial, precise. No text, no letters, no 3D, no shadows, no gradients. Legible at 24
> pixels. Open-source project logo aesthetic grounded in West African geometric craft.

**Negative prompt:** `text, letters, watermark, recycling symbol, yin yang, gear, circuit, 3D, glossy, shadow, neon, purple, photorealistic, cluttered`

---

## C. The Spine

> Flat vector logo mark, perfectly square, transparent background. A single bold vertical bar in
> deep green #0B6E4F running the full height, like a woven aso-oke cloth strip, with a fine
> repeating horizontal weave texture of thin lighter-green lines across it. Nine small solid
> squares sit along the bar at even intervals, alternating left and right of it, connected by short
> horizontal stems: eight of them bright palm green #2FBF71, and the fourth from the top in warm
> ochre #E8A33D. The whole reads simultaneously as a woven strip, a process timeline with nine
> checkpoints, and the vertical stroke of a letter. Strictly geometric, even stroke weight,
> generous negative space. Minimal and structural. No text, no letters, no 3D, no shadows, no
> glow. Legible at 24 pixels. Modern open-source logo grounded in West African textile geometry.

**Negative prompt:** `text, letters, watermark, DNA helix, ladder, barcode, circuit board, 3D, glossy, shadow, neon, purple, photorealistic`

---

## Banner (after you pick a mark)

> Wide banner image, 1280 by 400 pixels, deep forest green background #064A35. Centred, a single
> flat vector logo mark [describe the mark you chose] in bright palm green with one warm ochre
> accent. Behind it, very faint large-scale adire indigo geometric pattern at about 8 percent
> opacity: repeating triangles and grid lines, subtle enough to read as texture rather than
> pattern. Wide empty margins. No text. Calm, architectural, confident.

---

## Tuning notes

- **Generate the square mark first**, in isolation, before any banner or wordmark. A mark that
  works alone can be placed anywhere; one designed inside a banner rarely survives extraction.
- **Ask for four variations**, then judge each one shrunk to 24 pixels. That single test kills most
  candidates and is the only one that matters for a favicon.
- **If the output is too busy**, add: *"reduce to the fewest possible shapes, maximum simplicity,
  three colours only"*. Generators consistently over-decorate.
- **If the green looks like generic tech green**, add: *"warm, earthy green, not neon, not mint,
  not emerald"* and raise the ochre presence.
- **Do not let it generate the wordmark.** Diacritics (Ì, à) are reliably mangled. Set the wordmark
  in real type afterwards.
- **Ideogram and Recraft** handle flat vector logo work better than photoreal-tuned models. Recraft
  can export actual SVG.
