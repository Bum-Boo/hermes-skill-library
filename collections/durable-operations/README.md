# Durable Operations

Workflows for long-running agent projects that must remain recoverable across sessions and produce verified artifacts.

## Included skill

- [`durable-kanban-workflows`](../../skills/operations/durable-kanban-workflows/) — persistent execution graphs, bounded cards, crash-safe claims, serialized writers, controlled recovery, and final audits.

## Install

```bash
./scripts/install-collection.sh durable-operations
```

Install into one profile:

```bash
./scripts/install-collection.sh durable-operations ~/.hermes/profiles/<profile>/skills
```

## Use when

- work spans multiple batches or agent sessions;
- workers share an external writer or canonical ledger;
- retries must distinguish transient failures from owner decisions;
- board completion must be reconciled against real artifacts.
