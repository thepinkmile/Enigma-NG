# JTAG Signal Integrity — Analysis and Design Decision

**Status:** Adopted — see DEC-016 in `design/Design_Log.md`
**Project:** Enigma-NG
**Author:** Izzyonstage & GitHub Copilot
**Version:** v1.0
**Date:** 2026-04-05
**Affects:** Controller, Stator, Encoder, Reflector, Extension boards

---

## 1. Background and Problem Statement

The Enigma-NG JTAG chain spans multiple PCBs connected by 2.54mm IDC ribbon cables. During design
review it was identified that no impedance specification existed for JTAG traces, and no series
termination resistors had been defined for the cable-driving outputs. This document analyses all
available options, calculates trace widths and resistor values per board stackup, and records the
design decision adopted.

### JTAG Chain Topology

```text
FT232H (JDB)
    │  R1/R3 33Ω series R at TCK/TMS FT232H outputs → U5 buffer input
    │  U5 SN74LVC2G125DCUR buffer (TCK, TMS)
    │  R6/R7 33Ω after U5 output (TCK/TMS); R2 33Ω at FT232H TDI; R8 33Ω before J2 (TDI)
    ▼
J2 JTAG header → Controller hat-header (pass-through: no active components)
    ▼
LINK-BETA (BtB, no cable)
    │
    ▼
Stator CPLD (U1)
    │
    ├─ 75Ω ─▶ J4 ribbon cable (~100Ω IDC) ─▶ HID Encoder CPLD1
    │                                             33Ω (inter-CPLD)
    │                                         HID Encoder CPLD2
    │              75Ω ◀─ J4 TDO return ◀───────────────────────
    │
    ├─ 75Ω ─▶ J5 ribbon cable (~100Ω IDC) ─▶ Plugboard Encoder A CPLD1
    │                                             33Ω
    │                                         Plugboard Encoder A CPLD2
    │              75Ω ◀─ J5 TDO return ◀───────────────────────
    │
    ├─ 75Ω ─▶ J6 ribbon cable (~100Ω IDC) ─▶ Plugboard Encoder B CPLD1
    │                                             33Ω
    │                                         Plugboard Encoder B CPLD2
    │              75Ω ◀─ J6 TDO return ◀───────────────────────
    │
    └─▶ Rotor Stack (via Stator J1–J3 rotor interface → Rotor 1 J1–J3 → … → Rotor 30 J4–J6)
            └─▶ Rotor 1 … Rotor 30 … Reflector
                    └─▶ TTD_RETURN via J7 Extension Port ─▶ LINK-BETA pin 26 ─▶ FT232H
```

**TCK and TMS** are broadcast to all devices. On the Stator they fan out to J4, J5, and J6
encoder ports, each requiring its own series resistor before the ribbon cable.

**TDI/TDO** are serial-chained. Each cable-driving TDI output needs a series resistor; each
cable-driving TDO output similarly.

**SYS_RESET_N** is a very low-frequency quasi-DC signal (transitions only on system reset events).
Transmission line effects are negligible; no series resistor required.

---

## 2. Signal Characteristics

| Signal | Direction | Type | JTAG frequency | Rise time (EPM240) |
| --- | --- | --- | --- | --- |
| TCK | FT232H → all CPLDs | Clock (broadcast) | 1–10 MHz | ~2–3 ns |
| TMS | FT232H → all CPLDs | State (broadcast) | Transitions with TCK | ~2–3 ns |
| TDI | FT232H → CPLD chain | Serial data | Stable on TCK edge | ~2–3 ns |
| TDO | CPLD chain → FT232H | Serial data | Stable on TCK edge | ~2–3 ns |
| SYS_RESET_N | CM5 → all CPLDs | Active-low reset | DC / rare | N/A |

---

## 3. Physical Parameters by Board Stackup

### 3.1 JLCPCB JLC04161H-7628 — 4-Layer 1.6mm (Stator, Encoder, Rotor, Reflector, Extension)

