# Cypher-Input Board V1.0 Pinout Reference

**Status:** Draft
**Project:** Enigma-NG
**Author:** Izzyonstage & GitHub Copilot
**Version:** v.0.1.0
**Associated Hardware Revision:** Rev A
**Last Updated:** 2026-09-17

> **Board_Layout.md is a visualisation-only document.** Design narrative belongs in
> `Design_Spec.md`.

---

## Orientation Convention

- **Top-left edge:** `J1`, Cypher-facing left-pair male connector.
- **Bottom-left edge:** `J2`, Cypher-facing left-pair female connector.
- **Right edge:** `J3`, USM-facing right-angle male connector.
- **ENC module mount:** `J4`-`J6`.

---

## 1. J1 / J2 - Cypher Left Pair

> **Connector Definition Owner:** `Cypher/Board_Layout.md §4` (its own `J5`). The full 50-pin
> template, column numbering, and row convention are defined there — this section only records
> this board's own local wiring so it cannot drift out of sync with the owning definition.

This board occupies the **top row** (the "Input" role) of the shared template. Local wiring:

| Row / Pins | Wiring |
| :--- | :--- |
| Top row | Locally consumed - this board's own `BOARD_ROLE_ID_IN[3:0]` strap, `ENC_DATA_IN[5:0]`, and `ENC_ACTIVE_INPUT_N`, generated/driven onto `J1`/`J2` for relay toward the Cypher Board |
| Bottom row | Straight-through relay only - this board does not locally consume the bottom row (`BOARD_ROLE_ID_OUT[3:0]`, `ENC_DATA_OUT[5:0]`, `ENC_ACTIVE_OUTPUT_N`); it passes through untouched whenever this board is not the one directly facing the Cypher Board |
| `5V_MAIN`, GND | Board power entry / return, both rows |

> **`ENC_ACTIVE_INPUT_N`/`ENC_ACTIVE_OUTPUT_N` must only ever originate from and terminate at the
> Cypher Board.** Whichever HID board is not the signal's origin relays it electrically untouched
> and must NOT tap, buffer, or locally consume it in transit - these signals are timing-sensitive
> against the Rotor/Stack encoder chain's propagation delay, so a board-local interception would
> desynchronise them from what Cypher expects. This board must never read `ENC_ACTIVE_OUTPUT_N`
> off its own bottom row for any local purpose, even when it is physically carrying that signal
> through to Cypher.

---

## 2. J3 - USM Right-Edge Connector

> **Connector Definition Owner:** `User_Settings_Module/Board_Layout.md` (its own `J3`/`J4` left
> connectors). The full 50-pin template is defined there — this section only records this board's
> own local wiring so it cannot drift out of sync with the owning definition.

This board occupies the **top row** (the "Input" role) of the shared template. Local wiring:

| Row / Pins | Wiring |
| :--- | :--- |
| Top row | Locally consumed - `TDI_INPUT`/`TDO_INPUT` to this board's own ENC module JTAG pins; `I2C2` (`I2C_SDA`/`I2C_SCL`) to `U4` |
| Bottom row | Not consumed - `TDI_OUTPUT`/`TDO_OUTPUT` belong to whichever board is in the Output role |
| Broadcast (both rows, tied) | `3V3_ENIG`, `CPLD_RESET_N`, `TMS`, `TCK` to the local ENC module; `RED_DRIVE_N`/`GREEN_DRIVE_N`/`BLUE_DRIVE_N`/`ILLUMINATION_DRIVE_N` to the local LED stage |

---

## 3. J4 - J6 - ENC Module Mount

`J4`-`J6` continue to follow `Encoder_Module/Board_Layout.md §1a-1c` for their own pin-1/signal
definitions (canonical, owned by that board). The table below records what is already known from
that definition, plus a **placeholder pending user sign-off** for the exact pin numbers this board
uses when routing each signal onward to `J1`-`J3` or local components — fill in real pin numbers
before schematic capture.

| ENC Module Signal (CPLD pin) | Routes to (this board) |
| :--- | :--- |
| *(example only)* CPLD pin 17 | *(example only)* `J2` pin 4 |
| `PB[0:63]` (plain-bits, via `J4`, ENC module's own `J1`) | Local only - all 64 positions reserved for cipher-path keyswitches; not routed onward to `J1`-`J3` |
| `CB[0:5]` (cypher-bits, via `J5`, ENC module's own `J2`) | Feeds `J1`/`J2` `ENC_DATA_IN[5:0]` - exact pin numbers TBD |
| JTAG `TDI`/`TDO`/`TMS`/`TCK`/`CPLD_RESET_N` (via `J5`, ENC module's own `J2`) | Feeds `J3` `TDI_INPUT`/`TDO_INPUT`/`TMS`/`TCK`/`CPLD_RESET_N` - exact pin numbers TBD |
| `ENC_ACTIVE_N` (via `J5`, ENC module's own `J2`) | Expected to feed `J1`/`J2` `ENC_ACTIVE_INPUT_N` - **open item:** the ENC module currently defines only one role-dependent `ENC_ACTIVE_N` pin (see `Encoder_Module/Board_Layout.md §4.2`), not separate input/output signals; see `.copilot/todos/encoder-module-pin-agnostic-redesign-review.md` before finalising this row |
| `3V3_ENIG` (via `J6`, ENC module's own `J3`) | Local board power entry |

> **Note:** this placeholder does not yet reflect final schematic-level pin assignments. Update
> once the user has directed the exact routing, matching the level of detail already captured for
> `J1`/`J2`/`J3` above.
