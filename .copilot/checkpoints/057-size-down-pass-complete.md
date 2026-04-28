# Checkpoint 057 — Size-down pass complete

## Status
All size-down pass changes from the deep-review cycle are fully implemented, linted, and ready to commit.

## Work Completed
1. **Samsung CL21B106KAYQNNE introduced** (10µF X7R 25V 0805)
   - Replaces CL31B106KBHNNNE (10µF X7R 50V 1206) everywhere in system
   - Voltage margins confirmed: 25V÷3.3V=7.6× (3V3_ENIG), 25V÷5.0V=5.0× (5V_MAIN) — both exceed 2× mandatory
   - Markdown datasheet generated: design/Datasheets/Samsung-1276_CL21B1-datasheet.md
   - Board specs updated: AM, CTL, ENC, EXT, REF, ROT, STA

2. **Stator resistor consolidation to 0402**
   - R2–R41: 10kΩ 0603 ERJ-3EKF1002V → 0402 ERJ-2RKF1002X (19 resistors)
   - R7–R38: 75Ω 0603 ERJ-3EKF75R0V → 0402 ERJ-2RKF75R0X (18 resistors)
   - ERJ-3EKF75R0V eliminated from BOM (was Stator-only)

3. **Consolidated BOM updated**
   - Line 73: CL21B106KAYQNNE 0805 25V, CTL=10 (was 5), Total=212 (was 207)
   - Line 90: ERJ-3EKF1002V STA=0, Total=22 (was 41)
   - Line 91: ERJ-2RKF1002X STA=19, Total=180 (was 161)
   - Line 93: ERJ-3EKF75R0V row removed
   - Line 93 (new): ERJ-2RKF75R0X STA=18, Total=28 (was 10)
   - §2 Common Passives: 10uF Bulk and 10k Pull notes updated
   - §4b Stator Panel Switch: R16-R26 updated to 0402/ERJ-2RKF1002X
   - AM module C5 updated to CL21B106KAYQNNE 0805 25V

4. **Global_Routing_Spec.md §3 updated**
   - Bulk Entry Bank Rule: 50V/1206 → 25V (0805)
   - Voltage margin notes added (2× derating rule confirmed)
   - Standard part reference added with supplier codes

## Files Changed
- design/Electronics/Consolidated_BOM.md
- design/Standards/Global_Routing_Spec.md
- design/Electronics/Actuation_Module/Design_Spec.md
- design/Electronics/Controller/Design_Spec.md
- design/Electronics/Encoder/Design_Spec.md
- design/Electronics/Extension/Design_Spec.md
- design/Electronics/Reflector/Design_Spec.md
- design/Electronics/Rotor/Design_Spec.md
- design/Electronics/Stator/Design_Spec.md
- design/Datasheets/Samsung-1276_CL21B1-datasheet.md
- design/Datasheets/_generated_markdown_inventory.json

## Lint Status
All files pass markdownlint with exit code 0.
