# Session Name in Statusline — Waiting for Upstream

## Status: Blocked on upstream

**Issue:** [anthropics/claude-code#15029](https://github.com/anthropics/claude-code/issues/15029) — "Feature Request: Add session_name to statusline JSON data"
- Open since 2025-12-22, 15 comments, many +1s
- Labels: `enhancement`, `has repro`, `area:tui`
- No ETA from Anthropic yet

No implementation until the `session_name` field is available in statusline JSON input.

## When `session_name` becomes available

Display plan for all 4 statusline styles:

| Style | Placement | Format |
|-------|-----------|--------|
| **minimal** | After model, before directory | `🧠 opus · session-name │ dir │ main │ ████░ 40%` |
| **powerline** | Dedicated segment after model | Model ▶ SessionName ▶ Dir... |
| **powerline-short** | Same, truncated if >20 chars | Model ▶ Sess... ▶ Dir... |
| **breadcrumb** | After model icon | `🧠 opus › session-name › path › segments` |

- If no session name set → segment omitted
- Colors — catppuccin-mocha: `#b4befe` (Lavender); banana-blueberry: `#A89AE8` (soft purple)

---

## Dashboard Integration (historical note)

Originally planned to bundle statusline into the `dev-dashboard` repo for reproducibility (see fizzy-bubbling-crown plan). That approach was superseded by this dedicated `claude-statusline` repo.

The dashboard still consumes `~/.claude/usage-snapshot.json` written by `statusline.py`. The deploy script in this repo handles setup on new machines.
