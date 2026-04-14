# Enigma-NG Session Plan

> Canonical state: `.copilot/plan.md` in the repository root (gitignored).
> Update this file at the end of each session or at meaningful milestones.
> At the start of a new session, read this file plus relevant checkpoints in `.copilot/checkpoints/`.

---

## Overview

All board detailed designs are functionally complete. In session bb01fc15 (checkpoints 028–033):
supercap upgraded to 2S4P Abracon 25F/37.5F bank (DEC-029/030/031), CM5 Virtual Keyboard
feature added with MCP23017 ×2 + PCA9685 on Stator (DEC-031), and `design/Mechanical/` was
fully restructured from PCB-named stubs to assembly-based folders. A full system review cycle
is needed to validate the Stator + Controller changes from DEC-031.

Review rule: 2 consecutive clean passes — lint (`markdownlint`) AND deep-dive content.

---

## Board Design Status

| Board | Status |
|-------|--------|
| Power Module | ✅ Complete |
| Stator | ✅ Complete (updated: DEC-031 CM5 key injection — checkpoint 033) |
| Reflector | ✅ Complete |
| Extension | ✅ Complete |
| JDB | ✅ Complete |
| Controller | ✅ Complete (updated: GPIO/LINK-BETA freed for expanders — checkpoint 033) |
| Encoder | ✅ Complete |
| Rotor | ✅ Complete (design docs + 4-header J_INT + POS_B — checkpoint 027) |

---

## Full System Review Status

**Pending** — Stator and Controller changed in checkpoint 033; review needed before declaring
design complete.

---

## Todos

| ID | Title | Status |
|----|-------|--------|
| `kicad-setup-docs` | KiCad setup documentation | pending |
| `full-system-review` | Full system review cycle post-DEC-031 (2 clean passes) | pending |

---

## Immediate Next Steps

1. **Full system review cycle** — deep-dive R1+R2 clean passes to validate Stator/Controller
   changes from DEC-031 (CM5 key injection) and all mechanical restructure cross-refs.
2. **STGC_Generator.py relocation** — move to `design/Electronics/Rotor/`; update algorithm
   (relaxed unique-only constraint; current Gray single-bit-change is too strict).
3. **KiCad project setup** — create project structure, import footprints, begin schematic capture.
4. **Item J** — Marquardt 1800 illuminated power switch (RGB LED) — MPN deferred.

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

This rule exists because the TPS259804ONRGER eFuse has been erroneously swapped to TPS259807
(different variant, no OVLO feature) in multiple review rounds without datasheet verification.
The same risk applies to any component where the MPN encodes a variant-selecting digit.

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
- "100kΩ" / "18nF" for SYNC RC delay, "0.1%" for R_FSET or R_DLY
- "SN74LVC1G14" without DBVRQ1 suffix, SOIC-8 for TPS2065C, VQFN for TPD4E05U06
- 0402 for Reflector R1 22Ω, JLC04161H-7628 in Controller/Board_Layout, TPD12S016 anywhere
- "RST" as signal/net name, "Binary input from Keyboard CPLD" for ENC_IN
- SOT-23 (3-pin) for AP2331W, SOT-25 for AP2331W (use SOT-23-5)
- "L4 / L6" for Logic/I2C in CTL Design_Spec §9.3
- L1–L4 enclosure rib clearway in PM Design_Spec §1, L4 (Bottom) for PM Data Plate
- [L1/L4 2oz Copper] in PM Board_Layout, L6 = Diagnostic/Data Plate in CTL Board_Layout §9
- 9.05A peak load, 2.20A LDO load, 75.4% LMQ utilisation, 76.2% PoE cold-start (corrected)
- "accepted exception" for LMQ or PoE cold-start (zero exceptions remain)
- "Extension board: NO U1 buffer" — WRONG; Extension U1 IS correct and present
- ENC_B (→ POS_B), Würth 61201221721, J_INT as "2×11 IDC" / "22-pin keyed IDC"
- Molex 22-23-2261 (→ Amphenol T821126A1S100CEU), Molex 22-23-2161 (→ BHR-16-VUA)
- Würth 61300511021 / 61301011021 (→ RS1-05-G / RS1-10-G), C50950 / C2337 (JDB headers)
- **22F cells, 33F bank, 21.7 s hold-up** — stale pre-Abracon values; correct = 25F / 37.5F / ≥24.8 s
- "Passive components only" for Extension §5 — WRONG; U1 (SN74LVC2G125DCUR) is active IC on Extension
- **2S3P, 37.5F bank (3P), 6 cells, 24.8s, 5W load, 3 min charge** — stale pre-2S4P; correct = 2S4P, 50F bank, 8 cells
- **R14=28.7kΩ, threshold 4.644V** — stale pre-transient-fix; correct R14 per DEC-030
- **Old mechanical paths**: design/Mechanical/Keyboard/, design/Mechanical/Plugboard/ (replaced by HID_Assembly/ + Plugboard_Assembly/)
- **CM5 GPIO 4–15 and 26 driving ENC_IN/OUT/SYS_RESET_N directly** — stale; all migrated to MCP23017 expanders
- **SYS_RESET_N on CM5 GPIO 26** — stale; now U_EXP2 GPA[7] on Stator MCP23017
- **PCA9685 @ 0x40 or any address other than 0x60** — correct address is 0x60 (A5=HIGH, A4–A0=GND)

