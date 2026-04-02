# Reflector Board (V1.0) Design Specification

The Reflector Board sits at the far end of the 30-rotor stack. Its primary role is to receive the signals from the final rotor and return them back through the stack via a different electrical path.
It also acts as the JTAG termination hub and returns the JTAG_TDO directly back to the Stator to reduce required Pin count in the Rotor Interconnects.

## 1. Architecture

* **PCB:** 2oz Finished Copper / ENIG Gold / 2.0mm Filleted Corners.
* **Standard:** Includes Inverted White Data Plate on bottom layer.

### System Role: The "Turnaround"

* **Logic Type:** Passive (Loopback).
* **Routing Logic:** All signal mapping is handled remotely by the **Intel MAX II EPM240T100C5N CPLD** located on the Stator Board.
* **Signal Path:** Rotor 30 Out → Reflector Contacts → 60-pin FPC → Stator CPLD → 60-pin FPC → Reflector Contacts → Rotor 30 In.

## 2. JTAG & Logic Hub

* **Interconnect:** 16-pin (2x8) 2.54mm Shrouded Box Header (Vertical).
* **Termination:** 22Ω series resistor on TDO and 10kΩ pull-ups on TMS/TDI for end-of-chain stability.
* **JTAG Return:** TDO from Rotor 30 is routed to Pin 16 for return to the Stator.
* **Loopback:** Directly routes 6-bit ENC_IN to 6-bit ENC_OUT via 2oz 10-mil traces.
* **Cross-ref:** For interconnect pinouts on power (3V3_ENIG/GND), ENC_IN/ENC_OUT, and JTAG TDO_RETURN lines used for reflector loopback/plugboard mapping, See:
  * `Stator/Design_Spec.md`
  * `Extension/Design_Spec.md`

## 3. Diagnostic & Monitoring

To ensure the signal has successfully navigated the 30-rotor stack, a dedicated monitoring bank is included.

* **Bank Configuration:** 2x8 Gold-plated (ENIG) Diagnostic Probe Bank.
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

* **Diagnostics:** 2x8 ENIG Gold Diagnostic Bank on L1 for logic analysis.

---

## Bill of Materials

| Ref | Component | Value | Package | Mouser Part # | DigiKey Part # |
| :--- | :--- | :--- | :--- | :--- | :--- |
| J1 | Interconnect header | 16-pin 2x8 shrouded | 2.54mm | ??? | ??? |
| J2 | Diagnostic Bank | 2x8 ENIG | 2.54mm | ??? | ??? |
| R1 | JTAG termination | 22Ω | 0603 | ??? | ??? |
| R2-R3 | Pull-up resistors | 10kΩ | 0603 | ??? | ??? |
| U1 | CPLD support | (passive routing) | PCB | N/A | N/A |
