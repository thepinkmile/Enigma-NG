# Sweep All Design Documents for Historical/Rationale Wording (Current-Design-Only Rule)

**ID:** design-docs-current-only-sweep
**Status:** pending
**Category:** Documentation
**Source:** User review 2026-09-03 (found repeatedly in Cypher/Stack-* boards during ACTUATE_REQUEST work)

---

## Description

Per `document-rules.md`: design specs must contain **current design only** — no superseded
values, prior rationale, correction notes, or historical detail of any kind. History belongs
exclusively in `.copilot/checkpoints/` and `design/Design_Log/` (per-DEC files).

During the ACTUATE_REQUEST signal work (2026-09-01/03), this rule was repeatedly violated across
`Cypher/`, `Stack-Input/`, `Stack-Output/`, `Stack-Interposer/`, and `Stack-Blanking/` design
docs — sentences explaining *why* a signal is absent, *why* ownership was assigned to one board
over another, or *what previously existed* were found and removed in several passes (it took
multiple review rounds by the user to catch them all in just these five boards).

This todo tracks a **full repo-wide sweep** of every `design/Electronics/**/Design_Spec.md` and
`Board_Layout.md` (and other design docs outside `.copilot/` and `design/Design_Log/`) for the
same class of violation, since the Cypher/Stack-* pass only covered a handful of boards out of
the full board set.

## Patterns to search for (non-exhaustive — based on violations found so far)

- `"does not appear"` / `"does **not** appear"` — explaining a signal's absence with justification
- `"no longer"` — implies a prior state
- `"not by <board>"` / `"not this board"` / `"because this board is..."` — ownership rationale
  contrasting with a different arrangement
- `"previously"`, `"was previously"`, `"previously-spare"` — explicit historical reference
- `"reused, no new component required"` / `"no new part number"` — process/rationale narrative
  rather than a current-state fact
- `"confirmed"`, `"resolved"`, `"corrected"`, `"amends"`, `"stale"`, `"obsolete"`, `"superseded"`
  used as narrative connectors (as opposed to a bare `DEC-NNN` citation, which is fine)
- Any sentence structure explaining *why* the current design differs from an earlier version,
  rather than just stating the current fact

## Notes

- Bare `DEC-NNN` citations (e.g. "per DEC-094") are fine — they're just cross-references, not
  narrative. The violation is explanatory/contrastive prose, not the citation itself.
- Do not remove genuinely current-design comparative language (e.g. "4 connectors rather than a
  single interconnect" describing current architecture, not a past-vs-present change) — only
  remove sentences that are fundamentally *about* a change, correction, or history.
- Scope: all `design/Electronics/**/*.md` files at minimum; consider `design/Standards/`,
  `design/Software/`, and other top-level design docs too if time permits.
