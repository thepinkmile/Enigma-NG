# Create Cypher-Input Board Design

**ID:** merge-create-cypher-input
**Status:** done
**Category:** Electronics
**Source:** design-discussion-merge
**Blocked by:** design-discussion-merge, merge-grs-6layer-stackup

---

## Description

Create design files for the Cypher-Input Board - the keyboard panel board. Accepts 1 ENC
module via Hirose DF40C BtB connectors. Carries MX-compatible keyboard switches on
opposite face with Kailh PG151101S11 hot-swap sockets.

Draft created 2026-08-06: `design/Electronics/Cypher-Input/Design_Spec.md` and
`Board_Layout.md`. Restructured 2026-08-12 (per review feedback) to mirror the Rotor board's
common/variant-file split: `Design_Spec.md`/`Board_Layout.md` now hold only common circuit
content, with per-variant detail in `Cypher_Input_26_Char_Design.md`,
`Cypher_Input_64_Char_Design.md`, and the new `Cypher_Input_10_Numeric_Design.md`. Documents
**three variants**: **26-Char Classic** (QWERTZ, 26 letters only, no Shift/digits/symbols, mimics
original Enigma), **64-Char Extended** (42 keys: 26 letters + 10 digits + 2 base64-extra symbols
`+`/`/` + 2 Shift + Space + Enter; base64 alphabet per RFC 4648), and **10-Numeric** (12 keys: 10
digits in a common number-pad grid + Space + Enter, no Shift). All three variants share identical
circuit topology; only key count/layout, LED/resistor/socket quantities, `plain-bits` allocation,
and `BOARD_ROLE_ID[2:0]` value differ. U4's I2C address is a **single fixed value (0x38) shared
by all variants** (corrected 2026-08-12 - see DEC-086); variant identity is carried solely by
`BOARD_ROLE_ID[2:0]`.

## Notes

- Connector to Cypher Board (revised 2026-08-09): 4 connectors, J4/J5 (top, male,
  QTS-025-01-L-D-RA-P) + J6/J7 (bottom, female, QSS-025-01-L-D-RA-K), replacing the original
  single-J4 model. Left pair (J4/J6) = 3V3_ENIG/GND/Plugboard passthrough; right pair (J5/J7) =
  shared JTAG chain-through template owned by `Cypher/Board_Layout.md §4`. See
  `Cypher-Input/Design_Spec.md §7` and `Board_Layout.md §4` for full pin-level wiring.
- 555 astable PWM oscillator for LED brightness (dial: Bourns 3310P-001-503L). **Superseded
  2026-08-14 (DEC-087):** PWM no longer feeds the ENC module's `GCLK0` - it now gates a shared
  cathode-return switch (U8, BSS138) common to all LED colours; see below.
- **Superseded 2026-08-14 (DEC-087):** LEDs are no longer Kingbright APFA2507Y2G2C-C2 bicolour
  (Yellow/Green) driven from `YELLOW_DRIVE_N`/`GREEN_DRIVE_N` piggybacked onto spare `plain-bits`
  positions. Colour selection is now a fully local, software-configurable RGB circuit generated
  entirely on this board (never via the ENC module/`plain-bits`):
  - U4 (PCA9534A) GPIO defines colour code(s): 64-Char Extended (only variant with a Shift key)
    uses two codes ("Colour A"/"Colour B", 6 GPIO) selected in real time by a local hardware mux
    (U9, `74HC157PW-Q100,118` - reused from the Cypher Board's own keyboard-source mux) driven by
    a diode-OR Shift-sense network (D9 `BAT54C`, R9); Classic/10-Numeric drive one fixed-but-
    configurable colour directly (3 GPIO, no mux).
  - `RED_DRIVE_N`/`GREEN_DRIVE_N`/`BLUE_DRIVE_N` drive 3x P-MOSFETs (U5/U6/U7,
    SQ2319ADS-T1_BE3 - same part family as before, now 3 instead of 2).
  - LED part itself is now a **placeholder (TBD)** - the user needs to confirm a specific RGB SMD
    part that fits under the Cherry MX2A-71NB keyswitch cutout before current-limit resistor
    values can be finalised. Not sourced by the agent.
  - Final colour + brightness signals broadcast to the future Cypher-Output board via the left
    connector pair (`J4`/`J6`), not the JTAG pair - see `Design_Spec.md §5`/§6/§7 and DEC-087 for
    full detail.
- ENC module mounts: DF40C-90DS + DF40C-24DS + DF40C-10DS.
- New this session (2026-08-06): on-board I2C GPIO expander U4 (PCA9534A) for board-type
  identification on all variants, and (Extended and 10-Numeric variants only) reading Space/Enter
  outside the cipher pipeline. U4 connects to `I2C_SCL`/`I2C_SDA` (pins 31/29 on `J5`/`J7`) -
  **not** a pure passthrough; the future Cypher-Output board's own expander shares this same bus
  but takes its own address. **Corrected 2026-08-12 (DEC-086):** single fixed I2C address 0x38
  shared by all Cypher-Input variants (was 0x38 Extended / 0x39 Classic) - variant identity is
  carried solely by `BOARD_ROLE_ID[2:0]`, not I2C address. 0x39-0x3E remain free for future board
  *types* (e.g. Cypher-Output), not further Cypher-Input variants. **Updated 2026-08-14
  (DEC-087):** U4's remaining GPIO (previously flagged as reserved for "a future signal set") are
  now fully allocated to LED colour configuration - see above.
- 4 system-wide I2C address tables updated 2026-08-12 to the single 0x38 address: `Electronics/
  Electrical_Design.md`, `Electronics/System_Architecture.md`, `Electronics/Boards_Overview.md`,
  `Controller/Design_Spec.md §4.1`.

## Resolved items (2026-08-16)

- **Left-side (J4/J6) Plugboard passthrough question fully resolved (DEC-088).** There are **no**
  Plugboard-specific signals on this connector pair at all - the physical plugboard patch-jack
  harness wires directly from the Cypher Board's own spade terminal bank (`J20+`) to jacks
  mechanically mounted (no electrical connection) on the Plugboard board, bypassing the `J4`-`J7`
  HID interconnect stack entirely. The left pair only ever carries 3V3_ENIG/GND, the LED
  colour/brightness broadcast signals (per DEC-087), and now a few reserved/spare `5V_MAIN` pins
  (in case a future LED candidate needs more than 3.3V - see `merge-missing-components.md`'s
  SK6812MINI-E candidate note). This was the only remaining blocking item for this board - see
  checkpoint 185 and DEC-088 for full detail.

## Resolved items (2026-08-14)

- **LED colour architecture fully reworked (DEC-087)** - colour selection moved entirely off the
  ENC module's `plain-bits` bus onto a local, software-configurable RGB circuit (U4 GPIO + local
  mux/Shift-sense on the Extended variant only); brightness moved from feeding the ENC module's
  `GCLK0` to gating a shared cathode-return switch (U8); both broadcast to the future Cypher-Output
  board via the left connector pair (`J4`/`J6`) instead of the JTAG pair. See checkpoint 183 and
  DEC-087 for full detail. LED part itself remains an open placeholder (see below).

