# Checkpoint 039 — R3–R5 review fixes
## Date
2026-04-15
## Session
<sanitized-session-id>
## Overview
Three review rounds (R3, R4, R5) were run as part of the ongoing 2-consecutive-clean-pass
review cycle. R3 found 8 findings; R4 found 9 (propagation of R3 fix); R5 found 10
(SYS_RESET_N stale on LINK-BETA, duplicate SERVO_HOME passives, cross-board attribution).
All fixed and committed. Review cycle counter reset to 0.
## Commits
| SHA | Description |
|-----|-------------|
| `92fbc0c` | R3 fixes: NPN straggler, ERA R_ILIM in CertEvidence, R20/R26 STATOR_CFG_RDY, 3V3_ENIG DEC-033 |
| `7a29bb4` | R4 fixes: propagate R20/R26 STATOR_CFG_RDY renumbering to all prose |
| `eecc42e` | R5 fixes: SYS_RESET_N/Sniffer stale refs, SERVO_HOME BOM, U_EXP_SW_IN board attr |
## Work Done
### R3 — 8 findings
- Settings_Board/Design_Spec.md: last "NPN" straggler in U_EXP_LED table heading
- Certification_Evidence.md: ERJ-3EKF2100V (wrong) → ERA-3ARB2100V in §3.2 table and
  OA-01 closure (2 locations)
- Stator/Design_Spec.md: J_CFG JLCPCB PN C131342 (3-pin, wrong) → TBD
- Design_Log.md DEC-033: 3V3_SYSTEM → 3V3_ENIG
- Stator/Design_Spec.md BOM: R20=STATOR_CFG_RDY, R21–R26=SW2[0:5] (was R20/R26 swapped)
- Consolidated_BOM.md §4b: matching BOM row correction + summary count update
### R4 — 9 findings (same class — propagation)
R3 BOM renumbering not propagated to prose:
- Stator/Design_Spec.md: FR-STA-09, DR-STA-11, §3 Bank 2 (×3)
- Stator/Board_Layout.md: J_CFG placement note, U_EXP4 placement note (×2)
- Settings_Board/Design_Spec.md: §3 Bank 1/2 intro, §3 Bank 2 (×2)
- Design_Log.md DEC-032: Decision §3 and Rationale (×2)
### R5 — 10 findings
- Controller/Design_Spec.md: SYS_RESET_N stale in §2 overview, §2.2 LINK-BETA pin group,
  §8.3 JTAG shield label (×3)
- Controller/Board_Layout.md: LINK-BETA pin table + ASCII block diagram (stale Sniffer Bus,
  GPIO, Encryption labels) → SPARE (×2)
- Stator/Design_Spec.md: "Reset" in Data In, "12-bit Sniffer data" in Data Out, SYS_RESET_N
  in JTAG trace rule (×3); duplicate SERVO_HOME passives R_SH2+C_SH2 removed (×1)
- Reflector/Design_Spec.md: U_EXP_SW_IN @ 0x26 attributed to Stator → Settings Board (×1)
## Key Technical Notes
### Stator pull-down resistors (canonical post-R3/R4)
- R16–R19 = SW1[0:3] (DIP Bank 1)
- R20 = STATOR_CFG_RDY
- R21–R26 = SW2[0:5] (DIP Bank 2)
- System total 10kΩ 0603 = 31
### SYS_RESET_N (DEC-031)
- Virtual I²C signal driven by Stator U_EXP2 GPA[7] @ 0x21
- NOT a hardware pin on LINK-BETA; NOT a JTAG CI trace
- Routes at 0.20mm standard logic width
- LINK-BETA pins 8, 12–17, 19–24 = ALL SPARE
### SERVO_HOME (Stator only)
- One switch SW3, pull-up R_SH1 (10kΩ 1% 0402), debounce C_SH1 (100nF X7R 0402)
- R_SH2 and C_SH2 were erroneous duplicates — permanently removed
## Next Steps (at time of checkpoint)
- Run R6 deep-dive review
- Continue review cycle until 2 consecutive clean passes
