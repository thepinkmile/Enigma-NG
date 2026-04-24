# Checkpoint 047 — Repository review cleanup, two clean passes
## Date
2026-04-16
## Overview
This checkpoint records the repository-scoped active-document cleanup that followed the earlier
Settings Board / Power Module work. The objective was to bring `README.md` and `design/**/*.md`
back into internal agreement, then hold the checkpoint until the repo passed two consecutive clean
review cycles.

That gate is now satisfied: markdown lint is clean, the repository review findings were worked down
to zero, and two consecutive clean repository-scoped review passes were completed.
## Work Done
### Active-doc consistency cleanup completed
- Corrected stale top-level architecture and board-inventory summaries so active docs now include
  the Settings Board and reflect the current board set
- Normalized power-path wording across README, Power Module, User Manual, and Certification
  Evidence so active docs only claim documented PoE-over-USB-C priority and treat USB-C vs Battery
  precedence as voltage-dependent unless extra gating is added
- Corrected 3V3_ENIG scope so active docs no longer imply USB, HDMI, or Ethernet are powered from
  the LDO rail
- Fixed reflector / Stator / rotor return-path wording so the direct J7↔J4 ribbon and the Rotor 30
  J5 ↔ Reflector J2 mechanical mate are described consistently
- Brought LINK-BETA, TTD_RETURN, SYS_RESET_N, and downstream I2C descriptions into agreement across
  Controller, Stator, Reflector, and System Architecture docs
- Corrected rotor sensing/current wording so active docs consistently describe:
  - FDC2114 active current = 2.1mA per IC
  - 54.2mA typical / 55mA budget per rotor
  - two populated FDC2114s per rotor variant (`U2+U3` for N=64, `U2+U4` for N=26)
- Clarified that `fdc2112-datasheet.pdf` is the local FDC2x1x family datasheet that covers
  FDC2114
- Fixed stale mechanical / user-facing summaries that still referenced retired switch layouts,
  impossible source-priority claims, or outdated board responsibilities
### Review cycle completion
- Repeatedly ran repo-scoped markdown lint over `design/**/*.md` and `README.md`
- Repeatedly ran repository-scoped active-doc review passes until all high-signal findings were
  resolved
- Achieved **two consecutive clean passes** after the final fix set
## Commits
None. This checkpoint syncs repo-local `.copilot\` handoff state only.
## Key Technical Notes
### Current power-path truth in active docs
The active design now documents the following consistently:

1. **PoE is explicitly prioritised over USB-C** by the implemented gating on the USB-C path.
2. **USB-C vs Battery is not hard-prioritised** in the current schematic wording; precedence follows
   active source voltages unless extra gating is added.
3. **Reflector power enters via the direct Stator J7 ↔ Reflector J4 ribbon**, not via the
   Reflector J2 power pins, which are present only for the Rotor 30 mechanical mate.
### Remaining open items requiring future work or user input
- Continue manual component verification from `.copilot/components-todo.md`
- Finalise Settings Board red/green LED resistor values after brightness tuning
- Select and confirm the Settings Board `CFG_APPLY` pushbutton
- Confirm the JLCPCB part number for `J_CFG` / `J_I2C` (JST B4B-PH-K-S)
## Next Steps
1. Resume component re-verification from `.copilot/components-todo.md`
2. Propagate only explicitly verified parts into active BOM/design docs
3. Continue Settings Board part-lock work (LED resistor tuning, `CFG_APPLY`, `J_CFG` JLCPCB PN)
4. Start KiCad setup only after remaining TBD parts are locked
## Files Updated
- `README.md`
- `design/Electronics/Boards_Overview.md`
- `design/Electronics/Consolidated_BOM.md`
- `design/Electronics/Controller/Board_Layout.md`
- `design/Electronics/Controller/Design_Spec.md`
- `design/Electronics/Power_Budgets.md`
- `design/Electronics/Power_Module/Board_Layout.md`
- `design/Electronics/Power_Module/Design_Spec.md`
- `design/Electronics/Reflector/Design_Spec.md`
- `design/Electronics/Rotor/Board_Layout.md`
- `design/Electronics/Rotor/Design_Spec.md`
- `design/Electronics/Stator/Board_Layout.md`
- `design/Electronics/Stator/Design_Spec.md`
- `design/Electronics/System_Architecture.md`
- `design/Guides/Maintenance_Guide.md`
- `design/Guides/User_Manual.md`
- `design/Mechanical/HID_Assembly/Design_Spec.md`
- `design/Mechanical/Plugboard_Assembly/Design_Spec.md`
- `design/Mechanical/Power_Module/Design_Spec.md`
- `design/Software/GUI_App/Design_Spec.md`
- `design/Software/Linux_OS/Power_Management.md`
- `design/Standards/Certification_Evidence.md`
- `.copilot/plan.md`
- `.copilot/checkpoints/index.md`
- `.copilot/checkpoints/047-repository-review-cleanup-two-clean-passes.md`
