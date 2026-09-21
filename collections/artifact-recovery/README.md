# Artifact Recovery

Use this collection when the intended prior deliverable must be identified among ambiguous local exports and copied safely.

## Included skill

- `local-artifact-recovery` — ranks candidate files using provenance, content, timestamps, and hashes, then verifies the delivered copy.

## Install

```bash
./scripts/install-collection.sh artifact-recovery
```

For one Hermes profile:

```bash
./scripts/install-collection.sh artifact-recovery ~/.hermes/profiles/<profile>/skills
```

## Safety notes

- Search only user-approved locations and likely document roots.
- Treat filenames and timestamps as clues rather than proof.
- Copy by default; do not delete or move source files without explicit authorization.
- Compare hashes and reopen the destination before reporting delivery.
