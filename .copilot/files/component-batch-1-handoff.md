# Component Batch 1 Handoff

## Scope locked in this handoff

The first manual component-verification batch from `.copilot/components-todo.md` is now synced into
the active design docs and repo-local handoff.

### Verified rows in this batch

- `S003` — Settings Board `SW_CFG_APPLY` = Omron `B3F-1070`
- `S005` — Power Module `SW2` = Adafruit `3350`
- `S006` — HID keyboard custom switch = eBay item `365271584375`
- `S007` — Rotor `SW_CFG` = CTS `219-6LPSTR`
- `S008` — Power Module switch harness blade tabs = Keystone `1211`

## Critical design rule restored

Do not drift back to the earlier "64 physical keyboard keys" wording.

- **Physical HID layout:** 40 positions
- **Printable keys:** `[a-z0-9+=]`
- **Modifier keys:** Left Shift + Right Shift
- **Logical code space:** 64 characters total via Shift-generated uppercase alphabetic outputs

Authoritative references:

- `design/Design_Log.md` — **DEC-035**
- `design/Mechanical/HID_Assembly/Design_Spec.md`
- `design/Electronics/Encoder/Design_Spec.md`

## Supporting artifact

The purchased custom keyboard switch is now documented in:

- `design/Datasheets/Gadgetskingdom_DPDT_Keyboard_Switch_Pseudo_Datasheet.md`

That file contains only marketplace metadata and project-specific integration notes. It is **not** a
real manufacturer datasheet and should be treated accordingly.

## Resume point

Continue the manual verification queue from `.copilot/components-todo.md` after the locked switch
batch. The next best targets are the remaining power-management ICs and unresolved Settings Board
supplier rows.
