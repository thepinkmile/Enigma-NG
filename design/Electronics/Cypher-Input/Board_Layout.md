# Cypher-Input Board V1.0 Pinout Reference

**Status:** Draft
**Project:** Enigma-NG
**Author:** Izzyonstage & GitHub Copilot
**Version:** v.0.1.0
**Associated Hardware Revision:** Rev A
**Last Updated:** 2026-09-21

> **Board_Layout.md is a visualisation-only document.** Design narrative, specifications, and
> component rationale belong in `Design_Spec.md`. This file contains connector pinout references
> and board orientation notes only.

---

## Orientation Convention

- **Top face (L1):** LED bank (D1-D26, D1-D42, or D1-D12, depending on variant) only. **Not part
  of the JLCPCB PCBA order** - hand-soldered by the user after the bare-assembled board is
  delivered, keeping JLCPCB's automated SMT assembly single-sided (see `Design_Spec.md §2`
  Architecture). Keyswitches occupy the rest of this face (Cherry MX2A-71NB switches plug down
  through the board into rear-mounted Kailh hot-swap sockets - see Rear face below).
- **Rear face (L4):** fully populated by JLCPCB's single-sided SMT PCBA pass. ENC module mount
  (J4-J6, keyed and polarity-free per Hirose DF40C asymmetric standoff pattern) - positioned in
  the keyless region that corresponds to a number-pad area on a conventional keyboard, off to the
  side of the main keyswitch cluster; Cypher Board interconnect (J1/J2); User Settings Module
  interconnect (J3); I2C GPIO expander (U4); LED bank current-limit resistors; LED bank P-MOSFET
  switches (U5, U6, U7) and shared cathode-return illumination switch (U8); Kailh hot-swap
  sockets (SW1-SW26, SW1-SW42, or SW1-SW12, depending on variant); entry decoupling banks; local
  decoupling; Data Plate.
- **J1 (top, male):** Cypher Board interconnect, mounted flush with the board's top edge so the
  connector face sits flush with the enclosure lid's edge once cased. Mates upward, toward
  whichever is physically above this board (the Cypher Board directly, or the other HID board if
  this board is not closest to the Cypher Board).
- **J2 (bottom, female):** Cypher Board interconnect, mounted protruding past the board's bottom
  edge far enough to span the enclosure gap and fully mate with the neighbouring board's
  flush-mounted male connector. Mates downward, toward the other HID board or Cypher-Plugboard.
- **J3 (right edge, male):** User Settings Module interconnect - mates whichever of USM's two
  left-edge connectors is wired to this board's physical position.

---

## 1. J4 - ENC Module Mount, Connector A (DF40C-90DS-0.4V(51))

> **Connector Definition Owner:** `Encoder_Module/Board_Layout.md §1a`. The pin table below is
> reproduced here for layout reference. In case of conflict, the Encoder Module definition is
> authoritative. This board's connector mates with the ENC module's DF40C-90DP plug.

2 rows x 45 positions = 90 total pins. 64 plain-bit signal pins (PB) + 26 GND pins, zig-zag
distributed between rows (Bresenham-spread, max signal-only gap = 1 column between any two GND
columns). PB\[0\] is leftmost (LSB convention).

| Col | Row A | Row B |
| :--- | :--- | :--- |
| C01 | PB[0] | PB[1] |
| C02 | GND | PB[2] |
| C03 | PB[3] | GND |
| C04 | PB[4] | PB[5] |
| C05 | GND | PB[6] |
| C06 | PB[7] | PB[8] |
| C07 | PB[9] | GND |
| C08 | PB[10] | PB[11] |
| C09 | GND | PB[12] |
| C10 | PB[13] | GND |
| C11 | PB[14] | PB[15] |
| C12 | GND | PB[16] |
| C13 | PB[17] | PB[18] |
| C14 | PB[19] | GND |
| C15 | PB[20] | PB[21] |
| C16 | GND | PB[22] |
| C17 | PB[23] | GND |
| C18 | PB[24] | PB[25] |
| C19 | GND | PB[26] |
| C20 | PB[27] | PB[28] |
| C21 | PB[29] | GND |
| C22 | GND | PB[30] |
| C23 | PB[31] | PB[32] |
| C24 | PB[33] | GND |
| C25 | PB[34] | PB[35] |
| C26 | GND | PB[36] |
| C27 | PB[37] | PB[38] |
| C28 | PB[39] | GND |
| C29 | GND | PB[40] |
| C30 | PB[41] | PB[42] |
| C31 | PB[43] | GND |
| C32 | PB[44] | PB[45] |
| C33 | GND | PB[46] |
| C34 | PB[47] | PB[48] |
| C35 | PB[49] | GND |
| C36 | GND | PB[50] |
| C37 | PB[51] | PB[52] |
| C38 | PB[53] | GND |
| C39 | PB[54] | PB[55] |
| C40 | GND | PB[56] |
| C41 | PB[57] | PB[58] |
| C42 | PB[59] | GND |
| C43 | GND | PB[60] |
| C44 | PB[61] | PB[62] |
| C45 | PB[63] | GND |

