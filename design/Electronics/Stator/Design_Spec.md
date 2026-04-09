# Stator Board (V1.0) Design Specification

**Status:** Draft
**Project:** Enigma-NG
**Author:** Izzyonstage & GitHub Copilot
**Version:** v1.0.0
**Associated Hardware Revision:** Rev A
**Last Updated:** 2026-04-05

The Stator Board is the mechanical and electrical backbone of the rotor stack. It provides the high-current distribution and signal routing for the 30 modular rotors.

## 1. Overview

* **Stackup:** 4-Layer / 2oz Finished Copper.
* **Layer Mapping:** L1: Signal (JTAG/routing) | L2: GND | L3: 3V3_ENIG | L4: ENC Data.
* **Role:** Master Switchboard for the 30-rotor stack and peripheral encoder boards.

### Functional & Design Requirements

#### Functional Requirements

| ID | Functional Requirement | Notes | Satisfied By / Cross-Ref |
| :--- | :--- | :--- | :--- |
| FR-STA-01 | Serve as the fixed mechanical and electrical backplane for the 30-rotor stack | Provides all power, JTAG, and data connectivity to rotors | §2 Core Features; BOM J1–J3 (ERF8 rotor sockets) |
| FR-STA-02 | Distribute 3V3_ENIG power to all 30 rotor slots simultaneously | Via 2oz copper pour on L3 | §2 Core Features; §3 Encryption & JTAG Hub; BOM L1–L4 (ferrite beads) |
| FR-STA-03 | Route the JTAG chain from the Controller Board through all 30 rotor slots in sequence | Serial daisy-chain; Stator CPLD is device 1 | §3 Encryption & JTAG Hub; BOM U1 (EPM240T100I5N) |
| FR-STA-04 | Receive TTD_RETURN from the Reflector and forward to the Controller Board | Via J7 (16-pin Molex) → Link-Beta pin 26 | §3 Encryption & JTAG Hub; BOM J7, R2 (10kΩ pull-up) |
| FR-STA-05 | Interface with up to 3 Encoder boards (1 HID + 2 Plugboard) via IDC ribbon cables; route 6-bit data bus to plugboard passes at configurable signal chain positions | J4 = HID; J5 = Plugboard Pass A (configurable); J6 = Plugboard Pass B (configurable) | §3 Plugboard Routing; §4 Interconnects; BOM J4–J6 (26-pin Molex IDC) |
| FR-STA-06 | Host a CPLD as the first device in the system JTAG chain | Intel MAX II EPM240 | §3 Encryption & JTAG Hub; BOM U1 (EPM240T100I5N) |
| FR-STA-07 | Connect to the Controller Board via the Link-Beta BtB connector | J8 = ERM8-020 male | §4 Interconnects; BOM J8 (ERM8-020-05.0-S-DV-K-TR) |

#### Design Requirements

| ID | Design Requirement | Specification | Satisfied By / Cross-Ref |
| :--- | :--- | :--- | :--- |
| DR-STA-01 | PCB stackup | 4-layer, 2oz finished copper (JLC04161H-7628) | §7 PCB Fabrication & Stackup |
| DR-STA-02 | Layer mapping | L1 = Signal (JTAG/routing), L2 = GND, L3 = 3V3_ENIG, L4 = ENC Data | §1 Overview |
| DR-STA-03 | Rotor interface (per slot) | J1 = ERF8-005 (JTAG), J2 = ERF8-005 (Power), J3 = ERF8-010 (ENC); 1 slot set | §4 Interconnects; BOM J1–J3 (ERF8-005/ERF8-010) |
| DR-STA-04 | Encoder interface | J4/J5/J6 = 26-pin Molex IDC (HID encoder ports, one per encoder board) | §4 Interconnects; BOM J4–J6 (Molex 26-pin) |
| DR-STA-05 | TTD_RETURN input | J7 = 16-pin Molex; TTD_RETURN on pin 15 (from Reflector J4) | §3 Encryption & JTAG Hub; BOM J7 (16-pin Molex) |
| DR-STA-06 | Link-Beta connector | J8 = ERM8-020-05.0-S-DV-K-TR (40-pin male, 0.8 mm pitch) to Controller J2 | §4 Interconnects; BOM J8 (ERM8-020-05.0-S-DV-K-TR) |
| DR-STA-07 | CPLD | Intel MAX II EPM240T100I5N (TQFP-100) | §3 Encryption & JTAG Hub; BOM U1 (EPM240T100I5N) |
| DR-STA-08 | Power monitoring | INA219 current sensor; shunt R1 = CSS2H-2512R-R010ELF (10mΩ 2512 Kelvin), rated ≥2.20 A | §5 Power Telemetry; BOM U2 (INA219AIDR), R1 (CSS2H 10mΩ shunt) |
| DR-STA-09 | Maximum 3V3_ENIG load | 2.20 A worst-case (30 rotors + Stator CPLD + all encoders) | §2 Core Features; §5 Power Telemetry |

