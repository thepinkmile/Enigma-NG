# Enigma-NG Maintenance Guide

**Status:** Draft
**Version:** v1.0.0
**Associated Hardware Revision:** Rev A
**Last Updated:** 2026-03-30

## 1. Safety Procedures

* **Safety Glow (Amber):** If the external Amber LED is lit, the Supercapacitors are discharging (>5.1V). Do not open the machine.
* **Residual Voltage Test:** After the Amber LED extinguishes, use a multimeter on the 'SICHERHEITS-PROBE' (V+) and 'ERDE-PROBE' (GND) pads.
* **Touch-Safe Threshold:** Only begin work when the multimeter reads <2V.

### RTC Battery Safety

The Controller board contains an RTC backup battery (ML2032/CR2032 coin cell).

> ⚠️ **Battery Safety Warning:** The RTC backup battery (ML2032/CR2032 coin cell) is a lithium cell.
> Do not short-circuit, incinerate, disassemble, or expose to temperatures above 60°C. Replace only with the same or equivalent approved type. Dispose of in accordance with local regulations.

* **CR2032 (non-rechargeable):** Standard fit. The BAT54 protection diode (D1) must remain in circuit.
* **ML2032 (rechargeable):** Only if D1 is removed and the Linux OS `dtparam=rtc_bbat_vchg` parameter is enabled. See `design/Software/Linux_OS/` for software configuration.
* **Service interval:** >25 years under normal use. Battery replacement is a service-by-disassembly task — not field-replaceable in situ.

## 2. Internal Indicators

* **LOGIK-BEREIT (Green):** Located on the Power Module near the Controller dock edge. Indicates stable internal logic rails.

## 3. Diagnostic Probe Banks

The Controller board features two 2×10 ENIG Gold diagnostic probe pad banks for real-time bus monitoring during bring-up and fault diagnosis. Connect a logic analyser via a 2×10 ribbon cable.

### Bank-Alpha (PM Dock) — Top-Right of Controller

Monitors the Controller ↔ Power Module dock cluster.

| Pin | Signal | Direction | Description |
| :--- | :--- | :--- | :--- |
| 1 | 5V_MAIN_A | PM → CTRL | J1A regulated 5V sample |
| 2 | 5V_MAIN_B | PM → CTRL | J1A regulated 5V sample |
| 3 | 3V3_ENIG_A | PM → CTRL | J1A logic-rail sample |
| 4 | 3V3_ENIG_B | PM → CTRL | J1A logic-rail sample |
| 5 | VIN_POE_12V | CTRL → PM | J1B PoE auxiliary feed sample |
| 6 | I2C1_SDA | Bidir | PM telemetry bus |
| 7 | I2C1_SCL | Bidir | PM telemetry bus |
| 8 | PM_IO_INT_N | PM → CTRL | PM expander interrupt |
| 9 | PWR_GD | PM → CTRL | PM rail-health signal |
| 10 | ROTOR_EN | CTRL → PM | PM LDO enable |
| 11 | PWR_BUT | PM → CTRL | CM5 power-button path |
| 12 | GND | — | Signal ground |
| 13 | GND | — | Signal ground |
| 14 | GND | — | Signal ground |
| 15 | SPARE | — | Reserved for future use |
| 16 | SPARE | — | Reserved for future use |
| 17 | SPARE | — | Reserved for future use |
| 18 | SPARE | — | Reserved for future use |
| 19 | GND_CHASSIS | — | Chassis ground reference |
| 20 | GND | — | Signal/power ground return |

### Bank-Beta (Stator Dock) — Top-Left of Controller

Monitors the Controller ↔ Stator dock cluster.

| Pin | Signal | Direction | Description |
| :--- | :--- | :--- | :--- |
| 1 | 5V_MAIN_J2A_1 | CTRL → Stator | J2A 5V blade sample |
| 2 | 5V_MAIN_J2A_2 | CTRL → Stator | J2A 5V blade sample |
| 3 | 3V3_ENIG_J2B_1 | CTRL → Stator | J2B 3V3 blade sample |
| 4 | 3V3_ENIG_J2B_2 | CTRL → Stator | J2B 3V3 blade sample |
| 5 | I2C1_SDA | Bidir | Shared Stator / Settings I²C bus |
| 6 | I2C1_SCL | Bidir | Shared Stator / Settings I²C bus |
| 7 | JTAG_TCK | JDB → Stator | JTAG clock |
| 8 | TMS | JDB → Stator | JTAG mode select |
| 9 | TDI | JDB → Stator | JTAG data in |
| 10 | TTD_RETURN | Stator → JDB | JTAG return from rotor / reflector chain |
| 11 | GND_RET_A | — | Dock return / guard |
| 12 | GND_RET_B | — | Dock return / guard |
| 13 | GND_RET_C | — | Dock return / guard |
| 14 | GND_RET_D | — | Dock return / guard |
| 15 | SPARE | — | Reserved for future use |
| 16 | SPARE | — | Reserved for future use |
| 17 | SPARE | — | Reserved for future use |
| 18 | SPARE | — | Reserved for future use |
| 19 | GND_CHASSIS | — | Chassis ground reference |
| 20 | GND | — | Signal/power ground return |
