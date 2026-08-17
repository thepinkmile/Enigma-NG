# Cypher-Output Board V1.0 Pinout Reference

**Status:** Draft
**Project:** Enigma-NG
**Author:** Izzyonstage & GitHub Copilot
**Version:** v.0.1.0
**Associated Hardware Revision:** Rev A
**Last Updated:** 2026-08-17

> **Board_Layout.md is a visualisation-only document.** Design narrative, specifications, and
> component rationale belong in `Design_Spec.md`. This file contains connector pinout references
> and board orientation notes only.

---

## Orientation Convention

- **Top face (L1):** LED bank (D1-D26, D1-D42, or D1-D12, depending on variant) and, on the
  64-Character variant only, SW1 (custom-support switch). **Neither is part of the JLCPCB PCBA
  order** - both are hand-soldered by the user after the bare-assembled board is delivered,
  keeping JLCPCB's automated SMT assembly single-sided (see `Design_Spec.md §2` Architecture). A
  keyless keepout zone occupies the region corresponding to a number-pad area on a conventional
  keyboard, mirroring Cypher-Input's RV1 placement - this board has no local brightness control
  of its own (see `Design_Spec.md §1` Colour / Brightness Reception), so this zone carries no
  components on the 26-Char Classic and 10-Numeric variants, and only SW1 on the 64-Character
  variant.
- **Rear face (L4):** fully populated by JLCPCB's single-sided SMT PCBA pass. ENC module mount
  (J1-J3, keyed and polarity-free per Hirose DF40C asymmetric standoff pattern) - positioned
  directly beneath the keepout zone, in the same keyless region; Cypher Board interconnect
  (J4-J7); LED bank current-limit resistors; per-position LED select MOSFETs (Q1-Q26, Q1-Q42, or
  Q1-Q12, depending on variant); 3V3_ENIG entry decoupling bank; local decoupling; Data Plate.
- **J4 (top-left, male) and J5 (top-right, male):** Cypher Board interconnect, mounted flush
  with the board's top edge so the connector face sits flush with the enclosure lid's edge once
  cased. Mates upward, toward whichever is physically above this board (the Cypher Board
  directly, or the other HID board if this board is not closest to the Cypher Board).
- **J6 (bottom-left, female) and J7 (bottom-right, female):** Cypher Board interconnect, mounted
  protruding past the board's bottom edge far enough to span the enclosure gap and fully mate
  with the neighbouring board's flush-mounted male connector. Mates downward, toward the other
  HID board or a future Plugboard board.

---

## 1. J1 - ENC Module Mount, Connector A (DF40C-90DS-0.4V(51))

> **Connector Definition Owner:** `Encoder_Module/Board_Layout.md §1a`. The pin table below is
> reproduced here for layout reference - identical to Cypher-Input's own J1 table, per
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

> **This board's PB[] usage:** per-variant `plain-bits` allocation is defined in each variant's own
> design file (all share this pin map, using only as many PB[] positions as their lens count
> requires). **All 64 PB[] positions are reserved exclusively for one-hot lens-position select
> outputs on every variant** - this board's ENC module is programmed in the `LBD_DEC` role, so
> each PB[n] line is driven (not sensed) by the CPLD, one-hot, gating that position's select
> MOSFET (`Design_Spec.md §4`):
>
> - **64-Character variant:** PB[0:39] = 40 lens-position select outputs, position-for-position
>   matching Cypher-Input's own 64-Character `plain-bits` allocation; PB[40:63] unused/spare -
>   see `Cypher_Output_64_Char_Design.md §3`.
> - **26-Char Classic variant:** PB[0:25] = 26 lens-position select outputs; PB[26:63]
>   unused/spare - see `Cypher_Output_26_Char_Design.md §3`.
> - **10-Numeric variant:** PB[0:9] = 10 lens-position select outputs; PB[10:63] unused/spare -
>   see `Cypher_Output_10_Numeric_Design.md §3`.
>
> LED colour and brightness are received entirely as a broadcast from Cypher-Input on `J4`/`J6`
> and never appear on J1/J2/J3 - see `Design_Spec.md §1` Colour / Brightness Reception.

---

## 2. J2 - ENC Module Mount, Connector B (DF40C-24DS-0.4V(51))

> **Connector Definition Owner:** `Encoder_Module/Board_Layout.md §1b`. The pin table below is
> reproduced here for layout reference - identical to Cypher-Input's own J2 table. In case of
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
| C12 | GND | ENC_ACTIVE_N (received from J5/J7 as `ENC_ACTIVE_INPUT_N`) |

