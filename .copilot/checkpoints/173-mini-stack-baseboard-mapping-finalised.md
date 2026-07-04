# Checkpoint 173: Mini-stack Base-Board Mapping Finalised (Entry 20)

**Date**: 2026-06-06  
**Status**: Complete  
**Scope**: Discussion-state completion and session-state sync only (no implementation changes)

## Summary

Completed the mini-stack internal return-link discussion by finalising **Entry 20** in
`.copilot/discussions/extension-mechanical-usage.md`. The signal-flow model is now captured end-to-end with
`SIG-BLOCK-A` through `SIG-BLOCK-I`, and the passive base-board direction is locked with base-board-owned mapping.

## Work Completed

1. Expanded and finalised **Entry 20** with full flow descriptions:
   - ENC_DATA forward/reflector/return traversal model (`SIG-BLOCK-A/B/C/D`)
   - JTAG chain + distributed spoke model (`SIG-BLOCK-E/F`) including `CPLD_RESET_N`
   - Actuation + LED-enable sideband model (`SIG-BLOCK-G`) using canonical `ENC_ACTIVE_N`
   - Power distribution model (`SIG-BLOCK-H/I`) with Stack-Input-only `5V_MAIN`
2. Captured passive interposer direction:
   - mini-stack internal link now prefers a rigid passive base-board over flexible ribbon
   - connector orientation/mechanical assembly intent documented
3. Locked base-board-owned pin mapping for the internal link:
   - dual-row IDC style, **26 pins total (2x13)**, odd/even numbering
   - final zig-zag table recorded and applied to both base-board connectors
4. Updated Entry 19/20 naming alignment:
   - Entry 19 now maps `ENC_ACTIVE_INPUT_N` (pin 5) and `ENC_ACTIVE_OUTPUT_N` (pin 46), each related to `ENC_ACTIVE_N`
   - Entry 20 notes Cypher-level linkage while preserving interconnect net separation intent
5. Updated “Next discussion order” in the discussion file:
   - Item 2 marked complete

## Next Start Hint

Continue with the remaining unresolved discussion item:

1. Remaining new-parts closure, including LED current-limiting resistor sourcing rows

## Files Updated

- `.copilot/discussions/extension-mechanical-usage.md`
- `.copilot/plan.md`
- `.copilot/handoff.md`
- `.copilot/checkpoints/index.md`
- `.copilot/checkpoints/173-mini-stack-baseboard-mapping-finalised.md` (new)

## State After This Checkpoint

- Extension mechanical discussion item 1 (Cypher interconnect mapping): complete ✅
- Extension mechanical discussion item 2 (mini-stack return-link/base-board mapping): complete ✅
- Remaining extension-mechanical discussion item:
  1. Remaining new-parts closure (including LED resistor sourcing rows)
