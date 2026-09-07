# Claude Statusline

Custom terminal status bar for Claude Code — Python 3 script with 3 display styles and 6 color schemes.

## Scope
This project contains:
- `statusline.py` — main statusline script (reads JSON from stdin, outputs ANSI-formatted status bar)
- `.claude/skills/statusline/` — `/statusline` slash command for live style/scheme/rate-limit configuration (project-level skill, not deployed)
- `scripts/deploy.ps1` — deploys `statusline.py` to `~/.claude/` for runtime use (Windows)
- `scripts/deploy.sh` — same, for macOS/Linux
- Task history and documentation

## Runtime Deployment
- **This repo is the source of truth** — all edits happen here
- Deploy: `pwsh scripts/deploy.ps1` (Windows) or `bash scripts/deploy.sh` (macOS/Linux), or the `/deploy` skill when working in this repo
- Runtime location: `~/.claude/statusline.py` (the skill is **not** deployed — it is project-level)
- `settings.json` statusline block is managed by the `claude-setup` project
- `usage-snapshot.json` is written to `~/.claude/` at runtime (not tracked here)

## The `/statusline` skill
Project-level skill in `.claude/skills/statusline/`, so it only loads in sessions working on the statusline. The `claude-setup` repo keeps a byte-identical copy, produced by that repo's `scripts/sync-statusline-skill.ps1` — **edit it here, never there.**

`set_style.py` writes the deployed `~/.claude/statusline.py` (so the change takes effect immediately) *and* this repo's `statusline.py` when it is present, resolved relative to the script's own location. There is therefore no drift to reconcile before committing, and no `/deploy` needed after `/statusline`.

## Conventions
- Language: English for code, commits, and docs
- File/folder names: kebab-case
- Color palette references: `e:\tools\color-palettes\` (shared, not duplicated here)
- New task → create a task file in `tasks/wip/` before starting implementation
- Completed tasks move from `tasks/wip/` to `tasks/done/`

## Communication
- User communication: Hungarian (tech terms in English)
- Code, commits, documentation: English
