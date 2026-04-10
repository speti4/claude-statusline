# Claude Statusline

Custom terminal status bar for Claude Code — Python 3 script with 3 display styles and 3 color schemes.

## Scope
This project contains:
- `statusline.py` — main statusline script (reads JSON from stdin, outputs ANSI-formatted status bar)
- `skills/statusline/` — `/statusline` slash command for live style/scheme/rate-limit configuration
- `scripts/deploy.ps1` — deploys files to `~/.claude/` for runtime use
- Task history and documentation

## Runtime Deployment
- **This repo is the source of truth** — all edits happen here
- Deploy: `pwsh scripts/deploy.ps1` (or `/deploy` skill when working in this repo)
- Runtime location: `~/.claude/statusline.py` + `~/.claude/skills/statusline/`
- `settings.json` statusline block is managed by the `claude-setup` project
- `usage-snapshot.json` is written to `~/.claude/` at runtime (not tracked here)

## Note on `/statusline` skill drift
The `/statusline` skill modifies `~/.claude/statusline.py` directly (the deployed copy). Config vars (STYLE, COLOR_SCHEME, SHOW_RATE_LIMITS) may drift from the repo source. After tweaking via `/statusline`, sync changes back to this repo before committing.

## Conventions
- Language: English for code, commits, and docs
- File/folder names: kebab-case
- Color palette references: `e:\tools\color-palettes\` (shared, not duplicated here)
- New task → create a task file in `tasks/wip/` before starting implementation
- Completed tasks move from `tasks/wip/` to `tasks/done/`

## Communication
- User communication: Hungarian (tech terms in English)
- Code, commits, documentation: English

## Pending
- Session name display: waiting for [anthropics/claude-code#15029](https://github.com/anthropics/claude-code/issues/15029) — see `docs/session-name-plan.md`
