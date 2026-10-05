"""Generates the synthetic shape dataset with known ground truth.

Run from the repo root: python3 data/synthetic/generate.py
Writes PNGs to data/synthetic/images/ and labels to data/synthetic/ground_truth.json.
"""
import json
import math
import random
from pathlib import Path

import cv2
import numpy as np

OUT_DIR = Path(__file__).parent / "images"
CANVAS_SIZE = 200
SHAPE_COLOR = (40, 40, 40)   # BGR, near-black
BG_COLOR = (255, 255, 255)  # BGR, white

random.seed(42)


def _rotated_regular_polygon(center, radius, n_sides, rotation_deg):
    cx, cy = center
    angle0 = math.radians(rotation_deg - 90)  # -90 so n=3 points "up" at rotation 0
    pts = []
    for i in range(n_sides):
        theta = angle0 + 2 * math.pi * i / n_sides
        x = cx + radius * math.cos(theta)
        y = cy + radius * math.sin(theta)
        pts.append([x, y])
    return np.array(pts, dtype=np.int32)


def _rotated_rectangle(center, width, height, rotation_deg):
    cx, cy = center
    corners = np.array(
        [[-width / 2, -height / 2], [width / 2, -height / 2],
         [width / 2, height / 2], [-width / 2, height / 2]]
    )
    theta = math.radians(rotation_deg)
    rot = np.array([[math.cos(theta), -math.sin(theta)],
                     [math.sin(theta), math.cos(theta)]])
    pts = corners @ rot.T + np.array([cx, cy])
    return pts.astype(np.int32)


def _random_center(margin):
    lo, hi = margin, CANVAS_SIZE - margin
    return random.randint(lo, hi), random.randint(lo, hi)


def make_circle():
    radius = random.randint(25, 45)
    center = _random_center(radius + 5)
    canvas = np.full((CANVAS_SIZE, CANVAS_SIZE, 3), BG_COLOR, dtype=np.uint8)
    cv2.circle(canvas, center, radius, SHAPE_COLOR, -1)
    return canvas, {"shape": "circle", "center": list(center), "size": radius, "rotation_deg": 0}


def make_regular_polygon(n_sides, shape_name):
    radius = random.randint(30, 50)
    rotation = random.randint(0, 359)
    center = _random_center(radius + 5)
    canvas = np.full((CANVAS_SIZE, CANVAS_SIZE, 3), BG_COLOR, dtype=np.uint8)
    pts = _rotated_regular_polygon(center, radius, n_sides, rotation)
    cv2.fillPoly(canvas, [pts], SHAPE_COLOR)
    return canvas, {"shape": shape_name, "center": list(center), "size": radius, "rotation_deg": rotation}


def make_rectangle():
    width = random.randint(50, 80)
    height = random.randint(25, 45)  # kept != width so it's never square
    rotation = random.randint(0, 359)
    half_diag = int(math.hypot(width, height) / 2)
    center = _random_center(half_diag + 5)
    canvas = np.full((CANVAS_SIZE, CANVAS_SIZE, 3), BG_COLOR, dtype=np.uint8)
    pts = _rotated_rectangle(center, width, height, rotation)
    cv2.fillPoly(canvas, [pts], SHAPE_COLOR)
    return canvas, {"shape": "rectangle", "center": list(center), "size": [width, height], "rotation_deg": rotation}


GENERATORS = {
    "circle": lambda: make_circle(),
    "triangle": lambda: make_regular_polygon(3, "triangle"),
    "square": lambda: make_regular_polygon(4, "square"),
    "pentagon": lambda: make_regular_polygon(5, "pentagon"),
    "rectangle": lambda: make_rectangle(),
}
VARIANTS_PER_SHAPE = 6


def main():
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    ground_truth = []
    idx = 0
    for shape_name, gen in GENERATORS.items():
        for _ in range(VARIANTS_PER_SHAPE):
            canvas, label = gen()
            filename = f"{shape_name}_{idx:03d}.png"
            cv2.imwrite(str(OUT_DIR / filename), canvas)
            label["filename"] = filename
            ground_truth.append(label)
            idx += 1

    gt_path = Path(__file__).parent / "ground_truth.json"
    gt_path.write_text(json.dumps(ground_truth, indent=2))
    print(f"Wrote {idx} images to {OUT_DIR} and ground truth to {gt_path}")


if __name__ == "__main__":
    main()
