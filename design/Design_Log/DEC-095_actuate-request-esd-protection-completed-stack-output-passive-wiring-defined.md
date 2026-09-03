# DEC-095 - ACTUATE_REQUEST ESD Protection Completed (Stack-Input, Stack-Output); Stack-Output Passive Wiring Defined

|Field|Value|
|:---|:---|
|**Decision ID**|DEC-095|
|**Status**|Decided|
|**Date**|2026-09-02|
|**Author**|Izzyonstage & GitHub Copilot|
|**Amends**|-|
|**Related**|DEC-090, DEC-091, DEC-092, DEC-093, DEC-045, DEC-048|

## Context

An ESD audit of every connector carrying the new `ACTUATE_REQUEST*` signals (per DEC-093) found
two boards where the existing ESD arrays had no spare channel capacity, mirroring the same
constraint already found and fixed on the Rotor boards and (for `J3`) on Cypher:

1. **Stack-Input `J1`** (live-swap, IC-STA-CHAIN front connector): existing U3 (JTAG, 4ch) + U4-U6
   (ENC, 12ch) = 16/16 channels fully used - 0 spare for the 2 new pins.
2. **Stack-Input `J5`** (live-swap, mates with Rotor `J3`, which now carries the actuate pins):
   existing U7 (JTAG, 4ch) + U8-U10 (ENC, 12ch) = 16/16 fully used - 0 spare.
3. **Stack-Output `J5`** (live-swap, mates with Rotor `J6`, which now carries the actuate pins):
   existing U5 (JTAG, 4ch) + U6-U8 (ENC, 12ch) = 16/16 fully used - 0 spare.

Stack-Output's `J1` (IC-REF-CHAIN) already had sufficient spare capacity (U4: 2 of 4 channels
previously unused) and needed no new component. Stack-Interposer and Stack-Blanking do not
require ESD at all (not live-swap-accessible per their existing design).

Separately, Stack-Output's own internal wiring for `ACTUATE_REQUEST_REF_IN_N`/
`ACTUATE_REQUEST_REF_OUT_N` (flagged as "not yet defined" in DEC-093/DEC-094) is now defined:
since Stack-Output has no active ICs (CPLD/MCU) at all, both nets are simple passive
J1↔J2 passthroughs, exactly mirroring the existing SIG-BLOCK-B/C/F handling on the same connector
pair.

## Decision

1. **Stack-Input gains two new ESD ICs**, both extra counts of the existing
   `TPD4E05U06QDQARQ1` part (no new part number): **U11** (`J1`, protects
   `ACTUATE_REQUEST_IN_N`/`ACTUATE_REQUEST_OUT_N`, 2 channels used/2 spare) and **U12** (`J5`,
   protects the same two nets where they mate with Rotor `J3`'s pins 13/14, 2 channels used/2
   spare).
2. **Stack-Output gains one new ESD IC**: **U9** (`J5`, protects
   `ACTUATE_REQUEST_OUT_N`/`ACTUATE_REQUEST_IN_N` where they mate with Rotor `J6`'s pins 13/14, 2
   channels used/2 spare) — extra count of the same existing part.
3. **Stack-Output's `J1`↔`J2` `ACTUATE_REQUEST_REF_IN_N`/`REF_OUT_N` wiring is a passive
   passthrough**: `ACTUATE_REQUEST_REF_IN_N` follows the same `J2 → J1` direction as SIG-BLOCK-B/F
   (toward Cypher); `ACTUATE_REQUEST_REF_OUT_N` follows the same `J1 → J2` direction as
   SIG-BLOCK-C (toward the Stack-Blanking Board/next mini-stack). ESD for both is covered by
   `J1`'s existing U4 spare channels (no new component on `J1`).
4. **Stack-Output's `J5`↔`J6` interposer-link wiring is also a passive passthrough**, formalised
   as new signal blocks **SIG-BLOCK-G** (`J5 → J6`, forward, collected from the last ROT board's
   own carry mechanism) and **SIG-BLOCK-H** (`J6 → J5`, return, received from the
   Stack-Interposer Board), consistent with the existing SIG-BLOCK-A/D/E handling on this
   connector pair.

## Rationale

- Reusing the existing `TPD4E05U06QDQARQ1` part as extra-count ICs (rather than sourcing a new
  ESD part) keeps this consistent with the pattern already established and approved for Cypher's
  U19 and Rotor's U12/U13.
- Since Stack-Output has no active silicon anywhere on the board, every signal it carries is
  necessarily a passive passthrough — the same reasoning already applied to every existing
  SIG-BLOCK on this board applies identically to the two new actuate signals; no new decision
  logic was needed to reach this conclusion once the board's existing all-passive nature was
  taken into account.

## Open Item Found During This Audit (Not Resolved by This Decision)

**The Stack-Blanking Board's current design is inconsistent with the DEC-093 signal path** and
was not in scope for this ESD-focused pass:

- Its `Design_Spec.md` still treats `ACTUATE_REQUEST_N` as a single signal that **dead-ends** at
  this board (R5, a 10kΩ pull-up terminator) — but per DEC-093, the Stack-Blanking Board is
  actually the **reflection point** for the actuate signal (twice: once turning the STA-chain
  signal into the REF-chain, and again turning the REF-chain signal back into the STA-chain in
  reverse), not a dead end.
- It also still lists `ENC_ACTIVE_N` as a signal terminating at this board (R1, pull-up) — this
  is stale, predating the DEC-093 confirmation that `ENC_ACTIVE_N` never appears on the STA/REF
  chain at all.
- Several stale `merge-cypher-board-j3j6-pinouts` references remain (now-closed todo).

This requires a functional redesign (removing/repurposing R1 and R5, adding new bridging logic
mirroring FR-SBLK-02/03/04 for the two new actuate reflection passes) rather than a
straightforward documentation sync, and has been raised separately for explicit approval before
any changes are made.

## Impact

- `Stack-Input/Design_Spec.md` (§8 Thermal & ESD, FR-EXT-07, DR-EXT-12, BOM, mermaid diagram) —
  new U11/U12 ESD ICs.
- `Stack-Output/Design_Spec.md` (§3 Signal Return Path, §8 Thermal & ESD, FR-EXT-07, DR-EXT-12,
  BOM, mermaid diagram) and `Board_Layout.md` (§1, §2, §3) — new U9 ESD IC; `ACTUATE_REQUEST_REF_IN_N`/
  `REF_OUT_N` and SIG-BLOCK-G/H passive wiring defined.
- `merge-actuate-request-routing` todo — Stack-Output's own actuate wiring/ESD now resolved;
  Stack-Blanking Board's inconsistency added as new scope.
