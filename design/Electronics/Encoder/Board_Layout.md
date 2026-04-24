# Encoder Board Layout Visualisations

**Status:** Draft
**Project:** Enigma-NG
**Author:** Izzyonstage & GitHub Copilot
**Version:** v1.1.0
**Associated Hardware Revision:** Rev A
**Last Updated:** 2026-04-20

## Component Areas

```text
TOP VIEW (L1) - 4-Layer / 2oz Copper
 ____________________________________________________________________________
|                                                                            |
|   [ 64-LINE SPADE TERMINAL BANK ]  <--- External I/O Interface             |
|   (single generic bank used as either inputs or outputs)                   |
|                                                                            |
|   [ SINGLE CPLD + OPTIONAL RC INPUT NETWORK ]                              |
|   (EPM240T100I5N + encode-role pull-up/RC population area)                 |
|                                                                            |
|   [ DATA LINK HEADER ] <--- 26-pin Header (2x13, 2.54mm Pitch)             |
|   (3V3_ENIG, ENC_IN[0:5], JTAG, ENC_OUT[0:5], 3V3_ENIG)                    |
|                                                                            |
|   [ DIAGNOSTIC BANK ] <--- 2x8 ENIG Gold Probe Bank                        |
|                                                                            |
|   [ DATA PLATE ] <--- Inverted White Silkscreen on L4                      |
|____________________________________________________________________________|
```

## Simplified Layout

```text
_____________________________________________________________________________
|                                                                            |
|   [ 64-LINE BANK ]      [ CPLD ]      [ DATA LINK ]                        |
|                                                                            |
|   (Generic I/O field)     (U1)      (26-pin ribbon bus)                    |
|                                                                            |
|   [ DIAGNOSTIC BANK ]                                                      |
|____________________________________________________________________________|
```

## Data Link Pinout (26-Pin Connector)
>
> **Connector Definition Owner:** `Stator/Board_Layout.md — J4/J5/J6/J7/J8/J9`.
> The pin table below is reproduced here for layout reference. In case of conflict, the Stator
> definition is authoritative.

This is a 2×13 (26-pin) 2.54 mm shrouded box header with polarisation key. It connects to one of
the six matching headers on the Stator.

| Pin | Signal | Direction | Notes |
| :--- | :--- | :--- | :--- |
| 1 | 3V3_ENIG | Stator->Encoder | Power supply |
| 2 | ENC_IN[0] | Stator->Encoder | Decode-role input bit 0 |
| 3 | ENC_IN[1] | Stator->Encoder | Decode-role input bit 1 |
| 4 | ENC_IN[2] | Stator->Encoder | Decode-role input bit 2 |
| 5 | ENC_IN[3] | Stator->Encoder | Decode-role input bit 3 |
| 6 | ENC_IN[4] | Stator->Encoder | Decode-role input bit 4 |
| 7 | ENC_IN[5] | Stator->Encoder | Decode-role input bit 5 |
| 8 | GND | — | ENC_IN / JTAG group separator |
| 9 | TCK | Stator->Encoder | JTAG clock |
| 10 | GND | — | TCK/TMS inter-pin shield |
| 11 | TMS | Stator->Encoder | JTAG mode select |
| 12 | GND | — | TMS/TDO inter-pin shield |
| 13 | TDO | Encoder->Stator | JTAG data out |
| 14 | GND | — | TDO/TDI inter-pin shield |
| 15 | TDI | Stator->Encoder | JTAG data in |
| 16 | GND | — | TDI/SYS_RESET_N shield |
| 17 | SYS_RESET_N | Stator->Encoder | Active-low CPLD reset |
| 18 | GND | — | JTAG / ENC_OUT group separator |
| 19 | ENC_OUT[0] | Encoder->Stator | Encode-role output bit 0 |
| 20 | ENC_OUT[1] | Encoder->Stator | Encode-role output bit 1 |
| 21 | ENC_OUT[2] | Encoder->Stator | Encode-role output bit 2 |
| 22 | ENC_OUT[3] | Encoder->Stator | Encode-role output bit 3 |
| 23 | ENC_OUT[4] | Encoder->Stator | Encode-role output bit 4 |
| 24 | ENC_OUT[5] | Encoder->Stator | Encode-role output bit 5 |
| 25 | GND | — | ENC_OUT trailing shield / power return |
| 26 | 3V3_ENIG | Stator->Encoder | Power supply |

