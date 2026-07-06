#!/usr/bin/env bash
set -euo pipefail

COLLECTION="${1:-}"
TARGET="${2:-$HOME/.hermes/skills}"
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

if [[ -z "$COLLECTION" ]]; then
  echo "Usage: $0 <collection> [target-skills-dir]" >&2
  echo "Collections: gstack-safe, wsl-operator, oauth-browser-handoff, profile-context-diet" >&2
  exit 2
fi

mkdir -p "$TARGET"
case "$COLLECTION" in
  gstack-safe)
    mkdir -p "$TARGET/gstack-safe"
    cp -R "$ROOT/skills/gstack-safe/." "$TARGET/gstack-safe/"
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
  *)
    echo "Unknown collection: $COLLECTION" >&2
    exit 2
    ;;
esac

echo "Installed collection '$COLLECTION' into: $TARGET"
echo "Run: hermes skills list"
