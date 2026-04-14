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
2   | SYS_RESET_N     | Active-low CPLD reset (from Stator U_EXP2 GPA[7] @ 0x21 — DEC-031)
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

---

## §9 Routing — Trace Width Specifications

**Board specs:** 4-layer / 2oz finished copper (JLC04161H-7628).
L1 = signal (JTAG/routing); L2 = GND plane; L3 = 3V3_ENIG power pour; L4 = secondary routing / data plate.

**IPC-2221A basis (2oz copper, external, 10°C rise, 25°C ambient):**
For 2oz external: ~0.15 mm/A. The 3V3_ENIG inner pour (L3) carries the bus current without width constraints.
See Global_Routing_Spec.md §1.1 for the full current-category table.

### Trace Width Table

| Net | Peak Current | IPC Calc (2oz ext) | Design Min | **Specified Width** | Layer | Notes |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Signal (ENC_IN/OUT, SYS_RESET_N) | < 5 mA | < 0.001 mm | 0.20 mm | **0.20 mm** | L1 | 3.3 V passive loopback logic signals |
| JTAG signals: TTD_RETURN (CI) | signal | — | 0.127 mm | **0.127 mm (5 mil)** | L1 (external) | 50 Ω controlled impedance over L2 GND plane; per DEC-016. External layer — no inner-layer minimum conflict. See `JTAG_Integrity.md`. |
| 3V3_ENIG power (J4 pin 1 → bulk caps only) | ≤ 200 mA | 0.030 mm | 0.80 mm | **0.80 mm** | L1 + L3 pour | 3V3_ENIG canonical 0.80 mm (Global_Routing_Spec §1.1); passive board — minimal local draw; J2 power pins NC |
| 3V3_ENIG distribution (inner power pour) | ≤ 200 mA | — | pour | **copper pour** | L3 | Full uninterrupted 2oz plane |
| GND return (inner GND pour) | — | — | pour | **copper pour** | L2 | Reference plane; must be solid and uninterrupted under all CI traces on L1 |

### Notes

* **JTAG CI traces:** 0.127 mm (5 mil) on L1 over the L2 GND plane achieves 50 Ω controlled
  impedance on the JLC04161H-7628 stackup (h = 0.087 mm, t = 0.035 mm, Eᵣ = 4.4). Per DEC-016.
  See `design/Electronics/Investigations/JTAG_Integrity.md §3.1`.
* **3V3_ENIG entry:** Power received at J4 pin 1 and distributed to bulk caps (C1–C5) only.
  J2 power pins are NC — no distribution to the rotor chain from this board.
  0.80 mm is the system-wide canonical minimum for all 3V3_ENIG surface traces.
