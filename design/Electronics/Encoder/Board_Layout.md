# Encoder Board Layout Visualisations

## Component Areas

```text
TOP VIEW (L1) - 4-Layer / 1oz Copper
 ____________________________________________________________________________ 
|                                                                            |
|   [ SPADE TERMINAL BANK ] <--- External I/O Interface (Mechanical board)   |
|   (2x8 or 2x10 block for encoder rows, crossover wires)                    |
|                                                                            |
|   [ CPLD ARRAY ] <--- Intel MAX II EPM240T100C5N                           |
|   (Dual Logic Units for I/O Management)                                    |
|                                                                            |
|   [ DATA LINK HEADER ] <--- 16-pin Header (2x8, 2.54mm Pitch)              |
|   (2x 3V3_ENIG, 2x GND, ENC_IN[0:5], ENC_OUT[0:5])                         |
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
|   (64x Inputs/Outputs)       (Logic Core)   (16-Pin Ribbon Bus)            |
|                                                                            |
|   [ DIAGNOSTIC BANK ]                                                      |
|____________________________________________________________________________|
```

## Data Link Pinout (16-Pin Connector)

This is a ribbon-style footprint in the style of KiCad where odd pins are in row 1 and even pins are in row 2, moving left-to-right across the connector columns.

```text
PIN | SIGNAL     | DESCRIPTION | PHYSICAL POSITION (2x8 IDC cable)
----|------------|-------------|----------------------------------
1   | 3V3_ENIG   | Power       | Row 1, Col 1
2   | 3V3_ENIG   | Power       | Row 2, Col 1
3   | GND        | Ground      | Row 1, Col 2
4   | SYS_RESET_N | CPLD Reset  | Row 2, Col 2
5   | ENC_IN[0]  | Encrypt in  | Row 1, Col 3
6   | ENC_OUT[0] | Encrypt out | Row 2, Col 3
7   | ENC_IN[1]  | Encrypt in  | Row 1, Col 4
8   | ENC_OUT[1] | Encrypt out | Row 2, Col 4
9   | ENC_IN[2]  | Encrypt in  | Row 1, Col 5
10  | ENC_OUT[2] | Encrypt out | Row 2, Col 5
11  | ENC_IN[3]  | Encrypt in  | Row 1, Col 6
12  | ENC_OUT[3] | Encrypt out | Row 2, Col 6
13  | ENC_IN[4]  | Encrypt in  | Row 1, Col 7
14  | ENC_OUT[4] | Encrypt out | Row 2, Col 7
15  | ENC_IN[5]  | Encrypt in  | Row 1, Col 8
16  | ENC_OUT[5] | Encrypt out | Row 2, Col 8
```

## Diagnostic Bank Pinout (2x8)

This diagnostic bank mirrors the Data Link connector signals for full system validation with the same odd-even ribbon orientation as the link.

```text
ROW | COL1       | COL2       | COL3       | COL4       | COL5       | COL6       | COL7       | COL8
----|------------|------------|------------|------------|------------|------------|------------|-----------
1   | 3V3_ENIG   | GND        | ENC_IN[0]  | ENC_IN[1]  | ENC_IN[2]  | ENC_IN[3]  | ENC_IN[4]  | ENC_IN[5]
2   | 3V3_ENIG   | GND        | ENC_OUT[0] | ENC_OUT[1] | ENC_OUT[2] | ENC_OUT[3] | ENC_OUT[4] | ENC_OUT[5]
```

If required, additional probe points can be added to duplicate the data link rail power and ground at a second bank to match physical test workflows.
