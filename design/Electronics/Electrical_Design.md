# Electrical Design Requirements

**Status:** Reference
**Version:** v1.0.0
**Last Updated:** 2026-04-04

## 1. Component Rules (The "Museum-Grade" Standard)

* **Dielectric:** **X7R** for all ceramic capacitors (Strictly no Y5V or Z5U).
* **Derating:** **2.5x Voltage rating** for all power capacitors (e.g., 50V caps on 15V rails).
* **Tolerance:** **1% precision resistors** for eFuse ladders and INA219 current-sense shunts.
* **Vias:** **Teardrops** on all signal/power vias; **0.3mm drill** standard; **VIPPO (Via-In-Pad)** for high-density CM5/eFuse pads to prevent solder wicking.

## 2. I2C Bus Address Table

| I2C Address | Device | Module | Function |
| :--- | :--- | :--- | :--- |
| 0x28 | STUSB4500 | Power Module | USB-C PD Controller |
| 0x40 | INA219 | Power Module | Power rail telemetry (5V_MAIN, 3V3_ENIG, battery) |
| 0x45 | INA219 | Stator | Rotor stack power telemetry (3V3_ENIG shunt) |
| 0x0B | Smart Battery | Power Module | Smart battery / SMBus monitor |

> **Note:** This document captures global electrical design rules. Board-specific design rules are in each board's Design_Spec.md.
> Full design decision history: See `design/Design_Log.md`.