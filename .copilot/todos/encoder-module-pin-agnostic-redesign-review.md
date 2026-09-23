# Reviewing Encoder Module design to make it role-agnostic with direct CPLD-pin-to-connector-pin mapping

**ID:** encoder-module-pin-agnostic-redesign-review
**Status:** pending
**Category:** Electronics / Architecture Review
**Source:** User request, 2026-09-18

---

## Description

Review and likely redesign `design/Electronics/Encoder_Module/Design_Spec.md` and
`Board_Layout.md` so the module becomes a true multi-purpose, role-agnostic board: the module
itself should carry only the CPLD/FPGA (`U1`) and required passive components (decoupling
capacitors, JTAG/reset pull-ups), with its own docs defining a direct mapping from each CPLD/FPGA
pin straight to a connector pin (`J1`/`J2`/`J3`) - no role-dependent signal naming (e.g. no more
`PB[]`/`CB[]`/`ENC_ACTIVE_N` framed as fixed-role signals baked into the module's own spec). Each
carrier board (Cypher, Cypher-Input, Cypher-Output, Rotor, Stack-Input/Output, etc.) then owns its
own pin-to-signal usage table describing how it uses that carrier-agnostic pinout for its own
purpose.

Triggered by a specific gap found while updating Cypher-Input/Cypher-Output's ENC module
placeholder tables: the module's `J2` currently defines only ONE `ENC_ACTIVE_N` pin, direction
role-dependent (`KBD_ENC` drives it, `LBD_DEC` consumes it) - the USM-redesigned system needs two
logically distinct signals (an INPUT-role activity signal and an OUTPUT-role activity signal) to
support deterministic propagation timing against the Rotor/Stack encoder chain (see the explicit
note in Cypher-Input/Cypher-Output's own `Design_Spec.md` and `Board_Layout.md` that
`ENC_ACTIVE_INPUT_N`/`ENC_ACTIVE_OUTPUT_N` must only ever originate from/terminate at the Cypher
Board, never be tapped by an intermediate HID board). The current single bidirectional-by-role
`ENC_ACTIVE_N` pin cannot cleanly support this without ambiguity.

User may end up describing/solving this a different way once the wider role-agnostic redesign is
examined - do not assume the two-pin solution is final, this todo exists to work through the
options.

## Additional known issue to fix as part of this review (2026-09-23)

Cypher-Input's own `Board_Layout.md §1` (`J4` ENC module mount pin table) currently reproduces the
Encoder Module's full 64-position `PB[]` zig-zag table as if all 64 positions were always relevant.
This is only accurate for the 64-Character variant - the 26-Char Classic and 10-Numeric variants
only ever populate a subset of those 64 positions (see each variant's own `plain-bits` allocation
in their own design file). This has been left as-is intentionally pending this review, since the
correct fix is tied up in the same role-agnostic pin-mapping rework (once the module exposes a
direct CPLD-pin-to-connector-pin table instead of a fixed `PB[]` bus, each carrier board's own
usage table can correctly show only the positions it actually uses, per variant). Do not fix this
piecemeal before the wider rework - revisit it here.
