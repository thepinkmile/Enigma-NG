# Enigma-NG Session Plan

> Canonical state: `.copilot/plan.md` in the repository root (gitignored).
> Update this file at the end of each session or at meaningful milestones.
> At the start of a new session, read this file plus relevant checkpoints in `.copilot/checkpoints/`.

---

## Overview

All board detailed designs are complete. Recent sessions added three new features:
- **Virtual Keyboard / CM5 Key Injection** (DEC-028, checkpoints 032–033)
- **Settings Board** — panel-mount illuminated RGB rocker switches replacing Stator DIP switches,
  with CM5 I²C override via U_EXP4 (DEC-032, checkpoints 034–036)
- **DSI1 Display Provision** on Controller Board — ZIF/FPC connector for optional lid touchscreen
  (DEC-033, checkpoint 035)

A full system BOM deep-dive audit was completed (checkpoint 036). All board BOMs and the
Consolidated BOM are consistent. 13 RGB rocker switches unified to Marquardt 1800 series SPDT
(MPN TBD — user to research).

Review rule: 2 consecutive clean passes — lint (`markdownlint`) AND deep-dive content.

---

## Board Design Status

| Board | Status |
|-------|--------|
| Power Module | ✅ Complete |
| Stator | ✅ Complete (DIP switches removed; J_CFG to Settings Board DEC-032) |
| Reflector | ✅ Complete |
| Extension | ✅ Complete |
| JDB | ✅ Complete |
| Controller | ✅ Complete (DSI1 provision added DEC-033) |
| Encoder | ✅ Complete |
| Rotor | ✅ Complete |
| Settings Board | ✅ Design_Spec + Board_Layout complete (switch MPN TBD) |

---

## TBD Parts (User to Research)

| Ref | Description | Constraint |
| :--- | :--- | :--- |
| SW1 (PM) + SW_B1/B2 ×12 (SBD) | Marquardt 1800 SPDT latching rocker, RGB LED, black body | All 13 must be same MPN |
| SW_CFG_APPLY | Panel-mount SPST NO momentary pushbutton | Quality feel preferred |
| R_LED_ANODE ×4 | 0603 anode current-limiting resistors | Value blocked on switch LED Vf/If |
| J_I2C / J_CFG | JST B4B-PH-K-S 4-pin 2.0mm — JLCPCB PN | C131342 is 3-pin (wrong); 4-pin PN needed |
| J_DSI1 | 15-pin 1.0mm ZIF/FPC (CM5 DSI1) | Verify CM5 DSI1 pinout at schematic phase |

---

## Todos

| ID | Title | Status |
|----|-------|--------|
| `deep-dive-review` | Full system deep-dive review cycle (2 clean passes, post-DEC-032/033) | pending |
| `kicad-setup-docs` | KiCad setup documentation | pending (low priority) |

---

## Immediate Next Steps

1. **Deep-dive review cycle** — full system review with datasheet access; fix findings; repeat
   until 2 consecutive clean passes (lint + content).
2. **Part searches** (user) — Marquardt 1800 SPDT MPN; SW_CFG_APPLY; J_CFG 4-pin JLCPCB PN;
   J_DSI1 ZIF/FPC.
3. **R_LED_ANODE calculation** — R = (3.3V − Vf) / If once Marquardt LED spec known.
4. **KiCad project setup** — when schematic phase begins.

---

## Checkpoint Procedure

Every checkpoint MUST include ALL of the following steps (in order):

1. **Write checkpoint file** to `.copilot/checkpoints/NNN-short-title.md` in the **repository**.
   Include: overview, work done, commits, technical decisions, corrected known-correct list,
   open questions, and next steps.
2. **Update checkpoint index** at `.copilot/checkpoints/index.md` in the **repository** with the
   new entry.
3. **Update `.copilot/plan.md`** in the **repository** to reflect current state, todos, and
   immediate next steps. Ensure stale values list and JTAG topology notes are current.
4. **Copy any new agent-prompt files** (`.copilot/agent-prompts/*.txt`) to the **repository**
   if they were created in the session-state folder instead.
