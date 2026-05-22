# Control Manifest

These rules govern Moonlight Dispatch implementation.

## Product Rules

- Build for Windows and macOS first.
- Keep sessions short: 8-12 minutes per night.
- Preserve the paid premium scope: no ads, no in-app purchases, no live-service dependencies.
- Do not add multiplayer or mobile support before release candidate.

## Technical Rules

- Gameplay values must live in data files, constants, or exported properties.
- Job, tool, and district identifiers must be stable lowercase slugs.
- UI may display gameplay state but must not own authoritative gameplay state.
- Save files must not store Node paths or transient scene references.
- Every story must name a validation path before implementation.

## Content Rules

- Each delivery must have a readable route decision.
- Every new hazard must have visual warning and at least one counterplay option.
- Every NPC line must support the courier fantasy or package mystery.
- English copy is canonical; Simplified Chinese localization ships when strings stabilize.

## Release Rules

- Release candidate requires Windows and macOS build evidence.
- Steam and itch.io store material must not include unlicensed third-party assets.
- Wise, tax, and bank details are account setup data and must not be committed.
