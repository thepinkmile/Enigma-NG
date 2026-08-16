# DEC-086 - Cypher-Input Restructured into Common/Variant Files; 10-Numeric Variant Added; Single Shared I2C Address

|Field|Value|
|:---|:---|
|**Decision ID**|DEC-086|
|**Status**|Decided|
|**Date**|2026-08-12|
|**Author**|Izzyonstage & GitHub Copilot|
|**Amends**|Cypher-Input `Design_Spec.md §1, §3, §3a, §4, §5, §10, §11`; `Board_Layout.md §4`; supersedes the per-variant I2C addressing introduced in the 2026-08-06 session (see `handoff.md` "What changed in this session (2026-08-06)")|

## Context

The Cypher-Input Board `Design_Spec.md`/`Board_Layout.md` had grown to document two board variants
(26-Char Classic, 64-Char Extended) inline, with per-variant tables and BOM columns interleaved
throughout the common circuit description. This diverged from the pattern already established for
the Rotor board, which splits common circuit design (`Rotor/Design_Spec.md`) from per-variant
detail (`Rotor_26_Char_Design.md`, `Rotor_64_Char_Design.md`).

A design review also identified that the Cypher-Input Board's on-board I2C GPIO expander (U4,
PCA9534A) had been assigned a **distinct I2C address per variant** (0x38 Extended, 0x39 Classic)
for board-type identification. This was redundant: the Cypher Board interconnect already carries a
hardwired `BOARD_ROLE_ID[2:0]` strap (per `Cypher/Board_Layout.md §4`) whose sole purpose is
variant identification, with `0b010` already reserved for a future 10-Numeric variant. A keyboard
board only needs one identification mechanism.

Separately, the system was missing a **10-Numeric** variant: a dedicated number-pad keyboard (0-9)
alongside the existing Classic (26-letter) and Extended (64-character) variants.

## Decision

1. **Restructure Cypher-Input into common + per-variant files**, mirroring the Rotor pattern:
   - `Cypher-Input/Design_Spec.md` and `Board_Layout.md` retain only content common to all
     variants (ENC module interface, LED/brightness/interconnect circuits, PCB fabrication,
     common BOM).
   - `Cypher_Input_26_Char_Design.md`, `Cypher_Input_64_Char_Design.md`,
     `Cypher_Input_10_Numeric_Design.md` each hold that variant's key layout, `plain-bits`
     allocation, `BOARD_ROLE_ID[2:0]` value, LED behaviour note, and variant-specific BOM
     (LED bank, current-limit resistors, hot-swap sockets, mechanical keyswitches).

2. **Add the 10-Numeric variant**: 10 digit keys (0-9) in a common number-pad grid layout
   (`7 8 9 / 4 5 6 / 1 2 3 / Space 0 Enter`), plus Space and Enter for CM5 UI input clarity (same
   non-cipher role as on the Extended variant). No Shift key - digits have no case distinction.
   `BOARD_ROLE_ID[2:0] = 0b010` (already reserved in `Cypher/Board_Layout.md §4`).

3. **Collapse U4 (PCA9534A) to a single fixed I2C address (`0x38`) across all Cypher-Input
   variants.** Variant identification is carried solely by `BOARD_ROLE_ID[2:0]`, not by I2C
   address. `0x39` is no longer reserved for the 26-Char Classic variant and reverts to the free
   pool (`0x39-0x3E`) for future board *types* (e.g. Cypher-Output, or a fully custom keyboard
   board outside this family) - not for further Cypher-Input variants, which use `BOARD_ROLE_ID`
   instead.

## Rationale

- Splitting common/variant content keeps each variant file self-contained and avoids repeatedly
  interleaving 2-3 way conditional text through the common circuit description, consistent with
  the precedent set by the Rotor board.
- A single I2C address for U4 removes a redundant identification mechanism: `BOARD_ROLE_ID[2:0]`
  already exists on the shared Cypher Board interconnect and scales to any number of variants
  without consuming additional I2C address space.
- The 10-Numeric variant reuses the existing circuit topology (ENC module mount, LED bank,
  brightness control, board interconnect, I2C board-ID expander) with no new component types -
  only quantities, key layout, and the `BOARD_ROLE_ID` strap value change.

## Impact

- `design/Electronics/Cypher-Input/Design_Spec.md` - §1 (variant table + 3-file split reference),
  §3 (plain-bits allocation moved to variant files), §3a (single I2C address, BOARD_ROLE_ID as
  sole identifier), §4/§5 (variant text generalised), §10 (10-Numeric data plate naming), §11
  (BOM reduced to common components only).
- `design/Electronics/Cypher-Input/Board_Layout.md §4` - PB[] usage note and BOARD_ROLE_ID note
  updated to include the 10-Numeric variant.
- New files: `Cypher_Input_26_Char_Design.md`, `Cypher_Input_64_Char_Design.md`,
  `Cypher_Input_10_Numeric_Design.md`.
- System-wide I2C address tables updated to reflect the single shared `0x38` address:
  `design/Electronics/Boards_Overview.md`, `Electrical_Design.md`, `System_Architecture.md`,
  `Controller/Design_Spec.md §4.1`.