| Parameter | Value | Source |
| --- | --- | --- |
| Prepreg (L1→L2) | 2116 style | JLCPCB stackup document |
| Dielectric height h | **0.087 mm** | Verified: JLCPCB calculator gives 50Ω at 0.127mm for this stackup |
| Copper thickness t | 0.035 mm (1oz outer) | Standard |
| Dielectric constant Eᵣ | 4.4 | FR4 2116 prepreg |
| JTAG layer | L1 (top) — microstrip over L2 GND plane | See note below |
| Manufacturing minimum trace width | 0.127 mm (5 mil) | JLCPCB standard process |

> **Why L1?** On the JLC04161H-7628 stackup, L2 (GND) and L3 (3V3_ENIG power) are solid planes
> dedicated to their functions — they are not available as signal layers. This leaves L1 (top) and
> L4 (bottom) as the only signal layers. L1 over L2 GND provides the tightest dielectric coupling
> (h = 0.087 mm) and the best achievable controlled impedance. L4 over L3 (power plane) is
> functionally acceptable but less ideal. **L1 is therefore the mandatory JTAG routing layer on
> all 4-layer boards.** This decision is EMC-optimal for this stackup: the contiguous L2 GND plane
> immediately below L1 provides consistent return-current path and low radiated-field coupling.
> **Exception:** the JTAG Daughterboard (JDB) uses an inverted stackup (L1=GND/SMT, L2=signals,
> L3=Power, L4=GND) to orient SMT components toward the Controller Board when mounted as a hat.
> On the JDB, JTAG signals are routed on L2 over the L1 GND reference plane. See
> `JTAG_Daughterboard/Design_Spec.md §4` and DEC-017.

### 3.2 JLCPCB JLC06161H-2116 — 6-Layer 1.6mm (Controller)

| Parameter | Value | Source |
| --- | --- | --- |
| Prepreg (L5→L6) | 2116 style | JLCPCB 6-layer stackup |
| Dielectric height h | **~0.087 mm** | Similar outer prepreg to 4-layer; same calculator result |
| Copper thickness t | 0.035 mm (1oz outer) | Standard |
| Dielectric constant Eᵣ | 4.4 | FR4 2116 |
| JTAG layer | L6 (bottom) — microstrip over L5 GND plane | Per Controller stackup spec |
| Manufacturing minimum | 0.127 mm (5 mil) | JLCPCB standard process |

### 3.3 2-Layer 1.6mm FR4 — Historical Reference (Superseded by DEC-017)

> **Note:** The Reflector and Extension boards originally used a 2-layer stackup. DEC-017 upgrades
> all non-Controller boards to 4-layer JLC04161H-7628. The calculations in §4 below for 2-layer
> boards are retained for historical reference only. These boards now use the §3.1 parameters.

| Parameter | Value | Notes |
| --- | --- | --- |
| Dielectric height h | **1.53 mm** | Full board thickness minus both copper layers |
| Copper thickness t | 0.035 mm (1oz) | Standard |
| Dielectric constant Eᵣ | 4.4 | FR4 |
| JTAG layer | L1 — microstrip over any L2 GND pour | **Superseded** — no solid GND plane in former 2-layer design |

---

## 4. Impedance Formula (IPC-2141A Microstrip)

```text
Z₀ = (87 / √(Eᵣ + 1.41)) × ln(5.98h / (0.8w + t))

Where:
  Z₀  = characteristic impedance (Ω)
  Eᵣ  = dielectric constant of prepreg
  h   = dielectric height, copper-to-copper (mm)
  w   = trace width (mm)
  t   = copper thickness (mm)
```

For the 4-layer/6-layer outer-layer stackup (h = 0.087 mm, t = 0.035 mm, Eᵣ = 4.4):

```text
K = 87 / √(4.4 + 1.41) = 87 / √5.81 = 87 / 2.410 = 36.1
```

### Solving for 50Ω (w = ?)

```text
50 = 36.1 × ln(5.98 × 0.087 / (0.8w + 0.035))
50 = 36.1 × ln(0.520 / (0.8w + 0.035))
1.385 = ln(0.520 / (0.8w + 0.035))
3.994 = 0.520 / (0.8w + 0.035)
0.8w + 0.035 = 0.130
w = 0.119 mm → rounded to 0.127 mm (5 mil) for design rule consistency
```

