# Git status indicators next to the branch name

## Context
The statusline showed only the branch name. A dirty working tree or a branch
that has diverged from its upstream was invisible without running `git status`.
Show staged / modified / untracked counts plus ahead/behind next to the branch;
a clean, in-sync branch renders exactly as before.

Glyphs (plain Unicode): `●` staged, `✚` modified (incl. unmerged), `?` untracked,
`↑` ahead, `↓` behind.

## Steps
- [x] Replace the two git calls with one `git status --porcelain=v2 --branch`
      (timeout, `GIT_OPTIONAL_LOCKS=0`, cwd = displayed dir) and parse it
- [x] Render the counters in the minimal style (counters `C_WARN`, ahead/behind `C_GIT`)
- [x] Render the counters inside the powerline git segment
- [x] Update README feature list
- [x] Verify: clean, dirty, ahead, non-git dir, both styles
- [ ] Merge to main, push, deploy

## Status: WIP
