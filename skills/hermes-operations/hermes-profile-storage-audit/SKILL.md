---
name: hermes-profile-storage-audit
description: "Use when Hermes profiles accumulate files or disk usage; inventory storage safely, classify regeneration risk, and produce a dry-run cleanup plan."
version: 1.0.0
author: bumboo / Hermes Skill Library contributors
license: MIT
metadata:
  hermes:
    tags: [hermes, profiles, storage, cleanup, audit]
    related_skills: [hermes-profile-config-inspection, hermes-profile-context-diet]
---

# Hermes Profile Storage Audit

## Goal

Explain where profile storage is going without deleting anything or exposing private content.

## Inventory

For every selected profile, report file count and bytes grouped by top-level area. Distinguish at least:

- sessions and state;
- memories, libraries, and skills;
- cron definitions, outputs, and logs;
- backups and snapshots;
- caches and temporary files;
- local runtimes such as Node, LSP, virtual environments, or generated workspaces.

Use metadata and aggregate sizes first. Do not read credentials, customer data, session bodies, or unrelated user directories merely to calculate storage.

## Classification

Classify candidates as:

1. **Preserve** — config, credentials, memories, libraries, active sessions, source, and unique artifacts.
2. **Review** — old backups, cron outputs, logs, generated exports, and unknown workspaces.
3. **Regenerable** — documented caches and dependency/runtime copies that can be recreated.

Never infer that a folder is safe to delete from its name alone. Check ownership, references, active processes, symlinks, and whether the runtime is shared.

## Cleanup plan

Default to a dry-run table with path category, size, reason, risk, and recovery route. Require explicit approval before deletion. Quarantine or archive before permanent removal when practical, then remeasure and verify affected profiles still load.
