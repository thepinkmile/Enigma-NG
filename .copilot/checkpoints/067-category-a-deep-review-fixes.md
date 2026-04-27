# Checkpoint 067 — Category A deep-review fixes implemented and committed

**Date:** 2026-04-26
**Scope:** All Category A open items from the electronics deep-review cycle resolved, documented,
and committed together with the 13 pre-existing review-loop files as one coherent set.

## Outcome

All Category A user decisions (A1: AM support network, A2: Settings Board LED topology,
A3: Rotor FDC2114 resonant front-end) have been fully implemented across electronics and software
design documents. The working tree is now clean.

## Files modified/created in this session

### Actuation Module (A1)
- **`design/Electronics/Actuation_Module/Design_Spec.md`** — Added DR-AM-16 (C6 NRST filter
  cap, 100nF X7R per STM32G071 datasheet Figure 23) and DR-AM-17 (R5 BOOT0 10kΩ series
  resistor); updated J6/SW1/SW2/BOM rows.
- **`design/Software/Actuation_Module/Design_Spec.md`** — Updated ACTUATE_REQUEST signal row;
  added PUPDR `0b01` internal pull-up paragraph (firmware-configured, no external resistor).
- **`design/Electronics/Actuation_Module/Board_Layout.md`** — Added C6 and R5 placement notes.

### Settings Board (A2)
- **`design/Electronics/Settings_Board/Design_Spec.md`** — Added DR-SBD-10; rewrote U2/U3
  LED driver subsections for two-stage NMOS/PMOS hybrid topology; added Q7–Q30/R54–R77 BOM rows
  (Q19–Q30 and R66–R77 remain Cat B TBD).
- **`design/Electronics/Settings_Board/Board_Layout.md`** — Rewrote §1/§2/§5.1/§5.2/§6/§8.1
  for two-stage hybrid topology.

### Rotor (A3)
- **`design/Electronics/Rotor/Design_Spec.md`** — Corrected two U3/U4 unused-channel bullets
  (dummy LC tank wording per TI app note, replacing incorrect "GND via 100 kΩ"); added
  `#### Resonant Front-End Topology` subsection (LC tank 18 µH + 33 pF parallel, CLKIN→GND,
  CHx_FIN_SEL=`0b10`, IDRIVE `0b01111` → LT-001, deglitch `0b101` → LT-002, register map
  cross-refs); added L1–L12 and C20–C31 BOM rows (Cat B).
- **`design/Electronics/Rotor/Board_Layout.md`** — Added L1–L4/L5–L8/C20–C23/C24–C27 to Board
  A §2.1 table; L9–L12/C28–C31 to Board B §3.1 table.
- **`design/Software/CPLD_Logic/Rotor_Logic.md`** *(new file)* — FDC2114 I²C register map,
  internal oscillator rationale (DEC-044 cross-ref), CPLD I²C master behaviour, JTAG programming
  note, lab test cross-references.
- **`design/Procedures/Lab_Tests.md`** *(new file)* — LT-001 (IDRIVE baseline calibration)
  and LT-002 (fSENSOR resonant frequency validation).

### Cross-cutting
- **`design/Design_Log.md`** — Added DEC-044 "FDC2114 Internal Oscillator Selected (CLKIN → GND)";
  updated Last Updated date.
- **`design/Electronics/Consolidated_BOM.md`** — Added C6/R5 to AM section; added Q7–Q18/
  R54–R65 (locked) and Q19–Q30/R66–R77 (Cat B) to §4d Settings Board; added UNSOURCED rows for
  resonant tank inductors (L1–L12) and capacitors (C20–C31) to the component summary table;
  updated Last Updated date.

### Review-loop files (13 pre-existing, committed in same set)
All 13 files listed in checkpoint 066 carrying the electronics review-loop fixes.

## Category B items still open (not blocking)

| Item | Status |
| :--- | :--- |
| 18 µH shielded SMD resonant inductor (L1–L12) | Sourcing TBD |
| 33 pF C0G ±1% resonant capacitor (C20–C31) | Sourcing TBD |
| PMOS high-side switch Q19–Q30 | Part TBD |
| 47 kΩ PMOS gate pull-up R66–R77 | Part TBD |
| Rotor FDC2114 1 µF VDD bypass caps | Part TBD |
| Rotor FDC2114 I²C pull-ups R6/R7 | Value/part TBD |
| AM ACTUATE_REQUEST pull-up (firmware-configured internal) | Documented; no hardware change |

## Next session start

Read in this order:
1. `.copilot/plan.md`
2. `.copilot/handoff.md`
3. `.copilot/checkpoints/index.md` (this checkpoint is #67)
4. Continue with Category B sourcing or any new user direction.
