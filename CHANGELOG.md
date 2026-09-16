# Changelog

All notable changes to this project are documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.1.0] - 2026-09-16

First public release.

### Added

- Single-line status bar for Claude Code: model, working directory, git branch, context window usage, rate limits
- 3 display styles: `minimal`, `powerline`, `powerline-short`
- 6 color schemes: `default` (colorless, bold/dim only), `banana-blueberry`, `catppuccin-frappe`, `catppuccin-latte`, `catppuccin-macchiato`, `catppuccin-mocha`
- Rate-limit bars for the 5-hour session and 7-day weekly windows, with fill, elapsed-time marker and reset countdown; visibility switchable (`all`, `5h`, `7d`, `none`)
- Git working-tree indicators next to the branch: staged, modified, untracked counts and ahead/behind upstream, hidden when clean and in sync
- Context window bar with 60% / 80% color thresholds
- `~/.claude/usage-snapshot.json` written on every refresh for external dashboards
- `/statusline` skill to switch style, color scheme and rate-limit visibility from inside Claude Code
- `/deploy` skill and deploy scripts for Windows (`scripts/deploy.ps1`) and macOS/Linux (`scripts/deploy.sh`)
- Optional raw stdin dump (`CLAUDE_STATUSLINE_DUMP`) for inspecting the payload Claude Code sends

[0.1.0]: https://github.com/speti4/claude-statusline/releases/tag/v0.1.0
