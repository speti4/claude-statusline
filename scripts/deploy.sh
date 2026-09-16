#!/usr/bin/env bash
# Deploys the statusline script from this repo to ~/.claude/ for runtime use.
# macOS/Linux counterpart of deploy.ps1.
#
# The /statusline skill is deliberately not deployed: it is a project-level skill
# that ships with this repo under .claude/skills/statusline/, so it only loads in
# sessions working on the statusline. The claude-setup repo keeps its own copy,
# produced by that repo's sync script.
set -euo pipefail

repo_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
claude="$HOME/.claude"

cp "$repo_root/statusline.py" "$claude/statusline.py"

echo "Deployed statusline.py to $claude"
