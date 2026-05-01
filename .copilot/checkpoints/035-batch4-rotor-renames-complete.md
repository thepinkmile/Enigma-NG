# Checkpoint 035 — Batch 4 Rotor H_→J7–J10 Renames Complete

## Status
All Batch 4 (Rotor) H_→J7–J10 renames applied and lint-clean. Pass 2 BOM ordering work is now complete across all 11 boards.

## What Was Done

### Files Updated This Checkpoint

- `design/Electronics/Rotor/Board_Layout.md`
  - Intro paragraph: H_SW3/H_PWR/H_JTAG/H_SENS → J10/J7/J8/J9
  - Board A ASCII diagram inner face: H_SW3 M/H_PWR F/H_JTAG F/H_SENS M → J10 M/J7 F/J8 F/J9 M
  - Board A component summary table rows renamed to J7–J10
  - Board B ASCII diagram inner face: H_SW3 F/H_PWR M/H_JTAG M/H_SENS F → J10 F/J7 M/J8 M/J9 F
  - Board B component summary table rows renamed to J7–J10
  - §6.1 dedicated device pins table: H_JTAG → J8 (all 4 signal rows)
  - §6.2 GP signal groups: H_SW3 → J10, H_SENS → J9
  - Variant/reserve policy: H_SENS → J9

- `design/Software/CPLD_Logic/Rotor_Logic.md`
  - Line 14: H_SENS bus → J9 bus
  - Line 32: H_SENS bus → J9 bus
  - Section heading: `## 3. H_SENS I²C Bus` → `## 3. J9 I²C Bus`
  - Body text lines 70–75: all H_SENS → J9

- `design/Mechanical/Rotor/Design_Spec.md`
  - Section 6 "Internal Header Assembly": H_SW3/H_PWR/H_JTAG/H_SENS → J10/J7/J8/J9 throughout

- `design/Design_Log.md` (DEC-028)
  - Lines 1180–1181: header name description → J10/J7/J8/J9
  - Line 1228: Impact §3.4 BOM note → J10/J7/J8/J9; "BOM unified into single table"
  - Line 1235: Consolidated_BOM Impact → J10/J7/J8/J9

- `design/Electronics/Consolidated_BOM.md`
  - Rotor Board A rows: H_SW3→J10, H_PWR/H_JTAG→J7–J8, H_SENS→J9
  - Rotor Board B rows: H_SW3→J10, H_PWR/H_JTAG→J7–J8, H_SENS→J9
  - Descriptions updated to reflect role (return-map select for J10, power/JTAG for J7–J8, sensor for J9)

## Complete Pass 2 BOM Work — Summary

All 11 boards processed and lint-clean:

| Board | Status |
| :--- | :--- |
| Reflector | ✅ U2–U4 range merge |
| Controller | ✅ J14–J15, U5–U6 range merges |
| Extension | ✅ U3–U5, U7–U9 range merges |
| Stator | ✅ R reorder/merges; VCCINT 1.8V removed |
| Settings Board | ✅ Q1–Q6 merge; SW1–SW10 merge |
| Actuation Module | ✅ R reorder; U1 merged into main BOM |
| JTAG Daughterboard | ✅ C10–C12 repositions/merge |
| Encoder | ✅ D1/R1–R6 repositions |
| Power Module | ✅ Full reorder + range merges + FB1 added |
| Rotor | ✅ Unified BOM; H_→J7–J10 renames across all 6 files |
| Consolidated BOM | ✅ FB1 row added; Rotor rows updated to J7–J10 |

## Remaining Pass 2 Work

1. **Confirm Stator U10–U12 range merge** with user (all TPD4E05U06QDQARQ1 — same MPN as U5–U9)
2. **Settings_Board → User_Settings_Module rename** (~17 files + Design_Log DEC entry)
3. **Mark CSD17578Q5A and TPS25751DREFR footprints as downloaded** in Consolidated_BOM

## Key Technical Details

- H_→J mapping confirmed: H_PWR→J7, H_JTAG→J8, H_SENS→J9, H_SW3→J10
- Rotor BOM unified (V-scored single-board manufacture assumption)
- Banned manufacturers: Murata (blanket), TDK (military involvement)
- FB1 approved part: TE BMC-Q2AY0600M (2-2176748-1); DigiKey 1712-2-2176748-1CT-ND; Mouser 279-BMC-Q2AY0600M

## Git Status

Staged by user after prior session. Changes since staging not yet committed.
Awaiting "Let''s lock this in" for next commit.
