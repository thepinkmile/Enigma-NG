# Cypher-Plugboard Board V1.0 Pinout Reference

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

- **PCB strip:** carries `J1` and `J2` only.
- **Jack field:** separate mechanical enclosure / harness assembly.
- **This board is the lower end of the local HID / USM assembly.**

---

## 1. J1 - HID Left Pair Template

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

### This board's wiring at J1

| Pins | Wiring |
| :--- | :--- |
| `5V_MAIN`, GND | Received on connector pads only |
| `BOARD_ROLE_ID_IN[3:0]`, `BOARD_ROLE_ID_OUT[3:0]` | NC |
| `ENC_DATA_IN[5:0]`, `ENC_DATA_OUT[5:0]` | NC |
| `ENC_ACTIVE_INPUT_N`, `ENC_ACTIVE_OUTPUT_N` | NC |

---

## 2. J2 - USM Hub Template

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

### This board's wiring at J2

| Pins | Wiring |
| :--- | :--- |
| GND | Ground reference only |
| Every non-GND pin | NC |
