# Encoder Board Layout Visualisations

**Status:** Draft
**Project:** Enigma-NG
**Author:** Izzyonstage & GitHub Copilot
**Version:** v.0.1.0
**Associated Hardware Revision:** Rev A
**Last Updated:** 2026-04-20

## 1. Component Areas

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
|   [ DATA LINK HEADER ] <--- 20-pin Header (2x10, 2.54mm Pitch)             |
|   (3V3_ENIG, ENC_DATA[5:0], JTAG, GND, 3V3_ENIG)                           |
|                                                                            |
|   [ DATA PLATE ] <--- Inverted White Silkscreen on L4                      |
|____________________________________________________________________________|
```

## 2. Simplified Layout

```text
_____________________________________________________________________________
|                                                                            |
|   [ 64-LINE BANK ]      [ CPLD ]      [ DATA LINK ]                        |
|                                                                            |
|   (Generic I/O field)     (U1)      (20-pin ribbon bus)                    |
|____________________________________________________________________________|
```

## 3. Data Link Pinout (20-Pin Connector)

> **Connector Definition Owner:** `Stator/Board_Layout.md — J4/J5/J6/J7/J8/J9`.
> The pin table below is reproduced here for layout reference. In case of conflict, the Stator
> definition is authoritative.

This is a 2×10 (20-pin) 2.54 mm shrouded box header with polarisation key. It connects to one of
the six matching headers on the Stator.

| Pin | Signal | Direction | Notes |
| :--- | :--- | :--- | :--- |
| 1 | 3V3_ENIG | Stator->Encoder | Power supply |
| 2 | ENC_DATA[0] | Role-dependent | Generic 6-bit service bus |
| 3 | ENC_DATA[1] | Role-dependent | Generic 6-bit service bus |
| 4 | ENC_DATA[2] | Role-dependent | Generic 6-bit service bus |
| 5 | ENC_DATA[3] | Role-dependent | Generic 6-bit service bus |
| 6 | ENC_DATA[4] | Role-dependent | Generic 6-bit service bus |
| 7 | ENC_DATA[5] | Role-dependent | Generic 6-bit service bus |
| 8 | GND | — | ENC_DATA / JTAG group separator |
| 9 | TCK | Stator->Encoder | JTAG clock |
| 10 | GND | — | TCK/TMS inter-pin shield |
| 11 | TMS | Stator->Encoder | JTAG mode select |
| 12 | GND | — | TMS/TDO inter-pin shield |
| 13 | TDO | Encoder->Stator | JTAG data out |
| 14 | GND | — | TDO/TDI inter-pin shield |
| 15 | TDI | Stator->Encoder | JTAG data in |
| 16 | GND | — | TDI/SYS_RESET_N shield |
| 17 | SYS_RESET_N | Stator->Encoder | Active-low CPLD reset |
| 18 | GND | — | JTAG trailing shield / power return |
| 19 | GND | — | Power return |
| 20 | 3V3_ENIG | Stator->Encoder | Power supply |

**Power capacity:** 2 × 3V3_ENIG pins × 1 A/pin = 2.0 A. One Encoder Module estimated load ~104 mA
(1× EPM240 CPLD + 1× status LED + local margin) — substantial connector margin.

---

## 4. U1 — Encoder CPLD Signal Map (Logical Pin Budget)

> This is the board-authoritative **logical** signal map for U1. The local MAX II handbook confirms
> `EPM240T100` package availability in TQFP-100, but it points printed device pin-outs to external
> package documentation rather than embedding a fixed package pin table. The map below therefore
> freezes the required board-level connectivity while leaving the exact TQFP pad numbers to schematic
> capture.

### 4.1 Dedicated device pins

| Function | Source / destination | Notes |
| :--- | :--- | :--- |
| `TCK` | J2 pin 9 -> U1 | Dedicated JTAG clock input |
| `TMS` | J2 pin 11 -> U1 | Dedicated JTAG mode input |
| `TDI` | J2 pin 15 -> U1 | Dedicated JTAG serial input from the Stator-managed chain |
| `TDO` | U1 -> R6 -> J2 pin 13 | Dedicated JTAG serial output back to the Stator-managed chain |
| `DEV_CLRN` / reset input | J2 pin 17 (`SYS_RESET_N`) -> U1 | Active-low device reset; held high locally by R5 |

### 4.2 General-purpose signal groups

| Signal group | Pins | U1 direction | Notes |
| :--- | :---: | :--- | :--- |
| `BT1`-`BT64` 64-line bank | 64 | Role-dependent | Encode-role population reads one asserted line; decode-role population drives one-of-64 output |
| `ENC_DATA[5:0]` | 6 | Role-dependent | Encode role drives the 6-bit service bus back to the Stator; decode role consumes it |
| `D1` status LED | 1 | Output | Active-low debug LED: U1 drives LOW to illuminate |

**Logical budget summary:** 71 general-purpose signal connections total = **64 bank lines + 6 bus
lines + 1 LED**, plus the dedicated JTAG / reset pins above.

**Spare-pin policy:** the active docs do not currently claim any spare U1 user I/O.

---

## 5. Routing — Trace Width Specifications

**Board specs:** 4-layer / 2oz finished copper (JLC04161H-7628).  
L1 = signal (JTAG/routing); L2 = GND plane; L3 = 3V3_ENIG power pour; L4 = secondary routing /
data plate.

**IPC-2221A basis (2oz copper, external, 10°C rise, 25°C ambient):**  
For 2oz external: ~0.15 mm/A. The 3V3_ENIG inner pour (L3) handles board load without width
constraints. See `Global_Routing_Spec.md §1.1` for the full current-category table.

**Encoder board current budget:**  
1× EPM240T100I5N CPLD @ 50 mA; 1× status LED @ 4 mA; misc = ~50 mA; total worst-case:
**104 mA** from the 3V3_ENIG rail supplied via J2.

### 5.1 Trace Width Table

| Net | Peak Current | IPC Calc (2oz ext) | Design Min | **Specified Width** | Layer | Notes |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Signal (`ENC_DATA`, key lines, lamp lines, jack lines) | < 5 mA | < 0.001 mm | 0.20 mm | **0.20 mm** | L1 | 3.3 V logic; CPLD I/O; spade-terminal traces |
| JTAG signals: TCK, TMS, TDI, TDO (CI) | signal | — | 0.127 mm | **0.127 mm (5 mil)** | L1 (external) | 50 Ω controlled impedance over L2 GND plane; per DEC-016 |
| 3V3_ENIG power (J2 pin 1/20 -> CPLD + LED) | 104 mA | 0.016 mm | 0.80 mm | **0.80 mm** | L1 + L3 pour | Canonical 3V3_ENIG width |
| 3V3_ENIG distribution (inner power pour) | 104 mA | — | pour | **copper pour** | L3 | Full uninterrupted 2oz plane |
| GND return (inner GND pour) | — | — | pour | **copper pour** | L2 | Reference plane under all CI traces on L1 |

### 5.2 Notes

* **JTAG CI traces:** 0.127 mm (5 mil) on L1 over the L2 GND plane achieves 50 Ω controlled
  impedance on the JLC04161H-7628 stackup (h = 0.087 mm, t = 0.035 mm, E_r = 4.4). Per DEC-016.
* **Cable-output trace (U1 TDO -> R6 -> J2 pin 13):** R6 (75 Ω) is placed within 2 mm of U1 TDO;
  the post-R6 trace to the J2 connector pad should be kept short.
* **3V3_ENIG power entry (J2 pins 1 and 20):** both power pins connect to the same L3 copper pour
  via thermal vias; L1 traces from pins 1 and 20 to the via entry points at 0.50 mm minimum.
