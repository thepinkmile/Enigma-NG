# Cypher-Plugboard Board V1.0 Pinout Reference

**Status:** Draft
**Project:** Enigma-NG
**Author:** Izzyonstage & GitHub Copilot
**Version:** v.0.1.0
**Associated Hardware Revision:** Rev A
**Last Updated:** 2026-08-19

> **Board_Layout.md is a visualisation-only document.** Design narrative, specifications, and
> component rationale belong in `Design_Spec.md`. This file contains connector pinout references
> and board orientation notes only.

---

## Orientation Convention

- **PCB (thin strip, top edge only):** carries J1 (left) and J2 (right) HID interconnect
  connectors plus termination resistors R1-R3, fully populated by JLCPCB's single-sided SMT PCBA
  pass. Identical across all three variants - it does **not** carry the jack field.
- **Machined metal enclosure (separate from the PCB):** hosts the entire plugboard jack field -
  mechanical/harness-wired only, no PCB trace connection (see `Design_Spec.md §4`). Character
  rows run top-to-bottom, engraved/printed directly on the enclosure; row layout and jack count
  are variant-specific, and the enclosure itself is sized per variant (see each variant's own
  design file). Every jack's metal bushing bonds directly to this enclosure, keeping the whole
  jack field on the system's `GND_CHASSIS` network (see `Design_Spec.md §2`).
- **J1 (left, male)** and **J2 (right, male):** mounted flush with this board's top edge, mating
  upward with whichever HID board (Cypher-Input or Cypher-Output) sits directly above - the
  bottom-most board of the local 2-board HID stack. This board carries no bottom (female)
  connector pair of its own - it is always the last board in the local stack, per DEC-088.

---

## 1. J1 - Left Connector (Power / LED Broadcast / `BOARD_ROLE_ID` Template)

> **Connector Definition Owner:** Cypher Board `Board_Layout.md §4` (its own `J5`).
> Mates with the bottom-most HID board's `J6` (QSS-025-01-L-D-RA-K right-angle female).

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

### This board's wiring at J1

| Pin(s) | Wiring |
| :--- | :--- |
| 1-4, 47-50 - `3V3_ENIG` | Received - biases R1-R3's pull references (via J2) |
| 5-8, 43-46 - `5V_MAIN` | Received, left NC - no `5V_MAIN` consumer on this board |
| 9-12, 39-42 - GND | Received (return path) |
| 14 - `RED_DRIVE_N`, 16 - `GREEN_DRIVE_N`, 35 - `BRIGHTNESS_PWM_EN`, 37 - `BLUE_DRIVE_N` | Received, left NC - no LED bank on this board |
| 17-23 (top row) - `BOARD_ROLE_ID_IN[3:0]` | Received, left NC - this board carries no `BOARD_ROLE_ID` strap of its own |
| 28-34 (bottom row) - `BOARD_ROLE_ID_OUT[3:0]` | Received, left NC - same as above |
| 25/26 - GND (bar) | Fixed center GND bar |

> This board carries no bottom connector pair - it is always the last board in the local HID
> stack (per DEC-088), so nothing below it needs any of these signals relayed further.

---

## 2. J2 - Right Connector (JTAG + ENC_DATA + I2C + PWM Template)

> **Connector Definition Owner:** Cypher Board `Board_Layout.md §4` (its own `J6`).
> Mates with the bottom-most HID board's `J7` (QSS-025-01-L-D-RA-K right-angle female).

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

### This board's wiring at J2

| Pin(s) | Wiring |
| :--- | :--- |
| 3-14 - `ENC_DATA[5:0]` (both rows) | Received, left NC - no ENC module on this board |
| 23 - `CPLD_RESET_N` | → R3, 10 kOhm pull-up to `3V3_ENIG` |
| 24 - `ENC_ACTIVE_INPUT_N` | Received, left NC - no ENC module on this board |
| 27/28 - `I2C_SDA`/`I2C_SCL` | Received, left NC - no I2C device on this board |
| 36 - `TTD_HID_PASS`, 37 - `TTD_HID_IN`, 40 - `TTD_HID_OUT` | Received, left NC - no termination needed here; each HID board provides its own local TDI pull-up close to its own CPLD, via its ENC module's R3 (`Encoder_Module/Design_Spec.md §5` JTAG Chain Integrity - 10 kOhm to 3V3_ENIG, placed near U1; see `Design_Spec.md §3`). The system always requires both a Cypher-Input and a Cypher-Output board connected - there is no valid single-HID-board configuration. |
| 43/44 - `TMS` | → R2, 10 kOhm pull-up to `3V3_ENIG` |
| 47/48 - `TCK` | → R1, 10 kOhm pull-down to GND |

> This board carries no bottom connector pair - it is always the last board in the local HID
> stack (per DEC-088). TCK/TMS/`CPLD_RESET_N` are terminated here since they are broadcast/
> unchained signals that would otherwise dead-end floating; `ENC_DATA`, `I2C_SDA`/`I2C_SCL`,
> `ENC_ACTIVE_INPUT_N`, and `TTD_HID_IN`/`TTD_HID_PASS`/`TTD_HID_OUT` are simply left NC since
> this board has no ENC module, I2C device, or JTAG TDI/TDO of its own to consume them - each HID
> board's own local pull-up (close to its own CPLD) already gives these signals a defined idle
> state, and the system always requires both a Cypher-Input and a Cypher-Output board connected
> (no valid single-HID-board configuration exists).

---

## Diagram Reference

See `design/Diagrams/cypher-system-layout.drawio` and renders in `design/Diagrams/renders/` for
the system-level layout showing the Cypher-Plugboard Board's position at the bottom of the local
Cypher-Input/Cypher-Output HID stack.
