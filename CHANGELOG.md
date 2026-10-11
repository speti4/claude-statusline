# Changelog

All notable changes to this project are documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.3.0] - 2026-10-11

### Added

- Profile tag, for people who run more than one Claude Code account: an icon for the account
  type (Team / Enterprise or an individual plan) and the name of the profile's config dir
  (`CLAUDE_CONFIG_DIR` without the `.claude-` prefix, so `~/.claude-work` shows as `work`),
  right after the model in every style. Off by default — `SHOW_PROFILE_TAG`, or
  `/statusline profile-all | profile-icon | profile-name | profile-none`

### Changed

- The deploy scripts carry the settings (`STYLE`, `COLOR_SCHEME`, `SHOW_RATE_LIMITS`,
  `SHOW_PROFILE_TAG`) over from the copy already deployed, so updating no longer resets them
- `/statusline` reports a setting the deployed copy does not have yet, instead of silently
  skipping it

## [0.2.0] - 2026-10-09

### Added

- `usage-snapshot.json` has an `account` field — organization id, type and rate-limit tier, read
  from the profile's `.claude.json` — so a reader can tell which account the rate limits belong
  to. `null` when no account is logged in

### Fixed

- The usage snapshot and the default stdin dump directory now follow `CLAUDE_CONFIG_DIR`. Before,
  every profile wrote `~/.claude/usage-snapshot.json`, so with two accounts the last session to
  refresh overwrote the other's rate limits
- A failed snapshot rename (Windows, target held open by another process) no longer leaves a
  `usage-snapshot.json.<pid>.tmp` file behind

## [0.1.1] - 2026-09-24

### Fixed

- Powerline styles: the context and rate-limit segments were hard to read — light text on a light
  green / yellow / red background in the dark schemes. Their text color is now chosen per
  segment for the higher contrast (WCAG ratio ≥ 4.5 in every scheme)
- Catppuccin Latte, powerline styles: darker green for the git segment text

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

[0.3.0]: https://github.com/speti4/claude-statusline/releases/tag/v0.3.0
[0.2.0]: https://github.com/speti4/claude-statusline/releases/tag/v0.2.0
[0.1.1]: https://github.com/speti4/claude-statusline/releases/tag/v0.1.1
[0.1.0]: https://github.com/speti4/claude-statusline/releases/tag/v0.1.0
