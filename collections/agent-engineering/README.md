# Agent engineering workflows

Workflows for delegating to coding agents and verifying their outputs safely.

## Skills in this collection

- `ai-coding-agents`

## Install only this collection

From the repository root:

```bash
./scripts/install-collection.sh agent-engineering
hermes skills list
```

For a single Hermes profile:

```bash
./scripts/install-collection.sh agent-engineering ~/.hermes/profiles/<profile>/skills
hermes --profile <profile> skills list
```

## Usage examples

```text
Use ai-coding-agents to write a bounded Codex prompt for this bug. Do not run the agent until I approve.
```

## Agent guidance

Load the matching `SKILL.md` before acting. Keep side effects bounded, verify outputs with current evidence, and never expose credentials or private local paths.
