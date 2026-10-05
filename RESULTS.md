# Results

Findings logged as each step is completed — not written retroactively, so numbers and
threshold values here reflect what was actually observed, not guessed.

## Step 1 — I/O + synthetic dataset

30 synthetic images generated (`data/synthetic/generate.py`), 6 each of circle,
triangle, square, pentagon, rectangle, with exact ground truth in
`data/synthetic/ground_truth.json`. 4 real photos sourced from Wikimedia Commons
(CC0/public domain, see `data/real/SOURCES.md`): `coins.jpg`, `stop_sign.jpg`,
`dice.jpg`, `book.jpg`.

## Step 2 — Preprocess

`blur()` + `threshold_otsu()` tested on two real photos:

- `book.jpg` — clean result: solid white book silhouette on solid black background,
  wood-grain texture fully suppressed. One minor artifact: a thin jagged streak along
  part of the left edge, from the book's own cast shadow on the table — real shadow,
  not noise.
- `coins.jpg` — a genuine limitation surfaced here: the coins' reflective ridges
  alternate bright/dark, so one global Otsu threshold can't binarize them into a solid
  shape — each stack comes out zebra-striped instead. Background is still correctly
  separated; the object's own surface just isn't uniform enough for a single global
  threshold. Not a bug — a real constraint of global Otsu thresholding on
  textured/reflective surfaces.

## Step 3 — Edge detection (Sobel vs Canny)

Canny's two thresholds (`low`, `high`) do **not** generalize across photos — confirmed
by testing the same pair on all 4 real photos plus one synthetic shape:

| Image | `low=50, high=150` (default) | Best found |
| :--- | :--- | :--- |
| `pentagon_020.png` (synthetic) | Clean, fully closed outline | same — no tuning needed on clean synthetic input |
| `book.jpg` | Book outline clean, but heavy noise from wood-grain texture on the left | `(200, 300)` — fully suppresses the noise, outline stays closed |
| `stop_sign.jpg` | — | `(200, 300)` — clean octagon outline, sign text shows as extra internal edges (expected) |
| `dice.jpg` | — | `(200, 300)` — clean hexagonal silhouette (cube viewed at an angle — not a square, see `data/real/SOURCES.md`) |
| `coins.jpg` | — | `(200, 300)` **loses most of the real object edges** — this photo's gradient magnitudes sit on a different scale than the other three, so the same absolute thresholds that work elsewhere under-detect here |

**Takeaway:** a single fixed `(low, high)` pair is not photo-independent — it depends on
that image's own gradient/contrast statistics, not just whether the subject is "clean"
or "noisy." `(200, 300)` is a good default for 3 of the 4 real photos here, but not
for `coins.jpg`. A per-image automatic threshold (e.g. derive `high` from that image's
own Otsu threshold, `low = 0.5 * high`) would be the robust fix — logged as a stretch
goal rather than implemented now, to keep Step 3 scoped to Sobel vs Canny fluency, not
automatic threshold selection.
