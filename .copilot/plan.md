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

A full system BOM deep-dive audit was completed (checkpoint 036). 13 RGB rocker switches are
still unified to one Marquardt 1800 series SPDT family, but component confirmation is now being
reworked from `.copilot/components-todo.md`, which has grown beyond the original TBD-only list
into a combined supplier-verification table plus full BOM coverage checklist so non-TBD items are
not silently skipped. Connector verification has started there, with J_DSI1, J_CFG / J_I2C,
J_SERVO, and J_FAN already marked verified. A first-cut custom **Electronics review
engineer** agent has also been added under `.github/agents/` to steer future hardware-document
reviews away from software-centric assumptions. That agent prompt was then tested successfully by
driving a general-purpose review agent with the new instructions; direct by-name invocation should
be re-checked in a fresh session.

---

## Review Cycle Process

**Standard Review Cycle:** All design document changes must pass through this review process.

### Tools
1. **markdownlint** — syntax/formatting check
2. **Electronics review engineer agent** — hardware-focused technical review

### Review Cycle Rules
1. **2 consecutive clean passes required** — both lint AND electronics review must be clean
2. **Material technical issues count as findings** — any issue flagged by the electronics review 
   agent (CRITICAL, SIGNIFICANT, or CLARITY issues) requires investigation and resolution
3. **Fixes trigger new review** — any fix applied to resolve findings resets the clean-pass 
   counter to zero; must achieve 2 clean consecutive runs after all fixes
