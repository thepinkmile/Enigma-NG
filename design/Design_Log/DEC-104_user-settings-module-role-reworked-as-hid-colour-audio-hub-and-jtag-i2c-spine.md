# DEC-104 - User Settings Module Reworked as HID Colour / Audio Hub and JTAG/I2C Spine

|Field|Value|
|:---|:---|
|**Decision ID**|DEC-104|
|**Status**|Decided|
|**Date**|2026-09-17|
|**Author**|Izzyonstage & GitHub Copilot|
|**Amends**|DEC-032, DEC-034, DEC-051, DEC-071|
|**Related**|DEC-103, DEC-105|

## Context

USM previously documented a switch-and-indicator role for `CFG_ROUTE` / `CFG_REFMAP`. The agreed
redesign repurposes the board into the shared HID lighting hub and the physical bridge between
Cypher, the HID pair, and Plugboard.

## Decision

- USM becomes the shared HID colour / brightness hub.
- USM hosts the dedicated Cypher-peripherals I2C bus endpoint for the HID lighting path.
- USM hosts the relocated JTAG idle-termination network for the HID branch.
- USM reserves a placeholder-only audio position pending a later buzzer / speaker choice.
- USM no longer carries a user switch panel role.

## Rationale

- Centralises the shared HID lighting and JTAG aggregation on the one board that physically touches
  Cypher, both HID boards, and Plugboard.
- Removes now-obsolete panel-control circuitry from the active design.
- Keeps the deferred audio decision attached to the correct physical board.

## Impact

- `design/Electronics/User_Settings_Module/Design_Spec.md` and `Board_Layout.md` are rewritten.
- Cypher, Cypher-Input, Cypher-Output, and Cypher-Plugboard documents now reference USM as the
  HID hub and JTAG / I2C spine.
