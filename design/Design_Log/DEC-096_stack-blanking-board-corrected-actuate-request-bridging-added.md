# DEC-096 - Stack-Blanking Board Corrected: ENC_ACTIVE_N/ACTUATE_REQUEST_N Termination Removed; ACTUATE_REQUEST Bridging Added

|Field|Value|
|:---|:---|
|**Decision ID**|DEC-096|
|**Status**|Decided|
|**Date**|2026-09-02|
|**Author**|Izzyonstage & GitHub Copilot|
|**Amends**|-|
|**Related**|DEC-090, DEC-091, DEC-093, DEC-094, DEC-095|

## Context

An ESD/connector audit (DEC-095) surfaced that the Stack-Blanking Board's design had not been
updated to match the current `ACTUATE_REQUEST` signal model (DEC-093) or the `ENC_ACTIVE_N`
scoping confirmed during the `J3` pinout work (DEC-090):

1. **`R1` (ENC_ACTIVE_N pull-up) is stale.** `ENC_ACTIVE_N` is confirmed HID-local-only (Cypher
   Board ↔ Cypher-Input ↔ Cypher-Output only) and never appears on the STA/REF chain at all —
   there is nothing for this resistor to terminate.
2. **`R5` (ACTUATE_REQUEST_N pull-up) is based on an obsolete model.** The Stack-Blanking Board's
   design predates DEC-093, which established that `ACTUATE_REQUEST` is not a signal that
   dead-ends at the chain terminus — it is a full round-trip signal that originates and
   terminates at the Cypher Board's own CPLD, reflecting **twice** at this board (STA-chain →
   REF-chain, and later REF-chain → STA-chain in reverse). A dead-end pull-up is functionally
   wrong for this signal.

## Decision

1. **`R1` (ENC_ACTIVE_N) and `R5` (ACTUATE_REQUEST_N) are removed entirely** from the
   Stack-Blanking Board — no replacement termination is required for either.
2. **The remaining three termination resistors are renumbered** to close the gap: `R2`→`R1` (TCK
   pull-down), `R3`→`R2` (TMS pull-up), `R4`→`R3` (CPLD_RESET_N pull-up). These three signals
   (TCK, TMS, CPLD_RESET_N) are the only ones that genuinely dead-end at this board.
3. **Two new bridging paths are added**, following the same passive J1↔J2 trace-routing pattern
   already used for SIG-BLOCK-A/B, C/D, and E/F:
   - `ACTUATE_REQUEST_OUT_N` (arriving on J1, from the last mini-stack's Stack-Input, the STA-chain
     forward-pass terminus) is bridged to `ACTUATE_REQUEST_REF_IN_N` (departing via J2 into the
     REF-chain) — the first turnaround in the DEC-093 round trip (step 3).
   - `ACTUATE_REQUEST_REF_OUT_N` (arriving on J2, from Stack-Output, the REF-chain second-forward
     pass terminus) is bridged to `ACTUATE_REQUEST_IN_N` (departing via J1 into the STA-chain in
     reverse) — the second turnaround (step 6).
4. Cross-references to the connector-defining boards are updated to reflect DEC-094 (Stack-Input
   owns `J1`'s template, Stack-Output owns `J2`'s template — not Cypher), and stale
   `merge-cypher-board-j3j6-pinouts` references are removed.

## Rationale

- Bridging (not terminating) `ACTUATE_REQUEST` at this board is the only design consistent with
  DEC-093's round-trip model — the signal must physically continue past this board twice, not
  stop here. This exactly mirrors how the same board already correctly bridges (rather than
  terminates) every other passthrough signal in the system (ENC data, TTD).
- Removing the two resistors that no longer correspond to any real signal at this board (rather
  than leaving them stubbed/NC) keeps the BOM and schematic honest about what's actually
  connected, avoiding a future reviewer wondering what `R1`/`R5` are for.
- Renumbering the remaining resistors closes the gap left by the removals, consistent with this
  project's established renumbering practice (e.g. DEC-055, the Rotor RefDes gap-removal
  precedent).

## Impact

- `Stack-Blanking/Design_Spec.md` — Overview responsibility table, FR-SBLK-05/06/07 (06/07
  repurposed for the new bridging FRs), DR-SBLK-02/03/05/07, mermaid diagram, §3 Signal Routing
  and Termination (both tables), §4 Interconnects, BOM all updated. Resistor count reduced from
  5 to 3.
- `Stack-Blanking/Board_Layout.md` — J1/J2 sections and §3 Signal Bridge Summary updated to
  match.
- `merge-actuate-request-routing` todo — Stack-Blanking Board scope now resolved.
