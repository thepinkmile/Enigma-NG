# Reviewing mini-stack connector flush/protrude convention

**ID:** mini-stack-connector-flush-protrude-review
**Status:** pending
**Category:** Electronics / Mechanical Review
**Source:** User request, 2026-10-05
**Blocked by:** `usm-redesign-implementation`

---

## Description

While reviewing the Cypher system's board-to-board interconnects, the user identified that the
`Board_Layout.md` files had the flush/protruding mounting convention backwards for male vs.
female connectors. The correction applied (2026-10-05) across `Cypher/Board_Layout.md`,
`Cypher-Input/Board_Layout.md`, `Cypher-Output/Board_Layout.md`, and
`Cypher-Plugboard/Board_Layout.md`:

- **Male connectors** are mounted **protruding** past their board edge, far enough to span the
  enclosure gap and fully mate into the neighbouring board's connector.
- **Female connectors** are mounted **flush** with their board edge, so the socket opening sits
  flush with the enclosure edge/lid once cased, forming a clean opening for the mating board's
  protruding male pins to enter.

(Positions/roles - i.e. which physical connector is male vs. female at the top/bottom of each
board - are unchanged; only the flush-vs-protruding adjective assignment was swapped.)

## Scope for this pass

Once the Cypher system (`Cypher`, `Cypher-Input`, `Cypher-Output`, `Cypher-Plugboard`)
interconnect rebuild is fully complete and reviewed, check the mini-stack sub-system's own
`Board_Layout.md` files for the same mismatch - the user expects the same backwards
flush/protruding description is likely present there too, since it was inherited from the same
original authoring pass.

- Identify every board-to-board connector pair in the mini-stack sub-system.
- For each pair, confirm which side is male/female and correct the flush/protruding language to
  match the corrected convention above (protrude = male, flush = female).
- Cross-check against any owning/authoritative connector-template definition (as was done for
  the Cypher system's `Cypher/Board_Layout.md §4`), to avoid introducing a left/right or
  top/bottom inconsistency.

## Related

- Second stage of this correction (not yet started): add a placeholder connector-protrusion
  tolerance rule to `design/Standards/Global_Routing_Spec.md` (~0.02mm stack-up gap, pending
  confirmation against datasheet dimensions and PoC board testing), to be referenced generally
  and refined later on a per-connector-type basis.
