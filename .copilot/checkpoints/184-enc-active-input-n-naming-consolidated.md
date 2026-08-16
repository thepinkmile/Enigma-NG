# Checkpoint 184 — `ENC_ACTIVE_INPUT_N` Naming Consolidated (Cypher / Cypher-Input)

**Date:** 2026-08-15
**Session work:** During user review of `Cypher-Input/Board_Layout.md`, three signal names were
found in use for what should be at most two distinct signals: `ENC_ACTIVE_N` (the ENC module's own
local output pin, at `J2`), and two competing names for the *forwarded/broadcast* copy of that
signal on the Cypher <-> Cypher-Input `J5`/`J7` interconnect - `ENC_ACTIVE_INPUT_N` (the original
draft name) and `ENC_ACTIVE_KBD_N` (an incomplete rename from an earlier session intended to match
the Cypher Board's internal net name). Consolidated on **`ENC_ACTIVE_INPUT_N`** for the
forwarded/broadcast signal, per explicit user preference - it is not tied to being triggered by a
physical keyboard, since a future CM5-driven GPIO trigger for this signal is possible. Also
deferred RGB LED part sourcing for Cypher-Input to the batched `merge-missing-components` todo.

---

## Status

- `merge-create-cypher-input` — unchanged, still `in_progress`. This session's changes are pure
  naming/documentation consistency fixes plus a sourcing-deferral decision; no new blocking items
  were introduced or resolved. The only remaining blocking item is still the left-side (J4/J6)
  Plugboard passthrough signal definition, blocked on `merge-create-plugboard`.
- **RGB LED part sourcing** is no longer tracked as an open item blocking this board's own sign-off
  in `handoff.md` - it is now tracked in `merge-missing-components` alongside other outstanding BOM
  parts, per explicit user instruction (batching sourcing work is more efficient than resolving it
  ad hoc mid-merge). Current-limit resistor values remain TBD in the design docs until that part is
  selected; this was not changed this session.

---

## Changes made this session

| Change | Scope |
| --- | --- |
| `ENC_ACTIVE_KBD_N` -> `ENC_ACTIVE_INPUT_N` | `Cypher-Input/Board_Layout.md` (pin table + wiring note + §4 intro note), `Cypher-Input/Design_Spec.md` (FR-CYPI-06, §3 bidirectionality note, §7 interconnects text x2), `Cypher/Board_Layout.md` (pin table + rename note + J6 wiring table), `Cypher/Design_Spec.md` (mux forwarding bullet, U6 GPIO pin table) |
| "forwarded to J4" -> "forwarded to J5/J7" | `Cypher-Input/Board_Layout.md` §2 usage note; `Cypher-Input/Design_Spec.md` §3 "ENC_ACTIVE_N Bidirectionality" |
| `merge-missing-components.md` note added | Cypher-Input RGB LED indicator part (D1-D26/D1-D42/D1-D12) + dependent current-limit resistor values, explicitly deferred here 2026-08-15 |
| Stator board's own stale copies of the same naming inconsistency | **Left untouched** - explicit user decision; out of scope pending retirement via `merge-remove-old-boards` |
| Generic `ENC_ACTIVE_N` (ENC module's own local `J2` output pin, owned by `Encoder_Module/Design_Spec.md`) | **Left unchanged** - distinct signal from the forwarded/broadcast one being consolidated; appears identically across every board that mounts an ENC module (Cypher, Cypher-Input, Stack-Input, Stack-Blanking, Stator) and is not part of this naming conflict |

---

## Verification performed this session

- Confirmed via `grep` that no `ENC_ACTIVE_KBD_N` instances remain in `Cypher-Input/Board_Layout.md`,
  `Cypher-Input/Design_Spec.md`, `Cypher/Board_Layout.md`, or `Cypher/Design_Spec.md`.
- Confirmed `Cypher-Input/TEMP_Key_Mapping_Review.md`'s `ENC_ACTIVE_N` references are the generic
  module-level signal (correctly out of scope, untouched).
- Confirmed `ENC_ACTIVE_LBD_N` (a different, output-side/lightboard sideband name) was not affected
  by this rename - it is a distinct signal and out of scope.
- Traced the pin-map tables in both boards' `Board_Layout.md §4` to confirm pin 24 on `J5`/`J7`
  (not `J4`) is where the forwarded signal actually lives, before correcting the two stale "J4"
  cross-references.

---

## Next Session Start Point

1. `merge-create-cypher-input` remains `in_progress`, blocked only on the Plugboard passthrough
   signal definition (`merge-create-plugboard`) - which also needs pin allocation for the 4 LED
   broadcast signals on the same left connector pair (`J4`/`J6`).
2. RGB LED part sourcing (and its dependent current-limit resistor values) is now tracked under
   `merge-missing-components`, not as a standalone blocker on this board - no user follow-up is
   awaited on this specific item until that todo is actioned.
3. Likely next actionable step: `merge-create-cypher-output` (create the board files; note its LED
   bank is much simpler post-DEC-087 - just 3 colour MOSFETs + 1 cathode-return MOSFET driven by
   broadcast signals from Cypher-Input), or begin scoping `merge-create-plugboard`.
4. Mechanical assembly docs (`Keyboard_Assembly`, `Lightboard_Assembly`, `Plugboard_Assembly`)
   remain explicitly out of scope until a dedicated mechanical-overhaul pass after the electronics
   merge completes.
