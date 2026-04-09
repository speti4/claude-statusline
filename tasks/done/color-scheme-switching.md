# Color scheme switching for statusline

## Context
A statusline.py hardcoded Banana Blueberry színeket használt. Cél: Catppuccin Mocha alternatíva hozzáadása, megtartva a jelenlegi sémát, `/statusline` skill-lel váltható.

## What changed

### statusline.py
- Added `COLOR_SCHEME = "banana-blueberry"` config variable (line 8)
- Replaced hardcoded color constants with `PALETTES` dict containing both schemes
- Palette unpacking: `P = PALETTES[COLOR_SCHEME]` → same variable names, zero changes to rendering logic
- `BAR_RGB` threshold colors now pulled from palette dict (`P["BAR_OK"]` etc.)

### set_style.py (v2.1 → v2.2)
- Added `SCHEMES = {"banana-blueberry", "catppuccin-mocha"}`
- Auto-detects whether argument is a style or color scheme
- Sets `DIR_STYLE` or `COLOR_SCHEME` accordingly
- Error message now lists both valid styles and color schemes

### SKILL.md (v2.1.0 → v2.2.0)
- Updated description, argument-hint to include color scheme names

## Catppuccin Mocha color mapping

| Role | Mocha color | Hex |
|------|------------|-----|
| C_MODEL (model name) | Blue | `#89b4fa` |
| C_DIR (directory) | Text | `#cdd6f4` |
| C_DIM, C_SEP | Surface 2 | `#585b70` |
| C_GIT, C_OK (green) | Green | `#a6e3a1` |
| C_PCT (percentage) | Subtext 1 | `#bac2de` |
| C_WARN (yellow) | Yellow | `#f9e2af` |
| C_CRIT (red) | Red | `#f38ba8` |
| BG_MODEL | Crust | `#11111b` |
| BG_DARK | Mantle | `#181825` |
| BG_MID | Surface 0 | `#313244` |
| BG_LIGHT | Surface 1 | `#45475a` |
| BG_GIT | derived dark green | `#183228` |
| FG_WHITE, FG_MODEL, FG_GIT | Text/Blue/Green | matching fg colors |

## Usage
```
/statusline catppuccin-mocha    # switch to Mocha
/statusline banana-blueberry    # switch back
/statusline powerline           # style switching still works
```

## Status: DONE
