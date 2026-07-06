---
name: gstack-safe
description: "Use when choosing a safe evidence-first workflow for spec, review, or investigation tasks without assuming browser access, deployment rights, cookies, or telemetry hooks."
version: 1.0.0
author: Hermes Community Skills contributors
license: MIT
metadata:
  hermes:
    tags: [gstack, safety, routing, spec, review, investigation]
    related_skills: [gstack-spec, gstack-review, gstack-investigate]
---

# gstack-safe

## Overview

Use this as the umbrella router for a conservative, evidence-first workflow family. It helps an agent decide whether to write a spec, review a proposed change, or investigate a failure before editing.

## When to Use

Use when a request needs one of these modes:

- **Spec**: the goal is unclear, broad, or not yet ready for implementation.
- **Review**: the user asks whether a plan, prompt, diff, or design is safe and complete.
- **Investigation**: something failed and the root cause is not known.

## Non-Triggers

Do not use this skill to bypass normal safety requirements. It does not grant permission to:

- deploy, publish, push, merge, or delete;
- access private accounts, cookies, production data, or credentials;
- run browser actions against a user account;
- claim success without verifying current evidence.

## Routing

1. If the user wants a bounded implementation plan, load `gstack-spec`.
2. If the user wants critique or risk analysis, load `gstack-review`.
3. If the user provides errors, logs, failing tests, or unclear behavior, load `gstack-investigate`.
4. If the request includes external side effects, stop and ask for explicit approval or route to a more specific skill.

## Default Guardrails

- Inspect current evidence before proposing changes.
- Separate facts, assumptions, and recommendations.
- Prefer small reversible steps.
- Keep destructive or externally visible actions behind explicit approval.
- Report what was verified and what remains unknown.

## Output Contract

When used as a router, respond with:

- selected workflow;
- reason for the selection;
- required inputs, if any;
- immediate next safe step.
