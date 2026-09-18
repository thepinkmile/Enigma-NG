# DEC-103 - HID / USM Hub Connector Topology Rework

|Field|Value|
|:---|:---|
|**Decision ID**|DEC-103|
|**Status**|Decided|
|**Date**|2026-09-17|
|**Author**|Izzyonstage & GitHub Copilot|
|**Amends**|DEC-087, DEC-088, DEC-089|
|**Related**|DEC-104|

## Context

The local Cypher HID assembly previously used a left connector pair for power / board ID / LED
broadcast and a right connector pair for HID JTAG chain-through. The agreed redesign introduces a
User Settings Module hub between Cypher and the HID boards and relocates the HID JTAG serial-data
path onto a dedicated USM-facing connector.

## Decision

- Retire the HID boards' former right-pair `J5` / `J7` connectors.
- Add one dedicated USM-facing right-edge connector to Cypher-Input and one to Cypher-Output.
- Repurpose Cypher `J6` as the USM hub connector.
- Repurpose Cypher-Plugboard `J2` to mate USM rather than a HID board directly.
- Keep the HID left pair in place mechanically, but redefine its pinout to carry the new
  `ENC_DATA_IN[5:0]`, `ENC_DATA_OUT[5:0]`, `ENC_ACTIVE_INPUT_N`, and `ENC_ACTIVE_OUTPUT_N`
  allocation.

## Rationale

- Separates the HID serial-data path from the HID left-pair data / identity path.
- Lets USM serve as the fixed HID spine while keeping Cypher-Input / Cypher-Output order-agnostic.
- Moves the shared lighting-control and HID JTAG aggregation onto the same physical hub board.

## Impact

- Cypher `J5` and all mating HID / Plugboard left connectors adopt the new Template 1 pin map.
- Cypher `J6`, USM top / bottom connectors, and Plugboard `J2` adopt the new Template 2 pin map.
- Cypher-Input `J8`, Cypher-Output `J8`, and USM left connectors adopt the new Template 3 pin map.
