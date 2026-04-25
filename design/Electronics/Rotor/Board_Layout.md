# Rotor Board Layout Visualisations

**Status:** Draft
**Project:** Enigma-NG
**Author:** Izzyonstage & GitHub Copilot
**Version:** v1.0.0
**Associated Hardware Revision:** Rev A
**Last Updated:** 2026-04-20

For mechanical tolerances and shroud assembly details, see
`design/Mechanical/Rotor/Design_Spec.md`.

---

## 1. Split Board Architecture Overview

Each rotor assembly consists of two circular PCBs (Board A and Board B), each Ø92mm, separated
by an 11.8mm gap and connected by four single-row 2.54mm THT headers (H_SW3 1×7, H_PWR 1×5,
H_JTAG 1×5, H_SENS 1×5; 22 pins total; mixed gender for keying). The two boards are mechanically
retained inside the aluminium shroud (Ø100mm outer face, 4mm radial wall, Ø92mm inner). Total
rotor thickness is ~15mm.

---

## 2. Board A — Input Side (Ø92mm)

Board A faces the input (upstream) side of the rotor stack.

```text
4-Layer / 2oz Copper / ENIG / Circular Ø92mm — BOARD A (INPUT SIDE)

                        TOP (outer face, faces upstream)
         __________________________________________________
        /                                                  \
       /    [SW1] ring setting DIP                          \
      |     [SW2] forward map select DIP                     |
      |                                                      |
      |              [ U1: CPLD EPM570T100I5N ]              |
      |                    (centre)                          |
      |                                                      |
      |   [S0][S1][S2]  <-- Track A sensor electrodes        |
      |   (bare Cu pads at r=44mm, Board A face)             |
      |         [ U2: FDC2114 ] (at r~40mm)                  |
      |                                                      |
      | [J1 ERM8]  [J2 ERM8]  [J3 ERM8]                      |
       \   (JTAG)   (Power)  (ENC Data)   equally spaced     /
        \___________________________________________________/

                    BOTTOM (inner face, faces Board B)
          [ H_SW3 M ]  [ H_PWR F ]  [ H_JTAG F ]  [ H_SENS M ]
                         (manually assembled post-SMT)
```

### 2.1 Board A Component Summary

| Ref | Component | Notes |
| :--- | :--- | :--- |
| U1 | EPM570T100I5N CPLD | Centre of board |
| U2 | FDC2114RGHR | Track A capacitive encoder IC (I²C addr 0x2A); r~40mm |
| U3 | FDC2114RGHR | STGC bit[4] sensor IC (I²C addr 0x2B); Board A, N=26 builds only — NOT POPULATED for N=64 |
| S0–S2 | Sensor electrodes (Track A) | Bare Cu pads at r=44mm, N=64 bits[5:3]; or S0–S4 for N=26 |
| SW1 | 6-pos DIP — ring setting | Input side only |
| SW2 | 6-pos DIP — forward map select | Input side |
| J1 | ERM8-005 male | JTAG input (10-pin 2×5, 0.8mm pitch) |
| J2 | ERM8-005 male | Power input (10-pin 2×5, 0.8mm pitch) |
| J3 | ERM8-010 male | ENC data input (20-pin 2×10, 0.8mm pitch) |
| H_SW3 | Adam Tech PH1-07-UA (male 1×7) | Inner face; manually assembled post-JLCPCB SMT; H_SW3/H_SENS male on Board A |
| H_PWR | Adam Tech RS1-05-G (female 1×5) | Inner face; manually assembled post-JLCPCB SMT |
| H_JTAG | Adam Tech RS1-05-G (female 1×5) | Inner face; manually assembled post-JLCPCB SMT |
| H_SENS | Adam Tech PH1-05-UA (male 1×5) | Inner face; manually assembled post-JLCPCB SMT |

---

## 3. Board B — Output Side (Ø92mm)

Board B faces the output (downstream) side of the rotor stack.

```text
4-Layer / 2oz Copper / ENIG / Circular Ø92mm — BOARD B (OUTPUT SIDE)

                    TOP (inner face, faces Board A)
          [ H_SW3 F ]  [ H_PWR M ]  [ H_JTAG M ]  [ H_SENS F ]
                         (manually assembled post-SMT)

         ___________________________________________________
        /                                                   \
       /    [SW3] return map select DIP                      \
      |                                                      |
      |                                                      |
      |                                                      |
      |   [S3][S4][S5]  <-- Track B sensor electrodes        |
      |   (bare Cu pads at r=44mm, Board B face)             |
      |         [ U4: FDC2114 ] (at r~40mm)                  |
      |         (NOT POPULATED for N=26 rotor)               |
      |                                                      |
      | [J4 ERF8]  [J5 ERF8]  [J6 ERF8]                      |
       \   (JTAG)   (Power)  (ENC Data)   equally spaced     /
        \___________________________________________________/

                        BOTTOM (outer face, faces downstream)
```

