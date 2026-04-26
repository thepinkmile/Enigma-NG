# Checkpoint 063 — Encoder HID activity sideband
## Date
2026-04-26

## Overview
This checkpoint captures the connector-contract revision that adds a HID-local activity sideband to
the generic Stator ↔ Encoder interface. The active design now assigns **pin 8** on the 20-pin
Encoder connector to active-low `ENC_ACTIVE_N`, with the signal used only on the keyboard /
lightboard path.

## Work Done
### Connector-contract update
- Revised the generic 20-pin Encoder pin table so `ENC_ACTIVE_N` occupies pin 8
- Shifted the JTAG / shield / reset block down by one pin, moving `SYS_RESET_N` to pin 18
- Updated both the Stator-owned connector definition and the Encoder local pin-table copy so the
  physical contract is aligned in one place

### HID-path behaviour
- Defined `KBD_ENC` as the active source of `ENC_ACTIVE_N`, driven LOW only while a debounced key
  event is active
- Defined `LBD_DEC` to blank all outputs whenever `ENC_ACTIVE_N` is HIGH
- Explicitly kept `ENC_ACTIVE_N` out of the wider cipher path so it does not propagate through the
  plugboard, rotor, reflector, or extension interfaces

### Stator source-select and monitoring
- Updated the Stator design docs so the keyboard-source mux now selects both the 6-bit key data and
  the HID activity sideband together
- Allocated `CM5_KEY_ACTIVE_N` and `KEY_SRC_ACTIVE_N` monitoring usage on the Stator-side spare U7
  GPB capacity
- Recorded the interface change as **DEC-042** in `design/Design_Log.md`

## Validation
- The active Stator and Encoder docs now agree on the revised pin positions and signal naming
- The CPLD logic requirements now capture the required `ENC_ACTIVE_N` behaviour for `KBD_ENC` and
  `LBD_DEC`
- The touched markdown files lint cleanly with the repository markdownlint configuration

## Commits
- Pending at checkpoint write time; the next commit should include the `ENC_ACTIVE_N` connector
  update plus this repo-local state refresh

## Technical Decisions
- `ENC_ACTIVE_N` is the chosen HID activity sideband name
- `ENC_ACTIVE_N` is active-low and defaults HIGH / inactive
- The signal is intentionally HID-local rather than a system-wide cipher-path sideband

## Open Questions
- Schematic capture will still need to assign the exact Stator mux / U7 pin mapping in the future
- Prototype bring-up should confirm that the MAX II weak pull-up is sufficient as the default idle
  bias for any role that leaves `ENC_ACTIVE_N` unused

## Next Steps
1. Commit the `ENC_ACTIVE_N` connector update and the repo-local checkpoint refresh
2. Start the next session from `.copilot/plan.md`, `.copilot/handoff.md`, and this checkpoint
3. Continue with the next remaining design-review workstream

## Files Updated
- `design/Design_Log.md`
- `design/Electronics/Stator/Board_Layout.md`
- `design/Electronics/Stator/Design_Spec.md`
- `design/Electronics/Encoder/Board_Layout.md`
- `design/Electronics/Encoder/Design_Spec.md`
- `design/Software/CPLD_Logic/Encoder_Logic.md`
- `.copilot/plan.md`
- `.copilot/handoff.md`
- `.copilot/checkpoints/index.md`
- `.copilot/checkpoints/063-encoder-active-sideband.md`
