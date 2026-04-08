# JTAG Daughterboard (V1.0) Design Specification

**Status:** Draft
**Project:** Enigma-NG
**Author:** Izzyonstage & GitHub Copilot
**Version:** v1.0.0
**Associated Hardware Revision:** Rev A
**Last Updated:** 2026-04-05

## 1. Overview

A high-speed USB-to-JTAG bridge module that allows the CM5 to natively program the 30-rotor CPLDs and the 6 I/O CPLDs and 1 Mapping CPLD.
This module replicates the functionality of an **Intel (Altera) USB Blaster II** on a tiny daughterboard.

### Functional & Design Requirements

#### Functional Requirements

| ID | Functional Requirement | Notes | Satisfied By / Cross-Ref |
| :--- | :--- | :--- | :--- |
| FR-JDB-01 | Provide a USB-to-JTAG programming interface for all 37 CPLDs in the system | 1 Stator + 6 Encoder + 30 Rotor CPLDs | §2 Core Logic; BOM U1 (FT232H) |
| FR-JDB-02 | Generate series-damped drive signals suitable for the controlled-impedance JTAG chain | U5 buffers TCK/TMS; 33 Ω resistors at all JTAG outputs (R6/R7 after U5, R8 on TDI) | §6 Electrical Requirements; BOM U5, R6, R7, R8 |
| FR-JDB-03 | Interface with the CM5 via USB 2.0 for JTAG programming software control | Presented as FTDI JTAG device to OpenOCD via libftdi; no custom driver required | §3 Interface & Wiring; BOM J1 (INPUT 5-pin header), U1 (FT232H) |

#### Design Requirements

| ID | Design Requirement | Specification | Satisfied By / Cross-Ref |
| :--- | :--- | :--- | :--- |
| DR-JDB-01 | PCB stackup | 4-layer, 2oz finished copper (JLC04161H-7628) | §5 PCB Fabrication & Stackup |
| DR-JDB-02 | USB-to-JTAG bridge | FTDI FT232H (U1) in MPSSE mode | §2 Core Logic; BOM U1 (FT232H QFN-56) |
| DR-JDB-03 | TCK series damping at FT232H | R1 = 33 Ω 0402 at FT232H TCK output, before U5 buffer | §6 Electrical Requirements; BOM R1 |
| DR-JDB-04 | TDI series damping at FT232H | R2 = 33 Ω 0402 at FT232H TDI output | §6 Electrical Requirements; BOM R2 |
| DR-JDB-05 | TMS series damping at FT232H | R3 = 33 Ω 0402 at FT232H TMS output, before U5 buffer | §6 Electrical Requirements; BOM R3 |
| DR-JDB-06 | JTAG chain device count | 37 devices total (1 Stator CPLD + 6 Encoder CPLDs + 30 Rotor CPLDs) | §2 Core Logic; BOM U1 (FT232H) |
| DR-JDB-07 | USB interface | USB 2.0 Full Speed via CM5 internal USB port; D+/D− route via hat-header J1 | §3 Interface & Wiring; BOM J1 (5-pin INPUT header), Y1 (12MHz crystal) |
| DR-JDB-08 | Power source | 5V_USB and 3V3_ENIG from Controller Board via hat-header J1; FT232H self-powered USB mode | §6 Electrical Requirements |
| DR-JDB-09 | Hat-style connectors | J1 = 1×5 2.54mm female IDC (INPUT); J2 = 1×10 2.54mm female IDC (JTAG OUTPUT) | §3 Interface & Wiring; BOM J1, J2 |
| DR-JDB-10 | GND_CHASSIS not implemented | JDB is internal daughterboard; mounting holes tied to GND per DEC-022 | §3 Interface & Wiring |
| DR-JDB-11 | Bulk cap exception | JDB exempt from 5× bulk entry bank rule; C1–C4 per-IC decoupling + C5 4.7µF entry filter | §6 Electrical Requirements; BOM C1–C5 |
| DR-JDB-12 | JTAG buffer | U5 = SN74LVC2G125DCUR (SOT-23-6) dual-channel buffer for TCK and TMS; placed between FT232H and J2 header | §6 Electrical Requirements; BOM U5; DEC-023 |
| DR-JDB-13 | TCK series damping after buffer | R6 = 33 Ω 0402 after U5 TCK output, before J2 pin 1 (TCK) | §6 Electrical Requirements; BOM R6; DEC-023 |
| DR-JDB-14 | TMS series damping after buffer | R7 = 33 Ω 0402 after U5 TMS output, before J2 pin 7 (TMS) | §6 Electrical Requirements; BOM R7; DEC-023 |
| DR-JDB-15 | TDI series damping before J2 | R8 = 33 Ω 0402 before J2 pin 3 (TDI) | §6 Electrical Requirements; BOM R8; DEC-023 |
| DR-JDB-16 | TMS pull-up near J2 | R4 = 10 kΩ 0402 pull-up from TMS to 3V3_ENIG near J2 header; idle-state TAP control | §6 Electrical Requirements; BOM R4 |
| DR-JDB-17 | TCK pull-down near J2 | R5 = 10 kΩ 0402 pull-down from TCK to GND near J2 header; idle-state TAP control | §6 Electrical Requirements; BOM R5 |

