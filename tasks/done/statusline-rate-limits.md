# Statusline: Rate Limits megjelenítés

**Terv:** `C:\Users\peter\.claude\plans\snazzy-seeking-hickey.md`
**Dátum:** 2026-03-20
**Státusz:** done

## Cél
Rate limit usage (5h session + 7d weekly) megjelenítése a statusline-ban, claude-counter stílusú mini barral (fill + time marker).

## Lépések
- [x] Terv elkészítése és jóváhagyás
- [x] Step 0: rate_limits JSON struktúra verifikáció (debug dump)
  - Kulcsok: `five_hour`, `seven_day` (nem `5_hour`/`7_day`)
  - `resets_at`: Unix epoch timestamp (nem ISO string)
- [x] Step 1: statusline.py módosítás (helperek + output)
- [x] Tesztelés mock adattal (mind 4 stílus OK)
- [x] Debug dump eltávolítása
- [x] Marker fix: ▎ → fehér █ (szín kontraszt, nincs szélességi ugrás)
- [x] Bar szélesség: 5 → 10 karakter (konzisztens a context barral)
- [x] Layout redesign (minimal/breadcrumb): ikon + % + bar + reset idő
- [x] Ikonok:  (session/5h),  (weekly/7d)
- [x] Powerline: két külön szegmens egyedi severity színnel + ikonok
- [x] Éles tesztelés befejezése, task lezárása
- [x] Skill review (best practices + UX) → arg átnevezés, feedback, allowed-tools szűkítés
- [x] Docstring cleanup, audit
