# Checkpoint 186 - Cypher-Output Board Design Drafted; Power Budget Corrections

**Date:** 2026-08-16
**Status:** `merge-create-cypher-output` in progress - board files created and drafted, user
review in progress (paused mid-review for session reboot)

---

## Summary

This session covered two major threads: (1) a wide-ranging `BOARD_ROLE_ID` architecture redesign
on the Cypher/Cypher-Input boards (DEC-089), including several rounds of wording/pin-map
refinement per user feedback, and (2) drafting the full Cypher-Output board design (all 5 files),
followed by a detailed technical review that surfaced and fixed several real design gaps.

## Part 1 - `BOARD_ROLE_ID` Redesign (DEC-089)

- `BOARD_ROLE_ID` widened from a 3-bit enumerated index to a 4-bit capability bitmask
  (bit0=Characters, bit1=Numbers, bit2=Special, bit3=Custom), with an `AND`-based compatibility
  rule on the Cypher Board's CPLD comparator (`HID_VARIANT_ID[3:0]` output).
- CPLD pin budget freed by replacing the old `CFG_REFMAP[5:0]` parallel GPIO bus (removed from
  the User Settings Module, Bank 2) with a JTAG-based UFM write for reflector-map selection.
- `BOARD_ROLE_ID` migrated from the Cypher Board's `J6` (right, JTAG template - no spare budget
  once widened) to `J5` (left, power/LED-broadcast template - has headroom).
- Extensive iterative cleanup rounds per user feedback:
  - Removed all historical/narrative wording ("formerly", "moved here", "instead (see above)")
    - design docs must describe only the current state; history belongs in DEC log + git.
  - Removed "spare"/"reserved" pin labels - every pin must have a specific, current allocation;
    unallocated pins are simply `GND`. The only exception: `5V_MAIN`'s final downstream use may
    be described as depending on the LED part selection tracked in `merge-missing-components.md`.
  - Rebuilt the J5 pin map for **180° rotational symmetry** with an **equal 8/8/8 pin split**
    across `3V3_ENIG`/`5V_MAIN`/GND (excluding the unavoidable GND partner-row of a real signal),
    with RGB/brightness signals split diagonally (2 signals one side, 2 diagonally opposite) and
    `BOARD_ROLE_ID_IN[3:0]`/`BOARD_ROLE_ID_OUT[3:0]` each occupying a full top-row/bottom-row
    block, diagonally opposed.
  - Per further user request, swapped rows so RED/GREEN sit on the opposite row from
    `BOARD_ROLE_ID_IN`'s block (visually/electrically independent, not contiguous).
  - Moved `I2C_SDA`/`I2C_SCL` on the Cypher Board's `J6` template from pins 29/31 to a single
    adjacent pair, pins 27/28.
- Applied identically across `Cypher/Board_Layout.md`, `Cypher/Design_Spec.md`,
  `Cypher-Input/Board_Layout.md`, `Cypher-Input/Design_Spec.md`, and the 3 Cypher-Input variant
  files (`BOARD_ROLE_ID` strap values updated: Classic=`0b0001`, 10-Numeric=`0b0010`,
  64-Character=`0b0111`/`0b1111` custom-enabled).
- DEC-089 created documenting the full architecture change.
- Fixed two stale live-doc references in `Controller/Design_Spec.md` and `Electrical_Design.md`.

## Part 2 - Cypher-Output Board Design Created

