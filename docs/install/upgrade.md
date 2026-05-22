# Upgrade Guide

Use this guide when updating an existing Codex Game Studios clone or preparing a release branch.

## Before Updating

Check whether you have local work:

```bash
git status --short
```

If the tree is dirty, commit your work or move it to a branch before pulling updates. Do not overwrite local game design, production, source, or asset changes just to update the plugin package.

## Update To Latest Main

```bash
git fetch origin
git pull --ff-only origin main
git fetch --tags origin
```

Then validate:

Windows PowerShell:

```powershell
python tools\run_all_validators.py
```

macOS zsh or bash:

```bash
python3 tools/run_all_validators.py
```

## Update To A Specific Tag

```bash
git fetch --tags origin
git switch --detach v1.6.0
python3 tools/run_all_validators.py
```

If you need to keep working, create a branch from the tag:

```bash
git switch -c my-cgs-upgrade-v1-6 v1.6.0
```

## After Updating

Check these public surfaces:

- `plugins/codex-game-studios/.codex-plugin/plugin.json` has the expected version.
- `.agents/plugins/marketplace.json` still points at `./plugins/codex-game-studios`.
- `README.md` and `docs/releases/` mention the version you installed.
- `python3 tools/run_all_validators.py` or `python tools\run_all_validators.py` passes.

If Codex Desktop does not recognize `$cgs-*` by name after an update, use the path-based fallback in `docs/install/codex-desktop.md`.

## Maintainer Release Checklist

For a normal v1.x release:

1. Bump `plugins/codex-game-studios/.codex-plugin/plugin.json`.
2. Bump `tools/validate_cgs.py` and `tools/prepare_v01.py`.
3. Update `README.md`, `CHANGELOG.md`, `docs/releases/vX.Y.Z.md`, and `docs/v1-readiness/freeze-checklist.md` when affected.
4. Add or update validators for any new public contract.
5. Run `python3 tools/run_all_validators.py`.
6. Commit, tag, push `main`, push the tag, and verify the remote SHA.

Do not copy legacy runtime hooks into the Codex plugin package. Hook behavior remains reference-only unless the hook policy and validators change in the same release.