### 3.1 Board B Component Summary

| Ref | Component | Notes |
| :--- | :--- | :--- |
| U4 | FDC2114RGHR | Track B capacitive encoder IC (I²C addr 0x2B); r~40mm; **not populated for N=26** |
| S3–S5 | Sensor electrodes (Track B) | Bare Cu pads at r=44mm, N=64 bits[2:0]; not present for N=26 |
| SW3 | 6-pos DIP — return map select | Output side |
| J4 | ERF8-005 female | JTAG output (10-pin 2×5, 0.8mm pitch) |
| J5 | ERF8-005 female | Power output (10-pin 2×5, 0.8mm pitch) |
| J6 | ERF8-010 female | ENC data output (20-pin 2×10, 0.8mm pitch) |
| H_SW3 | Adam Tech RS1-07-G (female 1×7) | Inner face; manually assembled post-JLCPCB SMT; H_SW3/H_SENS female on Board B |
| H_PWR | Adam Tech PH1-05-UA (male 1×5) | Inner face; manually assembled post-JLCPCB SMT |
| H_JTAG | Adam Tech PH1-05-UA (male 1×5) | Inner face; manually assembled post-JLCPCB SMT |
| H_SENS | Adam Tech RS1-05-G (female 1×5) | Inner face; manually assembled post-JLCPCB SMT |

---

## 4. Stacking / Cross-Section

```text
  INPUT SIDE                                          OUTPUT SIDE
  (Board A outer)                                   (Board B outer)
      |                                                    |
      v                                                    v
  [J1 J2 J3]   [Board A 1.6mm]  [gap 11.8mm]  [Board B 1.6mm]   [J4 J5 J6]
  ERM8 male  |<--Ø92mm PCB-->|<--4 headers->|<--Ø92mm PCB-->|  ERF8 female
             |               |  22p total   |               |
             |<---------------  ~15mm total  -------------->|

  Aluminium shroud (Ø100mm outer, Ø92mm inner, 4mm radial wall)
  Shroud dish flange (Board A side): Track A Gray code slots milled on inner face
  Shroud cover flange (Board B side): Track B Gray code slots milled on inner face (N=64 only)
  Rolling-pin cylindrical bearings (ceramic or nylon) around circumference — electrically isolating
  Shroud outer cylindrical face: characters engraved at r=50mm
```

**Dimensions summary:**

| Item | Value |
| :--- | :--- |
| Shroud outer diameter | Ø100mm |
| Shroud radial wall thickness | 4mm |
| PCB diameter (both boards) | Ø92mm |
| PCB thickness (each) | 1.6mm |
| Board gap (Board A inner to Board B inner) | ~11.8mm |
| Total rotor thickness | ~15mm |
| Sensor electrode radius | r=44mm |
| Shroud–electrode gap | 0.5mm ±0.15mm |

---

## 5. Rotor Interface Connectors
>
> **Connector Definition Owner:** This board. All other boards hosting rotor interface connectors
> (Stator J1–J3, Extension J1–J6, Reflector J1–J3) cross-reference here.

Each rotor position uses **three connectors** — one for ENC data in, one for ENC data out, and one for power/JTAG.
These three connectors must be **positionally identical** across every board that mates with rotors
(Stator input side, Extension mid-stack, Reflector final output) to allow any rotor to mate at any position.

> **⚠️ Note:** The earlier draft signal maps (ENC-IN, ENC-OUT, PWR/JTAG with 8-pin and 14-pin tables)
> have been removed. All connector definitions now live exclusively in `Rotor/Design_Spec.md §3.4`.
> Use the Design_Spec §3.4 tables for all schematic and PCB layout work.
>
### 5.1 Connector Summary

Each rotor carries **six connectors** — three male ERM8 headers on the input side (J1–J3) and three female
ERF8 sockets on the output side (J4–J6). See `Rotor/Design_Spec.md §3.4` for the authoritative pinout tables.

