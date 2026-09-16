---
name: deploy
description: Deploy statusline.py to ~/.claude/ for runtime use
version: 2.0.0
allowed-tools:
  - Bash(pwsh scripts/deploy.ps1)
  - Bash(bash scripts/deploy.sh)
---

# /deploy

Deploy the statusline script from this repo to `~/.claude/`.

## What it does
Runs the deploy script for the current platform:

| Platform | Command |
|----------|---------|
| Windows | `pwsh scripts/deploy.ps1` |
| macOS / Linux | `bash scripts/deploy.sh` |

Both copy `statusline.py` → `~/.claude/statusline.py`, the path the `settings.json`
statusline command runs.

The `/statusline` skill is **not** deployed. It is a project-level skill living in
`.claude/skills/statusline/`, available whenever you work in this repo; the `claude-setup`
repo keeps its own copy, produced by that repo's sync script.

## When to use
After editing `statusline.py` in this repo.

Not needed after `/statusline`: that skill writes both the deployed copy and this repo's
`statusline.py` in one go.
