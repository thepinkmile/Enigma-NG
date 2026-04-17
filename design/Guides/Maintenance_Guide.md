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

* **LOGIK-BEREIT (Green):** Located on the Power Module near the Samtec link. Indicates stable internal logic rails.

## 3. Diagnostic Probe Banks

The Controller board features two 2×10 ENIG Gold diagnostic probe pad banks for real-time bus monitoring during bring-up and fault diagnosis. Connect a logic analyser via a 2×10 ribbon cable.

### Bank-Alpha (Power/Entry) — Top-Right of Controller

Monitors power rails, I²C telemetry bus, LED control signals, and power status.

| Pin | Signal | Direction | Description |
| :--- | :--- | :--- | :--- |
| 1 | 5V_MAIN | PM → CTRL | 5V power rail probe point |
| 2 | 5V_MAIN | PM → CTRL | 5V power rail (redundant) |
| 3 | 3V3_ENIG | PM → CTRL | 3.3V logic rail probe point |
| 4 | 3V3_ENIG | PM → CTRL | 3.3V logic rail (redundant) |
| 5 | I2C1_SDA | Bidir | I²C Telemetry bus data |
| 6 | I2C1_SCL | Bidir | I²C Telemetry bus clock |
| 7 | ETH_LED_LINK | CTRL → PM | Ethernet link status LED |
| 8 | ETH_LED_ACT | CTRL → PM | Ethernet activity LED |
| 9 | SW_LED_G | CTRL → PM | RGB LED green channel (GPIO 18) |
| 10 | SW_LED_R | CTRL → PM | RGB LED red channel (GPIO 17) |
| 11 | SW_LED_B | CTRL → PM | RGB LED blue channel (GPIO 19) |
| 12 | PWR_GD | PM → CTRL | Power-good signal (GPIO 27) |
| 13 | BATT_PRES_N | PM → CTRL | Battery presence active-low (GPIO 23) |
| 14 | SW_LED_CTRL | CTRL → PM | LED arbitration HIGH = CM5 in control (GPIO 20) |
| 15 | SPARE | — | Reserved for future use |
| 16 | SPARE | — | Reserved for future use |
| 17 | SPARE | — | Reserved for future use |
| 18 | SPARE | — | Reserved for future use |
| 19 | GND_CHASSIS | — | Chassis ground reference |
| 20 | GND | — | Signal/power ground return |

### Bank-Beta (Logic/Exit) — Top-Left of Controller

Monitors the remaining Link-Beta bring-up signals: JTAG, TTD_RETURN, I2C extension lines, and the
post-DEC-031 spare pads that replaced the former 12-bit encryption sniffer allocation.

| Pin | Signal | Direction | Description |
| :--- | :--- | :--- | :--- |
| 1 | SPARE | — | ENC_IN[0:5] freed by DEC-031; monitoring now via Stator U_EXP1 MCP23017 @ 0x20 |
| 2 | SPARE | — | ENC_IN[0:5] freed by DEC-031; monitoring now via Stator U_EXP1 MCP23017 @ 0x20 |
| 3 | SPARE | — | ENC_IN[0:5] freed by DEC-031; monitoring now via Stator U_EXP1 MCP23017 @ 0x20 |
| 4 | SPARE | — | ENC_IN[0:5] freed by DEC-031; monitoring now via Stator U_EXP1 MCP23017 @ 0x20 |
| 5 | SPARE | — | ENC_IN[0:5] freed by DEC-031; monitoring now via Stator U_EXP1 MCP23017 @ 0x20 |
| 6 | SPARE | — | ENC_IN[0:5] freed by DEC-031; monitoring now via Stator U_EXP1 MCP23017 @ 0x20 |
| 7 | SPARE | — | SYS_RESET_N freed by DEC-031; now Stator U_EXP2 GPA[7] @ 0x21 |
| 8 | GND | — | Ground reference |
| 9 | SPARE | — | ENC_OUT[0:5] freed by DEC-031; monitoring now via Stator U_EXP1 MCP23017 @ 0x20 |
| 10 | SPARE | — | ENC_OUT[0:5] freed by DEC-031; monitoring now via Stator U_EXP1 MCP23017 @ 0x20 |
| 11 | SPARE | — | ENC_OUT[0:5] freed by DEC-031; monitoring now via Stator U_EXP1 MCP23017 @ 0x20 |
| 12 | SPARE | — | ENC_OUT[0:5] freed by DEC-031; monitoring now via Stator U_EXP1 MCP23017 @ 0x20 |
| 13 | SPARE | — | ENC_OUT[0:5] freed by DEC-031; monitoring now via Stator U_EXP1 MCP23017 @ 0x20 |
| 14 | SPARE | — | ENC_OUT[0:5] freed by DEC-031; monitoring now via Stator U_EXP1 MCP23017 @ 0x20 |
| 15 | JTAG_TCK | JDB → Stator | JTAG clock (isolated from TDI/TMS) |
| 16 | GND | — | TCK shield / clock return |
| 17 | TMS | JDB → Stator | JTAG mode select |
| 18 | TDI | JDB → Stator | JTAG data in |
| 19 | TDO | Stator → JDB | JTAG data out (TTD_RETURN) |
| 20 | GND | — | JTAG trailing shield |
