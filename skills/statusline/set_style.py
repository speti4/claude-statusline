import sys, re, io, os

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")

FILE = os.path.join(os.path.expanduser("~"), ".claude", "statusline.py")

STYLES = {"minimal", "powerline", "powerline-short", "breadcrumb"}
SCHEMES = {"banana-blueberry", "catppuccin-mocha"}
TOGGLES = {
    "show-5h": ("SHOW_SESSION", True),
    "hide-5h": ("SHOW_SESSION", False),
    "show-7d": ("SHOW_WEEKLY", True),
    "hide-7d": ("SHOW_WEEKLY", False),
}

FRIENDLY = {
    "DIR_STYLE":    "Style",
    "COLOR_SCHEME": "Scheme",
    "SHOW_SESSION": "5h rate limit",
    "SHOW_WEEKLY":  "7d rate limit",
}

# ── Read current state ───────────────────────────────────────────
with open(FILE, "r", encoding="utf-8") as f:
    content = f.read()

def _read_str(var):
    m = re.search(rf'{var} = "([^"]*)"', content)
    return m.group(1) if m else "?"

def _read_bool(var):
    m = re.search(rf'{var} = (True|False)', content)
    return m.group(1) == "True" if m else True

cur_style   = _read_str("DIR_STYLE")
cur_scheme  = _read_str("COLOR_SCHEME")
cur_session = _read_bool("SHOW_SESSION")
cur_weekly  = _read_bool("SHOW_WEEKLY")

# ── No args → help with current state ────────────────────────────
if len(sys.argv) < 2:
    s_chk = "\u2713" if cur_session else "\u2717"
    w_chk = "\u2713" if cur_weekly else "\u2717"
    print(f"""/statusline \u2014 Configure statusline appearance

  Style:    minimal | powerline | powerline-short | breadcrumb
  Scheme:   banana-blueberry | catppuccin-mocha
  Rate:     show-5h | hide-5h | show-7d | hide-7d

  Current:  {cur_style} \u00b7 {cur_scheme} \u00b7 5h {s_chk} \u00b7 7d {w_chk}

  Examples: /statusline powerline
            /statusline hide-5h hide-7d""")
    sys.exit(0)

# ── Deduplicate: last-wins per variable ──────────────────────────
seen_vars = {}  # var_name → (index, arg)
raw_args = sys.argv[1:]

for i, arg in enumerate(raw_args):
    if arg in STYLES:
        seen_vars["DIR_STYLE"] = (i, arg)
    elif arg in SCHEMES:
        seen_vars["COLOR_SCHEME"] = (i, arg)
    elif arg in TOGGLES:
        var, _ = TOGGLES[arg]
        seen_vars[var] = (i, arg)
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
        comment = '# "minimal" | "powerline" | "powerline-short" | "breadcrumb"'
        old = _read_str(var)
        if old == arg:
            changes.append(f"{label}: already `{arg}`")
            continue
        content = re.sub(rf'{var} = "[^"]*".*', f'{var} = "{arg}"  {comment}', content)
        changes.append(f"{label}: {old} \u2192 {arg}")

    elif arg in SCHEMES:
        comment = '# "banana-blueberry" | "catppuccin-mocha"'
        old = _read_str(var)
        if old == arg:
            changes.append(f"{label}: already `{arg}`")
            continue
        content = re.sub(rf'{var} = "[^"]*".*', f'{var} = "{arg}"  {comment}', content)
        changes.append(f"{label}: {old} \u2192 {arg}")

    elif arg in TOGGLES:
        _, new_val = TOGGLES[arg]
        comment = f"# Show {'5-hour session' if 'SESSION' in var else '7-day weekly'} rate limit"
        old_val = _read_bool(var)
        vis_old = "visible" if old_val else "hidden"
        vis_new = "visible" if new_val else "hidden"
        if old_val == new_val:
            changes.append(f"{label}: already {vis_new}")
            continue
        content = re.sub(rf'{var} = (True|False).*', f"{var} = {new_val}   {comment}", content)
        changes.append(f"{label}: {vis_old} \u2192 {vis_new}")

# ── Write once ───────────────────────────────────────────────────
if any(not line.startswith("Unknown") for line in changes):
    with open(FILE, "w", encoding="utf-8") as f:
        f.write(content)

for line in changes:
    print(line)
for line in errors:
    print(line, file=sys.stderr)
    print(line)  # also to stdout so Claude sees it
