# Cypher-Plugboard Board V1.0 Pinout Reference

**Status:** Draft
**Project:** Enigma-NG
**Author:** Izzyonstage & GitHub Copilot
**Version:** v.0.1.0
**Associated Hardware Revision:** Rev A
**Last Updated:** 2026-10-05

> **Board_Layout.md is a visualisation-only document.** Design narrative, specifications, and
> component rationale belong in `Design_Spec.md`. This file contains connector pinout references
> and board orientation notes only.

---

## Orientation Convention

- **PCB (thin strip, top edge only):** carries J1 (left) and J2 (right) connectors, no active
  components, fully populated by JLCPCB's single-sided SMT PCBA pass. Identical across all three
  variants - it does **not** carry the jack field.
- **Machined metal enclosure (separate from the PCB):** hosts the entire plugboard jack field -
  mechanical/harness-wired only, no PCB trace connection (see `Design_Spec.md §4`). Character
  rows run top-to-bottom, engraved/printed directly on the enclosure; row layout and jack count
  are variant-specific, and the enclosure itself is sized per variant (see each variant's own
  design file). Every jack's metal bushing bonds directly to this enclosure, keeping the whole
  jack field on the system's `GND_CHASSIS` network (see `Design_Spec.md §2`).
- **J1 (left, male):** mounted protruding past this board's top edge far enough to span the
  enclosure gap and fully mate with the flush-mounted female connector of whichever HID board
  (Cypher-Input or Cypher-Output) sits directly above - the bottom-most board of the local
  2-board HID stack, per the shared Cypher Left Pair Template.
- **J2 (right, male):** mounted protruding past this board's top edge far enough to span the
  enclosure gap and fully mate with the User Settings Module's own flush-mounted female bottom
  Hub connector, per DEC-103. This board carries no bottom (female) connector pair of its own -
  it is always the last board in both local stacks (per DEC-088). Mating gap/tolerance:
  `design/Standards/Global_Routing_Spec.md §4.1a`.

---

## 1. J1 - Cypher Left Pair Template

> **Connector Definition Owner:** `Cypher/Board_Layout.md §4` (its own `J5`). Full 50-pin template
> defined there — this section only records this board's own local wiring so it cannot drift out
> of sync with the owning definition.

This board occupies no row of the shared template - it has no ENC module and no `BOARD_ROLE_ID`
strap of its own. Local wiring:

| Row / Pins | Wiring |
| :--- | :--- |
| Top row (`BOARD_ROLE_ID_IN[3:0]`, `ENC_DATA_IN[5:0]`, `ENC_ACTIVE_INPUT_N`) | Received, left NC - nothing below this board to relay to |
| Bottom row (`BOARD_ROLE_ID_OUT[3:0]`, `ENC_DATA_OUT[5:0]`, `ENC_ACTIVE_OUTPUT_N`) | Received, left NC - same as above |
| `5V_MAIN` | Received, left NC - no LED bank or other `5V_MAIN` consumer on this board |
| `3V3_ENIG` | Received, left NC - no active components remain on this board to bias |
| GND | Received, fully populated/continuous - not NC, maintains the signal-return path through this board even though it is the dead end of the chain |

> This board carries no bottom connector pair - it is always the last board in the local HID
> stack (per DEC-088), so nothing below it needs any of these signals relayed further.

---

## 2. J2 - USM Hub Connector Template

> **Connector Definition Owner:** `User_Settings_Module/Board_Layout.md §2` (its own `J2`). Full
> 50-pin template defined there — this section only records this board's own local wiring so it
> cannot drift out of sync with the owning definition.

This board mates USM's own bottom (`J2`, female) Hub connector, per DEC-103. Local wiring:

| Pins | Wiring |
| :--- | :--- |
| `I2C_SDA`/`I2C_SCL` | Received, left NC - no I2C device on this board |
| `TMS`/`TCK`/`CPLD_RESET_N` | Received, left NC - these broadcast JTAG lines are terminated on the User Settings Module itself (`R1`-`R3`), not on this board |
| `TDI`/`TDO` | Received, left NC - no JTAG TAP of its own; USM's own Hub Connector Template already leaves these NC on its `J2` side |
| `3V3_ENIG` | Received, left NC - no active components remain on this board to bias |
| GND | Received, fully populated/continuous - not NC, maintains the signal-return path through this board even though it is the dead end of the chain |

> This board carries no further connector beyond `J2` - it is always the last board in the local
> USM-hub stack (per DEC-088/DEC-103), so nothing below it needs any of these signals relayed
> further.

---

## Diagram Reference

See `design/Diagrams/cypher-system-layout.drawio` and renders in `design/Diagrams/renders/` for
the system-level layout showing the Cypher-Plugboard Board's position at the bottom of the local
Cypher-Input/Cypher-Output HID stack and the User Settings Module hub stack.
