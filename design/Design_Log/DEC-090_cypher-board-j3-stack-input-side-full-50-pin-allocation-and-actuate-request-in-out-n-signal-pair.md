# DEC-090 - Cypher Board `J3` (Stack-Input Side) Full 50-Pin Allocation; `ACTUATE_REQUEST_IN_N`/`ACTUATE_REQUEST_OUT_N` Signal Pair

|Field|Value|
|:---|:---|
|**Decision ID**|DEC-090|
|**Status**|Decided|
|**Date**|2026-09-01|
|**Author**|Izzyonstage & GitHub Copilot|
|**Amends**|`Cypher/Board_Layout.md §2`; `Cypher/Design_Spec.md §3`; `Stack-Input/Design_Spec.md` (FR-SIN-03/04, DR-EXT-02, DR-SIN-01, §4 Actuation Module, mermaid diagram); `Stack-Input/Board_Layout.md §1-2`|

## Context

`merge-cypher-board-j3j6-pinouts` closed out `J5`/`J6` in a prior session, but left `J3`
(Stack-Input/STA-side) and `J4` (Stack-Output/REF-side) with only 26/50 and 24/50 contacts
defined respectively - the remaining pins were placeholder-tied to GND with no signal rationale.
Reviewing `Stack-Input/Design_Spec.md` against the actual `J3` pin map surfaced two problems:

1. **Missing signals.** Stack-Input's own DR-EXT-02 already assumed its front connector (mating
   with Cypher's `J3`) carries `3V3_ENIG`, `5V_MAIN`, `ENC_ACTIVE_N`, and `ACTUATE_REQUEST_N` -
   none of which existed on Cypher's `J3` map. Without `3V3_ENIG`/`5V_MAIN`, Stack-Input has no
   power path from the Cypher Board at all.
2. **A genuine signal-definition contradiction.** `Cypher/Design_Spec.md §3` explicitly states
   `ENC_ACTIVE_N` is a HID-local sideband only, forwarded solely to `LBD_DEC` (`J6`) and "not
   propagated through the plugboard, rotor, or reflector interfaces" - directly contradicting
   Stack-Input's own assumption that it receives `ENC_ACTIVE_N` via `J1`/`J3`.
3. **`ACTUATE_REQUEST_N` was a single net**, but a Rotor Mini-Stack chain needs to both receive an
   actuation trigger from upstream (Cypher or the previous mini-stack) and propagate/generate a
   trigger for the next mini-stack downstream - two distinct roles that a single net cannot
   represent without ambiguity about direction.

## Decision

1. **`J3` (Stack-Input/STA-side) is now fully 50-pin allocated**, following the same
   board-agnostic template convention already established for `J5`/`J6` (fixed pin position →
   fixed signal role, center GND bar at pins 25/26). New pins added: `3V3_ENIG` ×4 (pins 1-4),
   `5V_MAIN` ×4 (pins 47-50), `ACTUATE_REQUEST_IN_N` (pin 16), `ACTUATE_REQUEST_OUT_N` (pin 35).
   All previously-undefined pins not carrying one of these four new nets are GND. See
   `Cypher/Board_Layout.md §2` for the full map.
2. **`ENC_ACTIVE_N` does not appear on `J3`.** It remains exclusively a HID-local sideband
   between Cypher-Input, the Cypher Board, and Cypher-Output (`J5`/`J6` only), per the existing
   `Cypher/Design_Spec.md §3` description. All `ENC_ACTIVE_N` references on Stack-Input's `J1`/
   `J2` are removed.
