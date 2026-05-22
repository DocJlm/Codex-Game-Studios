# Spark Sprint Example Transcript

This document links the Spark Sprint example project to the Codex Game Studios workflow loop. It is statically validated by default and optionally runnable in Godot 4.x.

Example path:

```text
examples/spark-sprint/
```

Realistic Codex run transcript:

```text
docs/transcripts/spark-sprint-codex-run.md
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

- Codex should treat the project as a Godot 4.3 / GDScript optional runnable example.
- Codex should not require Godot to be installed for repository validation.
- `python tools\validate_godot_example.py` should report `SKIP` when Godot is unavailable and try to load `scenes/main.tscn` when Godot is available.
- Codex should cite evidence paths before proposing edits.
- Runtime playtest evidence should be listed as optional manual follow-up.
