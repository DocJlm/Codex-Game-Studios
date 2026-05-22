---
name: cgs-release-checklist
description: "Codex Game Studios curated workflow adapted from original /release-checklist. Use when the user asks for /release-checklist, $cgs-release-checklist, or Create a focused release readiness checklist for one version and target platform set."
---

# CGS Release Checklist

Use `$cgs-release-checklist` only when the user explicitly asks for a release checklist, launch checklist, or go/no-go preparation.

## Procedure

1. Identify version, platform targets, release type, and milestone scope; default platform to `all` only if the user did not specify one.
2. Read milestone notes, release notes, known bugs, regression suite status, QA evidence, store/distribution notes, and CI/build evidence.
3. Separate blockers from advisory launch risks.
4. Include platform sections only for requested targets: PC, console, mobile, web, or custom.
5. Offer to write `production/releases/release-checklist-<version>.md` only after the user approves the draft.

## Gate Rules

- `READY`: no known blocker, build/test evidence exists, and sign-off owners are named.
- `READY WITH RISKS`: launch is possible but explicit risk acceptance is required.
- `NOT READY`: blocker bugs, missing build evidence, missing regression coverage, or missing required release assets.

## Output Contract

Return release scope, blocker list, checklist grouped by build/QA/content/store/ops/sign-off, go-no-go verdict, and next skill.
Recommend `$cgs-gate-check` or `$cgs-team-release` for final approval.
