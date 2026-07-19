# Compatibility review against current Claude Code (2026-07)

**Date:** 2026-07-19
**Status:** Done
**Outcome:** Fully compatible — no code fixes required.

## Scope

The repo was last touched in April 2026. Reviewed `statusline.py` and the `/statusline` skill against the current Claude Code (v2.1.x, July 2026) statusline integration to check whether any Anthropic-side changes require fixes.

## Findings

### Still valid (no action)
- All consumed stdin payload fields remain correct: `model.display_name`, `workspace.current_dir` (with `cwd` fallback), `context_window.used_percentage`, `rate_limits.five_hour` / `rate_limits.seven_day` with `used_percentage` and epoch-seconds `resets_at`.
- Hardcoded rate-limit window durations (5h / 168h) still match the official windows.
- The percentage-based context bar needs no change for Sonnet 5's 1M context window — Claude Code computes `used_percentage` against the actual window size.
- `.split(" (")[0]` display-name stripping is harmless with current display names — kept.
- 60/80% color thresholds are our own design choice, not tied to Claude Code internals.

### New payload fields reviewed and consciously skipped
`session_name`, `vim.mode`, `thinking.enabled`, `effort.level`, `fast_mode`, `cost.total_cost_usd`, `context_window.context_window_size`, `exceeds_200k_tokens`, `current_usage` (cache breakdown), `pr`, `worktree`, `output_style` — all already visible elsewhere in the Claude Code UI or not needed; the statusline stays minimal.

### Settings
- `statusLine.refreshInterval: 5` is already live in `~/.claude/settings.json` (managed by claude-setup), so rate-limit countdowns refresh during idle — no action needed.

### Housekeeping done in this task
- Synced config drift back from the deployed copy: `COLOR_SCHEME = "catppuccin-mocha"` (set via `/statusline`, repo still had `"default"`). Everything else (script body, skill files) was drift-free.
