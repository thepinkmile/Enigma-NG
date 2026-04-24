# Checkpoint 015 — Rotor CPLD Upgrade, DIP Switch Architecture Finalised
**Date:** 2026-04-11
**Session:** Prior session (stub — original file not committed to repo)

---
## Overview
Rotor and Stator CPLDs upgraded from EPM240T100I5N to EPM570T100I5N to accommodate increased
UFM capacity (21 forward maps per rotor). DIP switch architecture finalised:
- SW1 (6-bit, input side): ring setting — added to STGC-decoded position (mod N)
- SW2 (6-bit, input side): [4:0] = map index, [5] = direction (0=forward, 1=reverse)
- SW3 (6-bit, output side): [4:0] = map index, [5] = direction (0=forward, 1=reverse)
Direction bit doubles usable configurations from 21 to 42 per side without reprogramming.
Variant design files (Rotor_26_Char_Design.md, Rotor_64_Char_Design.md) created.
## Key Decisions
- EPM570T100I5N replaces EPM240 on Rotor (×30) and Stator (×1) — 570 LEs, greater UFM
- 21 UFM maps × 2 direction = 42 effective substitution configurations per side
- Consolidated BOM: EPM240T100I5N = 6 (Encoder only), EPM570T100I5N = 31 (Stator + 30 Rotors)
