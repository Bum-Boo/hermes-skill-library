# gstack-safe workflows

Spec, review, and investigation workflows for safer agent work.

## Skills in this collection

- `gstack-safe`
- `gstack-spec`
- `gstack-review`
- `gstack-investigate`

## Install only this collection

From the repository root:

```bash
./scripts/install-collection.sh gstack-safe
hermes skills list
```

For a single Hermes profile:

```bash
./scripts/install-collection.sh gstack-safe ~/.hermes/profiles/<profile>/skills
hermes --profile <profile> skills list
```

## Use

Ask your agent to load the matching skill by name, or describe the task clearly so automatic skill loading can select it.
