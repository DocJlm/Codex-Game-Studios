---
name: cgs-architecture-review
description: "Codex Game Studios curated workflow adapted from original /architecture-review. Use when the user asks for /architecture-review, $cgs-architecture-review, or Review architecture against design goals, engine constraints, and production stories."
---

# CGS Architecture Review

Use `$cgs-architecture-review` when architecture, module boundaries, ADRs, or technical direction need review.

## Procedure

1. Read `docs/architecture/architecture.md`, ADRs, technical preferences, control manifest, GDDs, and relevant source.
2. Check module ownership, data flow, persistence, scene or entity boundaries, UI separation, testability, and engine constraints.
3. Compare the architecture to active epics and stories; flag gaps that will block implementation.
4. Use technical director and lead programmer role-card perspectives sequentially.
5. Recommend ADRs only for decisions that need durable project memory.

## Output Contract

Return strengths, risks, required changes, optional improvements, and ADR recommendations.
