# Cypher-Output Board V1.0 Pinout Reference

**Status:** Draft
**Project:** Enigma-NG
**Author:** Izzyonstage & GitHub Copilot
**Version:** v.0.1.0
**Associated Hardware Revision:** Rev A
**Last Updated:** 2026-10-01

> **Board_Layout.md is a visualisation-only document.** Design narrative, specifications, and
> component rationale belong in `Design_Spec.md`. This file contains connector pinout references
> and board orientation notes only.

---

## Orientation Convention

- **Top face (L1):** LED bank (D1-D26, D1-D40, or D1-D12, depending on variant) and, on the
  64-Character variant only, SW1 (custom-support switch). **Neither is part of the JLCPCB PCBA
  order** - both are hand-soldered by the user after the bare-assembled board is delivered,
  keeping JLCPCB's automated SMT assembly single-sided (see `Design_Spec.md §2` Architecture). A
  keyless keepout zone occupies the region corresponding to a number-pad area on a conventional
  keyboard - this board has no local colour/illumination
  generation of its own (see `Design_Spec.md §1` Colour / Brightness Reception), so this zone
  carries no components on the 26-Char Classic and 10-Numeric variants, and only SW1 on the
  64-Character variant.
- **Rear face (L4):** fully populated by JLCPCB's single-sided SMT PCBA pass. ENC module mount
  (J4-J6, keyed and polarity-free per Hirose DF40C asymmetric standoff pattern) - positioned
  directly beneath the keepout zone, in the same keyless region; Cypher Board interconnect
  (J1/J2); User Settings Module interconnect (J3); LED bank current-limit resistors; LED
  colour-bank P-MOSFET switches (U1, U2, U3) and shared cathode-return illumination switch (U4);
  per-position LED select MOSFETs (Q1-Q26, Q1-Q40, or Q1-Q12, depending on variant); entry
  decoupling banks; local decoupling; Data Plate.
- **J1 (top, male):** Cypher Board interconnect, mounted protruding past the board's top edge
  far enough to span the enclosure gap and fully mate with the neighbouring board's flush-mounted
  female connector. Mates upward, toward whichever is physically above this board (the Cypher
  Board directly, or Cypher-Input if this board is not closest to the Cypher Board).
- **J2 (bottom, female):** Cypher Board interconnect, mounted flush with the board's bottom edge
  so the connector's socket opening sits flush with the enclosure lid's edge once cased, forming
  a clean opening for the next board's protruding male pins to enter. Mates downward, toward
  Cypher-Input or the Cypher-Plugboard. Mating gap/tolerance:
  `design/Standards/Global_Routing_Spec.md §4.1a`.
- **J3 (right edge, male):** User Settings Module interconnect - mates whichever of USM's two
  left-edge connectors is wired to this board's physical position.

---

## 1. J4 - ENC Module Mount, Connector A (DF40C-90DS-0.4V(51))

> **Connector Definition Owner:** `Encoder_Module/Board_Layout.md §1a`. The pin table below is
> reproduced here for layout reference - identical to Cypher-Input's own J4 table, per
> `Encoder_Module/Board_Layout.md §1a-1c`. In case of conflict, the Encoder Module definition is
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

> LED colour and illumination are received entirely from the User Settings Module on `J3` and
> never appear on `J4`/`J5`/`J6` - see `Design_Spec.md §1` Colour / Brightness Reception.

---

## 2. J5 - ENC Module Mount, Connector B (DF40C-24DS-0.4V(51))

> **Connector Definition Owner:** `Encoder_Module/Board_Layout.md §1b`. The pin table below is
> reproduced here for layout reference - identical to Cypher-Input's own J5 table. In case of
> conflict, the Encoder Module definition is authoritative. This board's connector mates with the
> ENC module's DF40C-24DP plug.

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
| C12 | GND | ENC_ACTIVE_N (received from `J1`/`J2` as `ENC_ACTIVE_OUTPUT_N`) |

> **This board's usage:** all 12 signals active. `ENC_ACTIVE_N` here is the ENC module's **input**
> (lightboard/decode role - see `Design_Spec.md §3`), sourced from `J1`/`J2`'s own
> `ENC_ACTIVE_OUTPUT_N` - the opposite direction to Cypher-Input's own `J5`, where this signal is
> an output.

---

## 3. J6 - ENC Module Mount, Connector C (DF40C-10DS-0.4V(51))

