# Reflector Board (V1.0) Design Specification

The Reflector Board sits at the far end of the 30-rotor stack. Its primary role is to receive the signals from the final rotor and return them back through the stack via a different electrical path.
It also acts as the JTAG termination hub and returns the JTAG_TDO directly back to the Stator to reduce required Pin count in the Rotor Interconnects.

## 1. Architecture

* **PCB:** 2oz Finished Copper / ENIG Gold / 2.0mm Filleted Corners.
* **Standard:** Includes Inverted White Data Plate on bottom layer.

### System Role: The "Turnaround"

* **Logic Type:** Passive (Loopback).
* **Routing Logic:** All signal mapping is handled remotely by the **Intel MAX II EPM240T100C5N CPLD** located on the Stator Board.
* **CPLD support:** PCB passive routing (no discrete component).
* **Signal Path:** Rotor 30 Out → Reflector Contacts → 60-pin FPC → Stator CPLD → 60-pin FPC → Reflector Contacts → Rotor 30 In.

## 2. JTAG & Logic Hub

* **Interconnect:** 16-pin (2x8) 2.54mm Shrouded Box Header (Vertical) — J1 pin allocation:
  - Pin 1: 3V3_ENIG (power in)
  - Pin 2: GND
  - Pins 3–8: ENC_IN[0:5]
  - Pins 9–14: ENC_OUT[0:5]
  - Pin 15: TDO_RETURN
  - Pin 16: GND

> **Compatibility note:** J1 pin allocation matches Stator J5 (16-pin 2×8). The Stator J5 was reduced from 20-pin to 16-pin in the design review (this revision) — J1 requires no changes.
* **Bulk Entry Bank Rule:** Use **5x 10uF X7R 50V** bulk decoupling capacitors near the interconnect power-entry pins in a **Symmetrical Star/Spoke pattern**.
* **Termination:** 22Ω series resistor on TDO and 10kΩ pull-ups on TMS/TDI for end-of-chain stability.
* **JTAG Return:** TDO from Rotor 30 is routed to Pin 16 for return to the Stator.
* **Loopback:** Directly routes 6-bit ENC_IN to 6-bit ENC_OUT via 2oz 10-mil traces.
* **Cross-ref:** For interconnect pinouts on power (3V3_ENIG/GND), ENC_IN/ENC_OUT, and JTAG TDO_RETURN lines used for reflector loopback/plugboard mapping, See:
  * `Stator/Design_Spec.md`
  * `Extension/Design_Spec.md`

### GND_CHASSIS Single-Point Bond

Per `design/Standards/Global_Routing_Spec.md §4`, each PCB must have a single-point GND_CHASSIS bond at its power entry connector.

**Reflector GND_CHASSIS bond point:** The GND_CHASSIS connection is made at J1 (Stator/Extension link connector, pin 2 or 16 GND). A single 0 Ω bond resistor (or direct via) connects the signal GND plane to the chassis copper pour at this point. No additional bonds are made on this board to avoid ground loops.

## 3. Diagnostic & Monitoring

To ensure the signal has successfully navigated the 30-rotor stack, a dedicated monitoring bank is included.

* **Bank Configuration:** 2x8 ENIG Gold Diagnostic Looped Probe Pad Bank.
* **Standard:** Matches the **Controller Board** 2.54mm (0.1") pitch standard for unified system debugging.
* **Labelling:** `REFLEKTOR-DIAGNOSE [Reflector Diag]` in ALL-CAPS German typewriter font.

## 4. PCB & Mechanical Specs

* **Stackup:** 2-Layer / 1oz Copper.
* **Contacts:** 26x Gold-plated friction pads matching the Rotor Module pitch.
* **Fillets:** 2.0mm Rounded PCB corners for consistent "Museum-Grade" enclosure fit.
* **Routing:** Global **0.5mm Fixed-Radius Circular Arcs** for all loopback traces.

## 5. Branding & Traceability

* **Data Plate:** Inverted white silkscreen "Data Plate" on Bottom (L2) containing the Enigma silhouette, "ENIGMA-NG" text, and JLC Serial Number block.
* **Label:** `REFLEKTOR-EINHEIT [Reflector Unit]` in ALL-CAPS German typewriter font.

## 6. Maintenance

* **Diagnostics:** 2x8 ENIG Gold Diagnostic Looped Probe Pad Bank on L1 for logic analysis.

---

## Bill of Materials

| Ref | Component | Value | Package | Mouser Part # | DigiKey Part # | JLCPCB Part # |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| C1-C5 | Bulk entry decoupling bank (star/spoke) | 10uF X7R 50V | 1206 | 187-CL31B106KBHNNNE | 1276-6767-1-ND | CL31B106KBHNNNE |
| J1 | Interconnect header | 16-pin 2x8 shrouded | 2.54mm | 538-22-23-2161 | WM2907-ND | ??? |
| J2 | Diagnostic looped probe pads | 2x8 ENIG Gold | 2.54mm | ??? | ??? | ??? |
| R1 | JTAG termination | 22Ω | 0603 | 667-ERJ-3EKF2200V | P22.0BYCT-ND | C25805 |
| R2-R3 | Pull-up resistors | 10kΩ | 0603 | 667-ERJ-3EKF1002V | P10.0KBYCT-ND | C25804 |
