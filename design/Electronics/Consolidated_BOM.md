# Enigma-NG Consolidated BOM & Spares

**Status:** Draft — pending schematic freeze
**Project:** Enigma-NG
**Author:** Izzyonstage & GitHub Copilot
**Version:** v1.0.0
**Last Updated:** 2026-04-05

## Overview

This is the consolidated Bill of Materials for all boards and modules in the Enigma-NG system.
It covers critical spares, common passives, high-speed interconnects, power components, and supplier
reference information. For per-board BOM notes and design constraints, refer to each board's
individual `Design_Spec.md` file.

## Component Usage Summary

This table shows the component count per board instance and system-wide totals, accounting for
×3 Encoder boards and ×30 Rotor boards in the complete system. The EXT column shows per-board
quantities for one Extension board; Rev A uses ×1 Extension board, while the full 30-rotor build
requires ×5 Extension boards (one between each pair of 5-rotor groups). System Total reflects
the Rev A single-Extension configuration unless otherwise noted.

| MPN / Description | PM | CTL | STA | ENC (×1) | ENC Total (×3) | ROT (×1) | ROT Total (×30) | REF | EXT | JDB | System Total |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| EPM240T100I5N — Intel MAX II CPLD (TQFP-100) | — | — | — | 2 | 6 | — | — | — | — | — | 6 |
| EPM570T100I5N — Intel MAX II CPLD (TQFP-100; 570 LEs; drop-in for EPM240; used on Stator and Rotor boards) | — | — | 1 | — | — | 1 | 30 | — | — | — | 31 |
| INA219AIDR — Zero-Drift Power Monitor (SOIC-8) | 1 | — | 1 | — | — | — | — | — | — | — | 2 |
| FDC2114RGHR — 4-ch Capacitive Sensor IC, U2 Track A (bits[5:3] N=64; bits[3:0] N=26), Board A, addr 0x2A (16-VQFN) | — | — | — | — | — | 1 | 30 | — | — | — | 30 |
| FDC2114RGHR — 4-ch Capacitive Sensor IC, U3 Track B (bits[2:0] N=64 only; NOT POPULATED for N=26), Board B, addr 0x2B (16-VQFN) | — | — | — | — | — | 1 | 30 | — | — | — | 30 |
| FDC2114RGHR — 4-ch Capacitive Sensor IC, U4 STGC bit[4] (N=26 only; NOT POPULATED for N=64), Board A, addr 0x2B (16-VQFN) | — | — | — | — | — | 1 | TBD | — | — | — | TBD (N=26 builds only) |
| SN74LVC2G125DCUR — Dual 3-State Buffer (VSSOP-8) | — | — | — | — | — | — | — | — | 1 | 1 | 2 |
| SN74LVC1G14DBVRQ1 — Single Schmitt Inverter (SOT-23-5) | 2 | — | — | — | — | — | — | — | — | — | 2 |
| FT232H — USB 2.0 to MPSSE Bridge (QFN-56) | — | — | — | — | — | — | — | — | — | 1 | 1 |
| CM5 — Raspberry Pi Compute Module 5 | — | 1 | — | — | — | — | — | — | — | — | 1 |
| TPS75733KTTRG3 — 3.3 V LDO Regulator (TO-263 KTT 5-pin) | 1 | — | — | — | — | — | — | — | — | — | 1 |
| TPS259804ONRGER — eFuse / Hot-Swap Controller (VQFN-24) | 1 | — | — | — | — | — | — | — | — | — | 1 |
| LMQ61460AFSQRJRRQ1 — 5 V Synchronous Buck Converter (VQFN-HR RJR 14-pin 4×3.5mm) | 2 | — | — | — | — | — | — | — | — | — | 2 |
| LTC3350EUHF#PBF — Supercapacitor Manager (QFN-38) | 1 | — | — | — | — | — | — | — | — | — | 1 |
| TPS25751DREFR — USB PD 3.1 DRP Controller (WQFN-38) | 1 | — | — | — | — | — | — | — | — | — | 1 |
| STUSB4500LQTR — USB-C Sink Controller (QFN-24) | 1 | — | — | — | — | — | — | — | — | — | 1 |
| LM74700QDBVRQ1 — Ideal-Diode OR-ing Controller (SOT-23-6) | 3 | — | — | — | — | — | — | — | — | — | 3 |
| MCP121T-450E/LB — 4.5 V Voltage Supervisor (SC70-3) | 1 | — | — | — | — | — | — | — | — | — | 1 |
| TPS2372-4 — PoE PD Interface Type 4 (VQFN-20) | 1 | — | — | — | — | — | — | — | — | — | 1 |
| TPS23730RMTR — PoE ACF DC-DC Controller (WQFN-20) | 1 | — | — | — | — | — | — | — | — | — | 1 |
| MIC1555YM5-TR — CMOS Timer / LED Oscillator (SOT-23-5) | 2 | — | — | — | — | — | — | — | — | — | 2 |
| TPS2065C — USB Power Distribution Switch (SOT-23-5) | — | 1 | — | — | — | — | — | — | — | — | 1 |
| AP2331W — HDMI Current Limiter (SOT-23-5) | — | 1 | — | — | — | — | — | — | — | — | 1 |
| TPD4E05U06QDQARQ1 — 4-Channel ESD Array (U-DFN-10) | 3 | 1 | — | — | — | — | — | — | — | — | 4 |
| TPD1E10B06DYARQ1 — Single-Channel ESD (SOD-523) | 1 | — | — | — | — | — | — | — | — | — | 1 |
| TPD2E2U06DRLR — Dual-Channel SMBus ESD (SOT-553) | 1 | — | — | — | — | — | — | — | — | — | 1 |
| CSD17483F4T — 30 V 10 A N-ch OR-ing MOSFET (SON-8) | 3 | — | — | — | — | — | — | — | — | — | 3 |
| BSS138 (onsemi) — 50 V N-ch Logic-Level MOSFET (SOT-23) | 2 | — | — | — | — | — | — | — | — | — | 2 |
| BAT54 (Diotec) — Schottky Diode (SOD-323 / SOT-23) | 2 | 1 | — | — | — | — | — | — | — | — | 3 |
| | | | | | | | | | | | |
| 0.1 µF X7R 0402 decoupling cap | 15 | 1 | 8 | 80 | 240 | 8 | 240 | — | 1 | 4 | 509 |
| 10 µF X7R 50 V 1206 bulk decoupling (CL31B106KBHNNNE) | — | 5 | 5 | 5 | 15 | 5 | 150 | 5 | 5 | — | 185 |
| 22 µF X7R 25 V 1210 bulk cap (CL32B226KAJNNNE) | 15 | — | — | — | — | — | — | — | — | — | 15 |
| 4.7 µF X7R 0402 entry filter (JDB 5V_USB, C19666) | — | — | — | — | — | — | — | — | — | 1 | 1 |
| 10 µF 16 V X7R 0603 monostable timing cap (CL10B106KA8NNNC) | 1 | — | — | — | — | — | — | — | — | — | 1 |
| 1 µF X7R 50 V 0805 (C0805C105K5RACTU) | 3 | — | — | — | — | — | — | — | — | — | 3 |
| 10 µF 25 V X7R 1206 LDO input cap (C1206C106K3RACTU) | 1 | — | — | — | — | — | — | — | — | — | 1 |
| 10 nF X7R 50 V 0402 soft-start cap (CL05B103KB5NNNC) | 1 | — | — | — | — | — | — | — | — | — | 1 |
| 10 nF 100 V X7R 0402 Bob Smith termination cap | 1 | — | — | — | — | — | — | — | — | — | 1 |
| 100 pF X7R 25 V 0402 SYNC SW-ringing LP filter (C0402C101K3RACAUTO) | 1 | — | — | — | — | — | — | — | — | — | 1 |
| 22 nF X7R 25 V 0603 SYNC phase-delay cap (CL10B223KB8WPNC) | 1 | — | — | — | — | — | — | — | — | — | 1 |
| 25 F / 2.7 V Supercapacitor (Abracon ADCR-T02R7SA256MB) | 6 | — | — | — | — | — | — | — | — | — | 6 |
| | | | | | | | | | | | |
| 10 kΩ 1% 0603 pull resistor (ERJ-3EKF1002V / C25804) | 6 | 2 | 9 | — | — | — | — | — | — | — | 17 |
| 10 kΩ 1% 0402 pull resistor (ERJ-2RKF1002X / C25744) | 2 | — | — | 68 | 204 | 4 | 120 | — | — | 2 | 328 |
| 75 Ω 1% 0603 series resistor (ERJ-3EKF75R0V / C105905) | — | — | 9 | — | — | — | — | — | — | — | 9 |
| 75 Ω 1% 0402 series resistor (ERJ-2RKF75R0X) | 4 | — | — | 1 | 3 | 1 | 30 | — | — | — | 37 |
| 33 Ω 1% 0603 series resistor (ERJ-3EKF33R0V / C25819) | — | — | — | — | — | — | — | — | — | — | — |
| 33 Ω 1% 0402 series resistor (ERJ-2RKF33R0X / C25808) | — | — | — | 1 | 3 | — | — | — | — | 4 | 7 |
| 22 Ω 0603 1% JTAG end-of-chain damping (ERJ-3EKF2200V) | — | — | — | — | — | — | — | 1 | — | — | 1 |
| 330 Ω 1% 0402 LED current-limit resistor (ERJ-2RKF3300X / C105872) | — | — | — | 2 | 6 | — | — | — | — | — | 6 |
| 330 Ω 1% 0603 Ethernet activity LED resistor (ERJ-3EKF3300V / C25803) | 2 | — | — | — | — | — | — | — | — | — | 2 |
| 4.7 kΩ 1% 0603 I²C pull-up (ERJ-3EKF4701V) | 2 | — | — | — | — | — | — | — | — | — | 2 |
| 100 Ω 1% 0603 differential termination (ERJ-3EKF1000V / C25806) | — | 1 | — | — | — | — | — | — | — | — | 1 |
| 20 mΩ 1% 1206 current-sense shunt (ERJ-6ENF20R0V / C123465) | — | — | — | — | — | — | — | — | — | — | — |
| 10 mΩ ±1% 5 A 2512 Kelvin shunt (CSS2H-2512R-R010ELF) | 2 | — | 1 | — | — | — | — | — | — | — | 3 |
| 121 kΩ 1% 0603 PoE MPS current set (ERJ-3EKF1213V) | 1 | — | — | — | — | — | — | — | — | — | 1 |
| 301 Ω 1% 0603 charge current set (ERJ-3EKF3010V) | 1 | — | — | — | — | — | — | — | — | — | 1 |
| 274 kΩ 1% 0603 MIC1555 U15 monostable R28 (ERJ-3EKF2743V) | 1 | — | — | — | — | — | — | — | — | — | 1 |
| 715 kΩ 1% 0603 MIC1555 timer R\_B (ERJ-3EKF7153V) | 1 | — | — | — | — | — | — | — | — | — | 1 |
| 232 kΩ 1% 0603 thick-film eFuse UVLO (ERJ-3EKF2323V) | 1 | — | — | — | — | — | — | — | — | — | 1 |
| 28.7 kΩ 1% 0603 thick-film eFuse UVLO (ERJ-3EKF2872V) | 1 | — | — | — | — | — | — | — | — | — | 1 |
| 210 Ω 1% 0603 thick-film eFuse ILIM (ERJ-3EKF2100V) | 1 | — | — | — | — | — | — | — | — | — | 1 |
| 86.6 kΩ 1% 0603 thick-film SYNC FSET resistor (ERJ-3EKF8662V) | 1 | — | — | — | — | — | — | — | — | — | 1 |
| 82.0 kΩ 1% 0402 thick-film SYNC phase-delay R\_DLY (ERJ-2RKF8202X) | 1 | — | — | — | — | — | — | — | — | — | 1 |
| 28.7 kΩ 0.1% 0603 thin-film supercap BACKUP R\_TOP (ERA-3ARB2872V) | 1 | — | — | — | — | — | — | — | — | — | 1 |
| 10.0 kΩ 0.1% 0603 thin-film supercap BACKUP R\_BOT (ERA-3ARB1002V) | 1 | — | — | — | — | — | — | — | — | — | 1 |
| 0 Ω 0603 bond / isolating resistor (ERJ-3GEY0R00V / C25807) | — | — | — | — | — | — | — | — | 2 | — | 2 |
| Ferrite bead 120 Ω @100 MHz 4.0 A 1206 (Laird HI1206P121R-10) | — | — | 4 | — | — | — | — | — | — | — | 4 |
| | | | | | | | | | | | |
| ERM8-040 80-pin Samtec BtB Male Header (Link-Alpha) | 1 | — | — | — | — | — | — | — | — | — | 1 |
| ERF8-040 80-pin Samtec BtB Female Socket (Link-Alpha) | — | 1 | — | — | — | — | — | — | — | — | 1 |
| ERM8-020 40-pin Samtec BtB Male Header (Link-Beta) | — | — | 1 | — | — | — | — | — | — | — | 1 |
| ERF8-020 40-pin Samtec BtB Female Socket (Link-Beta) | — | 1 | — | — | — | — | — | — | — | — | 1 |
| ERM8-005 10-pin Samtec Male Header 0.8 mm (Rotor interface) | — | — | — | — | — | 2 | 60 | 2 | 2 | — | 64 |
| ERF8-005 10-pin Samtec Female Socket 0.8 mm (Rotor interface) | — | — | 2 | — | — | 2 | 60 | — | 2 | — | 64 |
| ERM8-010 20-pin Samtec Male Header 0.8 mm (ENC data) | — | — | — | — | — | 1 | 30 | 1 | 1 | — | 32 |
| ERF8-010 20-pin Samtec Female Socket 0.8 mm (ENC data) | — | — | 1 | — | — | 1 | 30 | — | 1 | — | 32 |
| ⚠️ **Würth 61201221721** — 22-pin (2×11) keyed IDC box header, 2.54mm pitch — Rotor J\_INT (manually assembled post-JLCPCB SMT; 2 per rotor assembly) — **⚠️ Part does not exist — MPN requires verification; connector spec for J\_INT may need redesign** · All supplier PNs: TBD | — | — | — | — | — | 2 | 60 | — | — | — | 60 |
| Amphenol T821126A1S100CEU — 26-pin 2×13 shrouded box header, 2.54mm (RS-Online 832-3503; JLCPCB C3013501) | — | — | 3 | 1 | 3 | — | — | — | — | — | 6 |
| Adam Tech BHR-16-VUA — 16-pin 2×8 shrouded box header, 2.54mm (Mouser 737-BHR-16-VUA; DigiKey 2057-BHR-16-VUA-ND; JLCPCB C17692295) | — | — | 1 | — | — | — | — | 1 | 2 | — | 4 |
| ⚠️ **1×5 2.54mm female IDC header** — JDB J1 INPUT (5V_USB, 3V3_ENIG, D+, D−, GND) — **⚠️ No suitable part found — header spec requires redesign** · All supplier PNs: TBD | — | — | — | — | — | — | — | — | — | 1 | 1 |
| ⚠️ **1×10 2.54mm female IDC header** — JDB J2 JTAG OUTPUT (10-pin interleaved GND) — **⚠️ No suitable part found — header spec requires redesign** · All supplier PNs: TBD | — | — | — | — | — | — | — | — | — | 1 | 1 |
| USB 3.0 Type-A Dual-Stack (Molex 48406-0003) | — | 1 | — | — | — | — | — | — | — | — | 1 |
| HDMI Type-A Full-Size (TE 2007435-1) | — | 1 | — | — | — | — | — | — | — | — | 1 |
| USB-C SMT Receptacle 6-pos (GCT USB4135-GF-A) | 1 | — | — | — | — | — | — | — | — | — | 1 |
| RJ45 MagJack (Würth 7499111121A) | 1 | — | — | — | — | — | — | — | — | — | 1 |
| Battery Connector 5-pin Micro-Fit 3.0 (Molex 43650-0519) | 1 | — | — | — | — | — | — | — | — | — | 1 |
| | | | | | | | | | | | |
| 12 MHz Crystal SMD (Abracon ABM8-12.000MHz-B2-T / C9002) | — | — | — | — | — | — | — | — | — | 1 | 1 |
| 72°C SMD Thermal Cutoff (Bourns AC72ABD) | 1 | — | — | — | — | — | — | — | — | — | 1 |
| CR2032 Coin Cell Holder (Keystone 3034) | — | 1 | — | — | — | — | — | — | — | — | 1 |
| Würth 9774040151R M2.5 × 4.0mm SMT Brass Standoff (CM5 mount) | — | 4 | — | — | — | — | — | — | — | — | 4 |
| PoE ACF Isolation Transformer (Coilcraft POE600F-12LD) | 1 | — | — | — | — | — | — | — | — | — | 1 |
| EMI Common-Mode Choke (Würth WE-CMBNC 7448031002) | 2 | — | — | — | — | — | — | — | — | — | 2 |
| DM Filter Inductor 10 µH 15.5 A (Bourns SRP1265A-100M) | 1 | — | — | — | — | — | — | — | — | — | 1 |
| Power / RGB Rocker Switch (Marquardt 1800 series) | 1 | — | — | — | — | — | — | — | — | — | 1 |
| Tactile SMT Reset Switch (SKRPACE010) | 1 | — | — | — | — | — | — | — | — | — | 1 |
| Green SMD LED 0402 (Würth 150060VS75000 / C2286) | — | — | — | 2 | 6 | — | — | — | — | — | 6 |
| 6.35 mm Mono Switched Panel-Mount Jack Socket (Stecker) | — | — | — | 64 | 192 | — | — | — | — | — | 192 |
| DPDT 6-pin Momentary Keyboard Switch | — | — | — | 64 | 192 | — | — | — | — | — | 192 |
| 6.35 mm PCB Blade Terminal (Keystone 1285-ST) | — | — | — | 128 | 384 | — | — | — | — | — | 384 |
| CTS 219-4LPST — 4-pos DIP switch, 2.54mm THT | — | — | 1 | — | — | — | — | — | — | — | 1 |
| CTS 219-6LPSTR — 6-pos DIP switch, 2.54mm THT | — | — | 1 | — | — | 3 | 90 | — | — | — | 91 |

