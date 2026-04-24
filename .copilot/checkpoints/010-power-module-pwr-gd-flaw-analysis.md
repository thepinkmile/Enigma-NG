# Checkpoint 010 — Power Module PWR_GD Flaw Analysis & Resolution
## Overview
Board-by-board design sanity check (starting with Power Module). Two real design flaws were
identified and resolved:

1. **SW2 wired to wrong pin** — was `GLOBAL_EN` (hard PMIC reset); should be `PWR_BUT`
   (graceful power key). Corrected with full documentation.
2. **PMIC_EN glitch during supercap hold-up** — LTC3350 threshold (4.40V) was below MCP121T
   threshold (4.50V), meaning PMIC_EN could briefly deassert before LTC3350 activated.
   Fixed by raising R14 to 28.7kΩ → threshold 4.64V (now above MCP121T threshold).

Additionally, a new **MIC1555 monostable one-shot circuit (U15)** was designed to automatically
pulse `PWR_BUT` for 3 seconds when LTC3350 enters backup mode — providing hardware-guaranteed
graceful OS shutdown without any firmware polling requirement.

---
## Commits
- `ff97f44` — SW2 rewired to PWR_BUT; U15 MIC1555 monostable one-shot added; FR-PM-07/08 added;
  Link-Alpha pin 48 reassigned from GND to PWR_BUT; PM Design_Spec + Controller Design_Spec +
  Controller Board_Layout updated.
- `a9d04db` — R14 threshold change fully propagated to Consolidated_BOM.md and
  Power_Management.md rewritten for new hardware-primary shutdown architecture.

---
## Work Done
### SW2 Fix
- SW2 was always intended as a graceful power-key button (wake CM5 after shutdown; or initiate
  graceful shutdown when running). Implementation was wrong: it pulled `GLOBAL_EN` (PMIC_EN) LOW
  via the MCP121T RESET pin — causing a hard PMIC disable.
- Fixed: SW2 now wired directly to `PWR_BUT` (Link-Alpha pin 48). No pull-up needed (CM5 has
  internal 10kΩ on `PWR_BUT`).
### U15 MIC1555 Monostable One-Shot
- New component: U15 MIC1555YM5-TR (SOT-23-5) in monostable configuration.
- Trigger: LTC3350 `/INTB` falling edge (open-drain, R29 10kΩ pull-up to 3V3_ENIG).
- Timing: t = 1.1 × 274kΩ × 10µF = 3.014 s (R28=274kΩ ERJ-3EKF2743V, C32=10µF 16V X7R).
- Output: drives Q5 BSS138 N-FET gate HIGH for 3 s → Q5 pulls `PWR_BUT` to GND.
- 3 s is midpoint of CM5 PMIC power-key graceful-shutdown window (1–5 s LOW = graceful shutdown;
  >5–8 s = hard power-off). The one-shot prevents exceeding 5 s.
- C33 = 100nF bypass for U15 VCC.
### R14 Threshold Reversal
- Old: R14=26.7kΩ (ERA-3ARB2672V) → threshold 4.40V (100mV BELOW MCP121T 4.50V threshold).
- Problem: in the 4.40–4.50V window, MCP121T had already deasserted PMIC_EN but LTC3350 was
  not yet active → brief PMIC_EN glitch could reset CM5.
- Fix: R14=28.7kΩ (ERA-3ARB2872V) → threshold 4.644V (140mV ABOVE MCP121T threshold).
- LTC3350 now activates first → 5V_MAIN restored before MCP121T threshold is reached.
- PMIC_EN never drops during normal backup entry.
### Link-Alpha Pin 48 Reassignment
- Was: GND zone boundary separator (no signal).
- Now: PWR_BUT (PM→CTRL, active-LOW).
- Updated in: Controller/Design_Spec.md (pin table), Controller/Board_Layout.md (table + ASCII
  diagram + bullet reference).
### Power_Management.md Rewrite
- Primary shutdown path is now **hardware**: LTC3350 `/INTB` → U15 → `PWR_BUT` → PMIC power-key
  → `systemd-logind` HandlePowerKey=poweroff.
- Phase 1 (custom LTC3350 driver, DEC-025) repositioned as optional telemetry/LED enhancement.
- Phase 2 (gpio-shutdown PWR_GD overlay) kept as last-resort backstop on supercap depletion.
- Timing budget table rewritten. All stale 4.40V/26.7kΩ references removed.
- `HandlePowerKey=poweroff` in `/etc/systemd/logind.conf` is the only software config needed
  for the primary path.

