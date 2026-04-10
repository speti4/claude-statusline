# Merge SHOW_SESSION + SHOW_WEEKLY → SHOW_RATE_LIMITS

## Status: done

## Context
Two boolean config vars (`SHOW_SESSION`, `SHOW_WEEKLY`) are better expressed as a single string enum: `SHOW_RATE_LIMITS = "all" | "5h" | "7d" | "none"`. Skill commands change from `show-5h`/`hide-5h`/`show-7d`/`hide-7d` to `rate-all`/`rate-5h`/`rate-7d`/`rate-none`.

## Changes
- [x] `statusline.py`: replace 2 bools with 1 string, update conditionals
- [x] `set_style.py`: replace TOGGLES with RATE_OPTS, remove `_read_bool`, rewrite help
- [x] `SKILL.md`: update argument-hint
- [x] `CLAUDE.md`: update config var list
- [x] `README.md`: update rate limit description and examples
