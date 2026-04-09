# Statusline: Rate Limit Marker Redesign

**Dátum:** 2026-03-25
**Státusz:** done

## Cél
Rate limit bar időmarker vizuális finomítás — könnyebben megkülönböztethető a filled tickektől.

## Változások
- [x] Marker karakter: `█` (U+2588) → `░` (U+2591) — könnyebb, nem teli blokk
- [x] Marker szín: `C_DIR` (fehér #cdd6f4) → `C_PCT` (subtext1 #bac2de) — visszafogott, illeszkedik a témába
- [x] Docstring frissítés a `_rl_bar()` függvényben

## Eredmény
```
Előtte: ██████░░░░  (marker és filled egyaránt █, csak szín különbözteti meg)
Utána:  █████░░░░░  (marker ░ subtext1-ben, filled █ severity színben, empty ░ dim)
```

## Érintett fájl
- `C:\Users\peter\.claude\statusline.py` — `_rl_bar()` függvény (line ~176)
