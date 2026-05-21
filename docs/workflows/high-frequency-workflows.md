# High-Frequency Workflow Notes

These notes document the v0.3 polish targets for the first workflows users are likely to repeat during production.

## `$cgs-code-review`

Use it like a code review, not a rewrite command. It should inspect the diff, read the story context when available, and lead with concrete findings. A good answer starts with severity-ordered risks and only then gives summary context.

Minimum useful output:
- Findings with severity, file path, and line when possible.
- Open questions or assumptions.
- Test gaps and residual risk.
- Short change summary.

## `$cgs-qa-plan`

Use it when the user needs a scoped test plan. It should map acceptance criteria to verification paths and separate automated checks from manual gameplay checks.

Minimum useful output:
- Scope and out-of-scope boundaries.
- Risk matrix.
- Test matrix.
- Evidence artifacts.
- Exit criteria.

## `$cgs-smoke-check`

Use it for a fast confidence pass after implementation. It should run safe commands when available and clearly mark checks that require the game editor or a human play session.

Minimum useful output:
- Commands run.
- Pass/fail result.
- Manual checks remaining.
- Reproduction details for failures.
- Next fix or verification step.
