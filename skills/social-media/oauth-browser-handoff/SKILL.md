---
name: oauth-browser-handoff
description: "Use when a CLI, local service, or agent running in headless/remote/WSL context needs the human user to complete OAuth consent safely in a browser."
version: 1.0.0
author: Hermes Community Skills contributors
license: MIT
metadata:
  hermes:
    tags: [oauth, auth, browser-handoff, credentials, headless]
    related_skills: []
---

# OAuth Browser Handoff

## Overview

Use this skill when an agent can prepare an OAuth flow but the human must approve consent in a browser. The agent should protect secrets, avoid copying tokens through chat, and verify the result with sanitized output.

## When to Use

Use when:

- a CLI prints an OAuth authorization URL;
- WSL or a remote shell cannot open the browser automatically;
- a provider requires user consent, device code, or local callback confirmation;
- a local app needs an OAuth client file or callback listener.

## Non-Triggers

Do not use this skill to collect passwords, OAuth client secrets, refresh tokens, browser cookies, or private session files through chat.

## Protocol

1. Identify the provider, CLI/app, callback URL, and required scopes.
2. Run safe preflight checks without printing secret values.
3. Start the local callback listener only if needed.
4. Present the user with the exact browser action required.
5. Ask the user to complete consent in the provider UI.
6. After consent, verify authentication with a command that redacts tokens.
7. Store only sanitized status and setup notes.

## User-Facing Instruction Template

```markdown
## Browser step
Open this URL in your normal browser and approve the requested scopes:
<authorization URL or device-code page>

## Code, if shown by the provider
`<device-code>`

Do not paste passwords, client secrets, refresh tokens, or cookies into chat.
```

## Secret Handling Rules

- Do not print real token values.
- Do not save secrets in README files, skills, logs, or issue bodies.
- If a command emits secrets, summarize that a secret was produced and where it was stored locally.
- Prefer provider-supported secure storage, OS keychains, or environment variables over plaintext files.

## Verification Checklist

- [ ] The requested scopes are understood.
- [ ] The user completed consent in the provider UI.
- [ ] A sanitized auth-status command succeeded.
- [ ] No secrets were pasted into chat or committed to files.
- [ ] Any listener process was stopped or documented.
