# Encoder Board Layout Visualisations

**Status:** Draft
**Version:** v1.0.0
**Associated Hardware Revision:** Rev A
**Last Updated:** 2026-04-05

## Component Areas

```text
TOP VIEW (L1) - 4-Layer / 2oz Copper
 ____________________________________________________________________________ 
|                                                                            |
|   [ SPADE TERMINAL BANK ] <--- External I/O Interface (Mechanical board)   |
|   (2x8 or 2x10 block for encoder rows, crossover wires)                    |
|                                                                            |
|   [ CPLD ARRAY ] <--- Intel MAX II EPM240T100C5N                           |
|   (Dual Logic Units for I/O Management)                                    |
|                                                                            |
|   [ DATA LINK HEADER ] <--- 26-pin Header (2×13, 2.54mm Pitch)             |
|   (3V3_ENIG, ENC_IN[0:5], JTAG w/GND shields, ENC_OUT[0:5], 3V3_ENIG)     |
|                                                                            |
|   [ DIAGNOSTIC BANK ] <--- 2x8 ENIG Gold Probe Bank                        |
|   (2.54mm Pitch, L1)                                                       |
|                                                                            |
|   [ DATA PLATE ] <--- Inverted White Silkscreen on L4                      |
|   (Enigma Silhouette + JLC Serial)                                         |
|____________________________________________________________________________|
```

## Simplified Layout

```text
_____________________________________________________________________________ 
|                                                                            |
|   [ SPADE TERMINAL BANK ]      [ CPLDs ]      [ DATA LINK ]                |
|                                                                            |
|   (64x Inputs/Outputs)       (Logic Core)   (26-Pin Ribbon Bus)            |
|                                                                            |
|   [ DIAGNOSTIC BANK ]                                                      |
|____________________________________________________________________________|
```

## Data Link Pinout (26-Pin Connector)

> **Connector Definition Owner:** `Stator/Board_Layout.md — J6–J8`.
> The pin table below is reproduced here for layout reference. In case of conflict, the Stator definition is authoritative.

This is a 2×13 (26-pin) 2.54mm shrouded box header with polarisation key. Connects to matching
header on Stator (J6 = HID Unit, J7 = Plugboard A, J8 = Plugboard B).

| Pin | Signal | Direction | Notes |
| :--- | :--- | :--- | :--- |
| 1 | 3V3_ENIG | Stator→Encoder | Power supply |
| 2 | ENC_IN[0] | Stator→Encoder | Encoder input bit 0 |
| 3 | ENC_IN[1] | Stator→Encoder | Encoder input bit 1 |
| 4 | ENC_IN[2] | Stator→Encoder | Encoder input bit 2 |
| 5 | ENC_IN[3] | Stator→Encoder | Encoder input bit 3 |
| 6 | ENC_IN[4] | Stator→Encoder | Encoder input bit 4 |
| 7 | ENC_IN[5] | Stator→Encoder | Encoder input bit 5 |
| 8 | GND | — | ENC_IN / JTAG group separator |
| 9 | TCK | Stator→Encoder | JTAG clock (broadcast) |
| 10 | GND | — | TCK/TMS inter-pin shield |
| 11 | TMS | Stator→Encoder | JTAG mode select (broadcast) |
| 12 | GND | — | TMS/TDO inter-pin shield |
| 13 | TDO | Encoder→Stator | JTAG data out (to next device in chain) |
| 14 | GND | — | TDO/TDI inter-pin shield |
| 15 | TDI | Stator→Encoder | JTAG data in (from previous device in chain) |
| 16 | GND | — | TDI/SYS_RESET_N shield |
| 17 | SYS_RESET_N | Stator→Encoder | Active-low CPLD reset (broadcast) |
| 18 | GND | — | JTAG / ENC_OUT group separator |
| 19 | ENC_OUT[0] | Encoder→Stator | Encoder output bit 0 |
| 20 | ENC_OUT[1] | Encoder→Stator | Encoder output bit 1 |
| 21 | ENC_OUT[2] | Encoder→Stator | Encoder output bit 2 |
| 22 | ENC_OUT[3] | Encoder→Stator | Encoder output bit 3 |
| 23 | ENC_OUT[4] | Encoder→Stator | Encoder output bit 4 |
| 24 | ENC_OUT[5] | Encoder→Stator | Encoder output bit 5 |
| 25 | GND | — | ENC_OUT trailing shield / power return |
| 26 | 3V3_ENIG | Stator→Encoder | Power supply |

**Power capacity:** 2 × 3V3_ENIG pins × 1A/pin = 2.0A. Encoder estimated load ~208mA (2× EPM240 CPLDs + 2× status LEDs) — >9× margin.

## Diagnostic Bank Pinout (2x8)

This diagnostic bank mirrors the Data Link connector signals for full system validation with the same odd-even ribbon orientation as the link.

```text
ROW | COL1       | COL2       | COL3       | COL4       | COL5       | COL6       | COL7       | COL8
----|------------|------------|------------|------------|------------|------------|------------|-----------
1   | 3V3_ENIG   | GND        | ENC_IN[0]  | ENC_IN[1]  | ENC_IN[2]  | ENC_IN[3]  | ENC_IN[4]  | ENC_IN[5]
2   | 3V3_ENIG   | GND        | ENC_OUT[0] | ENC_OUT[1] | ENC_OUT[2] | ENC_OUT[3] | ENC_OUT[4] | ENC_OUT[5]
```

If required, additional probe points can be added to duplicate the data link rail power and ground at a second bank to match physical test workflows.
