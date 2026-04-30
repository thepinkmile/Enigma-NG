# Extension Board Layout Visualisations

**Status:** Draft
**Project:** Enigma-NG
**Author:** Izzyonstage & GitHub Copilot
**Version:** v.0.1.0
**Associated Hardware Revision:** Rev A
**Last Updated:** 2026-04-26

---

## 1. Component Areas

```text
TOP VIEW (L1) - 4-Layer / 2oz Copper / ENIG
 _____________________________________________________________________________
|                                                                             |
|   [ J7: EXTENSION PORT IN ] <--- 20-pin 2×10 shrouded, from previous stage  |
|                                                                             |
|   [ BULK DECOUPLING ] <--- 5x 10uF X7R star/spoke near J7                   |
|                                                                             |
|   [ ROTOR INTERFACE CONNECTORS ]                                            |
|   (J1-J3: input side ERM8 male; J4-J6: output side ERF8 female)             |
|                                                                             |
|   [ JTAG BUFFER (U1) ] <--- SN74LVC2G125DCUR, TCK+TMS re-drive for output   |
|   [ J9 / J10: AM HOST DOCKS ] <--- Power + Trigger sockets for shared AM    |
|                                                                             |
|   [ J8: EXTENSION PORT OUT ] <--- 20-pin 2×10 shrouded, to next stage       |
|                                                                             |
|   [ DATA PLATE ] <--- Inverted White Silkscreen on L4                       |
|_____________________________________________________________________________|
```

---

## 2. J7 — Extension Port IN (20-Pin 2×10)
>
> **Connector Definition Owner:** `Stator/Board_Layout.md — J10`.
> This board uses the mating connector on J7. See BOM for part number.
> Authoritative pinout: pins 1-16 preserve the existing reflector-boundary service bus; pins 17-20 add
> `5V_MAIN`, `GND`, `5V_MAIN`, `GND` for local actuation power.

---

## 3. J8 — Extension Port OUT (20-Pin 2×10)
>
> **Connector Definition Owner:** `Stator/Board_Layout.md — J10`.
> This board uses the mating connector on J8. Carries the same signals as J7, passed through.
> See BOM for part number.

---

