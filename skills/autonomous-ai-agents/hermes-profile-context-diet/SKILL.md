---
name: hermes-profile-context-diet
description: "Use when auditing or reducing a Hermes profile's prompt/context footprint, memories, enabled skills, or role text while preserving durable knowledge."
version: 1.0.0
author: Hermes Community Skills contributors
license: MIT
metadata:
  hermes:
    tags: [hermes, profiles, context, memory, skills, optimization]
    related_skills: []
---

# Hermes Profile Context Diet

## Overview

Use this skill to reduce the amount of information injected into a Hermes profile's prompt while preserving useful procedures and durable facts. Measure first. Do not delete knowledge just because a folder is large.

## When to Use

Use when:

- a profile prompt is too long;
- many skills are enabled but rarely used;
- memories contain stale task progress;
- profile role text repeats facts stored elsewhere;
- the user asks to slim, audit, consolidate, or reduce token cost.

## Non-Triggers

Do not use this as a general cleanup script. Disk size and prompt weight are different problems. A large archived file may be harmless if it is not injected into the prompt.

## Hard Gates

- Back up or record the original state before edits.
- Do not remove credentials or config blindly.
- Do not delete a skill without checking whether jobs, prompts, or workflows reference it.
- Do not move durable procedures into ordinary memory; use skills or references.
- Do not store temporary task progress in long-term memory.

## Protocol

1. Identify what is injected into the current profile prompt: role text, user profile, memory, enabled skills, and tool schemas.
2. Separately list disk-only bulk: archives, references, generated files, logs, and assets.
3. Classify entries:
   - durable user preference;
   - stable environment fact;
   - reusable procedure;
   - temporary task progress;
   - obsolete or duplicate content.
4. Propose a diet plan before editing.
5. Consolidate repeated procedures into class-level skills or references.
6. Shorten memories into compact declarative facts.
7. Archive rather than delete when unsure.
8. Verify the profile still loads the needed skills and remembers key preferences.

## Recommended Report

```markdown
## Measured prompt-weight items
- ...

## Disk-only bulk
- ...

## Safe reductions
- ...

## Needs approval
- ...

## Do not remove
- ...

## Verification plan
- ...
```

## Verification Checklist

- [ ] The audit distinguishes prompt injection from disk storage.
- [ ] Proposed removals are reversible.
- [ ] Durable preferences are preserved.
- [ ] Reusable procedures are skills, not long memory entries.
- [ ] Temporary task progress is removed or left in session history, not active memory.
- [ ] The final profile still has the skills needed for its role.
