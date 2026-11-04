#!/usr/bin/env bash
#
# Install, preview, or remove engineering skills for Claude Code, Codex, or DeepSeek Harness.
# Usage:
#   ./scripts/install.sh [options] [target_dir]
#
# Options:
#   -n, --dry-run     Show what would be installed/uninstalled without modifying disk.
#   -u, --uninstall   Remove the engineering skills from target directory.
#   -f, --force       Overwrite existing skills without confirmation prompt.
#   -h, --help        Show this help message.
#
# Target defaults:
#   1. DeepSeek Harness: ~/.dsh/skills (if ~/.dsh/skills exists)
#   2. Claude Code:      ~/.claude/skills (if ~/.claude/skills exists)
#   3. Codex:            ${CODEX_HOME:-~/.codex}/skills

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"

DRY_RUN=0
UNINSTALL=0
FORCE=0
TARGET_DIR=""

while [[ $# -gt 0 ]]; do
  case "$1" in
    -n|--dry-run)
      DRY_RUN=1
      shift
      ;;
    -u|--uninstall)
      UNINSTALL=1
      shift
      ;;
    -f|--force)
      FORCE=1
      shift
      ;;
    -h|--help)
      echo "Usage: $0 [options] [target_dir]"
      echo ""
      echo "Options:"
      echo "  -n, --dry-run     Preview operations without writing to disk."
      echo "  -u, --uninstall   Uninstall skills from target directory."
      echo "  -f, --force       Overwrite existing target files without prompting."
      echo "  -h, --help        Show help."
      exit 0
      ;;
    *)
      TARGET_DIR="$1"
      shift
      ;;
  esac
done

if [ -z "$TARGET_DIR" ]; then
  if [ -d "$HOME/.dsh/skills" ]; then
    TARGET_DIR="$HOME/.dsh/skills"
  elif [ -d "$HOME/.claude/skills" ]; then
    TARGET_DIR="$HOME/.claude/skills"
  else
    TARGET_DIR="${CODEX_HOME:-$HOME/.codex}/skills"
  fi
fi

if [ $UNINSTALL -eq 1 ]; then
  echo "Mode: UNINSTALL from $TARGET_DIR"
  if [ ! -d "$TARGET_DIR" ]; then
    echo "Target directory '$TARGET_DIR' does not exist. Nothing to uninstall."
    exit 0
  fi

  count=0
  for skill_dir in "$REPO_ROOT"/skills/*/; do
    skill_name="$(basename "$skill_dir")"
    dest="$TARGET_DIR/$skill_name"
    if [ -d "$dest" ]; then
      if [ $DRY_RUN -eq 1 ]; then
        echo "  [DRY-RUN] Would remove $dest"
      else
        rm -rf "$dest"
        echo "  ✓ Removed $skill_name"
      fi
      count=$((count + 1))
    fi
  done
  echo "Uninstall finished: $count skill(s) processed."
  exit 0
fi

echo "Mode: INSTALL into $TARGET_DIR"
if [ $DRY_RUN -eq 1 ]; then
  echo "  (DRY-RUN mode enabled: no files will be written)"
else
  mkdir -p "$TARGET_DIR"
fi

installed_count=0
for skill_dir in "$REPO_ROOT"/skills/*/; do
  if [ -d "$skill_dir" ]; then
    skill_name="$(basename "$skill_dir")"
    dest_dir="$TARGET_DIR/$skill_name"

    if [ -d "$dest_dir" ] && [ $FORCE -eq 0 ] && [ $DRY_RUN -eq 0 ]; then
      if [ -t 0 ]; then
        read -r -p "  ! Skill '$skill_name' already exists at '$dest_dir'. Overwrite? [y/N]: " confirm
        if [[ ! "$confirm" =~ ^[yY]$ ]]; then
          echo "    Skipping $skill_name."
          continue
        fi
      else
        echo "  ✗ Error: Skill directory '$dest_dir' already exists. Use --force to overwrite." >&2
        exit 1
      fi
    fi

    if [ $DRY_RUN -eq 1 ]; then
      echo "  [DRY-RUN] Would copy $(basename "$skill_dir") -> $dest_dir"
    else
      mkdir -p "$dest_dir"
      cp -R "$skill_dir." "$dest_dir/"
      echo "  ✓ $skill_name"
    fi
    installed_count=$((installed_count + 1))
  fi
done

if [ $DRY_RUN -eq 1 ]; then
  echo "Dry-run complete. $installed_count skill(s) ready to install."
else
  echo "Successfully installed $installed_count skills into $TARGET_DIR."
fi