### Key Design Decisions

- All capacitors: X7R dielectric
- JTAG CI traces: 0.127mm (5 mil) targeting 50Ω on JLC04161H-7628
- CPLD: EPM240T100I5N (industrial, −40°C to +100°C) for Encoder; EPM570T100I5N for Stator/Rotor
- Controller J1 + J2 = ERF8 female (both) for slide-in assembly
- U7 EN is active-LOW (EN LOW = on); pull-down to GND
- Extension board U1 buffers TCK/TMS every 5 rotors (NOT per-rotor buffering)
- TPS259804ONRGER = silicon-fixed 16.9V OVLO eFuse (no external OVLO pin; R3 = R_ILIM = 210Ω)

### Open Work Items (OWI)

- OWI-001: Test coupons per board
- OWI-002: PAS definitions per board
- OWI-003: VHDL pseudo-code and CPLD config plans
- OWI-018: ENIG rib clearway bonding pad
- Deferred: SW1 vintage switch research, ERA-3ARB2672V/ERA-3ARB1002V MOQ issue (R14/R15 LTC3350)
- Deferred: Item J — Marquardt 1800 illuminated power switch (RGB LED) MPN

> Canonical state: `.copilot/plan.md` in the repository root (gitignored).
> Update this file at the end of each session or at meaningful milestones.
> At the start of a new session, read this file plus relevant checkpoints in `.copilot/checkpoints/`.

---

## Overview

All board detailed designs are functionally complete. Full system review cycle (35 files, 9
rounds, 90 cumulative fixes) completed with R8+R9 both clean — checkpoint 020. The Rotor design
was substantially updated in session bb01fc15 (checkpoints 014–019): split two-board architecture
(Board A input / Board B output, Ø92mm each, keyed IDC J_INT 2×11 22-pin), dual-track capacitive
encoder, STGC/RBGC patterns corrected, U4 FDC2114RGER added for N=26 5th sensor, full
Mechanical/Rotor spec with tolerance table. User to manually review all design files before
declaring the design complete.

Review rule: 2 consecutive clean passes — lint (`markdownlint`) AND deep-dive content.

---

## Board Design Status

| Board | Status |
|-------|--------|
| Power Module | ✅ Complete (checkpoint 011) |
| Stator | ✅ Complete (checkpoint 013/016) |
| Reflector | ✅ Complete |
| Extension | ✅ Complete |
| JDB | ✅ Complete |
| Controller | ✅ Complete (checkpoint 012) |
| Encoder | ✅ Complete (R56+R57 clean — checkpoint 009) |
| Rotor | ✅ Complete (R4+R5 clean — checkpoint 019) |

---

## Full System Review Status

**COMPLETE — checkpoint 020** (R8+R9 clean, 9 rounds total, 90 cumulative fixes across 18 files)

---

## Todos

| ID | Title | Status |
|----|-------|--------|
| `kicad-setup-docs` | KiCad setup documentation | pending |
| `user-manual-review` | User manual review of all design files before final sign-off | pending |

