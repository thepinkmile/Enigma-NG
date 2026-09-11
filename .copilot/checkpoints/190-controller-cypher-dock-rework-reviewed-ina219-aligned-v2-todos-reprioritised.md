# Checkpoint 190 — Controller ↔ Cypher Dock Rework Complete & User-Reviewed; INA219 Address Aligned; v2.0 Todos Re-Prioritised

**Date:** 2026-09-11

## Summary

This checkpoint spans two working sessions since checkpoint 189: the main Controller/Cypher dock
rework session (2026-09-04) and a shorter follow-up review/correction session (2026-09-08 through
2026-09-11). `merge-ctl-dock-usb-allocation` and `merge-update-ctl-board` are now **done and
user-reviewed** — the user completed their review during the follow-up session, requested a
handful of small corrections (all applied), and re-prioritised several previously-deferred v2.0
todos. DEC-098 through DEC-101 were created across this span.

## 1. Controller ↔ Cypher dock split by electrical function (DEC-098)

The Controller's former Stator-facing dock (`J4`/`J5`, Molex EXTreme Guardian HD hybrid pair) was
reallocated to the Cypher Board (its electronic replacement) and split strictly by electrical
function:

- **`J4` — power-only** (Molex, unchanged part numbers `2195630015`/`2195620015`): 5x `GND` on
  the larger power-pitch contacts (mates first for safety), 8x `5V_MAIN` + 7x `3V3_ENIG` on
  signal-pitch contacts (4.5A/contact per the Molex product spec — far exceeding actual demand).
  Zero signal contacts.
- **`J5` — signal-only** (new Samtec QSS-025/QTS-025 family, reusing parts already qualified
  elsewhere in the system — no new BOM part number): `USB_D_PLUS`/`USB_D_MINUS` (to Cypher's
  native FT232H bridge), `I2C1` active bus + `I2C2`/`I2C3`/`I2C4`/`I2C6` reserved, `PWM0[0-3]` +
  `GPCLK[0]`/`GPCLK[1]` reserved (to bare test pads on Cypher), all remaining pins `GND`. Zero
  power rails. Full 50-pin map worked out interactively across many rounds with the user (mating
  order, ground-wedge physical layout, column symmetry, PWM staggering for shielding) — see
  `Controller/Board_Layout.md §3.2` / `Cypher/Board_Layout.md §1`.

The obsolete JTAG cluster (`TCK`/`TMS`/`TDI`/`TTD_RETURN`) that had lived on the old Stator dock
was removed from the Controller entirely — Cypher's own FT232H bridge and full 37-device JTAG
chain entry are native to Cypher and never need to leave that board.

## 2. CM5 I²C bank architecture, MIPI0→MIPI1 swap, PWM/GPCLK reservation (DEC-099)

Expanded from one shared "I2C-1" bus to six independent RP1 I²C controller instances:

| Bus | Role | Routing |
| --- | --- | --- |
| `I2C0` | PM-dedicated (freed by AM retirement — see §3) | Controller `J3` |
| `I2C1` | Active Cypher-peripherals bus (existing, unchanged) | Controller `J5` |
| `I2C2`/`I2C3`/`I2C4`/`I2C6` | Reserved/NC on Cypher for a future "Rotor-Cypher-Software-Updates" discussion (not yet in the repo) | Controller `J5` |

Relocated `ROTOR_EN_N`/`PM_IO_INT_N`/`USB_FAULT_N`/`PWR_GD` to free GPIO pins for `I2C2`/`I2C3`.
Moved Controller's DSI1 connector (`J9`) from CM5 MIPI0 to MIPI1 — a real pin-level routing
change (different physical CM5 200-pin DF40 pins), required because `I2C6`'s GPIO pair is shared
silicon with the MIPI0 control bus. Reserved 4x `PWM0` + 2x `GPCLK` channels, routed to six bare
copper test-pad loops on Cypher (`TP1`-`TP6`, each paired with a `GND` test-pad loop `TP7`-`TP12`)
for PoC bring-up flexibility — flagged the DEC-022 buffering precedent (an unbuffered CM5 clock
signal over a long backplane trace was already rejected once, for the JTAG Module) for any future
production use of these reserved signals.

## 3. JTAG Module and Actuation Module retirement from the Controller (DEC-100)

Removed `J12`/`MH9`-`MH12` (JM dock) and `J11`/`MH5`-`MH8`/GPIO8 `ACTUATE_REQUEST_N`/`R4` (AM
dock) entirely from the Controller. Both functions are already native elsewhere: the JTAG bridge
on Cypher (§1 above), and the Actuation Module's solenoid controller (STM32G071K8T3TR) natively
on the Stack-Input Board, one instance per mini-stack, triggered by the existing
`ACTUATE_REQUEST_IN_N`/`OUT_N` round-trip chain (DEC-093/DEC-097, unaffected by this change) —
this was a Controller-side dock removal only, not a system-wide removal of the actuator itself.

Full FR/DR/BOM renumbering was applied to the Controller to close the gaps left by the removed
JM/AM content, per the established project convention (DEC-055/DEC-080).

**Mid-session correction, caught before user review:** an early pass mistakenly deleted
`Power_Budgets.md`'s "servo rail" 5V_MAIN line entirely (conflating dock-removal with
power-removal). Corrected by relocating (not deleting) the line to "Stack-Input Board solenoid
actuation (via Cypher `J4`)" — total restored to 10.79 A / 89.9%. Corrected directly in DEC-100
itself (not a new amending DEC) since the user confirmed DEC-100 was not yet reviewed/sealed at
the time — this exchange is why `.copilot/directives/tertiary.md` now has an explicit rule: ask
the user whether a same-task, not-yet-reviewed DEC is sealed before choosing in-place-edit vs.
new-amending-DEC.