## 2. Core Features

* **Modular Slots:** 1× Samtec ERF8 female socket set (3 connectors: ERF8-005 JTAG, ERF8-005 Power, ERF8-010 ENC\_DATA) mating with the ERM8 male headers on the Rotor.
* **Power Tree:** A 2oz copper pour for the `3V3_ENIG` rail to handle the **2.20A worst-case** load without voltage sag (see `design/Electronics/Power_Budgets.md`).
  The 5A figure previously quoted was a conservative design margin; the LDO hard limit is 3.0A.

### GND_CHASSIS Single-Point Bond

Per `design/Standards/Global_Routing_Spec.md §5`, each PCB in the Enigma-NG system must have a documented single-point GND_CHASSIS bond at its power entry connector.

**Stator GND_CHASSIS bond point:** The GND_CHASSIS connection is made at the LINK-BETA connector
(J8, ERM8-020, power input from Controller Board).
A single 0 Ω bond resistor (or direct via) in a dedicated keepout zone connects the signal/power GND plane
to the chassis copper pour at this entry point. No additional chassis bonds are made on this board to avoid ground loops.

## 3. Encryption & JTAG Hub

* **CPLD:** Intel MAX II EPM240T100I5N CPLD (Logic Router).
* Decoupling and bulk entry capacitor requirements per `design/Standards/Global_Routing_Spec.md §3`.
* **Ferrite Bead Rule:**Use **4x ferrite beads** (one per 3V3_ENIG rotor feed) between Link-Beta entry and rotor power distribution to isolate switching transients from Controller logic.
* **Current Margin Check:** Rotor rail is budgeted at **1.50A typical** (30 rotors × 50mA — see `design/Electronics/Power_Budgets.md`);
  with 4 parallel feeds this is ~**375mA per bead** nominal sharing,
  well within the **3.5A** bead rating. Total 3V3_ENIG worst case including all CPLDs and encoders: 2.20A (27% headroom vs 3.0A LDO).
* **JTAG Return:** Includes 10kΩ pull-up on TTD_RETURN at the Link-Beta exit (R2).
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
  2 mm of each J4/J5/J6 connector pad **on the Stator PCB**, targeting 95 Ω source impedance to match the ~100 Ω IDC
  ribbon cable:
  * **R7, R8, R9:** TCK → J4, J5, J6 respectively.
  * **R10, R11, R12:** TMS → J4, J5, J6 respectively.
  * **R13:** Stator CPLD TDO → J4 TDI (HID encoder cable drive). Placed on Stator within 2 mm of J4 pin 13.
  * **R14:** J4 TDO return → J5 TDI (Plugboard A cable drive). Placed on Stator within 2 mm of J5 pin 13, on the
    trace carrying J4's TDO return signal.
  * **R15:** J5 TDO return → J6 TDI (Plugboard B cable drive). Placed on Stator within 2 mm of J6 pin 13, on the
    trace carrying J5's TDO return signal.
  * All R13–R15 are **Stator-side** resistors — no series resistors are required at the Encoder cable inputs.
* **Reset:** Pin 100 (DEV_CLRN) tied to the global SYS_RESET_N rail.

## 4. Interconnects

* **Controller Link (Link-Beta):** The **40-pin ERM8-020-05.0-S-DV-K-TR** male header on the Stator Board plugs into the matching ERF8-020 female socket on the Controller Board.
  * **Data In:** Receives JTAG, Reset from Controller.
  * **Data Out:** Transmits 12-bit Sniffer data to Controller.
  * **Power:** Receives 3V3_ENIG via the Controller pass-through for all backplane CPLDs.
  * **Cross-ref:** See `Controller/Design_Spec.md` Link-Beta mapping for explicit pin-number allocation; this Stator document mirrors that mapping for compatibility and implementation validation.
