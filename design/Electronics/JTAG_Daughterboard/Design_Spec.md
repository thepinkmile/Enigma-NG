# JTAG Daughterboard (V1.0) Design Specification

**Status:** Draft
**Version:** v1.0.0
**Associated Hardware Revision:** Rev A
**Last Updated:** 2026-04-04

## 1. Overview

A high-speed USB-to-JTAG bridge module that allows the CM5 to natively program the 30-rotor CPLDs and the 4 I/O CPLDs.
This module replicates the functionality of an **Intel (Altera) USB Blaster II** on a tiny daughterboard.

## 2. Core Logic

* **Role:** Converts the CM5's USB 2.0 signals into high-speed JTAG (TCK, TMS, TDI, TDO) commands.
* **Bridge IC:** [FT232H](https://ftdichip.com/wp-content/uploads/2023/09/DS_FT232H.pdf) High-Speed USB 2.0 to MPSSE.
* **Function:** Dedicated JTAG programmer for the global chain (30x Rotor CPLDs + 3x Encoder CPLDs + 1x Stator CPLD).
* **Configuration:** 24MHz crystal-controlled for high-speed programming via the CM5 GUI.
* **Integrated Driver:** Compatible with `OpenOCD` or `Quartus` via a custom Linux driver on the CM5.

## 3. Interface & Wiring

* **Power + USB:** Internal **6-pin** header (J1: 3V3_ENIG, GND, VBUS, D−, D+, GND) connecting to the Controller Board's USB 2.0 Hub and 3V3_ENIG supply
  — see **JTAG_Daughterboard/Board_Layout.md** for pinout. GND_CHASSIS bond point is at J1.
* **JTAG Pinout (MPSSE Mode):**
  * AD0 -> **TCK** (Clock)
  * AD1 -> **TDI** (Data In)
  * AD2 -> **TDO** (Data Out)
  * AD3 -> **TMS** (State Machine)
* **Voltage:** 3.3V logic level with 5V-tolerant I/O.

### GND_CHASSIS Single-Point Bond

Per `design/Standards/Global_Routing_Spec.md §4`, each PCB must have a single-point GND_CHASSIS bond at its power entry connector.

**JTAG Daughterboard GND_CHASSIS bond point:** The GND_CHASSIS connection is made at J1
(the USB-B or BtB power input connector receiving 3V3_ENIG from the Controller board).
A single 0 Ω bond resistor (or direct via) connects signal GND to the chassis copper pour at this entry point only.

## 4. Aesthetics & Mounting

* **Visibility:** Completely hidden internally.
* **Mounting:** Small **4-layer** PCB (DEC-017) mounted via 3M VHB tape or standoffs near the Controller.

## 5. Electrical Requirements

* **Voltage:** Powered by the `+3V3_ENIG` rail from the Power Module via the BtB interconnect.
* **Bulk Entry Bank Rule:** Use **5x 10uF X7R 50V** bulk decoupling capacitors near the USB/power-entry pins in a **Symmetrical Star/Spoke pattern**.
* **Clocking:** Dedicated 24MHz crystal for the FT232H to ensure JTAG clock stability across the 37-device chain.
* **JTAG Signal Integrity:**
  * **R1, R2 (33Ω):** Series termination on FT232H TDI and TCK outputs, placed within 2mm of the FT232H pins before the JTAG header (J2).
    Source impedance ≈ 53Ω, matched to the 50Ω controlled-impedance traces on the receiving board. Per DEC-016 intra-board/BtB termination rule.
    See `design/Electronics/JTAG_Integrity.md`.
  * **Trace Width Rule:** All JTAG signal traces on L1 shall be routed at **0.127 mm (5 mil)** over the L2 GND plane, targeting **50 Ω controlled impedance**. See DEC-016.
  * **Pull Resistors:** TMS 10kΩ pull-up and TCK 10kΩ pull-down near J2 header to hold JTAG TAP in defined state when idle. See JTAG best-practice note in `design/Electronics/JTAG_Integrity.md`.

---

## 6. Bill of Materials

| Ref | Component | Value | Package | Mouser Part # | DigiKey Part # | JLCPCB Part # |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| C1-C4 | Decoupling | 0.1µF | 0402 | 81-GRM155R71A104KE1D | 311-1424-1-ND | C49678 |
| C5-C9 | Bulk entry decoupling bank (star/spoke) | 10uF X7R 50V | 1206 | 187-CL31B106KBHNNNE | 1276-6767-1-ND | CL31B106KBHNNNE |
| J1 | Power + USB header (3V3_ENIG, GND, VBUS, D−, D+, GND) | **6-pin** 2×3 shrouded | 2.54mm | 538-22-23-2061 | WM2899-ND | ??? |
| J2 | JTAG header | 10-pin | 2.54mm | 538-22-23-2101 | WM2901-ND | ??? |
| R1, R2 | Series resistors (DEC-016 BtB/intra-board termination — JTAG output to LINK-BETA) | 33Ω | 0603 | 667-ERJ-3EKF33R0V | P33.0BYCT-ND | C25819 |
| U1 | FT232H | USB 2.0 to MPSSE | QFN-56 | 895-FT232HL-REEL | 768-1014-ND | C123467 |
| Y1 | Crystal | 24MHz | HC-49 | 520-ABL-24.000MHZ-B2 | 644-1053-1-ND | C123468 |

> **Design decision history:** See `design/Design_Log.md` for all formal design decisions (DEC-xxx) applicable to this board.
