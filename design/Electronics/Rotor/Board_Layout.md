# Rotor Board Layout Visualisations

**Status:** Draft
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
|   [ EDGE-RATE CONTACTS ] <--- Gold-plated friction pads (Samtec ERM8)      |
|   (Input side — mates with Stator/Extension J2–J4 input connectors)        |
|                                                                             |
|   [ EDGE-RATE CONTACTS ] <--- Gold-plated friction pads (Samtec ERM8)      |
|   (Output side — mates with next rotor input or Reflector last contacts)   |
|_____________________________________________________________________________|
```

---

## Rotor Interface Connectors

> **Connector Definition Owner:** This board. All other boards hosting rotor interface connectors
> (Stator J2–J4, Extension rotor connectors, Reflector contacts) cross-reference here.

Each rotor position uses **three connectors** — one for ENC data in, one for ENC data out, and one for power/JTAG.
These three connectors must be **positionally identical** across every board that mates with rotors
(Stator input side, Extension mid-stack, Reflector final output) to allow any rotor to mate at any position.

### Connector Type

**Samtec ERM8-020-05.0-S-DV-K-TR** (Male, 40-pin, 0.8mm pitch, 5.0mm stack height).
Mating connector: **Samtec CLP Series** low-profile female socket on Stator/Extension/Reflector boards.
ENIG-finished pads; rated for high mating cycles; hot-swap capable.

> **⚠️ Note:** The Rotor connector is a 0.8mm pitch Samtec Edge-Rate series. It is **not** compatible
> with 2.54mm shrouded headers. Stator J2–J4 and Extension rotor connectors must use the matching
> Samtec CLP female socket, not standard IDC headers.

### ENC-IN Connector Signal Map

| Pin | Signal | Direction | Notes |
| :--- | :--- | :--- | :--- |
| 1 | 3V3_ENIG | In | Logic power supply |
| 2 | ENC_IN[0] | In | Encryption input bit 0 (from previous stage) |
| 3 | ENC_IN[1] | In | Encryption input bit 1 |
| 4 | ENC_IN[2] | In | Encryption input bit 2 |
| 5 | ENC_IN[3] | In | Encryption input bit 3 |
| 6 | ENC_IN[4] | In | Encryption input bit 4 |
| 7 | ENC_IN[5] | In | Encryption input bit 5 |
| 8 | GND | — | Signal return |

### ENC-OUT Connector Signal Map

| Pin | Signal | Direction | Notes |
| :--- | :--- | :--- | :--- |
| 1 | 3V3_ENIG | Out | Logic power pass-through |
| 2 | ENC_OUT[0] | Out | Encryption output bit 0 (to next stage) |
| 3 | ENC_OUT[1] | Out | Encryption output bit 1 |
| 4 | ENC_OUT[2] | Out | Encryption output bit 2 |
| 5 | ENC_OUT[3] | Out | Encryption output bit 3 |
| 6 | ENC_OUT[4] | Out | Encryption output bit 4 |
| 7 | ENC_OUT[5] | Out | Encryption output bit 5 |
| 8 | GND | — | Signal return |

### PWR/JTAG Connector Signal Map

| Pin | Signal | Direction | Notes |
| :--- | :--- | :--- | :--- |
| 1 | 3V3_ENIG | In | Main power supply for CPLD and logic |
| 2 | GND | — | Power return |
| 3 | TCK | In | JTAG clock (broadcast from Stator) |
| 4 | GND | — | TCK shield |
| 5 | TMS | In | JTAG mode select (broadcast from Stator) |
| 6 | GND | — | TMS shield |
| 7 | TDI | In | JTAG data in (daisy-chain from previous rotor) |
| 8 | GND | — | TDI shield |
| 9 | SYS_RESET_N | In | Active-low CPLD reset (from Controller GPIO 26) |
| 10 | GND | — | SYS_RESET_N shield |
| 11 | TDO | Out | JTAG data out (daisy-chain to next rotor; TDO_RETURN on last rotor) |
| 12 | GND | — | TDO shield |
| 13 | 3V3_ENIG | In | Additional power pin (parallel with pin 1) |
| 14 | GND | — | Power return |

### TDO Routing Note

TDO does not chain back through the Extension Port individually per rotor. Each rotor passes TDO to the
**next rotor's TDI** directly via the PWR/JTAG connector. Only **Rotor 30** (last in chain) routes its
TDO to the Reflector TDO_RETURN pad, which carries it back to the Stator via the Extension Port (J5 Pin 15).