---
## New Components (Power Module)
| Ref | Part | Value | Package | Purpose |
|-----|------|-------|---------|---------|
| U15 | MIC1555YM5-TR | — | SOT-23-5 | Monostable one-shot (3.01 s PWR_BUT pulse) |
| Q5 | BSS138 | 50V N-FET | SOT-23 | Open-drain pull of PWR_BUT line |
| R28 | ERJ-3EKF2743V | 274kΩ 1% | 0603 | Monostable timing resistor |
| R29 | ERJ-3EKF1002V | 10kΩ 1% | 0603 | /INTB pull-up |
| C32 | CL10B106KA8NNNC | 10µF 16V X7R | 0603 | Monostable timing capacitor |
| C33 | CL05B104KB5NNNC | 100nF 50V X7R | 0402 | U15 VCC bypass |

---
## Files Modified
| File | Change |
|------|--------|
| design/Electronics/Power_Module/Design_Spec.md | SW2 rewired; FR-PM-07/08 added; U15/Q5/R28/R29/C32/C33 in BOM; R14 changed to 28.7kΩ/4.644V; shutdown sequence rewritten; Link-Alpha signal list updated |
| design/Electronics/Controller/Design_Spec.md | Pin 48: GND → PWR_BUT |
| design/Electronics/Controller/Board_Layout.md | Pin 48 in table, ASCII diagram, bullet |
| design/Electronics/Consolidated_BOM.md | R14 updated; U15, Q5, R28/R29/C32/C33 totals; new MIC1555 U15 detail row |
| design/Software/Linux_OS/Power_Management.md | Full rewrite: hardware-primary shutdown architecture |

---
## Technical Decisions
### PWR_GD / PMIC_EN / GLOBAL_EN (same net)
- Single MCP121T-450E open-drain output drives both CM5 `PMIC_EN` (via `GLOBAL_EN`) and GPIO 27
  (`PWR_GD` telemetry). They are the same physical wire.
- `PWR_GD` now acts as **rail-health telemetry only** — it does not trigger shutdown.
- `PWR_GD` remains HIGH throughout the entire hold-up window (LTC3350 keeps 5V_MAIN above 4.50V).
### CM5 PWR_BUT Timing (not yet PDF-verified)
- 1–5 s LOW: PMIC sends power-key event → systemd-logind → graceful shutdown (HandlePowerKey=poweroff).
- >5–8 s LOW: PMIC hard power-off (bypasses OS).
- 3 s one-shot chosen as midpoint — cannot overshoot into hard power-off.
- ⚠️ Exact thresholds not verified from `design/Datasheets/RPi-cm5-design-guide.pdf` (not
  text-extractable). Must verify at schematic capture stage.

---
## Open Work Items
- **Continue sanity check**: Controller → Stator → JDB → Encoder → Rotor → Extension → Reflector.
- **Rotor detailed design review** (R58+, two consecutive clean passes → INC-25, checkpoint 011).
- **OWI-001**: Test coupons per board.
- **OWI-002**: PAS definitions per board.
- **OWI-003**: VHDL pseudo-code and CPLD config plans.
- **OWI-018**: ENIG rib clearway bonding pad.
- **Deferred**: SW1 vintage switch research; ERA-3ARB2672V/ERA-3ARB1002V MOQ issue (now replaced by
  ERA-3ARB2872V for R14).

---
## Stale Values — Updated List
> All values from checkpoint 009 remain prohibited. Additions from this session:

- `26.7 kΩ` / `ERA-3ARB2672V` for R14 → now `28.7 kΩ` / `ERA-3ARB2872V`
- `4.40V` as LTC3350 backup trigger threshold → now `4.644V`
- "LTC3350 activates at 4.40V" anywhere → use "4.644V"
- "PWR_GD triggers shutdown" → `PWR_GD` is telemetry only; shutdown is via `PWR_BUT` one-shot
- "SW2 wired to GLOBAL_EN / hard reset" → SW2 is now `PWR_BUT` graceful power key
- "PM-06 fix" as the final threshold — PM-06 is superseded by R14 threshold reversal
- Any reference to `PMIC_EN` glitch concern — resolved by R14 raising threshold above MCP121T

---
## Next Steps
1. Continue board-by-board sanity check: **Controller Board** (next).
2. After all boards confirmed: launch **Rotor detailed design review cycle** (R58+).
3. Target two consecutive clean passes → INC-25 + checkpoint 011.
