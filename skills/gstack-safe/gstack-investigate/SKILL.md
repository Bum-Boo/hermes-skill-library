---
name: gstack-investigate
description: "Use when diagnosing errors, regressions, failed commands, failing tests, or unclear behavior before proposing a fix."
version: 1.0.0
author: Hermes Community Skills contributors
license: MIT
metadata:
  hermes:
    tags: [debugging, investigation, root-cause, evidence]
    related_skills: [gstack-safe, gstack-review]
---

# gstack-investigate

## Overview

Investigate first, fix second. The goal is to identify the smallest proven cause before changing files or settings.

## When to Use

Use when:

- a command, test, build, deployment, or automation failed;
- behavior changed unexpectedly;
- logs are noisy or contradictory;
- someone claims a cause but evidence is incomplete.

## Protocol

1. Capture the exact symptom and expected behavior.
2. Collect minimal current evidence: command, error, environment, recent changes, relevant logs.
3. Reproduce when safe and cheap.
4. Form competing hypotheses.
5. Test hypotheses one at a time.
6. Identify the smallest root cause supported by evidence.
7. Propose the minimal fix and verification command.
8. Stop before risky changes unless the user approves them.

## Evidence Table

Use this structure when useful:

| Evidence | Source | Meaning | Confidence |
|---|---|---|---|
| ... | ... | ... | high/medium/low |

## Stop Conditions

Stop and report instead of guessing when:

- the next step needs secrets, private account access, production data, or destructive changes;
- reproduction requires external cost or public side effects;
- evidence contradicts the leading hypothesis;
- the affected system is outside the allowed scope.

## Output Format

```markdown
## Symptom
...

## Evidence gathered
- ...

## Likely cause
...

## Ruled out
- ...

## Minimal fix
...

## Verification
...

## Remaining uncertainty
...
```
