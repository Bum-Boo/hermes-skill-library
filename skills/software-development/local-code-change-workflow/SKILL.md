---
name: local-code-change-workflow
description: "Use when editing an approved local codebase; inspect first, preserve user changes, make a narrow reversible patch, and verify with real execution."
version: 1.0.0
author: bumboo / Hermes Skill Library contributors
license: MIT
metadata:
  hermes:
    tags: [coding, local-files, testing, safety]
    related_skills: [verification-before-completion, wsl-github-release-workflows]
---

# Local Code Change Workflow

## Contract

1. Confirm the approved project root and task boundary.
2. Inspect repository status, relevant source, tests, and current behavior before editing.
3. Preserve unrelated tracked and untracked user changes.
4. Prefer the smallest targeted, reversible change over a rewrite.
5. Run the smallest meaningful test, lint, build, or smoke check that exercises the change.
6. Inspect the resulting diff, including new untracked files.
7. Report changed behavior, evidence, remaining risk, and rollback route.

## Approval boundaries

Local implementation approval does not imply permission to commit, push, merge, deploy, publish, delete data, use credentials, incur cost, or alter production. Ask only when the work crosses one of those boundaries.

## Failure handling

Fix ordinary in-scope technical failures and rerun the check. Stop when a required action expands scope, needs secrets or privilege, risks irreversible loss, or cannot be verified. Never replace a blocked execution path with invented output.
