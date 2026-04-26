# Checkpoint 061 — Encoder EPM570 upgrade and logic spec
## Date
2026-04-26

## Overview
This checkpoint captures the Encoder architecture update that standardises all six Encoder Modules
on the Intel MAX II `EPM570T100I5N`, retires the active design's external per-line RC debounce
network, and records the new CPLD-logic requirements document for later VHDL implementation.

## Work Done
### Encoder architecture update
- Updated the active Encoder docs to replace `EPM240T100I5N` with `EPM570T100I5N`
- Removed the active-design assumption that encode-role boards need role-specific RC debounce
  population
- Recorded that Encoder board role is now selected by the programmed CPLD image rather than by
  board-level switches or role-only passives

### Logic-spec capture
- Added `design/Software/CPLD_Logic/Encoder_Logic.md`
- Defined the intended sampled 64-bit debounce architecture for encode-role images
- Defined the required 64-to-6 encode and 6-to-64 decode behaviour at requirements level so VHDL
  can be developed later against a written reference

### Decision log and system-doc sync
- Added `DEC-041` to `design/Design_Log.md` to supersede the active Encoder assumptions around
  `EPM240T100I5N` and external per-line RC debounce
- Updated BOM, board overview, power-budget, certification, and GUI-planning docs so the Encoder
  boards are now counted as `EPM570` devices

## Validation
- Active Encoder docs now reference `EPM570T100I5N`
- The new logic-spec document exists under `design/Software/CPLD_Logic/`
- The decision log now includes `DEC-041` as the central rationale for this change

## Commits
- Pending at checkpoint write time; the next commit should include the Encoder CPLD upgrade,
  `DEC-041`, the new logic-spec document, and this repo-local state refresh

## Technical Decisions
- Encoder boards remain physically universal; role is chosen by programming, not by local switches
- Debounce is now an implementation concern of the CPLD logic rather than an active-board passive RC
  requirement
- Using `EPM570T100I5N` across Encoder, Rotor, and Stator simplifies part standardisation and
  preserves LE headroom for future logic changes

## Open Questions
- Final debounce constants still need prototype measurements and Quartus fit verification
- Exact invalid-state behaviour for encode-role multi-press / no-press conditions remains to be
  confirmed during bring-up

## Next Steps
1. Continue the Encoder board split review from the new `EPM570` / digital-debounce baseline
2. Commit the Encoder architecture update plus the repo-local checkpoint refresh when ready
3. Resume later VHDL work from `design/Software/CPLD_Logic/Encoder_Logic.md` once prototype boards
   exist

## Files Updated
- `.copilot/plan.md`
- `.copilot/handoff.md`
- `.copilot/checkpoints/index.md`
- `.copilot/checkpoints/061-encoder-epm570-and-logic-spec.md`
- `design/Design_Log.md`
- `design/Electronics/Encoder/Design_Spec.md`
- `design/Electronics/Encoder/Board_Layout.md`
- `design/Electronics/Consolidated_BOM.md`
- `design/Electronics/Boards_Overview.md`
- `design/Electronics/Power_Budgets.md`
- `design/Standards/Certification_Evidence.md`
- `design/Software/GUI_App/Design_Spec.md`
- `design/Software/CPLD_Logic/Encoder_Logic.md`
