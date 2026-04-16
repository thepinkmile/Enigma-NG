# Checkpoint 020 — Full System Review Complete (R8+R9 Clean)

**Date:** 2026-04-13  
**Session:** <sanitized-session-id>  
**HEAD commit:** `eb260d5`

---

## Summary

Full system design review cycle across all 35 active Enigma-NG design documents completed with
two consecutive clean passes (R8 + R9). Nine rounds of review were run in total (R1–R9); R8 and
R9 were both clean. The design is now ready for user manual review before final sign-off.

---

## Rounds Summary

| Round | Issues Found | Files Changed | Commit |
|-------|-------------|---------------|--------|
| R1 | 27 | 12 | `5fd19a8` |
| R2 | 7 | 3 | `318bf85` |
| R3 | 8 | 5 | `464a1fa` |
| R4 | 7 | 4 | `20e6ba0` |
| R5 | 28 | 8 | `066b2b5` |
| R6 | 9 | 5 | `5e1baa1` |
| R7 | 4 | 2 | `eb260d5` |
| R8 | 0 ✅ | — | — |
| R9 | 0 ✅ | — | — |

---

## All Issues Fixed (R1–R7 cumulative)

### R1 (27 issues)
- EPM570 (not EPM240) for Stator/Rotor in Power_Budgets and Cert_Evidence
- FDC2114RGER (not AS5600) in Power_Budgets and Cert_Evidence
- PWR_GD (GPIO 27) corrected to telemetry-only in Controller/Design_Spec and Design_Log DEC-025
- 4.644V threshold (not truncated 4.64V) in 7 locations
- GLOBAL_EN/PMIC_EN → PWR_GD throughout PM Design_Spec
- Reflector R1 package designation removed from FR-REF-04, DR-REF-04, BOM
- Rotor sensor gap: 0.5mm ±0.15mm (was ~0.5–1mm)
- GUI_App JTAG library: EPM240 ×6 + EPM570 ×31
- Controller Mechanical: ERF8-020-05.0-S-DV-K-TR (was FTSH)
- Controller Design_Spec §9.3: L6 removed from 3V3_ENIG power layer

### R2 (7 issues)
- PMIC_EN removed from 3 remaining locations in PM Design_Spec
- PMIC_EN removed from 2 locations in Power_Management.md
- Power_Management Phase 3: gpio-shutdown removed (PWR_GD is NOT a shutdown trigger)
- Cert_Evidence §7.1: qty=6 Encoder only; §7.2 added for EPM570T100I5N (31 devices)

### R3 (8 issues)
- Cert_Evidence §7.2 family: MAX II (was MAX V)
- PM Board_Layout LINK-ALPHA pin 48: PWR_BUT (was GND) — table + ASCII diagram
- ENC_IN[0:5] direction: Stator→CTRL in Controller/Board_Layout, Maintenance_Guide, Design_Log

### R4 (7 issues)
- Controller/Board_Layout DIAGNOSTIC BANK-BETA ENC_IN[0:5]: Stator→CTRL (R3 miss)
- Controller/Board_Layout + PM/Board_Layout: pin 48 removed from GND count footers
- Controller/Design_Spec §2.1: Pins 45–48 description updated (GND→PWR_BUT)
- README: TPS7A8333P→TPS75733KTTRG3; LDO load 1.85A/61.7%→2.11A/70.4%;
  supercap 4× 2S2P ~14s → 6× 2S3P 33F ≥21.7s

### R5 (28 issues)
- eFuse TPS259804ONRGER → TPS259807ONRGER (+ catalog PNs) across 4 files
- Supercap TPLH-2R7/22WR12X31 (THT) → SCMT32C156PRBA0 (SMD) across 3 files
- J_INT: 2×12 24-pin → 2×11 22-pin across Rotor/Design_Spec (×7), Rotor/Board_Layout (×5), BOM (×1)
- README: PoE util 70.8%→73.9%; Controller 4-layer→6-layer 2oz; ideal-diode LTC4412→LM74700-Q1;
  Rotor CPLD EPM240→EPM570; PCB dims 122mm/163mm→Ø92mm/Ø100mm; sensor TCRT5000L→FDC2114RGER;
  Encoder CPLD C5→I5 (industrial grade)

### R6 (9 issues)
- README: battery max 16.8V→16.4V; OR-FET SISS22DN→CSD17483F4T; JTAG buffer 74LVC125A
  on every rotor→SN74LVC2G125DCUR on Extension Boards; keyboard 37-key→64-key; plugboard 3.5mm→6.35mm ¼″
- Mechanical/Rotor/Design_Spec: J_INT 2×12 24-pin → 2×11 22-pin (missed by R5)
- Design_Log DEC-028: J_INT 2×12→2×11 in body + impact table
- Boards_Overview §12 Stator: ~2.2A → ~2.11A

### R7 (4 issues)
- README: eFuse range 17V→16.9V; Roadmap item 2: 163mm/De Bruijn→Ø100mm/FDC2114RGER;
  Roadmap item 4: 37-key Passive→64-key Hold-to-Shift
- GUI_App/Design_Spec §3: Stator current 2.2A→2.11A

---

## Files Modified This Review Cycle

- `design/Electronics/Power_Budgets.md`
- `design/Standards/Certification_Evidence.md`
- `design/Electronics/Controller/Design_Spec.md`
- `design/Electronics/Controller/Board_Layout.md`
- `design/Design_Log.md`
- `design/Electronics/Power_Module/Design_Spec.md`
- `design/Electronics/Power_Module/Board_Layout.md`
- `design/Software/Linux_OS/Power_Management.md`
- `design/Electronics/Consolidated_BOM.md`
- `design/Electronics/Reflector/Design_Spec.md`
- `design/Electronics/Rotor/Board_Layout.md`
- `design/Electronics/Rotor/Design_Spec.md`
- `design/Software/GUI_App/Design_Spec.md`
- `design/Mechanical/Controller/Mechanical_Design.md`
- `design/Mechanical/Rotor/Design_Spec.md`
- `design/Guides/Maintenance_Guide.md`
- `design/Electronics/Boards_Overview.md`
- `README.md`

---

## Current State

- Full system review cycle: **COMPLETE** (R8 + R9 both clean)
- All 35 active design documents verified consistent
- Ready for user manual review before final sign-off

## Pending Work

- `kicad-setup-docs`: KiCad project setup documentation (not started)
- OWI-019: Relocate STGC_Generator.py to `design/Electronics/Rotor/`, update algorithm
- OWI-020: GUI App — add DEC-027/FR-ROT-09 cross-reference when GUI spec is worked
- OWI-021: Complete 6 Mechanical stub files (Encoder, Stator, Reflector, Extension, JDB, PM)
