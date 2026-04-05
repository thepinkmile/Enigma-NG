# Detailed Design: Extension Board (V1.0)

**Status:** Draft
**Version:** v1.0.0
**Associated Hardware Revision:** Rev A
**Last Updated:** 2026-04-04

## 1. Modular "Mini-Stack" Logic

* **Role:** Mechanical anchor and Power Injection for 5-rotor groups.
* **Capacity:** Supports a 30-rotor maximum stack via modular 5-rotor increments.

## 2. Connectivity

* **Extension Port (J1 IN / J2 OUT):** 16-pin 2×8 shrouded box header.
  > **Connector Definition Owner:** `Stator/Board_Layout.md — J5`.
  > This board uses the mating connector on both J1 and J2 (Molex 22-23-2161 or equivalent — see BOM).
  > Authoritative pinout: Pin 1 = 3V3_ENIG, Pin 2 = SYS_RESET_N, Pins 3–8 = ENC_IN[0:5],
  > Pins 9–14 = ENC_OUT[0:5], Pin 15 = TDO_RETURN, Pin 16 = GND.
* **Rotor Interface Connectors (3 per rotor-facing side):** ENC-IN, ENC-OUT, and PWR/JTAG connector set. Must be
  **positionally identical** to the matching set on the Stator (Rotor 1 input) and Reflector (last rotor output).
  See `Stator/Board_Layout.md` J2–J4 section for planned signal groups. Exact pin count and connector type are
  pending mechanical design finalisation.
* **Power Injection:** Receives 3V3_ENIG and GND via Extension Port to prevent voltage sag across long stacks.
* **Bulk Entry Bank Rule:** Use **5x 10uF X7R 50V** bulk decoupling capacitors near the input header power-entry pins in a **Symmetrical Star/Spoke pattern**.
* **JTAG:** Pass-through for the serial chain; TDO_RETURN carried via Extension Port pin 15.
  * This board carries JTAG signals as a passive pass-through only. No active termination is
    required here; series termination is placed at the driving ends of each cable segment on
    the Stator (R7–R15) and Encoder boards (R7, R8). See `design/Electronics/Investigations/JTAG_Integrity.md`
    and DEC-016.
* **SYS_RESET_N:** Received via Extension Port pin 2; broadcast to all local rotor CPLDs in this group.
* **Cross-ref:** For interconnect pinouts on power (3V3_ENIG/GND), ENC_IN/ENC_OUT, and JTAG TDO_RETURN lines used for reflector loopback/plugboard mapping, See:
  * `Stator/Design_Spec.md`
  * `Reflector/Design_Spec.md`

## 3. Diagnostics & Branding

* **Diagnostics:** Integrated 2x8 ENIG Gold Diagnostic Looped Probe Pad Bank (Mid-Stack troubleshooting).
* **Identity:** 2oz Copper / Inverted White Data Plate (V1.0 traceability).

## 4. PCB Specs (JLCPCB)

* **Layers:** 4-Layer (JLC04161H-7628).
* **Finish:** ENIG (Gold) for connector and diagnostic pad surfaces.
* **Layer Mapping:** L1: Signal (JTAG pass-through / routing) | L2: GND | L3: 3V3_ENIG | L4: Signal (Data Plate).
* **Aesthetics:** Dark Green Solder Mask; Typewriter font (ALL-CAPS GERMAN).
* **JTAG Trace Width Rule:** The Extension board carries only the **TDO_RETURN** signal on its J1/J2 pass-through path
  (TCK, TMS, and TDI travel to the rotor stack via Stator J2–J4, not via the Extension Port). TDO_RETURN traces on L1 shall be routed at **0.127 mm (5 mil)**
  over the L2 GND plane, targeting **50 Ω controlled impedance**. See
  `design/Electronics/Investigations/JTAG_Integrity.md` and DEC-016. Stackup defined per DEC-017.

## 5. Bill of Materials

| Ref | Component | Value | Package | Mouser Part # | DigiKey Part # | JLCPCB Part # |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| C1-C5 | Bulk entry decoupling bank (star/spoke) | 10uF X7R 50V | 1206 | 187-CL31B106KBHNNNE | 1276-6767-1-ND | CL31B106KBHNNNE |
| J1 | Extension Port IN header | 16-pin 2×8 shrouded box | 2.54mm | 538-22-23-2161 | WM2907-ND | ??? |
| J2 | Extension Port OUT header | 16-pin 2×8 shrouded box | 2.54mm | 538-22-23-2161 | WM2907-ND | ??? |
| J3–J8 | Rotor interface connectors (3 per side × 2 sides — spec pending) | TBD | TBD | ??? | ??? | ??? |
| J9 | Diagnostic looped probe pads | 2x8 ENIG Gold | 2.54mm | ??? | ??? | ??? |
| R1 | Power resistors | 0Ω or 10Ω (optional) | 0603 | 667-ERJ-3GEY0R00V | P0.0BYCT-ND | C25807 |

> **Design decision history:** See `design/Design_Log.md` for all formal design decisions (DEC-xxx) applicable to this board.
