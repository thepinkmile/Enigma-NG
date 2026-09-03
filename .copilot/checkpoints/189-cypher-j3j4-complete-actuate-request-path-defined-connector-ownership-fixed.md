# Checkpoint 189 — Cypher J3/J4 Pinouts Complete; ACTUATE_REQUEST Signal Path Fully Defined; Connector Ownership Corrected

**Date:** 2026-09-03

## Summary

This session closed out `merge-cypher-board-j3j6-pinouts` (J3/J4, the last two unresolved Cypher
connectors), then followed the resulting `ACTUATE_REQUEST_IN_N`/`OUT_N` signal all the way through
every board in the Rotor Mini-Stack chain, fixing genuine design gaps at each stop (missing pins,
missing ESD protection, a stale termination model on the Stack-Blanking Board). It also corrected
a connector-ownership documentation error (DEC-018 model was being applied backwards for two
connector families) and did a thorough sweep removing historical/rationale wording that had crept
into several "current design only" documents. DEC-090 through DEC-097 were created this session.

## 1. Cypher `J3`/`J4` fully 50-pin allocated (DEC-090, DEC-092, DEC-093)

- **`J3` (Stack-Input/STA-side):** added `3V3_ENIG` ×4, `5V_MAIN` ×4, `ACTUATE_REQUEST_IN_N`,
  `ACTUATE_REQUEST_OUT_N`. Confirmed `ENC_ACTIVE_N` is HID-local-only and never belongs on this
  connector (resolved a real contradiction with Stack-Input's prior assumption).
- **`J4` (Stack-Output/REF-side):** mirrors J3's template (JTAG broadcast signals → GND,
  `5V_MAIN` groups → extra `3V3_ENIG`), `TTD_RETURN` at J3's `TTD` pin position,
  `ACTUATE_REQUEST_REF_IN_N`/`ACTUATE_REQUEST_REF_OUT_N` added (renamed from generic names to
  match the `ENC_IN_REF`/`ENC_OUT_REF` naming precedent).
- `merge-cypher-board-j3j6-pinouts` is **done** — all four Cypher connectors (J3-J6) now fully
  allocated.

## 2. `ACTUATE_REQUEST` end-to-end signal path defined (DEC-093)

