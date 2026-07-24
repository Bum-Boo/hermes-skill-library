#!/usr/bin/env bash
set -euo pipefail

COLLECTION="${1:-}"
TARGET="${2:-$HOME/.hermes/skills}"
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

if [[ -z "$COLLECTION" ]]; then
  echo "Usage: $0 <collection> [target-skills-dir]" >&2
  echo "Collections: gstack-safe, agent-engineering, research-workflows, comfyui-image-workflows, wsl-operator, oauth-browser-handoff, profile-context-diet, hermes-profile-operations, local-development-safety, github-publishing, telegram-operator, computer-use-safety" >&2
  exit 2
fi

mkdir -p "$TARGET"
case "$COLLECTION" in
  gstack-safe)
    mkdir -p "$TARGET/gstack-safe"
    cp -R "$ROOT/skills/gstack-safe/." "$TARGET/gstack-safe/"
    ;;
  agent-engineering)
    mkdir -p "$TARGET/autonomous-ai-agents"
    cp -R "$ROOT/skills/autonomous-ai-agents/ai-coding-agents" "$TARGET/autonomous-ai-agents/"
    ;;
  research-workflows)
    mkdir -p "$TARGET/research"
    cp -R "$ROOT/skills/research/research-intake-and-monitoring" "$TARGET/research/"
    cp -R "$ROOT/skills/research/ml-research-and-evaluation-workflows" "$TARGET/research/"
    ;;
  comfyui-image-workflows)
    mkdir -p "$TARGET/creative"
    cp -R "$ROOT/skills/creative/comfyui-image-workflows" "$TARGET/creative/"
    ;;
  wsl-operator)
    mkdir -p "$TARGET/software-development"
    cp -R "$ROOT/skills/software-development/windows-wsl-path-translation" "$TARGET/software-development/"
    cp -R "$ROOT/skills/software-development/windows-wsl-gui-launchers" "$TARGET/software-development/"
    ;;
  oauth-browser-handoff)
    mkdir -p "$TARGET/social-media"
    cp -R "$ROOT/skills/social-media/oauth-browser-handoff" "$TARGET/social-media/"
    ;;
  profile-context-diet)
    mkdir -p "$TARGET/autonomous-ai-agents"
    cp -R "$ROOT/skills/autonomous-ai-agents/hermes-profile-context-diet" "$TARGET/autonomous-ai-agents/"
    ;;
  hermes-profile-operations)
    mkdir -p "$TARGET/hermes-operations" "$TARGET/autonomous-ai-agents"
    cp -R "$ROOT/skills/hermes-operations/hermes-profile-config-inspection" "$TARGET/hermes-operations/"
    cp -R "$ROOT/skills/hermes-operations/hermes-profile-storage-audit" "$TARGET/hermes-operations/"
    cp -R "$ROOT/skills/autonomous-ai-agents/hermes-profile-context-diet" "$TARGET/autonomous-ai-agents/"
    ;;
  local-development-safety)
    mkdir -p "$TARGET/software-development"
    cp -R "$ROOT/skills/software-development/local-code-change-workflow" "$TARGET/software-development/"
    cp -R "$ROOT/skills/software-development/verification-before-completion" "$TARGET/software-development/"
    ;;
  github-publishing)
    mkdir -p "$TARGET/github"
    cp -R "$ROOT/skills/github/wsl-github-release-workflows" "$TARGET/github/"
    cp -R "$ROOT/skills/github/public-skill-library-maintenance" "$TARGET/github/"
    ;;
  telegram-operator)
    mkdir -p "$TARGET/communication"
    cp -R "$ROOT/skills/communication/telegram-rich-message-reporting" "$TARGET/communication/"
    ;;
  computer-use-safety)
    mkdir -p "$TARGET/computer-use"
    cp -R "$ROOT/skills/computer-use/computer-use-background-safety" "$TARGET/computer-use/"
    ;;
  *)
    echo "Unknown collection: $COLLECTION" >&2
    exit 2
    ;;
esac

echo "Installed collection '$COLLECTION' into: $TARGET"
echo "Run: hermes skills list"
