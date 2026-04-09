# Extension Board (V1.0) Design Specification

**Status:** Draft
**Project:** Enigma-NG
**Author:** Izzyonstage & GitHub Copilot
**Version:** v1.0.0
**Associated Hardware Revision:** Rev A
**Last Updated:** 2026-04-05

## 1. Overview

The Extension Board acts as a mid-stack JTAG pass-through and power injection point between
5-rotor sub-groups in extended rotor configurations. It bridges the TTD_RETURN signal and
3V3_ENIG power rail transparently between rotor groups via the Extension Port connectors (J7/J8).

* **Role:** Mechanical anchor and Power Injection for 5-rotor groups.
* **Capacity:** Up to ×5 Extension boards in a full 30-rotor build (Rev A power budget). Rev A
  prototype validates with 1 Extension board (10 rotors). Minimum configuration requires 0 Extensions
  (5 rotors: Stator → [5 Rotors] → Reflector). Each Extension board adds one further group of 5
  rotors. The 30-rotor / 5-extension limit is a power budget constraint — the architecture is
  theoretically scalable beyond 30 rotors with increased power.

### Functional & Design Requirements

#### Functional Requirements

| ID | Functional Requirement | Notes | Satisfied By / Cross-Ref |
| :--- | :--- | :--- | :--- |
| FR-EXT-01 | Pass JTAG signals through between rotor sub-groups in extended stacks | Passive pass-through; up to ×5 units in system | §2 Connectivity |
| FR-EXT-03 | Pass 3V3_ENIG power and encoder data bus transparently between rotor groups | Passive pass-through on J2/J5 and J3/J6 | §2 Connectivity; BOM J2, J5 (ERM8/ERF8-005), J3, J6 (ERM8/ERF8-010) |
| FR-EXT-04 | Connect on the input side to a Stator or upstream rotor group | J1–J3 (ERM8 male input headers) | §2 Connectivity; BOM J1–J3 (ERM8-005/010) |
| FR-EXT-05 | Connect on the output side to a downstream rotor group | J4–J6 (ERF8 female output sockets) | §2 Connectivity; BOM J4–J6 (ERF8-005/010) |

#### Design Requirements

| ID | Design Requirement | Specification | Satisfied By / Cross-Ref |
| :--- | :--- | :--- | :--- |
| DR-EXT-01 | PCB stackup | 4-layer, 2oz finished copper (JLC04161H-7628) | §4 PCB Fabrication & Stackup |
| DR-EXT-02 | Input connectors | J1 = ERM8-005 (JTAG in), J2 = ERM8-005 (Power in), J3 = ERM8-010 (ENC in) | §2 Connectivity; BOM J1–J3 |
| DR-EXT-03 | Output connectors | J4 = ERF8-005 (JTAG out), J5 = ERF8-005 (Power out), J6 = ERF8-010 (ENC out) | §2 Connectivity; BOM J4–J6 |
| DR-EXT-05 | JTAG pass-through pin assignment | TCK on J4 pin 2; TMS on J4 pin 4 (per DEC-018 pinout) | §2 Connectivity; Design_Log.md DEC-018 |
| DR-EXT-07 | System quantity | Up to ×5 Extension boards per system (Rev A power budget); Rev A prototype uses ×1 | §1 Overview; System_Architecture.md |

## 2. Connectivity

* **Extension Port (J7 IN / J8 OUT):** 16-pin 2×8 shrouded box header.
  > **Connector Definition Owner:** `Stator/Board_Layout.md — J7`.
  > This board uses the mating connector on both J7 and J8 (Molex 22-23-2161 or equivalent — see BOM).
  > Authoritative pinout: Pin 1 = 3V3_ENIG, Pin 2 = SYS_RESET_N, Pins 3–8 = ENC_IN[0:5],
  > Pins 9–14 = ENC_OUT[0:5], Pin 15 = TTD_RETURN, Pin 16 = GND.
