#!/usr/bin/env bash
set -euo pipefail

TARGET="${1:-$HOME/.hermes/skills}"
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

mkdir -p "$TARGET"
cp -R "$ROOT/skills/." "$TARGET/"

echo "Installed all skills into: $TARGET"
echo "Run: hermes skills list"
