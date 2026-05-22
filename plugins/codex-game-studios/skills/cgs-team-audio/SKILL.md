---
name: cgs-team-audio
description: "Codex Game Studios skill adapted from original /team-audio. Use when the user asks for /team-audio, $cgs-team-audio, or this workflow. Orchestrate audio team: audio-director + sound-designer + technical-artist + gameplay-programmer for full audio pipeline from direction to implementation."
---

# CGS: team-audio

## Codex Operating Notes

- This is the Codex-native version of the upstream `/team-audio` workflow; invoke it as `$cgs-team-audio`.
- Inspect repository state before asking questions; use `AGENTS.md` and project validators as the execution boundary.
- When a role perspective is needed, read the matching role card from `plugins/codex-game-studios/references/role-cards/` and apply it in the current session.
- Run role-card reviews sequentially by default. Use parallel agent work only when the user explicitly requests it and suitable tools are available.
- Treat legacy hook behavior as explicit checks: run relevant validators or project tests instead of relying on hidden runtime hooks.

If no argument is provided, output usage guidance and exit without running any role-card reviews:
> Usage: `$cgs-team-audio [feature or area]` -- specify the feature or area to design audio for (e.g., `combat`, `main menu`, `forest biome`, `boss encounter`). Do not use `ask one concise question` here; output the guidance directly.

When this skill is invoked with an argument, orchestrate the audio team through a structured pipeline.

**Decision Points:** At each step transition, use `ask one concise question` to present
the user with the role review's proposals as selectable options. Write the role review's
full analysis in conversation, then capture the decision with concise labels.
The user must approve before moving to the next step.

## Phase 0: Resolve Review Mode

1. If `--review [mode]` was passed as an argument, use that mode.
2. Else read `production/review-mode.txt` -- use whatever is written there.
3. Else default to `lean`.

Modes:
- `full` -- run all director and lead gates as described
- `lean` -- skip director gates unless they are PHASE-GATE type (CD-PHASE-GATE, TD-PHASE-GATE, PR-PHASE-GATE, AD-PHASE-GATE)
- `solo` -- skip all director gate role reviews entirely; run the skill without any role-card gates

Store the resolved mode for use in all subsequent phases.

1. **Read the argument** for the target feature or area (e.g., `combat`,
   `main menu`, `forest biome`, `boss encounter`).

2. **Gather context**:
   - Read relevant design docs in `design/gdd/` for the feature
   - Read the sound bible at `design/gdd/sound-bible.md` if it exists
   - Read existing audio asset lists in `assets/audio/`
   - Read any existing sound design docs for this area

## How to Delegate

Run these role-card reviews from `plugins/codex-game-studios/references/role-cards/`:
- Role card `audio-director` -- Sonic identity, emotional tone, audio palette
- Role card `sound-designer` -- SFX specifications, audio events, mixing groups
- Role card `technical-artist` -- Audio middleware, bus structure, memory budgets
- Role card `[primary engine specialist]` -- Validate audio integration patterns for the engine
- Role card `gameplay-programmer` -- Audio manager, gameplay triggers, adaptive music

Always provide full context in each role review brief (feature description, existing audio assets, design doc references).

3. **Orchestrate the audio team** in sequence:

### Step 1: Audio Direction (audio-director)
Apply role card `audio-director` to:
- Define the sonic identity for this feature/area
- Specify the emotional tone and audio palette
- Set music direction (adaptive layers, stems, transitions)
- Define audio priorities and mix targets
- Establish any adaptive audio rules (combat intensity, exploration, tension)

### Step 2: Sound Design and Audio Accessibility (parallel)
Apply role card `sound-designer` to:
- Create detailed SFX specifications for every audio event
- Define sound categories (ambient, UI, gameplay, music, dialogue)
- Specify per-sound parameters (volume range, pitch variation, attenuation)
- Plan audio event list with trigger conditions
- Define mixing groups and ducking rules

Run the `accessibility-specialist` role-card review as part of the same review set to:
- Identify which audio events carry critical gameplay information (damage received, enemy nearby, objective complete) and require visual alternatives for hearing-impaired players
- Specify subtitle requirements: which audio events need captions, what text format, on-screen duration
- Check that no gameplay state is communicated by audio alone (all must have a visual fallback)
- Review the audio event list for any that could cause issues for players with auditory sensitivities (high-frequency alerts, sudden loud events)
- Output: audio accessibility requirements list integrated into the audio event spec

### Step 3: Technical Implementation (parallel)
Apply role card `technical-artist` to:
- Design the audio middleware integration (Wwise/FMOD/native)
- Define audio bus structure and routing
- Specify memory budgets for audio assets per platform
- Plan streaming vs preloaded asset strategy
- Design any audio-reactive visual effects

Run the **primary engine specialist** in parallel (from `plugins/codex-game-studios/references/studio-docs/technical-preferences.md` Engine Specialists) to validate the integration approach:
- Is the proposed audio middleware integration idiomatic for the engine? (e.g., Godot's built-in AudioStreamPlayer vs FMOD, Unity's Audio Mixer vs Wwise, Unreal's MetaSounds vs FMOD)
- Any engine-specific audio node/component patterns that should be used?
- Known audio system changes in the pinned engine version that affect the integration plan?
- Output: engine audio integration notes to merge with the technical-artist's plan

If no engine is configured, skip the specialist role-card review.

### Step 4: Code Integration (gameplay-programmer)
Apply role card `gameplay-programmer` to:
- Implement audio manager system or review existing
- Wire up audio events to gameplay triggers
- Implement adaptive music system (if specified)
- Set up audio occlusion/reverb zones
- Write unit tests for audio event triggers

4. **Compile the audio design document** combining all team outputs.

5. **Save to** `design/audio/audio-[feature].md`.

   Note: If `design/audio/` does not exist, the role-card review writing the document should create it (the directory will be created automatically when the file is written).

6. **Output a summary** with: audio event count, estimated asset count,
   implementation tasks, and any open questions between team members.

Verdict: **COMPLETE** -- audio design document produced and team pipeline finished.

If the pipeline stops because a dependency is unresolved (e.g., critical accessibility gap or missing GDD not resolved by the user):

Verdict: **BLOCKED** -- [reason]

## File Write Protocol

All file writes (audio design docs, SFX specs, implementation files) are delegated
to role-card reviews run as role-card reviews. Each role-card review enforces the "May I write to [path]?"
protocol. This orchestrator does not write files directly.

## Next Steps

- Review the audio design doc with the audio-director before implementation begins.
- Use `$cgs-dev-story` to implement the audio manager and event system once the design is approved.
- Run `$cgs-asset-audit` after audio assets are created to verify naming and format compliance.

## Error Recovery Protocol

If any role-card review (through role-card review) returns BLOCKED, errors, or cannot complete:

1. **Surface immediately**: Report "[AgentName]: BLOCKED -- [reason]" to the user before continuing to dependent phases
2. **Assess dependencies**: Check whether the blocked role-card review's output is required by subsequent phases. If yes, do not proceed past that dependency point without user input.
3. **Offer options** via ask one concise question with choices:
   - Skip this role-card review and note the gap in the final report
   - Retry with narrower scope
   - Stop here and resolve the blocker first
4. **Always produce a partial report** -- output whatever was completed. Never discard work because one role-card review blocked.

Common blockers:
- Input file missing (story not found, GDD absent) -> redirect to the skill that creates it
- ADR status is Proposed -> do not implement; run `$cgs-architecture-decision` first
- Scope too large -> split into two stories via `$cgs-create-stories`
- Conflicting instructions between ADR and story -> surface the conflict, do not guess
