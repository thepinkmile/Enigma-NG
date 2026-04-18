# Enigma-NG Power Budgets

**Status:** Draft
**Version:** v1.0.0
**Associated Hardware Revision:** Rev A
**Last Updated:** 2026-04-05

---

## Design Constraint Hierarchy

1. **TPS75733KTTRG3 LDO** (Power Module U7): **3.0A maximum output** — hard limit, component not to be changed.
2. **LINK-ALPHA 3V3_ENIG pins** (pins 39–44): 6 pins × 0.5A = 3.0A capacity — matches LDO limit.
3. **LINK-BETA 3V3_ENIG pins** (pins 6–12 plus 29–35): 14 pins × 0.5A = 7.0A capacity — above LDO
   limit; connector is not the bottleneck, the LDO is.
4. **Available to Stator + Rotor stack:** LDO output minus Controller-local consumption (RJ45 LEDs, pull-ups)
   ≈ 2.95A (Controller overhead ≤ 50mA).

---

## 3V3_ENIG Load Analysis

### Per-Device Current (Intel MAX II EPM240T100I5N [Encoder ×6] / EPM570T100I5N [Rotor ×30 + Stator] @ 3.3V)

| Operating condition | ICC (core) | Source |
| :--- | :--- | :--- |
| Static (no switching) | ~5 mA | Intel MAX II Datasheet ICC_STATIC |
| Typical cipher logic (50 MHz toggle) | ~25 mA | Intel MAX II Power Estimator (50% toggle, 50% resource use) |
| Worst-case (100 MHz, 80% resource use) | ~80 mA | MAX II Datasheet ICC_DYNAMIC worst case |

**Design value used:** 50 mA per CPLD (conservative typical — accounts for VHDL cipher switching without
being an unachievable worst-case peak).

### Per-Device Current (TI FDC2114RGHR Capacitive Sensor IC @ 3.3V)

| Condition | ICC |
| :--- | :--- |
| Active | 2.1 mA typ |

---

## 3V3_ENIG Allocation Table

| Consumer | Count | Per-unit (mA) | Total (mA) | Notes |
| :--- | :---: | :---: | :---: | :--- |
| Stator CPLD (U1, EPM570T100I5N) | 1 | 50 | 50 | JTAG forwarding + ENC signal routing |
| HID Encoder CPLDs (EPM240 ×2) | 2 | 50 | 100 | Keyboard decode + lightboard CPLD |
| Plugboard Encoder A CPLDs (EPM240 ×2) | 2 | 50 | 100 | Stecker map CPLD |
| Plugboard Encoder B CPLDs (EPM240 ×2) | 2 | 50 | 100 | Stecker map CPLD |
| FT232H VCCIO (JTAG Daughterboard) | 1 | 10 | 10 | VCCIO domain only; VCC (100 mA) is 5V_USB-sourced — see 5V_MAIN table |
| Rotor CPLDs (EPM570T100I5N ×30) | 30 | 50 | 1500 | All rotors cipher-active simultaneously |
| Rotor FDC2114RGHR capacitive sensor ICs (U2/U3 or U2/U4, 2 ICs per rotor, 60 ICs total) | 60 | 2.1 | 126 | Continuous position polling; two ICs per rotor add 4.2 mA to the 50 mA CPLD budget, giving 54.2 mA typ / 55 mA budget per rotor |
| INA219 current monitor (Stator) | 1 | 1 | 1 | Negligible |
| INA219 current monitor (Power Module) | 1 | 1 | 1 | Negligible |
| Extension Buffer ICs (SN74LVC2G125DCUR) | 5 | 2 | 10 | TCK/TMS re-drive for each 5-rotor group; one per Extension board; negligible load |
| Controller-local (RJ45 LEDs, logic) | — | — | 50 | Controller overhead subtracted at LINK-ALPHA |
| **Typical total** | | | **2,048 mA** | |
| **Rounded budget** | | | **≤ 2.05 A** | |

### Headroom vs LDO Limit

| Limit | Value | Margin |
| :--- | :--- | :--- |
| LDO hard limit | 3.00 A | — |
| Typical worst-case load | 2.05 A | **+0.95 A (32%)** |
| LINK-BETA connector capacity | 7.00 A | Not the constraint |

> ✅ **Conclusion:** The 3A TPS75733KTTRG3 LDO provides ~32% headroom above the worst-case typical load.
> No LDO upgrade is required for the current 30-rotor design.

---

## 3V3_ENIG Conflict Resolution

### STA-05 / STA-06: Shunt resistor and power figure reconciliation

