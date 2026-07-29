# Pin line endings with .gitattributes

## Context
The repo is edited from both Windows (`core.autocrlf=true`) and macOS. After the
macOS-support commit (`1b6cae7`) added `scripts/deploy.sh`, the Windows checkout
converts it to CRLF. That doesn't break the Windows workflow (deploy.sh is never
run there), but it is fragile: copying the file outside Git, or a clone with
different autocrlf settings, would produce a CRLF shell script that fails on
macOS (`\r` in shebang and heredoc).

## Steps
- [x] Add `.gitattributes`: `* text=auto`, `*.sh text eol=lf`, `*.ps1 text eol=crlf`
- [x] `git add --renormalize .` and check for index churn
- [x] Verify `git check-attr eol scripts/deploy.sh` reports `lf` and the working
      tree copy is LF after re-checkout
- [x] Merge to main

## Status: DONE
