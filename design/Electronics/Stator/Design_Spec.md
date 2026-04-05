# Enigma-NG Stator Board (Backplane)

**Status:** Draft
**Version:** v1.0.0
**Associated Hardware Revision:** Rev A
**Last Updated:** 2026-04-04

The Stator Board is the mechanical and electrical backbone of the rotor stack. It provides the high-current distribution and signal routing for the 30 modular rotors.

## 1. Overview

* **Stackup:** 4-Layer / 2oz Finished Copper.
* **Layer Mapping:** L1: Signal (JTAG/routing) | L2: GND | L3: 3V3_ENIG | L4: ENIG Data.
* **Role:** Master Switchboard for the 30-rotor stack and peripheral encoder boards.

## 2. Core Features

* **Modular Slots:** 30x Samtec ERF8 female socket sets (3 connectors per slot: ERF8-005 JTAG, ERF8-005 Power, ERF8-010 ENC\_DATA) mating with the ERM8 male headers on each Rotor.
* **Power Tree:** A 2oz copper pour for the `+3V3_ENIG` rail to handle the **2.20A worst-case** load without voltage sag (see `design/Electronics/Power_Budgets.md`).
  The 5A figure previously quoted was a conservative design margin; the LDO hard limit is 3.0A.

### GND_CHASSIS Single-Point Bond

Per `design/Standards/Global_Routing_Spec.md §4`, each PCB in the Enigma-NG system must have a documented single-point GND_CHASSIS bond at its power entry connector.

**Stator GND_CHASSIS bond point:** The GND_CHASSIS connection is made at the LINK-BETA connector
(J4 or equivalent power input connector receiving 5V_MAIN and 3V3_ENIG from the Power Module via the BtB rotor stack).
A single 0 Ω bond resistor (or direct via) in a dedicated keepout zone connects the signal/power GND plane
to the chassis copper pour at this entry point. No additional chassis bonds are made on this board to avoid ground loops.

## 3. Encryption & JTAG Hub

* **CPLD:** Intel MAX II EPM240T100C5N CPLD (Logic Router).
* **Decoupling Rule:** Use **8x 0.1µF X7R** local decoupling capacitors per EPM240T100C5N IC (one per VCC pin).
* **Bulk Entry Bank Rule:** Use **5x 10uF X7R 50V** bulk decoupling capacitors near the Link-Beta power-entry pins in a **Symmetrical Star/Spoke pattern**.
* **Ferrite Bead Rule:** Use **4x ferrite beads** (one per 3V3_ENIG rotor feed) between Link-Beta entry and rotor power distribution to isolate switching transients from Controller logic.
* **Current Margin Check:** Rotor rail is budgeted at **1.50A typical** (30 rotors × 50mA — see `design/Electronics/Power_Budgets.md`); with 4 parallel feeds this is ~**375mA per bead** nominal sharing,
  well within the **3.5A** bead rating. Total 3V3_ENIG worst case including all CPLDs and encoders: 2.20A (27% headroom vs 3.0A LDO).
* **JTAG Return:** Includes 10kΩ pull-up on TDO_RETURN at the Link-Beta exit (R2).
* **JTAG Pull Resistors (×4, placed near Stator CPLD U1):**
  * **TMS:** 10kΩ pull-up to 3V3_ENIG (R3) — ensures JTAG TAP resets to Test-Logic-Reset on power-up and when controller is idle.
  * **TDI:** 10kΩ pull-up to 3V3_ENIG (R4) — holds TDI at logic-1 (BYPASS) when not actively driven by the Controller.
  * **TCK:** 10kΩ pull-down to GND (R5) — prevents spurious clocking when TCK line is floating.
  * **SYS_RESET_N:** 10kΩ pull-up to 3V3_ENIG (R6) — active-low signal; pull-up ensures CPLD remains
    out of reset by default.
* **JTAG Trace Width Rule:** All JTAG signal traces on L1 (TCK, TMS, TDI, TDO, SYS_RESET_N) shall
  be routed at **0.127 mm (5 mil)** width over the L2 GND plane, targeting **50 Ω controlled
  impedance**. See `design/Electronics/Investigations/JTAG_Integrity.md` and DEC-016.
* **JTAG Series Termination at Encoder Port Outputs (R7–R15):** 75 Ω series resistors placed within
  2 mm of each J6/J7/J8 connector pad **on the Stator PCB**, targeting 95 Ω source impedance to match the ~100 Ω IDC
  ribbon cable:
  * **R7, R8, R9:** TCK → J6, J7, J8 respectively.
  * **R10, R11, R12:** TMS → J6, J7, J8 respectively.
  * **R13:** Stator CPLD TDO → J6 TDI (HID encoder cable drive). Placed on Stator within 2 mm of J6 pin 13.
  * **R14:** J6 TDO return → J7 TDI (Plugboard A cable drive). Placed on Stator within 2 mm of J7 pin 13, on the
    trace carrying J6's TDO return signal.
  * **R15:** J7 TDO return → J8 TDI (Plugboard B cable drive). Placed on Stator within 2 mm of J8 pin 13, on the
    trace carrying J7's TDO return signal.
  * All R13–R15 are **Stator-side** resistors — no series resistors are required at the Encoder cable inputs.
