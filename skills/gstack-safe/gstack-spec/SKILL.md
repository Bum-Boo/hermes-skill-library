---
name: gstack-spec
description: "Use when turning a vague or risky project request into a bounded, reviewable implementation specification before any code changes."
version: 1.0.0
author: Hermes Community Skills contributors
license: MIT
metadata:
  hermes:
    tags: [specification, planning, scope, safety]
    related_skills: [gstack-safe, gstack-review]
---

# gstack-spec

## Overview

Use this skill to convert an ambiguous request into a precise implementation spec. The spec should be small enough to review, test, and roll back.

## When to Use

Use when:

- the requested change affects multiple files or systems;
- the requirements are incomplete;
- the task may have security, privacy, data, deployment, or cost impact;
- the user asks for a plan, architecture, or implementation prompt.

## Non-Triggers

Do not use this to delay a trivial safe edit. If the task is already clear, local, reversible, and testable, proceed with the normal local change workflow.

## Protocol

1. Restate the goal in one sentence.
2. List known facts from current evidence.
3. List assumptions separately.
4. Identify affected components and boundaries.
5. Define what is explicitly out of scope.
6. Break work into small tasks with verification for each task.
7. Define safety gates and approval points.
8. Define rollback steps.
9. End with open questions only if they block the next safe step.

## Spec Template

```markdown
# Spec: <title>

## Goal
<one sentence>

## Current evidence
- ...

## Assumptions
- ...

## Scope
### In scope
- ...

### Out of scope
- ...

## Implementation plan
1. ...

## Tests / verification
- ...

## Safety gates
- ...

## Rollback
- ...

## Open questions
- ...
```

## Verification Checklist

- [ ] The goal is single-purpose.
- [ ] Scope boundaries are explicit.
- [ ] Every implementation step has a verification step.
- [ ] Side effects require approval.
- [ ] Rollback is possible.
