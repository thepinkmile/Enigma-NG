# Checkpoint 192 — USM Redesign Connector Templates Finalised; Implementation Pass Partially Damaged, Pending User Revert Decision

**Date:** 2026-09-18
**Status at checkpoint:** Mid-implementation, deliberately paused for a clean weekend handoff.

---

## Summary

This checkpoint captures a messy-but-real intermediate state. The USM redesign's **design
decisions are fully settled** (all three shared connector pin-map templates finalised
pin-by-pin with the user), but the **file-level implementation pass has a serious quality
problem** on 4 of 5 affected boards that the user needs to resolve via their own git workflow
before work continues.

## What Is Fully Settled (decisions, not yet all correctly on disk)

Three shared connector templates, agreed pin-by-pin with the user across many iterations:

1. **Template 1 — "Cypher left pair"** (direct board-to-board, unchanged mechanical position):
   used by Cypher-Input/Output's own left connectors, Cypher's own connector to the closest HID
   board, and Cypher-Plugboard's connector to the HID board above it. Carries `5V_MAIN`/GND,
   `BOARD_ROLE_ID_IN`/`OUT[3:0]`, `ENC_DATA_IN`/`OUT[5:0]`, `ENC_ACTIVE_INPUT_N`/
   `ENC_ACTIVE_OUTPUT_N`. Top row = Input role (locally driven + generated), bottom row = Output
   role; each board locally drives/consumes only its own row and straight-passes the other row
   untouched. **Important constraint confirmed by user:** `ENC_ACTIVE_INPUT_N`/
   `ENC_ACTIVE_OUTPUT_N` must only ever originate from/terminate at the Cypher Board — no
   intermediate HID board may tap/buffer them, due to propagation-delay sensitivity against the
   Rotor/Stack encoder chain. Full final pin table is in the session transcript (2026-09-17) and
   is correctly implemented today in `Cypher-Input/Board_Layout.md §1`/`Design_Spec.md §7`.
2. **Template 2 — "hub" connector** (Cypher ⟷ USM.top ⟷ [internal USM routing] ⟷ USM.bottom ⟷
   Plugboard): carries `3V3_ENIG`, `CPLD_RESET_N`, `I2C_SDA`/`SCL`, `TMS`/`TCK`, `TDI`/`TDO`.
   Plugboard's own copy of this connector has every non-GND pin NC (Plugboard has zero active
   JTAG role — the Cypher→Input→Output loop closes entirely inside USM, never physically
   reaching Plugboard's own connector).
3. **Template 3 — "USM left connector"** (HID board's new right-edge connector ⟷ USM's
   left-upper/left-lower): carries `3V3_ENIG`, `I2C_SDA`/`SCL`, `CPLD_RESET_N`, `TMS`/`TCK`,
   `RED_DRIVE_N`/`GREEN_DRIVE_N`/`BLUE_DRIVE_N`/`ILLUMINATION_DRIVE_N` (broadcast, identical both
   rows), and role-specific `TDI_INPUT`/`TDO_INPUT` (top row) / `TDI_OUTPUT`/`TDO_OUTPUT` (bottom
   row). Final pin table is in the session transcript and correctly implemented today in
   `Cypher-Input/Board_Layout.md §2`.

**USM's role** (settled, not yet correctly on disk): stores 3 CM5-configured RGB colour values
(exact IC TBD) + retains the brightness dial (`RV1`) + hosts a buzzer placeholder (part TBD,
`usm-buzzer-audio-options`) + hosts the JTAG broadcast-signal termination resistors (moved off
Cypher-Plugboard) + 4 connectors (top/bottom = Template 2, left-upper/left-lower = Template 3).
**Cypher-Plugboard's role** (settled): purely mechanical/connector-only board — no active BOM,
no termination resistors, `ENC_ACTIVE`/JTAG chain does not electrically reach it.

**RefDes convention agreed for every HID board** (Cypher-Input/Output): `J1`/`J2` = Cypher left
pair (top/bottom), `J3` = USM connector, `J4`-`J6` = ENC module mount. Connector **pin maps**
themselves are NOT to be duplicated in each HID board's own file — they are owned by
`Cypher/Board_Layout.md §4` (Template 1) and `User_Settings_Module/Board_Layout.md` (Template 3)
respectively; each HID board's own doc states only its own row usage + which local component
each pin feeds.

## What Is Correctly Implemented Today

- **`Cypher-Input/Design_Spec.md` and `Board_Layout.md`** — fully renumbered and corrected:
  ownership pointers instead of duplicated pin tables, `ENC_ACTIVE_*` propagation-delay note
  added, LED colour architecture correctly repointed to USM as the source (local `U5`-`U8` drive
  stage retained, `U4` role reduced to Board ID + Space/Enter only).
