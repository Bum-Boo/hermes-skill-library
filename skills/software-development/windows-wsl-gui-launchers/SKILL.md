---
name: windows-wsl-gui-launchers
description: "Use when creating or troubleshooting Windows launchers for WSL GUI, Electron, browser, or local app processes."
version: 1.0.0
author: Hermes Community Skills contributors
license: MIT
metadata:
  hermes:
    tags: [windows, wsl, gui, launcher, electron, startup]
    related_skills: [windows-wsl-path-translation]
---

# Windows / WSL GUI Launchers

## Overview

Use this skill to make Windows-friendly launchers for applications that actually run inside WSL. The goal is a reliable launcher that does not leave stray console windows and can be verified without modifying Windows Startup by default.

## When to Use

Use when:

- the user wants a Windows shortcut for a WSL app;
- a `.cmd`, `.ps1`, `.vbs`, or `.lnk` wrapper fails;
- a GUI/Electron app starts only from a WSL shell;
- the user wants hidden or minimized launch behavior.

## Hard Gates

- Do not add or modify Windows Startup entries without explicit approval.
- Do not kill unrelated processes.
- Do not hardcode private user paths when a relative or discovered path is safer.
- Verify the command starts the intended app before creating hidden wrappers.

## Protocol

1. Identify the WSL distro, app command, working directory, and required environment.
2. Test the app command directly in WSL.
3. Create a visible launcher first for debugging.
4. If requested, wrap it with a hidden/minimized Windows launcher.
5. Verify the launcher starts the app and exits or stays resident as expected.
6. Report how to remove the launcher.

## Common Patterns

A Windows command can call WSL like this:

```cmd
wsl.exe -d <DistroName> --cd <LinuxWorkingDirectory> -- <command>
```

A hidden launcher can use a small VBScript wrapper that runs a `.cmd` file with window style `0`. Keep the script generic and avoid embedding secrets.

## Verification Checklist

- [ ] Direct WSL command works.
- [ ] Windows wrapper launches the same command.
- [ ] No unintended console window remains, if hidden mode was requested.
- [ ] The user knows where the launcher file is.
- [ ] Rollback/removal path is documented.
