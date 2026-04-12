# Checkpoint 018 — Rotor Capacitive Encoder Finalised; JLCPCB Single-Side Open

**Date:** 2026-04-12
**Session:** bb01fc15-4ce2-4b66-94c1-db3fabe7b119

---

## Overview

Completed all Rotor position encoder design decisions and document updates. The capacitive
single-track encoder architecture (FDC2114RGER, STGC track patterns, CPLD lookup table +
mod-N adder, Virtual JTAG position readback) is now fully documented across all relevant files.
Session concluded with a new open item: JLCPCB only supports single-side component assembly, and
the Rotor PCB currently has components on both sides. The user has a resolution plan to be
discussed next session. The Rotor detailed design review cycle is therefore deferred.

---

## Work Done This Session

### Design Decisions Made

| Decision | Details |
|----------|---------|
| Position encoder technology | Capacitive (TI FDC2114RGER) — replaces AS5600 magnetic. Shroud = passive conductive-ink track, no magnets |
| PCB diameter | Ø100mm (50mm radius) — satisfies arc-per-segment ≥ 4.9mm for N=64 at r=47mm |
| Track patterns | N=26 K=5: `00000100011001010011101111` (6 invalid codes); N=64 K=6: `0000001111110111100111010111000110110100110010110000101010001001` (de Bruijn, all 64 valid) |
| CPLD position decode | Combinational lookup ROM in VHDL; mod-N adder inside CPLD — no external adder hardware |
| Virtual JTAG readback | ALTERA_VIRTUAL_JTAG megafunction, USER0 UDR, 6-bit; JDB FT232H reads all 30 in one scan pass |
| Sensor IC | 2× FDC2114RGER per rotor: U2 (0x2A, S0–S3), U3 (0x2B, S4–S5); Mouser 595-FDC2114RGER, DigiKey 296-43218-1-ND |

### Commits

| Commit | Description |
|--------|-------------|
| `ff0c7c9` | Replace AS5600 with single-track capacitive encoder (FDC2114) — 5 files |
| `6e2bd5a` | Design Log: DEC-026 (capacitive encoder) + DEC-027 (Virtual JTAG readback) |
| `2308f02` | Rotor Design_Spec: FR-ROT-09 (Virtual JTAG UDR) |

### Files Modified

- `design/Electronics/Rotor/Design_Spec.md` — FR-ROT-02/08/09, DR-ROT-03/09, §1, §2.1 rewrite, §3.2, BOM U2→FDC2114 + U3 added
- `design/Electronics/Rotor/Rotor_26_Char_Design.md` — §5 updated, §7 added (geometry, track, lookup)
- `design/Electronics/Rotor/Rotor_64_Char_Design.md` — §5–§6 updated, §7 added (geometry, track, lookup)
- `design/Electronics/Rotor/Board_Layout.md` — Ø100mm, FDC2114 in ASCII diagram
- `design/Electronics/Consolidated_BOM.md` — AS5600 → 2× FDC2114RGER (60 units total)
- `design/Design_Log.md` — DEC-026, DEC-027

---

## Open Items (Rotor)

### BLOCKED: JLCPCB Single-Side Component Placement

JLCPCB only assembles components on one side of the PCB. The Rotor board currently has
components on both sides (e.g. connectors ERM8/ERF8 on front, CPLD and passives may conflict).
The user has a resolution plan. **Rotor detailed design review is blocked on this.**

Next session: agree the resolution approach, update Board_Layout.md and Design_Spec.md
accordingly, then launch the review cycle.

### STGC_Generator.py Relocation

`design/Electronics/Reflector/STGC_Generator.py` — should be moved to `design/Electronics/Rotor/`
and updated to use the relaxed unique-only constraint (the current Gray single-bit-change
constraint produces no valid solution for N=26 or N=64). Deferred to tidy-up pass.

### GUI App Cross-Reference

No mention of rotor position display in GUI App Design_Spec. Cross-reference to DEC-027 /
FR-ROT-09 to be added when GUI App spec is worked.

---

## Technical Reference

### Encoder Geometry

| Parameter | N=26 | N=64 |
|-----------|------|------|
| Sensors (K) | 5 | 6 |
| PCB radius | 50mm (Ø100mm) | 50mm (Ø100mm) |
| Sensor pad radius | 47mm | 47mm |
| Degrees/segment | 13.846° | 5.625° |
| Arc/segment at r=47mm | 12.1mm | 4.91mm |
| Sensor pitch | 13.846° | 5.625° |
| Invalid codes | 6 (jam detection) | 0 (de Bruijn) |

### FDC2114RGER Per Rotor

| IC | I²C Addr | Channels | Sensors |
|----|---------|----------|---------|
| U2 | 0x2A | 0–3 | S0–S3 |
| U3 | 0x2B | 0–1 (64-char) / 0 (26-char) | S4–S5 / S4 |

Unused channels: IN pin tied to GND via 100kΩ.

### Virtual JTAG (FR-ROT-09)

- Megafunction: `ALTERA_VIRTUAL_JTAG` in EPM570T100I5N
- Instruction: USER0
- UDR width: 6 bits (effective position = STGC-decoded + SW1 mod N)
- 26-char variant: bits [4:0] valid, bit [5] = 0
- JDB FT232H reads all 30 rotors in one serial scan (180 bits)
- Cipher logic runs independently on CPLD system clock

---

## Next Steps

1. **Next session:** Discuss and agree JLCPCB single-side resolution plan
2. Update `Rotor/Board_Layout.md` and `Rotor/Design_Spec.md` per agreed approach
3. Relocate and update `STGC_Generator.py`
4. Launch Rotor detailed design review cycle (2 consecutive clean passes)
5. Add GUI App cross-reference to DEC-027 / FR-ROT-09

---

## Known Correct (for Rotor review agent)

The following are confirmed correct and must not be flagged:

- FDC2114RGER ×2 per rotor (U2 + U3) — replaces AS5600
- EPM570T100I5N (not EPM240) — upgraded for UFM capacity
- Track patterns: N=26 `00000100011001010011101111`, N=64 `0000001111110111100111010111000110110100110010110000101010001001`
- Ø100mm PCB, sensor pads at r≈47mm
- SW1 = ring setting (input side, 6-bit, mod-N adder in CPLD)
- SW2 = forward map select (input side, 5 map + 1 direction bit)
- SW3 = return map select (output side, 5 map + 1 direction bit)
- 21 UFM maps; direction bit doubles to 42 effective configurations per side
- J1–J3 ERM8 (male, input side); J4–J6 ERF8 (female, output side)
- Pre-existing lint warnings (do not flag): User_Manual.md:134, Global_Routing_Spec.md:72
