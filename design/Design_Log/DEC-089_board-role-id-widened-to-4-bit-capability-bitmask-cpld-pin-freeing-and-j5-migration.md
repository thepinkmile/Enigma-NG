# DEC-089 - `BOARD_ROLE_ID` Widened to 4-Bit Capability Bitmask; CPLD Pin-Freeing via JTAG UFM Write; Migration to `J5`

|Field|Value|
|:---|:---|
|**Decision ID**|DEC-089|
|**Status**|Decided|
|**Date**|2026-08-16|
|**Author**|Izzyonstage & GitHub Copilot|
|**Amends**|`Cypher/Design_Spec.md §3, §3a`; `Cypher/Board_Layout.md §4`; `Cypher-Input/Design_Spec.md §3a, §7`; `Cypher-Input/Board_Layout.md §4`; `Cypher_Input_26_Char_Design.md`, `Cypher_Input_64_Char_Design.md`, `Cypher_Input_10_Numeric_Design.md`; `User_Settings_Module/Design_Spec.md` (`CFG_REFMAP` removal, tracked separately in `usm-cfg-refmap-removal-review.md`)|

## Context

The user requested that Cypher-Output boards mirror Cypher-Input's own variant family, with a
hardware compatibility check between whichever Cypher-Input and Cypher-Output boards are
installed together - so an incompatible pairing (e.g. a 26-Char Classic keyboard paired with a
10-Numeric lightboard) can be detected and reported to the CM5, rather than silently producing
garbled output.

Working through the mechanism surfaced several constraints:

1. **Row convention is fixed per board, not per physical position.** Each board's own PCB always
   drives its own `BOARD_ROLE_ID` value onto its own top row and passes the *other* board's value
   through unchanged on the bottom row (already established for `BOARD_ROLE_ID[2:0]` and
   `ENC_DATA[5:0]`). Because of this, the Cypher Board's own connector always sees Cypher-Input's
   ID on the top row and Cypher-Output's ID on the bottom row, regardless of which of the two HID
   boards is physically closer to the Cypher Board.
2. **A 3-bit enumerated ID cannot express a compatibility rule cleanly.** The user proposed
   redefining `BOARD_ROLE_ID` as a 4-bit **capability bitmask** instead of an enumerated index:
   bit0 = Characters, bit1 = Numbers, bit2 = Special, bit3 = Custom. A Cypher-Output board is
   compatible with a Cypher-Input board when `AND(BOARD_ROLE_ID_OUT, BOARD_ROLE_ID_IN) ==
   BOARD_ROLE_ID_IN` (the Output's capabilities must be a superset of the Input's requirements).
   This single rule also naturally covers the "Custom" bit with no special-casing.
3. **The CPLD (EPM570T100I5N, 76 user I/O) had zero spare pins for the extra comparator I/O.**
   Before this change: 70/76 used (60 for `ENC_DATA` routing across 10 six-bit ports, plus 4
   `CFG_ROUTE` + 6 `CFG_REFMAP`), leaving 6 spare - not enough for
   `BOARD_ROLE_ID_IN[3:0]` + `BOARD_ROLE_ID_OUT[3:0]` + `HID_VARIANT_ID[3:0]` (12 pins needed).
4. **The right-hand (`J6`) HID interconnect template had no spare pin budget** once widened from
   3 to 4 bits, since it is already fully packed with real switching signals (`ENC_DATA`, `TTD`,
   `TMS`, `TCK`, `I2C`) plus their required GND shielding.

## Decision

1. **`CFG_REFMAP[5:0]` (the parallel GPIO reflector-map-select bus) is removed entirely** and
   replaced with a JTAG-based mechanism: the CM5 writes the active reflector-map index directly
   into the CPLD's UFM via the existing JTAG chain (in-system UFM write via the FT232H JTAG
   bridge), rather than driving it as a live parallel bus. This frees the 6 CPLD I/O pins
   previously allocated to `CFG_REFMAP[5:0]`, and removes the corresponding Bank 2 hardware
   (SW5-SW10, D6-D12, U3 expander, associated MOSFETs/resistors) from the User Settings Module -
   tracked in `usm-cfg-refmap-removal-review.md`.
2. **`BOARD_ROLE_ID` is widened from 3 bits (enumerated index) to 4 bits (capability bitmask):**
   bit0 = Characters, bit1 = Numbers, bit2 = Special, bit3 = Custom. Known values: 26-Char
   Classic = `0b0001`; 10-Numeric = `0b0010`; 64-Character (default) = `0b0111`; 64-Character
   (custom-support enabled) = `0b1111`. The `0` value (`0b0000`) is reserved as the error/
   incompatible sentinel and is never a valid real-board ID.
