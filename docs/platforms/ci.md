# CI Usage

Codex Game Studios uses GitHub Actions to prove that the plugin package, docs, examples, and validators work across Windows, macOS, and Linux.

## Workflow Shape

The validation workflow lives at:

```text
.github/workflows/validate.yml
```

It runs on:

```text
windows-latest
macos-latest
ubuntu-latest
```

The workflow installs Python 3.12 and runs:

```bash
python tools/run_all_validators.py
```

## Local Reproduction

Run the same entrypoint locally before opening a pull request.

Windows PowerShell:

```powershell
python tools\run_all_validators.py
```

macOS zsh or bash:

```bash
python3 tools/run_all_validators.py
```

Linux:

```bash
python3 tools/run_all_validators.py
```

## What CI Covers

- Plugin manifest and marketplace shape.
- Skill count, skill names, and frontmatter.
- Role card and rule counts.
- Workflow transcripts and smoke fixture docs.
- Install, platform, upgrade, and community docs.
- Runtime hook policy.
- Godot example static validation and optional scene load when Godot is available.
- Upstream parity report.
- Codex-native skill migration rules.
- Testing framework repo-local path rules.

## CI Design Rules

- Keep the entrypoint cross-platform: `python tools/run_all_validators.py`.
- Avoid POSIX-only `find`, `wc`, or shell pipelines in GitHub Actions.
- Keep Godot optional in CI; local machines with Godot get the stronger scene-load check.
- Prefer explicit validators over hidden runtime behavior.
- When a doc becomes part of the public contract, add a validator token for it.
