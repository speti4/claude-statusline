#!/usr/bin/env bash
# Deploys the statusline script from this repo to ~/.claude/ for runtime use.
# macOS/Linux counterpart of deploy.ps1.
#
# The settings at the top of the script (STYLE, COLOR_SCHEME, SHOW_RATE_LIMITS,
# SHOW_PROFILE_TAG) are carried over from the copy already deployed, when there is
# one, so updating never resets them. A setting the old copy does not have keeps
# the new default.
#
# The /statusline skill is deliberately not deployed: it is a project-level skill
# that ships with this repo under .claude/skills/statusline/, so it only loads in
# sessions opened in this repo.
set -euo pipefail

repo_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
claude="$HOME/.claude"
source="$repo_root/statusline.py"
target="$claude/statusline.py"
settings=(STYLE COLOR_SCHEME SHOW_RATE_LIMITS SHOW_PROFILE_TAG)

mkdir -p "$claude"
tmp="$(mktemp "$claude/statusline.py.XXXXXX")"
cp "$source" "$tmp"

kept=""
if [[ -f "$target" ]]; then
  for var in "${settings[@]}"; do
    # Values are plain words; anything else is not a setting we recognise.
    value="$(sed -n "s/^$var = \"\([a-z0-9-]*\)\".*/\1/p" "$target" | head -n 1)"
    [[ -n "$value" ]] || continue
    grep -q "^$var = \"" "$tmp" || continue
    sed "s/^\($var = \)\"[^\"]*\"/\1\"$value\"/" "$tmp" > "$tmp.new"
    mv "$tmp.new" "$tmp"
    kept="${kept:+$kept, }$value"
  done
fi

mv "$tmp" "$target"

if [[ -n "$kept" ]]; then
  echo "Deployed statusline.py to $claude (kept settings: $kept)"
else
  echo "Deployed statusline.py to $claude"
fi
