# Create Cypher-Output Board Design

**ID:** merge-create-cypher-output
**Status:** pending
**Category:** Electronics
**Source:** design-discussion-merge
**Blocked by:** design-discussion-merge, merge-grs-6layer-stackup

---

## Description

Create design files for the Cypher-Output Board - the lightboard panel board. Accepts 1 ENC
module via Hirose DF40C BtB connectors. Carries LEDs on opposite face.

## Notes

- Connector to Cypher Board (revised 2026-08-09 - mirrors Cypher-Input): 4 connectors, J4/J5
  (top, male, QTS-025-01-L-D-RA-P) + J6/J7 (bottom, female, QSS-025-01-L-D-RA-K), not a single
  connector. Left pair = 3V3_ENIG/GND/reserved 5V_MAIN/LED colour+brightness broadcast (per
  DEC-088, 2026-08-16: no Plugboard-specific signals live here at all - the physical plugboard
  patch-jack harness wires directly from the Cypher Board's own spade terminal bank instead);
  right pair = shared HID Interconnect template owned by `Cypher/Board_Layout.md §4`. Full pin
  numbers (final, 2026-08-09):
  - JTAG: pin 36 (both connectors, tied) = own CPLD TDI; pin 40 (both connectors, tied) = own
    CPLD TDO; pin 37 = passthrough only, both connectors tied together (not connected to own
    CPLD; relays Cypher-Input's real TDI signal through when this board is closer to the Cypher
    Board); TMS/TCK (pins 43/44, 47/48) broadcast, tied both connectors; `CPLD_RESET_N` (pin 23
    only - single pin, broadcast/unchained) - see `Cypher/Design_Spec.md §3` JTAG Hub for the
    full chain order (this board is device 2 of 37, after Cypher-Input).
  - `ENC_ACTIVE_KBD_N` (pin 24, tied both connectors): consumed to activate this board's LEDs,
    and relayed onward (tied, not a pure passthrough - also tapped locally) toward the Cypher
    Board's I2C expander (U6) when this board is positioned between the Cypher Board and
    Cypher-Input. Renamed 2026-08-09 from the placeholder `ENC_ACTIVE_INPUT_N` to match the
    Cypher Board's own internal net name.
  - `ENC_DATA[5:0]` (pins 3-14): bottom row = this board's own consumed data (drives LED bank,
    from Cypher CPLD `ENC_OUT_LBD[5:0]`); top row = straight passthrough, relays Cypher-Input's
    own data through when this board is not directly under the Cypher Board.
  - `BOARD_ROLE_ID[2:0]` (pins 17-22): bottom row = this board's own hardwired variant-ID strap;
    top row = straight passthrough, relays Cypher-Input's own ID code. Encoding (MSB-to-LSB,
    `ID[2],ID[1],ID[0]`): `000` = 64-Char Variant, `001` = 26-Char Variant, `010` = 10-Numeric
    Variant, `011`-`111` reserved - see `Cypher/Board_Layout.md §4` for the full table.
  - `I2C_SCL`/`I2C_SDA` (pins 31/29, tied both connectors): connects to this board's own future
    I2C GPIO expander; shared multidrop bus with Cypher-Input's U4 and the Cypher Board's I2C-1.
  - **Retired per DEC-087 (2026-08-14):** `GREEN_PWM_N`/`YELLOW_PWM_N` (previously pins 30/32) no
    longer exist on this connector pair - see below for the new LED colour/brightness broadcast
    mechanism.
- **Superseded per DEC-087 (2026-08-14) - full LED colour/brightness architecture rework:**
  Cypher-Input generates all LED colour selection and brightness control locally (never via the
  ENC module/`plain-bits` bus - see `Cypher-Input/Design_Spec.md §5`/§6) and broadcasts the
  results to whichever HID board is adjacent via the **left** connector pair (`J4`/`J6` in
  Cypher-Input's numbering, not the JTAG chain-through pair): `RED_DRIVE_N`, `GREEN_DRIVE_N`,
  `BLUE_DRIVE_N` (final, post-mux colour signals) and `BRIGHTNESS_PWM_EN` (shared brightness
  gate). This board therefore needs **no local colour-select mux, Shift-sense network, or 555
  oscillator of its own** - it should simply receive these 4 broadcast signals on its own left
  connector pair and apply them to its own LED bank: 3x P-channel MOSFETs (colour banks, gated by
  the incoming `RED_DRIVE_N`/`GREEN_DRIVE_N`/`BLUE_DRIVE_N`) plus 1x N-channel MOSFET (shared
  cathode-return switch, gated by the incoming `BRIGHTNESS_PWM_EN`) - same topology as
  Cypher-Input's own LED bank, minus the colour-generation circuitry. RV1 (brightness dial) and
  U1 (555 oscillator) exist **only** on Cypher-Input - one physical dial dims every LED on both
  boards. Exact pin numbers for the 4 broadcast signals on the left connector pair are not yet
  finalised - pending `merge-cypher-board-j3j6-pinouts`/this todo's own pinout work.
- LED part: **placeholder, TBD** - Cypher-Input's design now uses a to-be-confirmed RGB SMD LED
  (replacing the previous Kingbright APFA2507Y2G2C-C2 bicolour part) pending user confirmation of
  a part that fits under the Cherry MX2A-71NB keyswitch. This board should use the same part once
  confirmed - see `Cypher-Input/Design_Spec.md §5`.
- 26 LEDs (Classic-equivalent) or 42 LEDs (Extended-equivalent, matching Cypher-Input's variant
  split - see `Cypher-Input/Design_Spec.md §1`); current-limit resistor values are also TBD
  pending the same LED part confirmation (per-channel, not per Yellow/Green as previously noted).
- **Updated per DEC-086 (2026-08-12):** Cypher-Input's U4 now uses a single fixed I2C address
  (`0x38`) shared across all its variants - variant identity is carried solely by
  `BOARD_ROLE_ID[2:0]`, not by I2C address (see `Cypher-Input/Design_Spec.md §3a`). This board
  will need its own I2C GPIO expander (PCA9534A, same part as Cypher-Input's U4) for board-*type*
  identification, connected to the same `I2C_SCL`/`I2C_SDA` bus (pins 31/29) on its Cypher
  interconnect - **not** a pure passthrough. It should take a single fixed address from the free
  `0x39-0x3E` pool (do not reuse `0x38`), mirroring Cypher-Input's single-address-per-board-type
  pattern - **not** per-variant addressing. This board is expected to need its own variants
  (mirroring Cypher-Input's Classic/Extended/10-Numeric split) identified via its own
  `BOARD_ROLE_ID[2:0]` strap value, the same mechanism Cypher-Input uses, once its variant
  requirements are confirmed with the user.
