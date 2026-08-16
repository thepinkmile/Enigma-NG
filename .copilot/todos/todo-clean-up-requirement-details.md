# Clean up FR/DR requirement detail across design files

**ID:** todo-clean-up-requirement-details
**Status:** pending
**Category:** Process / Documentation
**Source:** User request, 2026-08-14
**Blocked by:** design-discussion-merge

---

## Description

Once the design-discussion merge is complete, review every board `Design_Spec.md`'s Functional
Requirements (FR-xxx) and Design Requirements (DR-xxx) tables across the whole repository and
remove implementation detail that has crept into them. Requirements should stay high-level and
implementation-agnostic; they should read as statements of intent, not restatements of the design
itself.

## Guidance

- **Functional Requirements (FR-xxx)** should describe *what* the board/component must do,
  independent of *how* - e.g. "This component must provide N hot-swappable keyswitch positions"
  rather than naming the specific socket MPN, pin count, or connector family in the requirement
  text itself.
- **Design Requirements (DR-xxx)** should describe *what* the board/component must have or be -
  e.g. "This component must have a controlled-impedance JTAG trace" rather than the exact ohm
  value, layer, or manufacturer-specific stackup detail.
- Acceptable requirement phrasing patterns: "This component must have a ...", "This component
  must do ...", "This component must be ...".
- Detailed implementation content (exact MPNs, pin numbers, resistor values, connector part
  families, signal names, etc.) belongs in the prose sections of `Design_Spec.md` (e.g. §3-§9) or
  in `Board_Layout.md`, not in the FR/DR table cells themselves. The "Satisfied By / Cross-Ref"
  column already exists for pointing from a requirement to its implementing section - use that
  link rather than duplicating the implementation detail inline in the requirement's own
  Notes/Specification column.
- Being overly specific in a requirement duplicates the design information that already lives
  elsewhere, creates two sources of truth that can drift out of sync, and defeats the purpose of
  having a requirements table distinct from the implementation narrative.

## Scope

Every board `Design_Spec.md` under `design/Electronics/` (and any board added during the
design-discussion merge) should be swept for this issue. This is a repository-wide documentation
consistency pass, not limited to any single board.
