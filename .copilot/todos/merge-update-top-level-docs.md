# Update Boards_Overview, System_Architecture and related docs for merge

**ID:** merge-update-top-level-docs
**Status:** pending
**Category:** Electronics / Documentation
**Source:** design-discussion-merge
**Blocked by:** all merge-create-* and merge-update-ctl-board todos

---

## Description

Update all top-level design documents to reflect the new board set, replacing references to
retiring boards (STA, REF, EXT, JM, AM) with the new Cypher system boards.

## Notes

- design/Electronics/Boards_Overview.md — add all new boards, remove retiring boards.
- design/Electronics/System_Architecture.md — update block diagrams and interface names.
- design/Electronics/Electrical_Design.md — update power paths and signal routing.
- design/Electronics/Power_Budgets.md — recalculate for new board set.
- design/Electronics/Consolidated_BOM.md — remove retiring boards, add new boards.

## Known stale item queue (add to as discovered; do not fix piecemeal until this todo is worked)

- **INA219 rotor-stack monitor address (DEC-101, 2026-09-08):** Cypher Board's INA219 (U2) I2C
  address changed from `0x45` to `0x40` (now matches PM's `U10` default address; safe since the
  two devices are on independent I2C buses — `I2C0` for PM, `I2C1` for Cypher, per DEC-098/
  DEC-099). The following files still reference the old `0x45` address and the retired "Stator"
  board name for this device, and need updating when this todo is worked:
  - `design/Electronics/Boards_Overview.md` — "Stator INA219 (`0x45`): monitors rotor-stack
    `3V3_ENIG`"
  - `design/Electronics/Electrical_Design.md` — I2C address table row `0x45 | INA219 | Stator |
    Rotor stack power telemetry`
  - `design/Software/Linux_OS/Power_Management.md` — multiple references: "The Stator board
    carries an INA219 (U2, I2C address **0x45**)...", the `I2C address | 0x45 | Set by A0/A1 pin
    strapping on Stator INA219` table row, the `INA219_ADDR = 0x45 # Rotor stack monitor on
    Stator board` code sample, and a cross-ref note pointing at "`Stator/Design_Spec.md §5. Power
    Telemetry`" (also a stale board-name reference — that content now lives in
    `Cypher/Design_Spec.md §7 Power Telemetry`)
  - `design/Software/GUI_App/Design_Spec.md` — "Rotor stack monitor: INA219 at I²C address
    **0x45** (on Stator board)..." and a checklist item "address 0x45 (rotor stack), 0x40 (power
    module)"
  - `design/Software/GUI_App/Wireframes/01-main-dashboard.drawio` — two `mxCell` text values
    literally displaying "INA219 @ 0x45" in the mocked-up dashboard UI
  - (Already corrected as part of DEC-101 and NOT stale: `Cypher/Design_Spec.md`,
    `Controller/Design_Spec.md`, `Power_Budgets.md`.)

- **Stack-Input STM32G071K8T3TR MCU 3V3_ENIG power budget (2026-09-11):** `Power_Budgets.md`'s
  3V3_ENIG Allocation Table now carries a **placeholder** line item ("Stack-Input STM32G071K8T3TR
  MCUs (native Actuation Module, one per mini-stack)" — 6x 5 mA = 30 mA) for a consumer that had
  never been budgeted at all (a pre-existing gap predating the Controller/Cypher dock rework
  session, not something introduced by it). The 5 mA/unit figure is a conservative estimate derived
  from the local `design/Datasheets/stm32g071.md` Run-mode `IDD` table (~2.9 mA typ @ 24 MHz,
  rounded up for GPIO/peripheral overhead) — it is **not** a measured or firmware-confirmed value.
  When this todo is worked, revisit and replace with a real figure once:
  - `Stack-Input/Design_Spec.md §4`'s solenoid driver circuit is finalised (currently TBD), and
  - the actual firmware clock configuration (HSI/HSE selection, target frequency) is decided.
  - Also re-check the component selection itself at that point: `U1` is currently specified as
    **STM32G071K8T3TR** (64KB flash, LQFP-32) in `Stack-Input/Design_Spec.md`'s BOM — already
    confirmed as the selected part (not a placeholder). `STM32G071KBT3TR` (128KB flash) was
    considered as an alternative candidate during this session but was **not** adopted since the
    64KB part is already specified and nothing so far indicates 128KB is required; re-confirm
    flash usage is within 64KB once firmware is written, and only switch to `KBT3TR` if that
    proves insufficient.
