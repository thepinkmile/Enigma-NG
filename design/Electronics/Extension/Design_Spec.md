# Extension Board (V1.0) Design Specification

**Status:** Draft
**Project:** Enigma-NG
**Author:** Izzyonstage & GitHub Copilot
**Version:** v1.0.0
**Associated Hardware Revision:** Rev A
**Last Updated:** 2026-04-05

## 1. Overview

The Extension Board acts as a mid-stack JTAG signal repeater and power injection point between
5-rotor sub-groups in extended rotor configurations. It buffers TCK and TMS drive signals to
compensate for capacitive loading, and bridges the TTD_RETURN signal and 3V3_ENIG power rail
transparently between rotor groups via the Extension Port connectors (J7/J8).

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
| FR-EXT-01 | Act as a JTAG signal repeater between rotor sub-groups in extended stacks | Restores TCK/TMS drive strength mid-chain; up to ×5 units in system | §2 Connectivity; BOM U1 (SN74LVC2G125DCUR) |
| FR-EXT-02 | Buffer TCK and TMS signals to compensate for capacitive loading of upstream rotors | Dual-channel buffer preserves timing margins | §2 Connectivity; BOM U1 (SN74LVC2G125DCUR), C6 (100nF bypass) |
| FR-EXT-03 | Pass 3V3_ENIG power and encoder data bus transparently between rotor groups | Power: J7 → J5 (J2 power pins NC); ENC data: J3/J6 pass-through | §2 Connectivity; BOM J5 (ERF8-005), J3, J6 (ERM8/ERF8-010) |
| FR-EXT-04 | Connect on the input side to a Stator or upstream rotor group | J1–J3 (ERM8 male input headers) | §2 Connectivity; BOM J1–J3 (ERM8-005/010) |
| FR-EXT-05 | Connect on the output side to a downstream rotor group | J4–J6 (ERF8 female output sockets) | §2 Connectivity; BOM J4–J6 (ERF8-005/010) |

#### Design Requirements

| ID | Design Requirement | Specification | Satisfied By / Cross-Ref |
| :--- | :--- | :--- | :--- |
| DR-EXT-01 | PCB stackup | 4-layer, 2oz finished copper (JLC04161H-7628) | §4 PCB Fabrication & Stackup |
| DR-EXT-02 | Input connectors | J1 = ERM8-005 (JTAG in), J2 = ERM8-005 (Power in), J3 = ERM8-010 (ENC in) | §2 Connectivity; BOM J1–J3 |
| DR-EXT-03 | Output connectors | J4 = ERF8-005 (JTAG out), J5 = ERF8-005 (Power out), J6 = ERF8-010 (ENC out) | §2 Connectivity; BOM J4–J6 |
| DR-EXT-04 | JTAG buffer | U1 = SN74LVC2G125DCUR (dual-channel; TCK and TMS only; TDI passes unbuffered) | §2 Connectivity; BOM U1 (SN74LVC2G125DCUR) |
| DR-EXT-05 | Buffer output pin assignment | TCK → J4 pin 2; TMS → J4 pin 4 (per DEC-018 pinout) | §2 Connectivity; Design_Log.md DEC-018 |
| DR-EXT-06 | Buffer bypass capacitor | C6 = 100 nF 0402 within 2 mm of U1 VCC pin (L1) | §4 PCB Fabrication & Stackup; BOM C6 (100nF X7R) |
| DR-EXT-07 | System quantity | Up to ×5 Extension boards per system (Rev A power budget); Rev A prototype uses ×1 | §1 Overview; System_Architecture.md |

## 2. Connectivity

