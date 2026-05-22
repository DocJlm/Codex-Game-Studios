# Production Readiness Workflow Notes

These notes document the v0.7 polish targets for workflows used around story readiness, scope control, evidence review, regression coverage, and release readiness.

## `$cgs-story-readiness`

Use before implementation starts. The skill should decide whether one story is implementable now, not redesign the story or edit code.

Minimum useful output:
- Verdict: `READY`, `NEEDS WORK`, or `BLOCKED`.
- Evidence paths.
- Blocking decisions or dependencies.
- Smallest next action.
- Recommended next skill.

## `$cgs-scope-check`

Use when a story, epic, sprint, milestone, or feature may have drifted from its baseline. The skill should compare planned scope to current state and recommend cuts or formal re-scope.

Minimum useful output:
- Baseline evidence.
- Current evidence.
- Additions and removals.
- Schedule, quality, and integration risk.
- Verdict: `PASS`, `CONCERNS`, or `FAIL`.

## `$cgs-test-evidence-review`

Use before story closure, QA handoff, milestone review, or release review. The skill should map acceptance criteria to actual evidence and flag closure blockers.

Minimum useful output:
- Evidence table.
- Criterion coverage.
- Blocking gaps and advisory gaps.
- Verdict: `ADEQUATE`, `INCOMPLETE`, or `MISSING`.
- Routing to `$cgs-dev-story` or `$cgs-smoke-check` when evidence is absent.

## `$cgs-regression-suite`

Use before release gates, sprint close, or after bug fixes. The skill should report or update the regression-suite manifest only with explicit approval.

Minimum useful output:
- Mode: `report`, `audit`, or `update`.
- Critical-path and bug-fix coverage summary.
- Missing, partial, stale, flaky, and quarantined coverage.
- Recommended manifest changes.
- Verdict: `OK`, `GAPS`, or `STALE`.

## `$cgs-release-checklist`

Use only when explicitly requested for release readiness or go/no-go preparation. The skill should produce a focused checklist for a version and platform set.

Minimum useful output:
- Release scope and target platforms.
- Blocker list.
- Build, QA, content, store, ops, and sign-off checklist.
- Verdict: `READY`, `READY WITH RISKS`, or `NOT READY`.
- Routing to `$cgs-gate-check` or `$cgs-team-release`.
