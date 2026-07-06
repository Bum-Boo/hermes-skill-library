---
name: gstack-review
description: "Use when reviewing a plan, prompt, diff, architecture, or proposed change for correctness, safety, testability, and hidden assumptions."
version: 1.0.0
author: Hermes Community Skills contributors
license: MIT
metadata:
  hermes:
    tags: [review, risk, correctness, safety, testability]
    related_skills: [gstack-safe, gstack-spec, gstack-investigate]
---

# gstack-review

## Overview

Review the artifact from multiple angles before implementation or approval. Prefer evidence-backed findings over style opinions.

## When to Use

Use when the user asks:

- “Is this plan safe?”
- “Review this Codex prompt.”
- “Check this diff before I run it.”
- “What could go wrong?”

## Protocol

1. Identify the artifact being reviewed and its intended outcome.
2. Check for missing evidence or stale assumptions.
3. Review correctness and edge cases.
4. Review safety, privacy, credentials, and destructive side effects.
5. Review testability and rollback.
6. Separate blocking findings from non-blocking suggestions.
7. Recommend a smaller safer scope if needed.

## Output Format

```markdown
## Verdict
Proceed / revise first / blocked

## Blocking findings
- ...

## Non-blocking suggestions
- ...

## Evidence checked
- ...

## Safer next step
- ...
```

## Review Rules

- Do not approve work that cannot be verified.
- Do not approve access to secrets or production data without explicit authority.
- Do not rely on a worker's self-report when a file, command, URL, or API can be checked.
- If the artifact is a prompt for a coding agent, require allowed files, forbidden files, allowed commands, forbidden commands, tests, rollback, and stop conditions.
