# Reflector Board (V1.0) Design Specification

**Status:** Draft
**Project:** Enigma-NG
**Author:** Izzyonstage & GitHub Copilot
**Version:** v1.0.0
**Associated Hardware Revision:** Rev A
**Last Updated:** 2026-04-05

## 1. Overview

The Reflector Board sits at the far end of the 30-rotor stack. Its primary role is to receive the signals from the final rotor and return them back through the stack via a different electrical path.
It also acts as the JTAG termination hub and returns the TTD_RETURN directly back to the Stator to reduce required Pin count in the Rotor Interconnects.

### Functional & Design Requirements

#### Functional Requirements

| ID | Functional Requirement | Notes | Satisfied By / Cross-Ref |
| :--- | :--- | :--- | :--- |
| FR-REF-01 | Terminate the JTAG daisy-chain at the end of the 30-rotor stack | Connects to Rotor 30 J4/J5/J6 outputs | §3 JTAG & Logic Hub; BOM J1–J3 (ERM8) |
| FR-REF-02 | Emulate the historical Enigma reflector (fixed symmetric substitution cipher) | Passive wiring — no CPLD required | §2 Architecture; BOM J1–J3 (passive loopback traces) |
| FR-REF-03 | Return the JTAG TTD_RETURN signal from the end of the chain to the Stator | Via J4 → Stator J7 → Link-Beta pin 26 → FT232H | §3 JTAG & Logic Hub; BOM J4 (16-pin), R1 (22Ω) |
| FR-REF-04 | Provide end-of-chain JTAG signal damping | Prevents reflections in the serial chain | §3 JTAG & Logic Hub; BOM R1 (22Ω 0402) |

#### Design Requirements

| ID | Design Requirement | Specification | Satisfied By / Cross-Ref |
| :--- | :--- | :--- | :--- |
| DR-REF-01 | PCB stackup | 4-layer, 2oz finished copper (JLC04161H-7628) | §6 PCB Fabrication & Stackup |
| DR-REF-02 | Input connectors | J1 = ERM8-005 (JTAG, plugs into Rotor 30 J4), J2 = ERM8-005 (Power, Rotor 30 J5), J3 = ERM8-010 (ENC, Rotor 30 J6) | §4 Rotor Interface Connectors; BOM J1–J3 |
| DR-REF-03 | TTD_RETURN output | J4 connector (mates with Stator J7); TTD_RETURN on J4 pin 15 | §3 JTAG & Logic Hub; BOM J4 (16-pin 2×8 shrouded) |
| DR-REF-04 | End-of-chain damping | R1 = 22 Ω 0402 on TDO line | §3 JTAG & Logic Hub; BOM R1 (22Ω) |
| DR-REF-05 | Active logic | None — passive reflector function only; fixed wiring emulated in hardware | §2 Architecture |

## 2. Architecture

* **PCB:** 4-Layer (JLC04161H-7628) / 2oz Finished Copper / ENIG Gold / 2.0mm Filleted Corners.
* **Standard:** Includes Inverted White Data Plate on bottom layer.

### System Role: The "Turnaround"

* **Logic Type:** Passive (Loopback).
* **Routing Logic:** All signal mapping is handled remotely by the **Intel MAX II EPM240T100I5N CPLD** located on the Stator Board.
* **CPLD support:** PCB passive routing (no discrete component).
* **Signal Path:** Rotor 30 J4–J6 (ERF8 female) → Reflector J1–J3 (ERM8 male) → passive loopback traces → ENC cipher data reflected back; TTD_RETURN exits via J4 (16-pin Molex, pin 15) → Stator J7.

## 3. JTAG & Logic Hub

* **Interconnect:** 16-pin (2x8) 2.54mm Shrouded Box Header (Vertical).
  > **Connector Definition Owner:** `Stator/Board_Layout.md — J7`.
  > This board uses the mating connector as J4 (Molex 22-23-2161 or equivalent — see BOM). The authoritative
  > 16-pin pinout is defined on the Stator; Pin 1 = 3V3_ENIG, Pin 2 = SYS_RESET_N, Pins 3–8 = ENC_IN[0:5],
  > Pins 9–14 = ENC_OUT[0:5], Pin 15 = TTD_RETURN, Pin 16 = GND.

