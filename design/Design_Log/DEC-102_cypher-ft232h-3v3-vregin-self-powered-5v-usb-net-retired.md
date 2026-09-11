# DEC-102 - Cypher FT232H Moved to 3.3V VREGIN Self-Powered Operation (5V_USB Net Retired)

|Field|Value|
|:---|:---|
|**Decision ID**|DEC-102|
|**Status**|Decided|
|**Date**|2026-09-11|
|**Author**|Izzyonstage & GitHub Copilot|
|**Amends**|-|
|**Related**|DEC-098|

## Context

The Cypher Board's USB-JTAG bridge (FT232H, `U17`) was powered from a `5V_USB` rail supplied via
the Controller dock. Investigation (prompted by the `jdb-ft232h-3v3-vregin` todo, originally
written against the pre-merge JTAG Daughterboard architecture) found two issues:

1. **The FT232H part already supports the desired feature.** FT232H Rev C silicon supports
   3.0–3.6V operation on its `VREGIN` pin (in addition to the standard 5V `VREGIN` mode), letting
   the chip run entirely from a 3.3V rail with no separate 5V supply. The already-specified part
   (`FT232HL-REEL`) is this same silicon — Rev C has been the only shipping revision for years,
   and no different part number or package needs to be ordered. (A part number referenced in the
   original todo notes, `FT232HPQ-TRAY`, was investigated and found to be an unrelated FTDI
   product — the newer "HP" USB Type-C/Power-Delivery chip family, not a Rev C variant of the
   plain FT232H; it was not used.)
2. **`5V_USB` was already a phantom/stale net under the current dock architecture.** Following the
   DEC-098 Controller↔Cypher dock split, Cypher's power dock (`J1`) carries only `GND`,
   `5V_MAIN`, and `3V3_ENIG` — there is no `5V_USB` pin on it at all, and `5V_USB` does not appear
   anywhere in the Controller's own design spec. The Controller's `TPS2065C` (`U2`) — which the
   stale text credited as the source of "5V_USB" — is confirmed entirely local to the Controller,
   protecting only its own external USB-A port (`J6`); it has no BtB/dock pin. This was leftover
   terminology from the pre-merge JTAG Daughterboard architecture (which had its own physical
   `5V_USB` BtB pin) that was never fully reconciled when DEC-098 redefined the dock.

## Decision

FT232H (`U17`) is moved to self-powered 3.3V `VREGIN` operation, sourced entirely from
`3V3_ENIG`:

- **`VREGIN`** (pin 40): `3V3_ENIG` (was `5V_USB`).
- **`VCCD`** (pin 39): explicitly tied to `3V3_ENIG`. In 3.3V-`VREGIN` mode this pin becomes an
  **input** (per the FT232H datasheet §6.2.2 reference circuit) rather than the self-generated
  output it is in 5V-`VREGIN` mode — this requires an explicit trace that did not previously
  exist (previously `VCCD` only needed a decoupling cap, since it self-supplied `VCCIO`/`VPLL`/
  `VPHY` internally).
- **`VCCIO`** (pins 12/24/46), **`VPLL`** (pin 8), **`VPHY`** (pin 3): unchanged, already
  `3V3_ENIG`.
- **`VCCA`** (pin 37), **`VCORE`** (pin 38): unchanged — driven by the FT232H's internal 1.8V LDO
  output, no external supply connection either way.
- The `5V_USB` net and its entry filter (`C27`) are removed from Cypher's design entirely — no
  5V rail is required anywhere in the USB-JTAG bridge.
- USB self-powered EEPROM configuration is unchanged (identical requirement in both the 5V and
  3.3V `VREGIN` reference designs); the FT232H's `PWRSAV#`/`ACBUS7` VBUS-loss detection feature
  remains unused, since USB between this board and the CM5 is entirely internal (no external
  cable/connector, so no real VBUS-loss condition exists to detect).

## Rationale

- Removes a rail (`5V_USB`) and its associated entry-filter component entirely, simplifying the
  board's power architecture — one fewer rail to source, decouple, and budget.
- Uses the FT232H's own documented capability rather than any workaround; no part substitution
  or new component required.
- Corrects a genuine pre-existing documentation defect (the phantom `5V_USB` net) surfaced while
  investigating the todo, rather than leaving it in place.

## Impact

- `Cypher/Design_Spec.md §5 USB-JTAG Bridge`: Power Architecture section rewritten; FR-CYP-01,
  DR-CYP-08 updated; new DR-CYP-11 added; `C27` removed from BOM; component block diagram updated.
- `Power_Budgets.md`: FT232H's full 100 mA moved from the `5V_MAIN` table to the `3V3_ENIG`
  Allocation Table (previously split 10 mA `3V3_ENIG` / 100 mA `5V_MAIN`). `3V3_ENIG` typical
  total 2,193 mA → 2,283 mA (rounded 2.20 A → 2.29 A; LDO headroom 27% → 24%). `5V_MAIN` total
  10.79 A → 10.69 A (LMQ61460-Q1 utilisation 89.9% → 89.1%).
- Closes `jdb-ft232h-3v3-vregin`.
