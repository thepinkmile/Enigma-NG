# DEC-100 - JTAG Module and Actuation Module Retirement from Controller Board

|Field|Value|
|:---|:---|
|**Decision ID**|DEC-100|
|**Status**|Decided|
|**Date**|2026-09-04|
|**Author**|Izzyonstage & GitHub Copilot|
|**Amends**|-|
|**Related**|DEC-043, DEC-057, DEC-058, DEC-093, DEC-097, DEC-098, DEC-099|

## Context

The Controller Board's design still carried a physical daughterboard dock for both the JTAG
Module and the Actuation Module, plus a direct `ACTUATE_REQUEST_N` GPIO (CM5 GPIO 8) driving the
AM host dock. Both daughterboards are obsolete now that their functions live natively on other
boards:

- The JTAG Module's FT232H bridge, TCK/TMS/TDI series damping, and JTAG buffer are already
  duplicated on the Cypher Board (`U17`, `U18`, `Y1`) — the Controller's JM dock was therefore
  dead hardware with no active consumer.
- The Actuation Module's solenoid drive/homing/latching MCU (STM32G071K8T3TR) is native to the
  Stack-Input Board (`Stack-Input/Design_Spec.md DR-SIN-03`), one instance per mini-stack,
  triggered by `ACTUATE_REQUEST_IN_N` arriving on that board's own `J1`. The Controller's
  `ACTUATE_REQUEST_N` GPIO and AM host dock had no remaining role — the actuation trigger
  originates and terminates at the Cypher Board's own CPLD (`U1`), not at the Controller.

This decision **only** removes the Controller-side host docks for these two now-retired
daughterboards. It does not change the actuation architecture itself (already fully defined by
DEC-093/DEC-097) and does not imply the Actuation Module's MCU/solenoid circuitry has been removed
from the system — that circuitry remains native to the Stack-Input Board, one instance per
mini-stack (a known simplification to be revisited in a future discussion, per user direction).

## Decision

1. **Remove JM dock (`J12`).** Remove `J12` (Hirose DF40HC(3.5)-20DS-0.4V(51) BtB receptacle) and
   standoffs `MH9`-`MH12` (9774035151R) from the Controller Board. Remove the JTAG pass-through
   description (Controller previously routed `TCK`/`TMS`/`TDI`/`TTD_RETURN` from `J12` to the
   former Stator logic dock `J5` with no active components) — this entire signal path no longer
   exists on the Controller. Controller's L6 (bottom outer) layer role updated: "JTAG pass-through
   traces" removed from the stackup's signal-assignment table (no JTAG signals remain on the
   Controller at all).

2. **Remove AM host dock (`J11`).** Remove `J11` (Hirose DF40HC(3.5)-20DS-0.4V(51) BtB
   receptacle) and standoffs `MH5`-`MH8` (9774035151R) from the Controller Board. Remove CM5
   GPIO 8 `ACTUATE_REQUEST_N` allocation; GPIO 8 is reassigned to `I2C0_SDA` (see DEC-099). Remove
   `R4` (10kΩ boot-safe pull-up on the former `ACTUATE_REQUEST_N`) from the Controller BOM.

## Rationale

- Both daughterboards' functions are fully covered by existing native circuitry elsewhere in the
  system (Cypher Board for JTAG, Stack-Input Board for actuation); retaining dead connector
  footprints, standoffs, and GPIO allocations on the Controller serves no purpose and only
  consumes board area and BOM lines.
- Frees CM5 GPIO 8 for the `I2C0` PM-dedicated bus (DEC-099), directly enabling that architecture
  change.
- Consistent with the existing project convention (DEC-055/DEC-080) of closing FR/DR/BOM
  identifier gaps left by removed items via renumbering rather than leaving retired IDs in place.

## Impact

- `Controller/Design_Spec.md`: full FR/DR renumbering (see the document itself for the current
  authoritative numbering); JM (former §3 JTAG Programming Subsystem, former §8.3 JM BtB Dock) and
  AM (former §8.6 AM Host Dock) sections removed; BOM rows `J11`, `J12`, `MH5`-`MH8`, `MH9`-`MH12`,
  `R4` removed.
- `Controller/Board_Layout.md`: former §6 (J11 AM Host Dock) removed; placement summary diagram
  updated to remove the JM dock and Actuation Module boxes; subsequent sections renumbered.
- `Power_Budgets.md`: relocated the "servo rail" 5V_MAIN line item from a direct Controller draw
  (via the retired `J11` host dock) to "Stack-Input Board solenoid actuation" (via Cypher Board
  `J4` power dock → mini-stack `5V_MAIN`) — the actuator itself was never removed from the system,
  only its physical host dock moved off the Controller; the 0.50 A figure is retained as a
  placeholder pending the still-TBD solenoid driver circuit. Total 5V_MAIN worst case unchanged at
  10.79 A.
- `Boards_Overview.md`/`System_Architecture.md` still describe the pre-merge JM/AM architecture as
  part of a broader pre-existing staleness predating the Cypher Board merge — out of scope for
  this decision; flagged separately for a future documentation pass.
- Contributes to closing `merge-update-ctl-board`.
