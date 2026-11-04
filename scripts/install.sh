#!/usr/bin/env bash
#
# Install engineering skills into Claude Code, Codex, or DeepSeek Harness.
# Usage:
#   ./scripts/install.sh [target_dir]
#
# Defaults:
#   - DeepSeek Harness: ~/.dsh/skills
#   - Claude Code:      ~/.claude/skills
#   - Codex:            ${CODEX_HOME:-~/.codex}/skills

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"

# Detect environment or accept first argument
if [ $# -ge 1 ]; then
  TARGET_DIR="$1"
elif [ -d "$HOME/.dsh/skills" ]; then
  TARGET_DIR="$HOME/.dsh/skills"
elif [ -d "$HOME/.claude/skills" ]; then
  TARGET_DIR="$HOME/.claude/skills"
else
  TARGET_DIR="${CODEX_HOME:-$HOME/.codex}/skills"
fi

mkdir -p "$TARGET_DIR"

echo "Installing skills from $REPO_ROOT/skills into $TARGET_DIR..."

installed_count=0
for skill_dir in "$REPO_ROOT"/skills/*/; do
  if [ -d "$skill_dir" ]; then
    skill_name="$(basename "$skill_dir")"
    dest_dir="$TARGET_DIR/$skill_name"
    mkdir -p "$dest_dir"
    cp -R "$skill_dir." "$dest_dir/"
    echo "  ✓ $skill_name"
    installed_count=$((installed_count + 1))
  fi
done

echo "Successfully installed $installed_count skills into $TARGET_DIR."
