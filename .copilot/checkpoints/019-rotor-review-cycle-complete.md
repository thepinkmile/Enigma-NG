# Checkpoint 019 — Rotor Review Cycle Complete, Mechanical Specs Added

## Overview

This session resolved the outstanding JLCPCB single-side SMT assembly constraint for the Rotor
board by splitting it into two circular PCBs (Board A = input side, Board B = output side)
connected by a keyed 2×12 IDC header. This simultaneously defines rotor physical thickness
(~15mm total, matching an original Enigma rotor), enables dual-track capacitive encoding, and
satisfies JLCPCB single-side placement constraints.

A full `design/Mechanical/` folder structure was created with a complete Rotor mechanical spec
and tolerance table, plus six stubs for remaining boards. A 5-round review cycle was run with
R1–R3 producing fixes and R4+R5 both clean (confirming sign-off).

---

## Work Done

### Architecture Decision (DEC-028)

- Rotor split into Board A (Ø92mm, input side) and Board B (Ø92mm, output side)
- Connected by Würth 61201221721 — 2×12 24-pin keyed IDC header (J_INT), manually assembled post-JLCPCB SMT
- Board A: CPLD EPM570T100I5N (U1), FDC2114RGER U2 (addr 0x2A), FDC2114RGER U4 (addr 0x2B, N=26 only), SW1, SW2, J1/J2/J3 ERM8 male
- Board B: FDC2114RGER U3 (addr 0x2B, N=64 only; DNP for N=26), SW3, J4/J5/J6 ERF8 female
- Total rotor assembly: 15mm; 11.8mm gap between inner PCB faces
- J_INT pinout: pin 11=TDO A→B; pins 15–16=SW3[4:5] B→A; pins 17–18=SDA/SCL; pins 19–22=SW3[0:3] B→A; 3V3_ENIG ×4; GND ×4

### Capacitive Encoder Architecture

- Shroud = rotating aluminium outer ring (no electronics); PCB = static inner hub
- Shroud flanges (brake-caliper style) extend over both PCB flat faces
- Gray code pattern = milled slots in aluminium flange inner faces
- Sensor electrodes = bare copper pads at r=44mm on PCB flat face, connected to FDC2114
- Solid aluminium → high capacitance; milled slot (air) → low capacitance
- Shroud must be electrically FLOATING; ceramic/nylon rolling elements mandatory

### Critical Fixes in Review Cycle

**R1 (30 issues found):**
- N=64 Gray code Bit 0 and Bit 1 patterns corrected — previous patterns caused 20/64 multi-bit transitions
- N=26 design gap resolved: added U4 FDC2114RGER for 5th STGC sensor (FDC2114 has only 4 channels)
- J_INT pins 15–16 repurposed: DIR/CLK → SW3[4:5]
- EPM240 stale references replaced with EPM570 in 5 files
- TDO direction corrected to A→B in J_INT

**R2 (6 issues):** Remaining DEC-026 "conductive ink" phrase; U4 propagation gaps in Design_Spec.md  
**R3 (3 issues):** U4 missing from Board_Layout.md Board A table; Controller SYS_RESET_N EPM240-only (2 occurrences)  
**R4+R5:** CLEAN — two consecutive clean passes

### Mechanical Design Folder

Created `design/Mechanical/Rotor/Design_Spec.md` — full spec:
- Dimensions: PCB Ø92mm, shroud Ø100mm outer, 4mm wall, 15mm total assembly
- Tolerance table (canonical): PCB ±0.2mm, shroud inner bore H7, sensor gap 0.5mm ±0.15mm, Gray code slot angular ±0.1°
- Encoder slot geometry for both N=64 and N=26
- IDC assembly instructions (post-JLCPCB SMT, keyed connector mandatory)
- Bidirectional cross-references to/from all 4 Electronics/Rotor files

Stubs created: `design/Mechanical/Encoder/`, Stator/, Reflector/, Extension/, JTAG_Daughterboard/, Power_Module/ — all with placeholder `Design_Spec.md`

### Files Modified