> **This board's PB[] usage:** per-variant `plain-bits` allocation is defined in each variant's own
> design file (all share this pin map, using only as many PB[] positions as their key count
> requires). **All 64 PB[] positions are reserved exclusively for cipher-path keyswitch inputs on
> every variant - LED colour/brightness values are sourced entirely from the User Settings Module
> and never use any `plain-bits` position**:
>
> - **64-Character variant:** PB[0:39] = 40 cipher-path keyswitch inputs; PB[40:63]
>   unused/spare - see `Cypher_Input_64_Char_Design.md §3`.
> - **26-Char Classic variant:** PB[0:25] = 26 letter keys; PB[26:63] unused/spare - see
>   `Cypher_Input_26_Char_Design.md §3`.
> - **10-Numeric variant:** PB[0:9] = 10 digit keys; PB[10:63] unused/spare - see
>   `Cypher_Input_10_Numeric_Design.md §3`.

---

## 2. J5 - ENC Module Mount, Connector B (DF40C-24DS-0.4V(51))

> **Connector Definition Owner:** `Encoder_Module/Board_Layout.md §1b`. The pin table below is
> reproduced here for layout reference. In case of conflict, the Encoder Module definition is
> authoritative. This board's connector mates with the ENC module's DF40C-24DP plug.

2 rows x 12 positions = 24 total pins. 12 signal pins + 12 GND pins, full zig-zag (every signal
flanked by GND at adjacent columns). Signal order left-to-right: CB[0:5], then JTAG (TCK, RST_N,
TMS, TDI, TDO), then `ENC_ACTIVE_N`.

| Col | Row A | Row B |
| :--- | :--- | :--- |
| C01 | CB[0] | GND |
| C02 | GND | CB[1] |
| C03 | CB[2] | GND |
| C04 | GND | CB[3] |
| C05 | CB[4] | GND |
| C06 | GND | CB[5] |
| C07 | TCK | GND |
| C08 | GND | RST_N (`CPLD_RESET_N`) |
| C09 | TMS | GND |
| C10 | GND | TDI |
| C11 | TDO | GND |
| C12 | GND | ENC_ACTIVE_N (`ENC_ACTIVE_INPUT_N` toward J1/J2) |

> **This board's usage:** all 12 signals active. `ENC_ACTIVE_N` here is the ENC module's output
> (keyboard/encoder role - see `Design_Spec.md §3`), forwarded to J1/J2 as `ENC_ACTIVE_INPUT_N`.

---

## 3. J6 - ENC Module Mount, Connector C (DF40C-10DS-0.4V(51))

> **Connector Definition Owner:** `Encoder_Module/Board_Layout.md §1c`. The pin table below is
> reproduced here for layout reference. In case of conflict, the Encoder Module definition is
> authoritative. This board's connector mates with the ENC module's DF40C-10DP plug.

2 rows x 5 positions = 10 total pins. Power only, no zig-zag (solid rows). Row A = 3V3_ENIG,
Row B = GND.

| Col | Row A | Row B |
| :--- | :--- | :--- |
| C01 | 3V3_ENIG | GND |
| C02 | 3V3_ENIG | GND |
| C03 | 3V3_ENIG | GND |
| C04 | 3V3_ENIG | GND |
| C05 | 3V3_ENIG | GND |

> **Placeholder pending user sign-off:** the table below records what routes onward from each ENC
> module signal to this board's own `J1`-`J3` connectors or local components - fill in real pin
> numbers before schematic capture.

