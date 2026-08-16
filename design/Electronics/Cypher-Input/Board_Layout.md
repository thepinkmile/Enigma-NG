# Cypher-Input Board V1.0 Pinout Reference

**Status:** Draft
**Project:** Enigma-NG
**Author:** Izzyonstage & GitHub Copilot
**Version:** v.0.1.0
**Associated Hardware Revision:** Rev A
**Last Updated:** 2026-08-16

> **Board_Layout.md is a visualisation-only document.** Design narrative, specifications, and
> component rationale belong in `Design_Spec.md`. This file contains connector pinout references
> and board orientation notes only.

---

## Orientation Convention

- **Top face (L1):** LED bank (D1-D26, D1-D42, or D1-D12, depending on variant) and RV1
  (brightness potentiometer) only. **Neither is part of the JLCPCB PCBA order** - both are
  hand-soldered by the user after the bare-assembled board is delivered, keeping JLCPCB's
  automated SMT assembly single-sided (see `Design_Spec.md §2` Architecture). Keyswitches occupy
  the rest of this face (Cherry MX2A-71NB switches plug down through the board into rear-mounted
  Kailh hot-swap sockets - see Rear face below). RV1 sits in the keyless region that corresponds
  to a number-pad area on a conventional keyboard, off to the side of the main keyswitch cluster.
- **Rear face (L4):** fully populated by JLCPCB's single-sided SMT PCBA pass. ENC module mount
  (J1-J3, keyed and polarity-free per Hirose DF40C asymmetric standoff pattern) - positioned
  directly beneath RV1, in the same keyless region, since no keyswitches occupy that area on the
  top face; Cypher Board interconnect (J4-J7); I2C GPIO expander (U4); 555 oscillator (U1) and
  supporting passives; LED bank current-limit resistors; LED bank P-MOSFET switches (U5, U6, U7)
  and shared cathode-return brightness switch (U8); colour-select mux (U9) and Shift-key sense
  network (D9, R9) - 64-Character variant only; Kailh hot-swap sockets (SW1-SW26, SW1-SW42, or
  SW1-SW12, depending on variant); 3V3_ENIG entry decoupling bank; local decoupling; Data Plate.
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
> every variant - LED colour selection is generated entirely on this board and never uses any
> `plain-bits` position** (per DEC-087):
>
> - **64-Character variant:** PB[0:39] = 40 cipher-path keyswitch inputs; PB[40:63]
>   unused/spare - see `Cypher_Input_64_Char_Design.md §3`.
> - **26-Char Classic variant:** PB[0:25] = 26 letter keys; PB[26:63] unused/spare - see
>   `Cypher_Input_26_Char_Design.md §3`.
> - **10-Numeric variant:** PB[0:9] = 10 digit keys; PB[10:63] unused/spare - see
>   `Cypher_Input_10_Numeric_Design.md §3`.
>
> Space and Enter (64-Character and 10-Numeric variants) are not on this bus - see `Design_Spec.md §3a`
> (read via U4 instead). LED `RED_DRIVE_N`/`GREEN_DRIVE_N`/`BLUE_DRIVE_N` are generated by U4/U9
> (see `Design_Spec.md §5`) and never appear on J1/J2/J3.

---

## 2. J2 - ENC Module Mount, Connector B (DF40C-24DS-0.4V(51))

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
| C12 | GND | ENC_ACTIVE_N (`ENC_ACTIVE_INPUT_N` toward J5/J7) |

> **This board's usage:** all 12 signals active. `ENC_ACTIVE_N` here is the ENC module's output
> (keyboard/encoder role - see `Design_Spec.md §3`), forwarded to J5/J7 as `ENC_ACTIVE_INPUT_N`.
> **`BRIGHTNESS_PWM` is independent of the ENC module's CPLD GCLK0 pin** - brightness control (555
> oscillator, U1) is fully independent of the ENC module; see `Design_Spec.md §6`.

---