- `design/Electronics/Rotor/Design_Spec.md` — two-board architecture, J_INT pinout, U4, FR/DR updated, W/N notation, I²C polling note, UFM sentence
- `design/Electronics/Rotor/Board_Layout.md` — Board A/B sections, ASCII diagrams, Ø92mm, U4 row
- `design/Electronics/Rotor/Rotor_64_Char_Design.md` — de Bruijn replaced with 3+3 RBGC, XOR decode, Gray code Bit 0 and Bit 1 corrected
- `design/Electronics/Rotor/Rotor_26_Char_Design.md` — all-on-Board-A, U4 added to §7, geometry updated
- `design/Electronics/Consolidated_BOM.md` — Würth IDC added, U2/U3/U4 FDC2114 descriptions updated
- `design/Design_Log.md` — DEC-028 added; DEC-026 superseded notice + 10 body corrections
- `design/Electronics/Boards_Overview.md` — EPM570 for Rotor/Stator, AS5600→FDC2114
- `design/Electronics/Reflector/Design_Spec.md` — EPM570 for Stator CPLD
- `design/Electronics/Extension/Design_Spec.md` — EPM570 in JTAG buffer note
- `design/Electronics/Controller/Design_Spec.md` — SYS_RESET_N targets both EPM240 (Encoder ×6) and EPM570 (Rotor ×30 + Stator ×1) — 2 occurrences
- `design/Standards/Global_Routing_Spec.md` — CPLD decoupling rule extended to EPM570

### Commits

| Hash | Description |
|------|-------------|
| `d0c08d9` | Split dual-board rotor architecture (DEC-028) |
| `3678f22` | Mechanical/Rotor spec + stubs + cross-references |
| `26b015b` | R1 fixes (19 fixes, 11 files) |
| `29254ae` | R2 fixes (6 fixes, 2 files) |
| `d6e96b6` | R3 fixes (3 fixes, 3 files) |

---

## Corrected Known-Correct List

The following are confirmed correct and must not be changed by future review agents:

- Board A Ø92mm / Board B Ø92mm; shroud Ø100mm outer, 4mm wall, 15mm total, 11.8mm gap
- EPM570T100I5N on Rotor (×30) and Stator (×1); EPM240T100I5N on Encoder (×6) only
- FDC2114RGER U2 addr 0x2A (bits[5:3] N=64 / STGC bits[3:0] N=26); U4 addr 0x2B CH0=STGC bit[4] N=26 Board A only; U3 addr 0x2B bits[2:0] N=64 Board B only
- J_INT: pin 11=TDO A→B; pins 15–16=SW3[4:5] B→A; pins 17–18=SDA/SCL; pins 19–22=SW3[0:3] B→A
- STGC track `00000100011001010011101111` — verified all 26 5-bit windows unique
- N=64 RBGC patterns:
  - A5: `0000000000000000000000000000000011111111111111111111111111111111`
  - A4: `0000000000000000111111111111111111111111111111110000000000000000`
  - A3: `0000000011111111111111110000000000000000111111111111111100000000`
  - B2: `0000111111110000000011111111000000001111111100000000111111110000`
  - B1: `0011110000111100001111000011110000111100001111000011110000111100`
  - B0: `0110011001100110011001100110011001100110011001100110011001100110`
- CPLD XOR decode: B5=G5, B4=B5⊕G4, B3=B4⊕G3, B2=B3⊕G2, B1=B2⊕G1, B0=B1⊕G0
- SYS_RESET_N targets both EPM240 (Encoder ×6) AND EPM570 (Rotor ×30 + Stator ×1)
- Extension U1 SN74LVC2G125DCUR VSSOP-8 buffers TCK/TMS — present, correct, intentional
- UFM: 21 maps × 384 bits = 8,064 bits (confirmed in both rotor char design files)
- Pre-existing lint warnings acceptable: `User_Manual.md:134` MD013, `Global_Routing_Spec.md:72` MD013

---

## Open Questions

None — all design questions resolved this session.

---

## Open Work Items (Deferred)

| ID | Item |
|----|------|
| OWI-001 | Test coupons per board |
| OWI-002 | PAS definitions per board |
| OWI-003 | VHDL pseudo-code and CPLD config plans |
| OWI-018 | ENIG rib clearway bonding pad |
| OWI-019 | STGC_Generator.py — relocate from Reflector/ to Rotor/, update to relaxed unique-only algorithm |
| OWI-020 | GUI App Design_Spec — add cross-reference to DEC-027/FR-ROT-09 for position display |
| OWI-021 | Mechanical stub files — complete Encoder, Stator, Reflector, Extension, JTAG_Daughterboard, Power_Module mechanical specs |

---

## Next Steps

1. **User manual review** — user will manually review all design files and provide observations before declaring design complete
2. **KiCad setup documentation** (`kicad-setup-docs` todo) — pending
3. Remaining OWIs above as agreed
