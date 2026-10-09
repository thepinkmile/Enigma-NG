# Checkpoint 195 — USM Redesign Implementation Complete

**Date:** 2026-10-09
**Status at checkpoint:** `usm-redesign-implementation` marked **done**. All five boards (User
Settings Module, Cypher-Input, Cypher-Output, Cypher-Plugboard, Cypher) rebuilt, cross-checked,
and user-reviewed/committed. Session paused for the weekend.

---

## Summary

This closes out the multi-session USM redesign effort (begun checkpoint 192, continued through
193/194). This session completed the final board (Cypher itself), ran two consistency-review
passes across all five boards plus Controller, and fixed every issue found.

## What Is Done

1. **Cypher** (`Design_Spec.md`, `Board_Layout.md`) — fully rebuilt:
   - `J5` repurposed to the single **Cypher Left Pair Template** (replacing the old two-connector
     J5/J6 HID split): carries `3V3_ENIG`/`5V_MAIN`/GND, `ENC_DATA_IN[5:0]`/`ENC_DATA_OUT[5:0]`,
     `ENC_ACTIVE_INPUT_N`/`ENC_ACTIVE_OUTPUT_N`, `BOARD_ROLE_ID_IN[3:0]`/`BOARD_ROLE_ID_OUT[3:0]` -
     no LED signals (that's HID/USM-only knowledge, not described on this board at all). New
     50-pin map designed from scratch (Cypher is this template's canonical owner) with full 180°
     rotational symmetry - corrected twice after user review caught the symmetry was broken, then
     caught a further placement error; final layout user-verified pin-by-pin.
   - `J6` fully repurposed to the **Hub Connector Template**, now targeting the User Settings
     Module instead of a HID board directly (per DEC-103).
   - Former `J19` USM JST harness retired entirely (superseded by `J6`).
   - CPLD I/O budget, Port Mapping, Signal Routing Matrix, JTAG Hub chain order, `§3a`
     `BOARD_ROLE_ID` comparator, External Keyboard Source Mux all updated to match - including
     correctly describing `ENC_ACTIVE_OUTPUT_N` as a signal this board's own CPLD *generates*
     (after propagation-delay accounting), not merely forwards.
   - Several historical-wording violations caught and fixed across multiple passes (e.g.
     "replaces the former J19 harness", "replace the former single hybrid dock pair") - current-
     design-only rule re-applied repo-wide on this file.
2. **Controller** (`Design_Spec.md`) - `DR-CTL-13` fixed (was contradicting its own document by
   calling `I2C2` "reserved/NC" when the rest of the doc already treated it as the active
   USM/HID-lighting bus); a second historical-wording violation ("existing wiring, unchanged")
   also removed; `Last Updated` bumped (was stale from before these fixes).
3. **Two full consistency-review passes** across Cypher/Cypher-Input/Cypher-Output/
   Cypher-Plugboard/USM/Controller found and fixed:
   - An MPN mismatch in `Cypher/Design_Spec.md` (`-TR` reel suffix in prose vs. no suffix in the
     DR table/BOM for `J5`/`J6`).
   - A stale, confusing cross-reference in `Cypher/Design_Spec.md`'s `J20+` section (pointed at
     Cypher's own `DR-CYP-05/§6 J5/J6` to explain Cypher-Plugboard's electrical role; repointed to
     `Cypher-Plugboard/Design_Spec.md §3` directly).
   - **USM's `Board_Layout.md` was missing the flush/protruding mating-convention description and
     `Global_Routing_Spec.md §4.1a` cross-reference entirely** (the earlier fix was scoped only to
     the Cypher-system boards). Extended to USM's `J1`/`J2`/`J3`/`J4` - `J1` (male, mates Cypher)
     protrudes; `J2`/`J3`/`J4` (female) sit flush.

## Verified Consistent (no action needed)

- Connector ownership, gender, and signal lists match exactly across every board pair that shares
  a connector template.
- Section-number cross-references resolve correctly everywhere checked.
- I2C bus/address allocation (`I2C2` Cypher-peripherals bus, USM colour store `0x39`,
  Cypher-Input `0x38`) is consistent between the HID boards, USM, and `Controller`'s system-wide
  table.
- `ENC_ACTIVE_INPUT_N`/`ENC_ACTIVE_OUTPUT_N` treatment (two distinct signals, Cypher as sole
  generator of the latter) is described consistently on every board that touches it.
- DEC-103/104/107 citations check out against their actual decision log content.

## Not Yet Done (separate from USM redesign, pre-existing backlog)

- **`mini-stack-connector-flush-protrude-review`** (pending) - check the mini-stack sub-system's
  own `Board_Layout.md` files for the same male/female flush-vs-protruding mismatch that was found
  and fixed on the Cypher system + USM this session.
- **`cypher-input-led-independent-rgb-pwm-review`** (pending) - the user's stated next major topic:
  planning small test boards for the LED implementation PoC (analog multi-colour-bank vs.
  addressable LED decision), now that the connector/signal architecture feeding it is fully
  settled.
- `usm-3-part-hid-module-mechanical-review` (pending, was blocked on this item) - now unblocked;
  mechanical design for the combined Cypher-Input/Cypher-Output/USM 3-part HID module.
- `usm-template2-template1-unification-review` (pending) - captured idea, not actioned.

## Next Session — Start Here

1. Confirm git state (`git status`, `git log -3`) - should be clean, on `main`, with this
   checkpoint's commit as the tip (or the user's own follow-up commits after review).
2. Ask the user which of the "Not Yet Done" items to tackle next - the user previously indicated
   `mini-stack-connector-flush-protrude-review` and the LED PoC planning
   (`cypher-input-led-independent-rgb-pwm-review`) as the two live follow-ons, in no stated order.
3. No open design inconsistencies are currently known across the USM-redesign board set; do not
   re-run the full consistency sweep again unless new changes are made to these boards.
