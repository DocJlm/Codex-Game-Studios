---
name: cgs-create-architecture
description: "Codex Game Studios curated workflow adapted from original /create-architecture. Use when the user asks for /create-architecture, $cgs-create-architecture, or Create the master architecture plan from approved design docs."
---

# CGS Create Architecture

Use `$cgs-create-architecture` after core GDDs exist and before implementation stories.

## Procedure

1. Read GDDs, technical preferences, engine references, and existing source.
2. Identify modules, data ownership, runtime flow, persistence, UI boundary, testing strategy, and engine-specific constraints.
3. List required ADRs for decisions that should not live only in prose.
4. Draft `docs/architecture/architecture.md`.
5. Offer to write the draft and recommend `$cgs-architecture-decision` for each required ADR.

## Output Contract

Return architecture summary, module map, required ADR list, and known risks.
