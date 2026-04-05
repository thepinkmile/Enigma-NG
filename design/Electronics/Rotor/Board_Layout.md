# Rotor Board Layout Visualisations

**Status:** Draft
**Project:** Enigma-NG
**Author:** Enigma-NG Hardware Team
**Version:** v1.0.0
**Associated Hardware Revision:** Rev A
**Last Updated:** 2026-04-05

---

## Component Areas

```text
TOP VIEW (L1) - 4-Layer / 2oz Copper / ENIG
 _____________________________________________________________________________
|                                                                             |
|   [ CPLD ] <--- Intel MAX II EPM240T100C5N                                  |
|   (Wiring emulation + position decode)                                      |
|                                                                             |
|   [ AS5600 ] <--- Magnetic encoder IC                                       |
|   (6-bit Grey code position)                                                |
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
(last in chain) routes its TDO via the Reflector back to Stator J7 pin 15 as TDO_RETURN.
