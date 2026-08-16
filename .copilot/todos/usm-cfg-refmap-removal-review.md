# Revisit User Settings Module Bank 2 / CFG_REFMAP removal before next full design review

**ID:** usm-cfg-refmap-removal-review
**Status:** pending
**Category:** Electronics / Architecture Review
**Source:** User request, 2026-08-16
**Blocked by:** (none - informational tracking todo)

---

## Description

On 2026-08-16, the former Bank 2 (`CFG_REFMAP[5:0]` reflector-map selection) hardware was removed
from the User Settings Module (`SW5-SW10`, `D6-D12`, `U3` and its associated colour-rail/anode-
drive transistors and resistors) as an **interim step** to free CPLD I/O headroom on the Cypher
Board (see the `BOARD_ROLE_ID`/HID-variant-comparator discussion). This was explicitly flagged by
the user as temporary, pending a fuller redesign discussion.

RefDes gaps left by the removal (`SW5-SW10`, `D6-D12`, `U3`, `Q4-Q6`, `Q12-Q18`, `Q24-Q30`, and the
corresponding resistor sub-ranges - `R6-R11`, `R15-R17`, `R23-R29`, `R40-R53`, `R59-R65`, `R71-R77`,
`R81-R83`, `R89-R95`, `R98`) were **deliberately not renumbered** in that pass, to avoid doing the
renumbering work twice.

## What still needs resolving before this can be considered final

1. ~~**Reflector-map configuration mechanism.**~~ **Resolved 2026-08-16 (DEC-089).** The 6-bit
   `CFG_REFMAP[5:0]` value is replaced entirely by a JTAG-based mechanism: the CM5 writes the
   active map index directly into the Cypher Board's own CPLD (U1) UFM via the existing JTAG
   chain (in-system UFM write via the FT232H JTAG bridge) at configuration-apply time, with no
   dedicated parallel GPIO bus. This is documented in `Cypher/Design_Spec.md` (FR-STA-09,
   DR-STA-11, DR-STA-13, new §3a `BOARD_ROLE_ID` Compatibility Comparator section) - the CPLD I/O
   freed by this change (6 pins) was reallocated to the `BOARD_ROLE_ID`/`HID_VARIANT_ID`
   compatibility comparator per the same decision. Firmware-level detail of the UFM write
   sequence itself is still deferred to a later pass.
2. ~~**Stator CPLD `CFG_REFMAP[5:0]` input path**~~ **Resolved 2026-08-16.** "Stator" is the
   Cypher Board's own legacy FR/DR-ID prefix (`STA`) - there is no separate Stator board; the
   Cypher Board's own CPLD (U1) is what previously read `CFG_REFMAP[5:0]` and now performs the
   JTAG UFM write instead. `Cypher/Design_Spec.md` FR-STA-09/DR-STA-11/DR-STA-13 and the U8 GPIO
   table have been updated to remove all references to the old parallel bus and its pull-down
   resistors.
3. **RefDes renumbering.** Once the final replacement architecture is confirmed (does Bank 2
   hardware come back in a different form, stay fully removed, or get replaced by something else
   entirely on the USM?), do a full consecutive RefDes renumber across the User Settings Module's
   `Design_Spec.md`/`Board_Layout.md` (switches, LEDs, MCP23017 expanders, MOSFETs, resistors,
   capacitors) to close the gaps left by this interim pass.
4. **Power budget / component count final pass** - recheck once the above is settled; current
   USM `Design_Spec.md §11`/§12 numbers reflect Bank 1-only hardware as an interim state.

## Notes

- User indicated (2026-08-16) they may have "another discussion we will merge later that may
  resolve all of this" - check for that before starting this review, since it may already answer
  the reflector-map-mechanism question above.
- This todo is intentionally not hard-blocking anything else in the merge sequence - it's a
  tracking/reminder item to action **before the next full design review pass** (i.e. before
  `review-pass-11`/whichever is the next pending full review gate), not before any specific
  Cypher-family board todo.