> **This board's usage:** all 12 signals active. `ENC_ACTIVE_N` here is the ENC module's **input**
> (lightboard/decode role - see `Design_Spec.md §3`), received from J5/J7's own
> `ENC_ACTIVE_INPUT_N` - the opposite direction to Cypher-Input's own J2, where this signal is an
> output.

---

## 3. J3 - ENC Module Mount, Connector C (DF40C-10DS-0.4V(51))

> **Connector Definition Owner:** `Encoder_Module/Board_Layout.md §1c`. The pin table below is
> reproduced here for layout reference - identical to Cypher-Input's own J3 table. In case of
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

---

## 4. J4-J7 - Cypher Board Interconnect (Samtec QTS/QSS-025 family)

> **Connector Definition Owner:** Cypher Board `Board_Layout.md §4` (pin-level template);
> physical connector placement/orientation owned by this board.
>
> This board carries **4 connectors**, inset from the left/right board edges for mechanical
> stability: 2 male at the top edge (mate upward, toward whichever is physically above - the
> Cypher Board directly, or the other HID board if this board is not closest to Cypher Board),
> 2 female at the bottom edge (mate downward, toward the other HID board or a future Plugboard
> board). This lets Cypher-Input and Cypher-Output attach to the Cypher Board in either order.

| RefDes | Position | Gender | MPN | Content |
| :--- | :--- | :--- | :--- | :--- |
| J4 | Top-Left (TL) | Male, right-angle | QTS-025-01-L-D-RA-P | 3V3_ENIG, 5V_MAIN, GND, LED colour/brightness reception, `BOARD_ROLE_ID_OUT[3:0]` |
| J5 | Top-Right (TR) | Male, right-angle | QTS-025-01-L-D-RA-P | GND (center bar) + JTAG chain-through signals |
| J6 | Bottom-Left (BL) | Female, right-angle | QSS-025-01-L-D-RA-K | 3V3_ENIG, 5V_MAIN, GND, LED colour/brightness reception, `BOARD_ROLE_ID_OUT[3:0]` |
| J7 | Bottom-Right (BR) | Female, right-angle | QSS-025-01-L-D-RA-K | GND (center bar) + JTAG chain-through signals |

J4/J6 (left side) mate with whichever neighbour's opposite-gender left connector. This board
receives 4 LED-related signals on J4/J6: `RED_DRIVE_N`, `GREEN_DRIVE_N`, `BLUE_DRIVE_N` and
`BRIGHTNESS_PWM_EN` - generated by whichever Cypher-Input board is installed, consumed by this
board's own per-position LED select circuit (`Design_Spec.md §4`); this board never drives these
signals. This board's own `BOARD_ROLE_ID_OUT[3:0]` variant-ID strap is also carried on J4/J6 -
see the "J4 / J6 - Full Pin Map" section below for the concrete pin numbers. J5/J7
(right side) share the Cypher Board's board-agnostic HID Interconnect template
(`Cypher/Board_Layout.md §4`) - pin function is fixed by position, but each board wires it
internally per the table below.

### J4 / J6 - Full Pin Map (shared template, per `Cypher/Board_Layout.md §4`'s `J5`)

| Top Row Signal | Top Row Pin# | Bottom Row Pin# | Bottom Row Signal |
| :--- | :---: | :---: | :--- |
| **3V3_ENIG** | 1 | 2 | **3V3_ENIG** |
| **3V3_ENIG** | 3 | 4 | **3V3_ENIG** |
| **5V_MAIN** | 5 | 6 | **5V_MAIN** |
| **5V_MAIN** | 7 | 8 | **5V_MAIN** |
| GND | 9 | 10 | GND |
| GND | 11 | 12 | GND |
| GND | 13 | 14 | **RED_DRIVE_N** |
| GND | 15 | 16 | **GREEN_DRIVE_N** |
| **BOARD_ROLE_ID_IN[0]** | 17 | 18 | GND |
| **BOARD_ROLE_ID_IN[1]** | 19 | 20 | GND |
| **BOARD_ROLE_ID_IN[2]** | 21 | 22 | GND |
| **BOARD_ROLE_ID_IN[3]** | 23 | 24 | GND |
| GND (bar) | 25 | 26 | GND (bar) |
| GND | 27 | 28 | **BOARD_ROLE_ID_OUT[3]** |
| GND | 29 | 30 | **BOARD_ROLE_ID_OUT[2]** |
| GND | 31 | 32 | **BOARD_ROLE_ID_OUT[1]** |
| GND | 33 | 34 | **BOARD_ROLE_ID_OUT[0]** |
| **BRIGHTNESS_PWM_EN** | 35 | 36 | GND |
| **BLUE_DRIVE_N** | 37 | 38 | GND |
| GND | 39 | 40 | GND |
| GND | 41 | 42 | GND |
| **5V_MAIN** | 43 | 44 | **5V_MAIN** |
| **5V_MAIN** | 45 | 46 | **5V_MAIN** |
| **3V3_ENIG** | 47 | 48 | **3V3_ENIG** |
| **3V3_ENIG** | 49 | 50 | **3V3_ENIG** |

