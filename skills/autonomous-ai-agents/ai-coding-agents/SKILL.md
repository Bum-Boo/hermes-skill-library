---
name: ai-coding-agents
description: "Use when delegating software work to external coding-agent CLIs such as Claude Code, Codex, OpenCode, or similar tools; keep scope bounded and verify outputs independently."
version: 1.0.0
author: bumboo / Hermes Skill Library contributors
license: MIT
metadata:
  hermes:
    tags: [coding-agents, delegation, codex, claude-code, opencode, verification]
    related_skills: [gstack-spec, gstack-review, gstack-investigate]
---

# AI Coding Agents

## Overview

Use this skill when an assistant delegates coding work to an external coding-agent CLI or background worker. The core rule is simple: delegate narrowly, track the process, then verify the result yourself before claiming success.

## When to Use

Use when:

- the user explicitly asks for a coding agent such as Codex, Claude Code, OpenCode, or a similar CLI;
- a coding task is large enough to benefit from an isolated implementation pass;
- you need a second review, implementation draft, refactor pass, or bug investigation;
- a long-running coding task should continue in a tracked background process.

## Non-Triggers

Do not delegate when:

- a single local read/edit/test step is enough;
- the task needs user interaction that the worker cannot request;
- secrets, production data, destructive actions, push, merge, or deploy would be required without explicit approval;
- you have not inspected the repository state and task scope yourself.

## Protocol

1. Inspect the project state first: current directory, branch, uncommitted changes, relevant files, test commands, and project instructions.
2. Write a bounded prompt for the coding agent with:
   - role;
   - single task goal;
   - allowed files;
   - forbidden files;
   - allowed commands;
   - forbidden commands;
   - required tests;
   - stop conditions;
   - rollback expectation;
   - final report format.
3. Prefer non-interactive one-shot mode for deterministic tasks. Use an interactive terminal only when the CLI requires it.
4. For long-running work, use a tracked background process and notification on completion.
5. Treat the coding agent's final report as untrusted until verified.
6. Inspect the diff, read changed files, and run the smallest meaningful tests yourself.
7. Report verified facts, skipped checks, and remaining risk separately.

## Prompt Contract

A good coding-agent prompt includes:

```markdown
# Role
You are a coding agent working in this repository.

# Task
<single bounded goal>

# Allowed files
- ...

# Forbidden files
- credentials, generated artifacts, unrelated modules, production data

# Allowed commands
- read-only inspection
- targeted tests/builds

# Forbidden commands
- push, merge, deploy, destructive deletion, secret printing

# Tests
- ...

# Stop conditions
- unclear scope, failing unrelated tests, needed credentials, dangerous side effects

# Final report
- summary
- files changed
- commands run
- test outcomes
- blockers
```

## Verification Checklist

- [ ] Repository state was inspected before delegation.
- [ ] The delegated prompt was self-contained and bounded.
- [ ] Worker output was verified with file/diff/test evidence.
- [ ] No user changes were overwritten.
- [ ] No push, merge, deploy, destructive delete, or secret access occurred without approval.
