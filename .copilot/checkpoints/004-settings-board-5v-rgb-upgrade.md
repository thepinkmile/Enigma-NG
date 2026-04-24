# Checkpoint 004 — Settings Board 5V RGB upgrade complete
## Date
2026-04-17
## Overview
Settings Board LED control system upgraded from 3.3V single-color operation to 5V full RGB capability. The existing 3.3V supply was insufficient for proper LED brightness (green/blue LEDs have ~3.0V forward voltage, leaving only 0.3V headroom). The solution adds a second MCP23017 I²C expander (dual-IC architecture), routes 5V_MAIN from Controller Board through Link-Beta to power the LEDs, and recalculates all current-limiting resistors for 5V @ 20mA operation. The upgrade provides full RGB color capability while maintaining a shared color-rail topology that uses only 6 MOSFETs (2 banks × 3 colors) for 12 LEDs.
## Work Done
### Design Architecture
**5V RGB LED Control System:**
- Replaced single U_EXP_LED @ 0x27 with dual MCP23017s:
  - U_LED_B1 @ 0x40 (Bank 1: A2=HIGH, A1=LOW, A0=LOW)
  - U_LED_B2 @ 0x41 (Bank 2: A2=HIGH, A1=LOW, A0=HIGH)
- Added 6× BSS138 MOSFETs for shared color-rail topology (Q_BNK1_R/G/B, Q_BNK2_R/G/B)
- Shared color-rail architecture: 12 LEDs use only 6 MOSFETs (not 36)
  - Individual anode control per LED (HIGH = LED on)
  - Shared cathode rails per bank: BNKx_R, BNKx_G, BNKx_B
  - Low-side N-channel switching to GND
  - Only 1 color active per bank at any time (software enforced)

**5V Power Routing:**
- Source: Controller TPS259804 eFuse 5V_MAIN output (3A capable)
- Link-Beta pins 18, 23: 2× parallel for current sharing (0.5A each = 1.0A total)
- Stator: Pass-through to J_CFG pin 2 (5V_LED) and J_SERVO pin 1 (5V_MAIN)
- Settings Board: 5V_LED rail powers 12× RGB LED anodes via U_LED_B1/B2
- Load budget: 240mA max (12 LEDs × 20mA × 1 color), 1.0A capacity = 4× margin
- Bonus: Solved previously open J_SERVO power issue on Stator Board

**Resistor Calculations (5V @ 20mA):**
- Red: (5.0V - 2.0V) / 0.020A = 150Ω → ERJ-3EKF1500V (Panasonic 1% 0603)
- Green: (5.0V - 3.0V) / 0.020A = 100Ω → ERJ-3EKF1000V (Panasonic 1% 0603)
- Blue: (5.0V - 3.0V) / 0.020A = 100Ω → ERJ-3EKF1000V (same as green)
- Gate: 1kΩ ERJ-2RKF1001X (Panasonic 1% 0402, 6 units)
- Total: 36 LED resistors + 6 gate resistors

**Connector Upgrades:**
- J_CFG (Stator): B4B-PH-K-S → B6B-PH-K-S (4-pin → 6-pin JST PH)
- J_I2C (Settings): B4B-PH-K-S → B6B-PH-K-S (4-pin → 6-pin JST PH)
- Pin assignments: 1=3V3_ENIG, 2=5V_LED, 3=GND (logic), 4=SDA, 5=SCL, 6=GND (LED)
- Dual GND pins: pin 3 for logic return (~80mA), pin 6 for LED return (up to 240mA)
### Files Modified
**Controller/Design_Spec.md:**
- Line 8: Updated Last Updated to 2026-04-17
- Lines 105-106: Link-Beta pins 18, 23 assigned to 5V_MAIN (was SPARE)
- Lines 180-182: I²C address table updated (removed 0x27, added 0x40, 0x41)
- Line 225: GPIO I²C bus device list updated

**Stator/Design_Spec.md:**
- Line 8: Updated Last Updated to 2026-04-17
- Line 56 (DR-STA-14): J_SERVO changed from "5V_SERVO_TBD" to "5V_MAIN"
- Line 59 (DR-STA-17): J_CFG upgraded from 4-pin to 6-pin JST PH, added 5V_LED pin

**Settings_Board/Design_Spec.md:**
- Line 8: Updated Last Updated to 2026-04-17
- Lines 20-26: Overview updated to describe 3× MCP23017s
- Lines 45, 54-60: Functional and design requirements updated
- Lines 192-236: Replaced U_EXP_LED section with U_LED_B1/U_LED_B2 sections
- Lines 242-270: Updated LED Control Logic with RGB color scheme
- Lines 312-337: J_I2C connector upgraded to 6-pin with full pinout
- Lines 348-390: BOM table updated with new component values
- Lines 391-465: Added §10 Power Budget, §11 Component Count Summary, §12 Design Notes

