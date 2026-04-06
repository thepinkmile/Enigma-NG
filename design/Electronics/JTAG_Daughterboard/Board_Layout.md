# JTAG Daughterboard Layout Visualisations

**Status:** Draft
**Project:** Enigma-NG
**Author:** Izzyonstage & GitHub Copilot
**Version:** v1.0.0
**Associated Hardware Revision:** Rev A
**Last Updated:** 2026-04-05

This board implements our version of an Intel (Altera) USB Blaster II device for programming CPLDs.

## Component Areas

```text
TOP VIEW (L1) - 4-Layer (DEC-017) / 2oz Copper
 _____________________________________________________________________________ 
|                                                                             |
|   [ POWER HEADER ] <--- 5-Pin INPUT Header (USB + Power)                    |
|   (One Side, 2.54mm Pitch)                                                  |
|                                                                             |
|   [ FT232H IC ] <--- High-Speed USB to MPSSE Bridge                         |
|   (Main IC for JTAG Blaster, 12MHz Crystal Attached)                        |
|                                                                             |
|   [ JTAG HEADER ] <--- 10-Pin Shrouded Header (Asymmetrical)                |
|   (Opposite Side, 2.54mm Pitch, 1:1 GND Shielding)                          |
|                                                                             |
|   [ DATA PLATE ] <--- Inverted White Silkscreen on L4 (B.Silkscreen / exterior face)   |
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

## JTAG Header Pinout (J2 — 10-Pin, Interleaved GND)

```text
PIN | SIGNAL          | DESCRIPTION
----|------------------|---------------------------------
1   | TCK             | JTAG Clock
2   | GND             | Ground
3   | TDI             | JTAG Data In
4   | GND             | Ground
5   | TDO             | JTAG Data Out
6   | GND             | Ground
7   | TMS             | JTAG Mode Select
8   | GND             | Ground
9   | VREF (3V3_ENIG) | Voltage Reference
10  | GND             | Ground
```

## INPUT Header Pinout (J1 — 5-Pin)

```text
PIN | SIGNAL          | DESCRIPTION
----|------------------|---------------------------------
1   | 5V_USB          | USB Power (5V, Controller TPS2065C rail)
2   | 3V3_ENIG        | JTAG Signal Voltage Reference (3.3V)
3   | D+              | USB 2.0 Data +
4   | D-              | USB 2.0 Data -
5   | GND             | Ground
```

## PCB Stackup — JLC04161H-7628 (4-Layer)

**Stackup:** JLC04161H-7628 (JLCPCB standard 4-layer)

| Layer | Role | Notes |
| :--- | :--- | :--- |
| L1 | GND plane + SMT component pads (component side) | Faces toward Controller Board when JDB is mounted as a hat |
| L2 | All signal traces (inner layer) | Shielded between L1 GND reference and L3 power |
| L3 | Power distribution pours (5V_USB + 3V3_ENIG) | Inner power layer |
| L4 | GND pour shield | Faces away from Controller (exterior/top when mounted) |

## Grounding Notes

GND_CHASSIS is not implemented on the JDB — see DEC-022. Mounting holes connect to GND (circuit return).
