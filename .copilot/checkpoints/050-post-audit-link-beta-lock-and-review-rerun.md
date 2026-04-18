# Checkpoint 050 — Post-audit architecture sync and Link-Beta rebalance locked

## Date

2026-04-18

## Overview

This checkpoint locks the post-audit architecture cleanup that followed the one-off deep-dive design
review and datasheet audit. The active docs were brought into line with the user's clarifications:
the physical Reflector remains mandatory, Extensions stay optional in 5-rotor blocks, Link-Beta now
carries `5V_MAIN`, the Settings/Stator harness is the 6-pin form, and the Settings Board indicators
remain full RGB under CM5 control.

The final change in this batch was a deliberate Link-Beta rebalance. Instead of leaving a large
legacy spare block after DEC-031, the freed monitor pins were reallocated into grouped power rails:
four contiguous `5V_MAIN` pins, three additional `3V3_ENIG` pins, and three grouped `GND` returns.
That grouped-power scheme is now frozen in **DEC-036** and propagated through the active docs and
repo-local handoff.

## Work Done

### Post-audit architecture fixes synced

- Removed stale rotor-chain I2C wording from the active architecture docs
- Clarified that the Reflector board is always physically present, while Extension boards remain
  optional and are used in 5-rotor groups
- Updated the Stator/Settings harness to the 6-pin JST PH definition
- Normalised the Stator + Settings I2C address map to a contiguous block:
  - Stator: `0x20`, `0x21`, `0x22`
  - Settings Board: `0x23`, `0x24`, `0x25`
- Added missing-datasheet follow-up rows and the expander revisit note to
  `.copilot/components-todo.md`

### Settings Board RGB correction completed

- Reverted the temporary incorrect red/green-only interpretation
- Restored the correct **full RGB** model under **CM5 control**
- Synced the active Settings Board docs, Stator/Controller references, Consolidated BOM, Design Log,
  and repo-local handoff artifacts to the 6-MOSFET RGB rail topology

### Link-Beta grouped-power rebalance locked

- Kept the existing 40-pin Samtec LINK-BETA connector from DEC-015
- Replaced the old freed-monitor spare block with active grouped rails:
  - **Pins 14–17:** `5V_MAIN`
  - **Pin 18:** `GND`
  - **Pins 19–21:** additional `3V3_ENIG`
  - **Pins 22–24:** grouped `GND`
- Increased the Stator-side `5V_MAIN` connector capacity from **1.0A** to **2.0A**
- Repurposed Diagnostic Bank-Beta from dead spare pads into grouped power / I2C / JTAG bring-up
  probes
- Added **DEC-036** to preserve the final grouped-power allocation

### Validation

- `markdownlint` run completed clean on the touched active docs and `.copilot/plan.md`

## Commits

- Pending at checkpoint write time; filled in after the batch commit is created.

## Key Technical Notes

### Link-Beta is now an active mixed-power connector

Future sessions should **not** revert LINK-BETA to the old "mostly spare" post-DEC-031 model.
The active grouped-power rule is:

1. Keep the **40-pin** ERF8-020 / ERM8-020 connector pair
2. Group all four Stator-facing `5V_MAIN` pins together on **pins 14–17**
3. Use **pins 19–21** as additional `3V3_ENIG`
4. Use **pins 18 and 22–24** as the local grouped return / moat around that mixed-power block

### Settings Board RGB rule remains unchanged

The Settings Board indicators remain **full RGB under CM5 control**. The Link-Beta rail rebalance
changes the available 5V headroom only; it does **not** change the RGB topology, colour model, or
the six BSS138 shared colour-rail sink devices.

## Next Steps

1. Create the batch commit that locks this checkpoint and the synced repo-local handoff
2. Re-run the two one-off deep reviews from this frozen state:
   - complete design consistency / connectivity / net-name review
   - complete datasheet coverage / missing-datasheet URL review
3. Review the rerun findings and prepare the next fix batch only after the new reports are in

## Files Updated

- `.copilot/checkpoints/index.md`
- `.copilot/checkpoints/050-post-audit-link-beta-lock-and-review-rerun.md`
- `.copilot/component-types-summary.md`
- `.copilot/components-todo.md`
- `.copilot/files/5v-rgb-upgrade-changelog.md`
- `.copilot/files/settings-board-5v-rgb-upgrade.md`
- `.copilot/plan.md`
- `design/Design_Log.md`
- `design/Datasheets/Adafruit-3350-datasheet.pdf`
- `design/Electronics/Boards_Overview.md`
- `design/Electronics/Consolidated_BOM.md`
- `design/Electronics/Controller/Board_Layout.md`
- `design/Electronics/Controller/Design_Spec.md`
- `design/Electronics/Encoder/Design_Spec.md`
- `design/Electronics/Power_Budgets.md`
- `design/Electronics/Reflector/Design_Spec.md`
- `design/Electronics/Settings_Board/Board_Layout.md`
- `design/Electronics/Settings_Board/Design_Spec.md`
- `design/Electronics/Stator/Board_Layout.md`
- `design/Electronics/Stator/Design_Spec.md`
- `design/Electronics/System_Architecture.md`
- `design/Guides/Maintenance_Guide.md`
- `design/Mechanical/Complete_System_Assembly/Design_Spec.md`
