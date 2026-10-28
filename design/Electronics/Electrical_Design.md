# Electrical Design Requirements

**Status:** Reference
**Version:** v.0.1.0
**Last Updated:** 2026-10-28

## 1. Component Rules (The "Museum-Grade" Standard)

* **Dielectric:** **X7R** for all ceramic capacitors (Strictly no Y5V or Z5U).
* **Derating:** **2.5x Voltage rating** for all power capacitors (e.g., 50V caps on 15V rails).
* **Tolerance:** **1% precision resistors** for eFuse ladders and INA219 current-sense shunts.
* **Vias:** **Teardrops** on all signal/power vias; **0.3mm drill** standard; **VIPPO (Via-In-Pad)** for high-density CM5/eFuse pads to prevent solder wicking.

## 2. I2C Bus Address Table

| Bus | I2C Address | Device | Module | Function |
| :--- | :--- | :--- | :--- | :--- |
| `I2C0` | 0x09 | LTC3350 | Power Module | Supercap charger / health monitor |
| `I2C0` | 0x0B | Smart Battery | Power Module | Smart battery / SMBus monitor |
| `I2C0` | 0x28 | STUSB4500 | Power Module | USB-C PD Controller |
| `I2C0` | 0x3F | PCA9534A | Power Module | PM-local GPIO expander (`POE_STAT`, `SYS_FAULT`, `BATT_PRES_N`, `USB_STAT`, SW1 RGB control) |
| `I2C0` | 0x40 | INA219 | Power Module | 5V_MAIN current/power monitoring (10mΩ Kelvin-sense shunt R16) |
| `I2C1` | 0x20 | MCP23017 (U6) | Cypher Board | ENC_IN/ENC_OUT monitoring (16 GPIO) |
| `I2C1` | 0x21 | MCP23017 (U7) | Cypher Board | Virtual keypress injection, SOURCE_SEL, CPLD_RESET_N, spare GPIO |
| `I2C1` | 0x22 | MCP23017 (U8) | Cypher Board | CPLD configuration output driver (DEC-032) |
| `I2C1` | 0x40 | INA219 (U2) | Cypher Board | Rotor stack current/power telemetry (same address as PM's `I2C0` INA219 — safe reuse, independent buses; see DEC-101) |
| `I2C2` | 0x38 | PCA9534A (U4) | Cypher-Input (all variants) | Single fixed address; variant identified via `BOARD_ROLE_ID_IN[3:0]`, not I2C address; Space + Enter GPIO where populated |
| `I2C2` | 0x39 | Colour-value store (U1, TBD) | User Settings Module | Reserved address for the shared HID colour-value store / drive logic |

> **Note:** This document captures global electrical design rules. Board-specific design rules are in each board's Design_Spec.md.
> **Authoritative I2C address table:** `Controller/Design_Spec.md §4.1` is the single source of truth for this table; it is duplicated here for convenience only and must be kept in sync.
> Full design decision history: See `design/Design_Log/index.md`.
