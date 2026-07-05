# Update Boards_Overview, System_Architecture and related docs for merge

**ID:** merge-update-top-level-docs
**Status:** pending
**Category:** Electronics / Documentation
**Source:** design-discussion-merge
**Blocked by:** all merge-create-* and merge-update-ctl-board todos

---

## Description

Update all top-level design documents to reflect the new board set, replacing references to
retiring boards (STA, REF, EXT, JM, AM) with the new Cypher system boards.

## Notes

- design/Electronics/Boards_Overview.md — add all new boards, remove retiring boards.
- design/Electronics/System_Architecture.md — update block diagrams and interface names.
- design/Electronics/Electrical_Design.md — update power paths and signal routing.
- design/Electronics/Power_Budgets.md — recalculate for new board set.
- design/Electronics/Consolidated_BOM.md — remove retiring boards, add new boards.
