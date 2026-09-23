# DEC-107 - USM/HID Connector Four-Colour-Style Signal Expansion

|Field|Value|
|:---|:---|
|**Decision ID**|DEC-107|
|**Status**|Decided|
|**Date**|2026-09-21|
|**Author**|Izzyonstage & GitHub Copilot|
|**Amends**|DEC-103, DEC-104|
|**Related**|DEC-105, DEC-106|

## Context

The Template 3 connector (User Settings Module's left connectors, mating each HID board's own
right-edge connector) originally carried a single generic `RED_DRIVE_N`/`GREEN_DRIVE_N`/
`BLUE_DRIVE_N`/`ILLUMINATION_DRIVE_N` signal group, broadcast identically on both rows. Reviewing
the Cypher-Input 64-Character variant's LED requirements surfaced a gap: a HID board's own local
logic (e.g. a colour-select mux keyed on Shift state) needs simultaneous access to more than one
of USM's stored colour values in order to switch between them in real time. A single broadcast
signal group cannot represent more than one colour at a time.

## Decision

- Expand Template 3 to carry **four independent colour-style signal groups**, each with its own
  `RED_DRIVE_{n}_N`/`GREEN_DRIVE_{n}_N`/`BLUE_DRIVE_{n}_N`/`ILLUMINATION_DRIVE_{n}_N` set
  (`n` = 1-4), rather than one shared/generic group.
- The User Settings Module's colour-value store is expanded to hold **4 colour styles** instead
  of 3. The initial system configuration uses only 3 (Colour1 = idle/static baseline, Colour2 =
  standard key-press, Colour3 = shifted key-press); Colour4 is reserved for future use and is not
  consumed by any board today.
- Reallocate Template 3's pin map: `TDI_INPUT`/`TDO_INPUT`/`TMS`/`TCK`/`CPLD_RESET_N` shifted one
  column closer to the center GND bar (their neighbouring JTAG/reset signals do not create
  signal-integrity concerns when adjacent, since TDI/TDO are inactive whenever `CPLD_RESET_N` is
  toggled); `I2C_SDA`/`I2C_SCL` relocated adjacent to the static `3V3_ENIG` rails (also separated
  by the center GND bar, so signal integrity is unaffected by the static rail's proximity); the
  freed columns host the 3 additional colour-style signal groups (Colour1, Colour2, Colour4 -
  Colour3 keeps its original pin positions).

## Rationale

- A HID board cannot arbitrate between multiple stored colour values in real time using only one
  broadcast signal group - each value a board's own local logic needs simultaneous access to must
  have its own dedicated set of pins.
- Reserving a 4th colour style now avoids a second connector rework later if a future requirement
  needs a 4th distinct colour value.
- Repositioning JTAG/reset and I2C signals adjacent to their respective "safe" neighbours (reset
  state or static power rails) keeps the new colour-style pin groups contiguous and readable
  without introducing any new signal-integrity risk.

## Impact

- `User_Settings_Module/Board_Layout.md` (Template 3 owner) and both HID boards'
  (`Cypher-Input`/`Cypher-Output`) own connector-usage notes must be updated to reference the
  4-colour-style pin map instead of the single generic signal group.
- `User_Settings_Module/Design_Spec.md`'s colour-value store description changes from "3 colour
  values" to "4 colour styles (3 used, 1 reserved for future use)".
- Any HID board's own local colour-selection circuit (e.g. Cypher-Input 64-Character's Shift-key
  colour mux) now sources its inputs from the specific colour-style pin group(s) it needs, instead
  of a single shared signal group.
