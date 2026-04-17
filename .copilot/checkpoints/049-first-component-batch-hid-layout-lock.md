# Checkpoint 049 — First component batch locked; HID layout and pseudo datasheet synced

## Date
2026-04-17

## Overview

This checkpoint locks in the first manual component-verification batch after the repo-local handoff
was reloaded from `.copilot/`. The session started with the first five switch and user-input rows
from `.copilot/components-todo.md`, worked them through with explicit user confirmation, and then
propagated the approved parts into the active design docs.

The batch ended with a larger HID clarification than originally expected: the purchased custom
keyboard switch was accepted, a pseudo datasheet was written from the marketplace listing metadata,
and the keyboard/lightboard architecture was re-frozen as a **40-position physical layout** mapped
into the machine's **64-character logical code space**.

## Work Done

### First component verification batch completed

- Verified **Settings Board `SW_CFG_APPLY`** as **Omron `B3F-1070`**
- Replaced the stale Controller reset-button assumption with the correct **Power Module `SW2`**
  tracking row, then verified `SW2` as **Adafruit `3350`**
- Verified **Rotor `SW_CFG`** as **CTS `219-6LPSTR`**
- Rejected TE `1-1452688-2` as the Power Module harness blade-tab candidate because it is an
  ACTION-PIN press-fit style part, then verified **Keystone `1211`** instead
- Updated the Power Module docs so `SW1` + `SW2` now share the same 16 mm family / 2.8 mm terminal
  harness concept, with **12 total** Keystone `1211` blade tabs

### Settings Board `CFG_APPLY` requirement corrected

- Relaxed the old strict panel-mount requirement for `CFG_APPLY`
- Locked the design to a **board-mounted tactile switch** that may be actuated through the enclosure
- Updated both the electrical and mechanical docs to describe the actuator/plunger concept instead
  of a literal exposed panel pushbutton

### HID keyboard switch and layout locked

- Reviewed the custom keyboard-switch eBay listing from seller `gadgetskingdom`
- Extracted the usable marketplace metadata:
  - DPDT
  - momentary
  - 6 pins
  - straight through-hole terminals
  - 4 mm pin pitch
  - 42 mm × 9.7 mm × 18 mm nominal overall size
- Wrote a repo-local pseudo datasheet at:
  - `design/Datasheets/Gadgetskingdom_DPDT_Keyboard_Switch_Pseudo_Datasheet.md`
- Updated the HID and Encoder docs to replace the stale "64 physical keyboard keys" wording with:
  - **40 physical HID positions**
  - printable keys = `[a-z0-9+=]`
  - modifier keys = Left Shift + Right Shift
  - uppercase alphabetic outputs produced by Shift, not by separate uppercase-only key positions
- Added **DEC-035** to freeze that layout rule in the design log

## Commits

None. This checkpoint syncs the repo-local handoff state and the current working tree.

## Key Technical Notes

### Reset topology correction

The old Controller-local reset-button concept is stale. `SYS_RESET_N` is now driven from the Stator
side via `U_EXP2 GPA[7]`, so the user-input row that still implied a Controller reset button needed
to be retired from the active component queue.

### HID architecture now fixed

Future sessions should **not** reintroduce the old 64-physical-key assumption. The current design
rule is:

1. **Physical positions:** 40 total
2. **Printable positions:** `[a-z0-9+=]`
3. **Modifiers:** Left Shift + Right Shift
4. **Logical repertoire:** 64 unique codes = `a-z`, `A-Z`, `0-9`, `+`, `=`

### Current verification state

`.copilot/components-todo.md` now has **13 VERIFIED rows** total. The newly locked rows in this
checkpoint are:

- `S003` — `SW_CFG_APPLY`
- `S005` — Power Module `SW2`
- `S006` — HID keyboard custom switch
- `S007` — Rotor `SW_CFG`
- `S008` — Power Module switch harness blade tabs

## Next Steps

1. Continue manual component re-verification from `.copilot/components-todo.md`
2. Prioritise the remaining power-management ICs and outstanding Settings Board supplier rows
3. Propagate only explicitly `VERIFIED` rows into active design/BOM docs
4. Start KiCad project setup only after the critical remaining TBD parts are locked

## Files Updated

- `README.md`
- `design/Design_Log.md`
- `design/Datasheets/Gadgetskingdom_DPDT_Keyboard_Switch_Pseudo_Datasheet.md`
- `design/Electronics/Boards_Overview.md`
- `design/Electronics/Consolidated_BOM.md`
- `design/Electronics/Encoder/Design_Spec.md`
- `design/Electronics/Power_Module/Design_Spec.md`
- `design/Electronics/Settings_Board/Design_Spec.md`
- `design/Mechanical/HID_Assembly/Design_Spec.md`
- `design/Mechanical/Main_Enclosure/Design_Spec.md`
- `design/Mechanical/Rotor_Actuation_Assembly/Design_Spec.md`
- `.copilot/components-todo.md`
- `.copilot/plan.md`
- `.copilot/checkpoints/index.md`
- `.copilot/checkpoints/049-first-component-batch-hid-layout-lock.md`
- `.copilot/files/component-batch-1-handoff.md`
