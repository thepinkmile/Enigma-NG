# Enigma-NG Consolidated BOM & Spares

**Status:** Draft — pending schematic freeze
**Project:** Enigma-NG
**Author:** Izzyonstage & GitHub Copilot
**Version:** v.0.1.0
**Last Updated:** 2026-04-26

## Overview

This is the consolidated Bill of Materials for all boards and modules in the Enigma-NG system.
It covers critical spares, common passives, high-speed interconnects, power components, and supplier
reference information. For per-board BOM notes and design constraints, refer to each board's
individual `Design_Spec.md` file.

> **Review Policy:** Parts marked 🔒 have been confirmed by the project owner.
> Do not modify 🔒-marked items without owner approval.
>
## Component Usage Summary

This table shows the component count per board instance and system-wide totals, accounting for
×6 Encoder Modules and ×30 Rotor boards in the complete system. The EXT column shows per-board
quantities for one Extension board; Rev A uses ×1 Extension board, while the full 30-rotor build
requires ×5 Extension boards (one between each pair of 5-rotor groups). System Total reflects
the Rev A single-Extension configuration unless otherwise noted, and also includes the shared
two-module Rev A Actuation Module passive support-part population frozen in §4c where the common
summary rows below use the same sourced part. Active Encoder Module PCB
populations are common across all six modules.
Variant-dependent Rotor-only populations may use range-valued totals where the N=26 vs. N=64 build
mix changes whether a part is stuffed. When a variant-specific rotor part is populated, it is
fitted in complete rotor sets of **5, 10, 15, 20, 25, or 30** boards — never as a single loose
rotor. Assembly-level plugboard jacks and keyboard switches are listed in §4a instead of this
board matrix.

