---
name: deploy
description: Deploy statusline files to ~/.claude/ for runtime use
version: 1.1.0
allowed-tools:
  - Bash(pwsh scripts/deploy.ps1)
  - Bash(bash scripts/deploy.sh)
---

# /deploy

Deploy the statusline script and skill files from this repo to `~/.claude/`.

## What it does
Runs the deploy script for the current platform:

| Platform | Command |
|----------|---------|
| Windows | `pwsh scripts/deploy.ps1` |
| macOS / Linux | `bash scripts/deploy.sh` |

Both copy:
- `statusline.py` → `~/.claude/statusline.py`
- `skills/statusline/*` → `~/.claude/skills/statusline/`

On macOS and Linux, `deploy.sh` additionally rewrites `python` to `python3` in the
deployed `SKILL.md`, since those platforms have no `python` command. The repo source
stays Windows-targeted.

## When to use
After editing `statusline.py`, `SKILL.md`, or `set_style.py` in this repo.
