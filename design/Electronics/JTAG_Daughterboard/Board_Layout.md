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

---

## §9 Routing — Trace Width Specifications

**Board specs:** 4-layer / 2oz finished copper (JLC04161H-7628).
L1 = GND plane (component side); L2 = all signal traces (inner layer); L3 = power pours; L4 = GND pour.

**IPC-2221A basis (2oz copper, 10°C rise, 25°C ambient):**
External: ~0.15 mm/A. Internal: multiply by 2.5× for same thermal rise.
See Global_Routing_Spec.md §1.1 for the full current-category table.

### Trace Width Table

| Net | Peak Current | IPC Calc (2oz) | Design Min | **Specified Width** | Layer | Notes |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 5V_USB (J1 pin 1 → FT232H VCC) | 400 mA | 0.06 mm | 0.50 mm | **0.50 mm** | L1 + L3 pour | FT232H absolute max VCC draw; power-rail minimum applies |
| 3V3_ENIG (J1 pin 2 → FT232H VCCIO) | 15 mA | 0.002 mm | 0.50 mm | **0.50 mm** | L1 + L3 pour | VCCIO domain; power-rail minimum applies |
| JTAG signals: TCK, TMS, TDI, TDO (CI) | signal | — | 0.127 mm | **0.127 mm (5 mil)** | L2 (inner) | 50 Ω controlled impedance over L1 GND reference plane; per DEC-016. **CI exception** — overrides 10 mil inner-layer minimum in Global_Routing_Spec §1. |
| USB D+ / D− differential pair | signal | — | 0.15 mm | **0.15 mm (6 mil)** | L2 (inner) | 90 Ω differential USB 2.0; must be length-matched to within 0.1 mm; routed as a tightly-coupled pair |
| GND pours (outer layers) | — | — | pour | **copper pour** | L1 + L4 | Both outer layers = solid GND; provides dual-sided shielding for L2 signals |
| Power pours (inner power layer) | ≤ 400 mA | — | pour | **copper pour** | L3 | Separate pour zones for 5V_USB and 3V3_ENIG |

### Notes

* All JTAG traces on L2 are sandwiched between the L1 GND reference (top) and L3 power pour (bottom),
  providing inherent shielding and a well-defined impedance environment.
* The 0.127 mm JTAG trace width is calculated for the JLC04161H-7628 stackup
  (h = 0.087 mm dielectric, t = 0.035 mm copper, Eᵣ = 4.4) targeting 50 Ω per DEC-016.
  See `design/Electronics/Investigations/JTAG_Integrity.md §3.1`.
* USB D+/D− traces at 0.15 mm over the L1 GND plane yield approximately 90 Ω differential
  on the JLC04161H-7628 inner signal layer — correct for USB 2.0 Full Speed.