## Resolved items (2026-08-12)

- **Common/variant-file restructure** - Cypher-Input now mirrors the Rotor board pattern: common
  content in `Design_Spec.md`/`Board_Layout.md`, per-variant detail in
  `Cypher_Input_26_Char_Design.md`, `Cypher_Input_64_Char_Design.md`,
  `Cypher_Input_10_Numeric_Design.md`.
- **10-Numeric variant added** - 10 digit keys (0-9) in a common number-pad grid layout
  (`7 8 9 / 4 5 6 / 1 2 3 / Space 0 Enter`) + Space + Enter (non-cipher, same role as Extended);
  no Shift. `BOARD_ROLE_ID[2:0] = 0b010` (already reserved from 2026-08-09).
- **U4 I2C addressing corrected** - single fixed address 0x38 across all variants; see DEC-086.

## Resolved items (2026-08-09)

- **JTAG chain-through wiring** - fully resolved. Full 37-device chain order defined in
  `Cypher/Design_Spec.md §3` JTAG Hub: FT232H -> Cypher-Input CPLD (device 1) -> Cypher-Output
  CPLD (device 2) -> 4x Plugboard Encoder Modules (devices 3-6) -> Cypher Board's own U1 CPLD
  (device 7) -> 30x Rotor CPLDs (devices 8-37) -> `TTD_RETURN` -> FT232H. Pin-level wiring for
  this board's J5/J7 connectors defined in `Board_Layout.md §4`.
- **Second-connector/Plugboard gap** - partially resolved. The 4-connector-per-board architecture
  (2026-08-09) now provides a left-side connector pair (J4/J6) reserved for future Plugboard
  passthrough signals, addressing the structural gap. Exact Plugboard signal allocation is still
  undefined - tracked separately under the new `merge-create-plugboard` todo.
- **Non-JTAG signal reallocation into J4-J7** - fully resolved (2026-08-09). Full 50-pin map for
  J5/J7 now defined in `Cypher/Board_Layout.md §4` and `Cypher-Input/Board_Layout.md §4`:
  `ENC_DATA[5:0]` (pins 3-14, top row = this board's own generated data, bottom row = passthrough
  to Cypher-Output), `BOARD_ROLE_ID[2:0]` (pins 17-22, top row = this board's own hardwired
  variant-ID strap, bottom row = passthrough), `CPLD_RESET_N` (pin 23 only, broadcast), `I2C_SDA`/
  `I2C_SCL` (29/31, shared multidrop bus, single pin each - renamed from `I2C_SCL_PASS`/
  `I2C_SDA_PASS`), `GREEN_PWM_N`/`YELLOW_PWM_N` (30/32, driven by this board, consumed only by
  Cypher-Output - **retired 2026-08-14, DEC-087**: LED broadcast moved to the left connector pair
  `J4`/`J6` instead), plus the previously-resolved JTAG block (`TTD` x3, `TMS`, `TCK`).
- **`ENC_ACTIVE_KBD_N` pin assignment** - fully resolved (2026-08-09). Renamed from the
  placeholder `ENC_ACTIVE_INPUT_N` to match the Cypher Board's existing internal net name.
  Assigned pin 24 (freed up by reducing `CPLD_RESET_N` to a single pin, 23, since it is a
  broadcast/unchained signal and does not need 2 pins). Tied both J5 and J7 on this board -
  generated here, consumed by Cypher-Output (LED activation) and the Cypher Board's I2C
  expander U6 (rotor-actuation trigger).
- **`BOARD_ROLE_ID[2:0]` encoding** - fully resolved (2026-08-09), bit order MSB-to-LSB
  (`ID[2],ID[1],ID[0]`): `000` = 64-Char Variant, `001` = 26-Char Variant, `010` = 10-Numeric
  Variant, `011`-`111` reserved for future use. See `Board_Layout.md §4` for the full table.

## Blocking open items

**None remaining** - see "Resolved items (2026-08-16)" above.

## Open item (not blocking, but must resolve before BOM is final)

- **RGB LED part selection** - the LED bank BOM rows (all 3 variant files) are currently a
  placeholder (`TBD`). The user needs to confirm a specific SMD RGB LED part that physically fits
  under the Cherry MX2A-71NB keyswitch cutout before current-limit resistor values can be
  calculated. Not sourced by the agent - see DEC-087.