**Power capacity:** 2 × 3V3_ENIG pins × 1 A/pin = 2.0 A. One Encoder Module estimated load ~104 mA
(1× EPM240 CPLD + 1× status LED + local margin) — substantial connector margin.

## Diagnostic Bank Pinout (2x8)

This diagnostic bank mirrors the Data Link connector signals for system validation.

```text
ROW | COL1       | COL2       | COL3       | COL4       | COL5       | COL6       | COL7       | COL8
----|------------|------------|------------|------------|------------|------------|------------|-----------
1   | 3V3_ENIG   | GND        | ENC_IN[0]  | ENC_IN[1]  | ENC_IN[2]  | ENC_IN[3]  | ENC_IN[4]  | ENC_IN[5]
2   | 3V3_ENIG   | GND        | ENC_OUT[0] | ENC_OUT[1] | ENC_OUT[2] | ENC_OUT[3] | ENC_OUT[4] | ENC_OUT[5]
```

---

## §9 Routing — Trace Width Specifications

**Board specs:** 4-layer / 2oz finished copper (JLC04161H-7628).  
L1 = signal (JTAG/routing); L2 = GND plane; L3 = 3V3_ENIG power pour; L4 = secondary routing /
data plate.

**IPC-2221A basis (2oz copper, external, 10°C rise, 25°C ambient):**  
For 2oz external: ~0.15 mm/A. The 3V3_ENIG inner pour (L3) handles board load without width
constraints. See `Global_Routing_Spec.md §1.1` for the full current-category table.

**Encoder board current budget:**  
1× EPM240T100I5N CPLD @ 50 mA; 1× status LED @ 4 mA; misc = ~50 mA; total worst-case:
**104 mA** from the 3V3_ENIG rail supplied via J2.

### Trace Width Table

| Net | Peak Current | IPC Calc (2oz ext) | Design Min | **Specified Width** | Layer | Notes |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Signal (ENC_IN/OUT, key lines, lamp lines, jack lines) | < 5 mA | < 0.001 mm | 0.20 mm | **0.20 mm** | L1 | 3.3 V logic; CPLD I/O; spade-terminal traces |
| JTAG signals: TCK, TMS, TDI, TDO (CI) | signal | — | 0.127 mm | **0.127 mm (5 mil)** | L1 (external) | 50 Ω controlled impedance over L2 GND plane; per DEC-016 |
| 3V3_ENIG power (J2 pin 1/26 -> CPLD + LED) | 104 mA | 0.016 mm | 0.80 mm | **0.80 mm** | L1 + L3 pour | Canonical 3V3_ENIG width |
| 3V3_ENIG distribution (inner power pour) | 104 mA | — | pour | **copper pour** | L3 | Full uninterrupted 2oz plane |
| GND return (inner GND pour) | — | — | pour | **copper pour** | L2 | Reference plane under all CI traces on L1 |

### Notes

* **JTAG CI traces:** 0.127 mm (5 mil) on L1 over the L2 GND plane achieves 50 Ω controlled
  impedance on the JLC04161H-7628 stackup (h = 0.087 mm, t = 0.035 mm, E_r = 4.4). Per DEC-016.
* **Cable-output trace (U1 TDO -> R6 -> J2 pin 13):** R6 (75 Ω) is placed within 2 mm of U1 TDO;
  the post-R6 trace to the J2 connector pad should be kept short.
* **3V3_ENIG power entry (J2 pins 1 and 26):** both power pins connect to the same L3 copper pour
  via thermal vias; L1 traces from pins 1 and 26 to the via entry points at 0.50 mm minimum.
