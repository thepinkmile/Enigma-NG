# Checkpoint 071 — INA219 RC Filter BOM Complete

**Status:** Complete  
**Commit:** 1c03bfc  
**Files changed:** 3

## What was done

Added INA219 RC input filter resistors and differential capacitor to both INA219
instances (PM and Stator). Both boards previously had descriptive text referencing
an RC filter on IN+/IN- but neither had the actual BOM entries for the series
resistors (RF1/RF2) or differential filter capacitor (CF).

### Power Module — new components

| Ref | Description | Part |
|-----|-------------|------|
| R52 | INA219 U12 IN+ series filter resistor (RF1) | ERJ-2RKF10R0X — 10Ω 1% Thin-Film 0402 |
| R53 | INA219 U12 IN- series filter resistor (RF2) | ERJ-2RKF10R0X — 10Ω 1% Thin-Film 0402 |
| C52 | INA219 U12 differential filter capacitor (CF) | CL05B104KB5NNNC — 100nF 50V X7R 0402 |

### Stator — new components

| Ref | Description | Part |
|-----|-------------|------|
| R42 | INA219 U2 IN+ series filter resistor (RF1) | ERJ-2RKF10R0X — 10Ω 1% Thin-Film 0402 |
| R43 | INA219 U2 IN- series filter resistor (RF2) | ERJ-2RKF10R0X — 10Ω 1% Thin-Film 0402 |
| C21 | INA219 U2 differential filter capacitor (CF) | CL05B104KB5NNNC — 100nF 50V X7R 0402 |

### Design parameters

- RF1 = RF2 = 10Ω, CF = 100nF → differential f_3dB = 1/(2π × 2×10 × 100nF) ≈ 80 kHz
- Input bias current error: 20µA × 10Ω = 200µV on 50mV full-scale shunt → 0.4% (acceptable for health monitoring)
- PM rationale: suppresses 400kHz LMQ61460A buck switching harmonics
- Stator rationale: suppresses FDC2114 resonant oscillator and electromechanical rotor noise
- Reference: INA219 datasheet Figure 14

### No new sourcing required

Both parts were already approved in the BOM:
- ERJ-2RKF10R0X: same as PM R49/R50/R51 (LM74700 GATE resistors)
- CL05B104KB5NNNC: same as numerous 100nF bypass caps on both boards

### Consolidated BOM updates

- Cross-board 10Ω row: PM count 3 → 5, Stator count — → 2, total 3 → 7
- PM 100nF reference list extended to include C52

## Outstanding deferred items

- Size-down pass: bulk cap voltage margin check (1206→0805/0402)
- Category C battery connector sourcing — awaiting supplier email responses
- Extension / Reflector / AM / JDB deep-review not yet started
- ENC-L-001: Encoder JTAG pull resistor consolidation (10Ω, same as rotors)