4. **Agent invocation**: Use the "Electronics review engineer" custom agent with specific files 
   and clear scope (e.g., "Review Settings Board Design_Spec and Board_Layout for technical 
   consistency, sourcing feasibility, and manufacturing realism")
5. **Review scope**: Focus on component specifications, I²C/electrical topology, BOM accuracy, 
   datasheet alignment, and sourcing/manufacturing risks — not software or style issues

### Review Workflow
```
Round N: Run lint + electronics review
  ↓
  Clean? 
    YES → Increment clean-pass counter (0→1 or 1→2)
      ↓
      Counter = 2? → ✅ REVIEW CYCLE COMPLETE
      Counter = 1? → Run Round N+1
    NO → Apply fixes
      ↓
      Reset clean-pass counter to 0
      ↓
      Run Round N+1
```

**Current Status:** Full system review cycle complete (R15 clean pass #2 of 2, checkpoint 042).

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

## Full System Review Cycle Status

A full system deep-dive review cycle was run (R1–R13+). Target: 2 consecutive clean passes.

| Round | Result | Notes |
|-------|--------|-------|
| R1 | 21 findings | NPN/PNP, 3V3_ENIG, ERA R_ILIM, LINK-BETA cleanup |
| R2 | 19 findings | NPN→PNP propagation, 5V_MAIN ghost, R3 ERA/ERJ |
| R3 | 8 findings | ERA R_ILIM in CertEvidence, R20/R26 Stator, DEC-033 |
| R4 | 9 findings | R20/R26 prose propagation across 4 files |
| R5 | 10 findings | SYS_RESET_N stale, SERVO_HOME duplicates, attribution |
| R6 | 1 finding | SYS_RESET_N in CI row of Rotor/Board_Layout.md |
| R7 | 2 findings | DEC-015 pin table, DEC-031 Net Effect, Bank-Beta inventory |
| R8 | ✅ CLEAN | Pass 1 — reset by R10–R12 fixes |
| R9 | 3 false positives | No fixes — known-correct list corrected |
| R10 | 1 finding | Q_BNK transistor names in Settings_Board/Board_Layout.md |
| R11 | 2 findings | SERVO_HOME R_SH1/C_SH1 missing from BOM passive counts |
| R12 | 1 finding | TTD_RETURN in wrong trace-width row in Stator/Board_Layout.md |
| R13 | ✅ CLEAN | **Pass 1 of 2** (post-R10/R11/R12) |
| **R14** | 1 low-value clarity issue | Generic TPS25980 wording in Boards_Overview; corrected |
| **R15** | ✅ CLEAN | **Pass 2 of 2** — review cycle complete |

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
| `review-r14` | Review cycle completion after R14/R15 reruns | **done** |
| `electronics-review-agent` | Create first-cut hardware/electronics review agent from generic review pattern | **done** |
| `components-sourcing` | Work through `.copilot/components-todo.md` detailed verification rows plus BOM coverage checklist and confirm valid candidate parts | pending |
| `kicad-setup-docs` | KiCad setup documentation | pending (low priority) |

---

## Immediate Next Steps

1. **Full system review cycle complete** ✅ — R15 achieved clean pass #2 of 2 after the
   `Boards_Overview.md` eFuse wording was tightened to the locked variant.
2. **Electronics review agent tested** ✅ — Direct invocation successful (checkpoint 044). Agent 
   performed Settings Board review with 11 findings (3 CRITICAL, 6 SIGNIFICANT, 2 CLARITY), all 
   legitimate sourcing/documentation issues. Review cycle process formalized in plan.md.
3. **Re-verify components:** `.copilot/components-todo.md` is now the single working workspace for
   component re-verification, with a 30-row supplier-detail table plus a 106-line BOM coverage
   checklist. Treat every populated MPN/distributor field as provisional until manually checked
   unless the row is explicitly marked `VERIFIED`.
   - Priority detail rows 1–5: TBD parts (switches, connectors, R_LED_ANODE)
   - Connector rows already verified: 3 (J_DSI1), 5 (J_CFG / J_I2C), 23 (J_SERVO), 26 (J_FAN)
   - Remaining coverage items marked `NEEDS DETAIL ROW` still need promotion into the detailed table
4. **Apply confirmed parts only after re-verification** — update Consolidated_BOM.md + board BOMs
   once rows are explicitly confirmed.
5. **Address Settings Board findings** — after component verification, apply fixes and re-run 
   review cycle per new Review Cycle Process (expect 1–2 rounds to achieve 2 clean passes).
6. **R_LED_ANODE calculation** — R = (3.3V − Vf) / If once Marquardt LED spec is confirmed.
7. **KiCad project setup** — when schematic phase begins and all TBD parts are locked.

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
5. **Sanitize the synced handoff** so it is safe for version control:
   - Use repo-relative paths or `%USERPROFILE%` placeholders instead of machine-specific absolute paths
   - Do not store raw usernames or Copilot session IDs in committed `.copilot\` content
6. **Verify** all checkpoint artifacts are present in repo-local `.copilot\`
   before declaring the checkpoint complete.

> ⚠️ The session-state folder (`%USERPROFILE%\.copilot\session-state\<id>\`) is ephemeral and
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
- ERJ-3EKF2100V for R3 R_ILIM (wrong, 1% thick-film) → ERA-3ARB2100V (correct, 0.1% thin-film)
- "NPN" / "MMBT3904" for Settings Board colour-rail transistors → PNP MMBT3906
- U_EXP_SW_OUT @ 0x24 (stale artefact — never existed; use U_EXP_SW_IN @ 0x26)
- "Q1"/"Q2"/"Q3"/"Q4" as transistor names on Settings Board → Q_BNK1_G/R, Q_BNK2_G/R
- SYS_RESET_N in JTAG CI (0.127mm) row — it routes at 0.20mm (DEC-031, I²C-sourced)
- TTD_RETURN in 0.20mm signal row — it is a JTAG CI signal (0.127mm)
- R_SH2, C_SH2 (SERVO_HOME) — erroneous duplicates, permanently removed; only R_SH1, C_SH1 exist
- STATOR_CFG_RDY on R26 — correct is R20=STATOR_CFG_RDY; R26=SW2[5] (post-R3/R4)
- Molex 22-23-2261 (→ Amphenol T821126A1S100CEU), Molex 22-23-2161 (→ BHR-16-VUA)
- Würth 61300511021 / 61301011021 (→ RS1-05-G / RS1-10-G), C50950 / C2337 (JDB headers)
- 22F cells, 33F bank, 21.7 s hold-up — stale pre-Abracon values; correct = 25F cells / 50F bank / ≥33.5 s
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
- Settings Board topology: PNP MMBT3906 for colour-rail switching; emitter → 3V3_ENIG,
  collector → LED colour rail; GPIO LOW = transistor ON (active-low drive)
- Settings Board transistors: Q_BNK1_G, Q_BNK1_R, Q_BNK2_G, Q_BNK2_R (functional names)
- Settings Board I²C expanders: U_EXP_SW_IN @ 0x26 (reads switches), U_EXP_LED @ 0x27
  (drives LEDs + colour rails). U_EXP_SW_OUT @ 0x24 is a STALE ARTEFACT — never use.

### Open Work Items (OWI)

- OWI-001: Test coupons per board
- OWI-002: PAS definitions per board
- OWI-003: VHDL pseudo-code and CPLD config plans
- OWI-018: ENIG rib clearway bonding pad
- Deferred: ERA-3ARB2672V / ERA-3ARB1002V MOQ issue (R14/R15 LTC3350)