* **Reset:** Pin 100 (DEV_CLRN) tied to the global SYS_RESET_N rail.

## 4. Interconnects

* **Controller Link (Link-Beta):** The **40-pin ERM8-020-05.0-S-DV-K-TR** male header on the Stator Board plugs into the matching ERF8-020 female socket on the Controller Board.
  * **Data In:** Receives JTAG, Reset from Controller.
  * **Data Out:** Transmits 12-bit Sniffer data to Controller.
  * **Power:** Receives 3V3_ENIG via the Controller pass-through for all backplane CPLDs.
  * **Cross-ref:** See `Controller/Design_Spec.md` Link-Beta mapping for explicit pin-number allocation; this Stator document mirrors that mapping for compatibility and implementation validation.
* **Encoder Interconnects:** 40-pin (2x20) 2.54mm Shrouded Box Headers (Power, ENC_DATA, JTAG).
* **Reflector/Extension Interconnect:** 16-pin (2x8) Vertical Shrouded Header (Power, ENC_DATA, TDO_Return).
  * **Routing:** Cables secured to the chassis floor with conductive EMI tape.
  * Extension boards enable daisy chaining this interconnect (to enable multi-stack rotor configurations).
  * **Cross-ref:** For matching interconnect pinouts on power (3V3_ENIG/GND), ENC_IN/ENC_OUT, and JTAG TDO_RETURN lines used for reflector loopback/plugboard mapping, See:
    * `Extension/Design_Spec.md`
    * `Reflector/Design_Spec.md`
* **Rotor Interconnect:** Each of the 30 rotor slots uses 3 ERF8 female sockets (FEMALE, mating with ERM8 MALE headers on each Rotor PCB).
  * **JTAG:** ERF8-005-05.0-S-DV-K-TR (10-pin 2×5, 0.8mm pitch) — TCK, TMS, TDI, TDO, SYS\_RESET\_N with interleaved GND.
  * **Power:** ERF8-005-05.0-S-DV-K-TR (10-pin 2×5, 0.8mm pitch) — 5× 3V3\_ENIG, 5× GND. Same part as JTAG socket.
  * **ENC DATA:** ERF8-010-05.0-S-DV-K-TR (20-pin 2×10, 0.8mm pitch) — ENC\_IN\[0:5\], ENC\_OUT\[0:5\], 8× GND fill.
  * **Cross-ref:** Authoritative pinout is defined in `Rotor/Design_Spec.md §3.4` (DEC-018 ownership).
* **Diagnostics:** 2x8 ENIG Gold Diagnostic Looped Probe Pad Bank (L1, Mirror of Controller).

## 5. Power Telemetry (The "Encryption Load")

* **Purpose:** Provides real-time current/voltage data for the 30-rotor stack to the CM5 GUI.
* **Sensor:** TI INA219 Zero-Drift Power Monitor (Address: 0x45) — dedicated rotor-stack usage telemetry.
* **Placement:** Inserted on L1 (Top Layer) connected to the 3V3_ENIG rail immediately before the rotor stack.
  * Minimum 15mm isolation from Intel MAX II EPM240T100C5N CPLD logic core.
* **Shunt:** 20mΩ (1%) 0805 Current Sense Resistor (Rated for 2A continuous).
* **Interface:** I2C-1 Telemetry Bus (via Link-Beta, Shared with Power Module).
* **Filtering:** 0.1µF decoupling and RC filter on IN+/IN- for noise suppression from mechanical rotors.

## 6. EMI & Mechanical

* **Shield Mount:** 10mm ENIG Gold landing strip on L1 edge bonded to GND_CHASSIS.
* **Clamping:** Dual 3.2mm PTH anchors per cable for Galvanised Steel Bar compression.
* **Diagnostics:** 2x10 ENIG Gold Looped Probe Pad Bank mirrored to Controller's Bank-Beta pinout for A-B signal verification.

---

## 7. Bill of Materials

