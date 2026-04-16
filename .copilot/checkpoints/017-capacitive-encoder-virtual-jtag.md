# Checkpoint 017 — Capacitive Encoder Design, Virtual JTAG Readback

**Date:** 2026-04-12
**Session:** <sanitized-session-id>

---

## Overview

Position encoder technology decision made: single-track capacitive encoder using TI FDC2114RGER
(×2 per rotor). AS5600 magnetic encoder discarded. STGC track patterns computed from first
principles for both variants. CPLD mod-N adder and STGC lookup table confirmed as VHDL-only
(no external hardware). Virtual JTAG (ALTERA_VIRTUAL_JTAG USER0 UDR) chosen for GUI App
position readback. Design documents updated; DEC-026, DEC-027, FR-ROT-09 added.

## Commits

| Commit | Description |
|--------|-------------|
| `ff0c7c9` | Replace AS5600 with single-track capacitive encoder (FDC2114) |
| `6e2bd5a` | Design Log: DEC-026 + DEC-027 |
| `2308f02` | Rotor Design_Spec: FR-ROT-09 |

## Key Decisions

- FDC2114RGER ×2 per rotor: U2 (0x2A, S0–S3), U3 (0x2B, S4–S5)
- PCB Ø100mm; sensor pads at r≈47mm
- N=26 track: `00000100011001010011101111` (K=5, 6 invalid codes)
- N=64 track: `0000001111110111100111010111000110110100110010110000101010001001` (K=6, de Bruijn)
- STGC → binary: combinational lookup ROM in CPLD VHDL (same mechanism both variants)
- Mod-N adder (SW1 ring offset) entirely in CPLD logic
- Virtual JTAG USER0 UDR (6-bit): effective position readable by JDB FT232H without extra pins

## Next Steps at End of This Checkpoint

- JLCPCB single-side component placement constraint needs resolution before Rotor review
- STGC_Generator.py needs relocation from Reflector/ to Rotor/
- Rotor detailed design review cycle pending
