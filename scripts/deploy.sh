#!/usr/bin/env bash
# Deploys statusline files from this repo to ~/.claude/ for runtime use.
# macOS/Linux counterpart of deploy.ps1.
set -euo pipefail

repo_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
claude="$HOME/.claude"
skill_dest="$claude/skills/statusline"

mkdir -p "$skill_dest"

cp "$repo_root/statusline.py" "$claude/statusline.py"
count=1

for f in "$repo_root"/skills/statusline/*; do
    cp "$f" "$skill_dest/"
    count=$((count + 1))
done

# macOS and most Linux distros have no `python` command, only `python3`.
# The repo source targets Windows, so rewrite the interpreter in the deployed
# copy. Done in Python rather than sed to avoid BSD/GNU sed differences.
python3 - "$skill_dest/SKILL.md" <<'EOF'
import re, sys
path = sys.argv[1]
with open(path, encoding="utf-8") as f:
    text = f.read()
patched = re.sub(r"\bpython(?=[ \"])", "python3", text)
if patched != text:
    with open(path, "w", encoding="utf-8") as f:
        f.write(patched)
EOF

echo "Deployed $count files to $claude"
