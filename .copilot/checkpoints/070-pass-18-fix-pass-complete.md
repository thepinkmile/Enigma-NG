# Checkpoint 029 — Pass 18 Fix Pass Complete

## Status
All Pass 18 fix-pass edits applied, linted clean, and committed.

## Changes Applied

### Critical (assembly-blocking)
- **Rotor_26_Char_Design.md**: Fixed CRITICAL wiring error — `CH1–CH3 tied to GND via 100 kΩ`
  replaced with correct dummy LC tank reference (18µH + 33pF per TI app note; BOM L5–L8, C24–C27)
- **System_Architecture.md**: Added `LED_nPWR` to J3 description (line 86) and pin allocation list
  (`4 × GND` → `3 × GND`)

### High (schematic-blocking)
- **Stator/Design_Spec.md**: Added R39/R40/R41 — MCP23017 U6/U7/U8 RESET pull-ups (10kΩ 0603 ERJ-3EKF1002V)
- **Settings_Board/Design_Spec.md**: Added R78/R79/R80 — MCP23017 U1/U2/U3 RESET pull-ups (10kΩ 0402 ERJ-2RKF1002X)
- **Power_Module/Design_Spec.md**:
  - `C26-C32` → `C26–C30` (removed ghost C31/C32 for non-existent U9/U10)
  - Added C47–C51 (LMQ61460A BST caps ×2, STUSB4500 CC filter caps ×2, TPS75733 NR cap ×1)
  - Added R41–R51 (LMQ61460A FB dividers, EN/PG pull-ups, LM74700 gate series resistors)
  - Fixed R3 bulk note — R3 is 0.1% Thin-Film ILIM; now correctly separated from R1/R2 1% Thick-Film group

### Medium
- **Consolidated_BOM.md**:
  - Line 85 (10nF): PM — → 1, Total 1 → 2 (C51)
  - Line 92 (10kΩ 0603): STA 16 → 19, Total 38 → 41 (R39/R40/R41)
  - Line 93 (10kΩ 0402): PM 7 → 9, SBD — → 3, Total 155 → 160 (R43/R44 + R78/R79/R80)
  - Added 3 new PM resistor rows: ERJ-2RKF5232X 52.3kΩ (×2), ERJ-2RKF1003X 100kΩ (×4), ERJ-2RKF10R0X 10Ω (×3)
  - Section 3a: `C24-C39, C43-C46` → `C24-C30, C33-C39, C43-C50`; added CTL C12 and PM C51 rows
- **Controller/Design_Spec.md**:
  - Added C12 row — 100nF 0402 VDD_GPIO_REF decoupling (CL05B104KB5NNNC / C1525)
  - Added footnote after GPIO matrix clarifying PWR_BUT (CM5 PMIC HW pin) and LED_nPWR (CM5 pin 95 HW output → PM SW2 green LED)
- **Rotor/Design_Spec.md**: Removed stale "Category B pending" labels for resonant parts (now fully sourced)

## Deferred Items
- INA219 RC filter resistors (Stator U2 + PM U12) — BLOCKED pending value decision
- Size-down pass: bulk cap 1206→0805 voltage margin check; Controller/Settings 0603→0402
- Category C sourcing (battery-connector-final-review) — awaiting supplier emails
- Extension / Reflector / AM / JDB deep-review — pending