> **Compatibility note:** J4 pin allocation matches Stator J7 (16-pin 2×8). The Stator J7 was reduced from 20-pin to 16-pin in the design review (this revision) — J4 requires no changes.

* Decoupling and bulk entry capacitor requirements per `design/Standards/Global_Routing_Spec.md §3`.
* **Termination:**R1 (22Ω) is a series damping resistor on the TDO return line (end-of-chain
  signal from Rotor 30). It provides impedance damping at the final rotor output before the signal
  re-enters the Extension Port for return to the Stator.

> **Note:** TMS and TDI pull-up resistors (R2/R3) previously listed in this section have been removed.
> TMS and TDI are NOT routed on J4 (pin 15 = TTD_RETURN only for JTAG; pins 3–14 = ENC data; pin 2 = SYS_RESET_N).
> Pull-up termination for TMS and TDI is already provided by the Stator (R3/R4) and Encoder boards (R3/R4) where those signals originate.

* **JTAG Trace Width Rule:** All JTAG signal traces on L1 (TTD_RETURN and any in-board JTAG
  routing) shall be routed at **0.127 mm (5 mil)** width over the L2 GND plane, targeting
  **50 Ω controlled impedance**. Stackup upgraded to 4-Layer per DEC-017.
  See `design/Electronics/Investigations/JTAG_Integrity.md` and DEC-016.
* **JTAG Return:** TDO from Rotor 30 is routed to Pin 15 (TTD_RETURN) for return to the Stator.
* **Loopback:** Directly routes 6-bit ENC_IN to 6-bit ENC_OUT via 2oz 10-mil traces.
* **Cross-ref:** For interconnect pinouts on power (3V3_ENIG/GND), ENC_IN/ENC_OUT, and JTAG TTD_RETURN lines used for reflector loopback/plugboard mapping, See:
  * `Stator/Design_Spec.md`
  * `Extension/Design_Spec.md`

## 4. Rotor Interface Connectors

The Reflector connects to the **output side** of Rotor 30 using the same ERM8 male header family used
on each Rotor's output side (J4/J5/J6). One set of three connectors per the Rotor interface definition:

> **Connector Definition Owner:** `Rotor/Design_Spec.md §3.4`.
> This board provides ERM8 male headers that plug into Rotor 30's J4/J5/J6 ERF8 female output sockets.

| Ref | Type | Signal Group | Part Series | MPN |
| --- | ---- | ------------ | ----------- | --- |
| J1 | ERM8-005 (10-pin, **male**) | JTAG (TCK, TMS, TTD, SYS_RESET_N + GND) | Samtec ERM8 | ERM8-005-05.0-S-DV-K-TR |
| J2 | ERM8-005 (10-pin, **male**) | Power (3V3_ENIG × 5, GND × 5) | Samtec ERM8 | ERM8-005-05.0-S-DV-K-TR |
| J3 | ERM8-010 (20-pin, **male**) | ENC data (ENC_IN[0:5], ENC_OUT[0:5] + GND interleave) | Samtec ERM8 | ERM8-010-05.0-S-DV-K-TR |

**Orientation:** Facing the rotor output side (Rotor 30 top face), perpendicular to the rotor stack axis.
The ERM8 header pitch (0.8mm) is physically incompatible with 2.54mm connectors — label accordingly on silkscreen.

> **Note on §5 "26x Gold-plated friction pads":** This earlier notation referred to a draft mechanical
> contact concept and is superseded by the ERM8 connector approach defined here. The 40 active contacts
> (10 + 10 + 20) on J1–J3 provide the Reflector rotor interface; the friction pad concept is retired.

Per `design/Standards/Global_Routing_Spec.md §5`, each PCB must have a single-point GND_CHASSIS bond at its power entry connector.

**Reflector GND_CHASSIS bond point:** The GND_CHASSIS connection is made at J4 (Stator/Extension link connector, pin 16 GND).
A single 0 Ω bond resistor (or direct via) connects the signal GND plane to the chassis copper pour at this point.
No additional bonds are made on this board to avoid ground loops.

### 4.1 Prototype Bench-Testing Provision (Break-Off Coupons)