## 1. Critical Spares (MOQ Recommendations)

* **Bourns AC72 TCO:** Order 5 (MOQ) - (2x Spares).
* **Abracon ADCR-T02R7SA256MB (25F/2.7V) Supercap:** Order 10 — 6 required per build + 4 spare/test.
  Source via DigiKey (535-ADCR-T02R7SA256MB-ND) or Mouser (815-ADCRT02R7SA256MB). JLCPCB global sourcing only.
* **Samtec ERM8-040 (Gold, 80-pin):** Order 3 (MOQ) — Power Module J1, (1× Spare). Order separately from ERM8-020.
* **Samtec ERM8-020 (Gold, 40-pin):** Order 3 (MOQ) — Stator J8, (1× Spare). Poka-yoke pair with ERF8-020.
* **Samtec ERF8-040 (Gold, 80-pin):** Order 3 (MOQ) — Controller J1, (1× Spare).
* **Samtec ERF8-020 (Gold, 40-pin):** Order 3 (MOQ) — Controller J2, (1× Spare). Poka-yoke pair with ERM8-020.
* **0.1% Thin-Film Resistors:** Order 50 (MOQ) - (High attrition risk).

## 2. Common Passives

* **0.1uF Decoupling:** Samsung CL05B104KB5NNNC (0402).
* **10uF Bulk:** Samsung CL31B106KBHNNNE (1206).
* **10k Pull-ups:** Panasonic ERJ-3EKF1002V (0603).