### This board's wiring at J4 / J6

| Pin(s) | Wiring |
| :--- | :--- |
| 1-4 - `3V3_ENIG`, 9-12 - GND (J4 & J6, tied) | Board power entry/return |
| 5-8 - `5V_MAIN` (J4 & J6, tied) | Passthrough only - not consumed by this board's own circuitry (see `Design_Spec.md §1` Colour / Brightness Reception) |
| 14/16 - `RED_DRIVE_N`/`GREEN_DRIVE_N` (bottom row, J4 & J6); 35/37 - `BRIGHTNESS_PWM_EN`/`BLUE_DRIVE_N` (top row, J4 & J6) | Received from whichever Cypher-Input board is installed → this board's own per-position select MOSFET gates (`Design_Spec.md §4`) - this board does not drive these pins |
| 17/19/21/23 - `BOARD_ROLE_ID_IN[3:0]` top row (J4 <-> J6 passthrough) | Direct passthrough wire (this board's own internal trace bridging J4's top-row pin to J6's top-row pin) - relays whichever Cypher-Input board's own ID code is installed through this board when this board is not the one directly facing Cypher-Input, same convention as `ENC_DATA` at J5/J7 |
| 28/30/32/34 - `BOARD_ROLE_ID_OUT[3:0]` bottom row (J4 & J6, tied together) | Hardwired 3V3_ENIG/GND strap identifying this board's own variant (Classic/64-Character/10-Numeric, or custom-support state on the 64-Character variant only - see `Cypher_Output_64_Char_Design.md §4`); driven onto the bottom-row pin of both J4 and J6 - encoding per table below |

> **`BOARD_ROLE_ID_IN[3:0]`/`BOARD_ROLE_ID_OUT[3:0]` encoding (per `Cypher/Board_Layout.md §4`,
> capability bitmask - see `Design_Spec.md §3a`):** bit0 = Characters, bit1 = Numbers, bit2 =
> Special, bit3 = Custom.
>
> | ID[3] | ID[2] | ID[1] | ID[0] | Value | Variant |
> | :---: | :---: | :---: | :---: | :---: | :--- |
> | GND | GND | GND | 3V3 | 0b0001 | 26-Char Classic |
> | GND | GND | 3V3 | GND | 0b0010 | 10-Numeric |
> | GND | 3V3 | 3V3 | 3V3 | 0b0111 | 64-Character (default) |
> | 3V3 | 3V3 | 3V3 | 3V3 | 0b1111 | 64-Character (custom-support enabled via SW1) |
>
> This board's own `BOARD_ROLE_ID_OUT[3:0]` strap (pins 28/30/32/34) is hardwired per the above
> table according to which variant (26-Char Classic, 64-Character, or 10-Numeric) is populated;
> on the 64-Character variant only, bit3 (pin 28) is user-switchable via SW1 rather than a fixed
> strap - see `Cypher_Output_64_Char_Design.md §4`. `BOARD_ROLE_ID_IN[3:0]` (pins 17/19/21/23) is
> not generated on this board - it is a passthrough of whichever Cypher-Input board's own strap
> is installed.

### J5 / J7 - Full Pin Map (shared template, per `Cypher/Board_Layout.md §4`'s `J6`)

| Top Row Signal | Top Row Pin# | Bottom Row Pin# | Bottom Row Signal |
| :--- | :---: | :---: | :--- |
| GND | 1 | 2 | GND |
| **ENC_DATA[0]** | 3 | 4 | **ENC_DATA[0]** |
| **ENC_DATA[1]** | 5 | 6 | **ENC_DATA[1]** |
| **ENC_DATA[2]** | 7 | 8 | **ENC_DATA[2]** |
| **ENC_DATA[3]** | 9 | 10 | **ENC_DATA[3]** |
| **ENC_DATA[4]** | 11 | 12 | **ENC_DATA[4]** |
| **ENC_DATA[5]** | 13 | 14 | **ENC_DATA[5]** |
| GND | 15 | 16 | GND |
| GND | 17 | 18 | GND |
| GND | 19 | 20 | GND |
| GND | 21 | 22 | GND |
| **CPLD_RESET_N** | 23 | 24 | **ENC_ACTIVE_INPUT_N** |
| GND (bar) | 25 | 26 | GND (bar) |
| **I2C_SDA** | 27 | 28 | **I2C_SCL** |
| GND | 29 | 30 | GND |
| GND | 31 | 32 | GND |
| GND | 33 | 34 | GND |
| GND | 35 | 36 | **TTD_HID_PASS** |
| **TTD_HID_IN** | 37 | 38 | GND |
| GND | 39 | 40 | **TTD_HID_OUT** |
| GND | 41 | 42 | GND |
| **TMS** | 43 | 44 | **TMS** |
| GND | 45 | 46 | GND |
| **TCK** | 47 | 48 | **TCK** |
| GND | 49 | 50 | GND |

### This board's wiring at J5 / J7

| Pin(s) | Wiring |
| :--- | :--- |
| Top row (3,5,7,9,11,13) - `ENC_DATA[5:0]` (J5 <-> J7 passthrough) | Direct passthrough wire - not connected to this board's ENC module CPLD; relays Cypher-Input's own data when this board is not directly under the Cypher Board |
| Bottom row (4,6,8,10,12,14) - `ENC_DATA[5:0]` (J5 & J7, tied together) | → own ENC module CPLD `CB[0:5]` (via J2 columns C01-C06) - this board's generated cipher data |
| 17-22 (J5 & J7, tied) | GND |
| 23 - `CPLD_RESET_N` (J5 & J7, tied) | → own ENC module CPLD `RST_N` (via J2 column C08) |
| 24 - `ENC_ACTIVE_INPUT_N` (J5 & J7, tied) | → received into own ENC module `ENC_ACTIVE_N` input (via J2 column C12) - this board consumes this signal, it does not generate it |
| 27, 28 (J5 <-> J7) - `I2C_SDA`/`I2C_SCL` | Direct passthrough wire - not connected to this board's own circuitry (no I2C device on this board, see `Design_Spec.md §1`); relays Cypher-Input's I2C bus through to whichever board is directly under the Cypher Board |
| 30, 32 (J5 & J7, tied) | NC; LED colour/brightness reception is carried on `J4`/`J6` (see §4 intro and `Design_Spec.md §6`) |
| 36 (J5 & J7, tied together) - `TTD_HID_PASS` | → own ENC module CPLD TDI (via J2 column C10, Row B `TDI`) - receives Cypher-Input's own TDO |
| 37 (J5 <-> J7) - `TTD_HID_IN` | Direct passthrough wire - not connected to the ENC module CPLD; relays the Cypher Board's TDI through to Cypher-Input if this board is directly under the Cypher Board |
| 40 (J5 & J7, tied together) - `TTD_HID_OUT` | → own ENC module CPLD TDO (via J2 column C11, Row A `TDO`) |
| 43/44, 47/48 (J5 & J7, tied together per signal) | → own ENC module CPLD TMS / TCK (via J2 columns C09/C07) |

> This board's own real TDI is driven from pin 36 (`TTD_HID_PASS`, tied on both J5 and J7) -
> receiving Cypher-Input's own TDO. This board's own real TDO drives pin 40 (`TTD_HID_OUT`, tied
> on both J5 and J7), reaching back to the Cypher Board's `J6` pin 40. Pin 37 (`TTD_HID_IN`) is a
> straight passthrough on this board only (bridging J5 and J7, not touching the ENC module CPLD)
> - it exists so that if this board is directly under the Cypher Board, the Cypher Board's own
> TDI (arriving on pin 37) can still reach Cypher-Input by passing straight through this board.
> TCK/TMS/CPLD_RESET_N are broadcast (tied together on
> both J5 and J7, both rows) since they are not chained.
>
> **ENC_DATA row convention:** bottom row = this board's own generated/consumed signal (since
> this board is documented as the `LBD_DEC` role - the opposite row to Cypher-Input's own
> `KBD_ENC` role); top row = straight passthrough, relaying Cypher-Input's own signal when this
> board is not directly under the Cypher Board. `BOARD_ROLE_ID` is carried on `J4`/`J6`. Pins
> 27/28 (`I2C_SDA`/`I2C_SCL`) are a straight passthrough - not connected to this board's own
> circuitry (no I2C device on this board) - so Cypher-Input's I2C bus can still reach the Cypher
> Board if this board sits directly beneath it. Pins 30/32 are unused (NC) since LED
> colour/brightness reception is carried on `J4`/`J6` instead - see `Design_Spec.md §4`/§6.
>
> `ENC_ACTIVE_INPUT_N` (pin 24) matches the Cypher Board's own internal net name, and shares
> column C12 with `CPLD_RESET_N` (pin 23) - only one physical pin is needed for `CPLD_RESET_N`
> since it is a broadcast/unchained signal.

---

## Diagram Reference

See `design/Diagrams/cypher-system-layout.drawio` and renders in `design/Diagrams/renders/` for
the system-level layout diagram once the Cypher-Output Board is added to that diagram set.
