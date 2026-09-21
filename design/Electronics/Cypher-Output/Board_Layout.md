# Cypher-Output Board V1.0 Pinout Reference

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

- **Top-left edge:** `J4`, Cypher-facing left-pair male connector.
- **Bottom-left edge:** `J6`, Cypher-facing left-pair female connector.
- **Right edge:** `J8`, USM-facing right-angle male connector.
- **ENC module mount:** `J1`-`J3` remain unchanged.

---

## 1. ENC Module Mount

`J1`-`J3` continue to follow `Encoder_Module/Board_Layout.md §1a-1c`.

---

## 2. J4 / J6 - Cypher Left Pair Template

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

### This board's wiring at J4 / J6

| Pins | Wiring |
| :--- | :--- |
| `5V_MAIN` and GND pins | Board power entry / return |
| 10, 12, 14, 16, 18, 20 | Local `ENC_DATA_OUT[5:0]` |
| 42 | Local `ENC_ACTIVE_OUTPUT_N` |
| Bottom-row `BOARD_ROLE_ID_OUT[3:0]` positions | Local Output-board capability strap |
| Input-side positions | Straight-through relay for `ENC_DATA_IN[5:0]`, `ENC_ACTIVE_INPUT_N`, and `BOARD_ROLE_ID_IN[3:0]` |

---

## 3. J8 - USM Right-Edge Connector

| Top Row Signal | Top Pin# | Bottom Pin# | Bottom Row Signal |
| :--- | :---: | :---: | :--- |
| `3V3_ENIG` | 1 | 2 | `3V3_ENIG` |
| `3V3_ENIG` | 3 | 4 | `3V3_ENIG` |
| GND | 5 | 6 | GND |
| GND | 7 | 8 | `TCK` |
| `I2C_SDA` | 9 | 10 | GND |
| GND | 11 | 12 | `TMS` |
| `I2C_SCL` | 13 | 14 | GND |
| GND | 15 | 16 | `TDO_OUTPUT` |
| `RED_DRIVE_N` | 17 | 18 | GND |
| `GREEN_DRIVE_N` | 19 | 20 | `TDI_OUTPUT` |
| `BLUE_DRIVE_N` | 21 | 22 | GND |
| `ILLUMINATION_DRIVE_N` | 23 | 24 | `CPLD_RESET_N` |
| GND (bar) | 25 | 26 | GND (bar) |
| `CPLD_RESET_N` | 27 | 28 | `ILLUMINATION_DRIVE_N` |
| GND | 29 | 30 | `BLUE_DRIVE_N` |
| `TDI_INPUT` | 31 | 32 | `GREEN_DRIVE_N` |
| GND | 33 | 34 | `RED_DRIVE_N` |
| `TDO_INPUT` | 35 | 36 | GND |
| GND | 37 | 38 | `I2C_SCL` |
| `TMS` | 39 | 40 | GND |
| GND | 41 | 42 | `I2C_SDA` |
| `TCK` | 43 | 44 | GND |
| GND | 45 | 46 | GND |
| `3V3_ENIG` | 47 | 48 | `3V3_ENIG` |
| `3V3_ENIG` | 49 | 50 | `3V3_ENIG` |

### This board's wiring at J8

| Pins | Wiring |
| :--- | :--- |
| 17 / 19 / 21 / 23 / 28 / 30 / 32 / 34 | USM lighting-drive inputs to the local LED stage |
| 24 / 27 / 39 / 43 | `CPLD_RESET_N`, `TMS`, and `TCK` to the local ENC module |
| 16 / 20 | Local Output-role JTAG `TDO` / `TDI` |
| 31 / 35 | NC on this board |
| 9 / 13 / 38 / 42 | `I2C2` present on the connector, not consumed by the current common board circuitry |
