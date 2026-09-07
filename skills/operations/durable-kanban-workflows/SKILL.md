---
name: durable-kanban-workflows
description: "Use when a long-running project must survive session limits, coordinate shared writers, recover safely, and finish with verified artifacts."
version: 1.0.0
author: bumboo / Hermes Skill Library contributors
license: MIT
metadata:
  hermes:
    tags: [kanban, orchestration, recovery, long-running, verification]
    related_skills: [verification-before-completion]
---

# Durable Kanban Workflows

Use this skill for multi-batch work that must continue across agent sessions, process failures, or scheduler restarts without losing ownership or overstating progress.

## Core contract

1. **Persist the execution graph.** Store cards, dependencies, attempts, blockers, and terminal outcomes in durable state. Add one final audit card that depends on every execution card.
2. **Make cards bounded.** Every card needs explicit inputs, outputs, acceptance checks, retry limits, and an owner. A card describes a real artifact or state transition, not merely analysis activity.
3. **Use stable identities.** Key work by canonical source or domain identity rather than queue position. Deduplicate before applying batch limits.
4. **Make claims crash-safe.** Record `claimed`, `completed`, and `rolled_back` states through locking and atomic replacement. A restarted card may resume its own claim; another card must not take an active claim.
5. **Serialize shared writers.** Protect each shared external system, ledger, or final artifact with one writer lane. Recheck idempotency and current target state while holding the lock.
6. **Prove the production path early.** Before scheduling a batch, run a one-item canary through the same adapter and command path. Verify the resulting artifact independently.
7. **Separate internal review from owner decisions.** Handle tests, schema checks, and code review inside the workflow. Stop for the user only when authority changes: publication, cost, credentials, destructive action, or an unresolved policy choice.
8. **Finish with a fresh audit.** Reconcile expected and completed identities, unresolved blockers, duplicate artifacts, forbidden side effects, and exact readbacks. A completed board is not proof that its artifacts are correct.

## Recovery rules

- Retry only classified transient failures, with a small fixed cap.
- Re-read current card and target state before every recovery transition.
- Do not trust process exit code alone; require a positive transition acknowledgement and state readback.
- If a worker exits without a terminal card transition, classify it as a protocol failure and inspect its artifact state before retrying.
- Never mark incomplete work complete merely to clear a stale lock or blocked card.
- Keep rollback points and immutable run reports per attempt.

## Scheduler and concurrency safety

- Use one dispatcher owner for a board. A named board does not by itself prevent another scheduler from claiming its cards.
- Distinguish per-worker concurrency from limits on a resource shared by several workers.
- Keep heavy work in workers; scheduled jobs should enqueue idempotently or perform deterministic health checks.
- A dispatch count limits one invocation unless the scheduler explicitly guarantees a board-wide cap.
- Before promoting many dependent cards to ready, verify that the configured work-in-progress limit is real and supported.

## Progress reporting

Report these separately:

- completed cards and verified artifacts;
- currently running cards;
- blocked cards and whether recovery is automatic;
- remaining canonical work;
- whether the final audit has passed.

Do not count queued plans, started processes, or scheduler success as completed output. Prefer milestone reports and one final result over raw worker notifications.

## Completion checklist

- [ ] Canonical expected identities are frozen and deduplicated.
- [ ] Every completed card has a concrete artifact or verified state change.
- [ ] Shared writers were serialized and idempotency was checked under lock.
- [ ] Retries preserve prior reports and rollback points.
- [ ] No owner-decision blocker was bypassed.
- [ ] Final cardinality and duplicate checks pass.
- [ ] External or installed state was read back independently.
- [ ] Forbidden side-effect count is zero.
