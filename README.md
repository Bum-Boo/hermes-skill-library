# Hermes Skill Library

A curated skill library for Hermes Agent-style assistants.

This repository is intended to live at:

```text
https://github.com/bumboo/hermes-skill-library
```

The repo is a library, not a single-purpose package. Keep adding focused skill folders and updating the catalog README as the library grows.

## Current collections

| Collection | Use when | Skills |
|---|---|---|
| [`gstack-safe`](collections/gstack-safe/) | You need evidence-first spec, review, or investigation workflows before editing. | `gstack-safe`, `gstack-spec`, `gstack-review`, `gstack-investigate` |
| [`agent-engineering`](collections/agent-engineering/) | You delegate software work to coding-agent CLIs and need bounded prompts plus verification. | `ai-coding-agents` |
| [`research-workflows`](collections/research-workflows/) | You collect sources, monitor research inputs, or manage ML evaluation evidence. | `research-intake-and-monitoring`, `ml-research-and-evaluation-workflows` |
| [`comfyui-image-workflows`](collections/comfyui-image-workflows/) | You generate, batch, or troubleshoot images with ComfyUI workflows. | `comfyui-image-workflows` |
| [`wsl-operator`](collections/wsl-operator/) | Hermes runs inside WSL and the user needs Windows paths or launchers. | `windows-wsl-path-translation`, `windows-wsl-gui-launchers` |
| [`oauth-browser-handoff`](collections/oauth-browser-handoff/) | A headless/WSL/remote agent needs the user to complete OAuth in a browser. | `oauth-browser-handoff` |
| [`profile-context-diet`](collections/profile-context-diet/) | A Hermes profile has too much prompt weight, stale memory, or skill sprawl. | `hermes-profile-context-diet` |
| [`hermes-profile-operations`](collections/hermes-profile-operations/) | You operate multiple Hermes profiles and need safe config, storage, and context maintenance. | `hermes-profile-config-inspection`, `hermes-profile-storage-audit`, `hermes-profile-context-diet` |
| [`local-development-safety`](collections/local-development-safety/) | You need a narrow local code change with fresh completion evidence. | `local-code-change-workflow`, `verification-before-completion` |
| [`github-publishing`](collections/github-publishing/) | You publish repositories or skills from WSL and must verify remote state. | `wsl-github-release-workflows`, `public-skill-library-maintenance` |
| [`telegram-operator`](collections/telegram-operator/) | You report agent progress and results through Telegram. | `telegram-rich-message-reporting` |
| [`computer-use-safety`](collections/computer-use-safety/) | You drive desktop applications without stealing focus or skipping verification. | `computer-use-background-safety` |
| [`web-interface-verification`](collections/web-interface-verification/) | A responsive interface fails at tablet widths or mixes hover and touch behavior. | `responsive-touch-interface-verification` |

## Install all skills

Install globally for the current OS user:

```bash
git clone https://github.com/bumboo/hermes-skill-library.git
cd hermes-skill-library
./scripts/install.sh
hermes skills list
```

Install into one Hermes profile only:

```bash
./scripts/install.sh ~/.hermes/profiles/<profile>/skills
hermes --profile <profile> skills list
```

If your Hermes CLI does not support `--profile` for `skills list`, start a chat with that profile and ask it to list or load the installed skill.

## Install one collection only

```bash
./scripts/install-collection.sh gstack-safe
./scripts/install-collection.sh agent-engineering
./scripts/install-collection.sh research-workflows
./scripts/install-collection.sh comfyui-image-workflows
./scripts/install-collection.sh wsl-operator
./scripts/install-collection.sh oauth-browser-handoff
./scripts/install-collection.sh profile-context-diet
./scripts/install-collection.sh hermes-profile-operations
./scripts/install-collection.sh local-development-safety
./scripts/install-collection.sh github-publishing
./scripts/install-collection.sh telegram-operator
./scripts/install-collection.sh computer-use-safety
./scripts/install-collection.sh web-interface-verification
```

For a single profile:

```bash
./scripts/install-collection.sh comfyui-image-workflows ~/.hermes/profiles/<profile>/skills
```

## Repository layout

```text
skills/<category>/<skill-name>/SKILL.md      # installable Hermes skills
collections/<collection>/README.md          # human-facing usage notes by purpose
scripts/install.sh                          # install every skill
scripts/install-collection.sh               # install one purpose-based collection
SECURITY.md
LICENSE
```

## How to add a new skill

1. Create a focused skill folder:

   ```text
   skills/<category>/<skill-name>/SKILL.md
   ```

2. Include valid Hermes skill frontmatter:

   ```yaml
   ---
   name: skill-name
   description: "Use when <trigger>; <behavior>."
   version: 1.0.0
   author: bumboo / Hermes Skill Library contributors
   license: MIT
   metadata:
     hermes:
       tags: [tag1, tag2]
       related_skills: []
   ---
   ```

3. Add a collection README or update an existing one.
4. Update the table in this README.
5. Run the private-info scan below.
6. Test install into a temporary directory before publishing.

## Private information check before publishing

Run from the repository root:

```bash
grep -RInE '(/home/[^ /]+|/mnt/c/Users/[^ /]+|[A-Za-z0-9_]*TOKEN|SECRET|PASSWORD|PRIVATE KEY|chat_id|bot_token)' .
```

Review all matches manually. Safety-warning words are acceptable; real values, private account IDs, private local paths, customer names, and credentials are not.

## Local install verification

```bash
tmpdir="$(mktemp -d)"
./scripts/install.sh "$tmpdir"
find "$tmpdir" -name SKILL.md | sort
```

## Safety policy

Skills in this library should prefer:

- read-only inspection before mutation;
- explicit user approval before publishing, pushing, deploying, deleting, or using credentials;
- small scoped actions with verification;
- source evidence over stale memory;
- redaction of secrets, tokens, cookies, browser profiles, and private data.

## License

MIT. See [`LICENSE`](LICENSE).
