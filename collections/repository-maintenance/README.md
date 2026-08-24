# Repository Maintenance

Use this collection when auditing or maintaining repositories derived from upstream projects.

## Included skill

- `downstream-source-maintenance` — classifies fork and snapshot history, audits install/update identity and inherited automation, reviews privacy safely, and verifies findings against a pinned upstream baseline.

## Install

```bash
./scripts/install-collection.sh repository-maintenance
```

For one Hermes profile:

```bash
./scripts/install-collection.sh repository-maintenance ~/.hermes/profiles/<profile>/skills
```

## Safety notes

- Inspect before changing repository state.
- Pin the upstream baseline instead of comparing only with moving `main`.
- Keep candidate secret values out of logs and reports.
- Treat publishing, deployment, release, and history rewriting as separate authority boundaries.
- Verify local and remote state by exact commit identity.
