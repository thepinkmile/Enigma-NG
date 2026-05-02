# Checkpoint 096 — Rotor Variant RefDes Renames Complete

**Status:** All edits complete; lint clean; awaiting user commit confirmation.

## Work Completed This Checkpoint

Completed the full `rotor-variant-refdes-schematic` todo:

### Rename map applied
- `U3` → `U3A` (Board A, N=26 variant sensor)
- `U4` → `U3B` (Board B, N=64 variant sensor)
- Bypass caps: `C16`→`C16A`, `C17`→`C17A`; `C18`→`C18B`, `C19`→`C19B`
- Tank caps: `C24–C27`→`C24A–C27A`; `C28–C31`→`C28B–C31B`
- Tank inductors: `L5–L8`→`L5A–L8A`; `L9–L12`→`L9B–L12B`

### Files modified
- `design/Electronics/Rotor/Design_Spec.md` — all sensor RefDes updated throughout
- `design/Electronics/Rotor/Board_Layout.md` — Board A and Board B tables updated
- `design/Electronics/Rotor/Rotor_26_Char_Design.md` — variant spec fully updated
- `design/Electronics/Rotor/Rotor_64_Char_Design.md` — variant spec fully updated
- `design/Electronics/Consolidated_BOM.md` — 5 rows: RefDes renamed + System Qty corrected (mutually-exclusive sensor rows now qty 1 per rotor)
- `design/Design_Log.md` — DEC-052 added
- `.copilot/todo-list.md` — `rotor-variant-refdes-schematic` marked DONE

### BOM System Qty corrections
| Component | Before | After |
|---|---|---|
| 100nF bypass (C16A/C18B) | 92 | 82 |
| 1µF bypass (C17A/C19B) | 4 | 2 |
| 33pF tank (C24A-C27A / C28B-C31B) | 16 | 8 |
| 18µH inductor (L5A-L8A / L9B-L12B) | 16 | 8 |
| FDC2114 (U3A/U3B) | 4 | 2 |

## Verification
- Grep confirms only `U4`–`U6` (CTL false-positive, line 587 Design_Spec.md) remains — correct, not changed
- markdownlint: all 7 files pass with exit code 0
- SQL todo `rotor-variant-refdes-schematic` marked `done`

## Next Session
- Next todo to review: `rotor-esd-tvs` (ESD TVS sourcing for Rotor §6)