# DEC-098 - Controller ↔ Cypher Dock Split: Power-Only Molex + Signal-Only Samtec (Amends DEC-038, DEC-080)

|Field|Value|
|:---|:---|
|**Decision ID**|DEC-098|
|**Status**|Decided|
|**Date**|2026-09-04|
|**Author**|Izzyonstage & GitHub Copilot|
|**Amends**|DEC-038, DEC-080|
|**Related**|DEC-018, DEC-099, DEC-100|

## Context

The former Stator dock (`J4`/`J5`, per DEC-080) mixed power and signal contacts on the same
connector body: `J5` in particular carried `3V3_ENIG` power blades alongside the JTAG cluster
(`TCK`/`TMS`/`TDI`/`TTD_RETURN`) and I²C. That JTAG cluster is now entirely obsolete — the Cypher
Board's own FT232H USB-JTAG bridge and full 37-device JTAG chain entry are native to the Cypher
Board, so no JTAG signal ever needs to cross the Controller↔Cypher dock. Continuing to route power
and signal through the same 20-contact Molex body also left no useful path to add the newly
required USB D+/D- pair or the expanded I²C bank architecture (see DEC-099) without exceeding the
connector's 15 signal-pitch contacts.

The Cypher Board is the electronic replacement for the retired Stator/Reflector/JTAG Module
functions, so the Controller's former Stator-facing dock connectors are reallocated to serve
Cypher instead of being retired.

## Decision

1. **`J4` becomes a power-only dock** (Molex hybrid pair, unchanged part numbers): Molex
   `2195630015` (Controller receptacle) / `2195620015` (Cypher plug), `G+5P+15S+G` configuration
   (20 contacts: 5 power-pitch + 15 signal-pitch).

   | Contact type | Count | Allocation |
   | :--- | :---: | :--- |
   | Power-pitch (5.78mm pitch, big pins) | 5 | `GND` |
   | Signal-pitch (2.00mm pitch, 4.5A/contact per Molex `2141130000-PS-000` §4.2) | 8 | `5V_MAIN` |
   | Signal-pitch | 7 | `3V3_ENIG` |

   `GND` is deliberately placed on the larger, more mechanically robust power-pitch contacts so
   that it mates first on connector insertion — a safety-oriented mating-order choice, not a
   formal staged-pin guarantee (the Molex datasheet lists "First Mate / Last Break: No" for this
   part). 8 `5V_MAIN` contacts give 36A theoretical capacity and 7 `3V3_ENIG` contacts give 31.5A
   theoretical capacity — both far in excess of the system's actual worst-case demand
   (`Power_Budgets.md`), so splitting the rails across the smaller signal-pitch contacts (rather
   than consuming additional power-pitch positions) is electrically safe while freeing the
   power-pitch contacts entirely for `GND`.

2. **`J5` becomes a signal-only dock** (new Samtec QSS/QTS-025 family, already qualified elsewhere
   in the system): Samtec `QSS-025-01-L-D-A-GP-K` (Controller, vertical female receptacle) /
   `QTS-025-01-L-D-RA-P` (Cypher, right-angle male plug) — the same connector family and mating
   orientation already used between the Cypher Board (motherboard role) and Stack-Input
   (daughtercard role), reusing existing qualified parts with no new BOM line. 50 contacts (25
   columns × 2 rows), center `GND` bar.

   Full pin map: see `Controller/Board_Layout.md §3.2` and `Cypher/Board_Layout.md §1`. Summary of
   carried signals: `PWM0[0-3]`, `GPCLK[0]`/`GPCLK[1]` (reserved, to Cypher bare test pads — see
   DEC-099), `USB_D_PLUS`/`USB_D_MINUS` (to Cypher's native FT232H bridge), `I2C1_SDA`/`SCL`
   (active Cypher-peripherals bus), `I2C2`/`I2C3`/`I2C4`/`I2C6` `SDA`/`SCL` (reserved/NC — see
   DEC-099); all remaining pins `GND`. `I2C0` (PM-dedicated) is deliberately **not** present on
   this connector — see DEC-099.

   The connector's internal ground wedge runs the full connector length between the top (odd) and
   bottom (even) pin rows; top/bottom crosstalk within a column is therefore inherently shielded,
   and the exposure requiring `GND` separator columns is column-to-column (same-row) adjacency
   only.

3. **No TVS/ESD arrays required.** Both `J4` and `J5` remain blind-mate docks (Controller and
   Cypher are assembled together, not hot-swapped in the field like the mini-stack chain), so
   neither requires TVS/ESD protection — consistent with the existing "blind-mate dock: no TVS
   required" convention already stated for Cypher's own `J1`/`J2`.

## Rationale

- Matches electrical function to connector family: heavy, few-contact power on the Molex hybrid
  body (designed for grouped power delivery); high-pin-count controlled signals on the Samtec
  body (already the system's standard for controlled-impedance board-to-board signal chains).
- Frees the JTAG cluster entirely, since it is dead weight on this specific dock now that the
  JTAG bridge is native to Cypher (see DEC-100).
- Reuses existing qualified connector families (Molex hybrid pair, Samtec QSS/QTS-025) rather than
  introducing a third connector family, minimising BOM part-number growth.

## Impact

- `Controller/Design_Spec.md` and `Board_Layout.md`: `J4`/`J5` redefined; former "Stator dock"
  terminology retired in favour of "Cypher power dock" (`J4`) / "Cypher signal dock" (`J5`).
- `Cypher/Design_Spec.md` and `Board_Layout.md`: `J1`/`J2` redefined to match; stale JTAG-cluster
  references on `J2` (left over from the pre-merge Stator `J12` copy) removed.
- The `J4`/`J5` designators are retained (no renumbering) from DEC-080, but their target board and
  internal pin allocation are fully superseded by this decision. The Controller↔Stator dock
  architecture section of DEC-038 is superseded by this reallocation to Cypher; the three-connector
  PM dock and the general "Controller owns external I/O" principle from DEC-038 remain in force.
- Closes `merge-ctl-dock-usb-allocation` and contributes to closing `merge-update-ctl-board`.