✅ **0.127 mm is achievable** (JLCPCB minimum = 0.127 mm; confirmed by their online calculator)

> **Note on copper weight:** The IPC-2141A formula uses t = base copper thickness before plating.
> JLCPCB's 2oz finished specification starts from 1oz (t=0.035mm) base copper plus plating.
> Using t=0.035mm in the formula is correct for the geometric model. Actual finished Zo with
> 2oz plating build-up is approximately 40–50Ω depending on plating thickness. At JTAG operating
> frequencies of 1–10MHz, this variance is functionally tolerable; the 33Ω series resistors
> provide additional mismatch absorption.

### Solving for 100Ω (w = ?)

```text
100 = 36.1 × ln(0.520 / (0.8w + 0.035))
2.770 = ln(0.520 / (0.8w + 0.035))
15.96 = 0.520 / (0.8w + 0.035)
0.8w + 0.035 = 0.0326
0.8w = −0.0024   →   NEGATIVE — physically impossible
```

❌ **100Ω single-ended is not achievable** on this stackup. The thin 0.087 mm prepreg
(required for component density in 4-layer/6-layer boards) constrains the geometry such
that 100Ω would require a trace narrower than 0 mm. This is a fundamental physics constraint,
not a manufacturer limitation.

### 2-Layer Board — 50Ω Calculation (h = 1.53 mm)

```text
50 = 36.1 × ln(5.98 × 1.53 / (0.8w + 0.035))
50 = 36.1 × ln(9.15 / (0.8w + 0.035))
1.385 = ln(9.15 / (0.8w + 0.035))
3.994 = 9.15 / (0.8w + 0.035)
w = 2.82 mm
```

❌ **2.82 mm trace — impractical** for signal routing on a space-constrained PCB.
Controlled impedance is not specified for 2-layer boards (Reflector, Extension).

### 2-Layer Board — 100Ω Calculation (h = 1.53 mm)

```text
100 = 36.1 × ln(9.15 / (0.8w + 0.035))
2.770 = ln(9.15 / (0.8w + 0.035))
15.96 = 9.15 / (0.8w + 0.035)
w = 0.538 mm
```

⚠️ **0.538 mm (21 mil) — achievable** but not useful here. The 2-layer Reflector and Extension
boards have short JTAG traces (<50 mm) and no solid GND plane. At JTAG frequencies (1–10 MHz),
electrical lengths are well below the λ/6 critical threshold (~100 mm for 3 ns rise time). Series
termination resistors at the driving ends of each cable segment are sufficient.

---

## 5. Ribbon Cable Impedance

Standard 2.54 mm pitch IDC flat ribbon cable has the following impedance characteristics:

| Configuration | Approx. Zo | Notes |
| --- | --- | --- |
| All-signal (no interleaved GND) | 130–150 Ω | Worst case; no shielding |
| Alternating signal/GND | **~100 Ω** | Confirmed by Belden/3M cable datasheets |
| Shielded ribbon (overall foil) | ~100 Ω | Foil improves EMI; minimal Zo change |

The Enigma-NG 26-pin encoder port connector already specifies **alternating GND pins between all JTAG
signals** (J4–J6 pin table in `Stator/Board_Layout.md`). This places the cable Zo at approximately
**100 Ω**.

> **Key implication:** The PCB-to-cable impedance discontinuity is from 50 Ω (PCB trace) to 100 Ω
> (ribbon cable). This mismatch can be minimised by sizing the series resistor to target the **cable
> impedance** rather than the PCB trace impedance.

---

## 6. Options Analysis

### CPLD Output Driver Impedance

The Intel MAX II EPM240T100I5N has a typical I/O output impedance (Zo_driver) of approximately
**15–20 Ω** in its 3.3V LVTTL drive mode. For calculations below, **Zo_driver = 20 Ω** is used.

---

### Option A — No Series Termination (Baseline)

