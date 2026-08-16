# Review Cypher-Input/Cypher-Output LED colour controls for independent per-channel PWM

**ID:** cypher-input-led-independent-rgb-pwm-review
**Status:** pending
**Category:** Electronics / Architecture Review
**Source:** User request, 2026-08-16
**Blocked by:** merge-final-review

---

## Description

The current Cypher-Input LED colour architecture (DEC-087) drives each of `RED_DRIVE_N`/
`GREEN_DRIVE_N`/`BLUE_DRIVE_N` as a simple on/off gate per colour channel (software-selected via
U4 GPIO), with a single shared brightness PWM (RV1/555 astable, U1) gating one common
cathode-return switch (U8) downstream of colour selection for the whole board. This only supports
a small fixed palette of colour combinations at one shared brightness level - not full/continuous
colour mixing.

Review whether the LED bank should instead support **independent PWM control on each of the R, G,
and B lines**, so any colour (not just a fixed on/off palette) can be composited per key/board, and
consider whether this should be driven from the CM5 (e.g. via I2C brightness/colour registers or a
PWM-capable interface) rather than purely local hardware.

## Scope for this pass

- Evaluate replacing the current on/off `RED_DRIVE_N`/`GREEN_DRIVE_N`/`BLUE_DRIVE_N` gate drive
  with independent PWM-capable drive per channel (full colour mixing, not just palette selection).
- Evaluate whether/how the CM5 should drive this (new I2C interface, dedicated PWM lines, or
  continued local generation with CM5-configurable set-points).
- Identify what changes this implies for U4 (PCA9534A GPIO-only, no native PWM), U5-U7 (colour
  MOSFETs), and the brightness dial/555 astable circuit (U1, RV1).

## Explicitly out of scope for this pass (deferred, larger change)

- Per-user note (2026-08-16): making the brightness PWM astable oscillator **fully independent on
  each HID board** (i.e. Cypher-Input and the future Cypher-Output each generating and controlling
  their own PWM/brightness rather than one board's 555 broadcasting a shared
  `BRIGHTNESS_PWM_EN` to the other via `J4`/`J6`) is a materially bigger architecture change and is
  explicitly **not** in scope for this pass. Flag it as a follow-on consideration only - do not
  implement without a separate, explicit go-ahead.

## Notes

- This affects `Cypher-Input/Design_Spec.md` §5/§6, all 3 variant BOM files, and (once created)
  the Cypher-Output board's equivalent circuit - both boards currently share one broadcast
  brightness/colour signal set per DEC-087.
- Should be actioned after the design-discussion merge is fully signed off
  (`merge-final-review`), and before `todo-clean-up-requirement-details` starts.
