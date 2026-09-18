# DEC-105 - CFG_ROUTE Moved to Full CM5 Software Control; Physical USM Switches Retired

|Field|Value|
|:---|:---|
|**Decision ID**|DEC-105|
|**Status**|Decided|
|**Date**|2026-09-17|
|**Author**|Izzyonstage & GitHub Copilot|
|**Amends**|DEC-032, DEC-071|
|**Related**|DEC-089, DEC-104|

## Context

`CFG_REFMAP` had already moved to the Cypher JTAG UFM-write path under DEC-089. The remaining
physical `CFG_ROUTE` switch and `CFG_APPLY_N` pushbutton path on USM were then superseded by the
agreed Cypher-centric HID redesign.

## Decision

- Remove the physical `CFG_ROUTE` switches from USM.
- Remove the physical `CFG_APPLY_N` pushbutton path from USM.
- Keep `CFG_ROUTE[3:0]` as a CM5-owned value presented to Cypher `U8` over the Cypher-local I2C
  path.
- Keep reflector-map selection under DEC-089's JTAG UFM-write mechanism.

## Rationale

- Aligns both configuration banks under software ownership.
- Removes the remaining hardware state on USM that no longer serves the active design.

## Impact

- USM no longer hosts `CFG_ROUTE` or `CFG_APPLY_N` hardware.
- Cypher no longer documents the `CFG_APPLY_N` signal or the former USM harness connector.
