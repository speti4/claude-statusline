# Statusline skill — create & make global

## Context
A `/statusline <style>` skill that switches the `DIR_STYLE` setting in `~/.claude/statusline.py` between `minimal`, `powerline`, `powerline-short`, and `breadcrumb`.

## Completed steps

### v1.0 — Initial skill (Read + Edit based)
- Created `E:\projects\claude-setup\.claude\skills\statusline\SKILL.md`
- 5-step instructions: validate arg → Read file → Edit line → confirm
- Worked but slow — 2 tool calls + Claude thinking time per invocation

### v1.1 — Prompt optimization
- Stripped SKILL.md to 3 terse steps, added `limit: 10` hint for Read
- Still slow — the Read+Edit tool cycle is the real bottleneck

### v2.0 — Script-based (current)
- Created `set_style.py` alongside SKILL.md — all logic in Python
- SKILL.md reduced to single Bash call: `python set_style.py $ARGUMENTS`
- 1 tool call instead of 2, near-instant execution
- Added `sys.stdout` UTF-8 wrapper for Windows encoding fix

### v2.1 — Best practice cleanup
- Replaced hardcoded path with `${CLAUDE_SKILL_DIR}/set_style.py`
- Narrowed `allowed-tools: Bash` → `Bash(python *)`
- Added `argument-hint` frontmatter

### v2.1 → global
- Moved from project-level (`E:\projects\claude-setup\.claude\skills\`) to global (`C:\Users\peter\.claude\skills\statusline\`)
- No file changes needed — `${CLAUDE_SKILL_DIR}` resolved automatically
- Verified: `/statusline` accessible from other projects

## Final location
```
C:\Users\peter\.claude\skills\statusline\
├── SKILL.md      (v2.1.0)
└── set_style.py
```

## Status: DONE
