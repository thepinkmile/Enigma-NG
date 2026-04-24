<overview>
The session ran a full system-wide design review cycle across all 35 active Enigma-NG design documents, following completion of the Rotor-specific review cycle (checkpoint 019). The goal was to catch all cross-system inconsistencies before the user's manual final review. The approach was iterative: deep-dive review agent → fix agent → repeat until 2 consecutive clean passes. Nine rounds were run (R1–R9); R8 and R9 were both clean, closing the cycle at checkpoint 020. The user then identified two errors introduced by the review cycle itself (wrong eFuse MPN, wrongly removed R1 package), which are being corrected now.
</overview>

<history>

1. **User returned from being out and asked about the JLCPCB single-side manufacturing problem for the Rotor**
   - This had been left as an open question at checkpoint 018
   - User proposed splitting the rotor into two boards (Board A and Board B), connected by IDC headers
   - This would give the rotor its structural thickness to support the aluminium shroud
   - Discussion covered: rotor diameter ~Ø100mm (matching original Enigma), 1.5cm total thickness, dual-track Gray encoder possibility, shroud as aluminium "dish" bearing mechanism
   - Decided: Ø92mm PCBs, Ø100mm shroud outer, keyed IDC J_INT (Würth 61201221721, 2×11 22-pin), Board A = top (EPM570, U1 FDC2114, SW1/SW2), Board B = bottom (U2/U3 FDC2114, SW3)
   - Mechanical specs added to `design/Mechanical/Rotor/Design_Spec.md` (created)
   - STGC adder logic confirmed to live entirely in CPLD VHDL; result available via ALTERA_VIRTUAL_JTAG USER0 UDR (DEC-027, FR-ROT-09)
   - Design_Log updated with DEC-028 (split two-board rotor decision)
   - Checkpoint 019 created (commit `4f38141`)
2. **User confirmed ready for review cycles, then requested full system review (not just Rotor)**
   - All boards complete — appropriate time for cross-system sign-off
   - Launched full system review across 35 files
3. **Full system review R1 — 27 issues found, fixed (commit `5fd19a8`)**
   - EPM570 (not EPM240) for Stator/Rotor in Power_Budgets and Cert_Evidence
   - FDC2114RGER (not AS5600) in Power_Budgets and Cert_Evidence
   - PWR_GD (GPIO 27): corrected to telemetry-only in Controller/Design_Spec and DEC-025
   - 4.644V threshold (not 4.64V) in 7 locations
   - GLOBAL_EN/PMIC_EN → PWR_GD in PM Design_Spec (5 occurrences)
   - Reflector R1 package "0603" removed — **THIS WAS AN ERROR** (see corrections below)
   - Rotor sensor gap: 0.5mm ±0.15mm (was ~0.5–1mm)
   - GUI_App JTAG: EPM240 ×6 + EPM570 ×31
   - Controller Mechanical: ERF8 connector (was FTSH)
   - Controller Design_Spec §9.3: L6 removed from 3V3_ENIG power layer
4. **Full system review R2 — 7 issues, fixed (commit `318bf85`)**
   - PMIC_EN residuals (5 more occurrences)
   - Power_Management Phase 3: gpio-shutdown removed (PWR_GD NOT a shutdown trigger)
   - Cert_Evidence §7.1: qty=6 Encoder only; §7.2 added for EPM570 (31 devices)
5. **Full system review R3 — 8 issues, fixed (commit `464a1fa`)**
   - Cert_Evidence §7.2 family: MAX II (was incorrectly written as MAX V)
   - PM Board_Layout LINK-ALPHA pin 48: PWR_BUT (was GND) in table + ASCII diagram
   - ENC_IN[0:5] direction: Stator→CTRL corrected in Controller/Board_Layout (LINK-BETA), Maintenance_Guide, Design_Log DEC-015
6. **Full system review R4 — completed overnight, result lost to compaction; re-read next morning**
   - 7 issues: DIAGNOSTIC BANK-BETA ENC_IN miss, pin 48 GND count footers (×2), Controller §2.1 pin summary, README (LDO MPN, supercap config, LDO load figures)
   - Fixed (commit `20e6ba0`)
