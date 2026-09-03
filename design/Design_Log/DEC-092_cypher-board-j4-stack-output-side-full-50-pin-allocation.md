# DEC-092 - Cypher Board `J4` (Stack-Output Side) Full 50-Pin Allocation

|Field|Value|
|:---|:---|
|**Decision ID**|DEC-092|
|**Status**|Decided|
|**Date**|2026-09-02|
|**Author**|Izzyonstage & GitHub Copilot|
|**Amends**|-|
|**Related**|DEC-090, DEC-091 (J3 companion connector)|

## Context

Following DEC-090/DEC-091's resolution of `J3` (Stack-Input side), `J4` (Stack-Output/REF-side)
remained the last connector on the Cypher Board with an incomplete 50-pin allocation - only 24 of
50 contacts were defined (`ENC_IN[5:0]`/`ENC_OUT[5:0]` return, `TTD_RETURN` ×2 for symmetry, GND).
Cross-checking against `Stack-Output/Design_Spec.md` surfaced the same class of gap found on `J3`:

1. **Missing `3V3_ENIG`.** Stack-Output's own `DR-SOUT-01`/§5 Power state it receives `3V3_ENIG`
   on this connector's power region (with no `5V_MAIN`, per `DR-SOUT-07`) - not present on the
   Cypher-side `J4` map at all.
2. **`J4` also carries the actuation-request chain.** Initial review assumed `J4` was purely a
   cipher-signal turnaround connector (ENC return + `TTD_RETURN`) with no actuation-chain role,
   since Stack-Output has no native Actuation Module circuitry (`DR-SOUT-07`). The user corrected
   this assumption - `J4` requires `ACTUATE_REQUEST_IN_N`/`ACTUATE_REQUEST_OUT_N` as well, though
   the exact internal routing/purpose of these signals on the Stack-Output side of the loop is not
   yet fully defined and is deferred to a dedicated follow-up review (see Open Item below).

## Decision

1. **`J4` is now fully 50-pin allocated**, following the same board-agnostic template convention
   as `J3`/`J5`/`J6` (fixed pin position → fixed signal role, center GND bar at pins 25/26),
   directly mirroring `J3`'s layout with the JTAG broadcast signals (`TCK`, `TMS`,
   `CPLD_RESET_N`) replaced by GND (not needed on this connector - those are broadcast via `J3`
   only) and `J3`'s two `5V_MAIN` groups consolidated into two additional `3V3_ENIG` groups (since
   this connector only ever carries the single `3V3_ENIG` rail). See `Cypher/Board_Layout.md §3`
   for the full map.
2. **`TTD_RETURN` occupies pin 30** - the same physical pin position as `TTD` (TDI-out) on `J3` -
   since it is conceptually the same JTAG line's return leg, terminating at FT232H U17 TDO via
   R50, per the existing §4 Signal Turnaround description.
3. **`ACTUATE_REQUEST_IN_N` (pin 16) and `ACTUATE_REQUEST_OUT_N` (pin 35) are added at the same
   pin positions as `J3`**, for board-agnostic template consistency across all four Cypher
   connectors that use this connector family.
4. **ESD protection reuses existing spare capacity - no new component required.** `J4`'s existing
   ESD IC U16 already had 3 of 4 channels unused (only `ENC_OUT[5]` (return) was assigned). Two of
   those spare channels now cover `ACTUATE_REQUEST_IN_N`/`ACTUATE_REQUEST_OUT_N`, leaving 1 channel
   still spare. No equivalent to DEC-091's U19 addition was needed on this connector.

## Rationale

- Deriving `J4`'s layout directly from `J3`'s finalised template (rather than designing it from
  scratch) keeps the two connectors' physical/electrical conventions consistent and minimises
  review overhead, while still correctly reflecting the real differences between the two
  connectors (no JTAG broadcast signals, single power rail instead of two).
- Reusing U16's pre-existing spare ESD channels avoids adding a new component purely for
  symmetry with `J3`/DEC-091, since `J4` genuinely had headroom already provisioned.

## Open Item (Not Resolved by This Decision)

The exact internal routing of `ACTUATE_REQUEST_IN_N`/`ACTUATE_REQUEST_OUT_N` between `J3`, `J4`,
and CPLD U1 on the Cypher Board - and the equivalent routing through the Rotor boards and the
Stack-Interposer Board - is **not yet fully defined**. The user has indicated these nets are
intended to behave as a direct passthrough at each board (rear-connector `IN` wired directly to
front-connector `OUT`, and front-connector `IN` wired directly to rear-connector `OUT`), which
appears to sit alongside (not necessarily replace) the CPLD-arbitrated model described in
DEC-090. A dedicated follow-up review of the Rotor and Stack-Interposer connectors is planned to
fully trace and document the `ACTUATE_REQUEST` signal path end-to-end before this is considered
resolved.

## Impact

- `Cypher/Board_Layout.md §3` - `J4` full 50-pin map added, replacing the 24-defined/26-GND-
  placeholder table.
- `Cypher/Design_Spec.md §4` - Signal Turnaround section gains power-entry and actuation-request
  notes; ESD protection list updated (U16 channel reassignment, no new component).
- `merge-cypher-board-j3j6-pinouts` todo - fully resolved; all four Cypher connectors (`J3`-`J6`)
  now have complete 50-pin allocations.
- Follow-up work opened: Rotor and Stack-Interposer connector review to fully define
  `ACTUATE_REQUEST_IN_N`/`OUT_N` routing end-to-end.
