# Rotor Board Layout Visualisations

**Status:** Draft
**Project:** Enigma-NG
**Author:** Izzyonstage & GitHub Copilot
**Version:** v1.0.0
**Associated Hardware Revision:** Rev A
**Last Updated:** 2026-04-05

---

## Component Areas

```text
4-Layer / 2oz Copper / ENIG / Circular Ø100mm
 _____________________________________________________________________________
|                                                                             |
|   [ CPLD ] <--- Intel MAX II EPM570T100I5N                                  |
|   (Wiring emulation + position decode)                                      |
|                                                                             |
|   [ FDC2114 U2/U3 ] <--- Capacitive sensor ICs (×2)                        |
|   (Single-track absolute encoder; K pads at r≈47mm outer edge)             |
|                                                                             |
|   [ BULK DECOUPLING ] <--- 5x 10uF X7R star/spoke                          |
|   [ 8x 0.1uF LOCAL ] <--- Per CPLD VCC pin                                 |
|                                                                             |
|   [ EDGE-RATE CONTACTS ] <--- J1–J3: ERM8 male headers (input side — JTAG, Power, ENC Data)    |
|   (Input side — mates with Stator J1–J3 ERF8 female sockets or the previous Rotor's J4–J6 ERF8 female output sockets) |
|                                                                             |
|   [ EDGE-RATE CONTACTS ] <--- J4–J6: ERF8 female sockets (output side — JTAG, Power, ENC Data) |
|   (Output side — mates with next rotor input or Reflector last contacts)   |
|_____________________________________________________________________________|
```

---

## Rotor Interface Connectors

> **Connector Definition Owner:** This board. All other boards hosting rotor interface connectors
> (Stator J1–J3, Extension J1–J6, Reflector J1–J3) cross-reference here.

Each rotor position uses **three connectors** — one for ENC data in, one for ENC data out, and one for power/JTAG.
These three connectors must be **positionally identical** across every board that mates with rotors
(Stator input side, Extension mid-stack, Reflector final output) to allow any rotor to mate at any position.

> **⚠️ Note:** The earlier draft signal maps (ENC-IN, ENC-OUT, PWR/JTAG with 8-pin and 14-pin tables)
> have been removed. All connector definitions now live exclusively in `Rotor/Design_Spec.md §3.4`.
> Use the Design_Spec §3.4 tables for all schematic and PCB layout work.

### Connector Summary

Each rotor carries **six connectors** — three male ERM8 headers on the input side (J1–J3) and three female
ERF8 sockets on the output side (J4–J6). See `Rotor/Design_Spec.md §3.4` for the authoritative pinout tables.

| Designator | Type | Part | Pins | Function |
| :--- | :--- | :--- | :--- | :--- |
| J1 | ERM8-005 male | 200-ERM8005050SDVKTR | 10 (2×5) | JTAG input |
| J2 | ERM8-005 male | 200-ERM8005050SDVKTR | 10 (2×5) | Power input |
| J3 | ERM8-010 male | 200-ERM8010050SDVKTR | 20 (2×10) | Encoder data input |
| J4 | ERF8-005 female | 200-ERF8005050SDVKTR | 10 (2×5) | JTAG output → next rotor J1 |
| J5 | ERF8-005 female | 200-ERF8005050SDVKTR | 10 (2×5) | Power output → next rotor J2 |
| J6 | ERF8-010 female | 200-ERF8010050SDVKTR | 20 (2×10) | Encoder data output → next rotor J3 |

### TTD Routing Note

TTD (JTAG Transmission Data) does not chain back through the Extension Port individually per rotor. Each
rotor passes TTD to the **next rotor's TDI** directly via J4 pin 6 → next Rotor J1 pin 6. Only **Rotor 30**
(last in chain) routes its TDO via the Reflector back to Stator J7 pin 15 as TTD_RETURN.

---

## §9 Routing — Trace Width Specifications

**Board specs:** 4-layer / 2oz finished copper (JLC04161H-7628).
L1 = signal (JTAG/routing); L2 = GND plane; L3 = 3V3_ENIG power pour; L4 = secondary routing / data plate.