7. **Full system review R5 — 28 issues, fixed (commit `066b2b5`)**
   - **eFuse MPN: TPS259804ONRGER → TPS259807ONRGER** — **THIS WAS AN ERROR** (see corrections)
   - Supercap: TPLH-2R7/22WR12X31 (THT) → SCMT32C156PRBA0 (SMD) across 3 files
   - J_INT: 2×12 24-pin → 2×11 22-pin across 15 locations
   - README comprehensive overhaul (PoE util, layer count, ideal-diode, CPLD, dims, sensor)
8. **Full system review R6 — 9 issues, fixed (commit `5e1baa1`)**
   - README: battery max 16.8V→16.4V; OR-FET SISS22DN→CSD17483F4T; JTAG buffer correction; 37-key→64-key; 3.5mm→6.35mm jacks
   - Mechanical/Rotor/Design_Spec: J_INT 2×12→2×11 (missed by R5)
   - Design_Log DEC-028: J_INT 2×12→2×11 (body + impact)
   - Boards_Overview §12 Stator: ~2.2A → ~2.11A
9. **Full system review R7 — 4 issues, fixed (commit `eb260d5`)**
   - README: eFuse range 17V→16.9V; Roadmap items 2 and 4 stale; GUI_App 2.2A→2.11A
10. **Full system review R8 — CLEAN ✅ (first consecutive clean pass)**
11. **Full system review R9 — CLEAN ✅ (second consecutive clean pass)**
    - Review cycle closed
    - Checkpoint 020 created and committed (`b6ad5ca`)
12. **User reviewed changes and identified two errors introduced by the review cycle**
    - **Error 1**: TPS259807ONRGER is the NO-OVLO variant. TPS259804ONRGER is the silicon-fixed 16.9V OVLO variant. The R5 "fix" was wrong — revert to TPS259804ONRGER.
    - **Error 2**: Reflector R1 0603 package designation was valid (standing rule allows 0402 or 0603; 0603 was a deliberate specification). R1 removal was wrong — restore 0603.
    - Fix agent `revert-efuse-r1-fixes` launched (running)
    - User also requested a full parts list with supplier PNs and datasheet links

</history>

<work_done>

Files modified during full system review cycle (R1–R7):
- `design/Electronics/Power_Budgets.md` — EPM570, FDC2114RGER
- `design/Standards/Certification_Evidence.md` — FDC2114RGER, §7.1/§7.2, MAX II, eFuse MPN (pending revert)
- `design/Electronics/Controller/Design_Spec.md` — PWR_GD telemetry, §9.3 L6, §2.1 pin 48
- `design/Electronics/Controller/Board_Layout.md` — ENC_IN direction (LINK-BETA + DIAGNOSTIC BANK-BETA), pin 48 GND count
- `design/Design_Log.md` — DEC-015, DEC-025, DEC-028 J_INT, eFuse MPN (pending revert)
- `design/Electronics/Power_Module/Design_Spec.md` — 4.644V, PWR_GD, eFuse MPN (pending revert)
- `design/Electronics/Power_Module/Board_Layout.md` — pin 48 PWR_BUT, GND count footer
- `design/Software/Linux_OS/Power_Management.md` — 4.644V, PWR_GD, Phase 3 removed
- `design/Electronics/Consolidated_BOM.md` — 4.644V, PWR_GD, R1 package, supercap MPN, J_INT, eFuse MPN (pending revert)
- `design/Electronics/Reflector/Design_Spec.md` — R1 0603 removed (pending restore)
- `design/Electronics/Rotor/Board_Layout.md` — sensor gap, J_INT 2×11
- `design/Electronics/Rotor/Design_Spec.md` — sensor gap, J_INT 2×11
- `design/Software/GUI_App/Design_Spec.md` — EPM240/EPM570, 2.11A
- `design/Mechanical/Controller/Mechanical_Design.md` — ERF8 connector
- `design/Mechanical/Rotor/Design_Spec.md` — J_INT 2×11
- `design/Guides/Maintenance_Guide.md` — ENC_IN direction
- `design/Electronics/Boards_Overview.md` — 2.11A Stator
- `README.md` — comprehensive overhaul (LDO, supercap, CPLD, dims, sensor, keyboard, jacks, roadmap)
- `.copilot/checkpoints/020-full-system-review-complete-r8.md` — created
- `.copilot/checkpoints/index.md` — entry 020 added
- `.copilot/plan.md` — updated with review complete status, J_INT corrected

