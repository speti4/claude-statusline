# Add default colorless COLOR_SCHEME

## Status: done

## Context
Add a `"default"` color scheme that uses no RGB colors — only ANSI bold/dim attributes. Makes the statusline work in any terminal without assuming color support. Becomes the new default value.

## Changes
- [x] `statusline.py`: add `"default"` palette (bold/dim/reset), set as default, update fallback
- [x] `set_style.py`: add to SCHEMES, update help and comment
- [x] `CLAUDE.md`: update scheme count
- [x] `README.md`: update scheme count and list
