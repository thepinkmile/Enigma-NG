# User Settings Module V1.0 Layout & Pinout

**Status:** In Review
**Project:** Enigma-NG
**Author:** Izzyonstage & GitHub Copilot
**Version:** v.0.1.0
**Associated Hardware Revision:** Rev A
**Last Updated:** 2026-09-17

> **Board_Layout.md is a visualisation-only document.** Design narrative and requirements belong in
> `Design_Spec.md`.

---

## Orientation Convention

- **Top edge:** `J1`, Cypher-facing hub connector (Template 2, right-angle male).
- **Bottom edge:** `J2`, Plugboard-facing hub connector (Template 2, right-angle female).
- **Left edge:** `J3` upper HID connector and `J4` lower HID connector (Template 3, both
  right-angle female).
- **Local parts:** `U1` colour-value store / drive logic placeholder, `RV1` brightness dial,
  `R1`-`R3` JTAG termination, `BZ1` audio placeholder.

---

## 1. J1 / J2 - Hub Connector Template

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

### USM wiring notes

| Pins | Wiring |
| :--- | :--- |
| 1-4, 47-50 | `3V3_ENIG` entry / distribution |
| 18, 22 | `I2C_SDA` / `I2C_SCL` for the dedicated `I2C2` Cypher-peripherals bus |
| 21, 29, 30 | Broadcast `CPLD_RESET_N`, `TMS`, `TCK` with local termination at `R1`-`R3` |
| 33 (`J1`) | `TDI` in from Cypher |
| 34 (`J1`) | `TDO` return to Cypher from the HID-output board |
| 33 / 34 (`J2`) | NC |

---

## 2. J3 / J4 - HID Left Connector Template

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

### USM wiring notes

| Pins | Wiring |
| :--- | :--- |
| `3V3_ENIG`, GND | Broadcast to both HID boards |
| `I2C_SDA`, `I2C_SCL` | Broadcast `I2C2` bus to both HID boards |
| `RED_DRIVE_N`, `GREEN_DRIVE_N`, `BLUE_DRIVE_N`, `ILLUMINATION_DRIVE_N` | Shared lighting-drive broadcast from USM local logic |
| `CPLD_RESET_N`, `TMS`, `TCK` | Shared JTAG broadcast nets |
| `TDI_INPUT`, `TDO_INPUT` | Real JTAG path for whichever connected board identifies as Cypher-Input |
| `TDI_OUTPUT`, `TDO_OUTPUT` | Real JTAG path for whichever connected board identifies as Cypher-Output |

---

## 3. Mounting Holes

- `MH1`-`MH4`: M3 PTH, tied to `GND_CHASSIS`.
- Final board outline / enclosure integration is deferred to
  `.copilot/todos/usm-3-part-hid-module-mechanical-review.md`.