| Designator | Type | Part | Pins | Function |
| :--- | :--- | :--- | :--- | :--- |
| J1 | ERM8-005 male | 200-ERM8005050SDVKTR | 10 (2×5) | JTAG input |
| J2 | ERM8-005 male | 200-ERM8005050SDVKTR | 10 (2×5) | Power input |
| J3 | ERM8-010 male | 200-ERM8010050SDVKTR | 20 (2×10) | Encoder data input |
| J4 | ERF8-005 female | 200-ERF8005050SDVKTR | 10 (2×5) | JTAG output → next rotor J1 |
| J5 | ERF8-005 female | 200-ERF8005050SDVKTR | 10 (2×5) | Power output → next rotor J2 |
| J6 | ERF8-010 female | 200-ERF8010050SDVKTR | 20 (2×10) | Encoder data output → next rotor J3 |

### 5.2 TTD Routing Note

TTD (JTAG Transmission Data) does not chain back through the Extension Port individually per rotor. Each
rotor passes TTD to the **next rotor's TDI** directly via J4 pin 6 → next Rotor J1 pin 6. Only **Rotor 30**
(last in chain) routes its TDO via the Reflector back to Stator J10 pin 15 as TTD_RETURN.

---

## 6. U1 — Rotor CPLD Signal Map (Logical Pin Budget)

> This is the board-authoritative **logical** signal map for Rotor Board A `U1`. The local MAX II
> handbook confirms `EPM570T100` package availability in TQFP-100, but it points printed device
> pin-outs to external package documentation rather than providing a fixed package pin table locally.
> The map below therefore freezes the required rotor connectivity while leaving exact TQFP pad numbers
> to schematic capture.

### 6.1 Dedicated device pins

| Function | Source / destination | Notes |
| :--- | :--- | :--- |
| `TCK` | J1 pin 2 / H_JTAG pin 1 -> U1 | Dedicated JTAG clock input; forwarded to Board B and onwards to J4 |
| `TMS` | J1 pin 4 / H_JTAG pin 3 -> U1 | Dedicated JTAG mode input; forwarded to Board B and onwards to J4 |
| `TDI` | J1 pin 6 (`TTD`) -> U1 | Incoming serial JTAG data from the previous stage; connector name stays `TTD` for stack clarity |
| `TDO` | U1 -> H_JTAG pin 5 / J4 pin 6 (`TTD`) | Outgoing serial JTAG data to the next stage |
| `DEV_CLRN` / reset input | J1 pin 8 (`SYS_RESET_N`) / H_JTAG pin 4 -> U1 | Active-low device reset; held high locally by R5 |

### 6.2 General-purpose signal groups

| Signal group | Pins | U1 direction | Notes |
| :--- | :---: | :--- | :--- |
| `J3 ENC_IN[5:0]` | 6 | Input | Forward-path cipher input from the upstream stage |
| `J6 ENC_OUT[5:0]` | 6 | Output | Forward-path cipher result to the downstream stage |
| `J6 ENC_IN[5:0]` | 6 | Input | Return-path cipher input from the downstream stage |
| `J3 ENC_OUT[5:0]` | 6 | Output | Return-path cipher result back to the upstream stage |
| `SW1[5:0]` | 6 | Input | Ring-setting switch bank on Board A |
| `SW2[5:0]` | 6 | Input | Forward-map select switch bank on Board A |
| `SW3[5:0]` | 6 | Input | Return-map select switch bank brought from Board B via `H_SW3` |
| Local `SDA`, `SCL` | 2 | Bidirectional | CPLD I2C master for U2/U3/U4 position sensors; `H_SENS` extends the same bus to Board B U4 |

**Logical budget summary:** 44 general-purpose signal connections total = **30 inputs + 12 outputs + 2
bidirectional I2C lines**, plus the dedicated JTAG / reset pins above.

**Variant / reserve policy:** `ENC[5]` remains physically routed for the shared 20-pin connector pinout
even on N=26 builds where that bit is logically unused. `H_SENS` pins 3-5 stay reserved and are not
currently tied into U1. Virtual JTAG position export uses the dedicated JTAG infrastructure and does
not consume extra board-level I/O pins.

---

## 7. Routing — Trace Width Specifications

**Board specs:** 4-layer / 2oz finished copper (JLC04161H-7628).
L1 = signal (JTAG/routing); L2 = GND plane; L3 = 3V3_ENIG power pour; L4 = secondary routing / data plate.

