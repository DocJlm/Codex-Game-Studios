---
name: cgs-team-polish
description: "Codex Game Studios skill adapted from original /team-polish. Use when the user asks for /team-polish, $cgs-team-polish, or this workflow. Orchestrate the polish team: coordinates performance-analyst, technical-artist, sound-designer, and qa-tester to optimize, polish, and harden a feature or area for release quality."
---

# CGS: team-polish

## Codex Operating Notes

- This is the Codex-native version of the upstream `/team-polish` workflow; invoke it as `$cgs-team-polish`.
- Inspect repository state before asking questions; use `AGENTS.md` and project validators as the execution boundary.
- When a role perspective is needed, read the matching role card from `plugins/codex-game-studios/references/role-cards/` and apply it in the current session.
- Run role-card reviews sequentially by default. Use parallel agent work only when the user explicitly requests it and suitable tools are available.
- Treat legacy hook behavior as explicit checks: run relevant validators or project tests instead of relying on hidden runtime hooks.

If no argument is provided, output usage guidance and exit without running any role-card reviews:
> Usage: `$cgs-team-polish [feature or area]` -- specify the feature or area to polish (e.g., `combat`, `main menu`, `inventory system`, `level-1`). Do not use `ask one concise question` here; output the guidance directly.

When this skill is invoked with an argument, orchestrate the polish team through a structured pipeline.

**Decision Points:** At each phase transition, use `ask one concise question` to present
the user with the role review's proposals as selectable options. Write the role review's
full analysis in conversation, then capture the decision with concise labels.
The user must approve before moving to the next phase.

## Phase 0: Resolve Review Mode

1. If `--review [mode]` was passed as an argument, use that mode.
2. Else read `production/review-mode.txt` -- use whatever is written there.
3. Else default to `lean`.

Modes:
- `full` -- run all director and lead gates as described
- `lean` -- skip director gates unless they are PHASE-GATE type (CD-PHASE-GATE, TD-PHASE-GATE, PR-PHASE-GATE, AD-PHASE-GATE)
- `solo` -- skip all director gate role reviews entirely; run the skill without any role-card gates

Store the resolved mode for use in all subsequent phases.

**Director gate skip rule**: Before running any Tier 1 director or lead for review (outside of PHASE-GATE triggers), apply the resolved mode: skip if solo mode; skip if lean mode and this is not a PHASE-GATE.

## Team Composition
- **performance-analyst** -- Profiling, optimization, memory analysis, frame budget
- **engine-programmer** -- Engine-level bottlenecks: rendering pipeline, memory, resource loading (invoke when performance-analyst identifies low-level root causes)
- **technical-artist** -- VFX polish, shader optimization, visual quality
- **sound-designer** -- Audio polish, mixing, ambient layers, feedback sounds
- **tools-programmer** -- Content pipeline tool verification, editor tool stability, automation fixes (invoke when content authoring tools are involved in the polished area)
- **qa-tester** -- Edge case testing, regression testing, soak testing

## How to Delegate

Run these role-card reviews from `plugins/codex-game-studios/references/role-cards/`:
- Role card `performance-analyst` -- Profiling, optimization, memory analysis
- Role card `engine-programmer` -- Engine-level fixes for rendering, memory, resource loading
- Role card `technical-artist` -- VFX polish, shader optimization, visual quality
- Role card `sound-designer` -- Audio polish, mixing, ambient layers
- Role card `tools-programmer` -- Content pipeline and editor tool verification
- Role card `qa-tester` -- Edge case testing, regression testing, soak testing

Always provide full context in each role review brief (target feature/area, performance budgets, known issues). Run independent role-card reviews sequentially by default; use parallel agent work only when the user explicitly requests it and tools are available (e.g., Phases 3 and 4 can run simultaneously).

## Pipeline

### Phase 1: Assessment
Delegate to **performance-analyst**:
- Profile the target feature/area using `$cgs-perf-profile`
- Identify performance bottlenecks and frame budget violations
- Measure memory usage and check for leaks
- Benchmark against target hardware specs
- Output: performance report with prioritized optimization list

### Phase 2: Optimization
Delegate to **performance-analyst** (with relevant programmers as needed):
- Fix performance hotspots identified in Phase 1
- Optimize draw calls, reduce overdraw
- Fix memory leaks and reduce allocation pressure
- Verify optimizations don't change gameplay behavior
- Output: optimized code with before/after metrics

If Phase 1 identified engine-level root causes (rendering pipeline, resource loading, memory allocator), delegate those fixes to **engine-programmer** in parallel:
- Optimize hot paths in engine systems
- Fix allocation pressure in core loops
- Output: engine-level fixes with profiler validation

### Phase 3: Visual Polish (parallel with Phase 2)
Delegate to **technical-artist**:
- Review VFX for quality and consistency with art bible
- Optimize particle systems and shader effects
- Add screen shake, camera effects, and visual juice where appropriate
- Ensure effects degrade gracefully on lower settings
- Output: polished visual effects

### Phase 4: Audio Polish (parallel with Phase 2)
Delegate to **sound-designer**:
- Review audio events for completeness (are any actions missing sound feedback?)
- Check audio mix levels -- nothing too loud or too quiet relative to the mix
- Add ambient audio layers for atmosphere
- Verify audio plays correctly with spatial positioning
- Output: audio polish list and mixing notes

### Phase 5: Hardening
Delegate to **qa-tester**:
- Test all edge cases: boundary conditions, rapid inputs, unusual sequences
- Soak test: run the feature for extended periods checking for degradation
- Stress test: maximum entities, worst-case scenarios
- Regression test: verify polish changes haven't broken existing functionality
- Test on minimum spec hardware (if available)
- Output: test results with any remaining issues

### Phase 6: Sign-off
- Collect results from all team members
- Compare performance metrics against budgets
- Report: READY FOR RELEASE / NEEDS MORE WORK
- List any remaining issues with severity and recommendations

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

## File Write Protocol

All file writes (performance reports, test results, evidence docs) are delegated to
role-card reviews run as role-card reviews. Each role-card review enforces the "May I write to [path]?"
protocol. This orchestrator does not write files directly.

## Output

A summary report covering: performance before/after metrics, visual polish changes, audio polish changes, test results, and release readiness assessment.

## Next Steps

- If READY FOR RELEASE: run `$cgs-release-checklist` for the final pre-release validation.
- If NEEDS MORE WORK: schedule remaining issues in `$cgs-sprint-plan update` and re-run `$cgs-team-polish` after fixes.
- Run `$cgs-gate-check` for a formal phase gate verdict before handing off to release.
