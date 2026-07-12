# Checkpoint 178: Stack-Output and Stack-Blanking Boards Created; BOM Consistency Sweep

**Date:** 2026-07-12
**Status:** Complete
**Scope:** Design discussion merge — Stack-Output and Stack-Blanking sub-tasks complete;
BOM footprint column standardised across all boards; DEC-085 created

## Summary

Full design session working on the `design-discussion-merge` workstream. Created the Stack-Output
Board and Stack-Blanking Board design files. Several BOM and connector-ownership corrections made
during review of the Stack-Output spec. A system-wide BOM consistency sweep replaced all `Yes`
values in Footprint Available columns with `✔`. DEC-085 created for the Stack-Output J4 0Ω link
decision.

## Work Completed

### Stack-Output Board — `merge-create-stack-output` ✅

New files: `design/Electronics/Stack-Output/Design_Spec.md` and `Board_Layout.md`

- **Receives from:** last ROT board in mini-stack (J3/J4/J5 ERF8 female sockets)
- **Front stacking J1 (QTS-025 male R/A, left edge):** carries SIG-BLOCK-B/C/F;
  Cypher Board J4 is the pinout definition owner
- **Rear stacking J2 (QSS-025 female R/A, right edge):** same pinout as Cypher Board J4;
  Cypher Board J4 is the definition owner (corrected from "this board" during review)
- **J4 power connector:** 0Ω links R4/R5 fitted for prototype; see DEC-085
- **JTAG spoke termination (§4):** R1 TCK pull-down, R2 TMS pull-up, R3 CPLD_RESET_N pull-up;
  all 10 kΩ ERJ-2RKF1002X — mirrors Cypher Board R3/R5/R6 idle-bias pattern (DEC-016 intent)
- **FR/DR IDs:** FR-EXT-03/05/07 inherited; FR-SOUT-01–08, DR-SOUT-01–07 new
- **BOM:** C1–C5, J1–J6, R1–R5 (JTAG), R4–R5 (0Ω links), U1–U8

### Stack-Blanking Board — `merge-create-stack-blanking` ✅

New files: `design/Electronics/Stack-Blanking/Design_Spec.md` and `Board_Layout.md`

- **Passive signal-routing board** — no active ICs; 5× 0402 resistors + 2 connectors
- **J1 (QTS-025-01-L-D-A-GP-K-TR, right/Stack-Input side):** pinout = Cypher Board J3
- **J2 (QTS-025-01-L-D-A-GP-K-TR, left/Stack-Output side):** pinout = Cypher Board J4
- **Transport mode:** J1/J2 mate directly with Cypher Board J3/J4 (no mini-stacks fitted)
- **Signal bridges (inner layers L2/L3):** SIG-BLOCK-A→B, SIG-BLOCK-C→D, SIG-BLOCK-E→F
  (TTD renamed TTD_RETURN at this board)
- **Termination resistors (all 10 kΩ, ERJ-2RKF1002X):**
  R1 ENC_ACTIVE_N pull-up, R2 TCK pull-down, R3 TMS pull-up, R4 CPLD_RESET_N pull-up,
  R5 ACTUATE_REQUEST_N pull-up
- **5V_MAIN:** NC throughout (SIG-BLOCK-H terminates here)
- **PCB stackup:** GND pour L1/L4 (shielding), signal routing L2/L3 only
- **Sections §1–§8** consecutive

### DEC-085 — Stack-Output J4 Power-Pin 0Ω Links

- Created `design/Design_Log/DEC-085_stack-output-j4-power-pin-zero-ohm-links-prototype-test.md`
- Updated `design/Design_Log/index.md`
- Updated `.copilot/directives/tertiary.md` → Next DEC: **DEC-086**
- Status: Accepted — confirm after prototype testing
- ERJ-2GE0R00X: DigiKey P0.0JCT-ND, Mouser 667-ERJ-2GE0R00X, JLCPCB C242160
- Footprint **not in KiCAD library** (marked ✘ in Stack-Output BOM)

### System-Wide BOM Consistency Sweep

Replaced all `| Yes |` entries in Footprint Available columns with `| ✔ |` across 15 files:

| Files | Count |
| --- | --- |
| Board Design_Spec.md files | 12 |
| `Rotor_26_Char_Design.md`, `Rotor_64_Char_Design.md` | 2 |
| `Consolidated_BOM.md` | 1 (121 occurrences) |

`JTAG_Integrity.md` left unchanged — its `| Yes |` appears in an options analysis table, not a BOM.

## Files Created / Modified

**New:**

- `design/Electronics/Stack-Output/Design_Spec.md`
- `design/Electronics/Stack-Output/Board_Layout.md`
- `design/Electronics/Stack-Blanking/Design_Spec.md`
- `design/Electronics/Stack-Blanking/Board_Layout.md`
- `design/Design_Log/DEC-085_stack-output-j4-power-pin-zero-ohm-links-prototype-test.md`

**Modified:**

- `design/Design_Log/index.md` (DEC-085 row added)
- `.copilot/directives/tertiary.md` (Next DEC counter: DEC-086)
- 15× board Design_Spec.md files + Consolidated_BOM.md (BOM consistency sweep)

## Current Merge Sub-Task Status

| Sub-task | Status |
| --- | --- |
| `merge-grs-6layer-stackup` | ✅ done |
| `merge-create-cypher-board` | ✅ done |
| `merge-create-stack-input` | ✅ done |
| `merge-create-stack-output` | ✅ done |
| `merge-create-stack-blanking` | ✅ done |
| `merge-cypher-board-j3j6-pinouts` | pending |
| `merge-ctl-dock-usb-allocation` | pending |
| `merge-create-stack-interposer` | **pending — next task** |
| `merge-create-cypher-input` | pending |
| `merge-create-cypher-output` | pending |
| `merge-update-ctl-board` | pending (blocked by `merge-ctl-dock-usb-allocation`) |
| `merge-update-top-level-docs` | pending |
| `merge-remove-old-boards` | pending |
| `merge-consistency-review` | pending |
| `merge-missing-components` | pending |
| `merge-final-review` | pending |

## Next Start Hint

**Resume with: `merge-create-stack-interposer`** — the passive base-board that sits at the bottom
of each Rotor Mini-Stack, bridging Stack-Input J6 (SQT-115 right-angle female) to Stack-Output J6
(2BHR-30-VUA THT male header).

Key facts:

- Passive board; carries SIG-BLOCK-A/D/E signals (ENC_DATA forward, ENC_DATA return, TTD)
- Bidirectional: SIG-BLOCK-A + TTD go Stack-Output→Stack-Input; SIG-BLOCK-D goes Stack-Input→Stack-Output
- Connector on Stack-Input side: 2BHR-30-VUA male header (mating to Stack-Input SQT-115 female)
- Connector on Stack-Output side: SQT-115-01-L-D-RA right-angle female (mating to Stack-Output 2BHR-30-VUA male)
- Pin map defined in Entry 20 of `.copilot/discussions/cypher-system-discussion/extension-mechanical-usage.md`
- 4-layer stackup; GND outer layers; signal routing on inner layers