> **Connector Definition Owner:** `Encoder_Module/Board_Layout.md §1c`. The pin table below is
> reproduced here for layout reference - identical to Cypher-Input's own J6 table. In case of
> conflict, the Encoder Module definition is authoritative. This board's connector mates with the
> ENC module's DF40C-10DP plug.

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
| `PB[0:63]` (plain-bits, via `J4`, ENC module's own `J1`) | Local only - all 64 positions reserved for one-hot lens-position select outputs; not routed onward to `J1`-`J3` |
| `CB[0:5]` (cypher-bits, via `J5`, ENC module's own `J2`) | Feeds `J1`/`J2` `ENC_DATA_OUT[5:0]` - exact pin numbers TBD |
| JTAG `TDI`/`TDO`/`TMS`/`TCK`/`CPLD_RESET_N` (via `J5`, ENC module's own `J2`) | Feeds `J3` `TDI_OUTPUT`/`TDO_OUTPUT`/`TMS`/`TCK`/`CPLD_RESET_N` - exact pin numbers TBD |
| `ENC_ACTIVE_N` (via `J5`, ENC module's own `J2`) | Sourced from `J1`/`J2` `ENC_ACTIVE_OUTPUT_N` - **open item:** the ENC module currently defines only one role-dependent `ENC_ACTIVE_N` pin (see `Encoder_Module/Board_Layout.md §4.2`), not separate input/output signals; see `.copilot/todos/encoder-module-pin-agnostic-redesign-review.md` before finalising this row |
| `3V3_ENIG` (via `J6`, ENC module's own `J3`) | Local board power entry |

---

## 4. J1 / J2 - Cypher Left Pair Template

> **Connector Definition Owner:** `Cypher/Board_Layout.md §4` (its own `J5`). Full 50-pin template
> defined there — this section only records this board's own local wiring so it cannot drift out
> of sync with the owning definition.

This board occupies the **bottom row** (the "Output" role) of the shared template. Local wiring:

| Row / Pins | Wiring |
| :--- | :--- |
| Bottom row | Locally consumed - this board's own `BOARD_ROLE_ID_OUT[3:0]` strap and `ENC_DATA_OUT[5:0]`, generated/driven onto `J1`/`J2` for relay toward the Cypher Board; `ENC_ACTIVE_OUTPUT_N` is locally consumed here, fed into this board's own ENC module `ENC_ACTIVE_N` input |
| Top row | Straight-through relay only - this board does not locally consume the top row (`BOARD_ROLE_ID_IN[3:0]`, `ENC_DATA_IN[5:0]`, `ENC_ACTIVE_INPUT_N`); relayed untouched only when this board is the one directly facing Cypher-Input (bridging the signal on to whichever board sits above it); when this board instead faces the Cypher Board directly, there is nothing further to relay upward beyond this board |
| `5V_MAIN`, GND | Board power entry / return, both rows; `5V_MAIN` also feeds this board's own LED colour-bank P-MOSFETs (U1-U3, see `Design_Spec.md §4`) |

> **`ENC_ACTIVE_INPUT_N`/`ENC_ACTIVE_OUTPUT_N` must only ever originate from and terminate at the
> Cypher Board.** Whichever HID board is not the signal's origin relays it electrically untouched
> and must NOT tap, buffer, or locally consume it in transit - these signals are timing-sensitive
> against the Rotor/Stack encoder chain's propagation delay, so a board-local interception would
> desynchronise them from what Cypher expects. This board's own local consumption of
> `ENC_ACTIVE_OUTPUT_N` off its own bottom row is legitimate - this board is that signal's
> genuine, intended destination (generated by Cypher specifically for Cypher-Output, after
> Cypher's own propagation-delay compensation), not an interception of a signal meant for
> another board. This board must never read `ENC_ACTIVE_INPUT_N` off its own top row for any
> local purpose, even when it is physically carrying that signal through toward Cypher-Input.
>
> **`BOARD_ROLE_ID_OUT[3:0]` encoding (per `Cypher/Board_Layout.md §4`, capability bitmask - see
> `Design_Spec.md §3a`):** bit0 = Characters, bit1 = Numbers, bit2 = Special, bit3 = Custom.
>
> | ID[3] | ID[2] | ID[1] | ID[0] | Value | Variant |
> | :---: | :---: | :---: | :---: | :---: | :--- |
> | GND | GND | GND | 3V3 | 0b0001 | 26-Char Classic |
> | GND | GND | 3V3 | GND | 0b0010 | 10-Numeric |
> | GND | 3V3 | 3V3 | 3V3 | 0b0111 | 64-Character (default) |
> | 3V3 | 3V3 | 3V3 | 3V3 | 0b1111 | 64-Character (custom-support enabled via SW1) |
>
> This board's own `BOARD_ROLE_ID_OUT[3:0]` strap is hardwired per the above table according to
> which variant (26-Char Classic, 64-Character, or 10-Numeric) is populated; on the 64-Character
> variant only, bit3 is user-switchable via SW1 rather than a fixed strap - see
> `Cypher_Output_64_Char_Design.md §4`. `BOARD_ROLE_ID_IN[3:0]` is not generated on this board - it
> is a passthrough of whichever Cypher-Input board's own strap is installed.

---

## 5. J3 - USM Right-Edge Connector

> **Connector Definition Owner:** `User_Settings_Module/Board_Layout.md` (its own left
> connectors). Full 50-pin template defined there — this section only records this board's own
> local wiring so it cannot drift out of sync with the owning definition.

This board occupies the **bottom row** (the "Output" role) of the shared template. Local wiring:

| Row / Pins | Wiring |
| :--- | :--- |
| Bottom row | Locally consumed - `TDI_OUTPUT`/`TDO_OUTPUT` to this board's own ENC module JTAG pins |
| Top row | Not consumed - `TDI_INPUT`/`TDO_INPUT` belong to whichever board is in the Input role; `I2C_SDA`/`I2C_SCL` are NC on this board - no I2C device on this board, see `Design_Spec.md §1` "No I2C GPIO expander" note |
| Broadcast (both rows, tied) | `3V3_ENIG`, `CPLD_RESET_N`, `TMS`, `TCK` to the local ENC module; all four colour styles' `RED_DRIVE_{1,2,3,4}_N`/`GREEN_DRIVE_{1,2,3,4}_N`/`BLUE_DRIVE_{1,2,3,4}_N`/`ILLUMINATION_DRIVE_{1,2,3,4}_N` to the local LED colour-bank/illumination switching stage (U1-U4) - which style(s) drive the LED bank at a given moment is an open item, see `.copilot/todos/cypher-input-led-independent-rgb-pwm-review.md` |

---

## Diagram Reference

See `design/Diagrams/cypher-system-layout.drawio` and renders in `design/Diagrams/renders/` for
the system-level layout diagram once the Cypher-Output Board is added to that diagram set.
