# Claude Statusline

Custom terminal status bar for [Claude Code](https://claude.ai/code). Displays model info, working directory, git branch, context window usage, and rate limits with color-coded ANSI output.

## Features

- **3 display styles:** minimal, powerline, powerline-short
- **6 color schemes:** Default (colorless), Banana Blueberry, Catppuccin Frappé, Catppuccin Latte, Catppuccin Macchiato, Catppuccin Mocha
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
- Python 3.x (verified on 3.9+)
- A [Nerd Font](https://www.nerdfonts.com/) in your terminal — without one, the icons and powerline separators render as empty boxes
- PowerShell 7+ — Windows only, for `deploy.ps1`

### Deploy

<details open>
<summary><b>Windows</b></summary>

```powershell
pwsh scripts/deploy.ps1
```
</details>

<details open>
<summary><b>macOS / Linux</b></summary>

```bash
bash scripts/deploy.sh
```

`deploy.sh` also rewrites `python` to `python3` in the deployed `SKILL.md`, since macOS
and most Linux distros ship no `python` command. The repo source stays Windows-targeted.
</details>

This copies `statusline.py` and the skill files to `~/.claude/`. The `settings.json` statusline block must be configured separately (managed by the `claude-setup` project):

```json
"statusLine": {
  "type": "command",
  "command": "python ~/.claude/statusline.py",
  "padding": 1,
  "refreshInterval": 5
}
```

On macOS and Linux use `python3` in that command — there is no `python` executable.

### Configure

Use the `/statusline` skill in any Claude Code session:
```
/statusline minimal              # switch to minimal style
/statusline catppuccin-mocha     # switch color scheme
/statusline rate-none             # hide rate limits
```

## Development

Edit files in this repo, then deploy with the script for your platform (`deploy.ps1` on
Windows, `deploy.sh` on macOS/Linux), or run the `/deploy` skill from within this repo.

Color palette references are at `e:\tools\color-palettes\` on the Windows machine (not duplicated here).
