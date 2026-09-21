# Cypher Board V1.0 Pinout Reference

**Status:** Draft
**Project:** Enigma-NG
**Author:** Izzyonstage & GitHub Copilot
**Version:** v.0.1.0
**Associated Hardware Revision:** Rev A
**Last Updated:** 2026-09-17

> **Board_Layout.md is a visualisation-only document.** Design narrative and requirements belong in
> `Design_Spec.md`.

---

## Orientation Convention

- **Front face:** faces the first Rotor Mini-Stack.
- **Back face:** carries the ENC module mounts (`J7`-`J18`), the Controller dock connectors
  (`J1` / `J2`), the HID connectors (`J5` / `J6`), and the spade blade terminal bank (`J20+`).
- **STA side:** `J3`.
- **REF side:** `J4`.

---

## 1. J1 / J2 - Controller Dock

Connector definitions remain as documented by `Controller/Board_Layout.md`.

---

## 2. J3 - Stack-Input / STA-Side Stacking Connector

Connector definition remains owned by `Stack-Input/Board_Layout.md §1`.

---

## 3. J4 - Stack-Output / REF-Side Stacking Connector

Connector definition remains owned by `Stack-Output/Board_Layout.md §1`.

---

## 4. J5 / J6 - HID / USM Interfaces

### J5 - HID Left Pair Template

| Top Row Signal | Top Pin# | Bottom Pin# | Bottom Row Signal |
| :--- | :---: | :---: | :--- |
| `5V_MAIN` | 1 | 2 | `5V_MAIN` |
| `5V_MAIN` | 3 | 4 | `5V_MAIN` |
| GND | 5 | 6 | GND |
| GND | 7 | 8 | GND |
| `ENC_ACTIVE_INPUT_N` | 9 | 10 | `ENC_DATA_OUT[5]` |
| GND | 11 | 12 | `ENC_DATA_OUT[4]` |
| GND | 13 | 14 | `ENC_DATA_OUT[3]` |
| `BOARD_ROLE_ID_IN[0]` | 15 | 16 | `ENC_DATA_OUT[2]` |
| `BOARD_ROLE_ID_IN[1]` | 17 | 18 | `ENC_DATA_OUT[1]` |
| `BOARD_ROLE_ID_IN[2]` | 19 | 20 | `ENC_DATA_OUT[0]` |
| `BOARD_ROLE_ID_IN[3]` | 21 | 22 | GND |
| GND | 23 | 24 | GND |
| GND (bar) | 25 | 26 | GND (bar) |
| GND | 27 | 28 | GND |
| GND | 29 | 30 | `BOARD_ROLE_ID_OUT[3]` |
| `ENC_DATA_IN[0]` | 31 | 32 | `BOARD_ROLE_ID_OUT[2]` |
| `ENC_DATA_IN[1]` | 33 | 34 | `BOARD_ROLE_ID_OUT[1]` |
| `ENC_DATA_IN[2]` | 35 | 36 | `BOARD_ROLE_ID_OUT[0]` |
| `ENC_DATA_IN[3]` | 37 | 38 | GND |
| `ENC_DATA_IN[4]` | 39 | 40 | GND |
| `ENC_DATA_IN[5]` | 41 | 42 | `ENC_ACTIVE_OUTPUT_N` |
| GND | 43 | 44 | GND |
| GND | 45 | 46 | GND |
| `5V_MAIN` | 47 | 48 | `5V_MAIN` |
| `5V_MAIN` | 49 | 50 | `5V_MAIN` |

#### Cypher Board wiring at J5

| Pins | Wiring |
| :--- | :--- |
| 9 | `ENC_ACTIVE_INPUT_N` to the Cypher monitoring path |
| 15, 17, 19, 21 | `BOARD_ROLE_ID_IN[3:0]` to the CPLD compatibility comparator |
| 30, 32, 34, 36 | `BOARD_ROLE_ID_OUT[3:0]` to the CPLD compatibility comparator |
| 31, 33, 35, 37, 39, 41 | `ENC_IN_KBD[5:0]` to CPLD `U1` |
| 10, 12, 14, 16, 18, 20 | `ENC_OUT_LBD[5:0]` from CPLD `U1` |
| 42 | `ENC_ACTIVE_OUTPUT_N` to the Cypher monitoring path |
| `5V_MAIN` and GND | HID power / return distribution |

### J6 - USM Hub Template

| Top Row Signal | Top Pin# | Bottom Pin# | Bottom Row Signal |
| :--- | :---: | :---: | :--- |
| `3V3_ENIG` | 1 | 2 | `3V3_ENIG` |
| `3V3_ENIG` | 3 | 4 | `3V3_ENIG` |
| GND | 5 | 6 | GND |
| GND | 7 | 8 | GND |
| GND | 9 | 10 | GND |
| GND | 11 | 12 | GND |
| GND | 13 | 14 | GND |
| GND | 15 | 16 | GND |
| GND | 17 | 18 | `I2C_SDA` |
| GND | 19 | 20 | GND |
| `CPLD_RESET_N` | 21 | 22 | `I2C_SCL` |
| GND | 23 | 24 | GND |
| GND (bar) | 25 | 26 | GND (bar) |
| GND | 27 | 28 | GND |
| `TMS` | 29 | 30 | `TCK` |
| GND | 31 | 32 | GND |
| `TDI` | 33 | 34 | `TDO` |
| GND | 35 | 36 | GND |
| GND | 37 | 38 | GND |
| GND | 39 | 40 | GND |
| GND | 41 | 42 | GND |
| GND | 43 | 44 | GND |
| GND | 45 | 46 | GND |
| `3V3_ENIG` | 47 | 48 | `3V3_ENIG` |
| `3V3_ENIG` | 49 | 50 | `3V3_ENIG` |

#### Cypher Board wiring at J6

| Pins | Wiring |
| :--- | :--- |
| 18 / 22 | Dedicated `I2C2_SDA` / `I2C2_SCL` bus to USM |
| 21 / 29 / 30 | Broadcast `CPLD_RESET_N`, `TMS`, `TCK` from the Cypher JTAG hub |
| 33 | FT232H `U17` TDI source into the HID sub-chain |
| 34 | HID sub-chain TDO return from USM, then onward through `R50` to `U17` TDO |
| `3V3_ENIG` and GND | USM logic power / return |

---

## 5. J7-J18 - ENC Module Mounts

Connector definitions remain owned by `Encoder_Module/Board_Layout.md §1a-1c`.

---

## 6. J20+ - Spade Blade Terminal Bank

The plugboard jack harness still terminates at `J20+` on this board.
