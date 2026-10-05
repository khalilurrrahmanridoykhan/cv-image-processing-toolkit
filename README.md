# CV Image Processing Toolkit

A classical computer-vision toolkit built with OpenCV: read images, detect edges,
extract contours, and classify geometric shapes (circle, triangle, square, rectangle,
pentagon, polygon).

## Status

Early scaffold. No pipeline code yet — see the plan for the full step-by-step build.

## Why classical CV first

No deep learning, no training loop. The goal is fluency with the pipeline that every
later, fancier CV project depends on: image I/O → preprocessing → edge detection →
contour extraction → shape classification.

## Pipeline

1. **Read & preprocess** — load an image, convert color spaces, denoise/blur.
2. **Detect edges** — Sobel and Canny.
3. **Extract contours** — turn edges into closed object outlines (`cv2.findContours`).
4. **Identify shapes** — classify each contour by its geometry.

## Repo layout

```
toolkit/        # the library: io, preprocess, edges, contours, shapes, cli
tests/          # synthetic-shape accuracy test + end-to-end smoke test
notebooks/      # step-by-step visual walkthrough
data/synthetic/ # generated shapes with known ground truth
data/real/      # real photos (coins, boxes, signs, paper)
```

## Install (development)

```bash
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
```

## License

Apache License 2.0 — see [LICENSE](LICENSE).