**Consolidated_BOM.md:**
- Line 7: Updated Last Updated to 2026-04-17
- Line 56: BSS138 count: 6 → 8 (SBD: 4 → 6)
- Line 58: MCP23017 count: 5 → 7 (SBD: 2 → 3)
- Lines 270-271: Replaced U_EXP_LED @ 0x27 with U_LED_B1/U_LED_B2
- Line 277: J_I2C connector upgraded to 6-pin
- Line 278: MOSFET count updated (×4 → ×6)
- Lines 281-284: LED resistor values updated (R=150Ω, G/B=100Ω)
- Lines 286-287: Decoupling caps updated for dual ICs
- Line 252: J_CFG connector upgraded
- Line 257: Stator description updated with 5V routing

**components-todo.md:**
- Line 72 (IC018): MCP23017 count 5→7, addresses updated
- Line 108 (T001): BSS138 count 6→8
- Line 111 (T003): Gate resistor count ×4→×6
- Lines 178-180 (R027-R029): Resistor values updated (RECHECK status)
- Line 190 (R051): Blue resistor 100Ω (RECHECK status)
- Line 288: Verification summary: 8 VERIFIED (S001, S002, S004, L001, J022-J025), 98 RECHECK
### Session Artifacts Created
- `.copilot/files/settings-board-5v-rgb-upgrade.md` — Complete design document
- `.copilot/files/5v-rgb-upgrade-changelog.md` — Before/after change summary
- `.copilot/component-types-summary.md` — Component verification tracking
## Commits
**Commit 6b27f3a** — "Settings Board 5V RGB LED upgrade"
- 4 files changed, 203 insertions(+), 85 deletions(-)
- Controller, Stator, Settings Board Design_Spec.md files
- Consolidated_BOM.md
## Key Technical Notes
### Shared Color-Rail Topology
The design uses a shared color-rail topology instead of individual LED control:
- Each LED has individual anode control (MCP23017 GPIO HIGH = LED candidate for illumination)
- All LEDs in a bank share 3 color rails (BNKx_R, BNKx_G, BNKx_B)
- 6 MOSFETs total (Q_BNK1_R/G/B, Q_BNK2_R/G/B) switch color rails to GND
- Only 1 color active per bank at any time (enforced by software)
- This topology saves 30 MOSFETs compared to per-LED switching (36 vs 6)
### Why 5V Was Required
3.3V supply was fundamentally insufficient:
- Green LED Vf ≈ 3.0V, leaving only 0.3V headroom at 3.3V
- Blue LED Vf ≈ 3.0V, same issue
- MCP23017 GPIO limited to 16mA @ 3.3V (need 20mA for proper brightness)
- 5V provides 2.0V headroom for green/blue, proper current regulation
### I²C Address Selection
U_LED_B1 @ 0x40 and U_LED_B2 @ 0x41 chosen to:
- Avoid conflicts with existing devices (0x20-0x27 range)
- Reserve 0x2x range for future expansion
- Use sequential addresses for logical bank grouping
- Place in high address range (A2=HIGH) for clear separation
### CPLD Reload Architecture
Reload signal generated by Stator U_EXP4 @ 0x22, NOT Settings Board:
- CM5 controls reload via I²C write to Stator U_EXP4
- Two trigger modes: user button press OR CM5 programmatic
- Settings Board has no involvement in CPLD reload signaling
### Component Verification Status
Only connectors, switches, and LEDs are VERIFIED:
- User verified: S002 (panel toggles), S004 (power switch), L001 (RGB LEDs)
- User verified: J022, J023, J024, J025 (connectors)
- 5V RGB upgrade components (IC018, T001, T003, R027-R029, R051) remain RECHECK
- These need manual re-verification before propagating to design docs
## Next Steps
1. Continue manual component re-verification from `.copilot/components-todo.md`
2. Future schematic work: implement dual-IC architecture in KiCAD schematics
3. Future PCB work: route 5V_MAIN on Link-Beta, upgrade connectors to 6-pin
4. Verify resistor MPNs and datasheets during component re-verification pass
## Files Updated
Design specification files:
- `design/Electronics/Controller/Design_Spec.md`
- `design/Electronics/Stator/Design_Spec.md`
- `design/Electronics/Settings_Board/Design_Spec.md`
- `design/Electronics/Consolidated_BOM.md`

Repo-local tracking:
- `.copilot/components-todo.md`
- `.copilot/files/settings-board-5v-rgb-upgrade.md`
- `.copilot/files/5v-rgb-upgrade-changelog.md`
- `.copilot/component-types-summary.md`
- `.copilot/checkpoints/004-settings-board-5v-rgb-upgrade.md`
- `.copilot/checkpoints/index.md`