Current commit trail:
| Hash | Description |
|------|-------------|
| `4f38141` | Checkpoint 019 |
| `5fd19a8` | R1 fixes (27) |
| `318bf85` | R2 fixes (7) |
| `464a1fa` | R3 fixes (8) |
| `20e6ba0` | R4 fixes (7) |
| `066b2b5` | R5 fixes (28) |
| `5e1baa1` | R6 fixes (9) |
| `eb260d5` | R7 fixes (4) — HEAD of design changes |
| `b6ad5ca` | Checkpoint 020 |

**Currently in progress:**
- Agent `revert-efuse-r1-fixes` running — reverting TPS259807→TPS259804 and restoring Reflector R1 0603 package
- User also requested full parts list with supplier PNs and datasheet links (not yet compiled)

</work_done>

<technical_details>

**eFuse MPN — CRITICAL CORRECTION:**
- TPS259804ONRGER = silicon-fixed 16.9V OVLO ← CORRECT for this design
- TPS259807ONRGER = NO OVLO variant ← WRONG, must never be used
- Catalog PNs for TPS259804ONRGER: Mouser=595-TPS259804ONRGER, DigiKey=296-TPS259804ONRGERCT-ND, JLCPCB=C2878936
- The functional description ("16.9V silicon-fixed OVLO") is correct — only the MPN was wrong
- Previous session memories were contradictory on this. User's datasheet check is authoritative.

**Reflector R1 package:**
- R1 = 22Ω, 0603, ERJ-3EKF2200V — package IS specified as 0603 (valid per standing rule)
- Standing rule: 0402 or 0603 acceptable; 0603 was deliberately chosen
- Do NOT remove the 0603 designation in any future review

**PWR_GD architecture (confirmed correct):**
- MCP121T-450E output on GPIO 27; telemetry-only (HIGH when 5V_MAIN ≥ 4.50V)
- NOT a shutdown trigger; Power_Management Phase 3 = "Not applicable"
- Active shutdown: LTC3350 /INTB → MIC1555 U15 → Q5 BSS138 → PWR_BUT 3.01s one-shot

**J_INT connector (confirmed correct):**
- Würth 61201221721 = 2×11, 22-pin keyed IDC, 2.54mm pitch
- Signal allocation pins 1–22 only; pin 11=TDO A→B; 15-16=SW3[4:5]; 17-18=SDA/SCL; 19-22=SW3[0:3]
- Pins 23 and 24 (GND) were spurious — correctly removed

**Supercap (confirmed correct):**
- Tecate SCMT32C156PRBA0 (22F/2.7V, SMD) — was TPLH-2R7/22WR12X31 (THT) before R5
- 6× in 2S3P = 33F/5.4V; hold-up ≥21.7s
- DigiKey/Mouser/JLCPCB PNs currently marked (TBD) — user to verify

**LTC3350 threshold:**
- 4.644V (R14=28.7kΩ ERA-3ARB2872V, R15=10kΩ ERA-3ARB1002V) — confirmed correct

**ENC_IN[0:5] direction:**
- Stator→CTRL (CM5 input); was incorrectly stated as CTRL→Stator in 4 files — all corrected

**Battery voltage:**
- Max = 16.4V (4.1V/cell × 4S); eFuse OVLO trip = 16.9V (0.5V engineering margin above BMS max)

**Known-correct stale value list (must never reappear):**
- TPS7A8333P/PRMWR, LMQ61460ARUMR, AS5600, TPS259807ONRGER (for eFuse), TPLH-2R7/22WR12X31, SISS22DN, LTC4412, 74LVC125A per-rotor, PMIC_EN, GLOBAL_EN, 17V OVLO, 4.64V threshold, ~2.2A LDO, 37-key, 3.5mm jacks, 163mm shell, De Bruijn sensors, 2×12 24-pin J_INT, EPM240 on Stator/Rotor

**Review cycle process:**
- 2 consecutive clean passes required (lint + content)
- markdownlint: `.\node_modules\.bin\markdownlint.cmd --fix "design/**/*.md"` then without `--fix`
- Pre-existing acceptable MD013 warnings: User_Manual.md:134, Global_Routing_Spec.md:72 only
- `.copilot/` is gitignored but tracked via `git add -f`

