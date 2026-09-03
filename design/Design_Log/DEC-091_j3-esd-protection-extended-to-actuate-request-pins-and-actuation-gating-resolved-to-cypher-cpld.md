# DEC-091 - J3 ESD Protection Extended to `ACTUATE_REQUEST_IN_N`/`OUT_N`; Actuation Gating Resolved to Cypher CPLD (Amends DEC-090)

|Field|Value|
|:---|:---|
|**Decision ID**|DEC-091|
|**Status**|Decided|
|**Date**|2026-09-01|
|**Author**|Izzyonstage & GitHub Copilot|
|**Amends**|DEC-090|
|**Amends (files)**|`Cypher/Design_Spec.md §3, §7, §8` (ESD section, mermaid diagram, BOM); `Stack-Input/Design_Spec.md §4` (open-item note)|

## Context

DEC-090 added `ACTUATE_REQUEST_IN_N`/`ACTUATE_REQUEST_OUT_N` to Cypher's `J3` but left two items
unresolved:

1. `J3` is explicitly ESD-protected per DEC-045/DEC-048 (live mini-stack swap), but the two new
   signal pins had no allocated ESD channel — the existing 4 ESD ICs (U9–U12) were already fully
   utilised across the other 16 signal pins on this connector.
2. The previous design ANDed the actuation trigger with a keypress-active indication
   (`ENC_ACTIVE_N`), but that signal was confirmed HID-local-only and not present on `J3` — leaving
   the gating condition with no local signal source on the Stack-Input Board.

## Decision

1. **A new ESD IC, U19 (TPD4E05U06QDQARQ1), is added to the Cypher Board** — an additional count
   of the same part already used for U9–U16, providing 2 protected channels (2 spare) for
   `ACTUATE_REQUEST_IN_N`/`ACTUATE_REQUEST_OUT_N`. Placed within 3mm of the `J3` mating edge, per
   the same DEC-045/DEC-048 pattern as U9–U12.
2. **The actuation-request gating condition is resolved at the Cypher Board's own CPLD (U1), not
   locally on the Stack-Input Board.** U1 only asserts `ACTUATE_REQUEST_IN_N` onto `J3` while a
   key is actively depressed (U1 already has internal visibility of keypress-active state via its
   existing HID/`ENC_ACTIVE_N`-sourced logic). The Stack-Input Board's STM32G071 (U1) can therefore
   act directly on `ACTUATE_REQUEST_IN_N` with no local AND-gating against any second signal — the
   previously-flagged gap (DEC-090 open item) required no new signal or hardware, only this
   clarification of which board is responsible for the gating behaviour.

## Rationale

- Reusing the existing TPD4E05U06QDQARQ1 part for U19 (rather than sourcing a new ESD part) keeps
  BOM part-count low and avoids a new qualification/sourcing cycle for a single extra 4-channel
  array with 2 channels unused.
- Placing the gating responsibility upstream at the Cypher Board (the only board with direct
  visibility of keypress-active state before any HID-local signal reaches the rotor chain) avoids
  propagating a second signal down the actuation-request chain purely for gating purposes, keeping
  the IN/OUT pair (DEC-090) a clean single-purpose trigger signal at every downstream board.

## Impact

- `Cypher/Design_Spec.md §8 Thermal & ESD` — new U19 bullet; ESD working-voltage note range
  extended to include U19.
- `Cypher/Design_Spec.md §3` — component block diagram (mermaid) gains a U19 node and `J3` edge.
- `Cypher/Design_Spec.md` FR-STA-13 / DR-STA-16 — BOM references updated to include U19.
- `Cypher/Design_Spec.md` BOM table — new U19 row (TPD4E05U06QDQARQ1, qty 1).
- `Stack-Input/Design_Spec.md §4` — the DEC-090 open item regarding gating logic is resolved;
  no local hardware/signal change required on this board.
- **Not yet updated:** `design/Electronics/Consolidated_BOM.md` still reflects the pre-merge board
  naming (STA/REF/EXT abbreviations) for this TPD4E05U06QDQARQ1 line and has not been reconciled
  with the current Cypher/Stack-Input/Stack-Output board family — tracked separately under
  `post-merge-final-design-bom-sweep`, not addressed by this decision.