* **Encoder Interconnects:** 26-pin (2×13) 2.54mm Shrouded Box Headers (Power, ENC_DATA, JTAG).
* **Plugboard Routing — Configurable Signal Chain Positions:**
  The Stator CPLD routes the 6-bit character data bus between the rotor stack, reflector, and the
  three encoder ports (J4/J5/J6). This enables plugboard passes (each provided by one Encoder board)
  to be inserted at any configurable point in the encryption signal chain — replicating any historical
  Enigma variant or enabling novel configurations unique to Enigma-NG.

  | Port | Default role | Plugboard signal chain position |
  | :--- | :--- | :--- |
  | **J4** | HID — Keyboard & Lightboard | Fixed: HID interface (not used for plugboard passes) |
  | **J5** | Plugboard Pass A | Configurable: any point in encryption chain |
  | **J6** | Plugboard Pass B | Configurable: any point in encryption chain |

  **Historical reference configurations:**

  | Configuration | J5 position | J6 position |
  | :--- | :--- | :--- |
  | Original Enigma (pre-war) | After Keyboard / before Rotor 1 | After last Rotor / before Lightboard |
  | Later Enigma models | At Reflector | — (not used; single pass) |
  | Enigma-NG custom | Any configured point | Any configured point |

  The Stator CPLD implements the routing matrix in VHDL. See `design/Electronics/Stator/Board_Layout.md`
  and `design/Electronics/Encoder/Design_Spec.md §1` for further detail.
* **Reflector/Extension Interconnect:**16-pin (2x8) Vertical Shrouded Header (Power, ENC_DATA, TTD_RETURN).
  * **Routing:** Cables secured to the chassis floor with conductive EMI tape.
  * Extension boards enable daisy chaining this interconnect (to enable multi-stack rotor configurations).
  * **Cross-ref:** For matching interconnect pinouts on power (3V3_ENIG/GND), ENC_IN/ENC_OUT, and JTAG TTD_RETURN lines used for reflector loopback/plugboard mapping, See:
    * `Extension/Design_Spec.md`
    * `Reflector/Design_Spec.md`
* **Rotor Interconnect:** The Stator provides 1 rotor slot (Rotor 1 input side) using 3 ERF8 female sockets.
  * **JTAG:** ERF8-005-05.0-S-DV-K-TR (10-pin 2×5, 0.8mm pitch) — TCK, TMS, TTD (TDI function on input side),
    SYS\_RESET\_N with interleaved GND. **J1 pin 6 = TTD** (outgoing TDI to Rotor 1).
    Pin 10 = spare/GND (TDO does NOT return via this connector — it returns via J7 pin 15).
  * **Power:** ERF8-005-05.0-S-DV-K-TR (10-pin 2×5, 0.8mm pitch) — 5× 3V3\_ENIG, 5× GND. Same part as JTAG socket.
  * **ENC DATA:** ERF8-010-05.0-S-DV-K-TR (20-pin 2×10, 0.8mm pitch) — ENC\_IN\[0:5\], ENC\_OUT\[0:5\], 8× GND fill.
  * **Cross-ref:** Authoritative pinout is defined in `Rotor/Design_Spec.md §3.4` (DEC-018 ownership).
  * **Note:** Rotor-to-rotor connections beyond Rotor 1 are direct (each Rotor J4/J5/J6 output mates with
    the next Rotor J1/J2/J3 input); Extension boards provide inter-group bridging at group boundaries in
    the serial chain (Stator → Rotor 1 → … → Rotor 30 → Reflector J1–J3).
* **Diagnostics:** 2x10 ENIG Gold Diagnostic Looped Probe Pad Bank (L1, Mirror of Controller).

### 4.1 Prototype Bench-Testing Provision (Break-Off Coupons)

The board panel includes **4 break-off PCB coupons** attached by mousebite perforations. Each coupon
fans out the 0.8mm pitch Samtec pads to a standard **2.54mm pitch shrouded IDC box header**, permitting
standard ribbon cable assemblies to be used for bench testing. For final production the coupons are
snapped off.