## 4. J1–J6 — Rotor Interface Connectors (ERM8/ERF8 Family, 0.8mm Pitch)
>
> **Connector Definition Owner:** `Rotor/Design_Spec.md §3.4`.
> J1–J3 are ERM8 male headers (input side — plug into previous rotor group's last rotor J4–J6 ERF8 outputs).
> J4–J6 are ERF8 female sockets (output side — receive next rotor group's first rotor J1–J3 ERM8 male headers).

| Ref | Side | Signal Group | Type | JLCPCB PN |
| --- | ---- | ------------ | ---- | --------- |
| J1 | Input (plugs into previous group last rotor J4) | JTAG | ERM8-005-05.0-S-DV-K-TR (10-pin, **male**) | C3649741 |
| J2 | Input (plugs into previous group last rotor J5) | Power | ERM8-005-05.0-S-DV-K-TR (10-pin, **male**) | C3649741 |
| J3 | Input (plugs into previous group last rotor J6) | ENC Data | ERM8-010-05.0-S-DV-K-TR (20-pin, **male**) | C374877 |
| J4 | Output (receives next group first rotor J1) | JTAG | ERF8-005-05.0-S-DV-K-TR (10-pin, female) | C7273978 |
| J5 | Output (receives next group first rotor J2) | Power | ERF8-005-05.0-S-DV-K-TR (10-pin, female) | C7273978 |
| J6 | Output (receives next group first rotor J3) | ENC Data | ERF8-010-05.0-S-DV-K-TR (20-pin, female) | C3646170 |

**Important:** ERM8/ERF8 0.8mm pitch — physically incompatible with any 2.54mm connector.
Mark clearly on silkscreen: `ERM8/ERF8 / 0.8mm / NICHT 2.54mm`.

---

## 5. J9 / J10 — Actuation Module Host Docks

* **J9:** AM power dock host socket (ERF8-005) - routes `5V_MAIN`, `3V3_ENIG`, and grouped returns
  from the Extension Port power entry.
* **J10:** AM trigger dock host socket (ERF8-005) - routes the local active-low `ACTUATE_REQUEST`
  source into the AM.
* The mounted AM footprint on the Extension shall be kept as a **no-component placement zone** except
  for J9 / J10 and the routing / copper needed to reach them. This preserves the inverted module's
  clearance and keeps its manual-fit loom / service headers accessible after installation.

## 6. Routing — Trace Width Specifications

**Board specs:** 4-layer / 2oz finished copper (JLC04161H-7628).
L1 = signal (JTAG/routing); L2 = GND plane; L3 = 3V3_ENIG power pour; L4 = secondary routing / data plate.

**IPC-2221A basis (2oz copper, external, 10°C rise, 25°C ambient):**
For 2oz external: ~0.15 mm/A. The 3V3_ENIG inner pour (L3) carries the bus current without width constraints.
See Global_Routing_Spec.md §1.1 for the full current-category table.

**Extension board power pass-through analysis:**
The Extension board passes `3V3_ENIG` from its J7 input to the next rotor group (up to 5 rotors ×
55 mA = 275 mA local group draw plus remaining upstream groups), and now also receives a grouped
`5V_MAIN` feed for the local Actuation Module.
Worst-case: first Extension board (Rotor group 2) passes power for Rotors 6–30 = 25 rotors × 55 mA = 1.38 A through its J5 output.
All Extension boards share an identical PCB layout; traces must be sized for the worst case — the first Extension board in the stack.

### 5.1 Trace Width Table

| Net | Peak Current | IPC Calc (2oz ext) | Design Min | **Specified Width** | Layer | Notes |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Signal (ENC_IN/OUT, SYS_RESET_N, ACTUATE_REQUEST) | < 5 mA | < 0.001 mm | 0.20 mm | **0.20 mm** | L1 | 3.3 V logic signals; pass-through from J7 to J8 and local AM trigger routing |
| JTAG signals: TTD_RETURN (CI) | signal | — | 0.127 mm | **0.127 mm (5 mil)** | L1 (external) | 50 Ω controlled impedance over L2 GND plane; per DEC-016. External layer — no inner-layer minimum conflict. See `JTAG_Integrity.md`. |
| 3V3_ENIG entry / pass-through trunk (J7 → J5 output bus) | 1.43 A (worst case) | 0.21 mm | 0.80 mm | **0.80 mm** | L1 + L3 pour | 3V3_ENIG canonical 0.80 mm (Global_Routing_Spec §1.1); worst-case Extension 1 pass-through |
| 3V3_ENIG local draw (J7 → U1 VCC) | ≤ 10 mA | 0.002 mm | 0.80 mm | **0.80 mm** | L1 | Buffer IC supply; 3V3_ENIG canonical 0.80 mm minimum |
| 3V3_ENIG distribution (inner power pour) | 1.43 A | — | pour | **copper pour** | L3 | Full uninterrupted 2oz plane; primary distribution |
| 5V_MAIN to AM host dock (J7 → J9) | 0.50 A | 0.08 mm | 0.80 mm | **0.80 mm** | L1 | Local Extension actuation supply path |
| GND return (inner GND pour) | — | — | pour | **copper pour** | L2 | Reference plane; must be solid and uninterrupted under all CI traces on L1 |

### 5.2 Notes

* **JTAG CI traces:** 0.127 mm (5 mil) on L1 over the L2 GND plane achieves 50 Ω controlled
  impedance on the JLC04161H-7628 stackup (h = 0.087 mm, t = 0.035 mm, Eᵣ = 4.4). Per DEC-016.
  See `design/Electronics/Investigations/JTAG_Integrity.md §3.1`.
* **3V3_ENIG pass-through:** The 0.80 mm is the canonical system-wide minimum for all 3V3_ENIG
  surface traces (Global_Routing_Spec §1.1). IPC calculation for worst-case 1.43 A at 2oz external:
  1.43 × 0.15 mm = 0.21 mm → **0.80 mm** canonical width provides 6.8× margin above IPC minimum.

---

## 7. Thermal & ESD

> **ESD detail:** See `Design_Spec.md §5 — Thermal & ESD` for the full ESD protection scheme applicable to this board.

* **Rotor-facing connectors (TVS required):** All Samtec ERM8/ERF8 connectors (J1–J6) require TPD4E05U06QDQARQ1 ESD arrays within 3mm of the mating edge per DEC-045 and DEC-048.
  Arrays are assigned to U2–U9 (see `Design_Spec.md §5`).
* **Internal connectors (no TVS required):** J7, J8 (Extension Port BHR-20-VUA shrouded box) and J9, J10 (AM dock ERF8-005) are not operator-accessible during live rotor swap.
  No TVS required per `design/Standards/Global_Routing_Spec.md §9`.
