# DEC-097 - Cypher `J3` `ACTUATE_REQUEST_OUT_N` Wired to CPLD as Round-Trip Verification Input

|Field|Value|
|:---|:---|
|**Decision ID**|DEC-097|
|**Status**|Decided|
|**Date**|2026-09-02|
|**Author**|Izzyonstage & GitHub Copilot|
|**Amends**|DEC-090 (changes the `ACTUATE_REQUEST_OUT_N` wiring on Cypher's `J3` from NC to a live CPLD input + idle-bias resistor; pin position unchanged)|
|**Related**|DEC-091, DEC-093, DEC-096|

## Context

DEC-090 left Cypher's `J3` pin 35 (`ACTUATE_REQUEST_OUT_N`) as NC, reasoning that Cypher
originates the actuation-request round trip and never needs to consume an incoming request.
Reviewing this against the full round-trip path (DEC-093) identified two issues with plain NC:

1. In normal operation (≥1 mini-stack attached) this pin is actively driven by Mini-Stack 1's
   Stack-Input `J1` (itself a live passthrough sourced through the entire round trip) — so it is
   not simply unused.
2. In the Stack-Blanking Board's bench/transport mode (plugged directly into Cypher's `J3`/`J4`
   with no mini-stacks attached, per `DR-SBLK-02`/`03`), both ends of this connection are inputs
   with nothing driving either side — the pin genuinely floats, inconsistent with every other
   idle-bias-protected signal in this design (JTAG spoke ends, the former `ENC_ACTIVE_N`
   termination, Stack-Output's power-pin 0Ω links).

## Decision

`ACTUATE_REQUEST_OUT_N` (Cypher `J3` pin 35) is wired to **both**:

1. **CPLD U1**, as a genuine input. U1's firmware compares this value against the
   `ACTUATE_REQUEST_IN_N` it originally issued, providing a system self-test: confirmation that
   the actuation-request signal successfully completed its full round trip through the entire
   30-rotor stack (per the DEC-093 path) rather than stalling or getting lost somewhere in the
   chain.
2. **R51**, a 10 kOhm 0402 pull-up to `3V3_ENIG` — defines the idle/disconnected state (notably
   the Stack-Blanking bench-mode case above), consistent with the idle-bias convention already
   used throughout this design.

## Rationale

- A CMOS-class input left genuinely floating in a real (if edge-case) operating mode is
  inconsistent with this design's own established practice of biasing every signal that could
  ever be disconnected.
- Making the pin a real CPLD input (rather than just adding a bias resistor with no functional
  use) turns an otherwise-wasted pin into a useful diagnostic/validation signal, at negligible
  additional cost (the CPLD already has spare I/O headroom on this connector's template).

## Impact

- `Cypher/Board_Layout.md §2` — `J3` wiring note updated: pin 35 now CPLD input + R51, not NC.
- `Cypher/Design_Spec.md §3` — Actuation Request Chain description updated (step 6 termination
  language); new FR-STA-14, DR-STA-19; new R51 BOM row; mermaid diagram updated.
- `Stack-Input/Design_Spec.md`, `Board_Layout.md` — references to Cypher's `J3` pin 35
  "terminating NC" corrected to describe the round-trip completion check.
- No pin position, connector, or signal name change — purely an internal wiring addition on the
  Cypher Board.
