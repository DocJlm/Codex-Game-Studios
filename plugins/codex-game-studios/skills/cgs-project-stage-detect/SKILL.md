---
name: cgs-project-stage-detect
description: "Codex Game Studios core workflow adapted from original /project-stage-detect. Use when the user asks for /project-stage-detect, $cgs-project-stage-detect, or Audit an existing game project and classify its Codex Game Studios stage."
---

# CGS Project Stage Detect

Use `$cgs-project-stage-detect` for brownfield projects or when project state is unclear.

## Procedure

1. Inspect folders and files without changing them.
2. Detect engine and language from source, manifests, and project files.
3. Count design docs, architecture docs, epics, stories, sprint files, tests, prototypes, and release artifacts.
4. Compare findings with `workflow-catalog.yaml`.
5. Produce a stage report and a migration path.

## Output Contract

Return verdict: `FRESH`, `CONCEPT`, `SYSTEMS DESIGN`, `TECHNICAL SETUP`, `PRE-PRODUCTION`, `PRODUCTION`, `POLISH`, `RELEASE`, or `INCONSISTENT`.
Include evidence paths and the next 3 actions.