```text
Source impedance = 20 Ω (driver alone)
PCB trace Zo     = uncontrolled (~50–150 Ω depending on routing)
Cable Zo         = ~100 Ω
Mismatch at PCB→cable: significant
Re-reflection at source: severe (20 Ω vs 100 Ω → Γ = −0.67)
```

**Result:** Multiple round-trip reflections, potentially 20–50% overshoot, visible ringing on TCK.
At 10 MHz with 3 ns rise times, false clock edges are possible on longer cables.

❌ **Not recommended.**

---

### Option B — 50Ω PCB + 33Ω Series Resistor (Match PCB Trace)

```text
Series R        = 33 Ω
Total source Z  = 20 + 33 = 53 Ω ≈ 50 Ω (matched to PCB trace)
PCB trace Zo    = 50 Ω (controlled, 0.127 mm)
```

**At PCB→cable transition (50 Ω → 100 Ω):**

```text
Γ_forward = (100 − 50) / (100 + 50) = +0.33   (33% reflection toward source)
```

**Returning reflection hits source (53 Ω):**

```text
Γ_source = (50 − 53) / (50 + 53) ≈ 0.0   (reflection almost fully absorbed ✓)
```

**At cable end (high-Z CPLD input):**

```text
V_launched onto cable = 3.3 × 100 / (53 + 100) = 2.16 V  (on first wave)
V_at_destination = V_launched + reflected = 2.16 + (0.33 × 2.16) ≈ 2.87 V
```

⚠️ The destination sees a slightly reduced first swing (~2.87 V) before settling to 3.3 V after one
round trip (~5–10 ns). Functionally correct, but the cable-entry reflection is not absorbed.

**Conclusion:** Good on-board signal integrity. Cable mismatch creates an unabsorbed reflection that
travels to the source, gets absorbed, but leaves a partial glitch on the cable during settling.

⚠️ **Acceptable, but not optimal for cable-driving outputs.**

---

### Option C — 100Ω PCB + 82Ω Series Resistor (Ideal — Not Achievable)

```text
Series R        = 82 Ω
Total source Z  = 20 + 82 = 102 Ω ≈ 100 Ω (matched to cable)
PCB trace Zo    = 100 Ω — REQUIRES w ≈ −0.002 mm (impossible)
```

If achievable, this would give perfect PCB-to-cable impedance matching with zero reflection at the
cable entry. The signal at the destination would still reach full logic swing via the open-end
reflection (V_dest = 2 × V_launched = 2 × 1.65 V = 3.30 V ✓).

❌ **Not achievable** on JLCPCB JLC04161H-7628 or JLC06161H-2116 stackups.
See §4 trace width calculation.

---

### Option D — 50Ω PCB + 75Ω Series Resistor (Selected)

This approach decouples PCB trace impedance from source termination. The **series resistor targets
the cable impedance (100 Ω)** rather than the PCB trace impedance (50 Ω).

```text
Series R        = 75 Ω
Total source Z  = 20 + 75 = 95 Ω ≈ 100 Ω (matched to cable Zo)
PCB trace Zo    = 50 Ω (controlled, 0.127 mm — achievable)
```

**At PCB→cable transition (50 Ω → 100 Ω):**

```text
Γ_forward = (100 − 50) / (100 + 50) = +0.33   (33% reflection toward source)
```

**Returning reflection hits source (95 Ω):**

```text
Γ_source = (50 − 95) / (50 + 95) = −0.31   (31% re-reflected, with inversion)
```

The PCB-to-cable discontinuity is not perfectly eliminated, but the return reflection at the source
(−0.31) dampens successive bounces rapidly. Each successive wave is attenuated by 0.31², 0.31³ etc.

**Signal swing at destination (high-Z CPLD input):**

```text
V_launched onto cable = 3.3 × 100 / (95 + 100) = 1.69 V
V_at_destination = 2 × V_launched = 2 × 1.69 = 3.38 V ≈ 3.3 V  ✓  (full logic swing)
```

The open-circuit reflection at the CPLD input doubles the wave back to full logic swing. The
destination always sees full voltage — the series resistor does not weaken the received signal.

**Intra-board traces (inter-CPLD, CPLD→connector on same PCB):**