| Coupon | Connector | IDC Header | Signal |
| :--- | :--- | :--- | :--- |
| 1 | J8 — ERM8-020 (40-pin male) | 2×20 IDC box header, 2.54mm | Link-Beta (Controller) |
| 2 | J1 Slot 1 — ERF8-005 (10-pin female) | 2×5 IDC box header, 2.54mm | Rotor 1 JTAG/Power out |
| 3 | J2 Slot 1 — ERF8-005 (10-pin female) | 2×5 IDC box header, 2.54mm | Rotor 1 Power out |
| 4 | J3 Slot 1 — ERF8-010 (20-pin female) | 2×10 IDC box header, 2.54mm | Rotor 1 ENC Data out |

> Coupons 2–4 cover Rotor Slot 1 only (J1–J3 first instance); sufficient for single-rotor bench
> integration testing. IDC part numbers and coupon PCB fanout geometry to be defined at schematic/layout phase.

## 5. Power Telemetry (The "Encryption Load")

* **Purpose:** Provides real-time current/voltage data for the 30-rotor stack to the CM5 GUI.
* **Sensor:** TI INA219 Zero-Drift Power Monitor (Address: 0x45) — dedicated rotor-stack usage telemetry.
* **Placement:** Inserted on L1 (Top Layer) connected to the 3V3_ENIG rail immediately before the rotor stack.
  * Minimum 15mm isolation from Intel MAX II EPM240T100I5N CPLD logic core.
* **Shunt:** CSS2H-2512R-R010ELF (10mΩ ±1% 5A, 2512 Kelvin-sense) rotor-stack shunt resistor. Stator R1 instance. (PM R12 + PM R23 are the first and second system CSS2H; total build qty: 3 — see `Power_Budgets.md`.)
* **Interface:** I2C-1 Telemetry Bus (via Link-Beta, Shared with Power Module).
* **Filtering:** 0.1µF decoupling and RC filter on IN+/IN- for noise suppression from mechanical rotors.

## 6. EMI & Mechanical

* **Shield Mount:** 10mm ENIG Gold landing strip on L1 edge bonded to GND_CHASSIS.
* **Clamping:** Dual 3.2mm PTH anchors per cable for Galvanised Steel Bar compression.
* **Diagnostics:** 2x10 ENIG Gold Looped Probe Pad Bank mirrored to Controller's Bank-Beta pinout for A-B signal verification.

---

## 7. PCB Fabrication & Stackup

* **Manufacturer:** JLCPCB
* **Layer count:** 4-layer
* **Stackup:** JLC04161H-7628
* **Board thickness:** 1.6mm
* **Copper weight:** 2oz outer / 0.5oz inner
* **Surface finish:** ENIG
* **Min trace/space:** 0.1mm / 0.1mm
* **Min drill:** 0.2mm

## 8. Thermal & ESD

* **Thermal:** No active cooling required. Low-power passive components only. Relies on chassis airflow.
* **ESD:** TVS diode protection on external-facing signal lines. All connectors include GND guard pins per Samtec ERF8/ERM8 pinout.

## 9. Bill of Materials

