# Hermes Skill Library

**English** | [한국어](README.ko.md) | [日本語](README.ja.md) | [中文](README.zh-CN.md)

A curated library of reusable skills for Hermes Agent-style assistants. This is a collection rather than a single-purpose package: install the whole library or select one purpose-based collection.

## Collections

| Collection | Purpose |
|---|---|
| [`gstack-safe`](collections/gstack-safe/) | Evidence-first specification, review, and investigation. |
| [`agent-engineering`](collections/agent-engineering/) | Delegating bounded work to coding-agent CLIs. |
| [`research-workflows`](collections/research-workflows/) | Source intake, monitoring, ML experiments, and evaluation evidence. |
| [`comfyui-image-workflows`](collections/comfyui-image-workflows/) | ComfyUI generation, batching, verification, and troubleshooting. |
| [`wsl-operator`](collections/wsl-operator/) | Windows/WSL paths and GUI launchers. |
| [`oauth-browser-handoff`](collections/oauth-browser-handoff/) | Human browser completion of OAuth from headless, WSL, or remote agents. |
| [`profile-context-diet`](collections/profile-context-diet/) | Reducing stale or excessive Hermes profile context. |
| [`hermes-profile-operations`](collections/hermes-profile-operations/) | Multi-profile configuration, storage, and context maintenance. |
| [`local-development-safety`](collections/local-development-safety/) | Narrow local changes with fresh completion evidence. |
| [`github-publishing`](collections/github-publishing/) | WSL-aware repository and skill publishing with remote verification. |
| [`telegram-operator`](collections/telegram-operator/) | Compact, truthful Telegram progress and result reporting. |
| [`computer-use-safety`](collections/computer-use-safety/) | Background-first desktop control and safe escalation. |
| [`web-interface-verification`](collections/web-interface-verification/) | Responsive, touch, hover, and tablet-width verification. |
| [`repository-maintenance`](collections/repository-maintenance/) | Auditing forks, mirrors, vendored snapshots, and downstream codebases. |

Collection pages list their included skills and usage notes. The machine-readable inventory is in [`catalog.json`](catalog.json).

## Install all skills

```bash
git clone https://github.com/Bum-Boo/hermes-skill-library.git
cd hermes-skill-library
./scripts/install.sh
hermes skills list
```

```bash
# Install for one profile
./scripts/install.sh ~/.hermes/profiles/<profile>/skills
hermes --profile <profile> skills list
```

The default target is `~/.hermes/skills`. If your Hermes CLI does not support `--profile` for `skills list`, start a chat with that profile and ask it to list or load the installed skill.

> The installer copies the library into the target and may replace files with the same paths. Review the source and use an appropriate target before running it.

## Install one collection

```bash
./scripts/install-collection.sh <collection-name>
./scripts/install-collection.sh comfyui-image-workflows ~/.hermes/profiles/<profile>/skills
```

Use a collection name from the table above. The collection installer accepts only names implemented by [`scripts/install-collection.sh`](scripts/install-collection.sh); an unknown name exits with an error.

## Repository layout

```text
skills/<category>/<skill-name>/SKILL.md  Installable skills
collections/<collection>/README.md      Purpose-based collection notes
scripts/install.sh                      Install every skill
scripts/install-collection.sh           Install one collection
catalog.json                            Collection inventory
SECURITY.md                             Security policy
LICENSE                                 MIT license
```

## Contributing safely

Place each skill at `skills/<category>/<skill-name>/SKILL.md` with valid Hermes frontmatter, then add or update its collection documentation and `catalog.json`. Before sharing a change, test installation in a temporary directory and inspect the repository for credentials, private paths, account identifiers, browser profiles, and customer data. Never commit real secret values. See [`SECURITY.md`](SECURITY.md).

## Attribution request

If you share this library or publish derivative work, a courteous mention of **@Bum-Boo** and the [original repository](https://github.com/Bum-Boo/hermes-skill-library) would be appreciated. This is a request for acknowledgement, not an additional or modified license condition.

## License

MIT. See [`LICENSE`](LICENSE).