* **Rotor Interface Connectors (3 per rotor-facing side × 2 sides = 6 connectors total):**
  The Extension board provides ERM8 male headers on the **input side** (J1–J3, plugging into the
  previous rotor group's last rotor J4/J5/J6 ERF8 output sockets) and ERF8 female sockets on the
  **output side** (J4–J6, receiving the next rotor group's first rotor J1/J2/J3 ERM8 male headers).

  > **Connector Definition Owner:** `Rotor/Design_Spec.md §3.4`.
  > This board uses ERM8 male headers on the input side and ERF8 female sockets on the output side:

  | Ref | Side | Signal Group | Type | MPN |
  | --- | ---- | ------------ | ---- | --- |
  | J1 | Input (plugs into previous group's last rotor J4) | JTAG | ERM8-005 (10-pin, 0.8mm pitch, **male**) | ERM8-005-05.0-S-DV-K-TR |
  | J2 | Input (plugs into previous group's last rotor J5) | Power (3V3_ENIG × 5, GND × 5) | ERM8-005 (10-pin, 0.8mm pitch, **male**) | ERM8-005-05.0-S-DV-K-TR |
  | J3 | Input (plugs into previous group's last rotor J6) | ENC Data (ENC_IN/ENC_OUT + GND) | ERM8-010 (20-pin, 0.8mm pitch, **male**) | ERM8-010-05.0-S-DV-K-TR |
  | J4 | Output (receives next group's first rotor J1) | JTAG | ERF8-005 (10-pin, 0.8mm pitch, female) | ERF8-005-05.0-S-DV-K-TR |
  | J5 | Output (receives next group's first rotor J2) | Power (3V3_ENIG × 5, GND × 5) | ERF8-005 (10-pin, 0.8mm pitch, female) | ERF8-005-05.0-S-DV-K-TR |
  | J6 | Output (receives next group's first rotor J3) | ENC Data (ENC_IN/ENC_OUT + GND) | ERF8-010 (20-pin, 0.8mm pitch, female) | ERF8-010-05.0-S-DV-K-TR |

  **Note:** The ERM8/ERF8 0.8mm pitch is physically incompatible with 2.54mm connectors — label distinctly on silkscreen.
  Connector part numbers: ERM8-005 = Mouser 200-ERM8005050SDVKTR / DigiKey 612-ERM8-005-05.0-S-DV-K-TRCT-ND / JLCPCB C3649741;
  ERM8-010 = Mouser 200-ERM8010050SDVKTR / DigiKey SAM8610CT-ND / JLCPCB C374877;
  ERF8-005 = Mouser 200-ERF8005050SDVKTR / DigiKey SAM13517CT-ND / JLCPCB C7273978;
  ERF8-010 = Mouser 200-ERF8010050SDVKTR / DigiKey SAM8618CT-ND / JLCPCB C3646170.

* **JTAG:** Pass-through for the serial chain; TTD_RETURN carried via Extension Port pin 15.
  This board carries JTAG signals as a passive pass-through only. No active termination is
  required here; series termination is placed at the driving ends of each cable segment on
  the Stator (R7–R15) and Encoder boards (R7, R8). See `design/Electronics/Investigations/JTAG_Integrity.md`
  and DEC-016.

* **GND_CHASSIS Single-Point Bond:** Per `design/Standards/Global_Routing_Spec.md §5`, a single
  0Ω bond resistor (R2) or direct via connects signal GND to chassis copper pour at J7 pin 16 (GND).
  No additional bonds on this board to prevent ground loops.
* **Power Injection:** Receives 3V3_ENIG and GND via Extension Port to prevent voltage sag across long stacks.
* Decoupling and bulk entry capacitor requirements per `design/Standards/Global_Routing_Spec.md §3`.
* **SYS_RESET_N:** Received via Extension Port pin 2; broadcast to all local rotor CPLDs in this group.
* **Cross-ref:** For interconnect pinouts on power (3V3_ENIG/GND), ENC_IN/ENC_OUT, and JTAG TTD_RETURN lines used for reflector loopback/plugboard mapping, See:
  * `Stator/Design_Spec.md`
  * `Reflector/Design_Spec.md`

### 2.1 Prototype Bench-Testing Provision (Break-Off Coupons)

Each board panel includes **6 break-off PCB coupons** (one per ERx8 connector), attached by mousebite
perforations. Each coupon fans out the 0.8mm pitch Samtec pads to a standard **2.54mm pitch shrouded
IDC box header**, permitting standard ribbon cable assemblies to be used for bench testing before full
stack assembly. For final production the coupons are snapped off at the mousebite perforations.

| Coupon | Connector | IDC Header | Signal |
| :--- | :--- | :--- | :--- |
| 1 | J1 — ERM8-005 (10-pin male) | 2×5 IDC box header, 2.54mm | JTAG in |
| 2 | J2 — ERM8-005 (10-pin male) | 2×5 IDC box header, 2.54mm | Power in |
| 3 | J3 — ERM8-010 (20-pin male) | 2×10 IDC box header, 2.54mm | ENC Data in |
| 4 | J4 — ERF8-005 (10-pin female) | 2×5 IDC box header, 2.54mm | JTAG out |
| 5 | J5 — ERF8-005 (10-pin female) | 2×5 IDC box header, 2.54mm | Power out |
| 6 | J6 — ERF8-010 (20-pin female) | 2×10 IDC box header, 2.54mm | ENC Data out |

IDC part numbers and coupon PCB fanout geometry to be defined at schematic/layout phase.

## 3. Diagnostics & Branding

* **Diagnostics:** Integrated 2x8 ENIG Gold Diagnostic Looped Probe Pad Bank (Mid-Stack troubleshooting).
* **Identity:** 2oz Copper / Inverted White Data Plate (V1.0 traceability).

## 4. PCB Fabrication & Stackup

* **Layers:** 4-Layer (JLC04161H-7628).
* **Finish:** ENIG (Gold) for connector and diagnostic pad surfaces.
* **Layer Mapping:** L1: Signal (JTAG pass-through / routing) | L2: GND | L3: 3V3_ENIG | L4: Signal (Data Plate).
* **Aesthetics:** Dark Green Solder Mask; Typewriter font (ALL-CAPS GERMAN).
* **JTAG Trace Width Rule:** The Extension board carries only the **TTD_RETURN** signal on its J7/J8 pass-through path
  (TCK, TMS, and TDI travel to the rotor stack via Stator J1–J3, not via the Extension Port). TTD_RETURN traces on L1 shall be routed at **0.127 mm (5 mil)**
  over the L2 GND plane, targeting **50 Ω controlled impedance**. See
  `design/Electronics/Investigations/JTAG_Integrity.md` and DEC-016. Stackup defined per DEC-017.

## 5. Thermal & ESD

* **Thermal:** No active cooling required on the Extension board. Passive components only.
* **ESD:** TVS diode on exposed signal lines; board relies on enclosure shielding.

## 6. Bill of Materials

| Ref | Component | Value | Package | Mouser Part # | DigiKey Part # | JLCPCB Part # |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| C1-C5 | Bulk entry decoupling bank (star/spoke) | 10uF X7R 50V | 1206 | 187-CL31B106KBHNNNE | 1276-6767-1-ND | C89632 |
| J1 | Rotor group input — JTAG (ERM8-005, 10-pin **male**, 0.8mm pitch) | Samtec ERM8-005-05.0-S-DV-K-TR | SMT | 200-ERM8005050SDVKTR | 612-ERM8-005-05.0-S-DV-K-TRCT-ND | C3649741 |
| J2 | Rotor group input — Power (ERM8-005, 10-pin **male**, 0.8mm pitch) | Samtec ERM8-005-05.0-S-DV-K-TR | SMT | 200-ERM8005050SDVKTR | 612-ERM8-005-05.0-S-DV-K-TRCT-ND | C3649741 |
| J3 | Rotor group input — ENC Data (ERM8-010, 20-pin **male**, 0.8mm pitch) | Samtec ERM8-010-05.0-S-DV-K-TR | SMT | 200-ERM8010050SDVKTR | SAM8610CT-ND | C374877 |
| J4 | Rotor group output — JTAG (ERF8-005, 10-pin female, 0.8mm pitch) | Samtec ERF8-005-05.0-S-DV-K-TR | SMT | 200-ERF8005050SDVKTR | SAM13517CT-ND | C7273978 |
| J5 | Rotor group output — Power (ERF8-005, 10-pin female, 0.8mm pitch) | Samtec ERF8-005-05.0-S-DV-K-TR | SMT | 200-ERF8005050SDVKTR | SAM13517CT-ND | C7273978 |
| J6 | Rotor group output — ENC Data (ERF8-010, 20-pin female, 0.8mm pitch) | Samtec ERF8-010-05.0-S-DV-K-TR | SMT | 200-ERF8010050SDVKTR | SAM8618CT-ND | C3646170 |
| J7 | Extension Port IN header | 16-pin 2×8 shrouded box | 2.54mm | 538-22-23-2161 | WM2907-ND | N/A — Molex Milli-Grid, not stocked at JLCPCB; order from Mouser/DigiKey |
| J8 | Extension Port OUT header | 16-pin 2×8 shrouded box | 2.54mm | 538-22-23-2161 | WM2907-ND | N/A — Molex Milli-Grid, not stocked at JLCPCB; order from Mouser/DigiKey |
| J9 | Diagnostic looped probe pads | 2x8 ENIG Gold | 2.54mm | N/A | N/A | N/A — bare PCB pads; no component |
| R1 | GND plane isolating resistor (optional) | 0Ω or 10Ω | 0603 | 667-ERJ-3GEY0R00V | P0.0BYCT-ND | C25807 |
| R2 | GND_CHASSIS single-point bond | 0Ω | 0603 | 667-ERJ-3GEY0R00V | P0.0BYCT-ND | C25807 |