</technical_details>

<important_files>

- `design/Electronics/Power_Module/Design_Spec.md`
  - Primary board spec for PM; contains eFuse MPN (pending revert to TPS259804), 4.644V threshold, shutdown path, PWR_GD
  - Modified: eFuse MPN (revert in progress), PMIC_EN→PWR_GD, 4.644V
- `design/Electronics/Consolidated_BOM.md`
  - Master BOM for all 35 files; eFuse row pending revert; R1 row pending 0603 restore; supercap updated to SCMT32C156PRBA0
  - Key rows: line 37 (eFuse), line 75 (22Ω R1), line 67 (supercap), line 104 (J_INT)
- `design/Standards/Certification_Evidence.md`
  - Compliance evidence; §7.1 EPM240 qty=6, §7.2 EPM570 qty=31 (both MAX II); eFuse MPN pending revert; OA-01 entry
  - Key sections: §3.2 eFuse, §7.1/§7.2 CPLD, OA-01
- `design/Electronics/Reflector/Design_Spec.md`
  - Reflector board spec; R1 0603 package pending restore in DR-REF-04 and BOM row
  - Key lines: ~24 (FR-REF-04), ~33 (DR-REF-04), ~173 (BOM R1 row)
- `design/Design_Log.md`
  - All design decisions; eFuse MPN pending revert in DEC-005 rationale; DEC-028 J_INT corrected
  - Key entries: DEC-005 (eFuse), DEC-015 (ENC_IN), DEC-025 (PWR_GD), DEC-027 (Virtual JTAG), DEC-028 (split rotor)
- `design/Electronics/Rotor/Design_Spec.md`
  - Split two-board rotor; J_INT 2×11 22-pin; FDC2114RGER U2/U3/U4; EPM570 CPLD; STGC/RBGC patterns
  - Key sections: §1 overview, DR-ROT-11, §3.4 J_INT signal allocation
- `design/Mechanical/Rotor/Design_Spec.md`
  - Rotor mechanical spec (created this session); Ø92mm PCB, Ø100mm shroud, 1.5cm total thickness, bearing mechanism, aluminium shroud
  - §6 J_INT: 2×11 22-pin now correct
- `README.md`
  - Project overview; comprehensively updated: LDO TPS75733KTTRG3, CSD17483F4T OR-FETs, SN74LVC2G125DCUR on Extension Boards, Ø92mm/Ø100mm, FDC2114RGER sensing, 64-key, 6.35mm jacks, eFuse 16.9V range
- `.copilot/checkpoints/020-full-system-review-complete-r8.md`
  - Checkpoint for completed review cycle; full round-by-round summary
- `.copilot/plan.md`
  - Canonical session state; updated with review complete status; J_INT corrected to 2×11

</important_files>

<next_steps>

**Immediately in progress:**
- Agent `revert-efuse-r1-fixes` is running — will revert TPS259807→TPS259804ONRGER (+ catalog PNs) and restore Reflector R1 0603 package across 5 files; read result when notified

**After revert agent completes:**
- Read agent result, verify all changes applied correctly
- Compile full parts list with supplier PNs and datasheet links as requested by user
  - Format: all ICs, passives, connectors, mechanical parts
  - Include: MPN, Mouser PN, DigiKey PN, JLCPCB PN where known, datasheet URL
  - Flag any (TBD) PNs for user validation (notably supercap Tecate SCMT32C156PRBA0 catalog PNs)
- Note for user: Tecate SCMT32C156PRBA0 DigiKey/Mouser/JLCPCB PNs are currently (TBD) — need verification
- Note for user: JLCPCB PN C2878936 for TPS259804ONRGER should be verified against JLCPCB catalogue

**Pending longer-term:**
- `kicad-setup-docs` todo (KiCad project setup documentation)
- OWI-019: Relocate STGC_Generator.py to `design/Electronics/Rotor/`
- OWI-020: GUI App — DEC-027/FR-ROT-09 cross-reference
- OWI-021: Complete 6 Mechanical stub files (Encoder, Stator, Reflector, Extension, JDB, PM)
- User manual review of all design files before final sign-off

</next_steps>
