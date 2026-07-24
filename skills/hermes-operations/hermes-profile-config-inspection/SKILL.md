---
name: hermes-profile-config-inspection
description: "Use when inspecting or changing a Hermes profile configuration; distinguish active settings from defaults, protect secrets, and verify disk and live state separately."
version: 1.0.0
author: bumboo / Hermes Skill Library contributors
license: MIT
metadata:
  hermes:
    tags: [hermes, profiles, config, troubleshooting]
    related_skills: [hermes-profile-context-diet, hermes-profile-storage-audit]
---

# Hermes Profile Config Inspection

## Use this when

A profile has surprising settings, missing tools, provider failures, or a requested narrow configuration change.

## Workflow

1. Locate the target profile and resolve symlinks before reporting paths.
2. Read only the relevant configuration block. Never print credential values.
3. Classify each value as active selection, available preset/default, or generated scaffold.
4. Check platform-specific tool exposure before concluding a tool is absent.
5. Back up the configuration before an approved edit and change only the named key.
6. For maps and lists, verify the persisted YAML type; CLI setters may store JSON-looking input as a string.
7. Run the profile-scoped configuration check and feature-level command.
8. Report separately: on-disk state, fresh CLI behavior, and live gateway behavior.

## Provider and gateway diagnosis

A running gateway can still hold stale authentication. Inspect safe error classes and timestamps without displaying tokens. Re-authenticate profiles independently rather than copying refresh tokens. A successful CLI request does not prove the long-running gateway reloaded credentials; compare process start time with relevant file modification times and test the original channel after an approved restart.

## Stop conditions

Stop for secrets, broad profile rewrites, destructive cleanup, another account, or a gateway restart that was not approved. Do not claim a live fix from configuration validation alone.