For traces that do NOT drive a ribbon cable (e.g., CPLD1 TDO → CPLD2 TDI on the Encoder board),
the system is 50 Ω PCB throughout. Use **33 Ω series R** (source Z = 53 Ω ≈ 50 Ω, matched to PCB).

**Critical length check (do these traces actually need termination?):**

```text
Critical trace length = (Rise time × propagation speed) / 6
                      = (3 ns × 200 mm/ns) / 6  =  100 mm
```

At typical JTAG trace lengths on a PCB (<50 mm), intra-board traces are electrically short and
the 33 Ω resistor provides protection and slew-rate control rather than strict termination. At
cable lengths of 200–500 mm the 75 Ω resistors are functionally necessary.

✅ **Option D is the selected solution.** See DEC-016 for formal adoption.

---

### Option Summary Table

| Option | PCB Zo | Series R | Source Z | Cable Zo match | PCB-trace match | Achievable? | Verdict |
| --- | --- | --- | --- | --- | --- | --- | --- |
| A — No termination | Uncontrolled | None | 20 Ω | ❌ Poor | ❌ Poor | Yes | Rejected |
| B — Match PCB | 50 Ω | 33 Ω | 53 Ω | ⚠️ Partial | ✅ Excellent | Yes | Acceptable |
| C — Match cable (ideal) | 100 Ω | 82 Ω | 102 Ω | ✅ Excellent | ✅ Excellent | **No** | Not possible |
| **D — Hybrid (selected)** | **50 Ω** | **75 Ω (cable) / 33 Ω (intra-board)** | **95 Ω / 53 Ω** | **✅ Good** | **✅ Good** | **Yes** | **Selected** |

---

## 7. Component Values and Placement

### 7.1 Series Resistor Values

| Placement | R value | Rationale |
| --- | --- | --- |
| Driving a ribbon cable (~100 Ω IDC) | **75 Ω** | Source Z = 95 Ω ≈ cable Zo |
| Intra-board (CPLD output → same-board CPLD input) | **33 Ω** | Source Z = 53 Ω ≈ PCB Zo |
| JDB U5 output → LINK-BETA (BtB, no cable) | **33 Ω** | Short BtB trace; match 50 Ω PCB; U5 out Z (15Ω) + 33Ω ≈ 48Ω |

### 7.2 Placement Rule

Series resistors must be placed **within 2 mm of the driving pin** (CPLD output or buffer output).
Placing the resistor close to the source ensures reflections are absorbed before travelling any
distance on the trace.

### 7.3 Signals Requiring Series Resistors

| Signal | Cable-driving | Intra-board | Notes |
| --- | --- | --- | --- |
| TCK | 75 Ω (at each Stator encoder port output) | — | Clock — most critical |
| TMS | 75 Ω (at each Stator encoder port output) | — | State machine control |
| TDI | 75 Ω (at each Stator→encoder cable drive) | 33 Ω (inter-CPLD on Encoder) | Chained data |
| TDO | 75 Ω (at each Encoder CPLD2 → cable output) | — | Return chain data |
| SYS_RESET_N | None required | None required | Quasi-DC signal |

### 7.4 Per-Board Implementation

| Board | New refs | Value | Qty | Location |
| --- | --- | --- | --- | --- |
| JDB | R6 | 33 Ω | 1 | TCK after U5 buffer, before J2 JTAG header pin 1 (TCK) |
| JDB | R7 | 33 Ω | 1 | TMS after U5 buffer, before J2 JTAG header pin 7 (TMS) |
| JDB | R8 | 33 Ω | 1 | TDI series damping (not buffered — from FT232H), before J2 JTAG header pin 3 (TDI) |
| Stator | R7 | 75 Ω | 1 | TCK → J4 encoder port output |
| Stator | R8 | 75 Ω | 1 | TCK → J5 encoder port output |
| Stator | R9 | 75 Ω | 1 | TCK → J6 encoder port output |
| Stator | R10 | 75 Ω | 1 | TMS → J4 encoder port output |
| Stator | R11 | 75 Ω | 1 | TMS → J5 encoder port output |
| Stator | R12 | 75 Ω | 1 | TMS → J6 encoder port output |
| Stator | R13 | 75 Ω | 1 | Stator CPLD TDO → J4 TDI (ribbon drive) |
| Stator | R14 | 75 Ω | 1 | J4 TDO return → J5 TDI (ribbon drive) |
| Stator | R15 | 75 Ω | 1 | J5 TDO return → J6 TDI (ribbon drive) |
| Encoder | R7 | 33 Ω | 1 | CPLD1 TDO → CPLD2 TDI (intra-board 50 Ω trace) |
| Encoder | R8 | 75 Ω | 1 | CPLD2 TDO → J2 connector pin 13 (ribbon drive back to Stator) |
| Reflector | R1 (existing) | 22 Ω | 1 | TDO end-of-chain series damping (unchanged) |