## 3. Logic Passives  (0603 1% Thick-Film unless otherwise noted)

* **4.7kΩ:** 10 units (I2C-1 Telemetry Bus).
* **10kΩ:** 10 units (Reset, Battery Presence pull-ups to 3V3_ENIG & ROTOR_EN pull-down to GND).
* **22Ω:** 10 units (JTAG end-of-chain damping — Reflector R1 × 1; spares).
* **121kΩ:** 5 units (TPS2372-4 RMPS — MPS current set, R13).
* **301Ω:** 5 units (LTC3350 RICHARGE — charge current set, R11).
* **10mΩ / 5A (2512 Kelvin):** 3 build + 3 spares (PM R12 LTC3350 RSENSE + PM R23 INA219 U12 + Stator R1 INA219 U2; Bourns CSS2H-2512R-**R010**ELF).

## 3a. EMI Filter Passives

| Ref | Component | Part | Value | Package | Mouser Part # |
| :--- | :--- | :--- | :--- | :--- | :--- |
| L1 | EMI Primary CMC (broadband CM) | Würth WE-CMBNC 7448031002 | 2mH, 10A, nanocrystalline | THT 24×17×25mm | 710-7448031002 |
| L2 | EMI Secondary CMC (HF, >10MHz) | Würth WE-CMBNC 7448031002 (**replaces discontinued Laird CM5022**) | 2mH, 10A, nanocrystalline | THT 24×17×25mm | 710-7448031002 |
| L3 | EMI DM Pi-filter Inductor | Bourns SRP1265A-100M (replaces Würth 7447789100 — not in public catalog) | 10µH, 15.5A Isat, DCR 16.5mΩ | 13.5×12.5×6.2mm SMT ⚠️ footprint change | 652-SRP1265A-100M; alt: Farnell ~2741 in stock |
| C1, C4 | Pi-filter bulk cap (2× each) | Samsung CL32B226KAJNNNE | 22µF 25V X7R | 1210 | 187-CL32B226KAJNNNE |
| C2, C5 | Pi-filter mid-freq bypass (2× each) | Kemet C0805C105K5RACTU | 1µF 50V X7R | 0805 | 80-C0805C105K5R |
| C3, C6 | Pi-filter HF bypass (2× each) | Samsung CL05B104KB5NNNC | 100nF 50V X7R | 0402 | 187-CL05B104KB5NNNC |
| C7–C12 | Power IC bulk caps (U1 in/out, U2A in/out, U2B in/out) | Samsung CL32B226KAJNNNE | 22µF 25V X7R | 1210 | 187-CL32B226KAJNNNE |
| C13 | LDO input cap (U7 VIN) | Kemet C1206C106K3RACTU | 10µF 25V X7R | 1206 | 80-C1206C106K3R |
| C14 | LDO output cap (U7 VOUT) | Samsung CL32B226KAJNNNE | 22µF 25V X7R | 1210 | 187-CL32B226KAJNNNE |
| C15–C22 | IC VCC bypass (U3–U6, U8–U11) | Samsung CL05B104KB5NNNC | 100nF 50V X7R | 0402 | 187-CL05B104KB5NNNC |
| C26, C27 | IC VCC bypass for U6b and U6c (LM74700-Q1 OR-ing controllers — USB-C and Battery paths) | Samsung CL05B104KB5NNNC | 100nF 50V X7R | 0402 | 187-CL05B104KB5NNNC |
| C28 | SYNC SW-ringing low-pass filter (C_F1) | Kemet C0402C101K3RACAUTO | 100pF X7R 25V | 0402 | 80-C0402C101K3RAUTO |
| C29 | SYNC 180° phase delay capacitor (C_DLY) | Samsung CL10B223KB8WPNC | 22nF X7R 25V | 0603 | 187-CL10B223KB8WPNC |
| C30, C31 | VCC bypass for U13 and U14 (SN74LVC1G14DBVRQ1) | Samsung CL05B104KB5NNNC | 100nF 50V X7R | 0402 | 187-CL05B104KB5NNNC |
| C23 | MIC1555 timing cap (C_OSC) | Kemet C0805C105K5RACTU | 1µF 50V X7R | 0805 | 80-C0805C105K5R |
| C24 | TPS23730 soft-start cap (C_SS) | Samsung CL05B103KB5NNNC | 10nF 50V X7R | 0402 | 187-CL05B103KB5NNNC |

