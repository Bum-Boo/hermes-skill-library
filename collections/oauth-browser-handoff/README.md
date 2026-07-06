# OAuth browser handoff

Safe human-in-the-browser OAuth setup for headless, WSL, or remote agents.

## Skills in this collection

- `oauth-browser-handoff`

## Install only this collection

From the repository root:

```bash
./scripts/install-collection.sh oauth-browser-handoff
hermes skills list
```

For a single Hermes profile:

```bash
./scripts/install-collection.sh oauth-browser-handoff ~/.hermes/profiles/<profile>/skills
hermes --profile <profile> skills list
```

## Use

Ask your agent to load the matching skill by name, or describe the task clearly so automatic skill loading can select it.
