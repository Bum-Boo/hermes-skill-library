# Agent engineering workflows

Workflows for delegating to coding agents safely and designing multi-user visual editors with explicit system boundaries.

## Skills in this collection

- `ai-coding-agents`
- `collaborative-visual-editor-architecture`

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

Use collaborative-visual-editor-architecture to separate collaboration, persistence, and execution for this shared node editor.
```

## Agent guidance

Load the matching `SKILL.md` before acting. Keep side effects bounded, verify outputs with current evidence, and never expose credentials or private local paths.
