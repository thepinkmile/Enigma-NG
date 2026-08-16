# Review and update draw.io diagrams for the Cypher system merge

**ID:** merge-diagrams-review
**Status:** pending
**Category:** Documentation / Diagrams
**Source:** User request, 2026-08-15
**Blocked by:** merge-create-cypher-output, merge-create-plugboard

---

## Description

The `design/Diagrams/cypher-system-layout.drawio` file and its renders in
`design/Diagrams/renders/` were authored before the Cypher-family boards' interconnect
architecture was finalised (4-connector `J4-J7` HID template, JTAG chain reorder, LED
colour/brightness broadcast on the left connector pair, etc.). As a result the current renders no
longer match the design they claim to depict.

Known-incorrect renders (at minimum):

- `design/Diagrams/renders/01-Rotor-Mini-Stack-Architecture.png` - needs updating for the `J4-J7`
  connectors between the Cypher Board and Plugboard blocks (interconnect architecture has moved on
  since this render was produced).
- `design/Diagrams/renders/02-Mini-Stack-Vertical-Stack-Portrait.png` - same `J4-J7`
  Cypher-Board-to-Plugboard connector inconsistency.

Both are referenced from multiple boards' `Board_Layout.md §Diagram Reference` sections
(`Cypher`, `Cypher-Input`, `Stack-Input`, `Stack-Output`, `Stack-Blanking`, `Stack-Interposer`) via
`design/Diagrams/cypher-system-layout.drawio` and `design/Diagrams/renders/`, so any correction
needs to stay consistent across every board that cross-references them.

## Direction for this pass

Rather than patching the existing Rotor-Mini-Stack-oriented diagrams in place, this pass should:

1. **Create new diagrams specific to the Cypher system** (Cypher Board + Cypher-Input +
   Cypher-Output + Plugboard + their `J4-J7` interconnect architecture) as their own dedicated
   diagram set, separate from the Rotor Mini-Stack diagrams.
2. **Reduce the scope of the existing Rotor-based diagrams** so they focus on the Rotor Mini-Stack
   itself, rather than also trying to depict the now-more-complex Cypher-side HID interconnect.
3. **Embed/call out the new Cypher-system diagrams directly from each relevant board's
   `Board_Layout.md`** (e.g. `Cypher/Board_Layout.md`, `Cypher-Input/Board_Layout.md`,
   `Cypher-Output/Board_Layout.md` once created, `Plugboard/Board_Layout.md` once created), rather
   than relying solely on the current generic "see `cypher-system-layout.drawio`" cross-reference.

## Notes

- This must be actioned before `merge-final-review` signs off the design-discussion merge - the
  diagrams are part of the design documentation set, and stale renders would leave the merge
  visually inconsistent with the text specs even if the specs themselves are correct.
- Wait until `merge-create-cypher-output` and `merge-create-plugboard` are both `done` before
  finalising the new diagrams, since the `J4-J7` connector pinout on those boards (left pair —
  Plugboard passthrough + LED broadcast) is not yet fully locked (see `merge-cypher-board-j3j6-pinouts`).
- Preserve the existing Rotor Mini-Stack renders' file history where practical (e.g. via git) if
  they are being trimmed/reduced in scope rather than fully replaced.