3. **The Cypher Board's CPLD hosts a `BOARD_ROLE_ID` compatibility comparator:** inputs
   `BOARD_ROLE_ID_IN[3:0]` (from Cypher-Input) and `BOARD_ROLE_ID_OUT[3:0]` (from Cypher-Output),
   output `HID_VARIANT_ID[3:0]` = Cypher-Input's own ID value when
   `AND(BOARD_ROLE_ID_OUT, BOARD_ROLE_ID_IN) == BOARD_ROLE_ID_IN` (compatible), else `0b0000`
   (incompatible/error), for the CM5 to read and act on.
4. **`BOARD_ROLE_ID[3:0]` moves from the `J6` (right, JTAG-template) connector to the `J5` (left,
   power/LED-broadcast) connector**, since `J6` has no spare pin budget once widened to 4 bits
   while `J5` has 12 columns of spare headroom. Freed `J6` pins (formerly columns 9-11, pins
   17-22) become spare/GND. The `J5` template's power/GND pin budget rule (minimum 2 pins each of
   `3V3_ENIG`, `5V_MAIN`, and GND, excluding the center bar) is preserved; `BOARD_ROLE_ID[3:0]`
   occupies 8 of the resulting spare columns (pins 17-24), still leaving 12 columns (27-50) of
   headroom.
5. **A Cypher-Output board (not yet designed) will carry a user-accessible custom-support SPDT
   switch** next to its own brightness dial (RV1, the board's "keyboard settings" area), wired
   common-to-`BOARD_ROLE_ID[3]`, one throw to GND (default, bit3 = 0), the other to `3V3_ENIG`
   (custom-enabled, bit3 = 1) - so the 64-Character Cypher-Output variant can be switched between
   `0b0111` (default) and `0b1111` (declares custom-keyboard support) without a board respin. A
   0-Ohm DNF link is also reserved on the same net for user modification if a future custom
   lightboard needs the same capability.

## Rationale

- A capability bitmask with a simple `AND`-based compatibility rule is more extensible than an
  enumerated index requiring an explicit compatibility lookup table, and elegantly generalises to
  custom/future capability combinations without special-casing.
- Moving the reflector-map mechanism to JTAG UFM writes removes an entire 6-pin parallel bus and
  its associated USM front-panel hardware, at the cost of firmware-level engineering deferred to
  a later pass - an acceptable trade given the CPLD pin budget was otherwise exhausted.
- `J5` already has substantial spare headroom (12 free columns) while `J6` has none once widened;
  moving a permanently-tied hardware strap (not a dynamic/switching signal) to `J5` costs nothing
  in GND-shielding overhead, since it remains exempt from the "full zig-zag" shielding convention
  established for `BOARD_ROLE_ID` previously.

## Impact

- `Cypher/Design_Spec.md` - CPLD I/O budget table updated (0 spare, 76/76 used); new §3a
  `BOARD_ROLE_ID` Compatibility Comparator section; U7 GPIO table gains `HID_VARIANT_ID[3:0]`; U8
  GPIO table loses `CFG_REFMAP[5:0]`; FR-STA-09/DR-STA-11/DR-STA-13 rewritten for the JTAG UFM
  mechanism; BOM R18-R23 removed.
- `Cypher/Board_Layout.md` - new "J5 - Full Pin Map" section (power/LED broadcast/
  `BOARD_ROLE_ID[3:0]`); existing "J6 - Full Pin Map" section's former `BOARD_ROLE_ID[2:0]` pins
  (17-22) marked spare/GND, encoding table removed/pointed at the new `J5` section.
- `Cypher-Input/Design_Spec.md` - variant table and all `BOARD_ROLE_ID` references updated to
  4-bit values; §7 Interconnects rewritten so `BOARD_ROLE_ID[3:0]` lives on the `J4`/`J6` left
  pair (matching the Cypher Board's own `J5` template) instead of `J5`/`J7`.
- `Cypher-Input/Board_Layout.md` - new "J4 / J6 - Full Pin Map" section; "J5 / J7 - Full Pin Map"
  section's former `BOARD_ROLE_ID[2:0]` pins (17-22) marked spare/GND.
- `Cypher_Input_26_Char_Design.md`, `Cypher_Input_64_Char_Design.md`,
  `Cypher_Input_10_Numeric_Design.md` - `BOARD_ROLE_ID` strap value lines updated to `0b0001`,
  `0b0111`, `0b0010` respectively.
- `User_Settings_Module/Design_Spec.md`/`Board_Layout.md` - Bank 2 (`CFG_REFMAP`) hardware
  removed (tracked in `usm-cfg-refmap-removal-review.md`, now largely resolved by this decision's
  JTAG UFM mechanism).
- Cypher-Output board (not yet designed) - must include the custom-support SPDT switch next to
  RV1, and its own CPLD-side `BOARD_ROLE_ID_OUT[3:0]`/`HID_VARIANT_ID[3:0]` wiring per this
  decision, when that board's design work begins.