| MPN / Description | PM | CTL | STA | ENC (×1) | ENC Total (×6) | ROT (×1) | ROT Total (×30) | REF | EXT | JDB | SBD | System Total |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| EPM570T100I5N — Intel MAX II CPLD (TQFP-100; 570 LEs; common part across Encoder, Stator, and Rotor boards) | — | — | 1 | 1 | 6 | 1 | 30 | — | — | — | — | 37 |
| INA219AIDR — Zero-Drift Power Monitor (SOIC-8) | 1 | — | 1 | — | — | — | — | — | — | — | — | 2 |
| PCA9534APWR — I²C GPIO Expander 8-bit (TSSOP-16) | 1 | — | — | — | — | — | — | — | — | — | — | 1 |
| FDC2114RGHR — 4-ch Capacitive Sensor IC, U2 Track A (bits[5:3] N=64; bits[3:0] N=26), Board A, addr 0x2A (16-VQFN) | — | — | — | — | — | 1 | 30 | — | — | — | — | 30 |
| FDC2114RGHR — 4-ch Capacitive Sensor IC, U3 STGC bit[4] (N=26 only; NOT POPULATED for N=64), Board A, addr 0x2B (16-VQFN) | — | — | — | — | — | 0 / 1 | 5-30 (sets of 5) | — | — | — | — | 5-30 (sets of 5, N=26 builds only) |
| FDC2114RGHR — 4-ch Capacitive Sensor IC, U4 Track B (bits[2:0] N=64 only; NOT POPULATED for N=26), Board B, addr 0x2B (16-VQFN) | — | — | — | — | — | 0 / 1 | 5-30 (sets of 5) | — | — | — | — | 5-30 (sets of 5, N=64 builds only) |
| SN74LVC2G125DCUR — Dual 3-State Buffer (VSSOP-8) | — | — | — | — | — | — | — | — | 1 | 1 | — | 2 |
| 74HC157PW-Q100,118 — Automotive quad 2:1 mux (TSSOP-16) | — | — | 2 | — | — | — | — | — | — | — | — | 2 |
| NL27WZ14DFT2G-Q — Automotive Dual Schmitt Inverter (SC-88; PM U13/U14 SYNC delay chain + U17 SW2 signal conditioner) | 3 | — | — | — | — | — | — | — | — | — | — | 3 |
| FT232HL-REEL — USB 2.0 to MPSSE Bridge (QFN-56) | — | — | — | — | — | — | — | — | — | 1 | — | 1 |
| CM5 — Raspberry Pi Compute Module 5 | — | 1 | — | — | — | — | — | — | — | — | — | 1 |
| TPS75733KTTRG3 — 3.3 V LDO Regulator (TO-263 KTT 5-pin) | 1 | — | — | — | — | — | — | — | — | — | — | 1 |
| TPS259804ONRGER — eFuse / Hot-Swap Controller (VQFN-24) | 1 | — | — | — | — | — | — | — | — | — | — | 1 |
| LMQ61460AFSQRJRRQ1 — 5 V Synchronous Buck Converter (VQFN-HR RJR 14-pin 4×3.5mm) | 2 | — | — | — | — | — | — | — | — | — | — | 2 |
| LTC3350EUHF#PBF — Supercapacitor Manager (QFN-38) | 1 | — | — | — | — | — | — | — | — | — | — | 1 |
| TPS25751DREFR — USB PD 3.1 DRP Controller (WQFN-38) | 1 | — | — | — | — | — | — | — | — | — | — | 1 |
| STUSB4500LQTR — USB-C Sink Controller (QFN-24) | 1 | — | — | — | — | — | — | — | — | — | — | 1 |
| LM74700QDBVRQ1 — Ideal-Diode OR-ing Controller (SOT-23-6) | 3 | — | — | — | — | — | — | — | — | — | — | 3 |
| MCP121T-450E/LB — 4.5 V Voltage Supervisor (SC70-3) | 1 | — | — | — | — | — | — | — | — | — | — | 1 |
| TPS2372-4RGWR — PoE PD Interface Type 4 (VQFN-20) | — | 1 | — | — | — | — | — | — | — | — | — | 1 |
| TPS23730RMTR — PoE ACF DC-DC Controller (WQFN-20) | — | 1 | — | — | — | — | — | — | — | — | — | 1 |
| MIC1555YM5-TR — CMOS Timer / LED Oscillator (SOT-23-5) | 2 | — | — | — | — | — | — | — | — | — | — | 2 |
| TPS2065C — USB Power Distribution Switch (SOT-23-5) | — | 1 | — | — | — | — | — | — | — | — | — | 1 |
| AP2331W — HDMI Current Limiter (SOT-23-5) | — | 1 | — | — | — | — | — | — | — | — | — | 1 |
| UNSOURCED — Stator external signal-line TVS / ESD protection required by `Stator/Design_Spec.md §8` (`J10` / `J12` / `J13`; exact protected nets, device count, working voltage, package, and MPN owner-selected) | — | — | TBD | — | — | — | — | — | — | — | — | TBD |
| UNSOURCED — Extension exposed signal-line TVS / ESD protection required by `Extension/Design_Spec.md §5` (exact protected nets, device count, working voltage, package, and MPN owner-selected) | — | — | — | — | — | — | — | — | TBD | — | — | TBD |
| TPD4E05U06QDQARQ1 — 4-Channel ESD Array (U-DFN-10) | 1 | 3 | — | — | — | — | — | — | — | — | — | 4 |
| TPD1E10B06DYARQ1 — Single-Channel ESD (SOD-523) | 1 | — | — | — | — | — | — | — | — | — | — | 1 |
| TPD2E2U06DRLR — Dual-Channel SMBus ESD (SOT-553) | 1 | — | — | — | — | — | — | — | — | — | — | 1 |
| CSD17483F4T — 30 V 10 A N-ch OR-ing MOSFET (SON-8) | 3 | — | — | — | — | — | — | — | — | — | — | 3 |
| BSS138 — 50 V N-ch Logic-Level MOSFET (SOT-23) | 7 | — | — | — | — | — | — | — | — | — | 6 | 13 |
| SN74LVC1G175DBVR — Single D-type flip-flop with async clear, 1.65-5.5V, 3.3V logic compatible (PM SW2 shutdown latch) | 1 | — | — | — | — | — | — | — | — | — | — | 1 |
| SN74LVC1G08DBVR — Single 2-input AND gate (SOT-23-5; PM SW2 red blink gate + Stator reset/apply gate) | 1 | — | 1 | — | — | — | — | — | — | — | — | 2 |
| BAT54 — Schottky Diode (SOT-23) | 2 | 1 | — | — | — | — | — | — | — | — | — | 3 |
| MCP23017T-E/SO — I²C GPIO Expander 16-bit (SOIC-28) | — | — | 3 | — | — | — | — | — | — | — | 3 | 6 |
| J9 — DSI1 FPC 15-pin 1.0mm ZIF connector (Amphenol F52Q-1A7H1-11015) | — | 1 | — | — | — | — | — | — | — | — | — | 1 |
| | | | | | | | | | | | | |
| 0.1 µF X7R 0402 decoupling cap — common fitted population | 20 | 1 | 15 | 8 | 48 | 10 | 300 | — | 1 | 4 | 4 | 399 |
| 10 µF X7R 50 V 1206 bulk decoupling (CL31B106KBHNNNE) | — | 5 | 5 | 5 | 30 | 5 | 150 | 5 | 5 | — | — | 202 |
| 22 µF X7R 25 V 1210 bulk cap (CL32B226KAJNNNE) | 13 | — | — | — | — | — | — | — | — | — | — | 13 |
| 47 µF X7R 25 V 2220 buck output bulk cap (TDK CGA9N3X7R1E476M230KB) | 4 | — | — | — | — | — | — | — | — | — | — | 4 |
| 4.7 µF X7R 1210 entry filter (CGA6P3X7R1H475K250AD) | — | — | — | — | — | — | — | — | — | 1 | — | 3 |
| 10 µF 16 V X7R 1206 monostable timing cap (CC1206KKX7R8BB106) | 1 | — | — | — | — | — | — | — | — | — | — | 1 |
| 1 µF X7R 50 V 0805 (C0805C105K5RACTU) | 3 | — | — | — | — | — | — | — | — | — | — | 3 |
| UNSOURCED — Rotor FDC2114 local `VDD` reservoir capacitor (1 µF X7R MLCC, ≥6.3 V; footprint owner-selected) | — | — | — | — | — | 2 | 60 | — | — | — | — | 60 |
| UNSOURCED — Rotor FDC2114 resonant tank inductor (18 µH shielded SMD; 4 per active FDC2114; Cat B, part TBD; N=26 build 8 per board, N=64 build 8 per board; per-board count includes dummy LC tanks for unused channels) | — | — | — | — | — | 8 | 240 | — | — | — | — | 240 |
| UNSOURCED — Rotor FDC2114 resonant tank capacitor (33 pF C0G/NP0 ±1%; 4 per active FDC2114; Cat B, part TBD; count same as inductor) | — | — | — | — | — | 8 | 240 | — | — | — | — | 240 |
| 10 µF 25 V X7R 1206 LDO input cap (C1206C106K3RACTU) | 1 | — | — | — | — | — | — | — | — | — | — | 1 |
| 10 nF X7R 50 V 0402 soft-start cap (CL05B103KB5NNNC) | — | 1 | — | — | — | — | — | — | — | — | — | 1 |
| 10 nF 100 V X7R 0402 Bob Smith termination cap (C0402C103K1RACAUTO) | — | 1 | — | — | — | — | — | — | — | — | — | 1 |
| 100 pF X7R 25 V 0402 SYNC SW-ringing LP filter (C0402C101K3RACAUTO) | 1 | — | — | — | — | — | — | — | — | — | — | 1 |
| 22 nF X7R 25 V 0603 SYNC phase-delay cap (CL10B223KB8WPNC) | 1 | — | — | — | — | — | — | — | — | — | — | 1 |
| 25 F / 2.7 V Supercapacitor (Abracon ADCR-T02R7SA256MB) | 8 | — | — | — | — | — | — | — | — | — | — | 8 |
| 22 µF 25 V X7R 1210 5V_MAIN backup bulk cap C14/C15 (Samsung CL32B226KAJNNNE) | 2 | — | — | — | — | — | — | — | — | — | — | 2 |
| | | | | | | | | | | | | |
| 10 kΩ 1% 0603 fitted resistor — pull / series population (ERJ-3EKF1002V / C191124) | 6 | 5 | 16 | — | — | — | — | — | — | — | 11 | 38 |
| 10 kΩ 1% 0402 pull resistor — common fitted population (ERJ-2RKF1002X / C191123) | 7 | — | 0 | 4 | 24 | 4 | 120 | — | — | 2 | — | 155 |
| 1 kΩ 1% 0402 gate resistor — common fitted population (ERJ-2RKF1001X) | 5 | — | — | — | — | — | — | — | — | — | 6 | 11 |
| 75 Ω 1% 0603 series resistor (ERJ-3EKF75R0V / C105905) | — | — | 18 | — | — | — | — | — | — | — | — | 18 |
| 75 Ω 1% 0402 resistor (ERJ-2RKF75R0X / C413061) | — | 4 | — | 1 | 6 | — | — | — | — | — | — | 10 |
| 33 Ω 1% 0603 series resistor (ERJ-3EKF33R0V / C25819) | — | — | — | — | — | — | — | — | — | — | — | — |
| 33 Ω 1% 0402 series resistor (ERJ-2RKF33R0X / C25808) | — | — | — | — | — | — | — | — | — | 4 | — | 4 |
| 22 Ω 0603 1% JTAG end-of-chain damping (ERJ-3EKF2200V) | — | — | — | — | — | — | — | 1 | — | — | — | 1 |
| 330 Ω 1% 0402 LED current-limit resistor (ERJ-2RKF3300X / C105872) | — | — | — | 1 | 6 | — | — | — | — | — | — | 12 |
| 330 Ω 1% 0603 Ethernet activity LED resistor (ERJ-3EKF3300V / C25803) | — | 2 | — | — | — | — | — | — | — | — | — | 2 |
| 150 Ω 1% 0603 LED current-limit resistor (ERJ-3EKF1500V / C400650) | — | — | — | — | — | — | — | — | — | — | 12 | 12 |
| 100 Ω 1% 0603 LED current-limit resistor (ERJ-3EKF1000V / C193336) | — | — | — | — | — | — | — | — | — | — | 24 | 24 |
| 4.7 kΩ 1% 0603 I²C pull-up (ERJ-3EKF4701V / C192166) | 2 | — | — | — | — | — | — | — | — | — | — | 2 |
| UNSOURCED — Rotor local FDC2114 I²C pull-up resistor (`SDA` / `SCL`, 3.3 V local bus, 1 per line; value/footprint owner-selected) | — | — | — | — | — | 2 | 60 | — | — | — | — | 60 |
| 100 Ω 1% 0603 differential termination (ERJ-3EKF1000V / C193336) | — | 1 | — | — | — | — | — | — | — | — | — | 1 |
| 20 mΩ 1% 1206 current-sense shunt (ERJ-6ENF20R0V / C123465) | — | — | — | — | — | — | — | — | — | — | — | — |
| 10 mΩ ±1% 5 A 2512 Kelvin shunt (CSS2H-2512R-R010ELF) | 2 | — | 1 | — | — | — | — | — | — | — | — | 3 |
| 121 kΩ 1% 0603 PoE MPS current set (ERJ-3EKF1213V / C402905) | — | 1 | — | — | — | — | — | — | — | — | — | 1 |
| 301 Ω 1% 0603 charge current set (ERJ-3EKF3010V / C403144) | 1 | — | — | — | — | — | — | — | — | — | — | 1 |
| 274 kΩ 1% 0603 MIC1555 U15 monostable R28 (ERJ-3EKF2743V / C403126) | 1 | — | — | — | — | — | — | — | — | — | — | 1 |
| 715 kΩ 1% 0603 MIC1555 timer R\_B (ERJ-3EKF7153V / C403339) | 1 | — | — | — | — | — | — | — | — | — | — | 1 |
| 232 kΩ 1% 0603 thick-film eFuse UVLO (ERJ-3EKF2323V / C403086) | 1 | — | — | — | — | — | — | — | — | — | — | 1 |
| 28.7 kΩ 1% 0603 thick-film eFuse UVLO (ERJ-3EKF2872V / C403135) | 1 | — | — | — | — | — | — | — | — | — | — | 1 |
| 210 Ω 0.1% 0603 thin-film eFuse ILIM (ERA-3VEB2100V / C1861624) | 1 | — | — | — | — | — | — | — | — | — | — | 1 |
| 86.6 kΩ 1% 0603 thick-film SYNC FSET resistor (ERJ-3EKF8662V / C403381) | 1 | — | — | — | — | — | — | — | — | — | — | 1 |
| 82.0 kΩ 1% 0402 thick-film SYNC phase-delay R\_DLY (ERJ-2RKF8202X / C400641) | 1 | — | — | — | — | — | — | — | — | — | — | 1 |
| 30.1 kΩ 0.1% 0603 thin-film supercap BACKUP R\_TOP (ERA-3ARB3012V / C1728516 — see DEC-030) | 1 | — | — | — | — | — | — | — | — | — | — | 1 |
| 10.0 kΩ 0.1% 0603 thin-film supercap BACKUP R\_BOT (ERA-3ARB103V / C465746) | 1 | — | — | — | — | — | — | — | — | — | — | 1 |
| 33.2 kΩ 1% 0402 thick-film LTC3350 RT freq-set (ERA-2AEB3322X / C2087909) | 1 | — | — | — | — | — | — | — | — | — | — | 1 |
| 0 Ω 0603 bond / isolating resistor (ERJ-3GEY0R00V / C25807) | — | — | — | — | — | — | — | — | 1 | — | — | 1 |
| Ferrite bead 120 Ω @100 MHz 4.0 A 1206 (Laird HI1206P121R-10) | — | — | 4 | — | — | — | — | — | — | — | — | 4 |
| | | | | | | | | | | | | |
| TE 1123684-7 10-pin 2.5mm BtB PM dock header | 3 | — | — | — | — | — | — | — | — | — | — | 3 |
| TE 1-1674231-1 10-pin 2.5mm BtB PM dock receptacle | — | 3 | — | — | — | — | — | — | — | — | — | 3 |
| Molex 2195620015 hybrid Stator dock plug | — | — | 2 | — | — | — | — | — | — | — | — | 2 |
| Molex 2195630015 hybrid Stator dock receptacle | — | 2 | — | — | — | — | — | — | — | — | — | 2 |
| ERM8-005 10-pin Samtec Male Header 0.8 mm (Rotor interface) | — | — | — | — | — | 2 | 60 | 2 | 2 | — | — | 64 |
| ERF8-005 10-pin Samtec Female Socket 0.8 mm (Rotor interface) | — | — | 2 | — | — | 2 | 60 | — | 2 | — | — | 64 |
| ERM8-010 20-pin Samtec Male Header 0.8 mm (ENC data) | — | — | — | — | — | 1 | 30 | 1 | 1 | — | — | 32 |
| ERF8-010 20-pin Samtec Female Socket 0.8 mm (ENC data) | — | — | 1 | — | — | 1 | 30 | — | 1 | — | — | 32 |
| Adam Tech PH1-07-UA — 1×7 2.54mm male pin header, Rotor Board A H\_SW3 (Mouser 737-PH1-07-UA; DigiKey 2057-PH1-07-UA-ND; JLCPCB C3331618) | — | — | — | — | — | 1 | 30 | — | — | — | — | 30 |
| Adam Tech RS1-07-G — 1×7 2.54mm female socket, Rotor Board B H\_SW3 (Mouser 737-RS1-07-G; DigiKey 2057-RS1-07-G-ND; JLCPCB C3321543) | — | — | — | — | — | 1 | 30 | — | — | — | — | 30 |
| Adam Tech BHR-20-VUA / 2BHR-20-VUA — 20-pin 2×10 shrouded box header, 2.54mm (Mouser 737-BHR-20-VUA; DigiKey 2057-BHR-20-VUA-ND; JLCPCB C17340054 uses 2BHR-20-VUA MPN) | — | — | 7 | 1 | 6 | — | — | 1 | 2 | — | — | 16 |
| Adam Tech PH1-05-UA — 1×5 2.54mm male pin header, JDB J1/Rotor H\_PWR+H\_JTAG(BrdB)+H\_SENS(BrdA) (Mouser 737-PH1-05-UA; DigiKey 2057-PH1-05-UA-ND; JLCPCB C5374051) | — | — | — | — | — | 3 | 90 | — | — | 1 | — | 91 |
| Adam Tech RS1-05-G — 1×5 2.54mm female socket, CTL J\_JDB\_PWR/Rotor H\_PWR+H\_JTAG(BrdA)+H\_SENS(BrdB) (Mouser 737-RS1-05-G; DigiKey 2057-RS1-05-G-ND; JLCPCB C3321119) | — | 1 | — | — | — | 3 | 90 | — | — | — | — | 91 |
| Adam Tech PH1-10-UA — 1×10 2.54mm male pin header, JDB J2 JTAG OUTPUT (Mouser 737-PH1-10-UA; DigiKey 2057-PH1-10-UA-ND; JLCPCB C3330527) | — | — | — | — | — | — | — | — | — | 1 | — | 1 |
| Adam Tech RS1-10-G — 1×10 2.54mm female socket, Controller J13 (Mouser 737-RS1-10-G; DigiKey 2057-RS1-10-G-ND; JLCPCB C3320525) | — | 1 | — | — | — | — | — | — | — | — | — | 1 |
| USB 3.0 Type-A Dual-Stack (Molex 48406-0003) | — | 1 | — | — | — | — | — | — | — | — | — | 1 |
| HDMI Type-A Full-Size (TE 2007435-1) | — | 1 | — | — | — | — | — | — | — | — | — | 1 |
| USB-C SMT Receptacle 6-pos (GCT USB4135-GF-A) | 1 | — | — | — | — | — | — | — | — | — | — | 1 |
| RJ45 MagJack (Würth 7499111121A) | — | 1 | — | — | — | — | — | — | — | — | — | 1 |
| Battery Connector 5-pin Micro-Fit 3.0 (Molex 43650-0519) | 1 | — | — | — | — | — | — | — | — | — | — | 1 |
| | | | | | | | | | | | | |
| 12 MHz Crystal SMD(Abracon ABM8-12.000MHz-B2-T / C596894) | — | — | — | — | — | — | — | — | — | 1 | — | 1 |
| 72°C SMD Thermal Cutoff (Bourns AC72ABD / C17468669) | 1 | — | — | — | — | — | — | — | — | — | — | 1 |
| CR2032 Coin Cell Holder (Keystone 3034TR) | — | 1 | — | — | — | — | — | — | — | — | — | 1 |
| Würth 9774040151R M2.5 × 4.0mm SMT Brass Standoff (CM5 mount) | — | 4 | — | — | — | — | — | — | — | — | — | 4 |
| PoE ACF Isolation Transformer (Coilcraft POE600F-12L) | — | 1 | — | — | — | — | — | — | — | — | — | 1 |
| EMI Common-Mode Choke (Würth WE-CMBNC 7448031002) | 2 | — | — | — | — | — | — | — | — | — | — | 2 |
| DM Filter Inductor 10 µH 15.5 A (Bourns SRP1265A-100M) | 1 | — | — | — | — | — | — | — | — | — | — | 1 |
| Power Module RGB Metal Power Switch (Adafruit 4660) | 1 | — | — | — | — | — | — | — | — | — | — | 1 |
| Power Module Momentary RGB Metal Pushbutton (Adafruit 3350) | 1 | — | — | — | — | — | — | — | — | — | — | 1 |
| Power Module 2.8 mm PCB Male Quick-Fit Tabs (Keystone 1211; SW1 + SW2 harnesses) | 12 | — | — | — | — | — | — | — | — | — | — | 12 |
| Settings Board SPDT Toggle Switch (E-Switch 200MSP1T2B4M2QE) | — | — | — | — | — | — | — | — | — | — | 10 | 10 |
| Settings Board Discrete RGB LED (Kingbright WP154A4SEJ3VBDZGW/CA) | — | — | — | — | — | — | — | — | — | — | 12 | 12 |
| Green SMD LED 0402 (Würth 150060VS75000 / C6848499) | — | — | — | 1 | 6 | — | — | — | — | — | — | 6 |
| 6.35 mm PCB Blade Terminal (Keystone 1285-ST) | — | — | — | 64 | 384 | — | — | — | — | — | — | 384 |
| CTS 219-4LPST — 4-pos DIP switch, 2.54mm THT | — | — | — | — | — | — | — | — | — | — | — | 0 |
| CTS 219-6LPSTR — 6-pos DIP switch, 2.54mm THT | — | — | — | — | — | 3 | 90 | — | — | — | — | 90 |

