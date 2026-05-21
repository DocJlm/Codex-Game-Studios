---
name: cgs-map-systems
description: "Codex Game Studios curated workflow adapted from original /map-systems. Use when the user asks for /map-systems, $cgs-map-systems, or Break an approved game concept into systems and dependency order."
---

# CGS Map Systems

Use `$cgs-map-systems` after a concept exists and before writing per-system GDDs.

## Procedure

1. Read `design/gdd/game-concept.md` and any existing GDDs.
2. Identify player-facing systems, support systems, content systems, and platform systems.
3. Classify each system as MVP, stretch, or later.
4. Map dependencies and recommended design order.
5. Offer to write `design/gdd/systems-index.md`.

## Output Contract

Return system list, dependency graph in text form, MVP boundary, and next `$cgs-design-system` targets.
