# Post-merge final design/BOM consolidation sweep

**ID:** `post-merge-final-design-bom-sweep`  
**Status:** pending  
**Category:** Electronics  
**Source:** `extension-mechanical-usage` discussion
normalisation (2026-07-04)  
**Blocked by:** `extension-mechanical-usage`, `consolidate-design-spec-content`

---

## Description

Run a single final consolidation sweep after merged discussions are
applied into main design files.
This sweep closes remaining procurement-detail lock-in and verifies the complete updated design set
is coherent.

## Notes

- Scope includes final BOM/procurement
detail lock-in for newly merged architecture decisions.
- This is intentionally deferred until after discussion-merge implementation is complete.

## Known items to verify (add to as discovered)

- **Stack-Input U1 (STM32G071K8T3TR) part confirmation (2026-09-11):** currently specified in
  `Stack-Input/Design_Spec.md`'s BOM as `STM32G071K8T3TR` (64KB flash, LQFP-32, STMicroelectronics).
  Confirmed as the already-selected part, not a placeholder, at time of writing. Re-verify flash
  usage stays within 64KB once the Actuation Module firmware (solenoid drive + dual homing switch
  handling) is written — if 64KB proves insufficient, the alternative candidate
  `STM32G071KBT3TR` (128KB flash, same LQFP-32 package/pinout) should be substituted at that point.
  Also re-check the `Power_Budgets.md` 3V3_ENIG placeholder line for this part (currently an
  estimated 5 mA/unit, not measured) once firmware clock configuration is finalised — see
  `merge-update-top-level-docs.md` for the full detail.
