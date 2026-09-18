# DEC-106 - Cypher-Plugboard Reduced to Mechanical / Connector-Only Board

|Field|Value|
|:---|:---|
|**Decision ID**|DEC-106|
|**Status**|Decided|
|**Date**|2026-09-17|
|**Author**|Izzyonstage & GitHub Copilot|
|**Amends**|DEC-088|
|**Related**|DEC-103|

## Context

Cypher-Plugboard already carried a minimal electrical role after the Cypher integration work. The
agreed USM hub topology removes the board's remaining JTAG branch termination role as well.

## Decision

- Remove the Plugboard board's local termination resistors.
- Retain only the two board-to-board connector footprints (`J1`, `J2`) on the PCB strip.
- Keep the physical jack field mechanical-only and harnessed directly to Cypher `J20+`.

## Rationale

- Places the JTAG idle-termination network on USM, which now owns the HID branch aggregation.
- Leaves Cypher-Plugboard as a pure mechanical / connector board.

## Impact

- `design/Electronics/Cypher-Plugboard/Design_Spec.md` and `Board_Layout.md` remove all active
  electrical population.
- The plugboard variant files continue to own only the jack-field population and enclosure detail.
