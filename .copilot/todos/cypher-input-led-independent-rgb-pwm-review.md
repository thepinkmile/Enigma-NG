# Review Cypher-Input/Cypher-Output LED colour controls for independent per-channel PWM

**ID:** cypher-input-led-independent-rgb-pwm-review
**Status:** pending
**Category:** Electronics / Architecture Review
**Source:** User request, 2026-08-16
**Blocked by:** None — dependency on `merge-final-review` removed 2026-09-11 (user wants to pick
this up sooner, directly after `jdb-ft232h-3v3-vregin`)

---

## Description

The current Cypher-Input LED colour architecture (DEC-087) drives each of `RED_DRIVE_N`/
`GREEN_DRIVE_N`/`BLUE_DRIVE_N` as a simple on/off gate per colour channel (software-selected via
U4 GPIO), with a single shared brightness PWM (RV1/555 astable, U1) gating one common
cathode-return switch (U8) downstream of colour selection for the whole board. This only supports
a small fixed palette of colour combinations at one shared brightness level - not full/continuous
colour mixing.

Review whether the LED bank should instead support **independent PWM control on each of the R, G,
and B lines**, so any colour (not just a fixed on/off palette) can be composited per key/board, and
consider whether this should be driven from the CM5 (e.g. via I2C brightness/colour registers or a
PWM-capable interface) rather than purely local hardware.

## Scope for this pass

- Evaluate replacing the current on/off `RED_DRIVE_N`/`GREEN_DRIVE_N`/`BLUE_DRIVE_N` gate drive
  with independent PWM-capable drive per channel (full colour mixing, not just palette selection).
- Evaluate whether/how the CM5 should drive this (new I2C interface, dedicated PWM lines, or
  continued local generation with CM5-configurable set-points).
- Identify what changes this implies for U4 (PCA9534A GPIO-only, no native PWM), U5-U7 (colour
  MOSFETs), and the brightness dial/555 astable circuit (U1, RV1).

## Explicitly out of scope for this pass (deferred, larger change)

- Per-user note (2026-08-16): making the brightness PWM astable oscillator **fully independent on
  each HID board** (i.e. Cypher-Input and the future Cypher-Output each generating and controlling
  their own PWM/brightness rather than one board's 555 broadcasting a shared
  `BRIGHTNESS_PWM_EN` to the other via `J4`/`J6`) is a materially bigger architecture change and is
  explicitly **not** in scope for this pass. Flag it as a follow-on consideration only - do not
  implement without a separate, explicit go-ahead.

## Notes

- This affects `Cypher-Input/Design_Spec.md` §5/§6, all 3 variant BOM files, and (once created)
  the Cypher-Output board's equivalent circuit - both boards currently share one broadcast
  brightness/colour signal set per DEC-087.
- **Rescheduled (user, 2026-09-11):** no longer gated on `merge-final-review`. User wants to pick
  this up directly after `jdb-ft232h-3v3-vregin`, since the outcome will guide the design of a
  physical Mock Keyboard test rig (to validate the Cypher-Input board's components and allow real
  power-draw probing) before committing to the final Cypher-Input design.
- **User is not confident in the currently-selected RGB addressable LED part** (see
  `merge-missing-components.md` — SK6812MINI-E was the leading candidate under evaluation, not
  yet approved) — revisit LED part selection as part of this review, not just the drive-topology
  question.

## Superseding context from the USM redesign discussion (2026-09-16)

This todo is now **the** decision point for the HID boards' actual LED drive implementation,
following the wider User Settings Module (USM) redesign discussion (see
`.copilot/discussions/usm-redesign/usm-connector-topology-review.drawio` for the accompanying
connector topology diagram, and the session history around 2026-09-15/16 for the full discussion).
Key outcomes to carry forward into this review:

- **USM's role is now fixed, independent of which LED option this review picks:** USM stores 3
  independent CM5-configured RGB colour values (infrequent writes, effectively at boot) and a
  hardware brightness dial (`RV1`), and relays them plus `3V3_ENIG`/JTAG/I²C to whichever
  Cypher-Input/Cypher-Output pair is installed. USM never sees `ENC_DATA` and does **no** real-time
  per-key logic itself — applying the 3 colours to actual LEDs is entirely the HID board's own
  responsibility, using whichever local implementation this review selects.