**Pi-filter performance summary (f_c = 10.5kHz):**

* −46dB DM attenuation at 150kHz (EN 55032 Class B lower edge) ✓
* −51dB at 200kHz (TPS23730 ACF switching frequency) ✓
* −63dB at 400kHz (LMQ61460AFSQRJRRQ1 buck switching frequency) ✓

## 4. High-Speed Interconnects

* **Samtec ERM8-040-05.0-S-DV-K-TR (Male, 80-pin):** Power Module J1 (Link-Alpha).
* **Samtec ERM8-020-05.0-S-DV-K-TR (Male, 40-pin):** Stator J8 (Link-Beta).
* **Samtec ERF8-040-05.0-S-DV-K-TR (Female, 80-pin):** Controller J1 (Link-Alpha).
* **Samtec ERF8-020-05.0-S-DV-K-TR (Female, 40-pin):** Controller J2 (Link-Beta).
* **Samtec ERM8-010-05.0-S-DV-K-TR (Male, 20-pin):** Rotor J3, Reflector J3, Extension J3. JLCPCB: C374877
* **Intel EPM240T100I5N:** 6 units (Encoder ×2 per board ×3 boards = 6).
* **Intel EPM570T100I5N:** 31 units (Stator ×1, Rotor ×1 per board ×30 boards = 30; total 31).
  Same TQFP-100 footprint as EPM240; 570 LEs required for startup-loaded cipher/reflector map registers.
  DigiKey: 544-2281-ND · Mouser: 989-EPM570T100I5N · JLCPCB: C27319.

## 4a. Encoder Board — Plugboard Jacks, Keyboard Switches & PCB Spade Terminals