**IPC-2221A basis (2oz copper, external, 10°C rise, 25°C ambient):**
For 2oz external: ~0.15 mm/A. The 3V3_ENIG inner pour (L3) handles bus current without width constraints.
See Global_Routing_Spec.md §1.1 for the full current-category table.

**Rotor power analysis (pass-through sizing):**
Each rotor draws 50 mA (EPM570) + 2 × 2.1 mA (FDC2114 pair U2/U4 or U2/U3) = **54.2 mA ≈ 55 mA** locally.
The J2 power input connector daisy-chains 3V3_ENIG through J5 to the next rotor. All 30 rotor PCBs
are **identical**, so traces must be sized for the worst case — **Rotor 1**, which receives
Using the 55 mA design budget, Rotor 1 carries **1.65 A** through its J2 connector and passes
29 × 55 mA = **1.60 A** to Rotor 2 via J5.

| Rotor position | J2 input current | Local draw | J5 output current |
| :--- | :--- | :--- | :--- |
| Rotor 1 (worst case) | 1.65 A | 55 mA | 1.60 A |
| Rotor 15 (mid-stack) | 0.88 A | 55 mA | 0.83 A |
| Rotor 30 (last) | 55 mA | 55 mA | 0 A |

IPC calculation for worst-case 1.65 A at 2oz external: 1.65 × 0.15 mm = 0.25 mm → **0.80 mm** (3V3_ENIG canonical width per Global_Routing_Spec §1.1; consistent with PM and Stator 3V3_ENIG trunk traces).

### 7.1 Trace Width Table

| Net | Peak Current | IPC Calc (2oz ext) | Design Min | **Specified Width** | Layer | Notes |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Signal (ENC_IN/OUT, FDC2114 I2C SDA/SCL, SYS_RESET_N) | < 5 mA | < 0.001 mm | 0.20 mm | **0.20 mm** | L1 | 3.3 V logic; CPLD data I/O; I2C to FDC2114 capacitive encoder; SYS_RESET_N is a slow-logic CPLD reset sourced from Stator U7 GPA[7] — not a CI signal |
| JTAG signals: TCK, TMS, TTD in/out (CI) | signal | — | 0.127 mm | **0.127 mm (5 mil)** | L1 (external) | 50 Ω controlled impedance over L2 GND plane; per DEC-016. External layer — no inner-layer minimum conflict. |
| 3V3_ENIG local draw (J2 → CPLD + FDC2114 supply) | 55 mA | 0.008 mm | 0.80 mm | **0.80 mm** | L1 + L3 pour | 3V3_ENIG canonical 0.80 mm (Global_Routing_Spec §1.1); local IC supply only |
| 3V3_ENIG pass-through rail (J2 input → J5 output bus) | 1.65 A (Rotor 1 budget) | 0.25 mm | 0.80 mm | **0.80 mm** | L1 + L3 pour | Canonical 3V3_ENIG trunk width (Global_Routing_Spec §1.1); Rotor 1 worst case; feeds L3 pour via thermal vias between J2 and J5 |
| 3V3_ENIG distribution (inner power pour) | up to 1.65 A | — | pour | **copper pour** | L3 | Full uninterrupted 2oz plane; primary distribution across the board |
| GND return (inner GND pour) | — | — | pour | **copper pour** | L2 | Reference plane; must be solid and uninterrupted under all CI traces on L1 |

### 7.2 Notes

* **JTAG CI traces:** 0.127 mm (5 mil) on L1 over the L2 GND plane achieves 50 Ω controlled
  impedance on the JLC04161H-7628 stackup (h = 0.087 mm, t = 0.035 mm, Eᵣ = 4.4). Per DEC-016.
  See `design/Electronics/Investigations/JTAG_Integrity.md §3.1`.
* **Series termination R1 (75 Ω, CPLD TDO → J4 pin 6):** Placed within 2 mm of the CPLD TDO pin.
  Source impedance ≈ 95 Ω targeting the ~100 Ω inter-rotor Stator PCB segment. Trace from R1 to
  J4 kept < 5 mm and routed at 0.127 mm consistent with the CI chain.
* **3V3_ENIG power rail:** The L3 copper pour is the primary current path. L1 surface traces at
  0.80 mm connect J2/J5 connector pads to the L3 pour via thermal vias. All 30 rotor boards share
  the same PCB layout — the 1.65 A worst-case sizing ensures safe operation at every stack position.
