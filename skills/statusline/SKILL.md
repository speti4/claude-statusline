---
name: statusline
description: "Configure statusline: style, color scheme, rate limit visibility. Run without args for help."
argument-hint: "minimal | catppuccin-mocha | show-5h | hide-7d"
version: 3.1.0
allowed-tools: Bash(python "${CLAUDE_SKILL_DIR}/set_style.py" *)
---

Run: `python "${CLAUDE_SKILL_DIR}/set_style.py" $ARGUMENTS`

Print the script's stdout as your complete reply. Nothing else.
