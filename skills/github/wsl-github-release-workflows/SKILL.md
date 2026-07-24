---
name: wsl-github-release-workflows
description: "Use when creating repositories or releases from WSL with Windows GitHub CLI available; preserve auth safety and verify every remote side effect."
version: 1.0.0
author: bumboo / Hermes Skill Library contributors
license: MIT
metadata:
  hermes:
    tags: [github, wsl, release, gh-cli]
    related_skills: [local-code-change-workflow, public-skill-library-maintenance]
---

# WSL GitHub Release Workflows

## Preflight

1. Inspect `git status`, current branch, upstream, and remotes.
2. Verify GitHub CLI authentication without printing tokens.
3. Confirm owner, repository, visibility, default branch, and whether the release is source-only or includes binaries.
4. Require explicit approval for creation, push, publication, release, or visibility changes.

## WSL pattern

If Linux `gh` is unavailable, invoke authenticated Windows `gh.exe` through PowerShell. Avoid passing WSL UNC paths to commands that require a native Git repository; create the remote separately, then use Linux Git for the local repository.

If HTTPS Git cannot reach the Windows credential store, use a short-lived askpass helper sourced from authenticated CLI output. Never print the token and remove the helper immediately.

## Verification

After push or publication, verify:

- remote branch points to the intended commit;
- repository visibility and default branch;
- tag and release metadata;
- every expected asset and checksum;
- a raw file or release URL returns the intended content.

Treat repository creation, push, tag, release creation, and asset upload as separate states.
