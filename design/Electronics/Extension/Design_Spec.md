# Detailed Design: Extension Board (V1.0)

**Status:** Draft
**Version:** v1.0.0
**Associated Hardware Revision:** Rev A
**Last Updated:** 2026-04-04

## 1. Modular "Mini-Stack" Logic

* **Role:** Mechanical anchor and Power Injection for 5-rotor groups.
* **Capacity:** Supports a 30-rotor maximum stack via modular 5-rotor increments.

## 2. Connectivity

* **Bus Interface:** Dual 20-pin (2x10) Vertical Shrouded Headers (IN/OUT).
* **Power Injection:** Receives 3V3_ENIG and GND daisy-chain to prevent voltage sag across long stacks.
* **Bulk Entry Bank Rule:** Use **5x 10uF X7R 50V** bulk decoupling capacitors near the input header power-entry pins in a **Symmetrical Star/Spoke pattern**.
* **JTAG:** Pass-through for the serial chain; carries TDO_RETURN via dedicated Pin 16.
* **Cross-ref:** For interconnect pinouts on power (3V3_ENIG/GND), ENC_IN/ENC_OUT, and JTAG TDO_RETURN lines used for reflector loopback/plugboard mapping, See:
  * `Stator/Design_Spec.md`
  * `Reflector/Design_Spec.md`

## 3. Diagnostics & Branding

* **Diagnostics:** Integrated 2x8 ENIG Gold Diagnostic Looped Probe Pad Bank (Mid-Stack troubleshooting).
* **Identity:** 2oz Copper / Inverted White Data Plate (V1.0 traceability).

## 4. Bill of Materials

| Ref | Component | Value | Package | Mouser Part # | DigiKey Part # | JLCPCB Part # |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| C1-C5 | Bulk entry decoupling bank (star/spoke) | 10uF X7R 50V | 1206 | 187-CL31B106KBHNNNE | 1276-6767-1-ND | CL31B106KBHNNNE |
| J1 | Input header | 20-pin 2x10 shrouded | 2.54mm | 538-22-23-2201 | WM2911-ND | ??? |
| J2 | Output header | 20-pin 2x10 shrouded | 2.54mm | 538-22-23-2201 | WM2911-ND | ??? |
| J3 | Diagnostic looped probe pads | 2x8 ENIG Gold | 2.54mm | ??? | ??? | ??? |
| R1 | Power resistors | 0Ω or 10Ω (optional) | 0603 | 667-ERJ-3GEY0R00V | P0.0BYCT-ND | C25807 |

> **Design decision history:** See `design/Design_Log.md` for all formal design decisions (DEC-xxx) applicable to this board.
