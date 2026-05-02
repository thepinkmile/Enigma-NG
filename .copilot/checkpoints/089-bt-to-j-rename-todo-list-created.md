# Checkpoint 099 — BT→J rename complete, todo-list.md created

**Date:** 2026-05-01
**Preceding checkpoint:** 098

---

## What was accomplished

### 1. Stator SW1/SW2 removal (carried from prior session)

- `design/Electronics/Stator/Design_Spec.md`: rows for SW1 and SW2 fully removed (were showing
  `~~Removed — relocated to Settings Board~~` strikethrough).
- Directive enforced: design specs are "current state only" — no historical/removed content.

### 2. Encoder BT1–BT64 → J3–J66 rename

- Applied across 6 files / 10 occurrences:
  - `design/Electronics/Encoder/Design_Spec.md` (§4 narrative, BOM row, Qty notes)
  - `design/Electronics/Encoder/Board_Layout.md` (signal group table)
  - `design/Software/CPLD_Logic/Encoder_Logic.md` (lines 60, 67, 249)
  - `design/Electronics/Consolidated_BOM.md` (Encoder row RefDes, line 206)
  - `design/Datasheets/SaiBuy_Ltd_6p35mm_Mono_Jack_Pseudo_Datasheet.md` (wiring note, system
    BT65–BT128 encode-half → J3–J66 on encode Encoder board)
- `BT` is the IPC/EDA standard prefix for batteries only; blade terminals are `J` (connector).
- J1 = plugboard panel jacks (off-board), J2 = IDC service connector already taken → blade
  terminals start at J3.
- Both decode and encode Encoder boards use J3–J66 independently; board context distinguishes them.

### 3. DEC-050 appended to Design Log

- `design/Design_Log.md`: DEC-050 appended with full rationale, alternatives considered, and
  impact list.
- DEC-050 is now the last entry before `## Open Questions`.

### 4. Rotor N=26/N=64 variant todo registered

- Deferred to schematic capture phase.
- KiCAD board variant / DNF flag mechanism is the recommended approach (U3 Fit for N=26, U4 Fit
  for N=64; bypass caps follow same variant flag).
- Added to SQL todos as `rotor-variant-refdes-schematic` and to `.copilot/todo-list.md` as
  `rotor-variant-refdes-schematic`.

### 5. `.copilot/todo-list.md` created

New file — canonical deferred-work and open-action tracker for the project. Sections:

- **Open Workstreams** (plan-level): 5 items (`extension-mechanical-usage`,
  `coupon-testing-review`, `battery-connector-final-review`,
  `general-pin-mapping-schematic-capture`, `rerun-deep-reviews`)
- **Electronics Deferrals**: 6 items (`ctlh1-deferred`, `rotor-esd-tvs`,
  `rotor-variant-refdes-schematic`, `display-addon-board`, `cpld-production-replacement`,
  `connector-thermal-verification`)
- **Mechanical Deferrals**: 7 items (shaft/rolling-element/alloy/mechanism TBDs; display aperture;
  harnesses; connectors)
- **Software Deferrals**: 2 items (LTC3350 telemetry DEC-025; CPLD timing deferred)
- **Standards & Certification Actions**: 4 items (DA-01 through DA-04)

### 6. plan.md and handoff.md updated

- `plan.md` "Next Session Start Point": updated to reference `todo-list.md` and checkpoint 099.
- `plan.md` "Critical Notes": added directive to consult `todo-list.md` rather than re-scanning repo.
- `handoff.md` "Standing Directives": added reference to `todo-list.md`.

All changed files passed `markdownlint --dot` with exit code 0.

### 7. SaiBuy datasheet cleaned — design content removed

- `design/Datasheets/SaiBuy_Ltd_6p35mm_Mono_Jack_Pseudo_Datasheet.md`
- §2 "Intended Enigma-NG Use": removed system quantity (64 sockets) and the Tip/Switch/Sleeve →
  J3-J66 RefDes lines; replaced with single "Electrical type" descriptor at component level.
- §4 renamed from "Enigma-NG Integration Notes" to "Component Notes"; removed "Wiring" row
  (J3-J66 Encoder blade terminal reference) and "Plugboard role" row (design usage).
- Rule enforced: datasheets describe the component only — RefDes, wiring, and usage belong in
  Design_Spec.md / Board_Layout.md exclusively.

---

## Files changed this session (this checkpoint)

| File | Change |
| --- | --- |
| `design/Electronics/Stator/Design_Spec.md` | SW1/SW2 rows removed |
| `design/Electronics/Encoder/Design_Spec.md` | BT1–BT64 → J3–J66 (§4, BOM, Qty) |
| `design/Electronics/Encoder/Board_Layout.md` | BT1–BT64 → J3–J66 (signal group table) |
| `design/Software/CPLD_Logic/Encoder_Logic.md` | BT1–BT64 → J3–J66 (×3) |
| `design/Electronics/Consolidated_BOM.md` | Encoder row RefDes BT1–BT64 → J3–J66 |
| `design/Datasheets/SaiBuy_Ltd_6p35mm_Mono_Jack_Pseudo_Datasheet.md` | BT65–BT128 → J3–J66 (encode half) |
| `design/Design_Log.md` | DEC-050 appended |
| `.copilot/todo-list.md` | Created (new file) |
| `.copilot/plan.md` | Updated (next session start point + critical notes) |
| `.copilot/handoff.md` | Updated (Standing Directives section) |

---

## Commit status

**NOT YET COMMITTED** — awaiting explicit "Let's lock this in" from user.

---

## Next session start point

1. `.copilot/plan.md`
2. `.copilot/handoff.md`
3. `.copilot/todo-list.md`
4. This checkpoint
