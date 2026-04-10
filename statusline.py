#!/usr/bin/env python3
import json, sys, subprocess, os, io
from datetime import datetime, timezone

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")

# ── Config ──────────────────────────────────────────────────────────
STYLE = "minimal"  # "minimal" | "powerline" | "powerline-short"
COLOR_SCHEME = "default"  # "default" | "banana-blueberry" | "catppuccin-frappe" | "catppuccin-latte" | "catppuccin-macchiato" | "catppuccin-mocha"
SHOW_RATE_LIMITS = "all"  # "all" | "5h" | "7d" | "none"

# ── Data ────────────────────────────────────────────────────────────
data = json.load(sys.stdin)

model = data.get("model", {}).get("display_name", "?").split(" (")[0]
cwd = data.get("workspace", {}).get("current_dir", "") or data.get("cwd", "")
pct = int(data.get("context_window", {}).get("used_percentage", 0) or 0)

# Rate limits (may be absent for API key users)
rate_limits = data.get("rate_limits", {}) or {}
rl_5h = rate_limits.get("five_hour", {}) or {}
rl_7d = rate_limits.get("seven_day", {}) or {}
rl_5h_pct = int(rl_5h.get("used_percentage", 0) or 0)
rl_7d_pct = int(rl_7d.get("used_percentage", 0) or 0)

# ── Persist snapshot for dev-dashboard ──────────────────────────────
import time as _time
_snapshot_path = os.path.join(os.path.expanduser("~"), ".claude", "usage-snapshot.json")
try:
    _snapshot = {
        "timestamp": int(_time.time()),
        "model": model,
        "context_window_pct": pct,
        "rate_limits": {
            "five_hour": {"used_percentage": rl_5h_pct, "resets_at": rl_5h.get("resets_at")},
            "seven_day": {"used_percentage": rl_7d_pct, "resets_at": rl_7d.get("resets_at")},
        },
    }
    _tmp = _snapshot_path + ".tmp"
    with open(_tmp, "w", encoding="utf-8") as _f:
        json.dump(_snapshot, _f)
    os.replace(_tmp, _snapshot_path)
except Exception:
    pass

