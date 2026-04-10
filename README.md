# Claude Statusline

Custom terminal status bar for [Claude Code](https://claude.ai/code). Displays model info, working directory, git branch, context window usage, and rate limits with color-coded ANSI output.

## Features

- **3 display styles:** minimal, powerline, powerline-short
- **3 color schemes:** Default (colorless), Catppuccin Mocha, Banana Blueberry
- **Rate limit visualization:** 5-hour session + 7-day weekly limits with fill bars and time markers
- **Git integration:** current branch display
- **Usage snapshot:** writes `~/.claude/usage-snapshot.json` for external tools (e.g., dashboards)

## Files

| File | Purpose |
|------|---------|
| `statusline.py` | Main statusline script (Python 3) |
| `skills/statusline/SKILL.md` | `/statusline` skill definition |
| `skills/statusline/set_style.py` | Config helper for style/scheme switching |
| `scripts/deploy.ps1` | Deploy script — copies files to `~/.claude/` |

## Setup

### Prerequisites
- Claude Code installed
- Python 3.x
- PowerShell 7+ (for deploy script)

### Deploy

```powershell
pwsh scripts/deploy.ps1
```

This copies `statusline.py` and the skill files to `~/.claude/`. The `settings.json` statusline block must be configured separately (managed by [claude-setup](https://github.com/user/claude-setup)):

```json
"statusLine": {
  "type": "command",
  "command": "python ~/.claude/statusline.py",
  "padding": 1,
  "refreshInterval": 5
}
```

### Configure

Use the `/statusline` skill in any Claude Code session:
```
/statusline minimal              # switch to minimal style
/statusline catppuccin-mocha     # switch color scheme
/statusline rate-none             # hide rate limits
```

## Development

Edit files in this repo, then deploy:
```powershell
pwsh scripts/deploy.ps1
```

Color palette references are at `e:\tools\color-palettes\` (not duplicated here).
