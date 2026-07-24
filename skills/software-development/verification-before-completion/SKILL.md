---
name: verification-before-completion
description: "Use immediately before claiming work is done, fixed, installed, published, or safe; require fresh evidence that directly supports the exact claim."
version: 1.0.0
author: bumboo / Hermes Skill Library contributors
license: MIT
metadata:
  hermes:
    tags: [verification, evidence, testing, quality]
    related_skills: [local-code-change-workflow]
---

# Verification Before Completion

## Rule

Claim only what was freshly verified. Previous output, source markers, another agent's report, HTTP 200, or a successful write are not substitutes for behavior-level evidence.

## Claim-to-evidence examples

- Tests pass → fresh test output and exit status.
- Build works → fresh build output and produced artifact inspection.
- File exists → read or stat the expected path.
- Bug fixed → original reproduction or regression check now passes.
- Installed → the target runtime lists or loads it.
- Published → remote URL, ID, branch, release, or destination readback.
- UI fixed → exercise the real interaction and inspect the rendered state at relevant viewports.

## Protocol

1. State the exact intended claim.
2. Select the smallest direct check.
3. Run it after the final change.
4. Inspect status and relevant output.
5. Narrow the claim if evidence is partial.
6. If verification fails, fix and rerun or report the blocker honestly.

Keep disk/config, fresh-process, and long-running live-service state separate whenever stale runtime state is possible.
