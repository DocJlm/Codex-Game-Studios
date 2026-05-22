---
name: cgs-story-readiness
description: "Codex Game Studios curated workflow adapted from original /story-readiness. Use when the user asks for /story-readiness, $cgs-story-readiness, or Check whether a story is ready before implementation begins."
---

# CGS Story Readiness

Use `$cgs-story-readiness` before `$cgs-dev-story` or when a story feels ambiguous.

## Procedure

1. Read exactly one target story plus its epic, linked GDDs, ADRs, control manifest, and available test notes.
2. Check implementation scope, acceptance criteria, dependencies, required assets, data readiness, testability, and unresolved decisions.
3. Inspect relevant source only to confirm existing context; do not edit implementation files.
4. Identify the smallest unblocker: one question, one upstream doc fix, or one dependency to finish.
5. If ready, name the first `$cgs-dev-story` implementation focus and the tests that should prove it.

## Readiness Rules

- `READY`: scope is bounded, criteria are testable, dependencies are available, and the next implementation step is clear.
- `NEEDS WORK`: story can be fixed locally by clarifying criteria, narrowing scope, or adding missing test notes.
- `BLOCKED`: implementation depends on missing design, architecture, asset, engine, or product decisions.

## Output Contract

Return verdict: `READY`, `NEEDS WORK`, or `BLOCKED`.
Include evidence paths, blockers, smallest next action, and recommended next skill.
