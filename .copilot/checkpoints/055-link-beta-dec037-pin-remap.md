# Checkpoint 055 — LINK-BETA DEC-037 pin remap

## Date

2026-04-18

## Overview

This checkpoint locks the user-directed LINK-BETA pin remap into the active design docs. DEC-037 now
defines the sole active LINK-BETA allocation, DEC-036 is retained only as historical traceability,
and all affected Controller/Stator/power-budget/diagnostic references now use the new grouped rail,
guard, JTAG, and I2C layout.

## Work Done

### Active LINK-BETA remap

- Replaced the active LINK-BETA pin table in `Controller/Board_Layout.md`
- Synced the Controller design spec LINK-BETA summary, full table, and Bank-Beta diagnostic map
- Synced the Stator design spec and board-layout references to the new `5V_MAIN` and `3V3_ENIG`
  pin locations
- Updated `Power_Budgets.md` to the new LINK-BETA connector capacities:
  - `3V3_ENIG`: 14 pins = **7.0A** connector capacity
  - `5V_MAIN`: 4 pins = **2.0A** connector capacity
- Updated the maintenance guide and BOM prose so the probe and harness notes match the new pin map

### Design decision sync

- Added **DEC-037 — LINK-BETA Pin Map Regrouped Around Dedicated JTAG and I2C Guard Bands**
- Marked **DEC-036** obsolete and clarified that DEC-015 / DEC-036 tables are no longer active
  interface definitions
- Updated DEC-015 cross-reference text so the live allocation now points at DEC-037

## Validation

- `markdownlint` run completed clean on the touched files
- Targeted follow-up search confirmed active docs now reference the DEC-037 pin groupings and updated
  `5V_MAIN` pin set

## Commits

- Pending at checkpoint write time; the next commit locks DEC-037, the repo-local handoff sync, and
  the affected active-doc updates

## Notes

- The newly present local datasheet PDFs for `MCP23017T-E/SO`, `PCA9685`, and
  `T821126A1S100CEU-C3013501` were intentionally left outside this checkpoint commit so the LINK-BETA
  decision batch remains isolated from the still-pending component-verification pass.

## Next Steps

1. Create the locking commit for the DEC-037 LINK-BETA remap batch
2. Continue the pending component verification work (`MCP23017`, `PCA9685PW,118`, and
   `T821126A1S100CEU`)
3. Move on to the user's next issue, which is expected to include a partly mechanical concern

## Files Updated

- `.copilot/checkpoints/index.md`
- `.copilot/checkpoints/055-link-beta-dec037-pin-remap.md`
- `.copilot/plan.md`
- `design/Design_Log.md`
- `design/Electronics/Consolidated_BOM.md`
- `design/Electronics/Controller/Board_Layout.md`
- `design/Electronics/Controller/Design_Spec.md`
- `design/Electronics/Power_Budgets.md`
- `design/Electronics/Settings_Board/Design_Spec.md`
- `design/Electronics/Stator/Board_Layout.md`
- `design/Electronics/Stator/Design_Spec.md`
- `design/Guides/Maintenance_Guide.md`
