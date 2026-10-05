# Real photo sources

All four images are from Wikimedia Commons, public domain / CC0 — no attribution
required, but credited here for provenance.

| File | Source | Author | License |
| :--- | :--- | :--- | :--- |
| `coins.jpg` | [Stacks of Coins.jpg](https://commons.wikimedia.org/wiki/File:Stacks_of_Coins.jpg) | Kevin Schneider | CC0 1.0 Universal |
| `stop_sign.jpg` | [Bilingualstopsign.jpg](https://commons.wikimedia.org/wiki/File:Bilingualstopsign.jpg) | Steven Spell (User:Ibagli) | Public domain |
| `dice.jpg` | [One-red-dice-01.jpg](https://commons.wikimedia.org/wiki/File:One-red-dice-01.jpg) | Stephen Silver | CC0 1.0 Universal |
| `book.jpg` | [Blank book on a table.jpg](https://commons.wikimedia.org/wiki/File:Blank_book_on_a_table.jpg) | Trey Jones (User:Trey314159) | CC0 1.0 Universal |

Picked deliberately for variety, not just convenience:

- `coins.jpg` — stacked coins photographed edge-on, not face-on, so each stack reads as
  overlapping rounded rectangles rather than clean circles. A real-world instance of the
  "touching/overlapping objects merge into one contour" pitfall (see the plan's §6),
  not a mislabel.
- `stop_sign.jpg` — a real octagon in a cluttered street scene (buildings, flags,
  people) — tests contour filtering by area against genuine background noise, not a
  blank canvas.
- `dice.jpg` — a cube photographed at an angle, so its 2D silhouette is a hexagon, not
  a square. Another honest real-world mismatch with the clean synthetic shape classes.
- `book.jpg` — the one clean case: a white rectangular book on a wood-grain table,
  good contrast, a straightforward rectangle to detect correctly.
