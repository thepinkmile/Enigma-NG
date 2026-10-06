# Checkpoint 194 — Cypher-Output and Cypher-Plugboard Rebuilt & Reviewed; Connector Mating Convention Corrected

**Date:** 2026-10-06
**Status at checkpoint:** Cypher-Output and Cypher-Plugboard both fully rebuilt and reviewed by
the user. Session paused for user availability (career fair). Resume with **Cypher** itself next.

---

## Summary

Continuing the USM redesign rebuild started in checkpoint 193 (USM + Cypher-Input), this session
completed the same treatment for **Cypher-Output** and **Cypher-Plugboard**, plus fixed a
repo-wide mechanical convention error and added a new standards placeholder, both caught by the
user during review.

## What Is Done and User-Reviewed

1. **Cypher-Output** (`Design_Spec.md`, `Board_Layout.md`, all 3 variant files) — fully rebuilt
   and reviewed:
   - RefDes renumbered: `J1`/`J2` = Cypher Left Pair Template (top male/bottom female), `J3` = USM
     connector (bottom/Output row of the HID-Facing Connector Template), `J4`-`J6` = ENC module
     mount.
   - Connector pin maps NOT duplicated - owned by `Cypher/Board_Layout.md §4` and
     `User_Settings_Module/Board_Layout.md` respectively.
   - LED colour architecture repointed to USM's 4-colour-style signal groups (local `U1`-`U4`
     colour-bank/illumination drive stage retained, only the signal *source* changed).
   - **`ENC_ACTIVE_INPUT_N`/`ENC_ACTIVE_OUTPUT_N` resolved correctly** (user-corrected): these are
     two **distinct** signals, not one relayed under two names. `ENC_ACTIVE_INPUT_N` (Cypher-Input
     generated) terminates at Cypher only; Cypher itself, after accounting for propagation delay,
     generates a **separate** `ENC_ACTIVE_OUTPUT_N` for Cypher-Output to consume. Cypher-Output is
     the legitimate destination of `ENC_ACTIVE_OUTPUT_N`, not an intermediate tap.
   - **User-caught fixes this pass:**
     - All 3 variant files still had stale "LED colour/brightness received entirely as a
       broadcast from Cypher-Input" wording, stale `J1` ENC-mount zig-zag references, and stale
       `Design_Spec.md §10` BOM cross-refs (now `§11`) - missed in the first pass, caught when the
       user asked "were there not any updates required for the other variant design files?".
     - Stale "Cypher-Input's `RV1`" cross-references removed entirely (3 locations) - Cypher-Input
       no longer has an `RV1`; brightness is now one of the 4 received colour styles.
     - SW1 (64-Character variant's custom-support switch) **kept** on both boards after
       discussion - user confirmed no DEC change needed, it still exists purely to let the user
       toggle `BOARD_ROLE_ID_OUT[3]` at runtime (bits 0-2 remain fixed fit/DNF-link straps).
     - PCBA-exclusion rationale for SW1 corrected: it's excluded because it's a **THT** part
       (`JLCPCB_Manufacturing.md §3.2`), not because of the single-sided-SMT constraint (§3.1,
       which is the LED bank's actual rationale) - these were incorrectly conflated.
2. **Connector mating convention corrected repo-wide** (user caught this was backwards): **male**
   connectors mount **protruding** past their board edge to bridge the enclosure gap; **female**
   connectors mount **flush** with their board edge, forming the receiving socket opening. Fixed
   across `Cypher/Board_Layout.md §4`, `Cypher-Input/Board_Layout.md`,
   `Cypher-Output/Board_Layout.md`, `Cypher-Plugboard/Board_Layout.md`. New todo logged:
   `mini-stack-connector-flush-protrude-review` (check the mini-stack sub-system for the same
   mismatch once the Cypher system is complete) - properly persisted to `.copilot/todos/`
   (todos.sql, deps.sql, index.md, detail file), after an initial miss where it was only added to
   the session DB.
3. **New placeholder tolerance rule added:** `Global_Routing_Spec.md §4.1a` - Internal
   Board-to-Board Connector Mating Tolerance, ~0.02mm nominal stack-up gap, explicitly flagged as
   unconfirmed pending datasheet mating-dimension review and PoC board testing. Cross-referenced
   from all four Cypher-system `Board_Layout.md` files (reference kept plain, no "(placeholder)"
   qualifier repeated at each call site per user's instruction - the caveat lives solely in GRS).
4. **Cypher-Plugboard** (`Design_Spec.md`, `Board_Layout.md`) — fully rebuilt and reviewed:
   - **`R1`-`R3` JTAG termination removed entirely** - this board now has **no active components
     at all**. Termination moved to USM per DEC-103 (already decided, just not yet implemented on
     this board).
   - `J1` retargeted to the (now LED-free) Cypher Left Pair Template; `J2` retargeted from the old
     (retired) HID JTAG template to **USM's own bottom Hub connector**, per DEC-103.
   - BOM fixed: dropped `R1`-`R3`; corrected a pre-existing qty bug (`J1,J2` was listed as qty 1,
     should be 2).
   - **User-caught GND/3V3_ENIG contradiction (two rounds):** an initial pass incorrectly grouped
     `3V3_ENIG`/GND together as both "left NC", which contradicts needing a continuous
     signal-return path. Fixed to explicitly split: `3V3_ENIG` is genuinely NC (no consumer on
     this board), GND is explicitly kept fully populated/continuous (never NC) across every
     connector, for return-path integrity - this is distinct from (and unrelated to) the
     `GND_CHASSIS` network's own continuity via the jack bushings + machined enclosure + PCB
     mounting holes, which was already correct and unaffected.

## Not Yet Done (blocking `usm-redesign-implementation` completion)

- **Cypher** itself (`Design_Spec.md`, `Board_Layout.md`) - still has the **old, stale**
  connector topology throughout (its own `J5`/`J6` pin maps still show the pre-redesign
  "Power + LED Broadcast + BOARD_ROLE_ID" / "JTAG + ENC_DATA + Board ID + I2C + PWM" templates -
  these are now out of sync with the already-rebuilt-and-approved Cypher-Input/Cypher-Output,
  which reference "Cypher Left Pair Template" as owned by Cypher's own `J5`, without LED signals).
  Per the existing plan: `J5` gains `ENC_DATA`/`ENC_ACTIVE` per the (LED-free) Cypher Left Pair
  Template; `J6` repurposed to the Hub Connector Template targeting USM instead of a HID board
  directly; retire the old `J19` USM-harness section; fix the CPLD I/O budget table and JTAG
  chain description; verify the Controller's system-wide I2C address table is still consistent.
- `mini-stack-connector-flush-protrude-review` todo - check the mini-stack sub-system's own
  `Board_Layout.md` files for the same flush/protrude mismatch, once the Cypher system is fully
  done.
- Once Cypher itself is done, re-run the repo-wide stale-term greps (`J19`, `CFG_APPLY_N`,
  `TTD_HID_IN/PASS/OUT`, bare "Template 1/2/3", old LED-broadcast signal names) and markdownlint
  everything touched, then mark `usm-redesign-implementation` `done`.

## Next Session — Start Here

1. Confirm git state (`git status`, `git log -3`) - should be clean, on `main`, with this
   checkpoint's commit as the tip (or the user's own follow-up commits after review).
2. Redo **Cypher** itself next - this is the last board blocking `usm-redesign-implementation`.
   Use the same careful one-file-at-a-time approach, with the "recurring review issues" checklist
   (checkpoint 193) run proactively before presenting each file - do not dispatch a single large
   background-agent pass.
3. Pay particular attention to: the Cypher Left Pair Template's `J5` signal list must now match
   exactly what Cypher-Input/Cypher-Output already reference (no LED signals - those moved to the
   USM-facing connectors); `J6`'s full retarget to the Hub Connector Template; the CPLD I/O budget
   and JTAG chain description once the connector roles change; the system-wide I2C address table
   in `Controller/Design_Spec.md §4.1`.
4. Then tackle `mini-stack-connector-flush-protrude-review` (independent of the USM redesign, can
   be done any time after the Cypher system is finished).
5. After `usm-redesign-implementation` is marked `done`, the user's stated next step is planning
   small test boards for the LED implementation PoC
   (`cypher-input-led-independent-rgb-pwm-review`).
