---
name: cgs-smoke-check
description: "Codex Game Studios curated workflow adapted from original /smoke-check. Use when the user asks for /smoke-check, $cgs-smoke-check, or Run or design a fast smoke check for core game workflows."
---

# CGS Smoke Check

Use `$cgs-smoke-check` when the user wants a fast confidence pass after changes.

## Procedure

1. Identify the smallest playable or verifiable path for the current story or milestone.
2. Prefer existing commands in `AGENTS.md`, package manifests, engine project files, or test docs.
3. Run safe automated checks when available, then list manual checks that still require the user or a game runtime.
4. Capture failures with exact commands, paths, and reproduction steps.
5. Avoid broad regression testing unless the user asks for a full QA pass.

## Output Contract

Return commands run, pass/fail results, manual checks remaining, and the next fix or verification step.
