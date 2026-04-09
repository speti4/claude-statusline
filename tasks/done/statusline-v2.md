# Statusline v2: Python átírás + Banana Blueberry téma

## Context
A régi `statusline.sh` bash+grep-alapú JSON parsinggel működött (törékeny).
A claude-pulse bővítményt eltávolítottuk (429 rate limit), ezért saját statusline-t fejlesztettük tovább.

## Változások (2026-03-08)

### v2.0 — Python átírás
- `statusline.sh` → `statusline.py` (Python 3, `json.load()`)
- Dual-env command: WSL-ben `python3`, Git Bash-ben `python`
- Context bar küszöbök: <60% zöld, 60-79% sárga, 80%+ piros (autocompact-hoz igazítva)
- 1 soros layout, 10 char block bar

### v2.1 — Nerd Font ikonok + Banana Blueberry szín-séma
- Ikonok: 󱚣 (model, U+F16A3),  (dir, U+E5FF),  (git, U+E725)
- RGB true color (`\033[38;2;R;G;Bm`) a Banana Blueberry palettából
- Szeparátor: `│` (U+2502) halványszürkén (#495162)

## Fájlok
- **Aktív:** `C:\Users\peter\.claude\statusline.py`
- **Settings:** `C:\Users\peter\.claude\settings.json` → `"command": "python ~/.claude/statusline.py"`
- **Backup:** `C:\Users\peter\.claude\statusline.sh` (régi bash verzió, megtartva)
