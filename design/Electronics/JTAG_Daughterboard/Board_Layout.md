# JTAG Daughterboard Layout Visualisations

**Status:** Draft
**Version:** v1.0.0
**Associated Hardware Revision:** Rev A
**Last Updated:** 2026-04-05

This board implementsour version of an Intel (Altera) USB Blaster II device for programming CPLDs.

## Component Areas

```text
TOP VIEW (L1) - 4-Layer (DEC-017) / 2oz Copper
 _____________________________________________________________________________ 
|                                                                             |
|   [ POWER HEADER ] <--- 6-Pin Header (USB + Power)                          |
|   (One Side, 2.54mm Pitch)                                                  |
|                                                                             |
|   [ FT232H IC ] <--- High-Speed USB to MPSSE Bridge                         |
|   (Main IC for JTAG Blaster, 24MHz Crystal Attached)                        |
|                                                                             |
|   [ JTAG HEADER ] <--- 10-Pin Shrouded Header (Asymmetrical)                |
|   (Opposite Side, 2.54mm Pitch, 1:1 GND Shielding)                          |
|                                                                             |
|   [ DATA PLATE ] <--- Inverted White Silkscreen on L2                       |
|   (Enigma Silhouette + JLC Serial)                                          |
|_____________________________________________________________________________|
```

## Simplified Layout

```text
_____________________________________________________________________________ 
|                                                                             |
|   [ POWER HDR ]      [ FT232H ]      [ JTAG HDR ]                           |
|                                                                             |
|   (One Side)     (Main IC)       (Opposite Side)                            |
|                                                                             |
|_____________________________________________________________________________|
```

> **Connector Definition Owner:** This board. All other boards connecting to the JTAG Daughterboard cross-reference here.

## JTAG Header Pinout (10-Pin)

```text
PIN | SIGNAL          | DESCRIPTION
----|------------------|---------------------------------
1   | TCK             | JTAG Clock
2   | GND             | Ground
3   | TDO             | JTAG Data Out
4   | GND             | Ground
5   | TDI             | JTAG Data In
6   | GND             | Ground
7   | TMS             | JTAG Mode Select
8   | GND             | Ground
9   | RST             | Reset
10  | GND             | Ground
```

## Power Header Pinout (6-Pin)

```text
PIN | SIGNAL          | DESCRIPTION
----|------------------|---------------------------------
1   | 3V3_ENIG        | Logic Power
2   | GND             | Ground
3   | VBUS            | USB Power
4   | D-              | USB Data -
5   | D+              | USB Data +
6   | GND             | Ground
```