- **`Cypher-Input/Cypher_Input_64_Char_Design.md`** — restored from a badly-gutted state (the
  background agent had stripped ~75% of this file's content and altered its title/header format)
  back to full original detail, with only the genuinely-affected content updated: LED §5 rewritten
  to remove the obsolete `U9`/`D9`/`R9` local Colour-A/B mux circuit (colour now sourced from USM
  entirely) while correctly preserving/clarifying the **real behavioural requirement**: Shift is a
  **global** state (not per-key) — holding Shift switches **all** keys' baseline illumination from
  Colour1 to Colour3 (since Shift changes `[a-z]`→`[A-Z]`), with the currently-pressed key still
  showing Colour2 on top of whichever baseline is active. This corrected behaviour was also
  written into `cypher-input-led-independent-rgb-pwm-review.md`.
- **New todos created this session:**
  - `usm-3-part-hid-module-mechanical-review` — mechanical mounting review for the new
    USM+Input+Output "3-part HID module", deferred until electronics settle.
  - `encoder-module-pin-agnostic-redesign-review` — the Encoder Module should become a true
    role-agnostic board (CPLD/FPGA + passives only, direct pin→connector mapping owned by the
    module, each carrier board defines its own usage table); triggered specifically by
    `ENC_ACTIVE_N` currently being a single role-dependent pin when the new design needs two
    logically distinct signals (deterministic-propagation constraint above).
  - `usm-redesign-implementation` — master tracking todo for this whole changeset (status
    currently `done` in the todo DB from the background agent's pass, but see **Known Issue**
    below — this should probably be flipped back to `in_progress` once the user has resolved
    which files are being reverted).
- **`cypher-input-led-independent-rgb-pwm-review.md`** updated with: the corrected Shift/colour
  behaviour, an I2C-bus-allocation preference note (prefer folding the USM colour store onto
  `I2C1` unless it becomes over-populated; if a dedicated bus is still needed, user is leaning
  towards naming it `I2C6` rather than `I2C2`, to keep `I2C{1-4}` free for an unrelated future
  discussion), and a note that the reserved colour-store address (`0x39`) is provisional pending
  the LED PoC outcome.
- **`usm-cfg-refmap-removal-review.md`** archived to `.recycle-bin/todos/` (consistent with
  existing repo convention for retired todos) as superseded by `usm-redesign-implementation`.

## ⚠️ Known Issue — Needs User's Git Decision Before Next Session Continues

A background agent was dispatched mid-session to implement the (fully-agreed) connector/role
changes across `User_Settings_Module`, `Cypher-Input`, `Cypher-Output`, `Cypher-Plugboard`, and
`Cypher` (Design_Spec.md + Board_Layout.md each), plus `Controller/Design_Spec.md`'s I2C table,
plus new DEC-103 through DEC-106.

**The agent's technical decisions were largely fine, but its editing was destructive on 6 of 9
files it touched** — it didn't make targeted edits, it substantially rewrote/shortened several
files, discarding large amounts of legitimate pre-existing content (detailed FR/DR rows, full
component diagrams, full BOM detail, variant-specific circuits, prose) that had nothing to do
with the requested change. Confirmed via `git diff --stat` against the pre-agent `HEAD`:

| File | Lines changed | Status |
| :--- | ---: | :--- |
| `Cypher-Input/Design_Spec.md` | 671 (532 deletions) | **Fixed by hand this session** ✅ |
| `Cypher-Input/Board_Layout.md` | (renumbered cleanly) | **Fixed by hand this session** ✅ |
| `Cypher-Input/Cypher_Input_64_Char_Design.md` | 198→52 lines | **Fixed by hand this session** ✅ |
| `Cypher-Output/Design_Spec.md` | 609 | ⚠️ Not yet reviewed/fixed |
| `Cypher-Output/Board_Layout.md` | 374 | ⚠️ Not yet reviewed/fixed |
| `Cypher-Plugboard/Design_Spec.md` | 380 | ⚠️ Not yet reviewed/fixed |
| `Cypher-Plugboard/Board_Layout.md` | 169 | ⚠️ Not yet reviewed/fixed |
| `Cypher/Design_Spec.md` | 161 | ⚠️ Not yet reviewed/fixed (smallest delta - may be closer to OK) |
| `Cypher/Board_Layout.md` | 415 | ⚠️ Not yet reviewed/fixed |
| `User_Settings_Module/Design_Spec.md` | 684 | ⚠️ Not yet reviewed/fixed |
| `User_Settings_Module/Board_Layout.md` | 312 | ⚠️ Not yet reviewed/fixed |
| `Cypher_Output_64_Char_Design.md` + 3x `Cypher_Plugboard_*_Design.md` | 4-5 lines each | ✅ Small, targeted, appear fine |

**The user has decided to handle the git-level revert/keep decision themselves** (per their own
repo directives/workflow) rather than have this session run the revert. **DEC-103 through
DEC-106's actual decision content is believed sound** (topology change, USM role change, CFG_ROUTE
full CM5 control, Plugboard mechanical-only) — it's specifically the board
`Design_Spec.md`/`Board_Layout.md` *implementation* files that need re-doing carefully, not the
underlying decisions. If the user reverts the affected board files, the DEC log entries can likely
stay as-is (they document decisions, not implementation detail) — but double check DEC-103..106's
own text doesn't cite pin numbers/specifics that no longer match after a revert.

## Next Session — Start Here

1. Confirm what the user did with the flagged files (kept/reverted/hand-fixed) — check
   `git status`/`git diff --stat` against this checkpoint's table before assuming anything.
2. For every file still needing rework, apply the **same careful, one-section-at-a-time,
   diff-checked-before-moving-on approach** used to fix `Cypher-Input` this session — do **not**
   dispatch another single large background-agent pass for this; it produced this exact problem
   once already despite explicit "surgical, don't touch unrelated content" instructions in the
   prompt.
3. Once all 5 boards are correctly updated: re-verify `usm-redesign-implementation` and
   `usm-cfg-refmap-removal-review` todo statuses match reality, re-run the stale-term greps
   (`J19`, `CFG_APPLY_N`, `TTD_HID_IN`, `TTD_HID_PASS`, `TTD_HID_OUT`) across the 5 boards, and
   run markdownlint on everything touched.
4. Resume the LED implementation PoC discussion (`cypher-input-led-independent-rgb-pwm-review`)
   only after the connector/role implementation is confirmed correct and complete — user's stated
   plan is to move to planning small test boards for the LED PoC once file cleanup is done.
