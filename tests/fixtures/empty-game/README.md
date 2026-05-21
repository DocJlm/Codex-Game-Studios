# Empty Game Fixture

This fixture is a tiny Codex Game Studios project used for workflow smoke checks.

Expected smoke path:

1. `$cgs-start` detects an already bootstrapped lean project.
2. `$cgs-project-stage-detect` reports `PRODUCTION` because concept, engine preferences, architecture, epic, and ready story exist.
3. `$cgs-dev-story production/epics/core-loop/STORY-001-player-loop.md` has a small ready story to inspect.
4. `$cgs-story-done production/epics/core-loop/STORY-001-player-loop.md` can report missing implementation evidence.

See `WALKTHROUGH.md` for the expected transcript shape.
