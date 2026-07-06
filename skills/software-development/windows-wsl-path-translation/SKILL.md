---
name: windows-wsl-path-translation
description: "Use when reporting, validating, or troubleshooting file paths between WSL/Linux shells and Windows Explorer."
version: 1.0.0
author: Hermes Community Skills contributors
license: MIT
metadata:
  hermes:
    tags: [windows, wsl, paths, filesystem, reporting]
    related_skills: [windows-wsl-gui-launchers]
---

# Windows / WSL Path Translation

## Overview

Use this skill when an agent runs in WSL but the human user needs a path they can open in Windows Explorer, a Windows app, or a browser file picker.

## When to Use

Use when:

- the user asks where a generated file is on Windows;
- a path may be a symlink inside WSL;
- a Windows application must open a file created by Linux tools;
- a path starts with `/mnt/<drive>/`, `~`, or another Linux-only form.

## Protocol

1. Resolve the Linux path to an absolute path.
2. If the path may include symlinks, resolve the real path.
3. Convert to a Windows path with `wslpath -w` when available.
4. Prefer the Windows Explorer path in the user-facing answer.
5. Include the WSL path only as secondary technical detail.
6. If the path does not exist, say so and report the closest existing parent.

## Command Patterns

```bash
realpath <path>
wslpath -w <absolute-linux-path>
```

For a WSL home path, Windows Explorer usually needs the UNC form returned by `wslpath -w`, not a guessed `C:\Users\...` path.

## Output Format

```markdown
## Windows Explorer path
`\\wsl.localhost\...`

## WSL path
`/home/...`

## Status
Exists / missing / parent exists
```

## Safety Notes

- Do not scan a whole Windows user directory to guess a username unless necessary.
- Do not expose private directory names beyond the path the user asked about.
- Do not modify files while translating paths.