Off-board plugboard jack sockets and keyboard switches are assembly-level items rather than PCB-fitted
board BOM lines. See §4a for their static counts: **64 jacks per plugboard pass (128 system total)**
and **40 switches per Keyboard Assembly (40 system total)**.

## 1. Critical Spares (MOQ Recommendations)

* **Bourns AC72 TCO:** Order 5 (MOQ) - (2x Spares).
* **Abracon ADCR-T02R7SA256MB (25F/2.7V) Supercap:** Order 12 — 8 required per build + 4 spare/test.
  Source via DigiKey (535-ADCR-T02R7SA256MB-ND) or Mouser (815-ADCRT02R7SA256MB). JLCPCB global sourcing only.
* **TE 1123684-7 / 1-1674231-1 PM dock set:** Order 8 total — 3 PM headers + 3 Controller receptacles + 2 spares / fit-check samples.
* **Molex 2195620015 / 2195630015 Stator dock set:** Order 6 total — 2 Stator plugs + 2 Controller receptacles + 2 spares / fit-check samples.
* **Samtec ERM8 / ERF8 rotor-family connectors:** Order per Rotor / Reflector / Extension quantities
  only. The Controller ↔ Power Module dock uses TE parts and the Controller ↔ Stator dock uses Molex
  hybrid parts.
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
| L3 | EMI DM Pi-filter Inductor | Bourns SRP1265A-100M | 10µH, 15.5A Isat, DCR 16.5mΩ | 13.5×12.5×6.2mm SMT | 652-SRP1265A-100M; alt: Farnell ~2741 in stock |
| C1-C4 | Pi-filter bulk cap bank (C1/C2 at filter input, C3/C4 at filter output) | Samsung CL32B226KAJNNNE | 22µF 25V X7R | 1210 | 187-CL32B226KAJNNNE |
| C5-C8, C9-C12, C13-C15 | Power-stage 22µF bulk caps (buck inputs, eFuse input/output, LDO output, backup bank) | Samsung CL32B226KAJNNNE | 22µF 25V X7R | 1210 | 187-CL32B226KAJNNNE |
| C16-C19 | LMQ61460-Q1 buck output bulk caps | TDK CGA9N3X7R1E476M230KB | 4× 47µF 25V X7R MLCC total (2 fitted at U2A OUT, 2 fitted at U2B OUT) | 2220 | 810-A9N3X7476M23KB |
| C20 | LDO input cap (U7 VIN) | Kemet C1206C106K3RACTU | 10µF 25V X7R | 1206 | 80-C1206C106K3R |
| C21-C23 | 1µF caps (Pi-filter mid-frequency legs and U11 timer) | Kemet C0805C105K5RACTU | 1µF 50V X7R | 0805 | 80-C0805C105K5R |
| C24-C39, C43-C46 | 100nF caps (Pi-filter HF legs and IC VCC bypass network, including PM U12 INA219 bypass and PM U17/U18/U19 local VCC bypass) | Samsung CL05B104KB5NNNC | 100nF 50V X7R | 0402 | 187-CL05B104KB5NNNC |
| C40 | SYNC SW-ringing low-pass filter (C_F1) | Kemet C0402C101K3RACAUTO | 100pF X7R 25V | 0402 | 80-C0402C101K3RAUTO |
| C41 | SYNC 180° phase delay capacitor (C_DLY) | Samsung CL10B223KB8WPNC | 22nF X7R 25V | 0603 | 187-CL10B223KB8WPNC |
| C42 | U15 MIC1555 one-shot timing cap | Yageo CC1206KKX7R8BB106 | 10µF 16V X7R | 1206 | 603-CC126KKX7R8BB106 |
| CTL C24 | Controller PoE front-end TPS23730 soft-start cap (U10 C_SS) | Samsung CL05B103KB5NNNC | 10nF 50V X7R | 0402 | 187-CL05B103KB5NNNC |
| JDB C5 | 5V_USB power-entry filter cap | TDK CGA6P3X7R1H475K250AD | 4.7µF X7R | 1210 | 810-CGA6P3X7R1H475KD |

**Pi-filter performance summary (f_c = 7.5kHz):**

* −52dB DM attenuation at 150kHz (EN 55032 Class B lower edge) ✓
* −57dB at 200kHz (TPS23730 ACF switching frequency) ✓
* −69dB at 400kHz (LMQ61460AFSQRJRRQ1 buck switching frequency) ✓

## 4. Board-to-Board Interconnects

* **TE 1123684-7:** Power Module dock header (`J1/J2/J3` on PM side).
* **TE 1-1674231-1:** Controller-side mating receptacle for the PM dock (`J1/J2/J3`).
* **Molex 2195620015:** Stator-side hybrid dock plug (`J11/J12`).
* **Molex 2195630015:** Controller-side mating receptacle for the Stator hybrid dock (`J4/J5`).
* **Samtec ERM8-010-05.0-S-DV-K-TR (Male, 20-pin):** Rotor J3, Reflector J3, Extension J3. JLCPCB: C374877
* **Intel EPM570T100I5N:** 37 units (Encoder Module ×1 per board ×6 boards = 6, Stator ×1, Rotor
  ×1 per board ×30 boards = 30; total 37). Common CPLD across Encoder, Stator, and Rotor boards.
  DigiKey: 544-2281-ND · Mouser: 989-EPM570T100I5N · JLCPCB: C27319.

## 4a. Encoder Module — Plugboard Jacks, Keyboard Switches & PCB Spade Terminals

