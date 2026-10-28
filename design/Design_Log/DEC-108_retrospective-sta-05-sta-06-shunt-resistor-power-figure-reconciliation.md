# DEC-108 - Retrospective: STA-05/STA-06 Shunt Resistor and Power Figure Reconciliation

- **Status:** Decided
- **Date:** 2026-04-05
- **Category:** Power Budget / Component Selection
- **Area:** Stator (historical; superseded by Cypher Board), Controller, Rotor
- **Author:** Izzyonstage & GitHub Copilot

## Retrospective Note

This entry was **not recorded at the time the decision was made**. The
reconciliation below was originally resolved directly within
`Power_Budgets.md` (as a "Conflict Resolution" working log) rather than being
captured as a permanent Design Log entry, which is this project's actual
system of record for historical design decisions. This DEC is being written
retrospectively (2026-10-28) to correct that gap before the working-log
content is removed from `Power_Budgets.md`, which must contain current design
figures only, per this project's standing documentation convention.

## Summary

Reconciled three conflicting power/shunt figures found in early drafts of the
Stator, Controller, and Rotor design specs (tracked as findings `STA-05` and
`STA-06`): an inflated rotor-stack peak-current claim, a mismatched
Controller-dock capacity claim, and inconsistent shunt resistor values between
the Stator and Controller boards.

## Problem

1. **Stator §2 "5A peak" claim.** The Stator design spec claimed a 5.0 A peak
   current draw for the rotor-stack distribution branch. This figure was not
   derived from any per-device budget and did not match the per-CPLD current
   estimates used elsewhere in the design.
2. **Controller↔Stator dock capacity claim.** A separate claim of 5.5 A dock
   capacity (based on an earlier Samtec Link-Beta connector family, later
   retired by DEC-038) was carried forward after the connector family changed,
   leaving a stale figure that no longer matched the installed hardware.
3. **Rotor x30 "4.5A" claim.** The Rotor design spec claimed 4.5 A (150 mA per
   rotor x 30) for the full rotor stack, again not traceable to a per-device
   budget.
4. **Shunt resistor mismatch.** The Stator design used a 20 mΩ shunt while the
   Controller design assumed a 10 mΩ shunt for the same current-telemetry
   path, an inconsistency between two boards describing the same physical
   measurement point.

## Decision

| Finding | Old figure | Reconciled value |
| :--- | :--- | :--- |
| Stator §2 "5A peak" | 5.0 A | **2.05 A** worst-case typical (derived from the per-device 3V3_ENIG load analysis) |
| Controller↔Stator dock capacity | 5.5 A | Not the bottleneck - the hybrid Molex dock capacity comfortably exceeds the 3.0 A Power Module LDO limit, which is the true system constraint (Samtec Link-Beta figure retired by DEC-038) |
| Rotor x30 claim | 4.5 A | **1.65 A** (30 x 55 mA per-rotor budget figure, 1.63 A typical) |
| Shunt resistor | Stator: 20 mΩ; Controller: 10 mΩ | **10 mΩ CSS2H-2512R-R010ELF** (Kelvin-sense, 2512 package) on both boards' current-telemetry paths |

The reconciled 10 mΩ CSS2H-2512R-R010ELF shunt was selected using the
following rationale, re-derived against the reconciled 2.05 A typical / 3.00 A
max current range:

- V_drop at 2.05 A: 2.05 x 0.010 = 20.5 mV - within the INA219's ±80 mV PGA range.
- V_drop at 3.00 A max: 3.00 x 0.010 = 30 mV - within range.
- Resolution: 12-bit ADC at ±80 mV range gives an LSB of ~39 µV, so
  I_LSB = 39µV / 0.010Ω ≈ 4 mA current resolution.
- Power dissipation at 2.05 A: 2.05² x 0.010 = 42 mW; at 3.00 A max:
  3.00² x 0.010 = 90 mW - both comfortably within the 2512 Kelvin package's
  ≥0.5 W rating.
- CAL register: 0x0400 (1024), unchanged - CAL = 0.04096 / (Current_LSB x
  R_SHUNT) = 0.04096 / (0.004 x 0.010) = 1024.

## Rationale

Power budget and component-selection figures must be traceable to an actual
per-device load analysis rather than carried forward as unverified estimates.
Reconciling to a single shunt part across both boards sharing the same
current-telemetry measurement point also removes an inter-board inconsistency
that would otherwise require two different BOM entries for electrically
equivalent positions.

## Current Status

The Stator board's role in this measurement path has since been consolidated
into the Cypher Board (see the Cypher-system board merge). The reconciled
figures and shunt part selection remain in force; `Power_Budgets.md` and
`Cypher/Design_Spec.md` carry the current, non-historical statement of these
values.