# ── Color palettes ──────────────────────────────────────────────────
PALETTES = {
    "default": {
        "C_MODEL": "\033[1m",                      # Bold
        "C_DIR":   "\033[0m",                      # Default
        "C_DIM":   "\033[2m",                      # Dim
        "C_GIT":   "\033[0m",                      # Default
        "C_SEP":   "\033[2m",                      # Dim
        "C_PCT":   "\033[0m",                      # Default
        "C_OK":    "\033[0m",                      # Default
        "C_WARN":  "\033[0m",                      # Default
        "C_CRIT":  "\033[0m",                      # Default
        "BG_MODEL": (180, 180, 180),  # Light gray
        "BG_DARK":  (40, 40, 40),     # Dark gray
        "BG_MID":   (60, 60, 60),     # Mid gray
        "BG_LIGHT": (80, 80, 80),     # Light gray
        "BG_GIT":   (50, 50, 50),     # Dark gray
        "FG_WHITE": (220, 220, 220),  # Near-white
        "FG_MODEL": (30, 30, 30),     # Dark text on light bg
        "FG_GIT":   (200, 200, 200),  # Light text
        "BAR_OK":   (180, 180, 180),  # Gray
        "BAR_WARN": (180, 180, 180),  # Gray
        "BAR_CRIT": (180, 180, 180),  # Gray
    },
    "banana-blueberry": {
        "C_MODEL": "\033[38;2;34;232;223m",    # #22E8DF neon türkiz
        "C_DIR":   "\033[38;2;241;241;241m",   # #F1F1F1 fehér
        "C_DIM":   "\033[38;2;73;81;98m",      # #495162 halkabb szürke
        "C_GIT":   "\033[38;2;0;189;156m",     # #00BD9C smaragdzöld
        "C_SEP":   "\033[38;2;73;81;98m",      # #495162
        "C_PCT":   "\033[38;2;204;204;204m",   # #CCCCCC
        "C_OK":    "\033[38;2;0;189;156m",     # #00BD9C
        "C_WARN":  "\033[38;2;230;198;47m",    # #E6C62F
        "C_CRIT":  "\033[38;2;255;107;127m",   # #FF6B7F
        "BG_MODEL": (34, 232, 223),  # #22E8DF teal accent
        "BG_DARK":  (35, 30, 50),    # #231E32 sötét lila
        "BG_MID":   (73, 81, 98),    # #495162 közép szürke
        "BG_LIGHT": (90, 98, 120),   # #5A6278 világosabb
        "BG_GIT":   (10, 48, 41),    # #0A3029 sötét zöld
        "FG_WHITE": (241, 241, 241), # #F1F1F1
        "FG_MODEL": (23, 20, 31),    # #17141F dark text
        "FG_GIT":   (0, 189, 156),   # #00BD9C
        "BAR_OK":   (0, 189, 156),   # #00BD9C
        "BAR_WARN": (230, 198, 47),  # #E6C62F
        "BAR_CRIT": (255, 107, 127), # #FF6B7F
    },
    "catppuccin-frappe": {
        "C_MODEL": "\033[38;2;140;170;238m",   # #8caaee Blue
        "C_DIR":   "\033[38;2;198;208;245m",   # #c6d0f5 Text
        "C_DIM":   "\033[38;2;98;104;128m",    # #626880 Surface 2
        "C_GIT":   "\033[38;2;166;209;137m",   # #a6d189 Green
        "C_SEP":   "\033[38;2;98;104;128m",    # #626880 Surface 2
        "C_PCT":   "\033[38;2;181;191;226m",   # #b5bfe2 Subtext 1
        "C_OK":    "\033[38;2;166;209;137m",   # #a6d189 Green
        "C_WARN":  "\033[38;2;229;200;144m",   # #e5c890 Yellow
        "C_CRIT":  "\033[38;2;231;130;132m",   # #e78284 Red
        "BG_MODEL": (140, 170, 238), # #8caaee Blue accent
        "BG_DARK":  (41, 44, 60),    # #292c3c Mantle
        "BG_MID":   (65, 69, 89),    # #414559 Surface 0
        "BG_LIGHT": (81, 87, 109),   # #51576d Surface 1
        "BG_GIT":   (41, 70, 63),    # derived dark green
        "FG_WHITE": (198, 208, 245), # #c6d0f5 Text
        "FG_MODEL": (35, 38, 52),    # #232634 Crust dark text
        "FG_GIT":   (166, 209, 137), # #a6d189 Green
        "BAR_OK":   (166, 209, 137), # #a6d189 Green
        "BAR_WARN": (229, 200, 144), # #e5c890 Yellow
        "BAR_CRIT": (231, 130, 132), # #e78284 Red
    },
    "catppuccin-latte": {
        "C_MODEL": "\033[38;2;30;102;245m",    # #1e66f5 Blue
        "C_DIR":   "\033[38;2;76;79;105m",     # #4c4f69 Text
        "C_DIM":   "\033[38;2;172;176;190m",   # #acb0be Surface 2
        "C_GIT":   "\033[38;2;64;160;43m",     # #40a02b Green
        "C_SEP":   "\033[38;2;172;176;190m",   # #acb0be Surface 2
        "C_PCT":   "\033[38;2;92;95;119m",     # #5c5f77 Subtext 1
        "C_OK":    "\033[38;2;64;160;43m",     # #40a02b Green
        "C_WARN":  "\033[38;2;223;142;29m",    # #df8e1d Yellow
        "C_CRIT":  "\033[38;2;210;15;57m",     # #d20f39 Red
        "BG_MODEL": (30, 102, 245),  # #1e66f5 Blue accent
        "BG_DARK":  (230, 233, 239), # #e6e9ef Mantle
        "BG_MID":   (204, 208, 218), # #ccd0da Surface 0
        "BG_LIGHT": (188, 192, 204), # #bcc0cc Surface 1
        "BG_GIT":   (210, 243, 219), # derived light green
        "FG_WHITE": (76, 79, 105),   # #4c4f69 Text (dark for light bg)
        "FG_MODEL": (239, 241, 245), # #eff1f5 Base (light for dark bg)
        "FG_GIT":   (64, 160, 43),   # #40a02b Green
        "BAR_OK":   (64, 160, 43),   # #40a02b Green
        "BAR_WARN": (223, 142, 29),  # #df8e1d Yellow
        "BAR_CRIT": (210, 15, 57),   # #d20f39 Red
    },
    "catppuccin-macchiato": {
        "C_MODEL": "\033[38;2;138;173;244m",   # #8aadf4 Blue
        "C_DIR":   "\033[38;2;202;211;245m",   # #cad3f5 Text
        "C_DIM":   "\033[38;2;91;96;120m",     # #5b6078 Surface 2
        "C_GIT":   "\033[38;2;166;218;149m",   # #a6da95 Green
        "C_SEP":   "\033[38;2;91;96;120m",     # #5b6078 Surface 2
        "C_PCT":   "\033[38;2;184;192;224m",   # #b8c0e0 Subtext 1
        "C_OK":    "\033[38;2;166;218;149m",   # #a6da95 Green
        "C_WARN":  "\033[38;2;238;212;159m",   # #eed49f Yellow
        "C_CRIT":  "\033[38;2;237;135;150m",   # #ed8796 Red
        "BG_MODEL": (138, 173, 244), # #8aadf4 Blue accent
        "BG_DARK":  (30, 32, 48),    # #1e2030 Mantle
        "BG_MID":   (54, 58, 79),    # #363a4f Surface 0
        "BG_LIGHT": (73, 77, 100),   # #494d64 Surface 1
        "BG_GIT":   (30, 58, 51),    # derived dark green
        "FG_WHITE": (202, 211, 245), # #cad3f5 Text
        "FG_MODEL": (24, 25, 38),    # #181926 Crust dark text
        "FG_GIT":   (166, 218, 149), # #a6da95 Green
        "BAR_OK":   (166, 218, 149), # #a6da95 Green
        "BAR_WARN": (238, 212, 159), # #eed49f Yellow
        "BAR_CRIT": (237, 135, 150), # #ed8796 Red
    },
    "catppuccin-mocha": {
        "C_MODEL": "\033[38;2;137;180;250m",   # #89b4fa Blue
        "C_DIR":   "\033[38;2;205;214;244m",   # #cdd6f4 Text
        "C_DIM":   "\033[38;2;88;91;112m",     # #585b70 Surface 2
        "C_GIT":   "\033[38;2;166;227;161m",   # #a6e3a1 Green
        "C_SEP":   "\033[38;2;88;91;112m",     # #585b70 Surface 2
        "C_PCT":   "\033[38;2;186;194;222m",   # #bac2de Subtext 1
        "C_OK":    "\033[38;2;166;227;161m",   # #a6e3a1 Green
        "C_WARN":  "\033[38;2;249;226;175m",   # #f9e2af Yellow
        "C_CRIT":  "\033[38;2;243;139;168m",   # #f38ba8 Red
        "BG_MODEL": (137, 180, 250), # #89b4fa Blue accent
        "BG_DARK":  (24, 24, 37),    # #181825 Mantle
        "BG_MID":   (49, 50, 68),    # #313244 Surface 0
        "BG_LIGHT": (69, 71, 90),    # #45475a Surface 1
        "BG_GIT":   (24, 50, 40),    # #183228 derived dark green
        "FG_WHITE": (205, 214, 244), # #cdd6f4 Text
        "FG_MODEL": (17, 17, 27),    # #11111b Crust dark text
        "FG_GIT":   (166, 227, 161), # #a6e3a1 Green
        "BAR_OK":   (166, 227, 161), # #a6e3a1 Green
        "BAR_WARN": (249, 226, 175), # #f9e2af Yellow
        "BAR_CRIT": (243, 139, 168), # #f38ba8 Red
    },
}

