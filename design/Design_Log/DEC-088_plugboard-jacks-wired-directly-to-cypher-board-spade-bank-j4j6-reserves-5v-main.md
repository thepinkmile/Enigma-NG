# DEC-088 - Plugboard Jacks Wired Directly to Cypher Board Spade Bank; J4/J6 Left Pair Reserves 5V_MAIN

|Field|Value|
|:---|:---|
|**Decision ID**|DEC-088|
|**Status**|Decided|
|**Date**|2026-08-16|
|**Author**|Izzyonstage & GitHub Copilot|
|**Amends**|`Cypher/Design_Spec.md §6`; `Cypher/Board_Layout.md §4, §7`; `Cypher-Input/Design_Spec.md §7`; `.copilot/todos/merge-create-plugboard.md`; supersedes the earlier assumption (2026-08-09 session) that Plugboard-specific signals would be defined on the `J4`/`J6` HID interconnect left pair|

## Context

Two open items were being tracked for the Cypher system's HID interconnect left pair (`J4`/`J6`
on the Cypher Board, and the equivalent connectors on Cypher-Input/Cypher-Output):

1. The left pair was documented as carrying "3V3_ENIG/GND/Plugboard passthrough signals," with
   exact Plugboard signal allocation deferred to `merge-create-plugboard`/
   `merge-cypher-board-j3j6-pinouts`.
2. Separately, the Cypher Board already carries its own spade blade terminal bank (`J20+`,
   Keystone 1285-ST, 256 total) on its rear face - inherited from the pre-Cypher Encoder board's
   jack-field role - with physical arrangement noted as "TBD at layout."

Having reviewed the mechanical side of the design, the user determined that routing physical
plugboard patch-jack signals through the `J4`-`J7` PCB-to-PCB HID interconnect stack (Cypher
Board -> HID board -> HID board -> Plugboard board) is **not mechanically feasible**. The
Plugboard board sits at the far end of that stack, while the actual plugboard jack field needs a
short, direct wiring path back to the Cypher Board's own CPLD-side spade terminals.

## Decision

1. **The Plugboard board's only electrical connection is to the HID interconnect chain**, for
   passive termination of the broadcast/spoke JTAG signals (`TCK`, `TMS`, `CPLD_RESET_N`) at the
   end of the chain - exactly as already scoped in `merge-create-plugboard.md`. It carries **no**
   plugboard-signal-specific pins on its `J4`/`J6`-equivalent left connector; there is nothing left
   to define there.
2. **Physical plugboard patch jacks are mounted on the Plugboard board, but are not electrically
   connected to it.** The jacks are a mechanical-only fixture on that board (a convenient panel
   location within the enclosure). Each jack terminal is wired via a discrete spade-to-spade
   jumper cable **directly back to the Cypher Board's own spade terminal bank (`J20+`)** -
   bypassing the Plugboard board's own circuitry and the `J4`-`J7` HID interconnect stack
   entirely.
3. **Cypher Board's `J20+` spade bank general location is confirmed as the bottom edge of the
   rear face** (the HID interconnect connectors, `J5`/`J6`, remain at the top edge of the same
   face) - this is a general placement decision only; the exact per-tab arrangement/order within
   that bottom-edge region remains **TBD at layout**, unchanged from the existing note in
   `Board_Layout.md §7`.
4. **The `J4`/`J6` left pair (Cypher Board, and the equivalent connectors on Cypher-Input/
   Cypher-Output) gains reserved/spare `5V_MAIN` pins**, in case a future LED candidate (e.g. an
   addressable/"NeoPixel"-style part - see `merge-missing-components.md`) needs a supply above
   `3V3_ENIG`'s 3.3V. `5V_MAIN` already exists at the Cypher Board (via the Controller dock `J1`)
   and already has system precedent for LED power (User Settings Module harness `J19`). Reserving
   these pins now, while this connector's pinout is still open, costs nothing - unused reserved
   pins can be removed later if no LED candidate ends up needing them.

## Rationale

- Point-to-point spade wiring from the Cypher Board's existing spade bank is mechanically simpler
  and shorter than routing plugboard signals through 3 additional board-to-board connector stages
  (Cypher Board -> HID board 1 -> HID board 2 -> Plugboard board), each adding connector/trace
  length, cost, and failure points for signals that are fundamentally simple patch-cable
  continuity, not high-speed or timing-sensitive.
- Keeping the Plugboard board's electrical role limited to HID-chain JTAG termination (already
  scoped) avoids re-opening that board's design; only its mechanical/harness role changes.
- `5V_MAIN` is already present at the Cypher Board and already used elsewhere in the system for
  LED power (USM harness) - reserving spare pins for it on `J4`/`J6` is low-risk and keeps the
  door open for an addressable-LED candidate that needs more than 3.3V, without committing to
  using it.

## Impact

- `design/Electronics/Cypher/Design_Spec.md §6` (Interconnects) - clarify the spade bank (`J20+`)
  is wired via external point-to-point spade-to-spade harness to the Plugboard board's
  mechanically-mounted (electrically unconnected) jacks; remove any remaining "Plugboard
  passthrough" framing from the `J4`/`J6` left-pair description.
- `design/Electronics/Cypher/Board_Layout.md §4` (HID Interconnect) - update the `J5`/`J6` left
  pair intro to drop "Plugboard passthrough" and note reserved `5V_MAIN` pins instead;
  `Board_Layout.md §7` (`J20+`) - confirm bottom-edge-of-rear-face general location, arrangement
  still TBD at layout.
- `design/Electronics/Cypher-Input/Design_Spec.md §7` (Interconnects) - update the `J4`/`J6` left
  pair description to match (no Plugboard signals; reserved `5V_MAIN` pins added).
- `.copilot/todos/merge-create-plugboard.md` - rewritten to describe the passive HID-termination
  role plus the new mechanical-jack/spade-harness role, replacing the old "Plugboard passthrough
  signals TBD" framing.
- `design/Mechanical/Plugboard_Assembly/Design_Spec.md` - **not updated as part of this decision.**
  That document still describes the pre-Cypher standalone two-board-per-pass architecture and
  remains explicitly out of scope until the dedicated mechanical/software overhaul pass after the
  electronics merge completes (per existing `plan.md` direction). This DEC's harness concept
  should be carried forward into that future overhaul.
