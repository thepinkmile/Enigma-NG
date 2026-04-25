# Reflector Board Layout Visualisations

**Status:** Draft
**Project:** Enigma-NG
**Author:** Izzyonstage & GitHub Copilot
**Version:** v1.0.0
**Associated Hardware Revision:** Rev A
**Last Updated:** 2026-04-05

## 1. Component Areas

```text
TOP VIEW (L1) - 4-Layer / 2oz Copper
 ________________________________________________________________________________ 
|                                                                                |
|   [ 16-PIN INTERCONNECT HEADER ] <--- Vertical Shrouded Box Header             |
|   (2x8, 2.54mm Pitch)                                                          |
|                                                                                |
|   [ J1–J3: ERM8 CONNECTORS ] <--- ERM8-005 (×2) + ERM8-010 (×1), male headers  |
|   (Matching Rotor Pitch)                                                       |
|                                                                                |
|   [ DATA PLATE ] <--- Inverted White Silkscreen on L4                          |
|   (Enigma Silhouette + JLC Serial)                                             |
|                                                                                |
|   [ FILLETED CORNERS ] <--- 2.0mm Rounded PCB Edges                            |
|________________________________________________________________________________|
```

## 2. Simplified Layout

```text
 _____________________________________________ 
|                                             |
|   [ INTERCONNECT ]      [ CONTACTS ]        |
|                                             |
|   (JTAG Termination)   (Signal Loopback)    |
|                                             |
|   [ DATA PLATE ]                            |
|_____________________________________________|
```

## 3. Interconnect Pinout (16-Pin Header)

This 16-pin (2x8) ribbon-style connector follows odd/even row orientation (odd pins on row 1, even pins on row 2), consistent with the Encoder Data Link pinout format.

```text
PIN | SIGNAL          | DESCRIPTION
----|-----------------|---------------------------------
1   | 3V3_ENIG        | Power Supply
2   | SYS_RESET_N     | Active-low CPLD reset (broadcast from Stator)
3   | ENC_OUT_REF[0]  | Stator-owned outbound reflector-boundary bit 0
4   | ENC_OUT_REF[1]  | Stator-owned outbound reflector-boundary bit 1
5   | ENC_OUT_REF[2]  | Stator-owned outbound reflector-boundary bit 2
6   | ENC_OUT_REF[3]  | Stator-owned outbound reflector-boundary bit 3
7   | ENC_OUT_REF[4]  | Stator-owned outbound reflector-boundary bit 4
8   | ENC_OUT_REF[5]  | Stator-owned outbound reflector-boundary bit 5
9   | ENC_IN_REF[0]   | Stator-owned inbound reflector-boundary bit 0
10  | ENC_IN_REF[1]   | Stator-owned inbound reflector-boundary bit 1
11  | ENC_IN_REF[2]   | Stator-owned inbound reflector-boundary bit 2
12  | ENC_IN_REF[3]   | Stator-owned inbound reflector-boundary bit 3
13  | ENC_IN_REF[4]   | Stator-owned inbound reflector-boundary bit 4
14  | ENC_IN_REF[5]   | Stator-owned inbound reflector-boundary bit 5
15  | TTD_RETURN      | JTAG Data Out Return
16  | GND             | Ground (TDO Shield)
```

---

## 4. Routing — Trace Width Specifications

**Board specs:** 4-layer / 2oz finished copper (JLC04161H-7628).
L1 = signal (JTAG/routing); L2 = GND plane; L3 = 3V3_ENIG power pour; L4 = secondary routing / data plate.

**IPC-2221A basis (2oz copper, external, 10°C rise, 25°C ambient):**
For 2oz external: ~0.15 mm/A. The 3V3_ENIG inner pour (L3) carries the bus current without width constraints.
See Global_Routing_Spec.md §1.1 for the full current-category table.

### 4.1 Trace Width Table

| Net | Peak Current | IPC Calc (2oz ext) | Design Min | **Specified Width** | Layer | Notes |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Signal (`ENC_OUT_REF`/`ENC_IN_REF`, `SYS_RESET_N`) | < 5 mA | < 0.001 mm | 0.20 mm | **0.20 mm** | L1 | 3.3 V passive loopback logic signals |
| JTAG signals: TTD_RETURN (CI) | signal | — | 0.127 mm | **0.127 mm (5 mil)** | L1 (external) | 50 Ω controlled impedance over L2 GND plane; per DEC-016. External layer — no inner-layer minimum conflict. See `JTAG_Integrity.md`. |
| 3V3_ENIG power (J4 pin 1 → bulk caps only) | ≤ 200 mA | 0.030 mm | 0.80 mm | **0.80 mm** | L1 + L3 pour | 3V3_ENIG canonical 0.80 mm (Global_Routing_Spec §1.1); passive board — minimal local draw; J2 power pins NC |
| 3V3_ENIG distribution (inner power pour) | ≤ 200 mA | — | pour | **copper pour** | L3 | Full uninterrupted 2oz plane |
| GND return (inner GND pour) | — | — | pour | **copper pour** | L2 | Reference plane; must be solid and uninterrupted under all CI traces on L1 |

### 4.2 Notes

* **JTAG CI traces:** 0.127 mm (5 mil) on L1 over the L2 GND plane achieves 50 Ω controlled
  impedance on the JLC04161H-7628 stackup (h = 0.087 mm, t = 0.035 mm, Eᵣ = 4.4). Per DEC-016.
  See `design/Electronics/Investigations/JTAG_Integrity.md §3.1`.
* **3V3_ENIG entry:** Power received at J4 pin 1 and distributed to bulk caps (C1–C5) only.
  J2 power pins are NC — no distribution to the rotor chain from this board.
  0.80 mm is the system-wide canonical minimum for all 3V3_ENIG surface traces.