3. **`ACTUATE_REQUEST_N` is replaced by a pair of nets, `ACTUATE_REQUEST_IN_N` and
   `ACTUATE_REQUEST_OUT_N`**, both present at fixed pin positions on **every** instance of this
   connector template throughout the Rotor Mini-Stack chain (Cypher's `J3`, and both Stack-Input's
   `J1` front and `J2` rear) - not a simple front-IN/rear-OUT passthrough. Each board's own CPLD
   (or, for the Stack-Input Board specifically, its native STM32G071 AM controller, which has no
   local CPLD) decides via its own programmed/dynamic configuration how `IN` propagates to `OUT`:
   - **Cypher Board (`J3`):** `ACTUATE_REQUEST_IN_N` → CPLD U1 input, triggering Mini-Stack 1
     actuation per U1's configuration. `ACTUATE_REQUEST_OUT_N` → NC (Cypher originates the
     chain and never receives an incoming request).
   - **Stack-Input Board (`J1` front):** `ACTUATE_REQUEST_IN_N` → U1 (STM32G071), triggering this
     board's own solenoid actuation. `ACTUATE_REQUEST_OUT_N` → NC (mirrors Cypher's own NC -
     nothing is driven back upstream).
   - **Stack-Input Board (`J2` rear):** `ACTUATE_REQUEST_IN_N` → NC (reserved for a future
     bidirectional handshake). `ACTUATE_REQUEST_OUT_N` ← sourced from the last ROT board's own
     carry mechanism in this mini-stack, driving the next mini-stack's `ACTUATE_REQUEST_IN_N`.
   - Plain Rotor boards further down the chain are expected to carry all four nets (front-IN,
     front-OUT, rear-IN, rear-OUT) into their own CPLD fabric, even where the carry-mechanism
     logic itself is not yet defined, so the CPLD's synthesised configuration can determine
     actual propagation behaviour without a future board respin.

## Rationale

- Reusing the exact `J5`/`J6` board-agnostic template convention (fixed pin position → fixed
  signal role, identical center GND bar position) keeps all four HID/stacking connectors on the
  Cypher Board internally consistent, and lets every board along the Rotor Mini-Stack chain that
  uses this same connector part interpret a given pin identically.
- Splitting the single `ACTUATE_REQUEST_N` net into an IN/OUT pair - present at both the front and
  rear connector of every board in the chain - gives each board's CPLD (or, for Stack-Input,
  STM32G071) full visibility of both the upstream trigger and the downstream trigger it may need
  to assert, without assuming a fixed forward-only passthrough topology that would need revisiting
  once Rotor carry-mechanism logic is defined.
- Removing `ENC_ACTIVE_N` from `J3` resolves a genuine, pre-existing contradiction between the
  Cypher Board's own signal-scoping description and Stack-Input's connector assumptions - rather
  than papering over it with a workaround.

## Open Item (Not Resolved by This Decision)

The previous Stack-Input design description ANDed the (now-removed) `ENC_ACTIVE_N` with the
actuation-request signal, so actuation only triggered while a key was actively depressed. With
`ENC_ACTIVE_N` confirmed HID-local-only, that gating condition currently has **no local signal
source on the Stack-Input Board**. This requires a decision (e.g. re-deriving a button-press
indication via a different signal path, or dropping the gating requirement) before firmware and
schematic capture are finalised - tracked as an open item in `Stack-Input/Design_Spec.md §4`.

Also **out of scope for this decision:** `J4` (Stack-Output/REF-side) still requires its own
pin-by-pin review (currently missing at least `3V3_ENIG`). Unlike the initial assumption when this
review began, `J4` is now confirmed to also need to carry actuation-request signals - this will be
addressed together with the rest of `J4`'s missing-signal review in a follow-up pass.

## Impact

- `Cypher/Board_Layout.md §2` - `J3` full 50-pin map added, replacing the 26-defined/24-GND-
  placeholder table.
- `Cypher/Design_Spec.md §3` - new "Actuation Request Chain (`J3`)" subsection documenting this
  board's `ACTUATE_REQUEST_IN_N`/`ACTUATE_REQUEST_OUT_N` wiring.
- `Stack-Input/Design_Spec.md` - FR-SIN-03/04, DR-EXT-02, DR-SIN-01 reworded; `ENC_ACTIVE_N`
  references removed from the mermaid diagram and signal-source section; new "Actuation Request
  Chain" section with the open-item gating-logic note above.
- `Stack-Input/Board_Layout.md §1-2` - `J1`/`J2` sections updated with the newly-resolved pins.
- `merge-cypher-board-j3j6-pinouts` todo - `J3` scope now resolved; `J4` remains open.
