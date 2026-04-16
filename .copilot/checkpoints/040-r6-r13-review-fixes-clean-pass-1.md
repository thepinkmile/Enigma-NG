# Checkpoint 040 — R6–R13 review fixes, clean pass #1 of 2

## Date
2026-04-15

## Session
<sanitized-session-id>

## Overview

Review rounds R6–R13 were run autonomously overnight. R8 achieved the first clean pass;
however R9 contained false positives (corrected known-correct list), and R10–R12 found
3 genuine issues. R13 was the second clean pass attempt — and was CLEAN. This is clean pass #1
of 2 after the R10–R12 fixes. R14 was launched as the decisive second-pass confirmation but
was still in progress when the user needed to leave. Checkpoint created before laptop shutdown
to preserve all committed work.

## Commits

| SHA | Description |
|-----|-------------|
| `78eb2ac` | R6 fix: remove SYS_RESET_N from JTAG CI row in Rotor/Board_Layout.md |
| `a57a9b1` | R7 fix: update DEC-015 pin table and DEC-031 net effect in Design_Log.md |
| `1e79710` | R10 fix: correct PNP transistor designators in Settings_Board/Board_Layout.md |
| `94e0589` | R11 fix: add SERVO_HOME R_SH1 and C_SH1 to BOM summary counts |
| `8db86d8` | R12 fix: move TTD_RETURN to JTAG CI row in Stator/Board_Layout.md |

(R8 and R13 were clean — no commits needed. R9 had false positives only — no commits needed.)

## Work Done

### R6 — 1 finding

- Rotor/Board_Layout.md §9: SYS_RESET_N was in JTAG CI row (0.127mm). SYS_RESET_N is a
  slow-logic I²C-sourced signal (DEC-031) — moved to 0.20mm standard signal row.

### R7 — 2 findings

- Design_Log.md DEC-015: LINK-BETA pin table still showed pre-DEC-031 assignments
  (SYS_RESET_N on pin 8, ENC_IN/OUT on pins 12–24). Updated to show pins 8, 12–17, 19–24
  as ALL SPARE with DEC-031 cross-reference.
- Design_Log.md DEC-015: missing cross-ref to DEC-031. Added.
- Design_Log.md DEC-031: Net Effect only listed pins 12–17 (not 8, 19–24). Corrected.
- Design_Log.md Board Connector Inventory: Diagnostic Bank-Beta still said
  "Monitors 12-bit Sniffer, JTAG, SYS_RESET_N". Updated to SPARE.

### R8 — 0 findings ✅ CLEAN (pass #1 of 2 at that point — reset by R10–R12)

### R9 — 3 false positives (no fixes applied)

- Review agent had incorrect known-correct item #23 claiming U_EXP_SW_OUT @ 0x24.
- Authoritative state: U_EXP_SW_IN @ 0x26 (reads switches), U_EXP_LED @ 0x27 (drives LEDs).
- U_EXP_SW_OUT @ 0x24 is a stale artefact — NEVER use.
- Transistors Q_BNK1_G/R, Q_BNK2_G/R are correct (not Q1–Q4).
- Known-correct list corrected; stored in memory.

### R10 — 1 finding

- Settings_Board/Board_Layout.md §2 Placement Notes: used generic "Q1–Q4" instead of
  functional names Q_BNK1_G, Q_BNK1_R, Q_BNK2_G, Q_BNK2_R.

### R11 — 2 findings

- Consolidated_BOM.md passive summary was missing SERVO_HOME components:
  - R_SH1 (10kΩ 1% 0402, ERJ-2RKF1002X, Mouser C25744): STA count 0 → 1, total 328 → 329
  - C_SH1 (100nF X7R 0402, C1525): STA count 8 → 9, total 512 → 513

### R12 — 1 finding

- Stator/Board_Layout.md §9: TTD_RETURN was in 0.20mm logic signal row. TTD_RETURN is a
  JTAG CI signal (travels Reflector→Stator, then Stator→LINK-BETA pin 26). Moved to 0.127mm
  CI row. Reflector and Extension already had it correct.

### R13 — 0 findings ✅ CLEAN — clean pass #1 of 2 (post-R10/R11/R12 fixes)

### R14 — in progress at checkpoint time

- Launched as the decisive second clean pass. Still running when user needed to leave.
- When R14 completes: if clean → review cycle done (2/2); if findings → apply fixes, recount.

## Key Technical Notes

### TTD_RETURN routing (now correct everywhere)
- TTD_RETURN is a JTAG CI signal → 0.127mm on all boards
- Stator/Board_Layout.md was the only board with it wrong (R12 fix)
- Correct: Reflector, Extension, Encoder, Rotor, JDB, Controller all had it in CI row

### SYS_RESET_N routing (now correct everywhere)
- SYS_RESET_N is NOT a CI signal → 0.20mm standard logic
- Rotor/Board_Layout.md was corrected in R6

### BOM passive counts (post-R11, canonical)
- 10kΩ 0603 1% (pull-downs): STA=10, total=31
- 10kΩ 0402 1% (R_SH1): STA=1, total=329
- 100nF X7R 0402 (C_SH1 etc.): STA=9, total=513

### Settings Board authoritative state
- U_EXP_SW_IN @ 0x26 (reads switches)
- U_EXP_LED @ 0x27 (drives LEDs + PNP colour rails)
- Transistors: Q_BNK1_G, Q_BNK1_R, Q_BNK2_G, Q_BNK2_R (4× PNP MMBT3906)
- **STALE:** U_EXP_SW_OUT @ 0x24 — never use, never reinststate

## Review Cycle Status at Checkpoint

| Round | Result | Consecutive Clean |
|-------|--------|-------------------|
| R1 | 21 findings | 0 |
| R2 | 19 findings | 0 |
| R3 | 8 findings | 0 |
| R4 | 9 findings | 0 |
| R5 | 10 findings | 0 |
| R6 | 1 finding | 0 |
| R7 | 2 findings | 0 |
| R8 | 0 (CLEAN) | 1 — reset by R10-R12 |
| R9 | 3 false positives | n/a |
| R10 | 1 finding | 0 |
| R11 | 2 findings | 0 |
| R12 | 1 finding | 0 |
| R13 | 0 (CLEAN) | **1** ✅ |
| R14 | **pending** | needed: 2nd clean |

## Next Steps

1. Read R14 result when back at office (or rerun as R15 if session expired)
2. If clean: review cycle complete ✅ → proceed to components-todo.md sourcing
3. If findings: apply fixes, run R15, continue until 2 consecutive clean passes
4. Work through `.copilot/components-todo.md` — 21 TBD items to confirm part numbers
5. Update Consolidated_BOM.md and board BOMs with confirmed PNs