| Ref | Component | Part / Description | Qty | Supplier | Supplier Ref / Notes |
| :--- | :--- | :--- | :--- | :--- | :--- |
| J1 (×64 per plugboard pass) | Stecker jack sockets | 6.35mm (¼″) mono switched panel-mount jack — Tip + Switch: decode-role Encoder Module line; Sleeve: paired encode-role Encoder Module line. **Already purchased.** | 64 per pass | SaiBuy.Ltd (eBay) | eBay item 334364197440 — £1.66/unit (sold in packs of 3 for £4.99). [ebay.co.uk — SaiBuy.Ltd](https://www.ebay.co.uk/str/saibuyltd). See pseudo datasheet in `design/Datasheets/SaiBuy_Ltd_6p35mm_Mono_Jack_Pseudo_Datasheet.md`. |
| SW1-40 | Keyboard switches | uxcell-style DPDT 6-pin momentary push button — Pole 1 electrically active: COM1+NO1 → key-press to CPLD. Pole 2 pins soldered for mechanical key anchoring only (no electrical connection). NC1 not connected. Keys connect to the `KBD_ENC` module only. **Already purchased.** | 40 total | gadgetskingdom (eBay) | Sold in packs of 2. eBay item 365271584375. Listing title: "Momentary Push Button Switch DPDT 2 Pole 6 Pin 1 Position 2pcs". See pseudo datasheet in `design/Datasheets/`. |
| BT1-64 | PCB blade terminals — generic 64-line Encoder Module I/O bank | Keystone 1285-ST — 6.35mm (0.250″) straight vertical PCB-mount male blade tab, through-hole. Used as either decode-role outputs or encode-role inputs depending on module role. | 64 per module | Mouser / DigiKey / JLCPCB | Mouser: 534-1285-ST · DigiKey: 36-1285-ST-ND · JLCPCB: C5370868 |

**Notes:**

* **Plugboard jacks (J1 ×64 per pass):** mount in the plugboard panel. Each jack connects between one
  decode-role Encoder Module and one paired encode-role Encoder Module within the same pass.
* **Keyboard switches (SW1-40):** mount in the keyboard panel. The physical HID layout uses 40
  switches total: 38 printable positions (`[a-z0-9+=]`) plus Left Shift and Right Shift. These wire
  only to the `KBD_ENC` module.
* **Total PCB blade terminals: 64 per Encoder Module, 384 system-wide** — all Keystone 1285-ST.
* Stecker patch cables (plugboard) use 6.35mm mono jack plugs (TS) — not included in BOM; customer-supplied.

## 4b. Stator Board — Panel Switch Configuration Components

| Ref | Component | Value | Package | Mouser Part # | DigiKey Part # | JLCPCB Part # | Conf |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :---: |
| R16–R19 | SW1[3:0] CPLD config input pull-down resistors (×4) | 10kΩ 1% 0603 | 0603 | 667-ERJ-3EKF1002V | P10.0KHCT-ND | C191124 | 🔒 |
| R20 | `CFG_APPLY_N` pull-up resistor (×1) | 10kΩ 1% 0603 | 0603 | 667-ERJ-3EKF1002V | P10.0KHCT-ND | C191124 | 🔒 |
| R21–R26 | SW2[5:0] CPLD config input pull-down resistors (×6) | 10kΩ 1% 0603 | 0603 | 667-ERJ-3EKF1002V | P10.0KHCT-ND | C191124 | 🔒 |

Pull-down resistors R16–R19 and R21–R26 are retained on the Stator CPLD config input pins as
power-up safe defaults (hold all inputs LOW when U8 is uninitialised). R20 keeps `CFG_APPLY_N`
inactive HIGH until U8 actively asserts the Stator-local apply/reset pulse. Physical switches SW1 and SW2 have
been removed and relocated to the Settings Board. See `Settings_Board/Design_Spec.md` for the
full switch specifications and `Stator/Design_Spec.md §3 Panel Switch Configuration` for the
configuration tables.

## 4c. Stator Board — Virtual Keyboard / Key Injection Components

| Ref | Component | Value | Package | Mouser Part # | DigiKey Part # | JLCPCB Part # | Conf |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :---: |
| U6, U7 | MCP23017 I²C GPIO Expander (×2) | MCP23017T-E/SO | SOIC-28 | 579-MCP23017T-E/SO | MCP23017T-E/SOCT-ND | C47023 | 🔒 |
| U8 | MCP23017 I²C GPIO Expander (CPLD config output driver) | MCP23017T-E/SO @ 0x22 | SOIC-28 | 579-MCP23017T-E/SO | MCP23017T-E/SOCT-ND | C47023 | 🔒 |
| J13 | Settings Board I²C connector (6-pin JST PH 2.0mm) | JST B6B-PH-K-S(LF)(SN) | THT | 306-B6B-PH-K-SLFSN | 455-1708-ND | C131342 | 🔒 |

U6 @ 0x20: ENC_IN/ENC_OUT monitoring. U7 @ 0x21: virtual keypress injection, SOURCE_SEL,
SYS_RESET_N, spare GPIO. U8 @ 0x22: CPLD config output driver (`CFG_ROUTE[3:0]` +
`CFG_REFMAP[5:0]` + `CFG_APPLY_N`). J13 (6-pin JST PH) connects to Settings Board J1 and carries 3V3_ENIG,
5V_MAIN (used as the Settings indicator rail), 2× GND, SDA, SCL.

### Shared Actuation Module / Host Interface Components

Rev A currently uses **two AM modules total**: one on the Controller and one on the single fitted
Extension. A future full 30-rotor build would scale this to **six AM modules total** (Controller + 5
Extensions), but the totals below follow the same **Rev A single-Extension** convention used elsewhere
in this consolidated BOM.

| Ref | Component | Value | Package | Mouser Part # | DigiKey Part # | JLCPCB Part # | Conf | Qty per board/module | Rev A total |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :---: | :---: | :---: |
| J11 / J16 (Controller host) | Actuation Module host dock sockets (power + trigger) | Samtec ERF8-005-05.0-S-DV-K-TR | SMT 0.8mm pitch | 200-ERF8005050SDVKTR | SAM13517CT-ND | C7273978 | 🔒 | 2 per Controller | 2 |
| J9 / J10 (Extension host) | Actuation Module host dock sockets (power + trigger) | Samtec ERF8-005-05.0-S-DV-K-TR | SMT 0.8mm pitch | 200-ERF8005050SDVKTR | SAM13517CT-ND | C7273978 | 🔒 | 2 per Extension | 2 |
| J1 / J2 (AM module) | Actuation Module module-side dock headers (power + trigger) | Samtec ERM8-005-05.0-S-DV-K-TR | SMT 0.8mm pitch | 200-ERM8005050SDVKTR | 612-ERM8-005-05.0-S-DV-K-TRCT-ND | C3649741 | 🔒 | 2 per AM | 4 |
| J3 / J4 / J5 / J6 (AM module) | Manual-fit headers (servo + home switch + SWD + UART/bootloader service) | Adam Tech PH1-05-UA — 1×5 2.54mm male | THT | 737-PH1-05-UA | 2057-PH1-05-UA-ND | C5374051 | 🔒 | 4 per AM | 8 |
| SW1 (AM module) | Local reset pushbutton | Omron B3F-1070 — SPST NO through-hole tactile switch | THT tactile | 653-B3F-1070 | SW406-ND | C726011 | 🔒 | 1 per AM | 2 |
| SW2 (AM module) | Local `BOOT0` pushbutton | Omron B3F-1070 — SPST NO through-hole tactile switch | THT tactile | 653-B3F-1070 | SW406-ND | C726011 | 🔒 | 1 per AM | 2 |
| C2-C3 (AM module) | STM32 local supply decoupling | 100nF X7R 50V | 0402 | 187-CL05B104KB5NNNC | 1276-1009-1-ND | C1525 | 🔒 | 2 per AM | 4 |
| C4 (AM module) | `3V3_ENIG` local reservoir / entry filter | 4.7uF X7R (CGA6P3X7R1H475K250AD) | 1210 | 810-CGA6P3X7R1H475KD | 445-10040-1-ND | C3877549 | 🔒 | 1 per AM | 2 |
| C5 (AM module) | `5V_MAIN` local reservoir near servo power path | 10uF X7R 50V | 1206 | 187-CL31B106KBHNNNE | 1276-6767-1-ND | C89632 | 🔒 | 1 per AM | 2 |
| D1-D3 (AM module) | Local diagnostic LEDs (`PWR`, `HOMED`, `ACT`) | Wurth 150060VS75000 — Green SMD LED | 0402 | 710-150060VS75000 | 732-4980-1-ND | C6848499 | 🔒 | 3 per AM | 6 |
| R1-R3 (AM module) | LED current-limit resistors | 330Ω 1% 0402 | 0402 | 667-ERJ-2RKF3300X | P330LCT-ND | C278592 | 🔒 | 3 per AM | 6 |
| R4 (AM module) | `ACTUATION_HOME` pull-up resistor | 10kΩ 1% 0402 | 0402 | 667-ERJ-2RKF1002X | P10.0KLCT-ND | C191123 | 🔒 | 1 per AM | 2 |
| R5 (AM module) | `BOOT0` series resistor (prevents contention when both J6 pin 5 and MCU BOOT0 drive simultaneously) | 10kΩ 1% 0402 — same part as R4 | 0402 | 667-ERJ-2RKF1002X | P10.0KLCT-ND | C191123 | 🔒 | 1 per AM | 2 |
| C1 (AM module) | `ACTUATION_HOME` debounce capacitor | 100nF 50V X7R 0402 | 0402 | 187-CL05B104KB5NNNC | 1276-1009-1-ND | C1525 | 🔒 | 1 per AM | 2 |
| C6 (AM module) | NRST filter capacitor (100nF X7R per STM32G071 datasheet Figure 23) | 100nF 50V X7R 0402 — same part as C2/C3/C1 | 0402 | 187-CL05B104KB5NNNC | 1276-1009-1-ND | C1525 | 🔒 | 1 per AM | 2 |
| U1 (AM module) | Local actuation controller | STMicroelectronics STM32G071K8T3TR | LQFP32 | 511-STM32G071K8T3TR | 497-STM32G071K8T3TR-ND | Global sourcing / consignment only | 🔒 | 1 per AM | 2 |

The servo motor and its local home switch remain off-board electromechanical items and are therefore
not listed as PCB-fitted rows in the consolidated electronic BOM.

## 4d. Settings Board

The Settings Board replaces the Stator DIP switches with user-accessible panel-mount toggle
switches plus discrete RGB indicator LEDs. See `Settings_Board/Design_Spec.md` for the full design
specification.

| Ref | Component | Value | Package | Mouser Part # | DigiKey Part # | JLCPCB Part # | Conf |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :---: |
| U1 | MCP23017 I²C GPIO Expander (switch input reader) | MCP23017T-E/SO @ 0x23 | SOIC-28 | 579-MCP23017T-E/SO | MCP23017T-E/SOCT-ND | C47023 | 🔒 |
| U2 | MCP23017 I²C GPIO Expander (Bank 1 LED controller) | MCP23017T-E/SO @ 0x24 | SOIC-28 | 579-MCP23017T-E/SO | MCP23017T-E/SOCT-ND | C47023 | 🔒 |
| U3 | MCP23017 I²C GPIO Expander (Bank 2 LED controller) | MCP23017T-E/SO @ 0x25 | SOIC-28 | 579-MCP23017T-E/SO | MCP23017T-E/SOCT-ND | C47023 | 🔒 |
| D1-D5 | Bank 1 discrete RGB indicator LEDs (×5) | Kingbright WP154A4SEJ3VBDZGW/CA — 5mm common-anode RGB THT LED | THT 5mm LED | 604-WP154A43VBDZGWCA | 754-2029-ND | C7151795 | ✅ |
| D6-D12 | Bank 2 discrete RGB indicator LEDs (×7) | Kingbright WP154A4SEJ3VBDZGW/CA — same part as Bank 1 | THT 5mm LED | 604-WP154A43VBDZGWCA | 754-2029-ND | C7151795 | ✅ |
| SW11 | `CFG_APPLY_N` momentary pushbutton | Omron B3F-1070 — SPST NO through-hole tactile switch; board-mounted and mechanically actuated through enclosure | THT tactile | 653-B3F-1070 | SW406-ND | C726011 | ✅ |
| J1 | I²C ribbon cable connector to Stator J13 | JST B6B-PH-K-S(LF)(SN) — 6-pin JST PH 2.0mm | THT | 306-B6B-PH-K-SLFSN | 455-1708-ND | C131342 | 🔒 |
| Q1, Q2, Q3, Q4, Q5, Q6 | Low-side colour-rail sink MOSFETs (×6 total; 3 per bank for RGB) | BSS138 | SOT-23 | 512-BSS138 | BSS138CT-ND | C52895 | 🔒 |
| R1-R10 | Switch input pull-down resistors (×10: 4 Bank 1 + 6 Bank 2) | 10kΩ 1% | 0603 | 667-ERJ-3EKF1002V | P10.0KHCT-ND | C191124 | 🔒 |
| R11 | `CFG_APPLY_N` pull-up resistor | 10kΩ 1% | 0603 | 667-ERJ-3EKF1002V | P10.0KHCT-ND | C191124 | 🔒 |
| R12-R17 | MOSFET gate resistors (×6; 1 per MOSFET) | 1kΩ 1% | 0402 | 667-ERJ-2RKF1001X | P1.00KLCT-ND | C242161 | 🔒 |
| R18-R29 | Per-indicator red LED series resistors (×12) | 150Ω 1% — 5V operation @ 20mA nominal (Vf_red ≈ 2.0V) | 0603 | 667-ERJ-3EKF1500V | P150HCT-ND | C400650 | 🔒 |
| R30-R41 | Per-indicator green LED series resistors (×12) | 100Ω 1% — 5V operation @ 20mA nominal (Vf_green ≈ 3.0V) | 0603 | 667-ERJ-3EKF1000V | P100HCT-ND | C193336 | 🔒 |
| R42-R53 | Per-indicator blue LED series resistors (×12) | 100Ω 1% — 5V operation @ 20mA nominal (Vf_blue ≈ 3.0V) | 0603 | 667-ERJ-3EKF1000V | P100HCT-ND | C193336 | 🔒 |
| SW1-SW4 | Bank 1 configuration toggle switches (×4: routing bits 0–3) | E-Switch 200MSP1T2B4M2QE — SPDT latching sub-mini toggle, T2 actuator, B4 bushing, M2 termination, Q silver contacts, epoxy sealed | Panel-mount THT toggle | 612-200MSP1T2B4M2QE | EG5525-ND | C5491263 | ✅ |
| SW5-SW10 | Bank 2 configuration toggle switches (×6: reflector bits 0–5) | E-Switch 200MSP1T2B4M2QE — same part as Bank 1 | Panel-mount THT toggle | 612-200MSP1T2B4M2QE | EG5525-ND | C5491263 | ✅ |
| C4 | `CFG_APPLY_N` debounce capacitor | 100nF X7R 50V | 0402 | 187-CL05B104KB5NNNC | 1276-1009-1-ND | C1525 | 🔒 |
| C1 | VCC decoupling cap for U1 (MCP23017 @ 0x23) | 100nF X7R 50V | 0402 | 187-CL05B104KB5NNNC | 1276-1009-1-ND | C1525 | 🔒 |
| C2 | VCC decoupling cap for U2 (MCP23017 @ 0x24) | 100nF X7R 50V | 0402 | 187-CL05B104KB5NNNC | 1276-1009-1-ND | C1525 | 🔒 |
| C3 | VCC decoupling cap for U3 (MCP23017 @ 0x25) | 100nF X7R 50V | 0402 | 187-CL05B104KB5NNNC | 1276-1009-1-ND | C1525 | 🔒 |
| Q7–Q11 | Bank 1 per-anode low-side NMOS (5 total; one per Bank 1 LED anode → drives PMOS gate) | BSS138 — same part as Q1–Q6 | SOT-23 | 512-BSS138 | BSS138CT-ND | C52895 | 🔒 |
| Q12–Q18 | Bank 2 per-anode low-side NMOS (7 total; one per Bank 2 LED anode → drives PMOS gate) | BSS138 — same part as Q1–Q6 | SOT-23 | 512-BSS138 | BSS138CT-ND | C52895 | 🔒 |
| Q19–Q23 | Bank 1 per-anode high-side PMOS (5 total; source = 5V_MAIN, drain = LED anode; controlled by Q7–Q11) | PMOS high-side switch — **Cat B, part TBD** | SOT-23 | TBD (Cat B) | TBD (Cat B) | TBD (Cat B) | Cat B |
| Q24–Q30 | Bank 2 per-anode high-side PMOS (7 total; source = 5V_MAIN, drain = LED anode; controlled by Q12–Q18) | PMOS high-side switch — same part as Q19–Q23 (**Cat B**) | SOT-23 | TBD (Cat B) | TBD (Cat B) | TBD (Cat B) | Cat B |
| R54–R58 | Bank 1 NMOS gate resistors (×5; one per Q7–Q11 gate) | 1kΩ 1% 0402 — same part as R12–R17 | 0402 | 667-ERJ-2RKF1001X | P1.00KLCT-ND | C242161 | 🔒 |
| R59–R65 | Bank 2 NMOS gate resistors (×7; one per Q12–Q18 gate) | 1kΩ 1% 0402 — same part as R12–R17 | 0402 | 667-ERJ-2RKF1001X | P1.00KLCT-ND | C242161 | 🔒 |
| R66–R70 | Bank 1 PMOS gate pull-up resistors to 5V_MAIN (×5; one per Q19–Q23 gate) | 47kΩ 1% 0402 — **Cat B, part TBD** | 0402 | TBD (Cat B) | TBD (Cat B) | TBD (Cat B) | Cat B |
| R71–R77 | Bank 2 PMOS gate pull-up resistors to 5V_MAIN (×7; one per Q24–Q30 gate) | 47kΩ 1% 0402 — same part as R66–R70 (**Cat B**) | 0402 | TBD (Cat B) | TBD (Cat B) | TBD (Cat B) | Cat B |

U1 @ 0x23: reads the 10 configuration toggle states (`CFG_ROUTE[3:0]` on GPA[3:0], `CFG_REFMAP[5:0]` on GPB[5:0]) plus `CFG_APPLY_N` on GPB[7]. U2 @ 0x24 and U3 @ 0x25:
drive per-bit LED anodes and per-bank RGB colour-rail MOSFET sinks. All three share the Stator
I²C-1 bus via the J1 → J13 ribbon cable. LEDs operate at 5V @ 20mA with 150Ω red and 100Ω
green/blue series resistors. `5V_MAIN` is routed from the Controller via the `J4`
high-current dock through the Stator to the Settings Board.

## 5. Controller Specifics

* **CM5 Module:** Raspberry Pi Compute Module 5, end-user selected multi-variant option. Any non-Lite CM5 with at least 4GB RAM and 8GB eMMC is acceptable; on-board Wi-Fi may be fitted or omitted.
* **Stacked USB 3.0:** Molex 48406-0003 (THT Right-Angle).
* **Full HDMI:** TE Connectivity 2007435-1 (THT Type-A).

### 5.1. Controller User I/O Protection

* **TPS2065CDBVR:** USB Power Distribution Switch (SOT-23-5) (1.6A Limit).
* **AP2331W-7:** HDMI Current Limiter (SOT-23-5) (50mA Limit).
* **TPD4E05U06QDQARQ1:** 4-channel ESD array, U-DFN-10. DigiKey: `296-40696-1-ND`; Mouser: `595-PD4E05U06QDQARQ1`; JLCPCB: `C81353`.

### Controller Board — Power Entry Decoupling
>
> **Note:** C1-C5 and C7-C11 use the common 10uF 1206 bulk capacitor defined in
> §2 Common Passives — not duplicated by supplier row here.

| Ref | Description | Qty | Placement rule |
| :--- | :--- | :--- | :--- |
| C1-C5 | `5V_MAIN` bulk entry decoupling bank | 5 | Symmetrical star/spoke entry bank at `J1` `5V_MAIN` |
| C7-C11 | `3V3_ENIG` bulk entry decoupling bank | 5 | Symmetrical star/spoke entry bank at `J1` `3V3_ENIG` |

### Controller Board — RTC Battery Circuit
>
> **Note:** C6 (100nF X7R 0402, Samsung CL05B104KB5NNNC) uses the common 100nF 0402 passive from
> §2 Common Passives — not duplicated here.

| Ref | Component | Description | Qty | Supplier | Part Number |
| :--- | :--- | :--- | :--- | :--- | :--- |
| BT1 | Keystone 3034TR | CR2032 THT horizontal coin cell holder — RTC backup battery for CM5 MXL7704 PMIC (`TR` = tape-reel packaging) | 1 | Mouser: 534-3034TR / DigiKey: 36-3034CT-ND / JLCPCB: C5213768 | Keystone 3034TR |
| D1 (CTRL) | BAT54 | SOT-23 Schottky — VBAT (Pin 76) charge blocking diode (prevents PMIC from charging CR2032) | 1 | Mouser: 637-BAT54 / DigiKey: 4878-BAT54CT-ND / JLCPCB: C49435667 | BAT54 |
| — | Renata CR2032 | CR2032 3V coin cell (not fitted at PCB assembly — installed at commissioning) | 1 | Mouser: 614-CR2032 / DigiKey: P189-ND | Renata CR2032 |

### Controller Board — Connectors & Headers

| Ref | Component | Description | Mouser Part # | DigiKey Part # | JLCPCB Part # | Conf |
| :--- | :--- | :--- | :--- | :--- | :--- | :---: |
| J9 | DSI1 FPC connector (15-pin 1.0mm ZIF) | Amphenol F52Q-1A7H1-11015 — DSI1 4-lane FPC/ZIF connector for optional lid-mounted touchscreen; connector is fixed even though the display add-on remains deferred; 100 Ω differential, route on L3 | 649-F52Q-1A7H1-11015 | 609-F52Q-1A7H1-11015CT-ND | C3169095 | ✅ |
| J10 | JST SH 4-pin 1.0mm fan header | JST SM04B-SRSS-TB(LF)(SN) — 5V PWM fan connector (Pin 1 = 5V_MAIN, Pin 2 = GND, Pin 3 = TACH, Pin 4 = PWM) | 306-SM04BSRSSTBLFSN | 455-SM04B-SRSS-TBCT-ND | C160404 | 🔒 |

## 6. Backplane & Extension Components

* **20-pin Inter-Board Link (Adam Tech BHR-20-VUA / 2BHR-20-VUA, 2×10, 2.54mm):** Used for J10
  (Extension/Reflector link) on Stator, Extension (J7/J8), and Reflector (J4). Pins 1-16 preserve
  the reflector-boundary service bus; pins 17-20 add grouped `5V_MAIN` and returns for the
  Extension-local Actuation Module supply path.
* See individual board BOMs: Rotor/Board_Layout.md, Stator/Board_Layout.md, Extension/Board_Layout.md, Reflector/Board_Layout.md for authoritative connector part numbers.
* **Copper Shielding Tape:** 50mm (2.0") Conductive Adhesive (Manual cable wrap).

## 7. Power & Telemetry Sensors

* **INA219AIDR:** 2 units — PM U12 @ I²C 0x40 (5V\_MAIN current monitoring); Stator U2 @ I²C 0x45 (rotor telemetry).
* **PCA9534APWR:** 1 unit — PM U16 @ I²C 0x3F (status / SW1 RGB expander).
* **SW2 hardware indicator logic:** add 1× dual Schmitt inverter / buffer, 1× single D-type flip-flop
  with async clear, and 1× single 2-input AND gate. All must run from 3.3V logic and fit
  small-outline assembly packages.
* **20mΩ 1206 Shunt (ERJ-6ENF20R0V):** 0 units — retired from Stator; replaced by CSS2H-2512R-R010ELF.
* **10mΩ 2512 Kelvin Shunt (CSS2H-2512R-R010ELF):** 3 build + 3 spares — PM R12 (LTC3350 RSENSE) + PM R23 (INA219 U12, 0x40) + Stator R1 (INA219 U2, 0x45).

## 8. Controller Ethernet / PoE Auxiliary Subsystem

| Ref | Component | Part Number | Value / Notes | Supplier | Supplier Part # | Unit Price (1-off) | Unit Price (volume) |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| U9 | PoE PD Interface (Type 4) | TPS2372-4RGWR | TI VQFN-20; 802.3bt Type 4, external hotswap, up to 90W | Mouser | 595-TPS2372-4RGWR | ~£3.50 | ~£2.00 |
| U10 | PoE ACF DC-DC Controller | TPS23730RMTR | TI WQFN-20; ACF topology; PSR mode; 12V output set by POE600F-12L turns ratio; VS pin to aux winding | Mouser | 595-TPS23730RMTR | ~£3.50 | ~£2.00 |
| T2 | PoE ACF Isolation Transformer | **Coilcraft POE600F-12L** | 60W; 12V out; 36–72V in; 200kHz; ACF topology; ≥1500Vrms; SMT; RoHS. Base functional MPN; `D` suffix is packaging-only for pick-and-place. | Coilcraft Direct / consignment | POE600F-12L | **£3.54** | **~£1.86** |
| R13 | TPS2372-4 RMPS (MPS current set) | 121kΩ 1% Thick-Film | 121kΩ E96; IMPS = VIMPS/RMPS = 1.205V/121kΩ = 9.96mA (Type 4 MPS auto-stretch) | Mouser | 667-ERJ-3EKF1213V | ~£0.10 | ~£0.03 |

**Notes:**

* T2 is a **Coilcraft-only consignment part** — order direct from [coilcraft.com](https://www.coilcraft.com). The functional base MPN is `POE600F-12L`; `POE600F-12LD` denotes packaging only.
* TPS23730 operates in **PSR (Primary-Side Regulation) mode** using the auxiliary winding of the POE600F-12L. No external TL431 or optocoupler required.
* TPS2372-4 uses **Autoclass** for automatic 4-event IEEE 802.3bt Type 4 classification; no external RCLASS resistor required. R13 (RMPS) programs MPS pulse current only.
* OR-ing priority: TPS2372-4 `/PG` signal drives LM74700-Q1 enable on the USB-C path to enforce PoE source priority.

## 9. Power / Dock IC & Connector BOM (Multi-Distributor)
>
> **Legend:** ✓ = confirmed from distributor search · ~ = derived from manufacturer prefix convention
> · ⚠️ = part number issue flagged · — = not stocked / THT not assembled · 🔒 = owner-confirmed; do not change without owner approval

| Designator | Part | Package | Mouser # | DigiKey # | JLCPCB # | Notes |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| U3 | LTC3350EUHF#PBF | QFN-38 5×7 | 584-LTC3350EUHF#PBF ✓ | 505-LTC3350EUHF#PBF-ND ✓ | C580711 | 🔒 ~4.5k in stock Mouser (tube). DigiKey 505-prefix confirmed. JLCPCB C580711 confirmed. |
| U5 | STUSB4500LQTR | QFN-24 4×4 | 511-STUSB4500LQTR | 497-STUSB4500LQCT-ND | C506650 | 🔒 Primary PN: STUSB4500LQTR (lower Iq ~160µA). JLCPCB C506650 confirmed L-variant in stock. If OOS, use STUSB4500QTR as alternative (non-L variant, ~210µA Iq, pin-compatible). |
| U6 | ~~LM74700-Q1DCKR~~ → **LM74700QDBVRQ1** | SOT-23-6 (DBV) | 595-LM74700QDBVRQ1 | **296-LM74700QDBVRQ1CT-ND** ✓ | C2941042 | 🔒 LM74700QDBVRQ1 (DBV=SOT-23-6 package, not DCK/SC70). DigiKey 35k+ in stock. Alt T&R Mouser PN: 595-LM74700QDBVTQ1 (pin-compatible). |
| U8 | MCP121T-450E/LB | SC70-3 | 579-MCP121T-450E/LB | **MCP121T-450E/LBCT-ND** ✓ | C625189 | 🔒 DigiKey 2.3k in stock @ $0.53/1. SC70-3 = compact 3-pin package. Microchip prefix 579-. |
| U1 | TPS259804ONRGER | VQFN-24 (RGE) | 595-TPS259804ONRGER | 296-TPS259804ONRGERCT-ND | C2878936 | 🔒 16.9V silicon-fixed OVLO variant. OVLO set in silicon — no external R. R3 repurposed as R_ILIM (210 Ω). PNs confirmed. |
| U2A/U2B | LMQ61460AFSQRJRRQ1 | VQFN-HR (RJR) 14-pin 4×3.5mm | 595-Q61460AFSQRJRRQ1 | 296-LMQ61460AFSQRJRRQ1CT-ND | C1518767 | 🔒 AEC-Q100 automotive-qualified (Q1), VQFN-HR RJR 14-pin 4×3.5mm. ✓ |
| U4 | TPS25751DREFR | WQFN-38 6×4mm | 595-TPS25751DREFR | 296-TPS25751DREFRCT-ND | C30169739 | 🔒 ✅ Replaces NRND TPS25750DRCR (see DEC-012). PD3.1 certified (USB-IF TID#10306). Package: WQFN-38 6×4mm (note: different from TPS25750 QFN-28). |
| U7 | TPS75733KTTRG3 | TO-263 (KTT) 5-pin 10.16×15.24mm | 595-TPS75733KTTRG3 | 296-50559-1-ND | C3749924 | 🔒 Fixed 3.3V, TO-263 KTT 5-pin. Active-LOW EN (EN LOW = enabled). ✓ |
| U16 | PCA9534APWR | TSSOP-16 | 595-PCA9534APWR | 296-21760-1-ND | C2871127 | 🔒 PM-local 8-bit I²C GPIO expander at 0x3F. Inputs: `POE_STAT`, `SYS_FAULT`, `BATT_PRES_N`, `USB_STAT`. Outputs: `SW_LED_R/G/B`, `SW_LED_CTRL`. |
| U17 | NL27WZ14DFT2G-Q | SC-88 | 863-NL27WZ14DFT2G-Q | 488-NL27WZ14DFT2G-QCT-ND | C24511261 | PM SW2 hardware signal conditioner. Automotive dual Schmitt-trigger inverter, 1.65-5.5V supply, push-pull outputs, 5.5V-tolerant inputs. One gate conditions / inverts `LED_nPWR`; the second conditions / inverts `PWR_BUT` for the SW2 hardware indicator logic. |
| U18 | SN74LVC1G175DBVR | SOT-23-6 | 595-SN74LVC1G175DBVR | 296-17617-1-ND | C128412 | PM SW2 shutdown latch. Single D-type flip-flop with asynchronous clear, 1.65–5.5V supply, push-pull Q output, 5.5V-tolerant inputs. |
| U19 | SN74LVC1G08DBVR | SOT-23-5 | 595-SN74LVC1G08DBVR | 296-11601-1-ND | C7666 | PM SW2 red blink gate. Also reused as the Stator reset/apply gate (`SYS_RESET_N` AND `CFG_APPLY_N` -> `DEV_CLRN`). Single 2-input positive AND gate, 1.65–5.5V supply, push-pull output, 5.5V-tolerant inputs. |
| U9 | TPS2372-4RGWR | VQFN-20 | **595-TPS2372-4RGWR** (provided) | **296-52795-1-ND** ✓ | C470955 | 🔒 DigiKey stock verified. $3.09/1. VQFN-20 per TI. |
| U10 | TPS23730RMTR | WQFN-20 | **595-TPS23730RMTR** ✓ | **296-TPS23730RMCT-ND** ✓ | C3189530 | 🔒 ACF PoE+ DC-DC controller; PSR mode; 12V output; WQFN-20 package. ✅ Resolved (see §9.0 item 2). |
| D2 | TPD2E2U06DRLR | SOT-553 (DRL) | **595-TPD2E2U06DRLR** ✓ | **296-38361-1-ND** ✓ | C1972959 | 🔒 DigiKey 1.4k in stock @ $0.41/1. Dual-channel SMBus ESD, 5.5V. Part confirmed to exist. Farnell stocked (3116500). |
| Ethernet / PoE entry connector (Controller) | Würth 7499111121A | THT RJ45 | **710-7499111121A** ✓ | **1297-1070-5-ND** ✓ | C5523983 | 🔒 Controller-owned Ethernet / PoE entry connector. Mouser ~191, DigiKey ~879 in stock. ~$8.41/1 (Mouser), ~$8.41/1 (DigiKey). Farnell out of stock. JLCPCB C5523983 — hand-place or pre-fit. |
| J4 | Molex 0436500519 (43650-0519) | THT Micro-Fit 3.0 | 538-43650-0519 | WM14587-ND | C563849 | 🔒 Full Molex PN: 0436500519; short form 43650-0519. 5-circuit, 1-row, gold contacts, board lock, 3mm pitch. Farnell ~1143 in stock. JLCPCB C563849 confirmed. |
| J5 | GCT USB4135-GF-A | SMT vertical 8.94×3.5mm | 640-USB4135-GF-A | 2073-USB4135-GF-ACT-ND | C5438410 | 🔒 6-position USB Type-C receptacle (power only), 5A VBUS, CC1/CC2 included. Connects to STUSB4500 (U5) for 15V PD negotiation. JLCPCB C5438410. |
| Q1, Q2, Q3 | TI CSD17483F4T (×3) | SON-8 3.3×3.3mm | 595-CSD17483F4T | 296-37781-1-ND | C2871105 | 🔒 N-ch MOSFET, 30V, 10A, 8.4mΩ. Driven by LM74700-Q1 controllers **U6a/U6b/U6c** for triple-input ideal-diode OR-ing (PoE / USB-C / Battery). One controller + one MOSFET per input path. |
| R14, R15 | Panasonic ERA-3ARB series | 0603 0.1% Thin-Film | See PN below | See PN below | — | 🔒 R14 (ERA-3ARB3012V, Mouser 667-ERA-3ARB3012V, DigiKey 10-ERA-3ARB3012VCT-ND, JLCPCB C1728516). R15 (ERA-3ARB103V, Mouser 667-ERA-3ARB103V, DigiKey P10KBDCT-ND, JLCPCB C465746). BACKUP pin voltage divider for LTC3350 (U3). R14=30.1kΩ, R15=10.0kΩ. Sets BACKUP trigger at 4.812V (312mV above MCP121T 4.50V — see DEC-030). |
| R30 | ERA-2AEB3322X 33.2kΩ 1% 0402 | 0402 1% Thick-Film | 667-ERA-2AEB3322X | P33.2KDCCT-ND | C2087909 | 🔒 LTC3350 RT frequency-setting resistor — sets 400 kHz switching frequency (vs default 200 kHz with RT=INTVCC). Required for ≥4-cycle backup switchover window. See DEC-030. |
| U11 | MIC1555YM5-TR | SOT-23-5 | 998-MIC1555YM5TR | 576-2576-1-ND | C145373 | 🔒 CMOS timer IC (Microchip). 1Hz hardware status LED oscillator. R16=10kΩ (ERJ-3EKF series), R17=715kΩ (ERJ-3EKF7153V, Mouser 667-ERJ-3EKF7153V), C23=1µF (same Kemet C0805C105K5RACTU as C21/C22). |
| U15 | MIC1555YM5-TR | SOT-23-5 | 998-MIC1555YM5TR | 576-2576-1-ND | C145373 | 🔒 CMOS timer IC (Microchip). Monostable one-shot for hardware PWR_BUT shutdown. t=1.1×R28×C42=3.01s. R28=274kΩ (ERJ-3EKF2743V), C42=10µF 16V X7R (CC1206KKX7R8BB106), C38=100nF bypass cap. |
| R18–R21 | RJ45 Bob Smith termination resistors (×4) — 75Ω ±1% 0402 | 0402 | 667-ERJ-2RKF75R0X | P75.0LCT-ND | C413061 | 🔒 |
| CTL C25 | RJ45 Bob Smith termination capacitor — 10nF 100V X7R 0402 (⚠️ Y1-class 0402 is rare; 100V X7R acceptable proxy for EMC transient margin — Ethernet ESD discharge path to chassis) | 0402 | 80-C0402C103K1RAUTO | 399-C0402C103K1RACAUTOCT-ND | C19862710 | 🔒 |

### 9.0. Part Number Issues Requiring Action

1. **U6** — Replace `LM74700-Q1DCKR` with **`LM74700QDBVRQ1`** everywhere in schematics and BOM. The DCK (SC70) package does not exist for this part; DBV (SOT-23-6) is the correct package.
2. **U10** — ✅ Resolved: TPS23730 correct package is **RMTR (WQFN-20)** — MPN updated to `TPS23730RMTR` in BOM and Design_Spec.
3. **U1** — Updated to `TPS259804ONRGER` (16.9V silicon-fixed OVLO VQFN-24 variant). Mouser/DigiKey/JLCPCB PNs confirmed. R3 repurposed as R_ILIM = 210 Ω (ERA-3VEB2100V, 0.1% thin-film).
4. **U4** — Replaced with TPS25751DREFR (WQFN-38 6×4mm). See DEC-012. Package differs from TPS25750 QFN-28; KiCad symbol/footprint to be created at schematic capture.

## 10. Suppliers

Reference information for placing orders with key component suppliers.

| # | Supplier | Role | Website | Notes |
| :--- | :--- | :--- | :--- | :--- |
| S01 | **Mouser Electronics** | Global distributor (primary) | [mouser.co.uk](https://www.mouser.co.uk) | Free next-day delivery on orders over £50. Wide TI/ADI/Microchip stock. Use part numbers from `Mouser Part #` column in board BOM tables. |
| S02 | **Farnell** | Global distributor (secondary UK) | [uk.farnell.com](https://uk.farnell.com) | Same-day dispatch for most stock lines. Good for Samtec, Würth, Bourns, Coilcraft. |
| S03 | **DigiKey** | Global distributor (USA-based, fast to UK) | [digikey.co.uk](https://www.digikey.co.uk) | Good for ADI (LTC3350), TI (low-MOQ), STMicroelectronics (STUSB4500). |
| S04 | **Coilcraft** | Transformer / inductor manufacturer | [coilcraft.com](https://www.coilcraft.com) | Order T2 (`POE600F-12L`; `D` suffix = packaging only) direct from Coilcraft. Treat as a consignment part. Minimum order 1 unit. Sample requests available. UK-friendly shipping. |
| S05 | **Texas Instruments** | IC manufacturer (TI store) | [ti.com/store](https://www.ti.com/store) | For TI parts (TPS2372-4, TPS23730, TPS25980, LMQ61460AFSQRJRRQ1, LM74700-Q1, TPS25751DREFR, TPS75733). Samples available via ti.com. |
| S06 | **Analog Devices (ADI)** | IC manufacturer | [analog.com](https://www.analog.com) | For LTC3350 supercap manager. Samples available. |
| S07 | **STMicroelectronics** | IC manufacturer | [st.com](https://www.st.com) | For STUSB4500 USB-C sink controller. Samples and eval kits available. |
| S08 | **Samtec** | Connector manufacturer | [samtec.com](https://www.samtec.com) | For ERF8/ERM8 rotor-family BtB connectors only (Rotor / Reflector / Extension interfaces). Order direct or via Farnell/Mouser. |
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
| U1 | TPS259804ONRGER — eFuse 16.9V silicon-fixed OVLO | Texas Instruments | [TPS25980-datasheet.md](../Datasheets/TPS25980-datasheet.md) |
| U2A, U2B | LMQ61460AFSQRJRRQ1 — 6A Sync Buck (AEC-Q100) | Texas Instruments | [lmq61460-q1-datasheet.md](../Datasheets/lmq61460-q1-datasheet.md) |
| U3 | LTC3350EUHF#PBF — Supercap Manager / Charger / Backup | Analog Devices | [ltc3350-datasheet.md](../Datasheets/ltc3350-datasheet.md) |
| U4 | TPS25751DREFR — USB PD 3.1 DRP Controller | Texas Instruments | [tps25751-datasheet.md](../Datasheets/tps25751-datasheet.md) |
| U5 | STUSB4500LQTR — USB-C Sink PD Controller | STMicroelectronics | [stusb4500l-datasheet.md](../Datasheets/stusb4500l-datasheet.md) |
| U6 | LM74700QDBVRQ1 — Ideal-Diode OR-ing Controller | Texas Instruments | [lm74700-q1-datasheet.md](../Datasheets/lm74700-q1-datasheet.md) |
| U7 | TPS75733KTTRG3 — 3.3V 3A LDO (3V3_ENIG) | Texas Instruments | [tps757-datasheet.md](../Datasheets/tps757-datasheet.md) |
| U8 | MCP121T-450E/LB — 4.50V Voltage Supervisor | Microchip Technology | [MCP121-datasheet.md](../Datasheets/MCP121-datasheet.md) |
| U9 | TPS2372-4RGWR — IEEE 802.3bt PoE PD Controller | Texas Instruments | [tps2372-datasheet.md](../Datasheets/tps2372-datasheet.md) |
| U10 | TPS23730RMTR — ACF PoE+ DC/DC Controller | Texas Instruments | [tps23730-datasheet.md](../Datasheets/tps23730-datasheet.md) |
| U11, U15 | MIC1555YM5-TR — CMOS Timer / LED Oscillator | Microchip Technology | [MIC1555-datasheet.md](../Datasheets/MIC1555-datasheet.md) |
| U12 (PM), U2 (STA) | INA219AIDR — Zero-Drift Power Monitor | Texas Instruments | [INA219-datasheet.md](../Datasheets/INA219-datasheet.md) |
| U16 (PM) | PCA9534APWR — 8-bit I²C GPIO Expander | Texas Instruments | [pca9534a-datasheet.md](../Datasheets/pca9534a-datasheet.md) |
| U13, U14, U17 | NL27WZ14DFT2G-Q — Automotive Dual Schmitt Inverter | onsemi | [NL27WZ14-D.md](../Datasheets/NL27WZ14-D.md) |
| U2 (CTL) | TPS2065CDBVR — USB Power Switch 1.6A | Texas Instruments | [tps2065c-datasheet.md](../Datasheets/tps2065c-datasheet.md) |
| U3 (CTL) | AP2331W-7 — HDMI Current Limiter | Diodes Inc. | [AP2331-datasheet.md](../Datasheets/AP2331-datasheet.md) |
| D3 (PM); U4-U6 (CTL) | TPD4E05U06QDQARQ1 — 4-Channel ESD Array | Texas Instruments | [tpd4e05u06-q1-datasheet.md](../Datasheets/tpd4e05u06-q1-datasheet.md) |
| D2 | TPD2E2U06DRLR — Dual 5.5V SMBus ESD | Texas Instruments | [tpd2e2u06-datasheet.md](../Datasheets/tpd2e2u06-datasheet.md) |
| D1 | TPD1E10B06DYARQ1 — Single-ch 10V TVS ESD, SOD-523 | Texas Instruments | [tpd1e10b06-q1-datasheet.md](../Datasheets/tpd1e10b06-q1-datasheet.md) |
| C25 (CTL), C40 (PM) | C0402C103K1RACAUTO / C0402C101K3RACAUTO — KEMET automotive X7R MLCC family | KEMET | [KEM_C1023_X7R_AUTO_SMD-datasheet.md](../Datasheets/KEM_C1023_X7R_AUTO_SMD-datasheet.md) |
| U1 (EXT), U5 (JDB) | SN74LVC2G125DCUR — Dual 3-State Buffer | Texas Instruments | [sn74lvc2g125-datasheet.md](../Datasheets/sn74lvc2g125-datasheet.md) |
| U4-U5 (STA) | 74HC157PW-Q100,118 — Automotive quad 2:1 mux | Nexperia | [74HC_HCT157_Q100-datasheet.md](../Datasheets/74HC_HCT157_Q100-datasheet.md) |
| U1 (JDB) | FT232HL-REEL — USB 2.0 MPSSE Bridge | FTDI | [FT232H-datasheet.md](../Datasheets/FT232H-datasheet.md) |
| U1 (ENC/STA/ROT) | EPM570T100I5N — Intel MAX II CPLD 570 LE | Intel (Altera) | [Intel_max2_cpld-handbook.md](../Datasheets/Intel_max2_cpld-handbook.md) |
| U2/U3/U4 (ROT) | FDC2114RGHR — 4-ch Capacitive Sensor IC ⚠️ MOQ 4500 at distributors; MOQ 2 at JLCPCB | Texas Instruments | [fdc2112-datasheet.md](../Datasheets/fdc2112-datasheet.md) *(FDC2x1x family datasheet covering FDC2114)* |
| U1 (CTL) | CM5 — Raspberry Pi Compute Module 5 | Raspberry Pi Ltd | [RPi-cm5-datasheet.md](../Datasheets/RPi-cm5-datasheet.md) |
| Q1–Q3 | CSD17483F4T — N-ch MOSFET 30V/10A, SON-8 | Texas Instruments | [csd17483f4-datasheet.md](../Datasheets/csd17483f4-datasheet.md) |
| Q4, Q5 | BSS138 — N-ch Logic MOSFET 50V, SOT-23 | onsemi | [BSS138-onsemi-datasheet.md](../Datasheets/BSS138-onsemi-datasheet.md) |
| BAT54 | BAT54 — Schottky Diode, SOT-23 | Generic / multi-source | [bat54-diotec-datasheet.md](../Datasheets/bat54-diotec-datasheet.md) |
| T2 | POE600F-12L — Active Clamp Flyback Transformer (`D` suffix = packaging only) | Coilcraft | [coilcraft-poe600f-datasheet.md](../Datasheets/coilcraft-poe600f-datasheet.md) |
| L1, L2 | WE-CMBNC 7448031002 — Nanocrystalline CMC | Würth Elektronik | [WE-CMBNC-7448031002-datasheet.md](../Datasheets/WE-CMBNC-7448031002-datasheet.md) |
| L3 | SRP1265A-100M — 10µH 14A Power Inductor | Bourns | [srp1265a-datasheet.md](../Datasheets/srp1265a-datasheet.md) |
| R12 / R_SENSE | CSS2H-2512R-R010ELF — 10mΩ Kelvin Shunt | Bourns | [bourns.com/CSS2H](https://www.bourns.com/products/resistors/current-sense-resistors/product/CSS2H) |
| F1 | AC72ABD — 72C SMD Thermal Cutoff | Bourns | [Bourns-AC72ABD-datasheet.md](../Datasheets/Bourns-AC72ABD-datasheet.md) |
| J1/J2/J3 (PM) | 1123684-7 — 10-pin 2.5mm board-to-board dock header | TE Connectivity | [TE-1123684-7-datasheet.md](../Datasheets/TE-1123684-7-datasheet.md) |
| J3 (PM) | 43650-0519 — Micro-Fit 3.0, 5-pin Vertical THT | Molex | [Molex-PS-43650-datasheet.md](../Datasheets/Molex-PS-43650-datasheet.md) |
| J4 (PM) | USB4135-GF-A — USB Type-C SMT Receptacle, 5A | GCT | [usb4135-datasheet.md](../Datasheets/usb4135-datasheet.md) |
| J6 (CTL) | 48406-0003 — USB 3.0 Type-A Dual-Stack | Molex | [Molex-48406-0003-datasheet.md](../Datasheets/Molex-48406-0003-datasheet.md) |
| J7 (CTL) | 2007435-1 — HDMI Type-A Full-Size | TE Connectivity | [TE-2007435-1-datasheet.md](../Datasheets/TE-2007435-1-datasheet.md) |
| J9 (CTL) | F52Q-1A7H1-11015 — 15-pin 1.0mm right-angle ZIF/FPC connector | Amphenol | [amphenol_ffc_fpc_100mm_f52q_f52r-datasheet.md](../Datasheets/amphenol_ffc_fpc_100mm_f52q_f52r-datasheet.md) |
| J\_CM5\_A/B (CTL) | 10164227-1004A1RLF — 100-pin B2B SO-DIMM Socket 4.0mm | Amphenol | [Amphenol-10164227-1004A1RLF-datasheet.md](../Datasheets/Amphenol-10164227-1004A1RLF-datasheet.md) |
| J1/J2/J3 (CTL) | 1-1674231-1 — 10-pin 2.5mm board-to-board dock receptacle | TE Connectivity | [TE-1-1674231-1-datasheet.md](../Datasheets/TE-1-1674231-1-datasheet.md) |
| J4/J5 (CTL) / J11/J12 (STA) | 2195630015 / 2195620015 — EXTreme Guardian HD hybrid dock pair | Molex | [Molex-2195630015-datasheet.md](../Datasheets/Molex-2195630015-datasheet.md) |
| J4/J5 (CTL) | 2195630015 — EXTreme Guardian HD receptacle mechanical drawing | Molex | [Molex-2195630015-drawings.md](../Datasheets/Molex-2195630015-drawings.md) |
| J11/J12 (STA) | 2195620015 — EXTreme Guardian HD plug mechanical drawing | Molex | [Molex-2195620015-drawings.md](../Datasheets/Molex-2195620015-drawings.md) |
| J4/J5 / J11/J12 family | EXTreme Guardian HD product family specification | Molex | [Molex-ExtremeGuardianHD-2141130000-PS-000-specification.md](../Datasheets/Molex-ExtremeGuardianHD-2141130000-PS-000-specification.md) |
| C_SC1–8 (PM) | ADCR-T02R7SA256MB — 25F 2.7V Supercapacitor, THT Radial Can | Abracon | [ADCR-T02R7S-datasheet.md](../Datasheets/ADCR-T02R7S-datasheet.md) |
| SW1/SW2/SW3 (ROT) | 219-6LPSTR — 6-position DIP switch, 2.54mm THT | CTS | [CTS-Switches-DIP-219-Series-Datasheet.md](../Datasheets/CTS-Switches-DIP-219-Series-Datasheet.md) |
| J4–J9 (STA), J2 (ENC) | BHR-20-VUA / 2BHR-20-VUA — 20-pin 2×10 shrouded box header, 2.54mm | Adam Tech | [bhr-xx-vua-data-sheet.md](../Datasheets/bhr-xx-vua-data-sheet.md) |
| J10 (STA), J4 (REF), J7/J8 (EXT) | BHR-20-VUA / 2BHR-20-VUA — 20-pin 2×10 shrouded box header, 2.54mm | Adam Tech | [bhr-xx-vua-data-sheet.md](../Datasheets/bhr-xx-vua-data-sheet.md) |
| J11/J16 (CTL), J9/J10 (EXT) | ERF8-005-05.0-S-DV-K-TR — 10-pin 2×5 0.8mm female socket | Samtec | [samtec-erm8-erf8-datasheet.md](../Datasheets/samtec-erm8-erf8-datasheet.md) |
| J1/J2 (AM) | ERM8-005-05.0-S-DV-K-TR — 10-pin 2×5 0.8mm male header | Samtec | [samtec-erm8-erf8-datasheet.md](../Datasheets/samtec-erm8-erf8-datasheet.md) |
| J1 (JDB) | PH1-05-UA — 1×5 2.54mm male pin header | Adam Tech | [ph1-xx-ua-data-sheet.md](../Datasheets/ph1-xx-ua-data-sheet.md) |
| J2 (JDB) | PH1-10-UA — 1×10 2.54mm male pin header | Adam Tech | [ph1-xx-ua-data-sheet.md](../Datasheets/ph1-xx-ua-data-sheet.md) |
| J12 (CTL) | RS1-05-G — 1×5 2.54mm female socket | Adam Tech | [rs1-xx-g-datasheet.md](../Datasheets/rs1-xx-g-datasheet.md) |
| J13 (CTL) | RS1-10-G — 1×10 2.54mm female socket | Adam Tech | [rs1-xx-g-datasheet.md](../Datasheets/rs1-xx-g-datasheet.md) |
| H_SW3 Board A (ROT) | PH1-07-UA — 1×7 2.54mm male pin header | Adam Tech | [ph1-xx-ua-data-sheet.md](../Datasheets/ph1-xx-ua-data-sheet.md) |
| H_SW3 Board B (ROT) | RS1-07-G — 1×7 2.54mm female socket | Adam Tech | [rs1-xx-g-datasheet.md](../Datasheets/rs1-xx-g-datasheet.md) |
| SW1-40 (ENC/HID) | uxcell-style DPDT 6-pin momentary push button switch | gadgetskingdom (eBay) | [Gadgetskingdom_DPDT_Keyboard_Switch_Pseudo_Datasheet.md](../Datasheets/Gadgetskingdom_DPDT_Keyboard_Switch_Pseudo_Datasheet.md) |
