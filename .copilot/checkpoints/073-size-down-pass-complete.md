# Checkpoint 073 — Size-down pass complete

## Status

All size-down pass changes from the deep-review cycle are fully implemented, linted, and committed.

## What was done this checkpoint

1. **Samsung CL21B106KAYQNNE introduced** (10µF X7R 25V 0805)
   - Replaces CL31B106KBHNNNE (10µF X7R 50V 1206) everywhere in system
   - Voltage margins confirmed: 25V÷3.3V=7.6× (3V3\_ENIG), 25V÷5.0V=5.0× (5V\_MAIN) — both exceed 2× mandatory derating
   - Markdown datasheet generated: `design/Datasheets/Samsung-1276_CL21B1-datasheet.md`
   - Board specs updated: AM, CTL, ENC, EXT, REF, ROT, STA

2. **Stator resistor consolidation to 0402**
   - R2–R41: 10kΩ 0603 ERJ-3EKF1002V → 0402 ERJ-2RKF1002X (19 resistors)
   - R7–R38: 75Ω 0603 ERJ-3EKF75R0V → 0402 ERJ-2RKF75R0X (18 resistors)
   - ERJ-3EKF75R0V completely eliminated from system (was Stator-only)

3. **Consolidated BOM updated**
   - Line 73: description → CL21B106KAYQNNE 0805 25V; CTL corrected 5→10; total 207→212
   - Line 90: ERJ-3EKF1002V STA 19→0, total 41→22
   - Line 91: ERJ-2RKF1002X STA 0→19, total 161→180
   - ERJ-3EKF75R0V row removed
   - ERJ-2RKF75R0X STA `—`→18, total 10→28
   - §2 Common Passives notes updated (10uF Bulk + 10k Pull)
   - §4b Stator Panel Switch: R16–R26 updated to 0402/ERJ-2RKF1002X
   - AM module C5 updated to CL21B106KAYQNNE 0805 25V

4. **Global_Routing_Spec.md §3 updated**
   - Bulk Entry Bank Rule: 50V/1206 → 25V (0805)
   - Voltage margin notes added (2× derating rule confirmed)
   - Standard part reference with supplier codes added

## Commit

`9927b8d` — size-down: replace 1206 50V bulk caps with 0805 25V across all boards; consolidate Stator resistors to 0402

## Remaining open work

- Controller Board: LED resistor BOM consolidation, PWR\_BUT CM5 pin, VDD\_GPIO\_REF decoupling cap, DSI display power
- Category C battery connector sourcing (awaiting supplier emails)
- New-component sourcing todo list (size-down candidates and CRIT items from power module review)