## 2. Core Logic

* **Role:** Converts the CM5's USB 2.0 signals into standard JTAG signalling (TCK, TMS, TDI, TDO) commands.
* **Bridge IC:** [FT232H](https://ftdichip.com/wp-content/uploads/2023/09/DS_FT232H.pdf) High-Speed USB 2.0 to MPSSE.
* **Function:** Dedicated JTAG programmer for the global chain (30x Rotor CPLDs + 6x Encoder CPLDs + 1x Stator CPLD).
* **Configuration:** 12MHz crystal-controlled for stable JTAG programming via the CM5. See DEC-021.
* **Software Stack:** `ftdi_sio` kernel module for USB enumeration; `OpenOCD` with `libftdi` for JTAG/MPSSE
  operation (no custom driver required). CM5 enumerates the FT232H on Linux boot via `ftdi_sio`.

## 3. Interface & Wiring

### J1 — INPUT Header (5-Pin, USB/Power Side)

* **Type:** Single-row 2.54mm pitch female IDC header, 5 pins
* **Pinout:** Pin 1 = 5V_USB | Pin 2 = 3V3_ENIG | Pin 3 = D+ | Pin 4 = D− | Pin 5 = GND
* **Purpose:** System power in (5V_USB + GND from Controller Board TPS2065C-protected USB rail);
  JTAG signal voltage reference (3V3_ENIG from Controller Board); internal USB 2.0 data to CM5 (D+/D−)
* **Physical location:** One edge of the board (INPUT side)
* **JLCPCB:** C50950 (1×5 2.54mm female pin header) — see Board_Layout.md for full pinout

### J2 — JTAG OUTPUT Header (10-Pin)

* **Type:** Single-row 2.54mm pitch female IDC header, 10 pins
* **Physical location:** Opposing edge of the board (OUTPUT side), physically opposite J1
* **JLCPCB:** C2337 or equivalent 1×10 2.54mm female pin header — see Board_Layout.md for full pinout

> **No external connectors:** The JDB has no external connectors. USB is entirely internal via J1.
> No USB-C connector exists on the JDB. CC pins are irrelevant (USB 2.0 only).

### J2 JTAG Pinout (10-Pin, Interleaved GND)

| Pin | Signal | Description |
| :--- | :--- | :--- |
| 1 | TCK | JTAG Clock |
| 2 | GND | Ground |
| 3 | TDI | JTAG Data In |
| 4 | GND | Ground |
| 5 | TDO | JTAG Data Out |
| 6 | GND | Ground |
| 7 | TMS | JTAG Mode Select |
| 8 | GND | Ground |
| 9 | VREF (3V3_ENIG) | Voltage Reference |
| 10 | GND | Ground |

### FT232H JTAG Signal Mapping (MPSSE Mode)

* AD0 → **TCK** (Clock)
* AD1 → **TDI** (Data In)
* AD2 → **TDO** (Data Out)
* AD3 → **TMS** (State Machine)

### Voltage

3.3V logic level (VCCIO = 3V3_ENIG). FT232H VCC = 5V_USB. 5V-tolerant I/O.

### GND_CHASSIS Not Implemented

GND_CHASSIS is not implemented on the JDB — see DEC-022. The JDB is an internal daughterboard
with no chassis surface to bond to. Mounting holes connect to GND (circuit return), not GND_CHASSIS.

## 4. Aesthetics & Mounting

* **Visibility:** Completely hidden internally.
* **Mounting:** Small **4-layer** PCB (DEC-017) mounted as a hat on the Controller Board via conductive
  standoffs. Mounting holes tie to GND per DEC-022.

## 5. PCB Fabrication & Stackup

**Stackup:** JLC04161H-7628 (JLCPCB standard 4-layer, same as all other non-CTL/PM boards in the system)

| Layer | Role | Notes |
| :--- | :--- | :--- |
| L1 | GND plane + SMT component pads (component side) | Faces toward the Controller Board when JDB is mounted as a hat |
| L2 | All signal traces (inner layer) | Shielded between L1 GND reference and L3 power |
| L3 | Power distribution pours (5V_USB + 3V3_ENIG) | Inner power layer |
| L4 | GND pour shield | Faces away from the Controller (exterior/top when mounted) |

**Rationale:** Board mounts face-down on Controller (L1 toward Controller PCB). L4 GND provides exterior
shielding. L2 signals are sandwiched between two reference planes for good signal integrity. Single-side
assembly on L1 is consistent with JLCPCB SMT assembly requirements.

## 6. Electrical Requirements

* **Power Architecture:**
  * FT232H VCC = **5V_USB** (5V) via hat-header J1 Pin 1 — from the Controller Board's TPS2065C-protected
    USB power rail (same current-limited rail as the USB 3.0 ports, 1.6A limit).
  * FT232H VCCIO = **3V3_ENIG** (3.3V) via hat-header J1 Pin 2 — sets JTAG signal voltage to match
    CPLD I/O logic levels (same role as CM5 GPIO reference voltage).
  * FT232H VBUS pin tied to **5V_USB** (always-on; USB connection to CM5 is internal — no VBUS monitoring needed).
  * USB connection is **entirely internal**: D+ and D− travel from FT232H via J1 hat-header through the
    Controller Board PCB directly to the CM5 USB 2.0 port. No USB-C connector on the JDB.
  * FT232H operates in **self-powered USB mode** — power from system (5V_USB), not from USB host.
  * CM5 enumerates the FT232H when Linux boots and ftdi_sio loads; no JDB-side power sequencing required.
  * Controller TPS2065C is the upstream current limiter; no additional current limiter on JDB.
* **Bulk Capacitor Exception:** The JDB is exempt from the standard 5× bulk entry bank rule. The Controller
  Board upstream provides a fully-bypassed power rail. Per-IC decoupling per FT232H datasheet (C1–C4)
  plus a single 4.7µF entry filter (C5) on 5V_USB is sufficient.
* **Clocking:** Dedicated 12MHz SMD crystal (Y1) for the FT232H reference clock. The FT232H internal PLL requires 12MHz; CM5 GPCLK
  option was considered and rejected — see DEC-021. Crystal load capacitors C10–C11 (33pF C0G) set the 20pF crystal load capacitance.
* **JTAG Signal Integrity:**
  * **R1, R2 (33Ω):** Series termination on FT232H TCK and TDI outputs, placed within 2mm of the FT232H pins before the JTAG buffer (U5) / header (J2).
    Source impedance ≈ 53Ω, matched to the 50Ω controlled-impedance traces on the receiving board. Per DEC-016 intra-board/BtB termination rule.
    See `design/Electronics/Investigations/JTAG_Integrity.md`.
  * **R3 (33Ω):** Series damping on TMS output — same function as R1 (TCK) and R2 (TDI). All three JTAG drive outputs have series termination at the FT232H.
  * **U5 (SN74LVC2G125DCUR, SOT-23-6):** Dual-channel 3-state buffer placed between the FT232H and
    J2 header (JTAG OUTPUT), buffering TCK and TMS for the 37-device JTAG chain load. TDI is not
    buffered — FT232H TDI drives only the first device in the chain directly.
  * **R6 (33Ω):** Series damping on U5 TCK output, placed within 2mm of the U5 output pin, before
    J2 JTAG header (TCK pin). Source impedance after U5: U5_out (≈15Ω) + R6 (33Ω) ≈ 48Ω — matched
    to 50Ω BtB trace impedance per DEC-023.
  * **R7 (33Ω):** Series damping on U5 TMS output — same function as R6 (TCK). Placed before J2 (TMS pin).
  * **R8 (33Ω):** Series damping on TDI signal (not buffered) before J2 (TDI pin). Combined with R2 at FT232H, provides damping at both ends of the FT232H-to-J2 TDI path.
  * **Pull Resistors:** TMS 10kΩ pull-up (R4) and TCK 10kΩ pull-down (R5) near J2 header to hold JTAG TAP in defined state
    when idle (see §5 and JTAG best-practice note in `design/Electronics/Investigations/JTAG_Integrity.md`).
  * **Trace Width Rule:** All JTAG signal traces on L2 (signal layer) shall be routed at **0.127 mm (5 mil)** over the L1 GND reference plane, targeting **50 Ω controlled impedance**. See DEC-016.

> **Signal Integrity note (JDB as complete JTAG master):** The JDB hosts all JTAG buffering and
> termination for the system. U5 buffers TCK and TMS for the 37-device chain load. Series damping
> (R6–R8) at 33 Ω matches the BtB trace impedance (50 Ω) per DEC-016. LINK-BETA is a direct
> Board-to-Board connector (no cable) — 33 Ω applies throughout (not the 75 Ω cable-driving rule).
> The Controller board routes JTAG lines as pass-through without active components. See DEC-023.

## 7. Thermal & ESD

* **Thermal:** Low-power debug board; no thermal management required.
* **ESD:** ESD protection via U5 JTAG buffer (SN74LVC2G125DCUR). Standard PCB handling precautions apply.

---

## 8. Bill of Materials

| Ref | Component | Value | Package | Mouser Part # | DigiKey Part # | JLCPCB Part # |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| C1-C4 | Decoupling | 0.1µF X7R 50V | 0402 | 187-CL05B104KB5NNNC | 1276-1009-1-ND | C1525 |
| C5 | 5V_USB power-entry filter (hat-header J1 Pin 1, close to FT232H VCC) | 4.7µF X7R | 0402 | — | — | C19666 |
| J1 | INPUT header — 5V_USB, 3V3_ENIG, D+, D−, GND | 1×5 female IDC | 2.54mm | — | — | C50950 |
| J2 | JTAG OUTPUT header (10-pin interleaved GND) | 1×10 female IDC | 2.54mm | — | — | C2337 |
| R1 | Series termination on FT232H TCK output (before U5 buffer input) — DEC-016 | 33Ω 1% | 0402 | 667-ERJ-2RKF33R0X | P33.0ACCT-ND | C25808 |
| R2 | Series termination on FT232H TDI output (TDI not buffered) — DEC-016 | 33Ω 1% | 0402 | 667-ERJ-2RKF33R0X | P33.0ACCT-ND | C25808 |
| R3 | Series termination on FT232H TMS output (before U5 buffer input) — DEC-016 | 33Ω 1% | 0402 | 667-ERJ-2RKF33R0X | P33.0ACCT-ND | C25808 |
| R4 | TMS pull-up to 3V3_ENIG near J2 header — holds JTAG TAP in defined idle state per §6 | 10kΩ 1% | 0402 | 667-ERJ-2RKF1002X | P10.0ACCT-ND | C25744 |
| R5 | TCK pull-down to GND near J2 header — holds JTAG TAP in defined idle state per §6 | 10kΩ 1% | 0402 | 667-ERJ-2RKF1002X | P10.0ACCT-ND | C25744 |
| R6 | TCK series damping after U5 buffer output, before J2 pin 1 (TCK) — DEC-023 | 33Ω 1% | 0402 | 667-ERJ-2RKF33R0X | P33.0ACCT-ND | C25808 |
| R7 | TMS series damping after U5 buffer output, before J2 pin 7 (TMS) — DEC-023 | 33Ω 1% | 0402 | 667-ERJ-2RKF33R0X | P33.0ACCT-ND | C25808 |
| R8 | TDI series damping before J2 pin 3 (TDI) — DEC-023 | 33Ω 1% | 0402 | 667-ERJ-2RKF33R0X | P33.0ACCT-ND | C25808 |
| U1 | FT232H | USB 2.0 to MPSSE | QFN-56 | 895-FT232HL-REEL | 768-1014-ND | C123467 |
| U5 | SN74LVC2G125DCUR — dual-channel 3-state buffer for TCK and TMS drive (37-device chain load) — DEC-023 | Dual 3-state buffer | SOT-23-6 | 595-SN74LVC2G125DCUR | 296-SN74LVC2G125DCURCT-ND | C2688 |
| C10, C11 | Crystal load capacitors — **C0G/NP0 exception approved** (zero tempco mandatory for crystal load accuracy; X7R exhibits ≥5% capacitance shift with temperature, directly degrading oscillator frequency stability — this is the sole C0G exception in the design) | 33pF C0G/NP0 0402 | 0402 | 80-C0402C330J5GAUTO | 399-12979-1-ND | C2169327 |
| Y1 | Crystal — FT232H reference clock (per DEC-021) | 12MHz 20pF ±20ppm | SMD3225-4P | 815-ABM8-12.000MHZ-B2-T | 535-9977-1-ND | C9002 |