5. **Verify** all four items are present in `C:\_DATA_\Repositories\github\Enigma-NG\.copilot\`
   before declaring the checkpoint complete.

> ⚠️ The session-state folder (`C:\Users\izzyo\.copilot\session-state\<id>\`) is ephemeral and
> tied to a single session ID. The repository `.copilot\` folder is the canonical persistent
> store. Always write to (or sync to) the repository folder.

---

## Critical Notes

### Lint Process

- PATH refresh: `$env:PATH = [System.Environment]::GetEnvironmentVariable("PATH","Machine")+";"+[System.Environment]::GetEnvironmentVariable("PATH","User")`
- Run: `.\node_modules\.bin\markdownlint.cmd --fix "design/**/*.md"` then without `--fix` to confirm clean.
- Pre-existing MD013 lint errors (acceptable — cannot auto-fix): Consolidated_BOM lines 195-196,
  PM Design_Spec line 489, User_Manual line 134, Power_Management line 215, Global_Routing_Spec line 72.

### ⚠️ Part Number Change Rule (MANDATORY — review agents must follow this)

**Before proposing or applying ANY component MPN change during a review cycle:**

1. A datasheet for the proposed new MPN MUST exist in `design/Datasheets/`.
2. The agent MUST read that datasheet and verify ALL of the following match the design requirement:
   - Package / footprint (e.g. VQFN-24, VSSOP-8, SOT-23-5)
   - Key electrical parameters (voltage rating, current rating, logic levels, OVLO/UVLO thresholds)
   - Variant identifier (e.g. the `04` in TPS259804 vs `07` in TPS259807)
3. If no datasheet is present for the proposed part → **do NOT make the change**.
   Flag it as: "Proposed MPN change — no datasheet available; requires human verification."
4. If the datasheet exists but any parameter does not match → **do NOT make the change**.
   Flag it with the specific mismatch.

### JTAG Topology (CRITICAL — agents have repeatedly got this wrong)

- TCK/TMS/TDI travel via **BtB connectors** (ERM8/ERF8 Samtec 0.8mm pitch) through entire rotor stack.
  NO ribbon cables used for JTAG within the rotor stack.
- JTAG chain terminates at the **Reflector**. Reflector R1 (22Ω) = end-of-chain TDO damping.
- Reflector J4 → Stator J7 ribbon carries: pin 15=TTD_RETURN (JTAG), pins 3-14=ENC_IN/OUT (plugboard
  config for Stator CPLD — NOT JTAG). The ribbon does NOT extend the JTAG chain.
- Extension U1 (SN74LVC2G125DCUR) re-buffers TCK/TMS every 5-rotor group — CORRECT, INTENTIONAL.
- Stator R7-R15 (75Ω) and Encoder R7-R8 are for encoder RIBBON CABLE ports (J4/J5/J6) ONLY.

### Extension U1 Buffer (NEVER REMOVE)

- Extension board has U1 (SN74LVC2G125DCUR) + C6 (0.1µF bypass), FR-EXT-01/02, DR-EXT-04/05/06.
- Consolidated BOM: SN74LVC2G125DCUR EXT=1 Total=2; 0.1µF X7R 0402 EXT=1 Total=509.
- R43 wrongly removed this. R49-retry tried to remove it again. Both were wrong.
- Design_Spec is authoritative; BOM must match it (not the other way around).

### Connector Conventions

- Male headers on sub/daughterboards (JDB J1/J2, Rotor Board A H_SW3/H_SENS, Rotor Board B H_PWR/H_JTAG)
- Female sockets on main/receiving boards (Controller J_JDB_PWR/JTAG, Rotor Board A H_PWR/H_JTAG, Board B H_SW3/H_SENS)
- Adam Tech PH1-xx-UA = male; RS1-xx-G = female. Same footprint per pin count — confirmed mating pairs.
- RS-Online PNs go in description field, NOT Mouser column.
- Net names NEVER use + prefix: `3V3_ENIG` not `+3V3_ENIG`.
- Controller J1 + J2 = ERF8 female (both) for slide-in assembly.

### Rotor J_INT (4-Header Arrangement — confirmed correct)

- H_SW3 (1×7): Board A=PH1-07-UA male, Board B=RS1-07-G female | SW3[0:5], GND
- H_PWR (1×5): Board A=RS1-05-G female, Board B=PH1-05-UA male | 3V3_ENIG×4, GND
- H_JTAG (1×5): Board A=RS1-05-G female, Board B=PH1-05-UA male | TCK, GND, TMS, GND, TDO
- H_SENS (1×5): Board A=PH1-05-UA male, Board B=RS1-05-G female | SDA, SCL, POS_B[0:2]
- POS_B[0:2] = Track B position bits from FDC2114 U3 on Board B (N=64 only)
- All SMT on outer (top) face; headers on inner (bottom) face manually post-SMT
- Boards mate bottom-to-bottom; tops face outward into shroud

### Stale Values (must NEVER reappear)

- TPS7A8333PRMWR / TPS7A8333P, LMQ61460ARUMR, WSON-8 2×2mm / WSON-12
- C21397, 1276-1935-1-ND, WM7843-ND, C841785, TPS25980RPWR, TPS259807ONRGER
- ERA-3ARB2323V, ERA-3ARB2872V, "0.1% Thin-Film" for R1/R2/R3 on PM
- "adjustable OVLO" for DEC-005, SOT-23-6 for SN74LVC2G125DCUR
- C15281 / C2688 for SN74LVC2G125DCUR, ERJ-2RKF8200X for R26
- "100kΩ" / "18nF" for SYNC RC delay, "0.1%" for R_FSET or R_DLY in Cert_Evidence §3.3.3
- "SN74LVC1G14" without DBVRQ1 suffix, SOIC-8 for TPS2065C, VQFN for TPD4E05U06
- 0402 for Reflector R1 22Ω, JLC04161H-7628 in Controller/Board_Layout, TPD12S016 anywhere
- "RST" as signal/net name (incl. "TDI/RST"), "Binary input from Keyboard CPLD" for ENC_IN
- SOT-23 (3-pin) for AP2331W, SOT-25 for AP2331W (use SOT-23-5)
- "L4 / L6" for Logic/I2C in CTL Design_Spec §9.3, TPD4E1U06DBVR in Design_Log INC-22
- L1–L4 enclosure rib clearway in PM Design_Spec §1, L4 (Bottom) for PM Data Plate
- [L1/L4 2oz Copper] in PM Board_Layout, L6 = Diagnostic/Data Plate (short) in CTL Board_Layout §9
- 9.05A peak load, 2.20A LDO load, 75.4% LMQ utilisation, 76.2% PoE cold-start (all corrected)
- "accepted exception" for LMQ or PoE cold-start (zero exceptions remain in the system)
- "Extension board: NO U1 buffer" — WRONG; Extension U1 IS correct and present
- ENC_B (→ POS_B), Würth 61201221721, J_INT as "2×11 IDC" / "22-pin keyed IDC"
- Molex 22-23-2261 (→ Amphenol T821126A1S100CEU), Molex 22-23-2161 (→ BHR-16-VUA)
- Würth 61300511021 / 61301011021 (→ RS1-05-G / RS1-10-G), C50950 / C2337 (JDB headers)
- 22F cells, 33F bank, 21.7 s hold-up — stale pre-Abracon values; correct = 25F / 37.5F / ≥24.8 s
- 2S3P, 37.5F bank (3P), 6 cells, 24.8s — stale pre-2S4P; correct = 2S4P, 50F bank, 8 cells
- R14=28.7kΩ, threshold 4.644V — stale pre-transient-fix; correct R14 per DEC-030
- Old mechanical paths: design/Mechanical/Keyboard/, design/Mechanical/Plugboard/
- CM5 GPIO 4–15 and 26 driving ENC_IN/OUT/SYS_RESET_N directly — stale; all migrated to MCP23017
- SYS_RESET_N on CM5 GPIO 26 — stale; now U_EXP2 GPA[7] on Stator MCP23017
- PCA9685 @ 0x40 or any address other than 0x60 — correct address is 0x60 (A5=HIGH, A4–A0=GND)
- SW1 / SW2 DIP switches on Stator — REMOVED (replaced by Settings Board DEC-032)
- 2-layer stackup for Settings Board — WRONG; all boards use 4-layer JLC04161H-7628 (Controller = 6-layer)
- SPST for Marquardt 1800 SW1 (Power Module) — WRONG; unified to SPDT with Settings Board switches

### Key Design Decisions

- All capacitors: X7R dielectric
- JTAG CI traces: 0.127mm (5 mil) targeting 50Ω on JLC04161H-7628
- CPLD: EPM240T100I5N (industrial, −40°C to +100°C) for Encoder; EPM570T100I5N for Stator/Rotor
- Net names NEVER use + prefix: `5V_MAIN` not `+5V_MAIN`
- Controller J1 + J2 = ERF8 female (both) for slide-in assembly
- U7 EN is active-LOW (EN LOW = on); pull-down to GND
- Extension board U1 buffers TCK/TMS every 5 rotors (NOT per-rotor buffering)
- TPS259804ONRGER = silicon-fixed 16.9V OVLO eFuse (no external OVLO pin; R3 = R_ILIM = 210Ω)
- All boards 4-layer JLC04161H-7628 / 2oz copper except Controller (6-layer JLC06161H)
- MCP23017 I²C addresses: 0x20 (U_EXP1 STA), 0x21 (U_EXP2 STA), 0x22 (U_EXP4 STA),
  0x26 (U_EXP_SW_IN SBD), 0x27 (U_EXP_LED SBD). All 8 addresses (0x20–0x27) now in use.
- Settings Board LED: green = switch-defined, red = CM5-defined (per bank)
- Marquardt 1800 SPDT rocker: same MPN for all 13 switches (PM SW1 + SBD ×12)
- Settings Board topology: NPN MMBT3904 for colour-rail switching (biasing TBD at schematic phase)

### Open Work Items (OWI)

- OWI-001: Test coupons per board
- OWI-002: PAS definitions per board
- OWI-003: VHDL pseudo-code and CPLD config plans
- OWI-018: ENIG rib clearway bonding pad
- Deferred: ERA-3ARB2672V / ERA-3ARB1002V MOQ issue (R14/R15 LTC3350)
