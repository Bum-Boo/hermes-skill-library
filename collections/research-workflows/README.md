# Research workflows

Source intake, monitoring, ML experiment, evaluation, and evidence-backed reporting workflows.

## Skills in this collection

- `research-intake-and-monitoring`
- `ml-research-and-evaluation-workflows`

## Install only this collection

From the repository root:

```bash
./scripts/install-collection.sh research-workflows
hermes skills list
```

For a single Hermes profile:

```bash
./scripts/install-collection.sh research-workflows ~/.hermes/profiles/<profile>/skills
hermes --profile <profile> skills list
```

## Usage examples

```text
Use research-intake-and-monitoring to collect source evidence for this topic before summarizing.
```

```text
Use ml-research-and-evaluation-workflows to audit whether these benchmark claims are supported.
```

## Agent guidance

Load the matching `SKILL.md` before acting. Keep side effects bounded, verify outputs with current evidence, and never expose credentials or private local paths.
