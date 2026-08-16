# Checkpoint 182 — Encoder Module Renamed and Redesigned Around DF40C BtB Interconnect

**Date:** 2026-08-13
**Session work:** Renamed and rewrote the generic cipher-bank interface board from
`design/Electronics/Encoder/` to `design/Electronics/Encoder_Module/`, replacing its legacy
20-pin IDC ribbon + 64x spade-terminal interface with a 3-connector Hirose DF40C BtB family
(`J1`/`J2`/`J3`). Updated every live cross-reference from the Cypher Board and Cypher-Input Board
to point at the new module and confirmed the DEC-086 Cypher-Input common/variant restructure
(10-Numeric variant, single shared I2C address) is fully reflected across system-wide docs.

---

## Status

- Encoder Module redesign — **complete**. New canonical files: `Encoder_Module/Design_Spec.md`,
  `Encoder_Module/Board_Layout.md`. Old `Electronics/Encoder/` folder retired (superseded, not a
  content loss — this is a direct rename/rewrite of the same board, not deletion of unique
  design content).
- `merge-create-cypher-input` — still `in_progress`. Only remaining blocking item: left-side
  (J4/J6) Plugboard passthrough signal definition, blocked on `merge-create-plugboard`. No other
  blocking items remain for this board's own design.
- Mechanical assembly docs (`Mechanical/Keyboard_Assembly/Design_Spec.md`,
  `Lightboard_Assembly/Design_Spec.md`, `Plugboard_Assembly/Design_Spec.md`) still describe the
  pre-Cypher standalone-board / IDC-ribbon / spade-terminal architecture and are now stale
  relative to the Cypher-Input/Cypher-Output/Plugboard board designs. **Explicitly deferred** —
  user has directed that mechanical and software sections are out of scope until the electronics
  design is fully merged; a full mechanical-section overhaul will follow as its own pass.

---

## Key architecture decisions this session

| Decision | Detail |
| --- | --- |
| Encoder Module interconnect replaced | 20-pin IDC ribbon + `J2`-`J65` spade terminals (legacy) replaced with 3x Hirose DF40C-xDP BtB plugs: `J1` = DF40C-90DP (`plain-bits[63:0]`, 64 generic signal lines + 26 GND zig-zag), `J2` = DF40C-24DP (`cypher-bits[5:0]` + JTAG + `ENC_ACTIVE_N`, full zig-zag), `J3` = DF40C-10DP (3V3_ENIG power, 5+5, no zig-zag). |
| Module now carries no physical HID/plugboard interface | No on-board keyswitches, lamps, or jack terminals — those live entirely on whichever carrier board (Cypher-Input, Cypher-Output) or the future Plugboard Board the module is mounted to, wired back to the generic `plain-bits[63:0]` bus. |
| Connector Definition Owner | `Encoder_Module/Board_Layout.md §1a-1c` is now the sole canonical source for the ENC module BtB interface family. Carrier boards (Cypher Board J7-J18, Cypher-Input J1-J3, future Cypher-Output) reference it and carry only the mating DF40C-xDS receptacles (§4.1 of `Encoder_Module/Design_Spec.md`). |
| Legacy content preserved, not discarded | The removed spade-terminal BOM row and §7 Plugboard Jack-Sensing section were copied into `.copilot/todos/merge-create-plugboard.md` under a "Reference Material Preserved from Encoder Module Redesign" heading, since the Plugboard Board succeeds that role. |
| Cross-references updated | `Cypher/Design_Spec.md` §3 and `Cypher/Board_Layout.md §5` now point to `Encoder_Module/Board_Layout.md §1a-1c` (with the old inline description replaced by a pointer + "Encoder Module definition is authoritative" note); `Cypher-Input/Design_Spec.md` §1/DR-CYPI-02 already referenced the new module correctly. |
| DEC-086 confirmed fully applied | Verified `Cypher-Input/Design_Spec.md`/`Board_Layout.md` common/variant split, the new `Cypher_Input_10_Numeric_Design.md` file, and the single shared `0x38` I2C address for U4 are consistent across `Boards_Overview.md`, `Electrical_Design.md`, `System_Architecture.md`, and `Controller/Design_Spec.md §4.1`. |

---

## Verification performed this session

- Confirmed old `Electronics/Encoder/Design_Spec.md` (as last known via file history) and the new
  `Encoder_Module/Design_Spec.md` describe the same six board roles (`KBD_ENC`, `LBD_DEC`,
  `PLG_PASS1_DEC/ENC`, `PLG_PASS2_DEC/ENC`) — confirming this is a rename/rewrite of one board,
  not two different boards colliding under a shared name.
- Confirmed no stray references to the old `Electronics/Encoder/Design_Spec.md` or
  `Board_Layout.md` paths remain in any **electronics** doc, the Cypher/Cypher-Input board specs,
  or system-wide docs (`Boards_Overview.md`, `System_Architecture.md`, `Electrical_Design.md`).
  Remaining references are confined to append-only `Design_Log/DEC-0xx` entries (historically
  correct, must not be edited per TERTIARY) and mechanical/software docs (explicitly deferred).
- Found and corrected an over-eager `.recycle-bin/` archival of the old
  `Electronics/Encoder/Design_Spec.md`/`Board_Layout.md` content made in error early this session
  (mistakenly treated the rename as a deletion) — reverted once the user clarified it was a
  rename, not a content loss.

---

## Next Session Start Point

1. `merge-create-cypher-input` remains `in_progress`, blocked only on the Plugboard passthrough
   signal definition (`merge-create-plugboard`, itself blocked on both HID boards).
2. Likely next actionable step: `merge-create-cypher-output` (not blocked) — create
   `Cypher-Output/Design_Spec.md` + `Board_Layout.md`, applying the wiring notes already captured
   in `.copilot/todos/merge-create-cypher-output.md`. Note: that todo file's I2C addressing note
   is stale post-DEC-086 (still says "0x38 = Cypher-Input Extended, 0x39 = Cypher-Input Classic
   are already taken") and should be corrected to reflect the single shared `0x38` address before
   or during that work.
3. Mechanical assembly docs (`Keyboard_Assembly`, `Lightboard_Assembly`, `Plugboard_Assembly`)
   remain explicitly out of scope until a dedicated mechanical-overhaul pass after the electronics
   merge completes.
