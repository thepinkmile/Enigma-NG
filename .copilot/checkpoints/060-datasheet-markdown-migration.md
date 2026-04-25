# Checkpoint 060 — Datasheet markdown migration
## Date
2026-04-26

## Overview
This checkpoint captures the large datasheet-conversion pass across `design/Datasheets/`. Local PDF
datasheets now have markdown companions, the generated markdown files were reviewed in category
batches, and the active design docs were retargeted from PDF links to the reviewed markdown
datasheets.

## Work Done
### Datasheet markdown generation
- Generated markdown companions for all 78 local datasheet PDFs in `design/Datasheets/`
- Kept the two existing pseudo-datasheet markdown files in place
- Preserved explicit source-PDF references inside each generated markdown datasheet
- Included detailed extracted content plus searchable raw/page-oriented extraction sections

### Review pass
- Ran review batches across power, logic, passives, and connector/mechanical datasheets
- Tightened identity, ordering, pin, spec, mechanical, formula, and application sections where the
  initial extraction missed design-relevant detail
- Accepted lighter extraction for connector and mechanical-drawing PDFs per user direction

### Design-link migration
- Updated active design-doc references from `.pdf` datasheet links to the new `.md` datasheet links
- Cleaned residual `.pdf` wording in labels/headings so the design docs now consistently point at
  markdown datasheets
- Preserved source-PDF links only inside `design/Datasheets/*.md`

## Validation
- All 78 PDFs now have corresponding markdown files
- Design docs now contain zero `.pdf` references
- Source-PDF links remain present inside the generated datasheet markdown files

## Commits
- Pending at checkpoint write time; the next commit should include the generated markdown datasheets,
  design-link migration, and this repo-local state refresh

## Technical Decisions
- Deep review was required before retargeting the design-doc links from PDF to markdown
- Connector/mechanical-drawing datasheets are allowed to stay lighter because many source files are
  sparse drawings and fuller detail can be added later during KiCAD library work

## Open Questions
- Some large handbooks/family datasheets still have unavoidable figure/OCR/table extraction limits
- The next datasheet-related follow-up would be selective refinement only if a specific part needs
  more structured capture for schematic or footprint work

## Next Steps
1. Commit the datasheet markdown generation, link migration, and repo-local checkpoint refresh
2. Start the next session from `.copilot/plan.md`, `.copilot/handoff.md`, and this checkpoint
3. Resume the next open design-review task from the active `design/` docs

## Files Updated
- `.copilot/plan.md`
- `.copilot/handoff.md`
- `.copilot/checkpoints/index.md`
- `.copilot/checkpoints/060-datasheet-markdown-migration.md`
- `design/Datasheets/*.md` for generated/reviewed markdown datasheets
- design docs that previously linked to datasheet PDFs
