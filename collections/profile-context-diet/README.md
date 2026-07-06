# Hermes profile context diet

Audit and reduce Hermes profile context weight without losing durable knowledge.

## Skills in this collection

- `hermes-profile-context-diet`

## Install only this collection

From the repository root:

```bash
./scripts/install-collection.sh profile-context-diet
hermes skills list
```

For a single Hermes profile:

```bash
./scripts/install-collection.sh profile-context-diet ~/.hermes/profiles/<profile>/skills
hermes --profile <profile> skills list
```

## Use

Ask your agent to load the matching skill by name, or describe the task clearly so automatic skill loading can select it.
