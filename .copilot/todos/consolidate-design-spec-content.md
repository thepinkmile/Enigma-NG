# Consolidate Design Spec Content

**ID:** `consolidate-design-spec-content`
**Status:** pending
**Category:** Documentation
**Source:** Session decision — Design_Spec.md file size reduction
**Blocked by:** `enc-connector-review-pre-pcb`

---

## Description

Simplify and reduce the size of `Design_Spec.md` files across all boards. The goal is to reduce verbosity and file size without losing any design intent or traceability.

Approaches to consider for each board's Design_Spec.md:

1. **Replace duplicated standards prose** with a single cross-reference to `design/Standards/Global_Routing_Spec.md` or `design/Standards/JLCPCB_Manufacturing.md` rather than repeating the same text in each board spec.
2. **Collapse redundant requirement wording** where multiple FRs or DRs say the same thing in slightly different words; consolidate into one clear requirement.
3. **Move large reference tables** (e.g. full pin tables already captured in schematic) to a separate `Pin_Map.md` per board and link to them.
4. **Remove stale or superseded notes** that have been resolved by design decisions (DEC entries) — replace with a short reference to the DEC.

## Historical-language sweep (added 2026-08-15)

During review, a systemic pattern was flagged: design docs should describe **only the current
design state** - the git history and `design/Design_Log/` DEC entries already own the "what
changed and when" narrative. Words like "retired", "formerly", "superseded", "no longer",
"previously", "replaces the previous X" etc. should not appear in current design prose; state the
current fact directly and cross-reference a DEC entry only where genuinely useful, without
narrating the prior state inline.

`Cypher/Design_Spec.md`, `Cypher/Board_Layout.md`, `Cypher-Input/Design_Spec.md`, and
`Cypher-Input/Board_Layout.md` were already swept and fixed for this pattern (2026-08-15). The
following files still need the same sweep (found via repo-wide grep for
`retired|superseded|formerly|previously|no longer|renamed from|replaces the previous`):

- `design/Electronics/User_Settings_Module/Design_Spec.md`
- `design/Electronics/Reflector/Design_Spec.md`
- `design/Electronics/Stator/Design_Spec.md`
- `design/Electronics/Rotor/Design_Spec.md`
- `design/Electronics/Cypher-Input/TEMP_Key_Mapping_Review.md`
- `design/Electronics/Encoder_Module/Design_Spec.md`
- `design/Electronics/Controller/Design_Spec.md`
- `design/Electronics/Power_Budgets.md`
- `design/Electronics/Controller/PoE_Power_Analysis_Coilcraft_v2.md`
- `design/Electronics/JTAG_Module/JTAG_Integrity.md`

Note: not every match will need changing - some references to "previous" pass/rev/finding
numbers, or legitimate DEC cross-references, are fine. Each match needs individual review to
confirm whether it's narrating superseded design content (fix) or a legitimate current-state
statement that happens to use one of these words (leave alone).

## Scope

All board-level Design_Spec.md files:
- `design/Electronics/Controller/Design_Spec.md`
- `design/Electronics/Power_Module/Design_Spec.md`
- `design/Electronics/Stator/Design_Spec.md`
- `design/Electronics/Rotor/Design_Spec.md`
- `design/Electronics/Extension/Design_Spec.md`
- `design/Electronics/Reflector/Design_Spec.md`
- `design/Electronics/Encoder/Design_Spec.md`
- `design/Electronics/JTAG_Module/Design_Spec.md`
- `design/Electronics/User_Settings_Module/Design_Spec.md`
- `design/Electronics/Actuation_Module/Design_Spec.md`

## Notes

- Preserve all FR/DR requirement IDs — do not renumber.
- Preserve all cross-references and DEC citations.
- Do not remove any requirement that is not duplicated elsewhere.
- This is a v1.0 scope task (not v2.0 deferred).
