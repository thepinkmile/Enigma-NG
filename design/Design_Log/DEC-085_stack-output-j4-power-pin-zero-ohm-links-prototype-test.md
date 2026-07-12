# DEC-085 - Stack-Output J4 Power-Pin 0Ω Links for Prototype Test Flexibility

|Field|Value|
|:---|:---|
|**Decision ID**|DEC-085|
|**Status**|Accepted — confirm after prototype testing|
|**Date**|2026-07-12|
|**Author**|Izzyonstage & GitHub Copilot|
|**Amends**|DR-SOUT-04 in `design/Electronics/Stack-Output/Design_Spec.md`|

## Context

Stack-Output Board J4 is the ERF8-005 power connector receiving 3V3_ENIG (×5 pins) and GND (×5
pins) from the last ROT board in the mini-stack. The initial design set all J4 pins to NC, following
the conservative pattern of the retiring Extension Board J2 (no connect to avoid a dual-feed ground
loop).

A design review identified that, in the compact mini-stack assembly, the ground-loop concern is
weaker than in the original extended architecture:

1. **Board stackup shielding:** All boards use 4-layer stackup with GND planes on L1 and L4 (outer
   layers). This provides natural shielding within the board itself.
2. **Metal enclosure:** The system is housed in a metal enclosure that discharges through a single
   GND_CHASSIS to GND bond located at the Power Module (DEC-020). This single-point bond prevents
   enclosure-level ground loops.
3. **Compact loop area:** The current loop created by connecting J4 (mini-stack internal path) and J1
   stacking connector (external path) has a small physical area — far less susceptible to magnetic
   field coupling than the long inter-board ribbon cable loops of the legacy architecture.

Connecting J4 power pins would reduce power rail impedance and shorten return current paths for ROT
CPLD switching transients, potentially improving EMC performance.

## Decision

Install 0Ω link resistors on the Stack-Output Board:

- **R4 (0Ω link):** Connects the J4 3V3_ENIG bus node to the local 3V3_ENIG power plane
- **R5 (0Ω link):** Connects the J4 GND bus node to the local GND plane

Both resistors use standard 0402 footprint and can be removed by the assembler or reworked in the
field to break the J4 power connection if prototype testing reveals EMI or ground-loop issues.

This approach provides:

- Shorter return current paths for ROT CPLD switching transients within the mini-stack
- Reduced effective power rail impedance via parallel delivery
- A simple, reversible mechanism to test both connected and disconnected configurations

## Rationale

The 0Ω link approach was chosen over a hard-connected PCB trace because:

1. **Prototype test flexibility:** Removing two 0402 resistors is straightforward rework with a
   hot-air station or fine-tip iron. This avoids board re-spin if the connected configuration proves
   problematic.
2. **Conservative baseline retained:** If links are removed, the board reverts to the original NC
   behaviour with no functional impact.
3. **Low cost:** Two 0Ω 0402 resistors add negligible BOM cost.

## Prototype Testing Action

After first-article build and functional testing, evaluate EMC/EMI performance with R4/R5 fitted
(connected) vs. removed (NC). If no measurable improvement or regression is observed, retain the
connected configuration as the production default. If the connected configuration creates issues,
remove R4/R5 and update this DEC to **Confirmed — disconnected**.

## Impact

- `design/Electronics/Stack-Output/Design_Spec.md` — DR-SOUT-04 updated; R4/R5 added to BOM;
  §5 Power and §6 J4 sections updated.