Full quad-pass round trip (originates and terminates at Cypher's own CPLD U1), mirroring the
existing `ENC_DATA`/cipher signal's own four-pass structure: forward via the STA chain
(Cypher→Stack-Input→Rotors→Stack-Output→Stack-Interposer, repeating per mini-stack) → reflect at
Stack-Blanking → back via the REF chain (Stack-Output boards only) → CPLD reflection at Cypher →
forward via the REF chain again → reflect at Stack-Blanking again → back via the STA chain in
reverse rotor order → terminates at Cypher.

Extended into every board along the chain:
- **Rotor:** `ACTUATE_REQUEST_IN_N`/`OUT_N` added to the ENC data connectors (`J3`/`J6`, pins
  13/14) rather than the JTAG connector (insufficient spare capacity there). New ESD ICs **U12**
  (Board A) / **U13** (Board B) — extra counts of the existing TPD4E05U06QDQARQ1 part.
- **Stack-Interposer:** new SIG-BLOCK-G/H on previously-spare guard pins 15/16 — pure passive
  passthrough, no new component.
- **Stack-Output:** own `J1`/`J2` (IC-REF-CHAIN) fully pinned out; `J5` gains a new ESD IC **U9**.
  This board has no active ICs, so its `ACTUATE_REQUEST_REF_IN_N`/`REF_OUT_N` and `J5`↔`J6`
  SIG-BLOCK-G/H wiring are both simple passive passthroughs.
- **Stack-Input:** front-`OUT`/rear-`IN` "NC" assumptions (from the initial J3 pass) corrected —
  all four pins carry real two-pass traffic. New ESD ICs **U11** (`J1`) / **U12** (`J5`).
- **Cypher:** `J3`'s `ACTUATE_REQUEST_OUT_N` (pin 35) changed from NC to a real CPLD U1 input +
  new **R51** idle-bias pull-up (DEC-097) — U1 now verifies the round trip actually completed, as
  a system self-test, rather than leaving the pin unused.

## 3. Stack-Blanking Board corrected (DEC-096)

Was still using the pre-DEC-090 model (`ACTUATE_REQUEST_N` as a single dead-ending signal, `R5`
pull-up terminator) and a stale `ENC_ACTIVE_N` termination (`R1`) that was never actually routed
there. Both resistors removed; remaining R2-R4 renumbered to R1-R3 (TCK/TMS/CPLD_RESET_N only —
the genuine dead-end signals). Two new passive bridging paths added for the `ACTUATE_REQUEST`
round trip's two turnarounds, matching the board's existing ENC/TTD bridging pattern.

## 4. Connector ownership model corrected (DEC-094, amends DEC-018)

User identified that `J3`/`J4` (and the equivalent Stack-Input/Stack-Output `J1`/`J2` templates)
were being owned by the wrong board — Cypher held the canonical tables when the
repeatedly-instantiated Stack-Input/Stack-Output boards should own them instead (same reasoning
DEC-018 already applied to the Rotor Interface). Moved:

- **IC-STA-CHAIN** → **Stack-Input** (was Cypher)
- **IC-REF-CHAIN** → **Stack-Output** (was Cypher)
- IC-ROT-JTAG/ENC/PWR (Rotor) and IC-HID (Cypher) confirmed already correct
- Fixed a stale IC-INTERPOSER cross-reference on Stack-Output that still said "TBD — board not
  yet created" for a board that already exists

This surfaced real drift: Stack-Output's own docs still referenced the closed
`merge-cypher-board-j3j6-pinouts` todo and pre-dated Cypher's actual resolved state.

## 5. Historical/rationale wording sweep (multiple rounds)

Per `document-rules.md` ("current design only — no historical detail"), removed numerous
instances across Cypher and all four Stack-* boards: stale "does not appear" explanations, "not
by X, because..." ownership rationale, "previously spare, reused, no new component required"
narrative, "the actuator type has changed from servo to solenoid", ~13 BOM rows' worth of
"(from EXT ...)"/"(from AM ...)" provenance notes referencing pre-merge board names, and more.
Also caught and fixed a **functional** (not just wording) error along the way: Stack-Input's own
`J1` still claimed "Connector definition owner: Cypher Board" after DEC-094 had already
reassigned that ownership to Stack-Input itself.

Confirmed with the user that "Stator"/"Reflector" as role names on the Cypher Board (mapping to
the historical Enigma machine's own component roles, not the old separate PCB boards) are
legitimate current-design terminology and should **not** be removed.

New todo **`design-docs-current-only-sweep`** created to extend this review to the rest of the
design document tree later (this pass only covered Cypher + Stack-*).

## Decisions created this session

DEC-090 through DEC-097 (8 new entries) — see `design/Design_Log/index.md` for the full list.
Next DEC number: **098**.

## Status

- `merge-cypher-board-j3j6-pinouts`: **done**.
- `merge-actuate-request-routing`: **done** (all boards — Cypher, Stack-Input, Rotor,
  Stack-Interposer, Stack-Output, Stack-Blanking — now consistently implement the full
  `ACTUATE_REQUEST` round trip with complete ESD coverage).
- `design-docs-current-only-sweep`: **pending** (new, deferred).
- User is doing a final manual review of this whole change set before moving on.

## Next steps (user-confirmed order, see `plan.md`)

1. User's manual review of this session's change set (in progress).
2. **Controller board updates** — `merge-ctl-dock-usb-allocation` → `merge-update-ctl-board`:
   define USB D+/D- on Cypher's `J1` dock; remove JM (`J12`) and AM (`J11`) from Controller (JM is
   now native to Cypher — user believes no JTAG traces should remain on Controller at all, needs
   verifying against the actual schematic); add a Cypher-facing dock connector (old Stator dock
   `J4`/`J5` are being reallocated to serve this role, since Cypher is the Stator's replacement);
   retarget Link-Beta from Stator to Cypher.
3. `jdb-ft232h-3v3-vregin` — quick fix, native to Cypher's JTAG bridge section.
4. `cpld-production-replacement` — MAX10 FPGA discussion; likely mechanical implications for
   Rotor boards.
5. `footprint-requests-pending` — review/resolve outstanding footprints.
6. `cypher-input-led-independent-rgb-pwm-review` — pending user's own test board results.
7. `system-assembly-harnesses` and `system-config-variants-diagrams` — deferred until the above
   list is complete.
