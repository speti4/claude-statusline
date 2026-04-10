import sys, re, io, os

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")

FILE = os.path.join(os.path.expanduser("~"), ".claude", "statusline.py")

STYLES = {"minimal", "powerline", "powerline-short"}
SCHEMES = {"default", "banana-blueberry", "catppuccin-mocha"}
RATE_OPTS = {
    "rate-all":  "all",
    "rate-5h":   "5h",
    "rate-7d":   "7d",
    "rate-none": "none",
}

FRIENDLY = {
    "STYLE":        "Style",
    "COLOR_SCHEME": "Scheme",
    "SHOW_RATE_LIMITS": "Rate limits",
}

# ── Read current state ───────────────────────────────────────────
with open(FILE, "r", encoding="utf-8") as f:
    content = f.read()

def _read_str(var):
    m = re.search(rf'{var} = "([^"]*)"', content)
    return m.group(1) if m else "?"

cur_style   = _read_str("STYLE")
cur_scheme  = _read_str("COLOR_SCHEME")
cur_rate    = _read_str("SHOW_RATE_LIMITS")

# ── No args → help with current state ────────────────────────────
if len(sys.argv) < 2:
    print(f"""/statusline \u2014 Configure statusline appearance

  Style:    minimal | powerline | powerline-short
  Scheme:   default | banana-blueberry | catppuccin-mocha
  Rate:     rate-all | rate-5h | rate-7d | rate-none

  Current:  {cur_style} \u00b7 {cur_scheme} \u00b7 rate: {cur_rate}

  Examples: /statusline powerline
            /statusline rate-none""")
    sys.exit(0)

# ── Deduplicate: last-wins per variable ──────────────────────────
seen_vars = {}  # var_name → (index, arg)
raw_args = sys.argv[1:]

for i, arg in enumerate(raw_args):
    if arg in STYLES:
        seen_vars["STYLE"] = (i, arg)
    elif arg in SCHEMES:
        seen_vars["COLOR_SCHEME"] = (i, arg)
    elif arg in RATE_OPTS:
        seen_vars["SHOW_RATE_LIMITS"] = (i, arg)
    else:
        seen_vars[f"_error_{i}"] = (i, arg)

# ── Process deduplicated args in original order ──────────────────
changes = []
errors = []

for var, (_, arg) in sorted(seen_vars.items(), key=lambda x: x[1][0]):
    if var.startswith("_error_"):
        errors.append(f"Unknown: `{arg}` \u2014 run /statusline for help")
        continue

    label = FRIENDLY[var]

    if arg in STYLES:
        comment = '# "minimal" | "powerline" | "powerline-short"'
        old = _read_str(var)
        if old == arg:
            changes.append(f"{label}: already `{arg}`")
            continue
        content = re.sub(rf'{var} = "[^"]*".*', f'{var} = "{arg}"  {comment}', content)
        changes.append(f"{label}: {old} \u2192 {arg}")

    elif arg in SCHEMES:
        comment = '# "default" | "banana-blueberry" | "catppuccin-mocha"'
        old = _read_str(var)
        if old == arg:
            changes.append(f"{label}: already `{arg}`")
            continue
        content = re.sub(rf'{var} = "[^"]*".*', f'{var} = "{arg}"  {comment}', content)
        changes.append(f"{label}: {old} \u2192 {arg}")

    elif arg in RATE_OPTS:
        new_val = RATE_OPTS[arg]
        comment = '# "all" | "5h" | "7d" | "none"'
        old = _read_str(var)
        if old == new_val:
            changes.append(f"{label}: already `{new_val}`")
            continue
        content = re.sub(rf'{var} = "[^"]*".*', f'{var} = "{new_val}"  {comment}', content)
        changes.append(f"{label}: {old} \u2192 {new_val}")

# ── Write once ───────────────────────────────────────────────────
if any(not line.startswith("Unknown") for line in changes):
    with open(FILE, "w", encoding="utf-8") as f:
        f.write(content)

for line in changes:
    print(line)
for line in errors:
    print(line, file=sys.stderr)
    print(line)  # also to stdout so Claude sees it