P = PALETTES.get(COLOR_SCHEME, PALETTES["default"])
C_MODEL  = P["C_MODEL"]
C_DIR    = P["C_DIR"]
C_DIM    = P["C_DIM"]
C_GIT    = P["C_GIT"]
C_SEP    = P["C_SEP"]
C_PCT    = P["C_PCT"]
C_OK     = P["C_OK"]
C_WARN   = P["C_WARN"]
C_CRIT   = P["C_CRIT"]
RST      = "\033[0m"
BG_MODEL = P["BG_MODEL"]
BG_DARK  = P["BG_DARK"]
BG_MID   = P["BG_MID"]
BG_LIGHT = P["BG_LIGHT"]
BG_GIT   = P["BG_GIT"]
FG_WHITE = P["FG_WHITE"]
FG_MODEL = P["FG_MODEL"]
FG_GIT   = P["FG_GIT"]

SEP = f"{C_SEP}\u2502{RST}"

# ── Helpers ───────────────────────────────────────────────────────
def _fg(r, g, b):
    return f"\033[38;2;{r};{g};{b}m"

def _bg(r, g, b):
    return f"\033[48;2;{r};{g};{b}m"

def _segments(path):
    return [s for s in path.replace("\\", "/").split("/") if s]

def _powerline_chain(segments):
    """Build full powerline from [(bg_rgb, fg_rgb, text), ...]."""
    parts = []
    for i, (bg, fg, text) in enumerate(segments):
        parts.append(f"{_bg(*bg)}{_fg(*fg)} {text} ")
        if i < len(segments) - 1:
            next_bg = segments[i + 1][0]
            parts.append(f"{_bg(*next_bg)}{_fg(*bg)}\ue0b0")
        else:
            parts.append(f"{RST}{_fg(*bg)}\ue0b0{RST}")
    return "".join(parts)

