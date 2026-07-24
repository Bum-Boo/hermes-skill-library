---
name: telegram-rich-message-reporting
description: "Use when reporting agent work through Telegram; keep progress compact, format safely, and deliver one evidence-backed final result without leaking internals."
version: 1.0.0
author: bumboo / Hermes Skill Library contributors
license: MIT
metadata:
  hermes:
    tags: [telegram, reporting, markdown, ux]
    related_skills: [verification-before-completion]
---

# Telegram Rich Message Reporting

## Reporting pattern

- Send progress only at meaningful milestones or genuine blockers.
- Keep a progress update to one factual line when possible.
- Avoid raw tool names, internal payloads, credentials, and unnecessary local paths.
- Send one final report containing outcome, verification evidence, and any remaining boundary.

## Formatting

Use short headings, bullets, and compact labeled values. Keep tables small because narrow clients wrap aggressively. Use fenced code only when exact copy/paste text matters. Escape or restructure ambiguous Markdown rather than relying on platform-specific rendering quirks.

For media delivery, provide a descriptive caption and the final verified file, not temporary caches or unverified intermediate output. For long reports, lead with the result and move supporting detail below it.

## Truthfulness

Do not turn queued, submitted, written, or HTTP-accepted states into completed claims. Report uploaded, processed, edited, published, and verified counts separately when they differ.