| ENC Module Signal (CPLD pin) | Routes to (this board) |
| :--- | :--- |
| *(example only)* CPLD pin 17 | *(example only)* `J2` pin 4 |
| `PB[0:63]` (plain-bits, via `J4`, ENC module's own `J1`) | Local only - all 64 positions reserved for cipher-path keyswitches; not routed onward to `J1`-`J3` |
| `CB[0:5]` (cypher-bits, via `J5`, ENC module's own `J2`) | Feeds `J1`/`J2` `ENC_DATA_IN[5:0]` - exact pin numbers TBD |
| JTAG `TDI`/`TDO`/`TMS`/`TCK`/`CPLD_RESET_N` (via `J5`, ENC module's own `J2`) | Feeds `J3` `TDI_INPUT`/`TDO_INPUT`/`TMS`/`TCK`/`CPLD_RESET_N` - exact pin numbers TBD |
| `ENC_ACTIVE_N` (via `J5`, ENC module's own `J2`) | Expected to feed `J1`/`J2` `ENC_ACTIVE_INPUT_N` - **open item:** the ENC module currently defines only one role-dependent `ENC_ACTIVE_N` pin (see `Encoder_Module/Board_Layout.md §4.2`), not separate input/output signals; see `.copilot/todos/encoder-module-pin-agnostic-redesign-review.md` before finalising this row |
| `3V3_ENIG` (via `J6`, ENC module's own `J3`) | Local board power entry |

---

## 4. J1 / J2 - Cypher Left Pair Template

> **Connector Definition Owner:** `Cypher/Board_Layout.md §4` (its own `J5`). Full 50-pin template
> defined there — this section only records this board's own local wiring so it cannot drift out
> of sync with the owning definition.

This board occupies the **top row** (the "Input" role) of the shared template. Local wiring:

| Row / Pins | Wiring |
| :--- | :--- |
| Top row | Locally consumed - this board's own `BOARD_ROLE_ID_IN[3:0]` strap, `ENC_DATA_IN[5:0]`, and `ENC_ACTIVE_INPUT_N`, generated/driven onto `J1`/`J2` for relay toward the Cypher Board |
| Bottom row | Straight-through relay only - this board does not locally consume the bottom row (`BOARD_ROLE_ID_OUT[3:0]`, `ENC_DATA_OUT[5:0]`, `ENC_ACTIVE_OUTPUT_N`); relayed untouched only when this board is the one directly facing the Cypher Board (bridging the signal on to whichever board sits beneath it); when this board instead faces Cypher-Plugboard (the dead end of the local stack), there is nothing to relay to |
| `5V_MAIN`, GND | Board power entry / return, both rows |

> **`ENC_ACTIVE_INPUT_N`/`ENC_ACTIVE_OUTPUT_N` must only ever originate from and terminate at the
> Cypher Board.** Whichever HID board is not the signal's origin relays it electrically untouched
> and must NOT tap, buffer, or locally consume it in transit - these signals are timing-sensitive
> against the Rotor/Stack encoder chain's propagation delay, so a board-local interception would
> desynchronise them from what Cypher expects. This board must never read `ENC_ACTIVE_OUTPUT_N`
> off its own bottom row for any local purpose, even when it is physically carrying that signal
> through to Cypher.
>
> **`BOARD_ROLE_ID_IN[3:0]` encoding (per `Cypher/Board_Layout.md §4`, capability bitmask - see
> `Design_Spec.md §3a`):** bit0 = Characters, bit1 = Numbers, bit2 = Special, bit3 = Custom (never
> populated by a Cypher-Input board).
>
> | ID[3] | ID[2] | ID[1] | ID[0] | Value | Variant |
> | :---: | :---: | :---: | :---: | :---: | :--- |
> | GND | GND | GND | 3V3 | 0b0001 | 26-Char Classic |
> | GND | GND | 3V3 | GND | 0b0010 | 10-Numeric |
> | GND | 3V3 | 3V3 | 3V3 | 0b0111 | 64-Character |

---

## 5. J3 - USM Right-Edge Connector

> **Connector Definition Owner:** `User_Settings_Module/Board_Layout.md` (its own `J3`/`J4` left
> connectors). Full 50-pin template defined there — this section only records this board's own
> local wiring so it cannot drift out of sync with the owning definition.

This board occupies the **top row** (the "Input" role) of the shared template. Local wiring:

| Row / Pins | Wiring |
| :--- | :--- |
| Top row | Locally consumed - `TDI_INPUT`/`TDO_INPUT` to this board's own ENC module JTAG pins; `I2C2` (`I2C_SDA`/`I2C_SCL`) to `U4` |
| Bottom row | Not consumed - `TDI_OUTPUT`/`TDO_OUTPUT` belong to whichever board is in the Output role |
| Broadcast (both rows, tied) | `3V3_ENIG`, `CPLD_RESET_N`, `TMS`, `TCK` to the local ENC module; all four colour styles' `RED_DRIVE_{1,2,3,4}_N`/`GREEN_DRIVE_{1,2,3,4}_N`/`BLUE_DRIVE_{1,2,3,4}_N`/`ILLUMINATION_DRIVE_{1,2,3,4}_N` to the local LED stage - which style(s) drive the LED bank at a given moment is an open item, see `.copilot/todos/cypher-input-led-independent-rgb-pwm-review.md` |

---

## Diagram Reference

See `design/Diagrams/cypher-system-layout.drawio` and renders in `design/Diagrams/renders/` for
the system-level layout diagram once the Cypher-Input Board is added to that diagram set.
