# Reflector Board Layout Visualisations

**Status:** Draft
**Project:** Enigma-NG
**Author:** Izzyonstage & GitHub Copilot
**Version:** v1.0.0
**Associated Hardware Revision:** Rev A
**Last Updated:** 2026-04-05

## Component Areas

```text
TOP VIEW (L1) - 4-Layer / 2oz Copper
 _____________________________________________________________________________ 
|                                                                             |
|   [ 16-PIN INTERCONNECT HEADER ] <--- Vertical Shrouded Box Header          |
|   (2x8, 2.54mm Pitch)                                                       |
|                                                                             |
|   [ J1–J3: ERM8 CONNECTORS ] <--- ERM8-005 (×2) + ERM8-010 (×1), male headers                 |
|   (Matching Rotor Pitch)                                                    |
|                                                                             |
|   [ DIAGNOSTIC BANK ] <--- 2x8 ENIG Gold Probe Bank                         |
|   (2.54mm Pitch, L1)                                                        |
|                                                                             |
|   [ DATA PLATE ] <--- Inverted White Silkscreen on L4                       |
|   (Enigma Silhouette + JLC Serial)                                          |
|                                                                             |
|   [ FILLETED CORNERS ] <--- 2.0mm Rounded PCB Edges                         |
|_____________________________________________________________________________|
```

## Simplified Layout

```text
_____________________________________________________________________________ 
|                                                                            |
|   [ INTERCONNECT ]      [ CONTACTS ]      [ DIAGNOSTIC BANK ]              |
|                                                                            |
|   (JTAG Termination)   (Signal Loopback) (Monitoring)                      |
|                                                                            |
|   [ DATA PLATE ]                                                           |
|____________________________________________________________________________|
```

## Interconnect Pinout (16-Pin Header)

This 16-pin (2x8) ribbon-style connector follows odd/even row orientation (odd pins on row 1, even pins on row 2), consistent with the Encoder Data Link pinout format.

```text
PIN | SIGNAL          | DESCRIPTION
----|-----------------|---------------------------------
1   | 3V3_ENIG        | Power Supply
2   | SYS_RESET_N     | Active-low CPLD reset (from Controller GPIO 26 via Stator Extension Port)
3   | ENC_IN[0]       | Encryption Input Bit 0
4   | ENC_IN[1]       | Encryption Input Bit 1
5   | ENC_IN[2]       | Encryption Input Bit 2
6   | ENC_IN[3]       | Encryption Input Bit 3
7   | ENC_IN[4]       | Encryption Input Bit 4
8   | ENC_IN[5]       | Encryption Input Bit 5
9   | ENC_OUT[0]      | Encryption Output Bit 0
10  | ENC_OUT[1]      | Encryption Output Bit 1
11  | ENC_OUT[2]      | Encryption Output Bit 2
12  | ENC_OUT[3]      | Encryption Output Bit 3
13  | ENC_OUT[4]      | Encryption Output Bit 4
14  | ENC_OUT[5]      | Encryption Output Bit 5
15  | TTD_RETURN      | JTAG Data Out Return
16  | GND             | Ground (TDO Shield)
```

## Diagnostic Bank Pinout (2x8)

```text
ROW | COL1 | COL2 | COL3 | COL4 | COL5 | COL6 | COL7 | COL8
----|------|------|------|------|------|------|------|------
1   | ENC_IN[0] | ENC_IN[1] | ENC_IN[2] | ENC_IN[3] | ENC_IN[4] | ENC_IN[5] | GND | TTD_RETURN
2   | ENC_OUT[0]| ENC_OUT[1]| ENC_OUT[2]| ENC_OUT[3]| ENC_OUT[4]| ENC_OUT[5]| 3V3_ENIG | GND
```
