---
name: cgs-help
description: "Codex Game Studios core workflow adapted from original /help. Use when the user asks for /help, $cgs-help, or Context-aware next-step navigator for Codex Game Studios projects."
---

# CGS Help

Use `$cgs-help` when the user asks what to do next in the Codex Game Studios pipeline.

## Procedure

1. Read `plugins/codex-game-studios/references/studio-docs/workflow-catalog.yaml`.
2. Inspect project artifacts for each phase: concept, systems design, technical setup, pre-production, production, polish, release.
3. Identify the current phase by the first missing required artifact.
4. Recommend one next required action and up to two optional actions.
5. If the state is contradictory, route to `$cgs-project-stage-detect`.

## Output Contract

Return: current phase, completed signals, blockers, recommended next skill, and why it is next.
