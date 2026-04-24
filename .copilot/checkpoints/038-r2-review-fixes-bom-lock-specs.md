# Checkpoint 038 — R2 review fixes, BOM 🔒 markers, Required Specs column
## Date
2026-04-15
## Session
<sanitized-session-id>
## Overview
R2 deep-dive review (19 findings) was applied across 8 files. The `components-todo.md` file
was rewritten with a "Required Specs" column for all 21 TBD items. Confirmed-part (🔒) markers
were added throughout `Consolidated_BOM.md` to prevent future review agents from silently
changing owner-confirmed part numbers.
## Commits
| SHA | Description |
|-----|-------------|
| `bdb14eb` | R2 fixes: NPN→PNP, LINK-BETA ghost 5V_MAIN, 3V3_SYSTEM→3V3_ENIG, ERA-3ARB2100V |
| `79c8f9d` | BOM 🔒 markers: policy note, §9 legend, all confirmed rows, §4b/c/d/§5 Conf columns |
## Work Done
### R2 Fixes (commit `bdb14eb`) — 19 findings across 4 families
- **NPN→PNP (F1–F8):** Settings_Board/Design_Spec.md §1, §2, GPIO table (×4), §4 note;
  Settings_Board/Board_Layout.md Zone-D label, Placement Notes, §5 description, §7 table header.
  "Effect when HIGH" → "Effect when LOW" throughout.
- **Ghost 5V_MAIN on LINK-BETA (F9–F13):** DEC-031 in Design_Log.md incorrectly recorded
  5V_MAIN pins added to LINK-BETA; removed from Controller/Design_Spec.md §2.2 and §8.3,
  Stator/Design_Spec.md §4.2 (sentence + callout box removed), Design_Log.md DEC-031 corrected.
- **3V3_SYSTEM retired net (F14–F15):** Mechanical/Main_Enclosure/Design_Spec.md lid display
  power path and Controller/Design_Spec.md §8.5 J_DSI1 note.
- **R3 R_ILIM MPN (F16–F19):** ERJ-3EKF2100V (1% thick-film, wrong) → ERA-3ARB2100V
  (0.1% thin-film, correct) in Power_Module/Design_Spec.md (×3) and Consolidated_BOM.md.
  Also fixed R18–R21/C25 column misalignment in BOM §9 table.
### BOM 🔒 Markers (commit `79c8f9d`)
- Added policy note to Consolidated_BOM.md Overview section
- Added 🔒 definition to §9 legend
- Added 🔒 to Notes column for all 19 confirmed rows in §9 multi-distributor table
- Fixed R18–R21 and C25 column misalignment (value moved from Package col to Part col)
- Added `Conf` column to §4b (Power Module connectors), §4c (Stator), §4d (Settings Board),
  §5 (Controller connectors) tables
### components-todo.md (local only — never commit)
- Rewrote with Required Specs column for all 21 items:
  - Item #1: Marquardt 1800 SPDT (panel-mount RGB, ≥12V DC, ≥0.5A, black body)
  - Item #2: SW_CFG_APPLY (SPST NO momentary, ≥3.3V, ≥50mA)
  - Item #3: J_DSI1 (15-pin 1.0mm ZIF/FPC, 4-lane MIPI DSI)
  - Item #4: R_LED_ANODE (0603 ≤1%, value = (3.3V−Vf)/If)
  - Item #5: B4B-PH-K-S (4-pin 2.0mm pitch THT)
  - Items 6–7: ERA precision resistors (0.1% tolerance, 25ppm/°C TCR)
  - Items 8–20: ERJ 0402/0603 resistors (value, tol, package)
  - Item #21: Supercap 25F 2.7V THT radial
  - Item #18 (ERA-3ARB2100V R3): 210Ω 0.1% thin-film 0603 — DigiKey TBD, JLCPCB TBD
## Key Technical Notes
- **PNP topology confirmed:** MMBT3906, emitter → 3V3_ENIG, collector → LED rail; GPIO LOW = ON.
- **LINK-BETA pins 12–17:** ALL SPARE. No 5V_MAIN was ever added. DEC-031 corrected.
- **ERA-3ARB2100V** (not ERJ): R_ILIM for TPS259804ONRGER eFuse. Mouser 667-ERA-3ARB2100V.
- **BOM 🔒 policy:** Future review agents must NOT change 🔒 rows without owner confirmation.
## Next Steps (at time of checkpoint)
- Run R3 deep-dive review
- Continue review cycle until 2 consecutive clean passes
