# Move retiring board design files to .recycle-bin/

**ID:** merge-remove-old-boards
**Status:** pending
**Category:** Electronics / Documentation
**Source:** design-discussion-merge
**Blocked by:** merge-update-top-level-docs

---

## Description

Move design files for retiring boards to .recycle-bin/ per QUATERNARY directive.
Boards to retire: Stator (STA), Reflector (REF), Extension (EXT), JTAG Module (JM),
Actuation Module (AM).

## Notes

- All content from retiring boards must be inlined into new board specs BEFORE removal.
- Permanent deletion is a user-only action; only move to .recycle-bin/.
- Verify Consolidated_BOM.md and cross-references are updated before removing files.
