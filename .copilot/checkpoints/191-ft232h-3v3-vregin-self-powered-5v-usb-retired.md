# Checkpoint 191 — FT232H Moved to 3.3V VREGIN Self-Powered Operation; 5V_USB Net Retired

**Date:** 2026-09-11

## Summary

This short session closed `jdb-ft232h-3v3-vregin`. Investigation found the todo's referenced part
number (`FT232HPQ-TRAY`) was actually FTDI's unrelated newer "HP" USB Type-C/Power-Delivery chip
family, not a Rev C variant of the plain FT232H already in use — no part substitution was needed.
The real fix was simpler: the already-specified `FT232HL-REEL` already supports 3.0–3.6V `VREGIN`
operation on Rev C silicon (current production stock by default). Implementing it also surfaced
and fixed a genuine pre-existing defect: the `5V_USB` net referenced in Cypher's design was a
phantom/stale leftover from the pre-merge JTAG Daughterboard architecture, never actually present
on the current post-DEC-098 dock. DEC-102 was created.

## 1. Part number investigation

The todo's notes referenced `FT232HPQ-TRAY` (DigiKey `768-FT232HPQ-TRAY-ND`). Converted the
`FT232HPQ-Information.pdf` (already in `design/Datasheets/`, not yet in markdown) to markdown
using `.copilot/agent-scripts/generate_markdown_datasheets.py`, confirming it describes FTDI's
"HP Series" — a USB Type-C + PD3.0 controller chip family, materially different from and more
complex than the plain FT232H already used on Cypher. This part number was **not** adopted.

The actual 3.0–3.6V `VREGIN` capability is documented in the existing `FT232H-datasheet.md`
(§5.2 electrical table + errata: *"3.3V operation is for Revision C, see the errata for previous
revisions"*). The already-specified `FT232HL-REEL` is this same part; Rev C has been the only
shipping silicon revision for years, so no BOM part-number change was required.

## 2. Full required change set (not just VREGIN)

Cross-checking the FT232H datasheet's two self-powered reference circuits (§6.2.1 "5V" vs §6.2.2
"3.3V") surfaced that `VCCD` (pin 39) changes role between the two modes — in 5V-`VREGIN` mode it
is a self-generated output; in 3.3V-`VREGIN` mode it becomes an input requiring an explicit
external tie to the 3.3V rail. This had not been wired at all previously (only implicitly
decoupled as part of the generic bypass-cap list). Implemented on Cypher's `U17`:

- `VREGIN` (pin 40): tied to `3V3_ENIG`.
- `VCCD` (pin 39): new explicit trace to `3V3_ENIG`, alongside `VCCIO`/`VPLL`/`VPHY`.
- `VCCA`/`VCORE`: unchanged (internal 1.8V LDO output, no external tie either way).

## 3. Phantom `5V_USB` net discovered and retired

While verifying no other Cypher consumer needed 5V, found that `5V_USB` did not actually exist as
a real net under the current dock architecture at all: Cypher's power-only `J1` dock (per DEC-098)
carries only `GND`/`5V_MAIN`/`3V3_ENIG`, and `5V_USB` does not appear anywhere in the Controller's
own spec — the Controller's `TPS2065C` (`U2`) is confirmed entirely local to the Controller
(protects only its own external USB-A port, no BtB pin). This was stale terminology inherited from
the pre-merge JTAG Daughterboard architecture (which genuinely did have its own `5V_USB` BtB pin)
that was never fully reconciled when DEC-098 redefined the dock. Removed the `5V_USB` net and its
entry filter (`C27`) from Cypher's design entirely.

## 4. Power budget updates

`Power_Budgets.md`: FT232H's full 100 mA consolidated onto `3V3_ENIG` (previously split
10 mA `3V3_ENIG` / 100 mA `5V_MAIN` via the now-retired `5V_USB` net):

- `3V3_ENIG` typical total: 2,193 mA → 2,283 mA (rounded 2.20 A → 2.29 A; LDO headroom 27% → 24%).
- `5V_MAIN` total: 10.79 A → 10.69 A (LMQ61460-Q1 utilisation 89.9% → 89.1%).

## 5. Historical-wording cleanup (user review)

The user's review caught several instances of the same "current design only" violation class
found repeatedly in earlier sessions — contrastive/historical phrasing explaining *why* the
current state differs from a prior one, rather than just stating the current fact:

- `Cypher/Design_Spec.md §5`: removed "becomes an input (not self-generated... as it would be in
  5V mode)", "bypass/pass-through mode rather than 5V-to-3.3V regulation", and a trailing
  "unaffected by the VREGIN rail choice... both reference designs require..." comparison.
- `Cypher/Design_Spec.md` DR-CYP-11: removed the same "not self-generated... under 5V VREGIN"
  parenthetical.
- `Power_Budgets.md` 3V3_ENIG table row: removed "no 5V rail required" (redundant inside a table
  already scoped to 3V3_ENIG).
- `Power_Budgets.md` 5V_MAIN scope note: removed the "FT232H draws no 5V_MAIN... fully
  self-powered" sentence (a consumer table doesn't need to justify an absence).
- `Power_Budgets.md` LED margin note: replaced an "Updated 2026-09-11: FT232H's 0.1 A moved off
  5V_MAIN..." narrative with a plain statement of the current 89.1% figure, pointing to
  `Document History` for the change trail instead.

## Decision created this session

DEC-102 — see `design/Design_Log/index.md`. Next DEC number: **103**.

## Status

- `jdb-ft232h-3v3-vregin`: **done**.

## Next steps (user-confirmed order, see `plan.md`)

1. **User Settings Module review** (new, requested by the user before continuing to the LED/PWM
   task) — user has changes in mind that may impact Cypher, Cypher-Input, and Cypher-Output.
2. `cypher-input-led-independent-rgb-pwm-review` — independent per-channel RGB PWM + LED part
   reconsideration; feeds the planned Mock Keyboard test rig.
3. `cpld-production-replacement` — MAX10 FPGA discussion.
4. `footprint-requests-pending` — alongside the final BOM sweep.
5. `system-assembly-harnesses` and `system-config-variants-diagrams` — after the above.