# ── Rate limit helpers ───────────────────────────────────────────
def _fmt_reset(reset_epoch):
    """Convert Unix timestamp to compact remaining time: '3h45m', '4d3h'."""
    if not reset_epoch:
        return ""
    try:
        now = datetime.now(timezone.utc)
        reset = datetime.fromtimestamp(reset_epoch, tz=timezone.utc)
        total_min = max(0, int((reset - now).total_seconds()) // 60)
        if total_min < 60:
            return f"{total_min}m"
        hours = total_min // 60
        mins = total_min % 60
        if hours < 24:
            return f"{hours}h{mins:02d}m"
        days = hours // 24
        rem_h = hours % 24
        return f"{days}d{rem_h}h"
    except Exception:
        return ""

def _time_pct(reset_epoch, window_hours):
    """How far through the time window are we (0-100)."""
    if not reset_epoch:
        return 0
    try:
        now = datetime.now(timezone.utc)
        reset = datetime.fromtimestamp(reset_epoch, tz=timezone.utc)
        remaining_sec = max(0, (reset - now).total_seconds())
        window_sec = window_hours * 3600
        elapsed_sec = window_sec - remaining_sec
        return max(0, min(100, int(elapsed_sec / window_sec * 100)))
    except Exception:
        return 0

def _rl_color(pct):
    """Return (fg_ansi, bar_rgb) for rate limit percentage."""
    if pct < 60:
        return C_OK, P["BAR_OK"]
    elif pct < 80:
        return C_WARN, P["BAR_WARN"]
    else:
        return C_CRIT, P["BAR_CRIT"]

def _rl_bar(pct, time_pct_val, width=10):
    """Build usage bar with time position marker.

    Fill (█) = usage percentage, Marker (░ in C_PCT) = time position in window.
    If fill is ahead of marker, usage velocity is too high.
    """
    filled = max(0, pct * width // 100)
    marker_pos = max(0, min(width - 1, time_pct_val * (width - 1) // 100))
    color, _ = _rl_color(pct)

    chars = []
    for i in range(width):
        if i == marker_pos:
            chars.append(f"{C_PCT}\u2591{RST}")  # ░ in subtext1 #bac2de — time marker
        elif i < filled:
            chars.append(f"{color}\u2588{RST}")
        else:
            chars.append(f"{C_DIM}\u2591{RST}")
    return "".join(chars)

def _rl_part(icon, pct, reset_iso, window_hours):
    """Build ' 11% █░░█░░░░░░ 3h17m' — icon, pct, bar, reset time."""
    color, _ = _rl_color(pct)
    t_pct = _time_pct(reset_iso, window_hours)
    bar = _rl_bar(pct, t_pct)
    reset_str = _fmt_reset(reset_iso)
    reset_part = f" {C_DIM}{reset_str}{RST}" if reset_str else ""
    return f"{color}{icon} {pct}%{RST} {bar}{reset_part}"

# ── Git branch ────────────────────────────────────────────────────
branch_name = ""
try:
    subprocess.check_output(["git", "rev-parse", "--git-dir"], stderr=subprocess.DEVNULL)
    branch_name = subprocess.check_output(
        ["git", "branch", "--show-current"], text=True, stderr=subprocess.DEVNULL
    ).strip()
except Exception:
    pass

# ── Context ───────────────────────────────────────────────────────
BAR_RGB = P["BAR_OK"] if pct < 60 else P["BAR_WARN"] if pct < 80 else P["BAR_CRIT"]

# ── Output ────────────────────────────────────────────────────────
is_powerline = STYLE in ("powerline", "powerline-short")

if is_powerline:
    segs = []

    # Model segment
    segs.append((BG_MODEL, FG_MODEL, f"\U000F16A3 {model}"))

    # Dir segments
    path_segs = _segments(cwd)
    if STYLE == "powerline-short":
        path_segs = [s[0] if i < len(path_segs) - 1 else s for i, s in enumerate(path_segs)]
    for i, seg in enumerate(path_segs):
        if i == 0:
            bg = BG_DARK
        elif i == len(path_segs) - 1:
            bg = BG_LIGHT
        else:
            bg = BG_MID
        segs.append((bg, FG_WHITE, f"\ue5ff {seg}" if i == 0 else seg))

    # Git segment
    if branch_name:
        segs.append((BG_GIT, FG_GIT, f"\ue725 {branch_name}"))

    # Context segment (dynamic width)
    pad = max(1, pct * 8 // 100)
    segs.append((BAR_RGB, FG_WHITE, f"{' ' * pad}{pct}%"))

    # Rate limit segments (powerline) — one per window, individual severity color
    if SHOW_RATE_LIMITS in ("all", "5h") and rl_5h_pct:
        _, bg5 = _rl_color(rl_5h_pct)
        r5 = _fmt_reset(rl_5h.get("resets_at"))
        segs.append((bg5, FG_WHITE, f"\uf017 {rl_5h_pct}% {r5}"))
    if SHOW_RATE_LIMITS in ("all", "7d") and rl_7d_pct:
        _, bg7 = _rl_color(rl_7d_pct)
        r7 = _fmt_reset(rl_7d.get("resets_at"))
        segs.append((bg7, FG_WHITE, f"\uef38 {rl_7d_pct}% {r7}"))

    print(_powerline_chain(segs))

else:
    # ── Minimal output ────────────────────────────────────────────
    # Dir
    path_segs = _segments(cwd)
    dirname = path_segs[-1] if path_segs else "?"
    dir_part = f"{C_DIR}\ue5ff {dirname}{RST}"

    # Git
    branch_part = f" {SEP} {C_GIT}\ue725 {branch_name}{RST}" if branch_name else ""

    # Context (block bar)
    bar_fg = _fg(*BAR_RGB)
    filled = pct * 10 // 100
    ctx_part = f"{bar_fg}{chr(0x2588) * filled}{chr(0x2591) * (10 - filled)}{RST} {C_PCT}{pct}%{RST}"

    # Rate limits
    rl_part = ""
    rl_items = []
    if SHOW_RATE_LIMITS in ("all", "5h") and rl_5h_pct:
        rl_items.append(_rl_part("\uf017", rl_5h_pct, rl_5h.get("resets_at"), 5))
    if SHOW_RATE_LIMITS in ("all", "7d") and rl_7d_pct:
        rl_items.append(_rl_part("\uef38", rl_7d_pct, rl_7d.get("resets_at"), 168))
    if rl_items:
        rl_part = f" {SEP} {' '.join(rl_items)}"

    print(f"{C_MODEL}\U000F16A3 {model}{RST} {SEP} {dir_part}{branch_part} {SEP} {ctx_part}{rl_part}")