Each board panel includes **3 break-off PCB coupons** (one per ERx8 connector), attached by mousebite
perforations. Each coupon fans out the 0.8mm pitch Samtec pads to a standard **2.54mm pitch shrouded
IDC box header**, permitting standard ribbon cable assemblies to be used for bench testing before full
stack assembly. For final production the coupons are snapped off at the mousebite perforations.

| Coupon | Connector | IDC Header | Signal |
| :--- | :--- | :--- | :--- |
| 1 | J1 — ERM8-005 (10-pin male) | 2×5 IDC box header, 2.54mm | JTAG |
| 2 | J2 — ERM8-005 (10-pin male) | 2×5 IDC box header, 2.54mm | Power |
| 3 | J3 — ERM8-010 (20-pin male) | 2×10 IDC box header, 2.54mm | ENC Data |

IDC part numbers and coupon PCB fanout geometry to be defined at schematic/layout phase.

## 5. Diagnostic & Monitoring

To ensure the signal has successfully navigated the 30-rotor stack, a dedicated monitoring bank is included.

* **Bank Configuration:** 2x8 ENIG Gold Diagnostic Looped Probe Pad Bank.
* **Standard:** Matches the **Controller Board** 2.54mm (0.1") pitch standard for unified system debugging.
* **Labelling:** `REFLEKTOR-DIAGNOSE [Reflector Diag]` in ALL-CAPS German typewriter font.

## 6. PCB Fabrication & Stackup

* **Stackup:** 4-Layer (JLC04161H-7628) / 2oz Finished Copper.
* **Layer Mapping:** L1: Signal (JTAG/routing) | L2: GND | L3: 3V3_ENIG | L4: Signal (Data Plate).
* **Contacts:** ERM8-005 (×2, 10-pin, JTAG and Power) + ERM8-010 (×1, 20-pin, ENC Data) — male headers on J1–J3.
* **Fillets:** 2.0mm Rounded PCB corners for consistent "Museum-Grade" enclosure fit.
* **Routing:** Global **0.5mm Fixed-Radius Circular Arcs** for all loopback traces.

## 7. Branding & Traceability

* **Data Plate:** Inverted white silkscreen "Data Plate" on Bottom (L4) containing the Enigma silhouette, "ENIGMA-NG" text, and JLC Serial Number block.
* **Label:** `REFLEKTOR-EINHEIT [Reflector Unit]` in ALL-CAPS German typewriter font.

## 8. Bill of Materials

| Ref | Component | Value | Package | Mouser Part # | DigiKey Part # | JLCPCB Part # |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| C1-C5 | Bulk entry decoupling bank (star/spoke) | 10uF X7R 50V | 1206 | 187-CL31B106KBHNNNE | 1276-6767-1-ND | C89632 |
| J1 | Rotor 30 output interface — JTAG (ERM8-005, 10-pin **male**, 0.8mm pitch) | Plugs into Rotor 30 J4 (ERF8-005 female) | SMT | 200-ERM8005050SDVKTR | 612-ERM8-005-05.0-S-DV-K-TRCT-ND | C3649741 |
| J2 | Rotor 30 output interface — Power (ERM8-005, 10-pin **male**, 0.8mm pitch) | Plugs into Rotor 30 J5 (ERF8-005 female) | SMT | 200-ERM8005050SDVKTR | 612-ERM8-005-05.0-S-DV-K-TRCT-ND | C3649741 |
| J3 | Rotor 30 output interface — ENC Data (ERM8-010, 20-pin **male**, 0.8mm pitch) | Plugs into Rotor 30 J6 (ERF8-010 female) | SMT | 200-ERM8010050SDVKTR | SAM8610CT-ND | C374877 |
| J4 | Interconnect header | 16-pin 2x8 shrouded | 2.54mm | 538-22-23-2161 | WM2907-ND | N/A — Molex THT shrouded header, not stocked at JLCPCB; order from Mouser/DigiKey |
| J5 | Diagnostic looped probe pads | 2x8 ENIG Gold | 2.54mm | N/A | N/A | N/A — bare PCB pads; no component |
| R1 | JTAG termination | 22Ω | 0603 | 667-ERJ-3EKF2200V | P22.0BYCT-ND | C25805 |
