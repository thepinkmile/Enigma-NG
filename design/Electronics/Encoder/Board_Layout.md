# Encoder Board Layout Visualisations

**Status:** Draft
**Project:** Enigma-NG
**Author:** Izzyonstage & GitHub Copilot
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

> **Connector Definition Owner:** `Stator/Board_Layout.md — J4–J6`.
> The pin table below is reproduced here for layout reference. In case of conflict, the Stator definition is authoritative.

This is a 2×13 (26-pin) 2.54mm shrouded box header with polarisation key. Connects to matching
header on Stator (J4 = HID Unit, J5 = Plugboard A, J6 = Plugboard B).

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

---

## §9 Routing — Trace Width Specifications

**Board specs:** 4-layer / 2oz finished copper (JLC04161H-7628).
L1 = signal (JTAG/routing); L2 = GND plane; L3 = 3V3_ENIG power pour; L4 = secondary routing / data plate.

**IPC-2221A basis (2oz copper, external, 10°C rise, 25°C ambient):**
For 2oz external: ~0.15 mm/A. The 3V3_ENIG inner pour (L3) handles board load without width constraints.
See Global_Routing_Spec.md §1.1 for the full current-category table.

**Encoder board current budget:**
2× EPM240T100C5N CPLDs @ 50 mA each = 100 mA; 2× status LEDs @ 4 mA each = 8 mA; misc = ~100 mA;
Total worst-case: **208 mA** from the 3V3_ENIG rail supplied via J2 (Data Link) ribbon cable.

### Trace Width Table

| Net | Peak Current | IPC Calc (2oz ext) | Design Min | **Specified Width** | Layer | Notes |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Signal (ENC_IN/OUT, insertion-detect, key-press lines) | < 5 mA | < 0.001 mm | 0.20 mm | **0.20 mm** | L1 | 3.3 V logic; CPLD I/O; spade-terminal connection traces |
| JTAG signals: TCK, TMS, TDI, TDO (CI) | signal | — | 0.127 mm | **0.127 mm (5 mil)** | L1 (external) | 50 Ω controlled impedance over L2 GND plane; per DEC-016. External layer — no inner-layer minimum conflict. |
| Inter-CPLD trace: CPLD1 TDO → R7 → CPLD2 TDI | signal | — | 0.127 mm | **0.127 mm (5 mil)** | L1 (external) | Same 50 Ω CI rule intra-board; 53 Ω source impedance via R7 (33 Ω) matching the 50 Ω trace |
| 3V3_ENIG power (J2 pin 1/26 → CPLDs + LEDs) | 208 mA | 0.031 mm | 0.80 mm | **0.80 mm** | L1 + L3 pour | 3V3_ENIG canonical 0.80 mm (Global_Routing_Spec §1.1); 2× EPM240 + 2× status LED total load |
| 3V3_ENIG distribution (inner power pour) | 208 mA | — | pour | **copper pour** | L3 | Full uninterrupted 2oz plane |
| GND return (inner GND pour) | — | — | pour | **copper pour** | L2 | Reference plane; must be solid and uninterrupted under all CI traces on L1 |

### Notes

* **JTAG CI traces:** 0.127 mm (5 mil) on L1 over the L2 GND plane achieves 50 Ω controlled
  impedance on the JLC04161H-7628 stackup (h = 0.087 mm, t = 0.035 mm, Eᵣ = 4.4). Per DEC-016.
  See `design/Electronics/Investigations/JTAG_Integrity.md`.
* **Inter-CPLD trace (CPLD1 TDO → CPLD2 TDI):** R7 (33 Ω) is placed within 2 mm of CPLD1 TDO.
  The trace from R7 to CPLD2 TDI is also 0.127 mm; source impedance ≈ 53 Ω matching the 50 Ω trace.
* **Cable-output trace (CPLD2 TDO → J2 pin 13):** R8 (75 Ω) placed within 2 mm of CPLD2 TDO;
  source impedance ≈ 95 Ω targeting the ~100 Ω IDC ribbon cable impedance.
  The post-R8 trace to the J2 connector pad should be kept < 5 mm and routed at 0.20 mm.
* **3V3_ENIG power entry (J2 pins 1 + 26):** Both power pins connect to the same L3 copper pour via
  thermal vias; L1 traces from pins 1 and 26 to the via entry points at 0.50 mm minimum.
