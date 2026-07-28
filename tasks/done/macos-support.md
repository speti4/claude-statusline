# macOS support — deploy script and docs

## Context
The repo is now used from a MacBook (Apple Silicon, zsh) in addition to Windows.
Deployment was PowerShell-only and could not run on macOS.

## Problems found
1. `scripts/deploy.ps1` resolves the target with `$env:USERPROFILE`, which is **undefined on macOS**.
   Even with PowerShell 7 installed, the script would deploy to `/.claude`.
2. `pwsh` is not installed on macOS and is not a reasonable dependency there.
3. `README.md` documents `python ~/.claude/statusline.py` — macOS has **no `python` command**,
   only `python3`. The statusline block must use `python3`.
4. The `/statusline` skill invoked `python` too, so the skill would have failed on macOS
   even after a successful deploy.

## Decisions
- Add `scripts/deploy.sh` as the macOS/Linux counterpart. Keep `deploy.ps1` for Windows.
- Do not make `deploy.ps1` cross-platform: each script stays idiomatic for its own platform.
- `deploy.sh` rewrites `python` → `python3` in the deployed `SKILL.md`, so the repo keeps a
  single Windows-targeted source and no drift is introduced.

## Steps
- [x] Add `scripts/deploy.sh` (`$HOME`, `mkdir -p`, `cp`), executable bit set
- [x] Rewrite `python` → `python3` in the deployed `SKILL.md` (repo source stays Windows-targeted)
- [x] Update `.claude/skills/deploy/SKILL.md` for both platforms
- [x] Update `CLAUDE.md` deployment section
- [x] Add a macOS section to `README.md` (prerequisites, deploy, `python3` statusline block)
- [x] Deploy on macOS and verify `/statusline` help output runs
- [x] Install CaskaydiaCove Nerd Font (36 TTFs into `~/Library/Fonts`, no admin rights needed)
- [x] Confirm the statusline renders with correct glyphs

## Notes
- `statusline.py` itself needed **no changes** — verified running under the macOS
  system Python 3.9.6 with correct ANSI and Nerd Font output.
- **One font file, two family names.** Verified by parsing the TTF `name` table:
  nameID 1 (legacy family) is `CaskaydiaCove NFM`, nameID 16 (typographic family) is
  `CaskaydiaCove Nerd Font Mono`. Windows resolves fonts by nameID 1, while macOS CoreText
  prefers nameID 16 — so the *same* font is addressed by a *different* name per OS.
  VS Code Settings Sync carries the font name across machines but not the font itself, so the
  synced `'CaskaydiaCove NFM'` did not resolve on macOS and every glyph rendered as a box.
  Fixed by listing both names in `terminal.integrated.fontFamily`; the fallback list works
  unchanged on both platforms. This is not a Nerd Fonts v2/v3 versioning issue.
- Verified `U+F16A3` (the model icon) is present in the v3 font.

## Status: DONE