## 3. J3 - ENC Module Mount, Connector C (DF40C-10DS-0.4V(51))

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
| J4 | Top-Left (TL) | Male, right-angle | QTS-025-01-L-D-RA-P | 3V3_ENIG, 5V_MAIN, GND, LED colour/brightness broadcast, `BOARD_ROLE_ID[3:0]` |
| J5 | Top-Right (TR) | Male, right-angle | QTS-025-01-L-D-RA-P | GND (center bar) + JTAG chain-through signals |
| J6 | Bottom-Left (BL) | Female, right-angle | QSS-025-01-L-D-RA-K | 3V3_ENIG, 5V_MAIN, GND, LED colour/brightness broadcast, `BOARD_ROLE_ID[3:0]` |
| J7 | Bottom-Right (BR) | Female, right-angle | QSS-025-01-L-D-RA-K | GND (center bar) + JTAG chain-through signals |

J4/J6 (left side) mate with whichever neighbour's opposite-gender left connector. This board
drives 4 LED-related signals onto J4/J6 (broadcast, tied both connectors): `RED_DRIVE_N`,
`GREEN_DRIVE_N`, `BLUE_DRIVE_N` (final colour outputs from U9/U4, `Design_Spec.md §5`) and
`BRIGHTNESS_PWM_EN` (from U8, `Design_Spec.md §6`) - generated on this board, consumed only by
the future Cypher-Output board's own LED bank/cathode-return switch. This board's own
`BOARD_ROLE_ID[3:0]` variant-ID strap is also carried on J4/J6 - see the "J4 / J6 -
Full Pin Map" section below for the concrete pin numbers. J5/J7
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
| 5-8 - `5V_MAIN` (J4 & J6, tied) | Board power net; final downstream consumption depends on the LED component selected in `merge-missing-components.md` |
| 14/16 - `RED_DRIVE_N`/`GREEN_DRIVE_N` (bottom row, J4 & J6, tied); 35/37 - `BRIGHTNESS_PWM_EN`/`BLUE_DRIVE_N` (top row, J4 & J6, tied) | → this board's own U9/U4 colour outputs and U8 brightness gate (`Design_Spec.md §5`/§6) - generated on this board, consumed only by the future Cypher-Output board |
| 17/19/21/23 - `BOARD_ROLE_ID_IN[3:0]` top row (J4 & J6, tied together) | Hardwired 3V3_ENIG/GND strap identifying this board's own variant (Classic/64-Character/10-Numeric); driven onto the top-row pin of both J4 and J6 - encoding per table below |
| 34/32/30/28 - `BOARD_ROLE_ID_OUT[3:0]` bottom row (J4 <-> J6 passthrough) | Direct passthrough wire (this board's own internal trace bridging J4's bottom-row pin to J6's bottom-row pin) - relays Cypher-Output's own ID code through this board when this board is not the one directly facing Cypher-Output, same convention as `ENC_DATA` at J5/J7 |

> **`BOARD_ROLE_ID_IN[3:0]`/`BOARD_ROLE_ID_OUT[3:0]` encoding (per `Cypher/Board_Layout.md §4`,
> capability bitmask - see `Design_Spec.md §3a`):** bit0 = Characters, bit1 = Numbers, bit2 =
> Special, bit3 = Custom (never populated by a Cypher-Input board).
>
> | ID[3] | ID[2] | ID[1] | ID[0] | Value | Variant |
> | :---: | :---: | :---: | :---: | :---: | :--- |
> | GND | GND | GND | 3V3 | 0b0001 | 26-Char Classic |
> | GND | GND | 3V3 | GND | 0b0010 | 10-Numeric |
> | GND | 3V3 | 3V3 | 3V3 | 0b0111 | 64-Character |
>
> This board's own `BOARD_ROLE_ID_IN[3:0]` strap (pins 17/19/21/23) is hardwired per the above
> table according to which variant (26-Char Classic, 64-Character, or 10-Numeric) is populated.
> `BOARD_ROLE_ID_OUT[3:0]` (pins 34/32/30/28) is not generated on this board - it is a
> passthrough of whichever Cypher-Output board's own strap is installed.

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
| GND | 35 | 36 | **TTD** |
| **TTD** | 37 | 38 | GND |
| GND | 39 | 40 | **TTD** |
| GND | 41 | 42 | GND |
| **TMS** | 43 | 44 | **TMS** |
| GND | 45 | 46 | GND |
| **TCK** | 47 | 48 | **TCK** |
| GND | 49 | 50 | GND |

### This board's wiring at J5 / J7

| Pin(s) | Wiring |
| :--- | :--- |
| Top row (3,5,7,9,11,13) - `ENC_DATA[5:0]` (J5 & J7, tied together) | → own ENC module CPLD `CB[0:5]` (via J2 columns C01-C06) - this board's generated cipher data |
| Bottom row (4,6,8,10,12,14) - `ENC_DATA[5:0]` (J5 <-> J7 passthrough) | Direct passthrough wire - not connected to this board's ENC module CPLD; relays Cypher-Output's own data when this board is not directly under the Cypher Board |
| 17-22 (J5 & J7, tied) | GND |
| 23 - `CPLD_RESET_N` (J5 & J7, tied) | → own ENC module CPLD `RST_N` (via J2 column C08) |
| 24 - `ENC_ACTIVE_INPUT_N` (J5 & J7, tied) | → driven from own ENC module `ENC_ACTIVE_N` (via J2 column C12) - this board's own generated keypress-activity signal |
| 27 - `I2C_SDA`, 28 - `I2C_SCL` (J5 & J7, tied) | → own U4 (PCA9534A) I2C bus - shared multidrop bus, not row-differentiated |
| 30, 32 (J5 & J7, tied) | NC; LED colour/brightness broadcast is carried on `J4`/`J6` (see §4 intro and `Design_Spec.md §7`) |
| 36 (J5 & J7, tied together) | → own ENC module CPLD TDO (via J2 column C11, Row A `TDO`) |
| 37 (J5 active; NC on J7) | → own ENC module CPLD TDI (via J2 column C10, Row B `TDI`) |
| 40 (J5 <-> J7) | Direct passthrough wire - not connected to the ENC module CPLD |
| 43/44, 47/48 (J5 & J7, tied together per signal) | → own ENC module CPLD TMS / TCK (via J2 columns C09/C07) |

> `TTD` at pin 37 is this board's own real TDI (single-sided - only J5, the top/male connector, is
> active; J7 is NC). This board's own real TDO drives pin 36 (tied on both J5 and J7), reaching
> whichever neighbour needs it as its own TDI. Pin 40 is a straight passthrough on this board only
> (bridging J5 and J7, not touching the ENC module CPLD) - it exists so that if this board is
> *not* the one directly under the Cypher Board, the other HID board's own TDO (arriving on pin
> 40) can still reach the Cypher Board's `J6` pin 40 (`TTD_RETURN`) by passing straight through
> this board. TCK/TMS/CPLD_RESET_N are broadcast (tied together on both J5 and J7, both rows)
> since they are not chained.
>
> **ENC_DATA row convention:** top row = this board's own generated/consumed
> signal (since this board is documented as the `KBD_ENC` role); bottom row = straight
> passthrough, relaying Cypher-Output's own signal when this board is not directly under the
> Cypher Board. `I2C_SCL`/`I2C_SDA` are single, non-chained signals (multidrop bus) tied
> identically across both J5 and J7 - no row distinction needed. `BOARD_ROLE_ID[3:0]` is
> carried on `J4`/`J6`. Pins 30/32 are unused (NC) since LED colour/brightness broadcast
> is generated entirely on this board and carried on `J4`/`J6` - see `Design_Spec.md §5`/§6/§7.
>
> `ENC_ACTIVE_INPUT_N` (pin 24) matches the Cypher Board's own internal net name, and shares
> column C12 with `CPLD_RESET_N` (pin 23) - only one physical pin is needed for `CPLD_RESET_N`
> since it is a
> broadcast/unchained signal.

---

## Diagram Reference

See `design/Diagrams/cypher-system-layout.drawio` and renders in `design/Diagrams/renders/` for
the system-level layout diagram once the Cypher-Input Board is added to that diagram set.
