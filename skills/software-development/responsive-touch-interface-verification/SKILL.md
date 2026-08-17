---
name: responsive-touch-interface-verification
description: "Use when an interface works on phones and desktops but fails at tablet widths; isolate breakpoint and pointer-mode conflicts, reuse existing touch UI, and verify real interactions."
version: 1.0.0
author: bumboo / Hermes Skill Library contributors
license: MIT
metadata:
  hermes:
    tags: [responsive, tablet, touch, navigation, css, javascript]
    related_skills: [local-code-change-workflow, verification-before-completion]
---

# Responsive Touch Interface Verification

## Use when

Use this workflow when menus, popovers, dropdowns, or global navigation work on phones and desktops but become unreliable on tablets. Do not assume the framework is at fault: first separate the global shell, breakpoints, and input capabilities.

## Core principles

1. Viewport width and input mode are independent. Inspect `(hover)` and `(pointer)` capabilities as well as width breakpoints.
2. Do not leave a tablet as a shrunken desktop when the desktop interaction depends on hover. Reuse the existing touch-oriented menu or accordion where possible.
3. Do not widen every mobile breakpoint. Keep ownership of header, content, and footer behavior separate.
4. Prefer a small extension of an existing interaction contract over a new tablet-only interface.
5. Do not treat CSS source text as proof. Verify loaded CSS rules, computed styles, and click or keyboard state changes.

## Workflow

1. Identify the component or package that owns the failing surface and the assets actually loaded by the page.
2. Read desktop, tablet, and mobile breakpoints together with duplicated DOM branches and hover, click, focus, and keyboard handlers.
3. Check whether `mouseenter`, `mouseleave`, synthetic hover, or focus cleanup reverses a tap-driven state on coarse pointers.
4. Make the smallest change that explicitly assigns both layout mode and interaction mode for the affected capability range.
5. On resize or orientation change, clear state belonging to the mode that is no longer active.
6. Run source-contract tests and JavaScript syntax checks, then verify desktop, tablet, and phone behavior against the rendered page.

## Interaction checks

At minimum, verify:

- the first tablet tap is not lost;
- a second intentional tap follows the documented navigation contract;
- submenu open and close state is predictable;
- Escape, focus movement, and keyboard activation still work on desktop;
- hidden menus do not retain stale `aria-expanded`, focus, or open classes after resize;
- touch-target visibility is based on computed style rather than markup presence alone.

If browser emulation can alter pointer capabilities, test representative combinations such as wide/fine-pointer, tablet/coarse-pointer, and narrow/coarse-pointer. A width-only screenshot is not sufficient interaction evidence.

## Completion criteria

- Desktop hover, click, focus, and keyboard behavior remain intact.
- Tablet taps reliably open and close the intended controls.
- Phone layout remains unchanged unless it was explicitly in scope.
- Rotation or resizing does not leave inaccessible open state behind.
- Build or package checks pass, and unrelated modules are unchanged.
- The final report distinguishes source checks from rendered interaction checks.
