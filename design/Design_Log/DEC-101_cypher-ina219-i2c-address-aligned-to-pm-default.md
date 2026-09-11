# DEC-101 - Cypher Board INA219 I2C Address Aligned to PM Default (0x45 → 0x40)

|Field|Value|
|:---|:---|
|**Decision ID**|DEC-101|
|**Status**|Decided|
|**Date**|2026-09-08|
|**Author**|Izzyonstage & GitHub Copilot|
|**Amends**|-|
|**Related**|DEC-098, DEC-099|

## Context

The system has two INA219 current/power monitors: the Power Module's `U10` (5V_MAIN monitoring)
and the Cypher Board's `U2` (rotor-stack `3V3_ENIG` monitoring). `U10` sits at the INA219's
**default** address `0x40` (`A0`/`A1` both tied to `GND` — no address-strap components required).
`U2` was assigned `0x45`, a non-default address requiring a specific `A0`/`A1` strap combination
per the INA219 datasheet's address table — a strap that was never actually documented at the
pin level in the Cypher Board's own spec (unlike, e.g., the Cypher Board's `U8` MCP23017, whose
`A2`/`A1`/`A0` strapping is explicitly called out).

`0x45` was originally chosen purely to avoid an address collision with `U10`'s `0x40`, back when
both devices were expected to share a single physical I²C bus. DEC-098/DEC-099 (2026-09-04) split
the system onto six independent I²C bus instances, with the Power Module and Cypher Board now on
entirely separate buses (`I2C0` and `I2C1` respectively) — the original collision concern no
longer applies.

## Decision

Change the Cypher Board's `U2` (INA219) I²C address from `0x45` to `0x40`, matching the Power
Module's `U10`. Both devices use the INA219 default address configuration (`A0`/`A1` both tied to
`GND`), requiring zero address-strap components on either board.

## Rationale

- **Software simplification:** identical driver/read code can now service both power monitors,
  with only the I²C bus/bank number differing between them (`I2C0` for PM, `I2C1` for Cypher).
- **Hardware simplification:** the INA219 default address requires no strap components at all —
  simpler and cheaper than implementing the specific non-default strap `0x45` would have required
  (which, in any case, had never been fully specified at the pin level on the Cypher Board).
- No collision risk: the two devices are on independent I²C buses (`I2C0` vs `I2C1`), so
  duplicate addresses across boards are safe by construction.

## Impact

- `Cypher/Design_Spec.md §7 Power Telemetry`: `U2` address updated to `0x40`, with a note
  explaining the deliberate same-address reuse across independent buses.
- `Controller/Design_Spec.md §3 Telemetry & Logic, §3.1 I²C Bus Topology, FR-CTL-05`: INA219
  address references updated from `0x45` to `0x40`.
- `Power_Budgets.md`: shunt-part note (§ INA219 shunt selection rationale) updated to reference
  the new `0x40` address on the Cypher Board's `R1`/`U2`.
- Not touched (pre-existing staleness, deferred per prior user direction — see `plan.md`): the
  legacy "Stator" INA219 references in `Boards_Overview.md`, `Electrical_Design.md`,
  `Software/Linux_OS/Power_Management.md`, `Software/GUI_App/Design_Spec.md`, and the GUI
  wireframe `.drawio` files still describe the pre-merge architecture at `0x45`. These are already
  flagged for full rewrite under `merge-update-top-level-docs` (electronics docs) and the
  eventual software-documentation overhaul pass (out of scope until the full electronics design
  is merged), so are not corrected here to avoid inconsistent partial updates.