| Ref | Component | Value | Package | Mouser Part # | DigiKey Part # | JLCPCB Part # |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| C1-C8 | Decoupling (8 per CPLD) | 0.1µF (X7R) **10V** | 0402 | 81-GRM155R71A104KE1D | 311-1424-1-ND | C49678 |
| C9-C13 | Bulk entry decoupling bank (star/spoke) | 10uF X7R 50V | 1206 | 187-CL31B106KBHNNNE | 1276-6767-1-ND | CL31B106KBHNNNE |
| J1 | Link-Beta Connector (MALE header — mates with ERF8-020 female socket on Controller) | ERM8-020-05.0-S-DV-K-TR | 40-pin | 200-ERM8020050SDVKTR | SAM8611CT-ND (CT) / SAM8611TR-ND (T&R) / SAM8611DKR-ND (DKR) | C138400 |
| J2–J4 | Rotor Interface sockets (×3 types per rotor slot, ×30 slots = 90 total) — **cross-ref Rotor/Design_Spec.md §3.4 for pinout** | ERF8-005 (JTAG ×30), ERF8-005 (Power ×30), ERF8-010 (ENC\_DATA ×30) — FEMALE sockets mating with ERM8 MALE headers on Rotor | 10-pin / 10-pin / 20-pin 0.8mm pitch | 200-ERF8005050SDVKTR (J2+J3) / 200-ERF8010050SDVKTR (J4) | SAM13517CT-ND (J2+J3 CT) / SAM8618CT-ND (J4 CT) | C7273978 (J2+J3) / C3646170 (J4) |
| J5 | 16-pin Reflector/Extension port | 2x8 2.54mm shrouded | through-hole | 538-22-23-2161 | WM2907-ND | ??? |
| J6–J8 | Encoder port connectors (×3 positions: HID + Plugboard A + Plugboard B) | 26-pin 2×13 2.54mm shrouded | through-hole | 538-22-23-2261 | WM2913-ND | ??? |
| L1-L4 | Rotor rail ferrite bead bank | 120 Ohm @ 100MHz, 3.5A | 1206 | 81-BLM31PG121SN1L | 490-1056-1-ND | BLM31PG121SN1L |
| R1 | Shunt Resistor | 20mΩ (1%) 0.5W | 0805 | 667-ERJ-6ENF20R0V | P20.0MYCT-ND | C123465 |
| R2 | JTAG TDO_RETURN pull-up | 10kΩ (1%) | 0603 | 667-ERJ-3EKF1002V | P10.0KBYCT-ND | C25804 |
| R3 | TMS pull-up to 3V3_ENIG | 10kΩ (1%) | 0603 | 667-ERJ-3EKF1002V | P10.0KBYCT-ND | C25804 |
| R4 | TDI pull-up to 3V3_ENIG | 10kΩ (1%) | 0603 | 667-ERJ-3EKF1002V | P10.0KBYCT-ND | C25804 |
| R5 | TCK pull-down to GND | 10kΩ (1%) | 0603 | 667-ERJ-3EKF1002V | P10.0KBYCT-ND | C25804 |
| R6 | SYS_RESET_N pull-up to 3V3_ENIG | 10kΩ (1%) | 0603 | 667-ERJ-3EKF1002V | P10.0KBYCT-ND | C25804 |
| R7 | TCK series R → J6 encoder port | 75Ω (1%) | 0603 | 667-ERJ-3EKF75R0V | P75.0BYCT-ND | C105905 |
| R8 | TCK series R → J7 encoder port | 75Ω (1%) | 0603 | 667-ERJ-3EKF75R0V | P75.0BYCT-ND | C105905 |
| R9 | TCK series R → J8 encoder port | 75Ω (1%) | 0603 | 667-ERJ-3EKF75R0V | P75.0BYCT-ND | C105905 |
| R10 | TMS series R → J6 encoder port | 75Ω (1%) | 0603 | 667-ERJ-3EKF75R0V | P75.0BYCT-ND | C105905 |
| R11 | TMS series R → J7 encoder port | 75Ω (1%) | 0603 | 667-ERJ-3EKF75R0V | P75.0BYCT-ND | C105905 |
| R12 | TMS series R → J8 encoder port | 75Ω (1%) | 0603 | 667-ERJ-3EKF75R0V | P75.0BYCT-ND | C105905 |
| R13 | TDI chain: Stator CPLD TDO → J6 TDI | 75Ω (1%) | 0603 | 667-ERJ-3EKF75R0V | P75.0BYCT-ND | C105905 |
| R14 | TDI chain: J6 TDO return → J7 TDI | 75Ω (1%) | 0603 | 667-ERJ-3EKF75R0V | P75.0BYCT-ND | C105905 |
| R15 | TDI chain: J7 TDO return → J8 TDI | 75Ω (1%) | 0603 | 667-ERJ-3EKF75R0V | P75.0BYCT-ND | C105905 |
| U1 | Stator Management CPLD | EPM240T100C5N | TQFP-100 | 989-EPM240T100C5N | 544-EPM240T100C5N-ND | C123470 |
| U2 | 3V3_ENIG Current/Voltage Sensing | INA219AIDR | **SOIC-8** | 595-INA219AIDR | 296-INA219AIDRCT-ND | C123466 |

> **Design decision history:** See `design/Design_Log.md` for all formal design decisions (DEC-xxx) applicable to this board.
