# Review mechanical design for the new Cypher-Input/Cypher-Output/USM 3-part HID module

**ID:** `usm-3-part-hid-module-mechanical-review`
**Status:** pending
**Category:** Mechanical
**Source:** User request, 2026-09-16 (part of the wider USM redesign discussion)
**Blocked by:** the electronics-side USM redesign itself (connector topology, USM repurposing) —
action only once that is implemented, per the standing "electronics before mechanical" rule.

---

## Description

The redesigned User Settings Module (USM) is moving from a remote, panel-mounted board (connected
to the Cypher Board over a 6-wire harness) to a board that mounts **directly alongside**
Cypher-Input and Cypher-Output, connected to both via direct board-to-board connectors (see
`.copilot/discussions/usm-redesign/usm-connector-topology-review.drawio` for the connector-level
detail).

Mechanically, this forms one physical **3-part HID module**:

- Cypher-Input and Cypher-Output are stacked vertically (either order), as they already are today.
- USM sits to their right, rotated 90° relative to them, spanning the combined height of both
  boards — visualise 2 rectangles stacked on top of each other (Cypher-Input, Cypher-Output) with
  a third rectangle (USM) on their right edge, oriented perpendicular to them, so together the
  three boards form one larger rectangle (long edge at the bottom, short edges at the sides).
- USM has 4 physical connectors: one on its top edge (to the Cypher Board), one on its bottom edge
  (to the Cypher-Plugboard board), and two on its left edge (one to whichever HID board is
  currently on top, one to whichever is on the bottom).
- The assembled 3-part module screws down onto the top of the Enigma enclosure, positioned just
  in front of the Rotor Stacks.

## What this review needs to produce

1. Updated/new mechanical drawings for the combined 3-part module footprint, including how the 4
   USM connector mating points constrain relative board placement/alignment tolerances.
2. Confirmation of how the module attaches to the enclosure (fastening method, standoff/spacer
   requirements between the 3 boards, panel cutout implications if any exposed component - e.g.
   the buzzer/speaker chosen in `usm-buzzer-audio-options` - needs an acoustic port).
3. Update to `design/Mechanical/Main_Enclosure/Design_Spec.md` (and any other mechanical design
   docs referencing the old remote/panel-mount USM location) to reflect the new location and
   mounting method.
4. Confirmation of enclosure clearance in front of the Rotor Stacks for this combined module's
   footprint.

## Notes

- Deferred per the project's standing rule: mechanical/software sections are not touched until the
  electronics design is fully merged. This todo tracks the requirement so it is not lost, not to
  be actioned immediately.
- Depends on final connector positions being settled during PCB layout of Cypher-Input,
  Cypher-Output, and the redesigned USM, which is a separate (electronics) step that happens first.
- See also `usm-cfg-refmap-removal-review` (superseded by the wider USM redesign) and
  `cypher-input-led-independent-rgb-pwm-review` (LED implementation decision, may affect exact USM
  board outline/component placement, e.g. buzzer/speaker acoustic port location) for related
  context.