* **Extension Port (J7 IN / J8 OUT):** 16-pin 2×8 shrouded box header.
  > **Connector Definition Owner:** `Stator/Board_Layout.md — J7`.
  > This board uses the mating connector on both J7 and J8 (Adam Tech BHR-16-VUA — see BOM).
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
  | J2 | Input (plugs into previous group's last rotor J5) | Power (3V3_ENIG × 5, GND × 5) — **power pins NC on this board** | ERM8-005 (10-pin, 0.8mm pitch, **male**) | ERM8-005-05.0-S-DV-K-TR |
  | J3 | Input (plugs into previous group's last rotor J6) | ENC Data (ENC_IN/ENC_OUT + GND) | ERM8-010 (20-pin, 0.8mm pitch, **male**) | ERM8-010-05.0-S-DV-K-TR |
  | J4 | Output (receives next group's first rotor J1) | JTAG | ERF8-005 (10-pin, 0.8mm pitch, female) | ERF8-005-05.0-S-DV-K-TR |
  | J5 | Output (receives next group's first rotor J2) | Power (3V3_ENIG × 5, GND × 5) | ERF8-005 (10-pin, 0.8mm pitch, female) | ERF8-005-05.0-S-DV-K-TR |
  | J6 | Output (receives next group's first rotor J3) | ENC Data (ENC_IN/ENC_OUT + GND) | ERF8-010 (20-pin, 0.8mm pitch, female) | ERF8-010-05.0-S-DV-K-TR |

  > **J2 power pins (3V3_ENIG and GND) are not connected to the board power plane.** J2 is present
  > for mechanical engagement with the upstream rotor group only. The Extension board's sole power
  > entry is J7 (Extension Port IN, pin 1 = 3V3_ENIG, pin 16 = GND). This prevents a parallel power
  > path / ground loop between the rotor daisy-chain and the Extension Port ribbon. C1–C5 decouple
  > at the J7 power entry. Power is passed to the downstream rotor group via J5 (driven from J7).

  **Note:** The ERM8/ERF8 0.8mm pitch is physically incompatible with 2.54mm connectors — label distinctly on silkscreen.
  Connector part numbers: ERM8-005 = Mouser 200-ERM8005050SDVKTR / DigiKey 612-ERM8-005-05.0-S-DV-K-TRCT-ND / JLCPCB C3649741;
  ERM8-010 = Mouser 200-ERM8010050SDVKTR / DigiKey SAM8610CT-ND / JLCPCB C374877;
  ERF8-005 = Mouser 200-ERF8005050SDVKTR / DigiKey SAM13517CT-ND / JLCPCB C7273978;
  ERF8-010 = Mouser 200-ERF8010050SDVKTR / DigiKey SAM8618CT-ND / JLCPCB C3646170.

* **JTAG Signal Buffering:** The Extension board provides JTAG re-buffering for the 5-rotor group
  connected to its output side (J4–J6). A **74LVC2G125** dual-channel 3-state buffer (U1) buffers the
  **TCK and TMS** lines, providing a fresh drive from the Extension board's 3V3_ENIG rail:
  * TCK buffer output → J4 pin **2** (TCK) and broadcast to all 5 rotors in the output group.
  * TMS buffer output → J4 pin **4** (TMS) and broadcast.
  * Buffer enable (OE#): tied to GND permanently (always enabled).
  * Part: SN74LVC2G125DCUR (TI, VSSOP-8) — Mouser 595-SN74LVC2G125DCUR,
    DigiKey 296-SN74LVC2G125DCURCT-ND, JLCPCB C21404.
  * At 5 rotors per group connected via BtB (ERM8/ERF8), signal integrity analysis confirms this
    buffer interval is sufficient: 5 rotors × EPM570T100I5N input capacitance (≈6pF) + connector capacitance
    ≈ 30–40pF total load; well within the 50ns half-period at 10MHz TCK.

* **GND_CHASSIS Single-Point Bond:** Per `design/Standards/Global_Routing_Spec.md §5`, a single
  0Ω bond resistor (R2) or direct via connects signal GND to chassis copper pour at J7 pin 16 (GND).
  No additional bonds on this board to prevent ground loops.
* **Power Injection:** Receives 3V3_ENIG and GND via Extension Port to prevent voltage sag across long stacks.
* Decoupling and bulk entry capacitor requirements per `design/Standards/Global_Routing_Spec.md §3`.
* **JTAG TTD_RETURN / TDI:** TTD_RETURN (TDO chain return) is carried passively via Extension Port
  pin 15. TDI passes unbuffered board-to-board via BtB throughout the rotor stack — no series
  resistors are placed at each BtB hop. The JTAG chain terminates at the Reflector (R1 22 Ω
  end-of-chain damping). TTD_RETURN then returns from the Reflector to the Stator via the
  dedicated Reflector J4 → Stator J7 ribbon cable. The 75 Ω series resistors on the Stator
  (R7–R15) and Encoder boards (R7, R8) are for the **encoder ribbon cable ports** (J4–J6) only —
  they are NOT placed on the BtB rotor stack interface. See
  `design/Electronics/Investigations/JTAG_Integrity.md` and DEC-016.
  TCK and TMS are actively re-buffered by U1 (see JTAG Signal Buffering above).
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
* **U1 Bypass:** C6 (100nF) must be placed within 2mm of U1 VCC pin on L1.

## 5. Thermal & ESD

* **Thermal:** No active cooling required on the Extension board. U1 (SN74LVC2G125DCUR) is the
  only active IC; it dissipates <10mW and requires no heatsinking. C6 (0.1µF X7R 0402) provides
  the mandatory local bypass. All other components are passive.

  > ⚠️ **U1 must never be removed.** The Extension board actively re-buffers TCK and TMS for
  > every 5-rotor group. Without U1, signal integrity in long rotor stacks will fail.
  > See FR-EXT-01, DR-EXT-04/05/06.
* **ESD:** TVS diode on exposed signal lines; board relies on enclosure shielding.

## 6. Bill of Materials

| Ref | Component | Value | Package | Mouser Part # | DigiKey Part # | JLCPCB Part # |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| C1-C5 | Bulk entry decoupling bank (star/spoke) | 10uF X7R 50V | 1206 | 187-CL31B106KBHNNNE | 1276-6767-1-ND | C89632 |
| C6 | 100nF X7R 50V bypass — U1 VCC | Samsung CL05B104KB5NNNC | 0402 | 187-CL05B104KB5NNNC | 1276-1009-1-ND | C1525 |
| J1 | Rotor group input — JTAG (ERM8-005, 10-pin **male**, 0.8mm pitch) | Samtec ERM8-005-05.0-S-DV-K-TR | SMT | 200-ERM8005050SDVKTR | 612-ERM8-005-05.0-S-DV-K-TRCT-ND | C3649741 |
| J2 | Rotor group input — Power (ERM8-005, 10-pin **male**, 0.8mm pitch) | Samtec ERM8-005-05.0-S-DV-K-TR | SMT | 200-ERM8005050SDVKTR | 612-ERM8-005-05.0-S-DV-K-TRCT-ND | C3649741 |
| J3 | Rotor group input — ENC Data (ERM8-010, 20-pin **male**, 0.8mm pitch) | Samtec ERM8-010-05.0-S-DV-K-TR | SMT | 200-ERM8010050SDVKTR | SAM8610CT-ND | C374877 |
| J4 | Rotor group output — JTAG (ERF8-005, 10-pin female, 0.8mm pitch) | Samtec ERF8-005-05.0-S-DV-K-TR | SMT | 200-ERF8005050SDVKTR | SAM13517CT-ND | C7273978 |
| J5 | Rotor group output — Power (ERF8-005, 10-pin female, 0.8mm pitch) | Samtec ERF8-005-05.0-S-DV-K-TR | SMT | 200-ERF8005050SDVKTR | SAM13517CT-ND | C7273978 |
| J6 | Rotor group output — ENC Data (ERF8-010, 20-pin female, 0.8mm pitch) | Samtec ERF8-010-05.0-S-DV-K-TR | SMT | 200-ERF8010050SDVKTR | SAM8618CT-ND | C3646170 |
| J7 | Extension Port IN header | Adam Tech BHR-16-VUA — 16-pin 2×8 2.54mm shrouded box | 2.54mm | 737-BHR-16-VUA | 2057-BHR-16-VUA-ND | C17692295 |
| J8 | Extension Port OUT header | Adam Tech BHR-16-VUA — 16-pin 2×8 2.54mm shrouded box | 2.54mm | 737-BHR-16-VUA | 2057-BHR-16-VUA-ND | C17692295 |
| J9 | Diagnostic looped probe pads | 2x8 ENIG Gold | 2.54mm | N/A | N/A | N/A — bare PCB pads; no component |
| R1 | GND plane isolating resistor (optional) | 0Ω or 10Ω | 0603 | 667-ERJ-3GEY0R00V | P0.0BYCT-ND | C25807 |
| R2 | GND_CHASSIS single-point bond | 0Ω | 0603 | 667-ERJ-3GEY0R00V | P0.0BYCT-ND | C25807 |
| U1 | JTAG TCK/TMS dual buffer for output rotor group | SN74LVC2G125DCUR | VSSOP-8 | 595-SN74LVC2G125DCUR | 296-SN74LVC2G125DCURCT-ND | C21404 |
