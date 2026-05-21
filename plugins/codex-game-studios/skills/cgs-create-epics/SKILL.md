---
name: cgs-create-epics
description: "Codex Game Studios curated workflow adapted from original /create-epics. Use when the user asks for /create-epics, $cgs-create-epics, or Translate approved design and architecture into production epics."
---

# CGS Create Epics

Use `$cgs-create-epics` when GDDs and architecture are ready for production planning.

## Procedure

1. Read GDDs, architecture, accepted ADRs, and control manifest.
2. Group work into epics by coherent deliverable, not by file type.
3. For each epic, define goal, included systems, out-of-scope items, dependencies, acceptance criteria, and test evidence.
4. Offer to create `production/epics/<epic-slug>/EPIC.md`.

## Output Contract

Return proposed epic list first; write files only after approval.
