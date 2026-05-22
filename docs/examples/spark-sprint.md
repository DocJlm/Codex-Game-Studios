# Spark Sprint Example Transcript

This document links the v0.6 static example project to the Codex Game Studios workflow loop.

Example path:

```text
examples/spark-sprint/
```

Suggested prompt sequence:

```text
Use $cgs-start on examples/spark-sprint.
Use $cgs-project-stage-detect on examples/spark-sprint.
Use $cgs-dev-story examples/spark-sprint/production/epics/core-loop/STORY-001-player-loop.md.
Use $cgs-smoke-check for examples/spark-sprint.
Use $cgs-story-done examples/spark-sprint/production/epics/core-loop/STORY-001-player-loop.md.
Use $cgs-code-review on the Spark Sprint source draft.
Use $cgs-qa-plan for the Spark Sprint Core Loop epic.
```

Expected behavior:

- Codex should treat the project as a Godot 4.3 / GDScript static example.
- Codex should not require Godot to be installed for repository validation.
- Codex should cite evidence paths before proposing edits.
- Runtime playtest evidence should be listed as manual follow-up.
