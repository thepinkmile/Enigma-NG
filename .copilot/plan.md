# Enigma-NG Session Plan

> Canonical state: `.copilot/plan.md` in the repository root (gitignored).
> Update this file at the end of each session or at meaningful milestones.
> At the start of a new session, read this file plus relevant checkpoints in `.copilot/checkpoints/`.

---

## Overview

All board detailed designs are functionally complete and review cycles passed. The Rotor design
was substantially updated in session bb01fc15 (checkpoints 014–019): split two-board architecture
(Board A input / Board B output, Ø92mm each, keyed IDC J_INT), dual-track capacitive encoder,
STGC/RBGC patterns corrected, U4 FDC2114RGER added for N=26 5th sensor, full Mechanical/Rotor
spec with tolerance table. Review cycle R1–R5 complete (R4+R5 clean). User to manually review
all design files before declaring the design complete.

Review rule: 2 consecutive clean passes — lint (`markdownlint`) AND deep-dive content.

---

## Board Design Status

| Board | Status |
|-------|--------|
| Power Module | ✅ Complete (checkpoint 011) |
| Stator | ✅ Complete (checkpoint 013/016) |
| Reflector | ✅ Complete |
| Extension | ✅ Complete |
| JDB | ✅ Complete |
| Controller | ✅ Complete (checkpoint 012) |
| Encoder | ✅ Complete (R56+R57 clean — checkpoint 009) |
| Rotor | ✅ Complete (R4+R5 clean — checkpoint 019) |

---

## Todos

| ID | Title | Status |
|----|-------|--------|
| `kicad-setup-docs` | KiCad setup documentation | pending |
| `user-manual-review` | User manual review of all design files before final sign-off | pending |

---

## Immediate Next Steps

1. **User manual review** — manually review all design files and provide observations before declaring design complete.
2. **KiCad setup documentation** (`kicad-setup-docs` todo).
3. **Remaining OWIs** as agreed (see list below).

---

## Checkpoint Procedure

Every checkpoint MUST include ALL of the following steps (in order):

