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
* **Rotor Interface Connectors (3 per rotor-facing side × 2 sides = 6 connectors total):**
  The Extension board provides ERF8 female sockets on **both** the input side (J3–J5, facing the
  previous rotor group's output ERM8 headers) and the output side (J6–J8, facing the next rotor
  group's input ERM8 headers). The connector type matches the Stator rotor interface exactly:

  > **Connector Definition Owner:** `Rotor/Board_Layout.md — Rotor Interface Connectors`.
  > This board uses mating ERF8 female sockets on both sides. Signal groups per side:

  | Ref | Side | Signal Group | Type | MPN |
  | --- | ---- | ------------ | ---- | --- |
  | J3 | Input (from previous group output) | JTAG | ERF8-005 (10-pin, 0.8mm pitch, female) | ERF8-005-05.0-S-DV-K-TR |
  | J4 | Input (from previous group output) | Power (3V3_ENIG × 5, GND × 5) | ERF8-005 (10-pin, 0.8mm pitch, female) | ERF8-005-05.0-S-DV-K-TR |
  | J5 | Input (from previous group output) | ENC Data (ENC_IN/ENC_OUT + GND) | ERF8-010 (20-pin, 0.8mm pitch, female) | ERF8-010-05.0-S-DV-K-TR |
  | J6 | Output (to next group input) | JTAG | ERF8-005 (10-pin, 0.8mm pitch, female) | ERF8-005-05.0-S-DV-K-TR |
  | J7 | Output (to next group input) | Power (3V3_ENIG × 5, GND × 5) | ERF8-005 (10-pin, 0.8mm pitch, female) | ERF8-005-05.0-S-DV-K-TR |
  | J8 | Output (to next group input) | ENC Data (ENC_IN/ENC_OUT + GND) | ERF8-010 (20-pin, 0.8mm pitch, female) | ERF8-010-05.0-S-DV-K-TR |

  **Note:** The ERF8 0.8mm pitch is physically incompatible with 2.54mm connectors — label distinctly on silkscreen.
  Connector part numbers: ERF8-005 = Mouser 200-ERF8005050SDVKTR / DigiKey SAM13517CT-ND / JLCPCB C7273978;
  ERF8-010 = Mouser 200-ERF8010050SDVKTR / DigiKey SAM8618CT-ND / JLCPCB C3646170.

* **JTAG Signal Buffering:** The Extension board provides JTAG re-buffering for the 5-rotor group
  connected to its output side (J6–J8). A **74LVC2G125** dual-channel 3-state buffer (U1) buffers the
  **TCK and TMS** lines, providing a fresh drive from the Extension board's 3V3_ENIG rail:
  * TCK buffer output → J6 pin 1 (TCK) and broadcast to all 5 rotors in the output group.
  * TMS buffer output → J6 pin 3 (TMS) and broadcast.
  * Buffer enable (OE#): tied to GND permanently (always enabled).
  * Part: SN74LVC2G125DCUR (TI, SOT-23-6) — Mouser 595-SN74LVC2G125DCUR,
    DigiKey 296-SN74LVC2G125DCURCT-ND, JLCPCB C15281.
  * At 5 rotors per group, signal integrity analysis confirms this buffer interval is sufficient:
    5 rotors × EPM240 input capacitance (≈6pF) = 30pF total load; τ = 95Ω × 30pF = 2.85ns,
    well within the 50ns half-period at 10MHz TCK.

* **GND_CHASSIS Single-Point Bond:** Per `design/Standards/Global_Routing_Spec.md §4`, a single
  0Ω bond resistor (R2) or direct via connects signal GND to chassis copper pour at J1 pin 16 (GND).
  No additional bonds on this board to prevent ground loops.
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
| J3 | Rotor input side — JTAG (ERF8-005, 10-pin female, 0.8mm pitch) | Mating with incoming-rotor ERM8-005 | SMT | 200-ERF8005050SDVKTR | SAM13517CT-ND | C7273978 |
| J4 | Rotor input side — Power (ERF8-005, 10-pin female, 0.8mm pitch) | Mating with incoming-rotor ERM8-005 | SMT | 200-ERF8005050SDVKTR | SAM13517CT-ND | C7273978 |
| J5 | Rotor input side — ENC Data (ERF8-010, 20-pin female, 0.8mm pitch) | Mating with incoming-rotor ERM8-010 | SMT | 200-ERF8010050SDVKTR | SAM8618CT-ND | C3646170 |
| J6 | Rotor output side — JTAG (ERF8-005, 10-pin female, 0.8mm pitch) | Mating with outgoing-rotor ERM8-005 | SMT | 200-ERF8005050SDVKTR | SAM13517CT-ND | C7273978 |
| J7 | Rotor output side — Power (ERF8-005, 10-pin female, 0.8mm pitch) | Mating with outgoing-rotor ERM8-005 | SMT | 200-ERF8005050SDVKTR | SAM13517CT-ND | C7273978 |
| J8 | Rotor output side — ENC Data (ERF8-010, 20-pin female, 0.8mm pitch) | Mating with outgoing-rotor ERM8-010 | SMT | 200-ERF8010050SDVKTR | SAM8618CT-ND | C3646170 |
| J9 | Diagnostic looped probe pads | 2x8 ENIG Gold | 2.54mm | ??? | ??? | ??? |
| R1 | GND plane isolating resistor (optional) | 0Ω or 10Ω | 0603 | 667-ERJ-3GEY0R00V | P0.0BYCT-ND | C25807 |
| R2 | GND_CHASSIS single-point bond | 0Ω | 0603 | 667-ERJ-3GEY0R00V | P0.0BYCT-ND | C25807 |
| U1 | JTAG TCK/TMS dual buffer for output rotor group | SN74LVC2G125DCUR | SOT-23-6 | 595-SN74LVC2G125DCUR | 296-SN74LVC2G125DCURCT-ND | C15281 |

> **Design decision history:** See `design/Design_Log.md` for all formal design decisions (DEC-xxx) applicable to this board.
