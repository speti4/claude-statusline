# Rename DIR_STYLE → STYLE, remove breadcrumb

## Status: done

## Context
`DIR_STYLE` is unnecessarily verbose — `STYLE` is clearer. The `breadcrumb` display style is unused and adds complexity. Simplify to 3 styles: `minimal`, `powerline`, `powerline-short`.

## Changes
- [x] `statusline.py`: rename `DIR_STYLE` → `STYLE`, remove breadcrumb code path
- [x] `set_style.py`: update STYLES, FRIENDLY, regex, help text
- [x] `CLAUDE.md`: update config var list and description
- [x] `README.md`: update style count and list