| Ref | Component | Part / Description | Qty | Supplier | Supplier Ref / Notes |
| :--- | :--- | :--- | :--- | :--- | :--- |
| J1 (×64) | Stecker jack sockets | 6.35mm (¼″) mono switched panel-mount jack — Tip: ENC signal path; Switch (N/C): BT1–64 (same node as Tip; N/C contact shorts Switch→Sleeve when no plug present); Sleeve: BT65–128 (Encode Half / CPLD B input). **Already purchased.** | 64 | SaiBuy.Ltd (eBay) | eBay item 334364197440 — £1.66/unit (sold in packs of 3 for £4.99). [ebay.co.uk — SaiBuy.Ltd](https://www.ebay.co.uk/str/saibuyltd) |
| SW1-64 | Keyboard switches | DPDT 6-pin momentary push button — Pole 1 electrically active: COM1+NO1 → key-press to CPLD. Pole 2 pins soldered for mechanical key anchoring only (no electrical connection). NC1 not connected. Keys connect to keyboard Encoder board only; no direct switch connection to Lightboard. **Already purchased.** | 64 | gadgetkingdom (eBay) | Sold in packs of 2. Listing title: "Mechanical Push Button Switch DPDT 2 Pole 6 Pin 1 Position 2pcs". |
| BT1-64 | PCB blade terminals — ENC signal (Row 1) | Keystone 1285-ST — 6.35mm (0.250″) straight vertical PCB-mount male blade tab, through-hole. Accepts 6.35mm female crimp spade from jack Tip harness. | 64 | Mouser / DigiKey / JLCPCB | Mouser: 534-1285-ST · DigiKey: 36-1285-ST-ND · JLCPCB: C5370868 |
| BT65-128 | PCB blade terminals — Encode Half inputs / CPLD B encoder inputs (Row 2) | Keystone 1285-ST — same part. Wired to jack Sleeve (plugboard mode) or keyboard switch outputs (HID mode). | 64 | Mouser / DigiKey / JLCPCB | Mouser: 534-1285-ST · DigiKey: 36-1285-ST-ND · JLCPCB: C5370868 |

**Notes:**

* **Plugboard jacks (J1 ×64):** mount in the plugboard panel. Each jack connects via a 2-wire harness (Tip → BT1–64;
  Sleeve → BT65–128 Encode Half). Switch (N/C) is on the same node as Tip (BT1–64); it shorts Switch→Sleeve when no
  plug is inserted. Rows 1–2 (BT1–128).
* **Keyboard switches (SW1-64):** mount in the keyboard panel. In HID mode each switch output wires to BT65–128
  (Row 2, Encode Half). Pole 2 pins are mechanically soldered for physical anchoring — no electrical connection.
  Keys connect to the keyboard Encoder board only; no direct switch wiring to the Lightboard.
* **Total PCB blade terminals: 128** — two rows of 64, all Keystone 1285-ST.
* Stecker patch cables (plugboard) use 6.35mm mono jack plugs (TS) — not included in BOM; customer-supplied.

## 4b. Stator Board — DIP Switch Configuration Components

| Ref | Component | Value | Package | Mouser Part # | DigiKey Part # | JLCPCB Part # |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| R16–R19 | SW1 pull-down resistors (×4) | 10kΩ 1% 0603 | 0603 | 667-ERJ-3EKF1002V | P10.0KBYCT-ND | C25804 |
| SW1 | Routing config DIP switch | CTS 219-4LPST 4-pos 2.54mm THT | THT | 774-219-4LPST | CT2064-ND | C128947 |
| R20–R25 | SW2 pull-down resistors (×6) | 10kΩ 1% 0603 | 0603 | 667-ERJ-3EKF1002V | P10.0KBYCT-ND | C25804 |
| SW2 | Reflector map selector DIP switch | CTS 219-6LPSTR 6-pos 2.54mm THT | THT | 774-2196LPSTR | 119-219-6LPSTRCT-ND | C2842671 |

See `Stator/Design_Spec.md §3 DIP Switch Configuration (SW1)` for the full 16-configuration routing
table and placement requirements.

## 5. Controller Specifics

* **CM5 Module:** Raspberry Pi SC1180 (8GB/32GB/Wireless).
* **Stacked USB 3.0:** Molex 48406-0003 (THT Right-Angle).
* **Full HDMI:** TE Connectivity 2007435-1 (THT Type-A).

### 5.1. Controller User I/O Protection

* **TPS2065CDBVR:** USB Power Distribution Switch (SOT-23-5) (1.6A Limit).
* **AP2331W-7:** HDMI Current Limiter (SOT-23-5) (50mA Limit).
* **TPD4E05U06QDQARQ1:** 4-channel ESD array, U-DFN-10. DigiKey: `296-40696-1-ND`; Mouser: `595-PD4E05U06QDQARQ1`; JLCPCB: `C81353`.

### Controller Board — RTC Battery Circuit

> **Note:** C6 (100nF X7R 0402, Samsung CL05B104KB5NNNC) uses the common 100nF 0402 passive from
> §2 Common Passives — not duplicated here.

| Ref | Component | Description | Qty | Supplier | Part Number |
| :--- | :--- | :--- | :--- | :--- | :--- |
| BT1 | Keystone 3034 | CR2032 THT horizontal coin cell holder — RTC backup battery for CM5 MXL7704 PMIC | 1 | Mouser: 534-3034 / DigiKey: 36-3034-ND | Keystone 3034 |
| D1 (CTRL) | BAT54 (Diotec) | SOT-23 Schottky — VBAT (Pin 95) charge blocking diode (prevents PMIC from charging CR2032) | 1 | Mouser: 637-BAT54 / DigiKey: 4878-BAT54CT-ND / JLCPCB: C25835522 | BAT54 |
| — | Renata CR2032 | CR2032 3V coin cell (not fitted at PCB assembly — installed at commissioning) | 1 | Mouser: 614-CR2032 / DigiKey: P189-ND | Renata CR2032 |

## 6. Backplane & Extension Components

* **16-pin Inter-Board Link (Adam Tech BHR-16-VUA, 2×8, 2.54mm):** Used for J7 (Extension/Reflector link) on Stator, Extension (J7/J8), and Reflector (J4). Correct connector for TTD_RETURN path.
* See individual board BOMs: Rotor/Board_Layout.md, Stator/Board_Layout.md, Extension/Board_Layout.md, Reflector/Board_Layout.md for authoritative connector part numbers.
* **Copper Shielding Tape:** 50mm (2.0") Conductive Adhesive (Manual cable wrap).

## 7. Power & Telemetry Sensors

* **INA219AIDR:** 2 units — PM U12 @ I²C 0x40 (5V\_MAIN current monitoring); Stator U2 @ I²C 0x45 (rotor telemetry).
* **20mΩ 1206 Shunt (ERJ-6ENF20R0V):** 0 units — retired from Stator; replaced by CSS2H-2512R-R010ELF.
* **10mΩ 2512 Kelvin Shunt (CSS2H-2512R-R010ELF):** 3 build + 3 spares — PM R12 (LTC3350 RSENSE) + PM R23 (INA219 U12, 0x40) + Stator R1 (INA219 U2, 0x45).

## 8. Power Module — PoE Subsystem

| Ref | Component | Part Number | Value / Notes | Supplier | Supplier Part # | Unit Price (1-off) | Unit Price (volume) |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| U9 | PoE PD Interface (Type 4) | TPS2372-4RGWR | TI VQFN-20; 802.3bt Type 4, external hotswap, up to 90W | Mouser | 595-TPS2372-4RGWR | ~£3.50 | ~£2.00 |
| U10 | PoE ACF DC-DC Controller | TPS23730RMTR | TI WQFN-20; ACF topology; PSR mode; 12V output set by POE600F-12LD turns ratio; VS pin to aux winding | Mouser | 595-TPS23730RMTR | ~£3.50 | ~£2.00 |
| T2 | PoE ACF Isolation Transformer | **Coilcraft POE600F-12LD** | 60W; 12V out; 36–72V in; 200kHz; ACF topology; ≥1500Vrms; SMT; RoHS | Coilcraft Direct | POE600F-12LD | **£3.54** | **~£1.86** |
| R13 | TPS2372-4 RMPS (MPS current set) | 121kΩ 1% Thick-Film | 121kΩ E96; IMPS = VIMPS/RMPS = 1.205V/121kΩ = 9.96mA (Type 4 MPS auto-stretch) | Mouser | 667-ERJ-3EKF1213V | ~£0.10 | ~£0.03 |

**Notes:**

* T2 is an **off-the-shelf catalogue part** — order direct from [coilcraft.com](https://www.coilcraft.com). 668 units confirmed in stock (Coilcraft Direct as of 2026-04-03).
* TPS23730 operates in **PSR (Primary-Side Regulation) mode** using the auxiliary winding of the POE600F-12LD. No external TL431 or optocoupler required.
* TPS2372-4 uses **Autoclass** for automatic 4-event IEEE 802.3bt Type 4 classification; no external RCLASS resistor required. R13 (RMPS) programs MPS pulse current only.
* OR-ing priority: TPS2372-4 `/PG` signal drives LM74700-Q1 enable on the USB-C path to enforce PoE source priority.

## 9. Power Module — IC & Connector BOM (Multi-Distributor)

> **Legend:** ✓ = confirmed from distributor search · ~ = derived from manufacturer prefix convention · ⚠️ = part number issue flagged · — = not stocked / THT not assembled

| Designator | Part | Package | Mouser # | DigiKey # | JLCPCB # | Notes |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| U3 | LTC3350EUHF#PBF | QFN-38 5×7 | 584-LTC3350EUHF#PBF ✓ | 505-LTC3350EUHF#PBF-ND ✓ | C580711 | ~4.5k in stock Mouser (tube). DigiKey 505-prefix confirmed. JLCPCB C580711 confirmed. |
| U5 | STUSB4500LQTR | QFN-24 4×4 | 511-STUSB4500LQTR | 497-STUSB4500LQCT-ND | C506650 | Primary PN: STUSB4500LQTR (lower Iq ~160µA). JLCPCB C506650 confirmed L-variant in stock. If OOS, use STUSB4500QTR as alternative (non-L variant, ~210µA Iq, pin-compatible). |
| U6 | ~~LM74700-Q1DCKR~~ → **LM74700QDBVRQ1** | SOT-23-6 (DBV) | 595-LM74700QDBVRQ1 | **296-LM74700QDBVRQ1CT-ND** ✓ | C2941042 | LM74700QDBVRQ1 (DBV=SOT-23-6 package, not DCK/SC70). DigiKey 35k+ in stock. Alt T&R Mouser PN: 595-LM74700QDBVTQ1 (pin-compatible). |
| U8 | MCP121T-450E/LB | SC70-3 | 579-MCP121T-450E/LB | **MCP121T-450E/LBCT-ND** ✓ | C52146050 | DigiKey 2.3k in stock @ $0.53/1. SC70-3 = compact 3-pin package. Microchip prefix 579-. JLCPCB lists with TP prefix on MPN but is the same device. |
| U1 | TPS259804ONRGER | VQFN-24 (RGE) | 595-TPS259804ONRGER | 296-TPS259804ONRGERCT-ND | C2878936 | 16.9V silicon-fixed OVLO variant. OVLO set in silicon — no external R. R3 repurposed as R_ILIM (210 Ω). PNs confirmed. |
| U2A/U2B | LMQ61460AFSQRJRRQ1 | VQFN-HR (RJR) 14-pin 4×3.5mm | 595-Q61460AFSQRJRRQ1 | 296-LMQ61460AFSQRJRRQ1CT-ND | C1518767 | AEC-Q100 automotive-qualified (Q1), VQFN-HR RJR 14-pin 4×3.5mm. ✓ |
| U4 | TPS25751DREFR | WQFN-38 6×4mm | 595-TPS25751DREFR | 296-TPS25751DREFRCT-ND | C30169739 | ✅ Replaces NRND TPS25750DRCR (see DEC-012). PD3.1 certified (USB-IF TID#10306). Package: WQFN-38 6×4mm (note: different from TPS25750 QFN-28). |
| U7 | TPS75733KTTRG3 | TO-263 (KTT) 5-pin 10.16×15.24mm | 595-TPS75733KTTRG3 | 296-50559-1-ND | C3749924 | Fixed 3.3V, TO-263 KTT 5-pin. Active-LOW EN (EN LOW = enabled). ✓ |
| U9 | TPS2372-4RGWR | VQFN-20 | **595-TPS2372-4RGWR** (provided) | **296-52795-1-ND** ✓ | C470955 | DigiKey stock verified. $3.09/1. VQFN-20 per TI. |
| U10 | TPS23730RMTR | WQFN-20 | **595-TPS23730RMTR** ✓ | **296-TPS23730RMCT-ND** ✓ | C3189530 | ACF PoE+ DC-DC controller; PSR mode; 12V output; WQFN-20 package. ✅ Resolved (see §9.0 item 2). |
| D2 | TPD2E2U06DRLR | SOT-553 (DRL) | **595-TPD2E2U06DRLR** ✓ | **296-38361-1-ND** ✓ | C1972959 | DigiKey 1.4k in stock @ $0.41/1. Dual-channel SMBus ESD, 5.5V. Part confirmed to exist. Farnell stocked (3116500). |
| J2 | Würth 7499111121A | THT RJ45 | **710-7499111121A** ✓ | **1297-1070-5-ND** ✓ | C5523983 | Mouser ~191, DigiKey ~879 in stock. ~$8.41/1 (Mouser), ~$8.41/1 (DigiKey). Farnell out of stock. JLCPCB C5523983 — hand-place or pre-fit. |
| J3 | Molex 0436500519 (43650-0519) | THT Micro-Fit 3.0 | 538-43650-0519 | WM14587-ND | C563849 | Full Molex PN: 0436500519; short form 43650-0519. 5-circuit, 1-row, gold contacts, board lock, 3mm pitch. Farnell ~1143 in stock. JLCPCB C563849 confirmed. |
| J4 | GCT USB4135-GF-A | SMT vertical 8.94×3.5mm | 640-USB4135-GF-A | 2073-USB4135-GF-ACT-ND | C5438410 | 6-position USB Type-C receptacle (power only), 5A VBUS, CC1/CC2 included. Connects to STUSB4500 (U5) for 15V PD negotiation. JLCPCB C5438410. |
| Q1, Q2, Q3 | TI CSD17483F4T (×3) | SON-8 3.3×3.3mm | 595-CSD17483F4T | 296-37781-1-ND | C2871105 | N-ch MOSFET, 30V, 10A, 8.4mΩ. Driven by LM74700-Q1 (U6) for triple-input ideal-diode OR-ing (PoE / USB-C / Battery). One per input path. ⚠️ Verify U6 instance count — LM74700-Q1 controls one FET per IC; three inputs may require three U6 instances at schematic capture. |
| R14, R15 | Panasonic ERA-3ARB series | 0603 0.1% Thin-Film | See PN below | See PN below | — | BACKUP pin voltage divider for LTC3350 (U3). R14=28.7kΩ (ERA-3ARB2872V, Mouser 667-ERA-3ARB2872V, DigiKey P28.7KBYCT-ND). R15=10.0kΩ (ERA-3ARB1002V, Mouser 667-ERA-3ARB1002V, DigiKey P10.0KBYCT-ND). Sets BACKUP trigger at 4.644V (above MCP121T 4.50V — LTC3350 activates first, keeping PWR_GD stable). |
| U11 | MIC1555YM5-TR | SOT-23-5 | 579-MIC1555YM5TR | MIC1555YM5-TRCT-ND | C431119 | CMOS timer IC (Microchip). 1Hz hardware status LED oscillator. R16=10kΩ (ERJ-3EKF series), R17=715kΩ (ERJ-3EKF7153V, Mouser 667-ERJ-3EKF7153V), C23=1µF (same Kemet C0805C105K5RACTU as C2/C5). |
| U15 | MIC1555YM5-TR | SOT-23-5 | 579-MIC1555YM5TR | MIC1555YM5-TRCT-ND | C431119 | CMOS timer IC (Microchip). Monostable one-shot for hardware PWR_BUT shutdown. t=1.1×R28×C32=3.01s. R28=274kΩ (ERJ-3EKF2743V), C32=10µF 16V X7R (CL10B106KA8NNNC), C33=100nF bypass cap. |
| R18–R21 | RJ45 Bob Smith termination resistors (×4) | 75Ω ±1% 0402 | 0402 | 667-ERJ-2RKF75R0X | P75.0LCT-ND | C413061 |
| C25 | RJ45 Bob Smith termination capacitor (⚠️ Y1-class 0402 is rare; 100V X7R acceptable proxy for EMC transient margin — Ethernet ESD discharge path to chassis) | 10nF 100V X7R 0402 | 0402 | 80-C0402C103J1RAUTO | 399-C0402C103J1RACAUTOCT-ND | C19862706 |

### 9.0. Part Number Issues Requiring Action

1. **U6** — Replace `LM74700-Q1DCKR` with **`LM74700QDBVRQ1`** everywhere in schematics and BOM. The DCK (SC70) package does not exist for this part; DBV (SOT-23-6) is the correct package.
2. **U10** — ✅ Resolved: TPS23730 correct package is **RMTR (WQFN-20)** — MPN updated to `TPS23730RMTR` in BOM and Design_Spec.
3. **U1** — Updated to `TPS259804ONRGER` (16.9V silicon-fixed OVLO VQFN-24 variant). Mouser/DigiKey/JLCPCB PNs confirmed. R3 repurposed as R_ILIM = 210 Ω (ERJ-3EKF2100V).
4. **U4** — Replaced with TPS25751DREFR (WQFN-38 6×4mm). See DEC-012. Package differs from TPS25750 QFN-28; KiCad symbol/footprint to be created at schematic capture.

## 10. Suppliers

Reference information for placing orders with key component suppliers.

| # | Supplier | Role | Website | Notes |
| :--- | :--- | :--- | :--- | :--- |
| S01 | **Mouser Electronics** | Global distributor (primary) | [mouser.co.uk](https://www.mouser.co.uk) | Free next-day delivery on orders over £50. Wide TI/ADI/Microchip stock. Use part numbers from `Mouser Part #` column in board BOM tables. |
| S02 | **Farnell** | Global distributor (secondary UK) | [uk.farnell.com](https://uk.farnell.com) | Same-day dispatch for most stock lines. Good for Samtec, Würth, Bourns, Coilcraft. |
| S03 | **DigiKey** | Global distributor (USA-based, fast to UK) | [digikey.co.uk](https://www.digikey.co.uk) | Good for ADI (LTC3350), TI (low-MOQ), STMicroelectronics (STUSB4500). |
| S04 | **Coilcraft** | Transformer / inductor manufacturer | [coilcraft.com](https://www.coilcraft.com) | Order T2 (POE600F-12LD) direct from Coilcraft at coilcraft.com/en-us/. Minimum order 1 unit. Sample requests available. UK-friendly shipping. |
| S05 | **Texas Instruments** | IC manufacturer (TI store) | [ti.com/store](https://www.ti.com/store) | For TI parts (TPS2372-4, TPS23730, TPS25980, LMQ61460AFSQRJRRQ1, LM74700-Q1, TPS25751DREFR, TPS75733). Samples available via ti.com. |
| S06 | **Analog Devices (ADI)** | IC manufacturer | [analog.com](https://www.analog.com) | For LTC3350 supercap manager. Samples available. |
| S07 | **STMicroelectronics** | IC manufacturer | [st.com](https://www.st.com) | For STUSB4500 USB-C sink controller. Samples and eval kits available. |
| S08 | **Samtec** | Connector manufacturer | [samtec.com](https://www.samtec.com) | For ERF8/ERM8 BtB connectors (80-pin Link-Alpha, 40-pin Link-Beta). Order direct or via Farnell/Mouser. Min order typically 3 units. |
| S09 | **Würth Elektronik** | Passive / connector manufacturer | [we-online.com](https://www.we-online.com) | For RJ45 MagJack (7499111121A), EMI chokes (WE-CMBNC). Order via Farnell, Mouser, or direct. |
| S10 | **Molex** | Connector manufacturer | [molex.com](https://www.molex.com) | For battery connector (43650-0519 Micro-Fit 3.0, 5-pin vertical THT). Order via Mouser or DigiKey. |
| S11 | **Abracon** | Passive component manufacturer | [abracon.com](https://www.abracon.com) | For ADCR-T02R7SA256MB 25F/2.7V supercaps. Available from DigiKey (935 in stock) and Mouser. JLCPCB global sourcing only. |
| S12 | **JLCPCB** | PCB fabrication & SMT assembly | [jlcpcb.com](https://www.jlcpcb.com) | Primary PCB manufacturer. Use JLCPCB Part # column for SMT assembly BOM upload. Stackup: JLC04161H-7628 (4-layer, 2oz) for JDB, Stator, Encoder, Rotor, Reflector, Extension; JLC06161H-2116 (6-layer, 2oz) for Power Module and Controller. |
| S13 | **Newark (Avnet)** | Global distributor (UK stock) | [newark.com](https://www.newark.com) | Good for Würth passives with immediate UK stock. Note: WE-CMBNC 7448031002 is not stocked by Newark/Avnet — use Mouser (710-7448031002), DigiKey (732-5584-ND), or JLCPCB (C1519839). Same-group as Farnell/element14. |

---

## 11. Datasheet Links

Product page links for all major components for design review and procurement verification.

| Ref | Part / Description | Manufacturer | Local Datasheet |
| :--- | :--- | :--- | :--- |
| U1 | TPS259804ONRGER — eFuse 16.9V silicon-fixed OVLO | Texas Instruments | [TPS25980-datasheet.pdf](../Datasheets/TPS25980-datasheet.pdf) |
| U2A, U2B | LMQ61460AFSQRJRRQ1 — 6A Sync Buck (AEC-Q100) | Texas Instruments | [lmq61460-q1-datasheet.pdf](../Datasheets/lmq61460-q1-datasheet.pdf) |
| U3 | LTC3350EUHF#PBF — Supercap Manager / Charger / Backup | Analog Devices | [ltc3350-datasheet.pdf](../Datasheets/ltc3350-datasheet.pdf) |
| U4 | TPS25751DREFR — USB PD 3.1 DRP Controller | Texas Instruments | [tps25751-datasheet.pdf](../Datasheets/tps25751-datasheet.pdf) |
| U5 | STUSB4500LQTR — USB-C Sink PD Controller | STMicroelectronics | [stusb4500l-datasheet.pdf](../Datasheets/stusb4500l-datasheet.pdf) |
| U6 | LM74700QDBVRQ1 — Ideal-Diode OR-ing Controller | Texas Instruments | [lm74700-q1-datasheet.pdf](../Datasheets/lm74700-q1-datasheet.pdf) |
| U7 | TPS75733KTTRG3 — 3.3V 3A LDO (3V3_ENIG) | Texas Instruments | [tps757-datasheet.pdf](../Datasheets/tps757-datasheet.pdf) |
| U8 | MCP121T-450E/LB — 4.50V Voltage Supervisor | Microchip Technology | [MCP121-datasheet.pdf](../Datasheets/MCP121-datasheet.pdf) |
| U9 | TPS2372-4RGWR — IEEE 802.3bt PoE PD Controller | Texas Instruments | [tps2372-datasheet.pdf](../Datasheets/tps2372-datasheet.pdf) |
| U10 | TPS23730RMTR — ACF PoE+ DC/DC Controller | Texas Instruments | [tps23730-datasheet.pdf](../Datasheets/tps23730-datasheet.pdf) |
| U11, U15 | MIC1555YM5-TR — CMOS Timer / LED Oscillator | Microchip Technology | [MIC1555-datasheet.pdf](../Datasheets/MIC1555-datasheet.pdf) |
| U12 (PM), U2 (STA) | INA219AIDR — Zero-Drift Power Monitor | Texas Instruments | [INA219-datasheet.pdf](../Datasheets/INA219-datasheet.pdf) |
| U13, U14 | SN74LVC1G14DBVRQ1 — Single Schmitt Inverter | Texas Instruments | [sn74lvc1g14-q1-datasheet.pdf](../Datasheets/sn74lvc1g14-q1-datasheet.pdf) |
| U2 (CTL) | TPS2065CDBVR — USB Power Switch 1.6A | Texas Instruments | [tps2065c-datasheet.pdf](../Datasheets/tps2065c-datasheet.pdf) |
| U3 (CTL) | AP2331W-7 — HDMI Current Limiter | Diodes Inc. | [AP2331-datasheet.pdf](../Datasheets/AP2331-datasheet.pdf) |
| D3, D4, D5 (PM); U4 (CTL) | TPD4E05U06QDQARQ1 — 4-Channel ESD Array | Texas Instruments | TBD — datasheet to be added |
| D2 | TPD2E2U06DRLR — Dual 5.5V SMBus ESD | Texas Instruments | [tpd2e2u06-datasheet.pdf](../Datasheets/tpd2e2u06-datasheet.pdf) |
| D1 | TPD1E10B06DYARQ1 — Single-ch 10V TVS ESD, SOD-523 | Texas Instruments | [tpd1e10b06-q1-datasheet.pdf](../Datasheets/tpd1e10b06-q1-datasheet.pdf) |
| U1 (EXT), U5 (JDB) | SN74LVC2G125DCUR — Dual 3-State Buffer | Texas Instruments | [sn74lvc2g125-datasheet.pdf](../Datasheets/sn74lvc2g125-datasheet.pdf) |
| U1 (JDB) | FT232HL-REEL — USB 2.0 MPSSE Bridge | FTDI | [FT232H-datasheet.pdf](../Datasheets/FT232H-datasheet.pdf) |
| U1 (ENC) | EPM240T100I5N — Intel MAX II CPLD 240 LE | Intel (Altera) | [Intel_max2_cpld-handbook.pdf](../Datasheets/Intel_max2_cpld-handbook.pdf) |
| U1 (STA/ROT) | EPM570T100I5N — Intel MAX II CPLD 570 LE | Intel (Altera) | [Intel_max2_cpld-handbook.pdf](../Datasheets/Intel_max2_cpld-handbook.pdf) |
| U2/U3/U4 (ROT) | FDC2114RGHR — 4-ch Capacitive Sensor IC ⚠️ MOQ 4500 at distributors; MOQ 2 at JLCPCB | Texas Instruments | [fdc2112-datasheet.pdf](../Datasheets/fdc2112-datasheet.pdf) |
| U1 (CTL) | CM5 — Raspberry Pi Compute Module 5 | Raspberry Pi Ltd | [RPi-cm5-datasheet.pdf](../Datasheets/RPi-cm5-datasheet.pdf) |
| Q1–Q3 | CSD17483F4T — N-ch MOSFET 30V/10A, SON-8 | Texas Instruments | [csd17483f4-datasheet.pdf](../Datasheets/csd17483f4-datasheet.pdf) |
| Q4, Q5 | BSS138 (onsemi) — N-ch Logic MOSFET 50V, SOT-23 | onsemi | [BSS138-onsemi-datasheet.pdf](../Datasheets/BSS138-onsemi-datasheet.pdf) |
| BAT54 | BAT54 (Diotec) — Schottky Diode, SOT-23 | Diotec | [bat54-diotec-datasheet.pdf](../Datasheets/bat54-diotec-datasheet.pdf) |
| T2 | POE600F-12LD — Active Clamp Flyback Transformer | Coilcraft | [coilcraft.com/POE600F](https://www.coilcraft.com/en-us/products/power-magnetics/power-transformers/poe-transformers/poe600f/) |
| L1, L2 | WE-CMBNC 7448031002 — Nanocrystalline CMC | Würth Elektronik | [we-online.com](https://www.we-online.com/en/components/products/CMBNC) |
| L3 | SRP1265A-100M — 10µH 14A Power Inductor | Bourns | [bourns.com/SRP1265A](https://www.bourns.com/products/inductors/power-inductors/product/SRP1265A) |
| R12 / R_SENSE | CSS2H-2512R-R010ELF — 10mΩ Kelvin Shunt | Bourns | [bourns.com/CSS2H](https://www.bourns.com/products/resistors/current-sense-resistors/product/CSS2H) |
| J2 (PM) | 7499111121A — GbE RJ45 MagJack with LEDs | Würth Elektronik | [Wurth-7499111121A-datasheet.pdf](../Datasheets/Wurth-7499111121A-datasheet.pdf) |
| J3 (PM) | 43650-0519 — Micro-Fit 3.0, 5-pin Vertical THT | Molex | [molex.com/436500519](https://www.molex.com/en-us/products/part-detail/436500519) |
| J4 (PM) | USB4135-GF-A — USB Type-C SMT Receptacle, 5A | GCT | [usb4135-datasheet.pdf](../Datasheets/usb4135-datasheet.pdf) |
| J3 (CTL) | 48406-0003 — USB 3.0 Type-A Dual-Stack | Molex | [Molex-48406-0003-datasheet.pdf](../Datasheets/Molex-48406-0003-datasheet.pdf) |
| J4 (CTL) | 2007435-1 — HDMI Type-A Full-Size | TE Connectivity | [TE-2007435-1-datasheet.pdf](../Datasheets/TE-2007435-1-datasheet.pdf) |
| J\_CM5\_A/B (CTL) | 10164227-1004A1RLF — 100-pin B2B SO-DIMM Socket 4.0mm | Amphenol | [Amphenol-10164227-1004A1RLF-datasheet.pdf](../Datasheets/Amphenol-10164227-1004A1RLF-datasheet.pdf) |
| J1 (PM) + Rotor/Stator/Reflector/Extension ERM8 | ERM8-040/020/010/005 — 0.8mm-pitch BtB Male Headers | Samtec | [erm8-xxx-xx.x-xxx-dv-xxxx-xx-mkt-datasheet.pdf](../Datasheets/erm8-xxx-xx.x-xxx-dv-xxxx-xx-mkt-datasheet.pdf) |
| J1/J2 (CTL) + Rotor/Stator/Reflector/Extension ERF8 | ERF8-040/020/010/005 — 0.8mm-pitch BtB Female Sockets | Samtec | [erf8-xxx-xx.x-xxx-dv-xxxx-xx-mkt-datasheet.pdf](../Datasheets/erf8-xxx-xx.x-xxx-dv-xxxx-xx-mkt-datasheet.pdf) |
| C_SC1–6 (PM) | ADCR-T02R7SA256MB — 25F 2.7V Supercapacitor, THT Radial Can | Abracon | [ADCR-T02R7S-datasheet.pdf](../Datasheets/ADCR-T02R7S-datasheet.pdf) |
| SW2 (STA), SW1/SW2/SW3 (ROT) | 219-6LPSTR — 6-position DIP switch, 2.54mm THT | CTS | [CTS-Switches-DIP-219-Series-Datasheet.pdf](../Datasheets/CTS-Switches-DIP-219-Series-Datasheet.pdf) |
