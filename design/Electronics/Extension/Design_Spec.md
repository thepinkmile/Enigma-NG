# Detailed Design: Extension Board (V1.0)

**Status:** Draft
**Version:** v1.0.0
**Associated Hardware Revision:** Rev A
**Last Updated:** 2026-04-05

## 1. Modular "Mini-Stack" Logic

* **Role:** Mechanical anchor and Power Injection for 5-rotor groups.
* **Capacity:** Supports a 30-rotor maximum stack via modular 5-rotor increments.

## 2. Connectivity

* **Extension Port (J7 IN / J8 OUT):** 16-pin 2×8 shrouded box header.
  > **Connector Definition Owner:** `Stator/Board_Layout.md — J7`.
  > This board uses the mating connector on both J7 and J8 (Molex 22-23-2161 or equivalent — see BOM).
  > Authoritative pinout: Pin 1 = 3V3_ENIG, Pin 2 = SYS_RESET_N, Pins 3–8 = ENC_IN[0:5],
  > Pins 9–14 = ENC_OUT[0:5], Pin 15 = TDO_RETURN, Pin 16 = GND.
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
  Connector part numbers: ERM8-005 = Mouser 200-ERM8005050SDVKTR / DigiKey 612-ERM8-005-05.0-S-DV-K-TRCT-ND / JLCPCB C374877;
  ERM8-010 = Mouser 200-ERM8010050SDVKTR / DigiKey SAM8610CT-ND / JLCPCB C374877;
  ERF8-005 = Mouser 200-ERF8005050SDVKTR / DigiKey SAM13517CT-ND / JLCPCB C7273978;
  ERF8-010 = Mouser 200-ERF8010050SDVKTR / DigiKey SAM8618CT-ND / JLCPCB C3646170.

* **JTAG Signal Buffering:** The Extension board provides JTAG re-buffering for the 5-rotor group
  connected to its output side (J4–J6). A **74LVC2G125** dual-channel 3-state buffer (U1) buffers the
  **TCK and TMS** lines, providing a fresh drive from the Extension board's 3V3_ENIG rail:
  * TCK buffer output → J4 pin **2** (TCK) and broadcast to all 5 rotors in the output group.
  * TMS buffer output → J4 pin **4** (TMS) and broadcast.
  * Buffer enable (OE#): tied to GND permanently (always enabled).
  * Part: SN74LVC2G125DCUR (TI, SOT-23-6) — Mouser 595-SN74LVC2G125DCUR,
    DigiKey 296-SN74LVC2G125DCURCT-ND, JLCPCB C15281.
  * At 5 rotors per group, signal integrity analysis confirms this buffer interval is sufficient:
    5 rotors × EPM240 input capacitance (≈6pF) = 30pF total load; τ = 95Ω × 30pF = 2.85ns,
    well within the 50ns half-period at 10MHz TCK.

* **GND_CHASSIS Single-Point Bond:** Per `design/Standards/Global_Routing_Spec.md §4`, a single
  0Ω bond resistor (R2) or direct via connects signal GND to chassis copper pour at J7 pin 16 (GND).
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
* **JTAG Trace Width Rule:** The Extension board carries only the **TDO_RETURN** signal on its J7/J8 pass-through path
  (TCK, TMS, and TDI travel to the rotor stack via Stator J1–J3, not via the Extension Port). TDO_RETURN traces on L1 shall be routed at **0.127 mm (5 mil)**
  over the L2 GND plane, targeting **50 Ω controlled impedance**. See
  `design/Electronics/Investigations/JTAG_Integrity.md` and DEC-016. Stackup defined per DEC-017.
* **U1 Bypass:** C6 (100nF) must be placed within 2mm of U1 VCC pin on L1.

## 5. Bill of Materials

| Ref | Component | Value | Package | Mouser Part # | DigiKey Part # | JLCPCB Part # |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| C1-C5 | Bulk entry decoupling bank (star/spoke) | 10uF X7R 50V | 1206 | 187-CL31B106KBHNNNE | 1276-6767-1-ND | CL31B106KBHNNNE |
| C6 | 100nF X7R 50V bypass — U1 VCC | Samsung CL05B104KB5NNNC | 0402 | 187-CL05B104KB5NNNC | 1276-1009-1-ND | C1525 |
| J1 | Rotor group input — JTAG (ERM8-005, 10-pin **male**, 0.8mm pitch) | Samtec ERM8-005-05.0-S-DV-K-TR | SMT | 200-ERM8005050SDVKTR | 612-ERM8-005-05.0-S-DV-K-TRCT-ND | C374877 |
| J2 | Rotor group input — Power (ERM8-005, 10-pin **male**, 0.8mm pitch) | Samtec ERM8-005-05.0-S-DV-K-TR | SMT | 200-ERM8005050SDVKTR | 612-ERM8-005-05.0-S-DV-K-TRCT-ND | C374877 |
| J3 | Rotor group input — ENC Data (ERM8-010, 20-pin **male**, 0.8mm pitch) | Samtec ERM8-010-05.0-S-DV-K-TR | SMT | 200-ERM8010050SDVKTR | SAM8610CT-ND | C374877 |
| J4 | Rotor group output — JTAG (ERF8-005, 10-pin female, 0.8mm pitch) | Samtec ERF8-005-05.0-S-DV-K-TR | SMT | 200-ERF8005050SDVKTR | SAM13517CT-ND | C7273978 |
| J5 | Rotor group output — Power (ERF8-005, 10-pin female, 0.8mm pitch) | Samtec ERF8-005-05.0-S-DV-K-TR | SMT | 200-ERF8005050SDVKTR | SAM13517CT-ND | C7273978 |
| J6 | Rotor group output — ENC Data (ERF8-010, 20-pin female, 0.8mm pitch) | Samtec ERF8-010-05.0-S-DV-K-TR | SMT | 200-ERF8010050SDVKTR | SAM8618CT-ND | C3646170 |
| J7 | Extension Port IN header | 16-pin 2×8 shrouded box | 2.54mm | 538-22-23-2161 | WM2907-ND | ??? |
| J8 | Extension Port OUT header | 16-pin 2×8 shrouded box | 2.54mm | 538-22-23-2161 | WM2907-ND | ??? |
| J9 | Diagnostic looped probe pads | 2x8 ENIG Gold | 2.54mm | ??? | ??? | ??? |
| R1 | GND plane isolating resistor (optional) | 0Ω or 10Ω | 0603 | 667-ERJ-3GEY0R00V | P0.0BYCT-ND | C25807 |
| R2 | GND_CHASSIS single-point bond | 0Ω | 0603 | 667-ERJ-3GEY0R00V | P0.0BYCT-ND | C25807 |
| U1 | JTAG TCK/TMS dual buffer for output rotor group | SN74LVC2G125DCUR | SOT-23-6 | 595-SN74LVC2G125DCUR | 296-SN74LVC2G125DCURCT-ND | C15281 |

> **Design decision history:** See `design/Design_Log.md` for all formal design decisions (DEC-xxx) applicable to this board.
