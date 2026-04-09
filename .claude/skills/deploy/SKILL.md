---
name: deploy
description: Deploy statusline files to ~/.claude/ for runtime use
version: 1.0.0
allowed-tools:
  - Bash(pwsh scripts/deploy.ps1)
---

# /deploy

Deploy the statusline script and skill files from this repo to `~/.claude/`.

## What it does
Runs `pwsh scripts/deploy.ps1` which copies:
- `statusline.py` → `~/.claude/statusline.py`
- `skills/statusline/*` → `~/.claude/skills/statusline/`

## When to use
After editing `statusline.py`, `SKILL.md`, or `set_style.py` in this repo.