| Ref | Component | Value | Package | Mouser Part # | DigiKey Part # | JLCPCB Part # |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| C1-C8 | Decoupling (8 per CPLD) | 0.1µF X7R 50V | 0402 | 187-CL05B104KB5NNNC | 1276-1009-1-ND | C1525 |
| C9-C13 | Bulk entry decoupling bank (star/spoke) | 10uF X7R 50V | 1206 | 187-CL31B106KBHNNNE | 1276-6767-1-ND | C89632 |
| J1-J3 | Rotor 1 interface sockets (1 slot × 3 connectors: JTAG ERF8-005, Power ERF8-005, ENC ERF8-010) — cross-ref Rotor/Design_Spec.md §3.4 | ERF8-005 (J1+J2) / ERF8-010 (J3) | SMT 0.8mm pitch | 200-ERF8005050SDVKTR (J1+J2) / 200-ERF8010050SDVKTR (J3) | SAM13517CT-ND (J1+J2 CT) / SAM8618CT-ND (J3 CT) | C7273978 (J1+J2) / C3646170 (J3) |
| J4-J6 | Encoder port connectors (×3 positions: HID J4 + Plugboard A J5 + Plugboard B J6) | 26-pin 2×13 2.54mm shrouded | through-hole | 538-22-23-2261 | WM2913-ND | N/A — Molex THT shrouded header, not stocked at JLCPCB; order from Mouser/DigiKey |
| J7 | 16-pin Reflector/Extension port | 2x8 2.54mm shrouded | through-hole | 538-22-23-2161 | WM2907-ND | N/A — Molex THT shrouded header, not stocked at JLCPCB; order from Mouser/DigiKey |
| J8 | Link-Beta Connector (MALE header — mates with ERF8-020 female socket on Controller) | ERM8-020-05.0-S-DV-K-TR | 40-pin | 200-ERM8020050SDVKTR | SAM8611CT-ND (CT) / SAM8611TR-ND (T&R) / SAM8611DKR-ND (DKR) | C138400 |
| L1-L4 | Rotor rail ferrite bead bank | 120 Ω @100 MHz, 4.0A | 1206 | 875-HI1206P121R-10 | 240-2410-1-ND | C2442103 |
| R1 | Rotor-Stack Shunt Resistor (CSS2H — Stator R1; PM R12 LTC3350 RSENSE and PM R23 INA219 U12 are first and second system instances, total build qty: 3) | CSS2H-2512R-R010ELF (10mΩ ±1% 5A) | 2512 Kelvin | 652-CSS2H-2512R-R010ELF | CSS2H-2512R-R010ELF-ND | — |
| R2 | JTAG TTD_RETURN pull-up | 10kΩ (1%) | 0603 | 667-ERJ-3EKF1002V | P10.0KBYCT-ND | C25804 |
| R3 | TMS pull-up to 3V3_ENIG | 10kΩ (1%) | 0603 | 667-ERJ-3EKF1002V | P10.0KBYCT-ND | C25804 |
| R4 | TDI pull-up to 3V3_ENIG | 10kΩ (1%) | 0603 | 667-ERJ-3EKF1002V | P10.0KBYCT-ND | C25804 |
| R5 | TCK pull-down to GND | 10kΩ (1%) | 0603 | 667-ERJ-3EKF1002V | P10.0KBYCT-ND | C25804 |
| R6 | SYS_RESET_N pull-up to 3V3_ENIG | 10kΩ (1%) | 0603 | 667-ERJ-3EKF1002V | P10.0KBYCT-ND | C25804 |
| R7 | TCK series R → J4 encoder port | 75Ω (1%) | 0603 | 667-ERJ-3EKF75R0V | P75.0BYCT-ND | C105905 |
| R8 | TCK series R → J5 encoder port | 75Ω (1%) | 0603 | 667-ERJ-3EKF75R0V | P75.0BYCT-ND | C105905 |
| R9 | TCK series R → J6 encoder port | 75Ω (1%) | 0603 | 667-ERJ-3EKF75R0V | P75.0BYCT-ND | C105905 |
| R10 | TMS series R → J4 encoder port | 75Ω (1%) | 0603 | 667-ERJ-3EKF75R0V | P75.0BYCT-ND | C105905 |
| R11 | TMS series R → J5 encoder port | 75Ω (1%) | 0603 | 667-ERJ-3EKF75R0V | P75.0BYCT-ND | C105905 |
| R12 | TMS series R → J6 encoder port | 75Ω (1%) | 0603 | 667-ERJ-3EKF75R0V | P75.0BYCT-ND | C105905 |
| R13 | TDI chain: Stator CPLD TDO → J4 TDI | 75Ω (1%) | 0603 | 667-ERJ-3EKF75R0V | P75.0BYCT-ND | C105905 |
| R14 | TDI chain: J4 TDO return → J5 TDI | 75Ω (1%) | 0603 | 667-ERJ-3EKF75R0V | P75.0BYCT-ND | C105905 |
| R15 | TDI chain: J5 TDO return → J6 TDI | 75Ω (1%) | 0603 | 667-ERJ-3EKF75R0V | P75.0BYCT-ND | C105905 |
| U1 | Stator Management CPLD | EPM240T100I5N | TQFP-100 | 989-EPM240T100I5N | 544-2276-ND | C40067 |
| U2 | 3V3_ENIG Current/Voltage Sensing | INA219AIDR | **SOIC-8** | 595-INA219AIDR | 296-23978-1-ND | C138706 |