**IPC-2221A basis (2oz copper, external, 10°C rise, 25°C ambient):**
For 2oz external: ~0.15 mm/A. The 3V3_ENIG inner pour (L3) handles bus current without width constraints.
See Global_Routing_Spec.md §1.1 for the full current-category table.

**Rotor power analysis (pass-through sizing):**
Each rotor draws 50 mA (EPM570) + 6.5 mA (AS5600) = **56.5 mA ≈ 57 mA** locally.
The J2 power input connector daisy-chains 3V3_ENIG through J5 to the next rotor. All 30 rotor PCBs
are **identical**, so traces must be sized for the worst case — **Rotor 1**, which receives
30 × 57 mA = **1.71 A** through its J2 connector and passes 29 × 57 mA = 1.65 A to Rotor 2 via J5.

| Rotor position | J2 input current | Local draw | J5 output current |
| :--- | :--- | :--- | :--- |
| Rotor 1 (worst case) | 1.71 A | 57 mA | 1.65 A |
| Rotor 15 (mid-stack) | 0.86 A | 57 mA | 0.80 A |
| Rotor 30 (last) | 57 mA | 57 mA | 0 A |

IPC calculation for worst-case 1.71 A at 2oz external: 1.71 × 0.15 mm = 0.26 mm → **0.80 mm** (3V3_ENIG canonical width per Global_Routing_Spec §1.1; consistent with PM and Stator 3V3_ENIG trunk traces).

### Trace Width Table

| Net | Peak Current | IPC Calc (2oz ext) | Design Min | **Specified Width** | Layer | Notes |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Signal (ENC_IN/OUT, AS5600 I2C SDA/SCL) | < 5 mA | < 0.001 mm | 0.20 mm | **0.20 mm** | L1 | 3.3 V logic; CPLD data I/O; I2C to AS5600 magnetic encoder |
| JTAG signals: TCK, TMS, TTD in/out, SYS_RESET_N (CI) | signal | — | 0.127 mm | **0.127 mm (5 mil)** | L1 (external) | 50 Ω controlled impedance over L2 GND plane; per DEC-016. External layer — no inner-layer minimum conflict. |
| 3V3_ENIG local draw (J2 → CPLD + AS5600 supply) | 57 mA | 0.009 mm | 0.80 mm | **0.80 mm** | L1 + L3 pour | 3V3_ENIG canonical 0.80 mm (Global_Routing_Spec §1.1); local IC supply only |
| 3V3_ENIG pass-through rail (J2 input → J5 output bus) | 1.71 A (Rotor 1) | 0.26 mm | 0.80 mm | **0.80 mm** | L1 + L3 pour | Canonical 3V3_ENIG trunk width (Global_Routing_Spec §1.1); Rotor 1 worst case; feeds L3 pour via thermal vias between J2 and J5 |
| 3V3_ENIG distribution (inner power pour) | up to 1.71 A | — | pour | **copper pour** | L3 | Full uninterrupted 2oz plane; primary distribution across the board |
| GND return (inner GND pour) | — | — | pour | **copper pour** | L2 | Reference plane; must be solid and uninterrupted under all CI traces on L1 |

### Notes

* **JTAG CI traces:** 0.127 mm (5 mil) on L1 over the L2 GND plane achieves 50 Ω controlled
  impedance on the JLC04161H-7628 stackup (h = 0.087 mm, t = 0.035 mm, Eᵣ = 4.4). Per DEC-016.
  See `design/Electronics/Investigations/JTAG_Integrity.md §3.1`.
* **Series termination R1 (75 Ω, CPLD TDO → J4 pin 6):** Placed within 2 mm of the CPLD TDO pin.
  Source impedance ≈ 95 Ω targeting the ~100 Ω inter-rotor Stator PCB segment. Trace from R1 to
  J4 kept < 5 mm and routed at 0.127 mm consistent with the CI chain.
* **3V3_ENIG power rail:** The L3 copper pour is the primary current path. L1 surface traces at
  0.80 mm connect J2/J5 connector pads to the L3 pour via thermal vias. All 30 rotor boards share
  the same PCB layout — the 1.71 A worst-case sizing ensures safe operation at every stack position.
