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
| `.claude/skills/statusline/SKILL.md` | `/statusline` skill definition (project-level) |
| `.claude/skills/statusline/set_style.py` | Config helper for style/scheme switching |
| `scripts/deploy.ps1` | Deploy script — copies `statusline.py` to `~/.claude/` |

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
</details>

This copies `statusline.py` to `~/.claude/`. The `/statusline` skill is not deployed — it is
a project-level skill under `.claude/skills/`, available whenever you work in this repo. The
`settings.json` statusline block must be configured separately (managed by the `claude-setup`
project):

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

Use the `/statusline` skill from a session working in this repo:
```
/statusline minimal              # switch to minimal style
/statusline catppuccin-mocha     # switch color scheme
/statusline rate-none             # hide rate limits
```

It writes the deployed `~/.claude/statusline.py`, so the change shows up in the status bar
right away, and this repo's `statusline.py` alongside it — no `/deploy` needed afterwards,
and the two copies cannot drift apart.

## Development

Edit `statusline.py` in this repo, then deploy with the script for your platform
(`deploy.ps1` on Windows, `deploy.sh` on macOS/Linux), or run the `/deploy` skill from
within this repo.

### Dumping the raw stdin payload

Claude Code documents only part of what it sends the statusline, so when a question comes
up about a field, dump the payload instead of guessing. Set `CLAUDE_STATUSLINE_DUMP` to a
directory (or to `1` for `~/.claude/statusline-dump/`) and each invocation appends its
stdin verbatim as one JSON line:

```powershell
$env:CLAUDE_STATUSLINE_DUMP = "1"; claude    # PowerShell
```
```bash
CLAUDE_STATUSLINE_DUMP=1 claude              # bash / zsh
```

Two constraints: Claude Code reads the variable when it starts, so it has to be set
**before** launching a session — an already-running one never dumps. And each session
writes its own `stdin-<pid>.jsonl`, because concurrent appends to a single file
interleave into unparseable lines. Each file stops growing at 20 MB.

Color palette references are at `e:\tools\color-palettes\` on the Windows machine (not duplicated here).
