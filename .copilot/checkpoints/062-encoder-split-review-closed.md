# Checkpoint 062 — Encoder split review closed
## Date
2026-04-26

## Overview
This checkpoint captures the closeout of the Encoder board split review. The active Encoder
baseline is now locked around the shared `EPM570T100I5N` CPLD, digital debounce in logic,
programming-defined role selection, MAX II weak pull-up input bias, and the internal/UFM oscillator
as the default debounce timebase.

## Work Done
### Encoder split review closeout
- Completed the Encoder split review workstream and removed it from the active open-workstream list
- Kept the generic Encoder PCB model while moving role identification entirely into CPLD programming
- Removed the stale requirement for role-specific silkscreen labels (`ENCODE USE` / `DECODE USE`)

### Logic and bias clarifications
- Clarified that encode-role input pins should use the MAX II **weak pull-up** configuration as the
  active baseline
- Recorded the justification for weak pull-ups in the Encoder design docs, including the short
  expected Stator↔Encoder ribbon length and prior MAX II bench validation
- Kept the internal/UFM oscillator as the preferred debounce/sample-tick source because the Encoder
  logic needs a repeatable local timebase rather than a precision external clock

### Keyboard-variant notes
- Clarified that the current keyboard mapping section describes the **64-character** keyboard
  implementation
- Added notes that the same generic Encoder hardware can also support a **26-character Enigma-style
  keyboard** and other educational custom keyboard mappings through alternate programming

## Validation
- Active Encoder docs now align on the same programming-defined role model
- Repo-local `.copilot/` state now treats the Encoder split review as complete
- The updated design-doc and checkpoint set forms a clean restart point for the next session

## Commits
- Pending at checkpoint write time; the next commit should include the Encoder split review closeout
  plus this repo-local state refresh

## Technical Decisions
- Encoder split review is complete as a design-decision workstream
- The active Encoder hardware baseline no longer depends on role-specific fitted passives
- The remaining Encoder follow-up work, if any, is implementation/prototype tuning rather than
  unresolved architecture

## Open Questions
- Final debounce constants and any invalid-state policy details still require prototype and Quartus
  fit confirmation
- Broader non-Encoder follow-up workstreams remain open elsewhere in the project

## Next Steps
1. Commit the closed Encoder split review state and the repo-local checkpoint refresh
2. Start the next session from `.copilot/plan.md`, `.copilot/handoff.md`, and this checkpoint
3. Continue with the next remaining non-Encoder review workstream

## Files Updated
- `.copilot/plan.md`
- `.copilot/handoff.md`
- `.copilot/checkpoints/index.md`
- `.copilot/checkpoints/062-encoder-split-review-closed.md`
