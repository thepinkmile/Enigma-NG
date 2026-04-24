# Checkpoint 053 — BHR verified and review fixes locked
## Date
2026-04-18
## Overview
This checkpoint locks the next review-fix batch after checkpoint 052. The latest design-review drift
around LINK-BETA `3V3_ENIG` capacity, deferred DSI scope, and the Settings Board indicator-rail budget
has been corrected in the active docs, and the shared 16-pin `BHR-16-VUA` backplane connector now has
local datasheet coverage plus verified supplier part numbers in the repo-local component queue.
## Work Done
### Review-finding fixes applied
- Updated `Power_Budgets.md` to the active post-DEC-036 LINK-BETA `3V3_ENIG` model:
  **11 pins total = 5.5A connector capacity**
- Updated `Controller/Board_Layout.md` so the high-level 3V3 pass-through summary also uses the
  11-pin / 5.5A grouped-rail model
- Removed the stray active-doc requirement for a separate adjacent display-power header near `J_DSI1`
  and clarified that `J_DSI1` is the only fixed Controller-side display connector in the current scope
- Updated the Main Enclosure display note so only the DSI FPC path is fixed today; any auxiliary
  display power or touch harness remains future deferred scope
- Normalized the Settings Board indicator-rail wording so the docs now explicitly state the definitive
  current math:
  - Bank 1 = **5 × 20mA = 100mA max**
  - Bank 2 = **7 × 20mA = 140mA max**
  - Total = **240mA max**
- Replaced the stale Stator J7 note that previously claimed the Extension/Reflector path was only
  **1A / ≤200mA** with wording that references the actual documented Extension reinjection requirement
  of **up to 1.43A worst case** and defers final rating confirmation to the BHR datasheet verification
### BHR-16-VUA verification synced
- Added local datasheet coverage: `design/Datasheets/bhr-xx-vua-data-sheet.pdf`
- Updated `.copilot/components-todo.md` row `J016` with the confirmed supplier numbers:
  - DigiKey: `2057-BHR-16-VUA-ND`
  - Mouser: `737-BHR-16-VUA`
  - JLCPCB: `C17692295`
- Marked `J016` as **VERIFIED**
- Removed `BHR-16-VUA` from the "Missing local datasheets to fetch" queue
## Validation
- `markdownlint` run completed clean on the touched active design docs
- Targeted text sweep found no remaining matches for the stale display-header, 8-pin LINK-BETA, or
  per-bank LED-budget wording corrected in this batch
## Commits
- Pending at checkpoint write time; the next commit locks this checkpoint, the active-doc updates, the
  BHR datasheet PDF, and the synced repo-local handoff
## Key Technical Notes
### Current CR-01 state
The design-review contradiction has been reduced to a concrete hardware verification question rather
than conflicting prose. The active docs now consistently acknowledge that the Stator-to-Extension J7
path may need to support **up to 1.43A** for the first Extension's downstream reinjection case. The
remaining question is whether the verified `BHR-16-VUA` connector family and the intended harnessing
comfortably support that current in the actual implementation.
### Display-scope boundary
The active architecture now treats:

1. `J_DSI1` as the **only** fixed Controller-side display connector
2. all future display power / touch-side auxiliary wiring as **deferred add-on scope**

This avoids ghost requirements in the Controller and enclosure docs until the display add-on is
designed explicitly.
## Next Steps
1. Create the locking commit for this cleanup batch and synced repo-local handoff
2. Re-run the deep design consistency review against the new baseline
3. Re-run the datasheet coverage audit against the new baseline
4. Review whether the BHR datasheet resolves the remaining current-rating concern or whether the
   Stator/Extension link architecture still needs a physical change
## Files Updated
- `.copilot/checkpoints/index.md`
- `.copilot/checkpoints/053-bhr-verified-and-review-fixes.md`
- `.copilot/components-todo.md`
- `.copilot/plan.md`
- `design/Datasheets/bhr-xx-vua-data-sheet.pdf`
- `design/Design_Log.md`
- `design/Electronics/Controller/Board_Layout.md`
- `design/Electronics/Controller/Design_Spec.md`
- `design/Electronics/Power_Budgets.md`
- `design/Electronics/Settings_Board/Design_Spec.md`
- `design/Electronics/Stator/Board_Layout.md`
- `design/Mechanical/Main_Enclosure/Design_Spec.md`
