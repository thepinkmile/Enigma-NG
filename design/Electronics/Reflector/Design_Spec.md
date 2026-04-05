# Reflector Board (V1.0) Design Specification

**Status:** Draft
**Version:** v1.0.0
**Associated Hardware Revision:** Rev A
**Last Updated:** 2026-04-04

## 1. Overview

The Reflector Board sits at the far end of the 30-rotor stack. Its primary role is to receive the signals from the final rotor and return them back through the stack via a different electrical path.
It also acts as the JTAG termination hub and returns the JTAG_TDO directly back to the Stator to reduce required Pin count in the Rotor Interconnects.

## 2. Architecture

* **PCB:** 4-Layer (JLC04161H-7628) / 2oz Finished Copper / ENIG Gold / 2.0mm Filleted Corners.
* **Standard:** Includes Inverted White Data Plate on bottom layer.

### System Role: The "Turnaround"

* **Logic Type:** Passive (Loopback).
* **Routing Logic:** All signal mapping is handled remotely by the **Intel MAX II EPM240T100C5N CPLD** located on the Stator Board.
* **CPLD support:** PCB passive routing (no discrete component).
* **Signal Path:** Rotor 30 Out → Reflector Contacts → 60-pin FPC → Stator CPLD → 60-pin FPC → Reflector Contacts → Rotor 30 In.

## 3. JTAG & Logic Hub

* **Interconnect:** 16-pin (2x8) 2.54mm Shrouded Box Header (Vertical) — J1 pin allocation:
  * Pin 1: 3V3_ENIG (power in)
  * Pin 2: GND
  * Pins 3–8: ENC_IN[0:5]
  * Pins 9–14: ENC_OUT[0:5]
  * Pin 15: TDO_RETURN
  * Pin 16: GND

> **Compatibility note:** J1 pin allocation matches Stator J5 (16-pin 2×8). The Stator J5 was reduced from 20-pin to 16-pin in the design review (this revision) — J1 requires no changes.

* **Bulk Entry Bank Rule:**Use **5x 10uF X7R 50V** bulk decoupling capacitors near the interconnect power-entry pins in a **Symmetrical Star/Spoke pattern**.
* **Termination:** R1 (22Ω) is a series damping resistor on the TDO return line (end-of-chain
  signal from Rotor 30). It provides impedance damping at the final rotor output before the signal
  re-enters the Extension Port for return to the Stator.
* **Pull Resistors (R2–R3, 10kΩ):** TMS pull-up to 3V3_ENIG and TDI pull-up to 3V3_ENIG —
  ensures the JTAG TAP holds a defined state at the chain end when the controller is idle.
* **JTAG Trace Width Rule:** All JTAG signal traces on L1 (TDO_RETURN and any in-board JTAG
  routing) shall be routed at **0.127 mm (5 mil)** width over the L2 GND plane, targeting
  **50 Ω controlled impedance**. Stackup upgraded to 4-Layer per DEC-017.
  See `design/Electronics/JTAG_Integrity.md` and DEC-016.
* **JTAG Return:** TDO from Rotor 30 is routed to Pin 16 for return to the Stator.
* **Loopback:** Directly routes 6-bit ENC_IN to 6-bit ENC_OUT via 2oz 10-mil traces.
* **Cross-ref:** For interconnect pinouts on power (3V3_ENIG/GND), ENC_IN/ENC_OUT, and JTAG TDO_RETURN lines used for reflector loopback/plugboard mapping, See:
  * `Stator/Design_Spec.md`
  * `Extension/Design_Spec.md`

### GND_CHASSIS Single-Point Bond

Per `design/Standards/Global_Routing_Spec.md §4`, each PCB must have a single-point GND_CHASSIS bond at its power entry connector.

**Reflector GND_CHASSIS bond point:** The GND_CHASSIS connection is made at J1 (Stator/Extension link connector, pin 2 or 16 GND).
A single 0 Ω bond resistor (or direct via) connects the signal GND plane to the chassis copper pour at this point.
No additional bonds are made on this board to avoid ground loops.

## 4. Diagnostic & Monitoring

To ensure the signal has successfully navigated the 30-rotor stack, a dedicated monitoring bank is included.

* **Bank Configuration:** 2x8 ENIG Gold Diagnostic Looped Probe Pad Bank.
* **Standard:** Matches the **Controller Board** 2.54mm (0.1") pitch standard for unified system debugging.
* **Labelling:** `REFLEKTOR-DIAGNOSE [Reflector Diag]` in ALL-CAPS German typewriter font.

## 5. PCB & Mechanical Specs

* **Stackup:** 4-Layer (JLC04161H-7628) / 2oz Finished Copper.
* **Layer Mapping:** L1: Signal (JTAG/routing) | L2: GND | L3: 3V3_ENIG | L4: Signal (Data Plate).
* **Contacts:** 26x Gold-plated friction pads matching the Rotor Module pitch.
* **Fillets:** 2.0mm Rounded PCB corners for consistent "Museum-Grade" enclosure fit.
* **Routing:** Global **0.5mm Fixed-Radius Circular Arcs** for all loopback traces.

## 6. Branding & Traceability

* **Data Plate:** Inverted white silkscreen "Data Plate" on Bottom (L4) containing the Enigma silhouette, "ENIGMA-NG" text, and JLC Serial Number block.
* **Label:** `REFLEKTOR-EINHEIT [Reflector Unit]` in ALL-CAPS German typewriter font.

## 7. Bill of Materials

| Ref | Component | Value | Package | Mouser Part # | DigiKey Part # | JLCPCB Part # |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| C1-C5 | Bulk entry decoupling bank (star/spoke) | 10uF X7R 50V | 1206 | 187-CL31B106KBHNNNE | 1276-6767-1-ND | CL31B106KBHNNNE |
| J1 | Interconnect header | 16-pin 2x8 shrouded | 2.54mm | 538-22-23-2161 | WM2907-ND | ??? |
| J2 | Diagnostic looped probe pads | 2x8 ENIG Gold | 2.54mm | ??? | ??? | ??? |
| R1 | JTAG termination | 22Ω | 0603 | 667-ERJ-3EKF2200V | P22.0BYCT-ND | C25805 |
| R2-R3 | Pull-up resistors | 10kΩ | 0603 | 667-ERJ-3EKF1002V | P10.0KBYCT-ND | C25804 |

> **Design decision history:** See `design/Design_Log.md` for all formal design decisions (DEC-xxx) applicable to this board.