Created `design/Electronics/Cypher-Output/` (mirrors Cypher-Input's file structure):

- `Design_Spec.md` - common spec, 3 variants (26-Char Classic/64-Character/10-Numeric)
- `Board_Layout.md` - connector pinouts, ENC module mount tables (identical to Cypher-Input's)
- `Cypher_Output_26_Char_Design.md`, `Cypher_Output_64_Char_Design.md`,
  `Cypher_Output_10_Numeric_Design.md` - variant-specific files

**Key architectural decisions confirmed with user during drafting:**

- Cypher-Output's ENC module runs in the `LBD_DEC` role: decodes `cypher-bits[5:0]` into a
  one-hot `plain-bits[63:0]` lens-position select output (only one lens ever lit at a time).
- **Per-position discrete N-channel MOSFETs (Q1-Qxx, 2N7002K)** gate each lens position's LED,
  driven directly by that position's decoded `PB[n]` line - **not** a shared MOSFET-per-channel
  topology like Cypher-Input (which lights all keys simultaneously with one shared colour). This
  was explicitly justified against sinking LEDs directly through CPLD pins: the EPM570T100I5N has
  zero spare `plain-bits` pins to split colour channels, and a single pin sinking a lit position's
  full worst-case current (up to 30mA for 3 channels through one shared cathode) would exceed the
  CPLD's 8/16mA programmable drive-strength rating (MAX II Device Handbook Table 2-6/8-1) even
  though under the ±25mA absolute max - risking an unreliable VOL/VOH margin. Rationale note added
  directly to `Design_Spec.md §4`.
- No local colour/brightness generation and **no I2C GPIO expander** on this board at all -
  `BOARD_ROLE_ID_OUT[3:0]` is a pure hardwired strap, colour/brightness are received entirely as
  broadcast signals from Cypher-Input via `J4`/`J6`.
- **The custom-support switch (SW1) DOES belong on Cypher-Output** (initially removed by mistake
  mid-session, then correctly restored per user correction) - 64-Character variant only, a
  panel-mount SPDT switch toggling `BOARD_ROLE_ID_OUT[3]` between `0b0111` (default) and `0b1111`
  (custom-support enabled), placed in the same keyless keepout zone that mirrors Cypher-Input's
  RV1 location (this board has no RV1 of its own - brightness is received, not generated).
- Fixed a lens-count inconsistency introduced mid-session: 64-Character variant is **40 lenses**
  (D1-D40/Q1-Q40), not 42 - Shift/Space/Enter have no corresponding lens (nothing to display).
- Removed a redundant "Custom-support strap" row from the common `Design_Spec.md`'s Circuit
  Responsibility table (variant-specific, already fully documented in the 64-Character variant
  file) per user request.

## Part 3 - Design Review Findings (in progress when session paused)

User-led technical review of the completed Cypher-Output draft surfaced several real gaps, all
now fixed:

1. **CPLD drive-strength research** - confirmed via the MAX II Device Handbook that IOH/IOL
   drive-strength settings (8mA/16mA at 3.3V LVTTL/LVCMOS) apply symmetrically to sourcing AND
   sinking, informing the per-position-MOSFET rationale above.
2. **LED mounting-face open item propagated to both boards** - a reverse-mount addressable LED
   candidate (SK6812MINI-E, tracked in `merge-missing-components.md`) could allow rear-face
   mounting instead of top-face hand-soldering; added matching "open item" callouts to both
   `Cypher-Input/Design_Spec.md` and `Cypher-Output/Design_Spec.md`, and updated the todo to
   explicitly require both boards be updated together if/when this is decided.
3. **5V_MAIN power budget gap (significant)** - discovered Cypher-Input's LED bank (U5-U7,
   3 P-MOSFETs, one per colour channel, lighting the ENTIRE key bank simultaneously) draws from
   `5V_MAIN`, not `3V3_ENIG`, and this was **never budgeted anywhere**:
   - Added a `5V_MAIN` entry decoupling bank to Cypher-Input (`DR-CYPI-14a`, C9-C13, 5x 10uF
     X7R 1206) - previously only `3V3_ENIG` had one, despite `5V_MAIN` being a real rail on the
     board per the GRS's per-rail Bulk Entry Bank Rule.
   - Documented the combined worst-case current across all 3 channels (mixed colour, e.g.
     white/yellow/cyan) = **1.26A** (64-Character variant, 42 keys x 3 channels x 10mA) -
     distinct from the existing 420mA single-channel MOSFET-rating figure, which remains correct
     for the per-MOSFET check but was insufficient for the shared-rail figure.
   - Added this 1.26A line item to `Power_Budgets.md`'s 5V_MAIN Load Analysis (previously
     Cypher-Input/Output were entirely absent from the system power budget) - revised system
     total from 9.50A to 10.76A, LMQ61460-Q1 utilisation from 79.2% to 89.7%.
   - **Also fixed a pre-existing stale figure** in the same table: the User Settings Module
     indicator-rail row still showed the old 0.24A (pre-Bank-2-removal) figure, even though
     `User_Settings_Module/Design_Spec.md` itself was already correctly updated to 0.10A earlier
     this session (Bank 2/`CFG_REFMAP` removal, DEC-089) - this cross-reference had not been
     propagated. Corrected and documented in `Power_Budgets.md`'s Document History.
4. **Connector "ownership" wording backwards** - both Cypher-Input's and Cypher-Output's
   `Design_Spec.md` J4-J7 Interconnects subsections had a confusing "Connector definition owner:
   this board..." phrasing that read as if the HID board owned the pin-level template (it does
   not - the Cypher Board does; the HID board only owns its own physical placement/gender).
   Corrected in both files. Also removed misleading `(KBD_ENC role)`/`(LBD_DEC role)` suffixes
   from the J4-J7 heading itself, since those are ENC-module CPLD roles, not properties of the
   interconnect.

## What's Left / Next Steps

**User is continuing the Cypher-Output document review next session before marking
`merge-create-cypher-output` complete.** Do not mark it done until the user confirms the review
is finished. Known still-open items going into that review:

- General re-read of all 5 Cypher-Output files for any remaining inconsistencies (the session
  found several real ones via careful reading - assume more may exist).
- LED part sourcing remains deferred to `merge-missing-components` (SK6812MINI-E candidate under
  evaluation, not yet approved; VDD-vs-3V3_ENIG concern still unresolved for that candidate).
- Once Cypher-Output is confirmed complete: `merge-create-plugboard`, then
  `merge-cypher-board-j3j6-pinouts` (if not already fully resolved by the J5/J6 pin map work this
  session - check current state, this may now be complete).

## Files Changed This Session

- `design/Electronics/Cypher/Design_Spec.md`, `Board_Layout.md`
- `design/Electronics/Cypher-Input/Design_Spec.md`, `Board_Layout.md`, all 3 variant files
- `design/Electronics/Cypher-Output/Design_Spec.md`, `Board_Layout.md`, all 3 variant files
  (**new**)
- `design/Electronics/Controller/Design_Spec.md`, `Electrical_Design.md` (stale reference fixes)
- `design/Electronics/Power_Budgets.md` (5V_MAIN load analysis corrections)
- `design/Design_Log/DEC-089_board-role-id-widened-to-4-bit-capability-bitmask-cpld-pin-freeing-and-j5-migration.md`
  (**new**), `index.md`
- `.copilot/todos/usm-cfg-refmap-removal-review.md`, `.copilot/todos/merge-missing-components.md`

All files lint-clean (`markdownlint`) as of end of session.