---

## Immediate Next Steps

1. **User manual review** — manually review all design files and provide observations before declaring design complete.
2. **KiCad setup documentation** (`kicad-setup-docs` todo).
3. **Remaining OWIs** as agreed (see list below).

## Checkpoint Procedure

Every checkpoint MUST include ALL of the following steps (in order):

1. **Write checkpoint file** to `.copilot/checkpoints/NNN-short-title.md` in the **repository**.
2. **Update checkpoint index** at `.copilot/checkpoints/index.md` in the **repository**.
3. **Update `.copilot/plan.md`** in the **repository** to reflect current state.
4. **Copy any new agent-prompt files** to `.copilot/agent-prompts/` in the **repository**.
5. **Verify** all items present in `C:\_DATA_\Repositories\github\Enigma-NG\.copilot\` before declaring complete.

> The session-state folder is ephemeral. The repository `.copilot\` folder is the canonical persistent store.

---

## Critical Notes

### Standard Review File List (28 files)

Core files + Rotor variant files:

- design/Electronics/Consolidated_BOM.md
- design/Design_Log.md
- design/Electronics/Power_Budgets.md
- design/Electronics/Power_Module/Design_Spec.md + Board_Layout.md
- design/Electronics/Stator/Design_Spec.md + Board_Layout.md
- design/Electronics/Reflector/Design_Spec.md + Board_Layout.md
- design/Electronics/Extension/Design_Spec.md + Board_Layout.md
- design/Electronics/JTAG_Daughterboard/Design_Spec.md + Board_Layout.md
- design/Electronics/Controller/Design_Spec.md + Board_Layout.md
- design/Electronics/Encoder/Design_Spec.md + Board_Layout.md
- design/Electronics/Rotor/Design_Spec.md + Board_Layout.md
- design/Electronics/Rotor/Rotor_26_Char_Design.md
- design/Electronics/Rotor/Rotor_64_Char_Design.md
- design/Electronics/Investigations/JTAG_Integrity.md
- design/Standards/Global_Routing_Spec.md
- design/Guides/Maintenance_Guide.md

### Lint Process

- PATH refresh: `$env:PATH = [System.Environment]::GetEnvironmentVariable("PATH","Machine")+";"+[System.Environment]::GetEnvironmentVariable("PATH","User")`
- Run: `.\node_modules\.bin\markdownlint.cmd --fix "design/**/*.md"` then without `--fix`.
- Pre-existing MD013 lint errors (acceptable — do not flag): User_Manual.md:134, Global_Routing_Spec.md:72.

### JTAG Topology (CRITICAL — agents repeatedly get this wrong)

- TCK/TMS/TDI via **BtB connectors** (ERM8/ERF8 Samtec 0.8mm pitch) through entire rotor stack.
  NO ribbon cables used for JTAG within the rotor stack.
- JTAG chain terminates at the **Reflector**. Reflector R1 (22Ω) = end-of-chain TDO damping.
- Reflector J4 → Stator J7 ribbon: pin 15=TTD_RETURN (JTAG), pins 3–14=ENC_IN/OUT (plugboard
  config for Stator CPLD — NOT JTAG extension).
- Extension U1 (SN74LVC2G125DCUR) re-buffers TCK/TMS every 5-rotor group — CORRECT, NEVER REMOVE.
- Stator R7–R15 (75Ω) and Encoder R7–R8 are for encoder RIBBON CABLE ports (J4/J5/J6) ONLY.

### Extension U1 Buffer (NEVER REMOVE)

- Extension board has U1 (SN74LVC2G125DCUR) + C6 (0.1µF bypass), FR-EXT-01/02, DR-EXT-04/05/06.
- Consolidated BOM: SN74LVC2G125DCUR EXT=1, Total=2.
- Design_Spec is authoritative; BOM must match it.

### Key Correct Values

- GPIO 20=SW_LED_CTRL, GPIO 24=POE_STAT (active-low) — correct in ALL files
- Peak load 8.76A; LDO 2.11A / ~0.46W / 30% headroom; LMQ 73.0%; PoE 73.9%; zero exceptions
- CSS2H shunt build qty: 3 (JDB=1, STR=1, PM=1)
- Consolidated BOM: SN74LVC2G125DCUR JDB=1, EXT=1, Total=2
- Consolidated BOM: 0.1µF X7R 0402 PM=15, Total=509
- Consolidated BOM: MIC1555YM5-TR PM=2, BSS138 PM=2
- Consolidated BOM: EPM240T100I5N = 6 (Encoder only); EPM570T100I5N = 31 (Stator + 30 Rotors)
- Consolidated BOM: FDC2114RGER = 30 (U2, all rotors) + 30 (U3, N=64 rotors) + TBD (U4, N=26 rotors)
- LTC3350 BACKUP threshold: 4.644V (R14=28.7kΩ ERA-3ARB2872V)
- SW2 wired to PWR_BUT (graceful power key), NOT GLOBAL_EN
- Link-Alpha pin 48: PWR_BUT (was GND)
- PWR_GD (GPIO 27) = rail-health telemetry only; does NOT trigger shutdown
- Primary shutdown: LTC3350 /INTB → U15 MIC1555 → Q5 BSS138 → PWR_BUT (3.01 s LOW)
- DEC-025 (last before session bb01fc15): CM5 shutdown mechanism (Software category)
- DEC-026: Capacitive encoder replaces AS5600 (FDC2114RGER, STGC track patterns) — superseded by DEC-028
- DEC-027: Virtual JTAG USER0 UDR for rotor position readback (FR-ROT-09)
- DEC-028: Split two-board rotor architecture (Board A + Board B, keyed IDC J_INT)

### Rotor-Specific Correct Values (NEVER flag as errors)

- **Two-board split:** Board A (input, Ø92mm) + Board B (output, Ø92mm); 15mm total; 11.8mm inner gap
- Board A: EPM570T100I5N U1, FDC2114RGER U2 (0x2A), FDC2114RGER U4 (0x2B, N=26 only), SW1, SW2, J1–J3 ERM8 male
- Board B: FDC2114RGER U3 (0x2B, N=64 only; DNP N=26), SW3, J4–J6 ERF8 female
- J_INT: Würth 61201221721, 2×11 22-pin keyed IDC; pin 11=TDO A→B; pins 15–16=SW3[4:5]; pins 17–18=SDA/SCL; pins 19–22=SW3[0:3] B→A
- FDC2114RGER U2 addr 0x2A (N=64: ch0–2=bits[5:3]; N=26: ch0–3=STGC bits[3:0])
- FDC2114RGER U4 addr 0x2B ch0=STGC bit[4] — N=26 Board A only
- FDC2114RGER U3 addr 0x2B ch0–2=bits[2:0] — N=64 Board B only (U3 and U4 mutually exclusive)
- Sensor pads at r=44mm on PCB flat face; capacitive gap 0.5mm ±0.15mm (bearing-controlled)
- N=26 track (K=5): `00000100011001010011101111` — all 26 5-bit windows unique
- N=64 dual-track RBGC (corrected R1 — Track B Bit 0 and Bit 1 were wrong):
  - A5: `0000000000000000000000000000000011111111111111111111111111111111`
  - A4: `0000000000000000111111111111111111111111111111110000000000000000`
  - A3: `0000000011111111111111110000000000000000111111111111111100000000`
  - B2: `0000111111110000000011111111000000001111111100000000111111110000`
  - B1: `0011110000111100001111000011110000111100001111000011110000111100`
  - B0: `0110011001100110011001100110011001100110011001100110011001100110`
- CPLD XOR decode: B5=G5, B4=B5⊕G4, B3=B4⊕G3, B2=B3⊕G2, B1=B2⊕G1, B0=B1⊕G0
- SW1 (6-bit, Board A): ring setting, mod-N adder entirely in CPLD VHDL
- SW2 (6-bit, Board A): [4:0]=map index, [5]=direction
- SW3 (6-bit, Board B): [4:0]=map index, [5]=direction
- 21 UFM maps stored in EPM570 UFM; UFM size = 21 × 384 bits = 8,064 bits
- J1–J3 ERM8 male (input side Board A); J4–J6 ERF8 female (output side Board B)
- FR-ROT-09: ALTERA_VIRTUAL_JTAG megafunction, USER0 UDR, 6-bit effective position
- TDO in J_INT travels A→B (CPLD on Board A → J4 connector on Board B)

### Stale Values (must NEVER reappear)

- TPS259807ONRGER, TPS259803ONRGER, TPS25980RPWR, TPS7A8333PRMWR, LMQ61460ARUMR
- C21397, C15281, C2688, 1276-1935-1-ND, WM7843-ND, C841785
- ERA-3ARB2323V, ERA-3ARB2672V (old R14), ERJ-2RKF8200X
- WSON-8 2×2mm, WSON-12, SOIC-8 for TPS2065C, VQFN for TPD4E05U06, SOT-23-6 for buffer
- 9.05A peak, 2.20A LDO, 75.4% LMQ, 76.2% PoE, 27% LDO headroom, "accepted exception"
- GPIO 20=POE_STAT or GPIO 24=SW_LED_CTRL (swapped — both wrong)
- "RST" as signal/net name; + prefix on net names
- "Extension: no U1 buffer" or "passive pass-through" — WRONG
- Pull-up on U7 EN (must be pull-DOWN to GND)
- TPD12S016, TPD4E1U06DBVR
- 4.40V as LTC3350 backup threshold (correct: 4.644V)
- "SW2 wired to GLOBAL_EN / hard reset" (SW2 = PWR_BUT)
- "PWR_GD triggers shutdown" (telemetry only)
- 0.1µF X7R 0402 PM=14 or Total=508 (correct: PM=15, Total=509)
- MIC1555 PM=1 (correct: PM=2); BSS138 PM=1 (correct: PM=2)
- EPM240T100I5N on Rotor or Stator (correct: EPM570T100I5N)
- AS5600 anywhere on Rotor (replaced by FDC2114RGER)
- "Single magnet" or "diametrically magnetised" for Rotor position sensor
- "Ø100mm" for Rotor PCB (correct: Ø92mm; shroud outer is Ø100mm)
- "de Bruijn" as an active N=64 encoder pattern (replaced by RBGC; de Bruijn only in DEC-028 rationale/history)
- Old N=64 Track B patterns: Bit 1 as period-16 `0011111100001111` repeating, Bit 0 as simple alternating `01`
- "FDC2114 reads all 5 STGC sensors from U2" (impossible — 4 channels max; U4 added for 5th)
- "U4 NOT POPULATED" for N=26 builds (U4 IS populated for N=26)
- "U3 populated for N=26" (U3 DNP for N=26)
- DIR/CLK on J_INT pins 15–16 (correct: SW3[4:5] B→A)
- Single-board rotor (correct: two-board split)

### Key Design Decisions

- All capacitors: X7R dielectric
- JTAG CI traces: 0.127mm (5 mil) targeting 50Ω — documented exception to Global_Routing_Spec
- Net names: NO + prefix (e.g. `5V_MAIN` not `+5V_MAIN`)
- Controller J1+J2: both ERF8 female (slide-in assembly convenience)
- U7 EN: active-LOW, pull-down to GND
- Extension U1 buffers TCK/TMS every 5 rotors (not per-rotor)
- PWR_BUT = primary shutdown trigger + manual power key; 3.01 s one-shot from U15 MIC1555
- Rotor position encoder: single-track capacitive, FDC2114RGER, STGC patterns
- Rotor position readback: ALTERA_VIRTUAL_JTAG USER0 UDR (DEC-027, FR-ROT-09)

### Open Work Items (OWI)

- OWI-001: Test coupons (break-off PCB) per board
- OWI-002: PAS definitions per board
- OWI-003: VHDL pseudo-code and CPLD config plans
- OWI-018: ENIG rib clearway bonding pad
- OWI-019: STGC_Generator.py — relocate to `Rotor/`, update to relaxed unique-only algorithm
- OWI-020: GUI App Design_Spec — add cross-reference to DEC-027/FR-ROT-09 for position display
- OWI-021: Mechanical stub files — complete Encoder, Stator, Reflector, Extension, JDB, Power_Module mechanical specs
- Deferred: SW1 vintage switch research; CM5 PWR_BUT timing thresholds (verify at schematic capture)