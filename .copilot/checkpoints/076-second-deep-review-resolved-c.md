# Checkpoint 076 — Second deep-review cycle resolved and committed

**Date:** 2026-04-29
**Session:** fbc2318d-bfe5-48d5-a96b-8a3f6463c575

## What was done this session

Resolved all outstanding findings from the second electronics deep-review cycle that ran in the
previous sessions. All changes are now committed as a single coherent set.

### CTL-L2 — bypass/decoupling capacitor voltage rating

- Confirmed 50V rating retained on all non-PM boards. 25V would be sufficient but no approved 25V
  equivalents exist; cost delta is negligible; functional 50V specs (BSS138, C0G caps) are not
  derating specs.
- Bulk reservoir caps (10µF) already down-specced to 25V in a prior pass — unaffected.
- **DEC-046** written to `design/Design_Log.md` formally documenting this rationale.

### CTL-H1 — R1/R2 stale placeholder resistors (Controller BOM)

- R1 (10kΩ "pull-up for reset"): stale placeholder from an early design where nRSTIN was tied
  directly to the power switch. Superseded by PWR_BUT → PM path; CM5 PMIC has an internal 10kΩ
  pull-up on the power-key input. No other Controller pin requires this resistor.
- R2 (100Ω "termination for differential"): no Controller differential signal requires an external
  termination. All high-speed interfaces (USB, HDMI, GbE, DSI1) use BCM2712 internal termination.
  JTAG explicitly has no series resistors on the Controller per §3. Added by a prior review agent
  and committed before the user could review.
- Both removed. R3–R6 renumbered sequentially to R1–R4.
- Consolidated BOM updated: 100Ω differential termination row removed; 10kΩ 0603 CTL count 5→4,
  system total 22→21.

### Rotor ESD section rewrite

- Phantom signals `ENC_ACTIVE_N` and `ENC_CLK` removed from ESD coverage listing.
- U5–U12 TPD4E05U06 array count corrected; ESD table now covers `ENC_IN[5:0]` and `ENC_OUT[5:0]`.

### Power Module Design_Spec

- PM-H5 (battery connector suitability review) removed from spec body — this is not a design item;
  suppression note for review agents lives in `.copilot/handoff.md`.
- ODU added as a potential supplier alongside Glenair for the military battery socket replacement.

### Encoder Design_Spec

- "Encode vs decode role identification is no longer a silkscreen requirement" → "is not a silkscreen
  requirement" — removed historical language from the active design spec.

### Stator Design_Spec

- Retired servo requirements (originally FR-STA-09 to FR-STA-12) removed entirely from active spec.
  Historical context preserved in DEC-038 in the Design Log.
- FR-STA-13 typo fixed ("sourceand" → "source and").
- Requirements renumbered sequentially (no gaps).

### Consolidated BOM

- TPD4E05U06 rotor system total corrected.
- 100Ω 0603 CTL differential termination row removed (was CTL=1, System Total=1).
- 10kΩ 0603 CTL count corrected 5→4 (System Total 22→21).
- Various earlier BOM fixes from review cycle included in this commit.

## Files changed

- `design/Design_Log.md` — DEC-046 added
- `design/Electronics/Controller/Design_Spec.md` — R1/R2 removed; R3–R6 → R1–R4
- `design/Electronics/Consolidated_BOM.md` — resistor count corrections
- `design/Electronics/Rotor/Design_Spec.md` — ESD section rewrite
- `design/Electronics/Power_Module/Design_Spec.md` — PM-H5 removed; ODU added
- `design/Electronics/Encoder/Design_Spec.md` — "no longer" wording removed
- `design/Electronics/Stator/Design_Spec.md` — retired reqs removed; typo fixed; renumbered
- `design/Electronics/Extension/Design_Spec.md` — minor wording fix from prior review
- `design/Standards/Global_Routing_Spec.md` — minor wording fix from prior review
- `.copilot/handoff.md` — PM-H5 review suppression note added; session result updated

## Design decisions recorded

- **DEC-046** — Bypass/Decoupling Capacitor Voltage Rating: 50V Retained on All Non-PM Boards

## Open items (not actioned this session)

- Battery connector sourcing (Category C) — awaiting supplier email responses
- Follow-up work listed in `handoff.md` §"Remaining follow-up work" unchanged

## Next checkpoint will be 077
