# Skill Test Spec: $cgs-vertical-slice

## Purpose

`$cgs-vertical-slice` validates whether a game concept can reach production-quality execution for one complete loop. It should define a falsifiable validation question, gate scope before implementation, track multi-session progress, and produce a PROCEED / PIVOT / KILL verdict.

## Static Expectations

- [ ] Has valid `name` and `description` frontmatter.
- [ ] Reads project context before defining scope.
- [ ] Asks for confirmation before creating or writing the vertical slice directory.
- [ ] Produces explicit verdict language: PROCEED / PIVOT / KILL.
- [ ] Has a next-step handoff based on verdict.

## Director Gate Expectations

None required. `$cgs-vertical-slice` is a pre-production validation utility; formal phase advancement remains handled by `$cgs-gate-check`.

## Test Cases

### Case 1: Happy Path - Scope Confirmed and Slice Created

**Fixture**

- `AGENTS.md`, game concept, systems index, architecture, and key GDDs exist.
- User provides a concrete slice target.
- User approves the proposed scope and directory creation.

**Input:** `$cgs-vertical-slice`

**Expected Behavior**

1. Skill reads the required project context files.
2. Skill defines a falsifiable validation question.
3. Skill presents 3-5 minute scope and success criteria for confirmation.
4. Skill asks before creating `prototypes/[concept-name]-vertical-slice/`.
5. Skill writes or updates `production/session-state/active.md` as a checkpoint.

**Assertions**

- [ ] Context sources are listed before scope is proposed.
- [ ] Scope is confirmed before implementation begins.
- [ ] Directory creation is gated behind "May I create".
- [ ] Progress checkpoint includes validation question, systems in scope, and phase.

### Case 2: Missing Design Foundation

**Fixture**

- `design/gdd/game-concept.md` is missing.
- Architecture docs are incomplete.

**Input:** `$cgs-vertical-slice`

**Expected Behavior**

1. Skill reports missing required design or architecture inputs.
2. Skill does not create prototype files.
3. Skill recommends the correct prerequisite workflow.

**Assertions**

- [ ] Missing files are listed explicitly.
- [ ] No prototype directory is created.
- [ ] Next step points to `$cgs-brainstorm`, `$cgs-map-systems`, `$cgs-create-architecture`, or another relevant prerequisite.

### Case 3: Scope Too Large

**Fixture**

- Context files exist.
- Proposed slice would exceed 5 minutes or require too many systems.

**Input:** `$cgs-vertical-slice`

**Expected Behavior**

1. Skill identifies scope creep before implementation.
2. Skill recommends cutting content, not lowering quality.
3. Skill asks the user to approve a smaller validation question.

**Assertions**

- [ ] The 3-5 minute slice rule is enforced.
- [ ] The skill preserves representative quality requirements.
- [ ] User confirmation is required before continuing.

### Case 4: Playtest Debrief and Report

**Fixture**

- Vertical slice loop is demonstrable.
- User has completed a playthrough and reports observations.

**Input:** `$cgs-vertical-slice`

**Expected Behavior**

1. Skill asks playtest debrief questions one at a time.
2. Skill captures loop completion, time-to-action, core fantasy, blockers, and pipeline feasibility.
3. Skill generates a report with evidence-backed findings.

**Assertions**

- [ ] Debrief questions are structured and sequential.
- [ ] Vague answers trigger follow-up for a specific moment.
- [ ] Report separates player-experience evidence from production-feasibility evidence.

### Case 5: Verdict Handling

**Fixture**

- Playtest and build evidence exist.
- User gives a PROCEED, PIVOT, or KILL recommendation.

**Input:** `$cgs-vertical-slice`

**Expected Behavior**

1. Skill records a final verdict.
2. Skill explains the concrete reason for the verdict.
3. Skill recommends the correct next workflow.

**Assertions**

- [ ] Verdict is exactly PROCEED, PIVOT, or KILL.
- [ ] PROCEED points toward production planning or `$cgs-gate-check`.
- [ ] PIVOT points toward design or architecture revision.
- [ ] KILL points toward archival and retrospective decisions.

## Protocol Compliance

- [ ] Reads before writes.
- [ ] Uses explicit approval before creating files or directories.
- [ ] Does not silently advance `production/stage.txt`.
- [ ] Produces a partial report if implementation or playtesting is blocked.