- **Required per-key/per-lens behaviour (drives the PoC test plan):**
  - Cypher-Input: static/idle state = **all** keys show Colour1. The currently-pressed key shows
    Colour2. On the 64-Character variant, holding Shift is a **global** state change (not
    per-key): while Shift is held, **all** keys switch their baseline illumination from Colour1 to
    Colour3 (indicating the letter keys are now producing uppercase output - Shift changes the
    `[a-z]` keys' cipher meaning to `[A-Z]`), and the currently-pressed key still shows Colour2 on
    top of that Colour3 baseline exactly as it would on top of the normal Colour1 baseline.
  - Cypher-Output: the ENC module's `LBD_DEC` CPLD decodes whether the output character is
    uppercase (treated as "shifted") from `ENC_DATA[5:0]` and lights that position's LED Colour3
    if so, Colour2 otherwise; **no** lens is illuminated at all when no key is currently active.
- **Two live implementation options remain open, both requiring PoC/bench validation before a
  choice is made:**
  1. **Existing analog RGB LED drive** (the ICs/topology already specified: `U4` PCA9534A colour
     GPIO, `U5-U7`/`U1-U3` P-MOSFET colour-bank switches, `RV1`/555 astable + `U8` brightness
     switch). **Known open technical question for the PoC to resolve:** this topology drives one
     shared colour per board via common R/G/B rails — it does not natively support the
     simultaneous multi-colour-per-key behaviour above (e.g. most keys Colour1 while one key is
     simultaneously Colour2) without additional per-key bank-selection hardware that does not
     currently exist in the design. Confirm during the PoC whether this is achievable within
     acceptable complexity/cost, or whether it rules this option out for the stated behaviour.
  2. **Addressable RGB LEDs** (e.g. the SK6812MINI-E candidate already flagged in
     `merge-missing-components.md`) — naturally supports independent per-key/per-lens colour via
     its own addressing protocol, generated locally by each ENC module's CPLD (reading the 3
     stored colour values off the shared I²C bus, then combining them with real-time key
     state/decoded case). **Two known dependencies to fold into the PoC/decision:**
     - The current CPLD (MAX II EPM570) very likely does not have enough LEs for this additional
       per-key addressable-protocol + colour-selection logic — `cpld-production-replacement`
       (MAX10 candidate) is the tracked follow-up for this; flag as a note in the affected board
       specs that this is a known constraint, not yet resolved.
     - Addressable LEDs of this class are conventionally 5V-logic parts (~0.7×VDD high threshold),
       while the CPLD's output is 3.3V — a small single-bit level-shifter/buffer IC per board
       between the CPLD's LED-data output and the local LED chain is expected to be needed if this
       option is chosen; the level-shifting/regulation stays local to each HID board, USM only
       ever carries 3.3V logic.
- **Do not remove or redesign the existing analog LED drive components on Cypher-Input/
  Cypher-Output yet** — they remain the current default circuit until this review's PoC concludes
  and a final option is chosen. Only the *signal source* changes as part of the wider USM redesign
  (colour/brightness values now arrive from USM via I²C instead of being locally generated by
  Cypher-Input's own `U4`/`RV1`/`U1`), which is being implemented ahead of this review being
  resolved.
- `Power_Budgets.md`'s existing 5V_MAIN LED-bank figures remain the current-best-estimate ceiling
  until this review's PoC and final option choice - do not recalculate until then.

## Follow-up items from USM redesign implementation (2026-09-17)

- **I2C bus allocation review needed once the LED implementation is chosen.** The USM redesign
  implementation created a dedicated `I2C2` bus ("Cypher-peripherals") purely as a placeholder for
  the USM colour-value store. User's preference: only keep a genuinely separate dedicated bus if
  `I2C1` actually becomes over-populated as a result of whatever LED implementation this review
  selects - if `I2C1` has enough headroom, prefer folding the colour-value store onto it instead
  of keeping a second bus. User also wants to reserve the numbering `I2C{1-4}` for a **different,
  not-yet-had discussion** (a future idea, unrelated to this review) - so if a dedicated bus does
  turn out to be needed, user is currently leaning towards naming it `I2C6` (the "Cypher-local"
  bus) rather than `I2C2`, specifically to keep `I2C{1-4}` free for that other discussion. Nothing
  needs to change right now - this is deferred until the LED PoC/decision is made, then revisit the
  bus numbering/allocation as part of wrapping up this review.
- **Colour-store I2C address (`0x39` on the placeholder `I2C2` bus, per `User_Settings_Module/
  Design_Spec.md` DR-USM-07) is provisional only.** It's probably fine as a starting point, but
  the final address (and which bus it sits on - see point above) will likely depend on the outcome
  of the LED selection PoC and whatever the chosen implementation actually needs. Re-confirm/update
  this address as part of closing out this review, don't assume `0x39`/`I2C2` is final.
