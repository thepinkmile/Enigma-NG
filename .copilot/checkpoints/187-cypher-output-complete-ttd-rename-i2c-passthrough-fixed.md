# Checkpoint 187 — Cypher-Output Complete; TTD Rename & I2C Passthrough Fixed

**Date:** 2026-08-17

## Summary

`merge-create-cypher-output` is now **done**. This session closed out the remaining review
findings on the Cypher-Output board and fixed several real bugs surfaced during that review,
then renamed an ambiguous signal group across the whole Cypher HID interconnect family.

## 1. Cypher-Output `5V_MAIN` bug fixed (missing LED anode-side circuit)

`Cypher-Output/Design_Spec.md §6` claimed `5V_MAIN` was "not consumed by this board's own
circuitry today - passthrough only." This was wrong: the LED bank's anode-side current has to
come from somewhere locally, and no such circuit existed in the doc. Designed and added the
missing drive circuit:

- **U1-U3** (SQ2319ADS-T1_BE3 P-MOSFETs) - colour-bank switches, sourced from local `5V_MAIN`,
  gated by *received* `RED/GREEN/BLUE_DRIVE_N` (never generated locally on this board).
- **U4** (BSS138) - shared brightness termination switch downstream of the per-position select
  MOSFETs (Q1-Qxx), gated by received `BRIGHTNESS_PWM_EN`.
- **C6-C10** - new `5V_MAIN` entry decoupling bank (DR-CYPO-14).
- Updated Circuit Responsibility/FR/DR tables, the component block diagram, BOM, and the J4/J6
  interconnect wiring description.
- Real worst-case current worked out at **30mA** (not the ~1.2A initially assumed) - because only
  one lens position is ever lit at a time on this board (one-hot decode), unlike Cypher-Input's
  whole-bank illumination.
- `Power_Budgets.md` 5V_MAIN Load Analysis updated: added the Cypher-Output line item, total
  revised **10.76A → 10.79A** (89.9% of the LMQ61460-Q1's 12.0A capacity).

## 2. Cross-board documentation bug fixed (Cypher-Input asserting Cypher-Output internals)

`Cypher-Input/Design_Spec.md §3a`/DR-CYPI-17 incorrectly claimed Cypher-Output has "its own I2C
GPIO expander" needing an address from the reserved `0x39-0x3E` block. Cypher-Output's actual,
already-confirmed design has **no I2C bus connection at all**. Removed the Cypher-Output-internals
claim from Cypher-Input's spec and generalised the reserved-address-block wording; also cleaned up
several stale "future Cypher-Output board" references now that it is a real, drafted board.

## 3. LED power-reduction options captured in `merge-missing-components.md`

Discussed options to reduce the LED bank's power draw (row/column scanning/multiplexing, higher-
efficacy LED parts, capped max brightness, dedicated regulator, addressable-LED-enables-software-
control). User's direction: **SK6812MINI-E + row/column scanning**, with capped brightness as a
possible further step. Added a **PoC test board** step to the todo: a small board with a handful
of SK6812MINI-E pixels, current-measurement probe hooks (shunt/Kelvin-sense, mirroring the
`CSS2H-2512R-R010ELF` precedent), **and Kailh PG151101S11 sockets + real Cherry MX2A-71NB
switches/keycaps** so the full mechanical + LED stack-up can be validated together (light
transmission through the light-pipe cutout, clearance, perceived brightness/flicker).

## 4. TTD signal group renamed across the Cypher HID interconnect family

The 3 pins on the Cypher Board's `J6` / Cypher-Input's & Cypher-Output's `J5`/`J7` JTAG template
were all ambiguously named `TTD`. Renamed to describe the actual fixed logical chain (independent
of which board physically sits closest to the Cypher Board):

| Pin (row) | Name | Function |
| :--- | :--- | :--- |
| 37 (top) | `TTD_HID_IN` | Cypher Board → Cypher-Input's own real TDI |
| 36 (bottom) | `TTD_HID_PASS` | Cypher-Input's own real TDO → Cypher-Output's own real TDI |
| 40 (bottom) | `TTD_HID_OUT` | Cypher-Output's own real TDO → back to the Cypher Board |

Each board wires the pins that belong to *its own* role to its real CPLD TDI/TDO, and passes the
other board's pin straight through (not connected to its own CPLD) - e.g. Cypher-Input passes pin
40 straight through, Cypher-Output passes pin 37 straight through. This was a genuine pre-existing
bug (Cypher-Output's original wiring table was copy-pasted identically from Cypher-Input's, which
would not actually form a valid serial JTAG chain). Fixed in `Cypher/Board_Layout.md`,
`Cypher-Input/Board_Layout.md` + `Design_Spec.md`, `Cypher-Output/Board_Layout.md` +
`Design_Spec.md`. The unrelated, system-wide `TTD`/`TTD_RETURN` naming used elsewhere (Controller
`J1/J2`, Cypher `J3/J4`, Stator/Reflector/Extension/Rotor chain) was left untouched - that is a
different physical chain.

## 5. I2C passthrough restored on Cypher-Output `J5`/`J7`

Pins 27/28 (`I2C_SDA`/`I2C_SCL` on the shared template) had been incorrectly marked `GND` on
Cypher-Output - they must remain a passthrough (not connected to Cypher-Output's own circuitry,
since it has no I2C device) so Cypher-Input's I2C bus can still reach the Cypher Board when
Cypher-Output sits directly beneath it. Fixed in `Cypher-Output/Board_Layout.md` and
`Design_Spec.md`.

## Status

- `merge-create-cypher-output`: **done**.
- Todo detail file archived to `.recycle-bin/merge-create-cypher-output.md` (content was stale
  relative to the final built design; this checkpoint is the authoritative summary).
- Next session: start with `merge-create-plugboard` (all its dependencies - `design-discussion-
  merge`, `merge-grs-6layer-stackup`, `merge-create-cypher-input`, `merge-create-cypher-output` -
  are satisfied; well-scoped by DEC-088 as a passive HID-chain termination board, mirroring
  Stack-Blanking, plus mechanical-only jack-field mounting wired via spade harness to the Cypher
  Board).
