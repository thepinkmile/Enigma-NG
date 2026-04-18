# Checkpoint 052 — DSI confirmed and topology cleanup locked

## Date

2026-04-18

## Overview

This checkpoint locks the next post-review cleanup batch after checkpoint 051. The Controller Board
`J_DSI1` connector is now confirmed as a real, verified component in the active design docs, and the
remaining cross-document architecture issues from the latest deep-design rerun were resolved so the
mechanical assembly flow, high-level power narrative, and Reflector ownership model all match the
current intended system behavior.

## Work Done

### Controller DSI connector confirmed

- Replaced the remaining `J_DSI1` TBD wording in the active Controller docs with the verified
  Amphenol **F52Q-1A7H1-11015** 15-pin 1.0mm ZIF/FPC connector
- Updated the shared BOM so `J_DSI1` now has real Mouser / DigiKey / JLCPCB fields and no longer
  appears as an unresolved placeholder
- Linked the existing local Amphenol F52Q/F52R datasheet PDF in the datasheet coverage table
- Fixed the stale `TPD4E05U06QDQARQ1` datasheet note so it now points at the local PDF already present

### Remaining architecture-review findings resolved

- Corrected the top-level mechanical assembly order to the intended structure:
  `Stator -> 5 rotors -> [Extension -> 5 rotors]* -> Reflector`
- Clarified that the Reflector is **mandatory** and **passive**
- Clarified that the **Stator CPLD** owns reflector-map selection/application so all mapping logic
  stays centralized on the Stator rather than requiring another CPLD on the Reflector
- Updated the high-level power docs so `3V3_ENIG` is described as the logic/control rail while the
  Settings Board RGB indicators are powered from `5V_MAIN`
- Tightened the high-level grounding wording so only the Power Module is described as the galvanic
  `GND` ↔ `GND_CHASSIS` bond point
- Added the Extension **J7 -> J5** reinjection path to the system-level 3V3 distribution narrative

## Validation

- `markdownlint` run completed clean on the touched design docs and `.copilot/plan.md`
- Targeted text sweep found no remaining matches for the stale wording corrected in this batch

## Commits

- Pending at checkpoint write time; the next commit locks this checkpoint, the active-doc fixes, and
  the synced repo-local handoff

## Key Technical Notes

### Reflector ownership model

The Reflector board is a **passive turnaround board**. It does not contain a local CPLD. The Stator
CPLD owns reflector-map selection and application so the component placement mapping remains
centralized and the design avoids an unnecessary second CPLD with low pin utilization.

### DSI connector state

`J_DSI1` is now a confirmed component choice, but the **display add-on board** remains deferred. The
active design now distinguishes clearly between:

1. the **Controller-side connector** (confirmed and locked)
2. the eventual **screen / touch / mounting assembly** (still future work)

## Next Steps

1. Create the locking commit for this cleanup batch and synced repo-local handoff
2. Re-run the deep design consistency review against the new baseline
3. Re-run the datasheet coverage audit against the new baseline
4. Review whether any remaining findings are substantive or only residual watch-items

## Files Updated

- `.copilot/checkpoints/index.md`
- `.copilot/checkpoints/052-dsi-confirmed-and-topology-cleanup.md`
- `.copilot/plan.md`
- `design/Design_Log.md`
- `design/Electronics/Boards_Overview.md`
- `design/Electronics/Consolidated_BOM.md`
- `design/Electronics/Controller/Design_Spec.md`
- `design/Electronics/Reflector/Design_Spec.md`
- `design/Electronics/System_Architecture.md`
- `design/Mechanical/Complete_System_Assembly/Design_Spec.md`
