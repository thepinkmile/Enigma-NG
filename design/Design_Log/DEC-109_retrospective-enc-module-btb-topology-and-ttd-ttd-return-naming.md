# DEC-109 - Retrospective: ENC Module BtB Connector Topology and TTD/TTD_RETURN Naming Convention

- **Status:** Decided
- **Date:** 2026-06-02 / 2026-06-06
- **Category:** Connector Topology / Signal Naming Convention
- **Area:** Cypher-Input, Cypher-Output, Stack-Output, Stack-Blanking, Stack-Interposer
- **Author:** Izzyonstage & GitHub Copilot

## Retrospective Note

This entry was **not recorded at the time the decisions were made**. Both decisions were
originally captured only in a working discussion document
(`.copilot/discussions/cypher-system-discussion/extension-mechanical-usage.md`, Entries 16 and
20), which several boards' own `Design_Spec.md` files cited directly as their rationale source.
Citing an informal discussion document from a live design spec is inconsistent with this
project's convention that historical/rationale content belongs in the Design Log. This DEC is
being written retrospectively (2026-10-29) to correct that gap before the discussion document is
moved to `.recycle-bin/`.

## Decision 1: ENC Module BtB Connector Topology (Entry 16)

The Cypher-Input and Cypher-Output boards each host one ENC (Encoder) module in their respective
cipher role via **three Hirose DF40C BtB receptacle sets**, carrying the full ENC-side signal
mapping (JTAG, ENC data, power) between the ENC module and the Cypher Board. The same three-set
DF40C topology and ENC-side signal mapping is shared identically by both boards (Cypher-Input and
Cypher-Output), since they both host functionally equivalent ENC modules differing only in role
configuration (Keyboard vs Lightboard).

## Decision 2: TTD / TTD_RETURN Naming Convention (Entry 20)

Within the rotor mini-stack signal-flow chain, the JTAG serial chain data signal is named
differently depending on its position in the chain, to avoid ambiguity:

- **TTD** - used for the signal on the interposer link (Stack-Interposer `J6`): the JTAG serial
  chain signal forwarded from the last Rotor Module's TDO output to Stack-Output, continuing on to
  Stack-Blanking. Not yet renamed at this point in the chain.
- **TTD_RETURN** - used for the signal on the stacking connectors (Stack-Input/Stack-Output
  `J1`/`J2`) after the Stack-Blanking Board renames the outbound TTD chain at the point it
  terminates and turns around. Propagates from the Stack-Blanking Board forward through
  Stack-Output, back through the mini-stack, to Stack-Input, and ultimately back to the Cypher
  Board.

## Rationale

Both decisions reflect the finalised Cypher-system mechanical/electrical interconnect topology
agreed during the extension-mechanical-usage discussion. Recording them here preserves that
rationale permanently in the Design Log rather than in a working discussion document that is
being retired now that the Cypher-system board merge is complete.

## Current Status

Both decisions remain in force. `Cypher-Input/Design_Spec.md §3`, `Cypher-Output/Design_Spec.md`,
`Stack-Output/Design_Spec.md`, `Stack-Blanking/Design_Spec.md`, and `Stack-Interposer/Design_Spec.md`
carry the current, non-historical statement of these conventions.