> **Controller JTAG pass-through:** The Controller board carries no active JTAG components. All
> buffering (U5 SN74LVC2G125DCUR) and series damping (R6–R8, 33 Ω 0402) are located on the JDB.
> LINK-BETA is a direct BtB connector (no cable), so 33 Ω applies (not 75 Ω). See DEC-024.
>
> **Reflector and Extension:** Upgraded to 4-layer JLC04161H-7628 per DEC-017. Both boards now
> have a solid L2 GND plane. JTAG traces route on L1 at 0.127 mm (50 Ω controlled impedance),
> consistent with all other 4-layer boards. The "uncontrolled impedance" note from DEC-016 is
> superseded.

---

## 8. Trace Width Design Rule

| Board | Stackup | JTAG Layer | Target Zo | Trace width | Status |
| --- | --- | --- | --- | --- | --- |
| JDB | JLC04161H-7628 (4L) | L2 over L1 GND | 50 Ω | **0.127 mm (5 mil)** | JDB is the complete JTAG master. U5 buffer and R6–R8 series damping on JDB. Controller is pass-through. |
| Controller | JLC06161H-2116 (6L) | L6 over L5 GND | 50 Ω | **0.127 mm (5 mil)** | Pass-through only — no active JTAG components on Controller (see DEC-024) |
| Stator | JLC04161H-7628 (4L) | L1 over L2 GND | 50 Ω | **0.127 mm (5 mil)** | Added to §3 |
| Encoder | JLC04161H-7628 (4L) | L1 over L2 GND | 50 Ω | **0.127 mm (5 mil)** | Added to §6 |
| Reflector | JLC04161H-7628 (4L) | L1 over L2 GND | 50 Ω | **0.127 mm (5 mil)** | Updated per DEC-017 |
| Extension | JLC04161H-7628 (4L) | L1 over L2 GND | 50 Ω | **0.127 mm (5 mil)** | Updated per DEC-017 |

---

## 9. Cost Analysis

| Item | Unit cost | Qty (full system) | Total |
| --- | --- | --- | --- |
| 75 Ω 1% 0603 (Stator R7–R15) | ~£0.002 | 9 | <£0.02 |
| 75 Ω 1% 0402 (Encoder R8, ×3 boards) | ~£0.001 | 3 | <£0.01 |
| 33 Ω 1% 0402 (Encoder R7, ×3 boards) | ~£0.001 | 3 | <£0.01 |
| 33 Ω 1% 0402 (JDB R6–R8) | ~£0.002 | 3 | <£0.01 |
| Controlled impedance JLCPCB certification (optional) | ~£40/order | Per board type | ~£120 total if verified |
| **Controlled impedance design only (self-calc, no cert)** | **£0** | — | **£0** |

> **Recommendation:** Specify the 0.127 mm trace width in design rules. Do not pay for JLCPCB
> impedance verification on prototype boards — the self-calculated value is within ±10% of the
> target, which is well within the functional margin for 1–10 MHz JTAG signals. Impedance
> certification adds value only for production runs where consistency must be guaranteed.
>
> **Total additional BOM cost per full system: < £0.05** (a few tens of passive resistors).

---

*Decision formally recorded as DEC-016 in `design/Design_Log.md`.*
