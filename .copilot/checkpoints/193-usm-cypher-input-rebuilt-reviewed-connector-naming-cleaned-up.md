# Checkpoint 193 — USM Redesign Rebuilt Cleanly; Cypher-Input Reviewed & Corrected; Connector Naming Cleaned Up

**Date:** 2026-09-23
**Status at checkpoint:** USM and Cypher-Input fully rebuilt and reviewed by the user. Paused for
a token-limit reset; resume with Cypher-Output next.

---

## Summary

Following the prior session's discovery that a background agent had destructively rewritten 8 of
9 files during the USM redesign implementation, the user reverted `main` back to a clean state
(preserving the full damaged attempt on `branches/usm-updates-attempt-1` for reference only) and
this session redid the work by hand, one board at a time, with the user reviewing and correcting
each file directly.

## What Is Done and User-Reviewed

1. **User Settings Module** (`Design_Spec.md` + `Board_Layout.md`) — fully rebuilt:
   - Role: shared LED-colour/audio/JTAG-I2C spine board for the Cypher HID assembly.
   - **4 colour styles** (not 3) stored in `U1` (exact device TBD, reserved I2C `0x39`) - the
     initial system configuration uses 3 (Colour1 = idle baseline, Colour2 = key-press, Colour3 =
     shifted key-press), Colour4 reserved for future use. This 3→4 expansion was itself a
     mid-session correction (see DEC-107 below).
   - `RV1` shared brightness dial, `BZ1` audio-warning placeholder, `R1`-`R3` JTAG idle
     termination - all hosted on USM.
   - Two connector templates, both fully pinned out in `Board_Layout.md` (NOT duplicated in
     `Design_Spec.md`, which only has prose + pointers): the **Hub Connector Template** (`J1` top,
     mates Cypher; `J2` bottom, mates Cypher-Plugboard - identical pin map, `TDI`/`TDO` NC on
     `J2`) and the **HID-Facing Connector Template** (`J3` left-upper, `J4` left-lower - identical
     pin map, either HID board may occupy either port; carries all 4 colour styles'
     `RED`/`GREEN`/`BLUE`/`ILLUMINATION_DRIVE_{1-4}_N` signal groups plus role-specific
     `TDI_INPUT`/`TDO_INPUT`/`TDI_OUTPUT`/`TDO_OUTPUT`).
   - **Naming convention fixed:** the connectors were initially called "Template 2"/"Template 3"
     (bare numbers, no meaning) - the user objected and they are now called by function only:
     "Hub Connector Template" and "HID-Facing Connector Template". **This same fix was then
     applied to `Cypher-Input/Design_Spec.md`**, which had two leftover bare "Template 1"/
     "Template 3" references (now "Cypher Left Pair Template" and "HID-Facing Connector
     Template"). A repo-wide grep confirmed no other file contains bare "Template 1/2/3" text.
   - Several user-caught doc-quality issues fixed along the way (this is a recurring pattern this
     session - see "Recurring review issues" below): historical/past-tense wording, describing
     another board's own internal wiring instead of only this board's own side, an out-of-place
     mention of a template ("Template 1") that doesn't even belong to this board, `Bulk Entry
     Bank Rule` wording not matching the phrase already established on the Cypher board, and an
     honestly-open (not falsely-resolved) ESD question for `RV1` (operator-touched potentiometer
     knob - GRS §9 only scopes connectors, no established precedent found for this case).
2. **Cypher-Input** (`Design_Spec.md`, `Board_Layout.md`, all 3 variant files) — fully rebuilt and
   reviewed:
   - RefDes renumbered: `J1`/`J2` = Cypher left pair, `J3` = USM connector, `J4`-`J6` = ENC module
     mount.
   - Connector pin maps are NOT duplicated here - owned by `Cypher/Board_Layout.md §4` (Cypher
     Left Pair Template) and `User_Settings_Module/Board_Layout.md` (HID-Facing Connector
     Template) respectively; this board's own docs state only its own row usage and local wiring.
   - `ENC_ACTIVE_INPUT_N`/`ENC_ACTIVE_OUTPUT_N` propagation-delay constraint documented explicitly
     (must only originate/terminate at Cypher, never tapped by an intermediate HID board).
   - LED colour architecture repointed to USM's 4-colour-style signal groups (local `U5`-`U8`
     drive stage retained as-is; only the signal *source* changed). `U4`'s role reduced to Board
     ID + Space/Enter only.
   - `Cypher_Input_64_Char_Design.md` restored from an earlier accidental near-total rewrite back
     to full original detail, with only the LED section (§5) genuinely updated: removed the
     obsolete local `U9`/`D9`/`R9` Colour-A/B mux (colour is now USM-sourced), and correctly
     stated the real behaviour - Shift is a **global** state (not per-key): holding it switches
     **all** keys' baseline from Colour1 to Colour3, with the pressed key still showing Colour2 on
     top of whichever baseline is active.
   - **User-caught fixes this pass (2026-09-23):** "a future Plugboard board" → "Cypher-Plugboard"
     (it's a real, current board, not a hypothetical); an out-of-place Space/Enter/`U4` note
     removed from a connector-pinout table (that fact already lives independently in
     `Design_Spec.md §3a`); a **logic error** in the passthrough description was caught and fixed
     - passthrough only happens when this board is the one **directly facing Cypher** (relaying
       to whichever board sits beneath it); the Plugboard-facing position is the actual dead end
       with nothing to relay to (the original wording had this backwards).
3. **DEC-107** created — "USM/HID Connector Four-Colour-Style Signal Expansion": documents why
   Template 3 (now HID-Facing Connector Template) needed 4 independent colour-style signal groups
   instead of 1 generic one (a HID board's own local mux logic needs simultaneous access to more
   than one stored colour value - e.g. the 64-Char variant's Shift-triggered switching - which a
   single broadcast group cannot provide).
4. **New/updated todos this session:**
   - `encoder-module-pin-agnostic-redesign-review` (`.copilot/todos/`) — recreated on disk (was
     DB-only, lost during the revert) with its original scope (make the Encoder Module carry only
     CPLD/FPGA + passives, with direct pin→connector mapping owned by the module and per-carrier
     usage tables) **plus a new note**: Cypher-Input's own `J4` ENC-mount pin table currently
     (incorrectly) shows the full 64-position `PB[]` bus as if relevant to every variant - only
     true for 64-Character; 26-Char/10-Numeric only use a subset. Deliberately left unfixed
     pending this wider rework.
   - `usm-template2-template1-unification-review` (new) — captures the user's question of whether
     the Hub Connector Template should just reuse the Cypher Left Pair Template's full pin map
     (marking unused pins NC) for future flexibility. Explicitly not to be actioned without further
     discussion.
   - `todo-clean-up-requirement-details` — expanded with a concrete example
     (`Cypher-Input/Design_Spec.md`'s `DR-CYPI-09` → `DR-CYPI-11a` numbering gap) and broadened
     scope to include gap-free FR/DR renumbering repo-wide, not just removing implementation
     detail from requirement text.
   - `cypher-input-led-independent-rgb-pwm-review` — two new notes added: (a) if addressable LEDs
     are chosen, they're expected to move to the rear face and join the standard JLCPCB SMT pass
     (removing a manual hand-soldering step), a real production-simplification factor for the
     PoC/decision; (b) a candidate use for the previously-unused Colour4 style: "shifted + pressed"
     as a 4th distinct indicator, instead of just overlaying Colour2 on every baseline regardless
     of Shift state - not decided, just captured as an idea.
   - All of the above synced into `.copilot/todos/todos.sql` and `.copilot/todos/index.md` for
     persistence (some had only existed in the session DB, not on disk, from before the
     mid-session revert - this gap is now closed).
   - `usm-redesign-implementation` is `in_progress` (correctly, since Cypher-Output,
     Cypher-Plugboard, and Cypher's own connector/role updates are not yet redone).

## Recurring Review Issues This Session (pattern to watch for next session too)

The user's review of both USM and Cypher-Input caught the same handful of issue classes
repeatedly - worth actively checking for these before presenting Cypher-Output/Cypher-Plugboard/
Cypher for review, to save review cycles:

1. **Historical/past-tense wording** creeping into "current design only" docs (e.g. "relocated
   from...", "previously used on...", "moved onto USM from...") - state only the current fact.
2. **Describing another board's own internal wiring** from this board's own spec (board-boundary
   violation) - e.g. asserting what Cypher-Plugboard does with its own NC pins inside USM's own
   doc. Each board's docs should describe only its own side of a shared connector.
3. **Bare numeric template names** ("Template 1/2/3") with no functional meaning - use
   descriptive names instead (now: "Cypher Left Pair Template", "Hub Connector Template",
   "HID-Facing Connector Template").
4. **Connector pin maps duplicated** in `Design_Spec.md` when they should live only in
   `Board_Layout.md` (matching the existing repo convention already used by e.g. Cypher's own
   files) - `Design_Spec.md` should have prose + a cross-reference pointer only.
5. **FR/DR entries citing "Section N" of prose** instead of pointing directly to the
   `Board_Layout.md` section that actually has the detail - fixed on USM, worth checking on the
   remaining boards too.
6. **Directional/logic errors in passthrough descriptions** - always double-check which physical
   board position (facing Cypher vs facing Plugboard) is the one that actually needs to relay a
   given signal, don't assume it's symmetric or guess.
7. **Falsely resolved open items** stated as settled (e.g. an ESD requirement asserted as "not
   needed" when the standard doesn't actually cover the case) - if a rule doesn't clearly apply,
   say so honestly rather than picking the answer that requires less work.

## Not Yet Done (blocking `usm-redesign-implementation` completion)

- **Cypher-Output** (`Design_Spec.md`, `Board_Layout.md`, 3 variant files) - needs the same
  treatment as Cypher-Input: RefDes renumbering, connector-ownership pointers instead of
  duplicated pin tables, USM 4-colour-style signal repointing, `ENC_ACTIVE` propagation-delay
  note, and the same "recurring review issues" checklist applied proactively before presenting to
  the user.
- **Cypher-Plugboard** (`Design_Spec.md`, `Board_Layout.md`, 3 variant files) - reduce to
  mechanical/connector-only (no active BOM, no termination resistors - those moved to USM), retarget
  its own hub-facing connector to mate USM's bottom connector instead of a HID board directly.
- **Cypher** (`Design_Spec.md`, `Board_Layout.md`) - `J5` gains `ENC_DATA`/`ENC_ACTIVE` (Cypher
  Left Pair Template), its other connector repurposed to the Hub Connector Template (targeting
  USM instead of the closest HID board directly), retire the old `J19` USM-harness section, fix
  the CPLD I/O budget table and JTAG chain description, add the new "Cypher-peripherals" I2C bus
  entry to `Controller/Design_Spec.md §4.1`'s system-wide table (already partially done per
  DEC-103/104 - verify it's still consistent after all the naming changes this session).

## Next Session — Start Here

1. Confirm git state (`git status`, `git log -3`) - should be clean, on `main`, with this
   checkpoint's commit as the tip (or the user's own follow-up commits after review).
2. Redo **Cypher-Output** next (mirrors Cypher-Input, from the Output-role perspective), using the
   same careful one-file-at-a-time approach with the "recurring review issues" checklist run
   proactively before presenting each file - do not dispatch a single large background-agent pass.
3. Then Cypher-Plugboard, then Cypher's own connector/role sections.
4. Once all 5 boards are done and internally consistent, re-run the repo-wide stale-term greps
   (`J19`, `CFG_APPLY_N`, `TTD_HID_IN`, `TTD_HID_PASS`, `TTD_HID_OUT`, bare "Template 1/2/3") and
   markdownlint everything touched, then mark `usm-redesign-implementation` `done`.
5. After that, the user's stated next step is planning small test boards for the LED
   implementation PoC (`cypher-input-led-independent-rgb-pwm-review`).
