# Checkpoint 064 — Battery connector candidate documented
## Date
2026-04-26

## Overview
This checkpoint captures the closeout of the current battery-connector review workstream at the
candidate-document stage. The active Power Module docs now preserve the Glenair military / Nett
Warrior-style connector direction, its supporting datasheet extraction, and the interposer-based
integration approach without yet promoting the connector into the official production Power Module
interface.

## Work Done
### Battery connector review closeout
- Added `design/Electronics/Power_Module/Millitary_Battery_Connection_Option.md` to hold the
  candidate military battery connector details separately from the main Power Module design
- Updated `design/Electronics/Power_Module/Design_Spec.md` to cross-reference the candidate option
  while keeping the current Molex battery connector as the active official interface
- Recorded the preferred **PM-side interposer / daughterboard** approach for rear-face alignment near
  the USB-C connector
- Recorded the separate prototype-only adapter-board direction using the same female Glenair
  receptacle and the existing Accutronics / Inspired Energy battery interface

### Datasheet extraction and confirmation state
- Generated `design/Datasheets/Glenair-807-216-datasheet.md` from the two Glenair PDFs and linked
  both source PDFs inside the markdown file
- Linked the new Power Module battery option note to the markdown datasheet extraction
- Recorded that `Y` keying is confirmed as the standard battery keying intended to prevent mating
  with data-only STAR-PAN / STAR-PAN NG ports

## Validation
- Updated Power Module battery-review markdown files lint cleanly with the repo markdownlint rules
- Repo-local `.copilot/` state now treats the battery connector review as closed at the candidate
  documentation stage
- The remaining connector-specific unknowns are now explicitly captured as final-review gates rather
  than an active open workstream

## Commits
- Pending at checkpoint write time; the next commit should include the battery connector candidate
  docs, datasheet markdown, source PDFs, and this repo-local state refresh

## Technical Decisions
- Glenair `807-216-00ZNU6-6DY` is the documented military battery connector candidate
- `Y` keying is confirmed as the correct standard battery keying for the chosen family
- The preferred mechanical integration path is a small Power Module interposer / daughterboard
- The current review does **not** yet promote the candidate into the official production connector

## Open Questions
- Exact 6-pin contact assignment remains to be confirmed
- Exact `BATT_PRES_N` contact position remains to be confirmed
- The role of any reserved / unused contact in the 6-pin layout remains to be confirmed
- Final mating cable choice and interposer fit still need confirmation

## Next Steps
1. Commit the battery connector candidate documentation and repo-local checkpoint refresh
2. Start the next session from `.copilot/plan.md`, `.copilot/handoff.md`, and this checkpoint
3. Continue with the next remaining non-battery review workstream
4. Re-check the remaining connector specifics during the final deep-dive and manual review before
   treating the design as a complete Version 1 release

## Files Updated
- `design/Electronics/Power_Module/Design_Spec.md`
- `design/Electronics/Power_Module/Millitary_Battery_Connection_Option.md`
- `design/Datasheets/Glenair-807-216-datasheet.md`
- `design/Datasheets/Glenair_03232018_807_216-3045547-datasheet.pdf`
- `design/Datasheets/Glenair_mighty-mouse-807-nw-connector_catalogue.pdf`
- `.copilot/plan.md`
- `.copilot/handoff.md`
- `.copilot/checkpoints/index.md`
- `.copilot/checkpoints/064-battery-connector-candidate.md`
