# Checkpoint 185 — Cypher-Input Board Design Complete; Plugboard/5V_MAIN Architecture Clarified (DEC-088)

**Date:** 2026-08-16
**Session work:** A long review/cleanup session on the Cypher-Input board and related shared
Cypher Board docs, culminating in `merge-create-cypher-input` being marked **done** and a new
architecture decision (DEC-088) resolving its last blocking item.

---

## Status

- **`merge-create-cypher-input` is now `done`.** Its only remaining blocking item (left-side
  `J4`/`J6` Plugboard passthrough signal definition) is resolved via DEC-088: there are no
  Plugboard-specific signals on that connector at all.
- **`merge-create-plugboard`** updated to reflect the clarified architecture (passive HID-chain
  termination + mechanical-only jack mounting, spade-harness wired to the Cypher Board) but
  remains `pending` - the board itself still needs to be designed.
- **`merge-create-cypher-output`** notes synced to match (Plugboard passthrough wording replaced);
  still `pending` - this is the recommended next design task.
- **`cypher-input-led-independent-rgb-pwm-review`** and **`merge-missing-components`** (SK6812
  candidate) remain open/deferred as previously logged - unaffected by this session's changes.

---

## Changes made this session (since checkpoint 184)

| Area | Change |
| --- | --- |
| `BOARD_ROLE_ID` vs I2C wording | Removed incorrect "I2C address"/"I2C board-identification" framing for the `BOARD_ROLE_ID[2:0]` hardware strap across `Cypher/Board_Layout.md` and 4 Cypher-Input files; corrected the "board family / interface contract" note so custom keyboard boards reuse the shared `0x38` I2C address and only need their own `BOARD_ROLE_ID` value; added a note that unused `0b011`-`0b111` IDs are intended for software-mapped custom-board CPLD images |
| Historical-language sweep | Removed "retired"/"formerly"/"superseded"/"no longer"/"revised `<date>`" narration from `Cypher`/`Cypher-Input` Design_Spec/Board_Layout files - design docs now state only current facts; logged the remaining 10-file repo-wide sweep under `consolidate-design-spec-content` |
| `merge-diagrams-review` todo created | New todo (blocks `merge-final-review`) to review/update the stale `01-Rotor-Mini-Stack-Architecture.png`/`02-Mini-Stack-Vertical-Stack-Portrait.png` renders and create dedicated Cypher-system diagrams, embedded per-board in `Board_Layout.md` files |
| `ENC_ACTIVE_INPUT_N` naming | (Prior session, referenced) consolidated forwarded keypress-activity signal naming |
| Ē character fix | Replaced non-ASCII `Ē` (unapproved, not on the character matrix) with plain `` `E` (mux enable, active-low) `` in `Cypher_Input_64_Char_Design.md` |
| 64-Character variant naming | Renamed "64-Char Extended"/"Extended" to "64-Character" across 8 files, matching the Rotor board's "64-Character Variant" convention; left 2 unrelated JLCPCB-sourcing "(Extended)" tags untouched |
| Key indicator LED wording | Fixed a stale "driven entirely off the `plain-bits` bus" LED description (pre-DEC-087 leftover) in the Circuit Responsibility table |
| ASCII key layouts added | Added placeholder/real ASCII-art key layouts to `Cypher_Input_26_Char_Design.md` §2 (historical German Enigma 9-8-9 QWERTZ layout, `P` aligned under `Q`) and `Cypher_Input_64_Char_Design.md` §2 (provisional 42-key layout, to be superseded by the user's own mock layout/renders) |
| Single-sided JLCPCB assembly | Found and resolved a real constraint violation: `design/Production/JLCPCB_Manufacturing.md §3.1` states JLCPCB standard PCBA is single-sided-SMT only. Restructured Cypher-Input so **only LEDs + RV1** are top-face, hand-soldered by the user post-delivery (not part of the JLCPCB order) - everything else (resistors, ICs, connectors, sockets) is on the rear face, fully populated by JLCPCB's single-sided SMT pass |
| RGB mux moved to variant file | Per user request, moved the 64-Character-only colour-select mux (U9)/Shift-sense (D9/R9) circuit, its BOM rows, and its dedicated Mermaid diagram out of the common `Design_Spec.md` into `Cypher_Input_64_Char_Design.md` §5-§6; common file now describes only the generic single-colour architecture |
| SK6812MINI-E LED candidate | User proposed an addressable ("NeoPixel"-style) LED (Adafruit #4960) as a possible replacement for the placeholder RGB LED part. Confirmed datasheet + KiCad library zip already staged locally; generated a markdown datasheet via `.copilot/agent-scripts/generate_markdown_datasheets.py` and rebuilt `_generated_markdown_inventory.json`; logged full findings in `merge-missing-components.md` including a **critical open concern** (datasheet VDD spec 3.7-5.5V vs. system's 3.3V `3V3_ENIG` rail) and the required drive-circuit redesign (current R1-Rxx/U5-U9 topology is incompatible with an addressable single-wire-protocol LED) - **not yet approved for sourcing or import** |
| `cypher-input-led-independent-rgb-pwm-review` todo created | Per user request, for reviewing independent per-channel RGB PWM control (vs. today's on/off colour-select drive); explicitly excludes per-board-independent brightness oscillators as a separate, bigger, deferred change; sequenced between `merge-final-review` and `todo-clean-up-requirement-details` |
| **DEC-088 (new)** | Plugboard board's electrical role is passive HID-chain termination only (no plugboard-signal pins at all); physical patch jacks mount on it mechanically only, wired via spade-to-spade harness directly to the Cypher Board's own `J20+` spade bank (bottom edge of rear face - general location only, exact arrangement still TBD at layout); `J4`/`J6` left pair gains reserved/spare `5V_MAIN` pins for potential future LED power needs |

---

## Verification performed this session

- Re-grepped the full `design/` tree after each rename/wording pass to confirm no stale references
  remained (BOARD_ROLE_ID/I2C conflation, historical language, "Extended" naming, "Plugboard
  passthrough" wording).
- Confirmed markdownlint clean on every file touched this session.
- Extracted and cross-checked the actual SK6812MINI-E datasheet (pinout, VDD range, protocol
  timing, data structure/bit order) rather than assuming spec values.
- Confirmed the JLCPCB single-sided-SMT constraint directly from `JLCPCB_Manufacturing.md §3.1`
  before restructuring the assembly plan, rather than assuming.

---

## Next Session Start Point

**Recommended next task: `merge-create-cypher-output`** (lightboard/output panel board) - see
`.copilot/todos/merge-create-cypher-output.md` for the full note set already prepared (JTAG/
signal pin numbers, LED broadcast-consumer architecture per DEC-087, I2C addressing pattern per
DEC-086, now-synced Plugboard/5V_MAIN wording per DEC-088). In summary, this board:

1. Mirrors Cypher-Input's 4-connector HID interconnect architecture (J4/J5 top male, J6/J7 bottom
   female) - same left-pair/right-pair split, now with the same reserved `5V_MAIN` pins.
2. Needs **no local colour-select mux, Shift-sense network, or 555 oscillator** - it only
   receives the 4 broadcast signals (`RED_DRIVE_N`/`GREEN_DRIVE_N`/`BLUE_DRIVE_N`/
   `BRIGHTNESS_PWM_EN`) from whichever HID board is adjacent and applies them to its own LED bank
   (3x colour P-MOSFETs + 1x cathode-return N-MOSFET - same parts as Cypher-Input's own U5-U8).
3. Needs its own I2C GPIO expander (PCA9534A) for board-*type* identification, taking a fresh
   address from the `0x39-0x3E` pool (not `0x38`, which is Cypher-Input's) - connected to the same
   shared `I2C_SCL`/`I2C_SDA` bus, not a pure passthrough.
4. Will need its own `BOARD_ROLE_ID[2:0]` variant scheme once its own variant requirements (LED
   count/layout for whichever lightboard configurations exist) are confirmed with the user.
5. LED part remains the same TBD placeholder as Cypher-Input (SK6812MINI-E candidate under
   evaluation, or the original small-SMD-RGB placeholder) - do not source or finalise until that
   decision lands.
6. Should also get the same single-sided-JLCPCB-assembly treatment applied to Cypher-Input this
   session (LEDs hand-soldered top face only; everything else rear face, automated SMT).

After that: `merge-create-plugboard` (now well-scoped by DEC-088), then
`merge-cypher-board-j3j6-pinouts` (final pin numbers for the reserved `5V_MAIN`/LED broadcast
signals), then `merge-update-ctl-board`, working down the remaining `design-discussion-merge`
sub-tasks toward `merge-final-review`.
