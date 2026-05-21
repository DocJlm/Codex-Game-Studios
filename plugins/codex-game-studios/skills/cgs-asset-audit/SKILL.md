---
name: cgs-asset-audit
description: "Codex Game Studios skill adapted from original /asset-audit. Use when the user asks for /asset-audit, $cgs-asset-audit, or this workflow. Audits game assets for compliance with naming conventions, file size budgets, format standards, and pipeline requirements. Identifies orphaned assets, missing references, and standard violations."
---

# CGS: asset-audit

> Codex adaptation: this skill is migrated from the upstream `/asset-audit` workflow. Invoke it as `$cgs-asset-audit`. Use Codex tools and the current workspace rules; do not depend on Claude-only frontmatter, settings hooks, or slash-command runtime behavior.

> Migration phase: Full migration. Legacy role names are available as role cards under `plugins/codex-game-studios/references/role-cards/`.

## Phase 1: Read Standards

Read the art bible or asset standards from the relevant design docs and the AGENTS.md naming conventions.

---

## Phase 2: Scan Asset Directories

Scan the target asset directory using Glob:

- `assets/art/**/*` for art assets
- `assets/audio/**/*` for audio assets
- `assets/vfx/**/*` for VFX assets
- `assets/shaders/**/*` for shaders
- `assets/data/**/*` for data files

---

## Phase 3: Run Compliance Checks

**Naming conventions:**
- Art: `[category]_[name]_[variant]_[size].[ext]`
- Audio: `[category]_[context]_[name]_[variant].[ext]`
- All files must be lowercase with underscores

**File standards:**
- Textures: Power-of-two dimensions, correct format (PNG for UI, compressed for 3D), within size budget
- Audio: Correct sample rate, format (OGG for SFX, OGG/MP3 for music), within duration limits
- Data: Valid JSON/YAML, schema-compliant

**Orphaned assets:** Search code for references to each asset file. Flag any with no references.

**Missing assets:** Search code for asset references and verify the files exist.

---

## Phase 4: Output Audit Report

```markdown
# Asset Audit Report -- [Category] -- [Date]

## Summary
- **Total assets scanned**: [N]
- **Naming violations**: [N]
- **Size violations**: [N]
- **Format violations**: [N]
- **Orphaned assets**: [N]
- **Missing assets**: [N]
- **Overall health**: [CLEAN / MINOR ISSUES / NEEDS ATTENTION]

## Naming Violations
| File | Expected Pattern | Issue |
|------|-----------------|-------|

## Size Violations
| File | Budget | Actual | Overage |
|------|--------|--------|---------|

## Format Violations
| File | Expected Format | Actual Format |
|------|----------------|---------------|

## Orphaned Assets (no code references found)
| File | Last Modified | Size | Recommendation |
|------|-------------|------|---------------|

## Missing Assets (referenced but not found)
| Reference Location | Expected Path |
|-------------------|---------------|

## Recommendations
[Prioritized list of fixes]

## Verdict: [COMPLIANT / WARNINGS / NON-COMPLIANT]
```

This skill is read-only -- it produces a report but does not write files.

---

## Phase 5: Next Steps

- Fix naming violations using the patterns defined in AGENTS.md.
- Delete confirmed orphaned assets after manual review.
- Run `$cgs-content-audit` to cross-check asset counts against GDD-specified requirements.