1. **Write checkpoint file** to `.copilot/checkpoints/NNN-short-title.md` in the **repository**.
2. **Update checkpoint index** at `.copilot/checkpoints/index.md` in the **repository**.
3. **Update `.copilot/plan.md`** in the **repository** to reflect current state.
4. **Copy any new agent-prompt files** to `.copilot/agent-prompts/` in the **repository**.
5. **Verify** all items present in `C:\_DATA_\Repositories\github\Enigma-NG\.copilot\` before declaring complete.

> The session-state folder is ephemeral. The repository `.copilot\` folder is the canonical persistent store.

---

## Critical Notes

### Standard Review File List (28 files)

Core files + Rotor variant files:

- design/Electronics/Consolidated_BOM.md
- design/Design_Log.md
- design/Electronics/Power_Budgets.md
- design/Electronics/Power_Module/Design_Spec.md + Board_Layout.md
- design/Electronics/Stator/Design_Spec.md + Board_Layout.md
- design/Electronics/Reflector/Design_Spec.md + Board_Layout.md
- design/Electronics/Extension/Design_Spec.md + Board_Layout.md
- design/Electronics/JTAG_Daughterboard/Design_Spec.md + Board_Layout.md
- design/Electronics/Controller/Design_Spec.md + Board_Layout.md
- design/Electronics/Encoder/Design_Spec.md + Board_Layout.md
- design/Electronics/Rotor/Design_Spec.md + Board_Layout.md
- design/Electronics/Rotor/Rotor_26_Char_Design.md
- design/Electronics/Rotor/Rotor_64_Char_Design.md
- design/Electronics/Investigations/JTAG_Integrity.md
- design/Standards/Global_Routing_Spec.md
- design/Guides/Maintenance_Guide.md

### Lint Process

- PATH refresh: `$env:PATH = [System.Environment]::GetEnvironmentVariable("PATH","Machine")+";"+[System.Environment]::GetEnvironmentVariable("PATH","User")`
- Run: `.\node_modules\.bin\markdownlint.cmd --fix "design/**/*.md"` then without `--fix`.
- Pre-existing MD013 lint errors (acceptable — do not flag): User_Manual.md:134, Global_Routing_Spec.md:72.

### JTAG Topology (CRITICAL — agents repeatedly get this wrong)

- TCK/TMS/TDI via **BtB connectors** (ERM8/ERF8 Samtec 0.8mm pitch) through entire rotor stack.
  NO ribbon cables used for JTAG within the rotor stack.
- JTAG chain terminates at the **Reflector**. Reflector R1 (22Ω) = end-of-chain TDO damping.
- Reflector J4 → Stator J7 ribbon: pin 15=TTD_RETURN (JTAG), pins 3–14=ENC_IN/OUT (plugboard
  config for Stator CPLD — NOT JTAG extension).
- Extension U1 (SN74LVC2G125DCUR) re-buffers TCK/TMS every 5-rotor group — CORRECT, NEVER REMOVE.
- Stator R7–R15 (75Ω) and Encoder R7–R8 are for encoder RIBBON CABLE ports (J4/J5/J6) ONLY.

### Extension U1 Buffer (NEVER REMOVE)

- Extension board has U1 (SN74LVC2G125DCUR) + C6 (0.1µF bypass), FR-EXT-01/02, DR-EXT-04/05/06.
- Consolidated BOM: SN74LVC2G125DCUR EXT=1, Total=2.
- Design_Spec is authoritative; BOM must match it.

### Key Correct Values

- GPIO 20=SW_LED_CTRL, GPIO 24=POE_STAT (active-low) — correct in ALL files
- Peak load 8.76A; LDO 2.11A / ~0.46W / 30% headroom; LMQ 73.0%; PoE 73.9%; zero exceptions
- CSS2H shunt build qty: 3 (JDB=1, STR=1, PM=1)
- Consolidated BOM: SN74LVC2G125DCUR JDB=1, EXT=1, Total=2
- Consolidated BOM: 0.1µF X7R 0402 PM=15, Total=509
- Consolidated BOM: MIC1555YM5-TR PM=2, BSS138 PM=2
- Consolidated BOM: EPM240T100I5N = 6 (Encoder only); EPM570T100I5N = 31 (Stator + 30 Rotors)
- Consolidated BOM: FDC2114RGER = 30 (U2, all rotors) + 30 (U3, N=64 rotors) + TBD (U4, N=26 rotors)
- LTC3350 BACKUP threshold: 4.644V (R14=28.7kΩ ERA-3ARB2872V)
- SW2 wired to PWR_BUT (graceful power key), NOT GLOBAL_EN
- Link-Alpha pin 48: PWR_BUT (was GND)
- PWR_GD (GPIO 27) = rail-health telemetry only; does NOT trigger shutdown
- Primary shutdown: LTC3350 /INTB → U15 MIC1555 → Q5 BSS138 → PWR_BUT (3.01 s LOW)
- DEC-025 (last before session bb01fc15): CM5 shutdown mechanism (Software category)
- DEC-026: Capacitive encoder replaces AS5600 (FDC2114RGER, STGC track patterns) — superseded by DEC-028
- DEC-027: Virtual JTAG USER0 UDR for rotor position readback (FR-ROT-09)
- DEC-028: Split two-board rotor architecture (Board A + Board B, keyed IDC J_INT)

### Rotor-Specific Correct Values (NEVER flag as errors)

- **Two-board split:** Board A (input, Ø92mm) + Board B (output, Ø92mm); 15mm total; 11.8mm inner gap
- Board A: EPM570T100I5N U1, FDC2114RGER U2 (0x2A), FDC2114RGER U4 (0x2B, N=26 only), SW1, SW2, J1–J3 ERM8 male
- Board B: FDC2114RGER U3 (0x2B, N=64 only; DNP N=26), SW3, J4–J6 ERF8 female
- J_INT: Würth 61201221721, 2×12 24-pin keyed IDC; pin 11=TDO A→B; pins 15–16=SW3[4:5]; pins 17–18=SDA/SCL; pins 19–22=SW3[0:3] B→A
- FDC2114RGER U2 addr 0x2A (N=64: ch0–2=bits[5:3]; N=26: ch0–3=STGC bits[3:0])
- FDC2114RGER U4 addr 0x2B ch0=STGC bit[4] — N=26 Board A only
- FDC2114RGER U3 addr 0x2B ch0–2=bits[2:0] — N=64 Board B only (U3 and U4 mutually exclusive)
- Sensor pads at r=44mm on PCB flat face; capacitive gap 0.5mm ±0.15mm (bearing-controlled)
- N=26 track (K=5): `00000100011001010011101111` — all 26 5-bit windows unique
- N=64 dual-track RBGC (corrected R1 — Track B Bit 0 and Bit 1 were wrong):
  - A5: `0000000000000000000000000000000011111111111111111111111111111111`
  - A4: `0000000000000000111111111111111111111111111111110000000000000000`
  - A3: `0000000011111111111111110000000000000000111111111111111100000000`
  - B2: `0000111111110000000011111111000000001111111100000000111111110000`
  - B1: `0011110000111100001111000011110000111100001111000011110000111100`
  - B0: `0110011001100110011001100110011001100110011001100110011001100110`
- CPLD XOR decode: B5=G5, B4=B5⊕G4, B3=B4⊕G3, B2=B3⊕G2, B1=B2⊕G1, B0=B1⊕G0
- SW1 (6-bit, Board A): ring setting, mod-N adder entirely in CPLD VHDL
- SW2 (6-bit, Board A): [4:0]=map index, [5]=direction
- SW3 (6-bit, Board B): [4:0]=map index, [5]=direction
- 21 UFM maps stored in EPM570 UFM; UFM size = 21 × 384 bits = 8,064 bits
- J1–J3 ERM8 male (input side Board A); J4–J6 ERF8 female (output side Board B)
- FR-ROT-09: ALTERA_VIRTUAL_JTAG megafunction, USER0 UDR, 6-bit effective position
- TDO in J_INT travels A→B (CPLD on Board A → J4 connector on Board B)

### Stale Values (must NEVER reappear)

- TPS259807ONRGER, TPS259803ONRGER, TPS25980RPWR, TPS7A8333PRMWR, LMQ61460ARUMR
- C21397, C15281, C2688, 1276-1935-1-ND, WM7843-ND, C841785
- ERA-3ARB2323V, ERA-3ARB2672V (old R14), ERJ-2RKF8200X
- WSON-8 2×2mm, WSON-12, SOIC-8 for TPS2065C, VQFN for TPD4E05U06, SOT-23-6 for buffer
- 9.05A peak, 2.20A LDO, 75.4% LMQ, 76.2% PoE, 27% LDO headroom, "accepted exception"
- GPIO 20=POE_STAT or GPIO 24=SW_LED_CTRL (swapped — both wrong)
- "RST" as signal/net name; + prefix on net names
- "Extension: no U1 buffer" or "passive pass-through" — WRONG
- Pull-up on U7 EN (must be pull-DOWN to GND)
- TPD12S016, TPD4E1U06DBVR
- 4.40V as LTC3350 backup threshold (correct: 4.644V)
- "SW2 wired to GLOBAL_EN / hard reset" (SW2 = PWR_BUT)
- "PWR_GD triggers shutdown" (telemetry only)
- 0.1µF X7R 0402 PM=14 or Total=508 (correct: PM=15, Total=509)
- MIC1555 PM=1 (correct: PM=2); BSS138 PM=1 (correct: PM=2)
- EPM240T100I5N on Rotor or Stator (correct: EPM570T100I5N)
- AS5600 anywhere on Rotor (replaced by FDC2114RGER)
- "Single magnet" or "diametrically magnetised" for Rotor position sensor
- "Ø100mm" for Rotor PCB (correct: Ø92mm; shroud outer is Ø100mm)
- "de Bruijn" as an active N=64 encoder pattern (replaced by RBGC; de Bruijn only in DEC-028 rationale/history)
- Old N=64 Track B patterns: Bit 1 as period-16 `0011111100001111` repeating, Bit 0 as simple alternating `01`
- "FDC2114 reads all 5 STGC sensors from U2" (impossible — 4 channels max; U4 added for 5th)
- "U4 NOT POPULATED" for N=26 builds (U4 IS populated for N=26)
- "U3 populated for N=26" (U3 DNP for N=26)
- DIR/CLK on J_INT pins 15–16 (correct: SW3[4:5] B→A)
- Single-board rotor (correct: two-board split)

### Key Design Decisions

- All capacitors: X7R dielectric
- JTAG CI traces: 0.127mm (5 mil) targeting 50Ω — documented exception to Global_Routing_Spec
- Net names: NO + prefix (e.g. `5V_MAIN` not `+5V_MAIN`)
- Controller J1+J2: both ERF8 female (slide-in assembly convenience)
- U7 EN: active-LOW, pull-down to GND
- Extension U1 buffers TCK/TMS every 5 rotors (not per-rotor)
- PWR_BUT = primary shutdown trigger + manual power key; 3.01 s one-shot from U15 MIC1555
- Rotor position encoder: single-track capacitive, FDC2114RGER, STGC patterns
- Rotor position readback: ALTERA_VIRTUAL_JTAG USER0 UDR (DEC-027, FR-ROT-09)

### Open Work Items (OWI)

- OWI-001: Test coupons (break-off PCB) per board
- OWI-002: PAS definitions per board
- OWI-003: VHDL pseudo-code and CPLD config plans
- OWI-018: ENIG rib clearway bonding pad
- OWI-019: STGC_Generator.py — relocate to `Rotor/`, update to relaxed unique-only algorithm
- OWI-020: GUI App Design_Spec — add cross-reference to DEC-027/FR-ROT-09 for position display
- OWI-021: Mechanical stub files — complete Encoder, Stator, Reflector, Extension, JDB, Power_Module mechanical specs
- Deferred: SW1 vintage switch research; CM5 PWR_BUT timing thresholds (verify at schematic capture)