# Enigma-NG Session Plan

> Canonical state: `.copilot/plan.md` in the repository root (gitignored).
> Update this file at the end of each session or at meaningful milestones.
> At the start of a new session, read this file plus relevant checkpoints in `.copilot/checkpoints/`.

---

## Overview

All board detailed designs are functionally complete. The Rotor design was substantially updated
in session bb01fc15 (checkpoints 011–018): DIP switch architecture, variant split
(Rotor_26_Char / Rotor_64_Char), capacitive position encoder (FDC2114RGER ×2 per rotor), STGC
track patterns, CPLD lookup table + mod-N adder, Virtual JTAG position readback (DEC-026/027,
FR-ROT-09). The **Rotor detailed design review cycle** is next but is blocked pending a
JLCPCB single-side component assembly constraint resolution.

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
| Rotor | 🔶 Design docs updated (checkpoint 017/018); **blocked on JLCPCB single-side resolution** |

---

## Todos

| ID | Title | Status |
|----|-------|--------|
| `rotor-single-side` | Resolve JLCPCB single-side placement constraint | pending |
| `rotor-detailed-design` | Rotor detailed design review (2 clean passes) | pending (blocked) |
| `kicad-setup-docs` | KiCad setup documentation | pending |

---

## Immediate Next Steps

1. **Discuss JLCPCB single-side constraint** — user has a resolution plan. Agree approach,
   update `Rotor/Board_Layout.md` and `Rotor/Design_Spec.md` accordingly.
2. **Relocate STGC_Generator.py** — move from `design/Electronics/Reflector/` to
   `design/Electronics/Rotor/`; update to use relaxed unique-only constraint algorithm
   (current script produces no valid results for N=26 or N=64).
3. **Launch Rotor review cycle** — deep-dive pass, fix, repeat until 2 consecutive clean passes.
4. **GUI App cross-reference** — add position display note (DEC-027 / FR-ROT-09) when spec started.

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
- Consolidated BOM: FDC2114RGER = 60 (2× per rotor × 30 rotors)
- LTC3350 BACKUP threshold: 4.644V (R14=28.7kΩ ERA-3ARB2872V)
- SW2 wired to PWR_BUT (graceful power key), NOT GLOBAL_EN
- Link-Alpha pin 48: PWR_BUT (was GND)
- PWR_GD (GPIO 27) = rail-health telemetry only; does NOT trigger shutdown
- Primary shutdown: LTC3350 /INTB → U15 MIC1555 → Q5 BSS138 → PWR_BUT (3.01 s LOW)
- DEC-025 (last before this session): CM5 shutdown mechanism (Software category)
- DEC-026: Capacitive encoder replaces AS5600 (FDC2114RGER, STGC track patterns)
- DEC-027: Virtual JTAG USER0 UDR for rotor position readback (FR-ROT-09)

### Rotor-Specific Correct Values (NEVER flag as errors)

- FDC2114RGER ×2 per rotor: U2 (0x2A, ch0–3=S0–S3), U3 (0x2B, ch0–1=S4–S5)
- PCB Ø100mm; sensor pads at r≈47mm
- N=26 track (K=5): `00000100011001010011101111` — 6 invalid codes (jam detection)
- N=64 track (K=6): `0000001111110111100111010111000110110100110010110000101010001001` — de Bruijn, all valid
- SW1 (6-bit, input side): ring setting, mod-N adder entirely in CPLD VHDL
- SW2 (6-bit, input side): [4:0]=map index, [5]=direction (42 effective configs forward path)
- SW3 (6-bit, output side): [4:0]=map index, [5]=direction (42 effective configs return path)
- 21 UFM maps stored in EPM570 UFM; direction bit doubles usable configs
- J1–J3 ERM8 male (input side); J4–J6 ERF8 female (output side)
- FR-ROT-09: ALTERA_VIRTUAL_JTAG megafunction, USER0 UDR, 6-bit effective position

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
- STGC_Generator.py: relocate to `Rotor/`, update algorithm (relaxed unique-only)
- Deferred: SW1 vintage switch research; CM5 PWR_BUT timing thresholds (verify at schematic capture)