| Document | Old figure | Resolved value | Action |
| :--- | :--- | :--- | :--- |
| Stator §2 "5A peak" | 5.0 A | **2.05 A** worst-case typical | ✅ Complete — Stator §2 updated to 2.05A worst-case typical; 5A figure retired |
| LINK-BETA capacity | 5.5 A | 7.0 A (14 pins total after DEC-037 — still not the bottleneck) | ✅ Complete — updated to regrouped rail model |
| Rotor ×30 claim "4.5A" | 4.5 A | **1.65 A** (30 × 55 mA budget; 1.63 A typ) | ✅ Complete — Rotor DR-ROT-06 and §3.1 now use the 54.2 mA typical / 55 mA budget figure; 150 mA figure retired |
| Shunt resistor | Stator: 20 mΩ, Controller: 10 mΩ | **10 mΩ CSS2H** (Stator R1 = CSS2H-2512R-R010ELF; Controller has no shunt) | ✅ Complete — Stator R1 updated to CSS2H-2512R-R010ELF (10mΩ, 2512 Kelvin) |

**INA219 shunt selection rationale (10 mΩ CSS2H-2512R-R010ELF):**

* V_drop at 2.05A: 2.05 × 0.010 = **20.5 mV** — within INA219 ±80 mV PGA range.
* V_drop at 3.00A max: 3.00 × 0.010 = **30 mV** — within ±80 mV range.
* Resolution: with 12-bit ADC at ±80 mV range, LSB = 2×80mV/4096 ≈ **39 µV/LSB** → I_LSB = 39µV/0.010Ω ≈ **4 mA** current resolution.
* Power dissipation at 2.05A: 2.05² × 0.010 = **42 mW** — 2512 Kelvin package (rated ≥0.5W) is adequate with >10× margin.
* Power dissipation at 3.00A max: 3.00² × 0.010 = **90 mW** — 2512 Kelvin package ≥0.5W still OK.
* CAL register: 0x0400 (1024) — unchanged. CAL = 0.04096 / (Current_LSB × R_SHUNT) = 0.04096 / (0.004 × 0.010) = 1024 ✓
* Part: CSS2H-2512R-R010ELF (Bourns 2512 Kelvin-sense, 10mΩ ±1%, 5A). Used on **PM R12** (LTC3350 RSENSE), **PM R23** (INA219 U12, 0x40, 5V_MAIN monitoring) and **Stator R1**
  (INA219 U2, 0x45, rotor-stack monitoring).
  Total build qty: 3.

---

## 5V_MAIN Load Analysis

| Consumer | Current | Notes |
| :--- | :--- | :--- |
| CM5 (Raspberry Pi Compute Module 5) | 5.0 A max | CM5 boot-to-load current profile; 25W at 5V = 5A |
| 3V3_ENIG LDO quiescent (TPS75733KTTRG3) | 2.05 A | Sourced from 5V_MAIN; P_in = 5V × 2.05A = 10.25W |
| Status LEDs, RJ45, misc. | 0.1 A | |
| FT232H VCC (JTAG Daughterboard — via Controller TPS2065C) | 0.1 A | USB HS active; VCC from 5V_USB (TPS2065C-protected 5V_MAIN output) |
| USB 3.0 external devices (TPS2065C rated max) | 1.60 A | System boundary: connected USB device load; TPS2065C hard-limits output |
| HDMI sink device | 0.05 A | System boundary: connected HDMI sink; AP2331W-limited |
| Settings Board indicator rail (via Link-Beta → Stator J_CFG) | 0.24 A | 12 indicators, one active colour per bank, 240mA max |
| Stator servo rail (via Link-Beta → J_SERVO) | 0.50 A | Budgeted Stator-side servo allocation |
| **Total 5V_MAIN worst case (system boundary)** | **9.50 A** | |
| **LMQ61460-Q1 dual-phase capacity** | **12.0 A** | 79.2% utilisation (9.50/12.0) ✓ |

> **Scope note:** The 7.40 A board-level budget (internal consumers: CM5 + LDO + misc + FT232H) covers internal consumers only.
> External device loads (USB 3.0 + HDMI) plus the Link-Beta-fed Settings Board + servo loads add 2.39 A, giving a system total of 9.50 A.
> Component utilisation figures (e.g. LMQ61460-Q1) are calculated against the 9.50 A system total.
>
> **Link-Beta 5V margin:** The Stator-facing 5V_MAIN group now uses four dedicated LINK-BETA pins
> (pins 3, 4, 37, and 38), giving **2.0 A connector capacity** for the Settings Board + servo branch. The
> current downstream budget is **0.74 A**, leaving ~**1.26 A** connector headroom for future 5V
> peripherals on the Stator side.

---

## Document History

| Date | Change |
| :--- | :--- |
| 2026-04-05 | Initial document — created to resolve STA-05/STA-06/ROT-04/PM-05 inconsistencies |