## 4. User review (2026-09-11) and follow-up corrections

The user completed their review of the above and found four issues, all fixed inline:

1. **Two more leftover historical/contrastive sentences** in `Controller/Design_Spec.md` — an
   "entirely native to the Cypher Board" JTAG-removal explainer on FR-CTL-04, and four "Relocated
   from GPIO X..." notes in the GPIO mapping table. Same "current design only" violation class as
   the original pass, just missed the first time.
2. **Board-boundary violation:** `Cypher/Design_Spec.md §7` and `Power_Module/Design_Spec.md §3`
   each named the *other* board's INA219 despite having no direct connection to each other —
   removed both cross-references (system-wide views belong only in `Controller/Design_Spec.md`
   and `Power_Budgets.md`).
3. **DEC-101 created:** Cypher's INA219 (`U2`) I²C address changed `0x45` → `0x40` to match the
   Power Module's `U10` default address — safe since the two devices are on independent I²C buses
   (`I2C0`/`I2C1`); simplifies both hardware (`0x40` needs zero address-strap components, unlike
   the never-fully-specified `0x45` strap) and future monitoring software (identical driver code,
   only the bus differs). Logged the pre-existing stale `0x45`/"Stator" references scattered
   across `Boards_Overview.md`, `Electrical_Design.md`, `Software/Linux_OS/Power_Management.md`,
   `Software/GUI_App/Design_Spec.md`, and a dashboard `.drawio` wireframe into
   `merge-update-top-level-docs.md`'s notes, to be fixed at that todo's proper scheduled pass.
4. **Found (while investigating #3) a genuine pre-existing gap**, unrelated to this session's
   dock rework: `Power_Budgets.md`'s 3V3_ENIG Allocation Table had never budgeted Stack-Input's
   native STM32G071K8T3TR MCU current draw at all. Added a 30 mA (6× 5 mA) placeholder line,
   sourced from the local `stm32g071.md` datasheet's Run-mode `IDD` table, explicitly flagged as
   unverified pending firmware clock configuration and the still-TBD solenoid driver circuit.
   Confirmed `U1` is already `STM32G071K8T3TR` (64KB flash) in the BOM — not a placeholder part;
   noted `STM32G071KBT3TR` (128KB) only as a fallback if 64KB proves insufficient once firmware
   exists. Logged into `post-merge-final-design-bom-sweep.md`'s notes. Typical 3V3_ENIG total
   revised 2,163 mA → 2,193 mA (rounded 2.17 A → 2.20 A; LDO headroom 28% → 27%).

## 5. Todo re-prioritisation (user, 2026-09-11)

Of five previously-blocked "v2.0" items:

- **`cpld-production-replacement` — unblocked.** Tied to the `max-10-fpga-details` and
  (partially) `rp2040-discussion` discussion threads already present in `.copilot/discussions/`.
- **`jdb-ft232h-3v3-vregin` — unblocked.** The Rev C FT232H part (3.0–3.6V VREGIN) is now
  available/sourced.
- `display-addon-board`, `display-aperture`, `ctl-t1-coilcraft-v2-review` — confirmed still
  correctly deferred to v2.0, no change.

Additionally:

- **`cypher-input-led-independent-rgb-pwm-review`** had its `merge-final-review` dependency
  **removed** from `todo_deps` (was gating it on the full design-merge sign-off). User wants to
  pick it up directly after `jdb-ft232h-3v3-vregin`, since its outcome will guide a physical Mock
  Keyboard test rig for the Cypher-Input board (component validation + power-draw probing), and
  the user is not confident in the currently-selected RGB LED part (SK6812MINI-E candidate,
  `merge-missing-components.md`) either.
- **`footprint-requests-pending`** rescheduled (note only, no dependency change) to run alongside
  `post-merge-final-design-bom-sweep` rather than as a standalone earlier task.

## Decisions created this span

DEC-098, DEC-099, DEC-100, DEC-101 — see `design/Design_Log/index.md` for the full list. Next DEC
number: **102**.

## Status

- `merge-ctl-dock-usb-allocation`: **done**.
- `merge-update-ctl-board`: **done**.
- Both **user-reviewed and approved** (2026-09-11) — no pending review gate remains.
- `cpld-production-replacement`, `jdb-ft232h-3v3-vregin`: unblocked, now `pending`.
- `cypher-input-led-independent-rgb-pwm-review`: `merge-final-review` dependency removed, now
  actionable.

## Next steps (user-confirmed order, see `plan.md`)

1. `jdb-ft232h-3v3-vregin` — Rev C FT232H 3V3 VREGIN; now native to Cypher's `U17` USB-JTAG
   bridge section (`Cypher/Design_Spec.md §5`), not a separate JTAG Module.
2. `cypher-input-led-independent-rgb-pwm-review` — independent per-channel RGB PWM + LED part
   reconsideration; feeds directly into the user's planned Mock Keyboard test rig.
3. `cpld-production-replacement` — MAX10 FPGA discussion (`max-10-fpga-details`,
   `rp2040-discussion`); likely mechanical implications for Rotor boards.
4. `footprint-requests-pending` — alongside the final BOM sweep, not standalone.
5. `system-assembly-harnesses` and `system-config-variants-diagrams` — deferred until the above
   list is complete.

Also still queued (not yet scheduled): `design-docs-current-only-sweep` — a repo-wide sweep for
historical/rationale wording that shouldn't be in "current design only" docs (previously only
covered Cypher + Stack-* boards).
