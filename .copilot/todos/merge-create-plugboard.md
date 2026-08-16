# Create Plugboard Board Design

**ID:** merge-create-plugboard
**Status:** pending
**Category:** Electronics
**Source:** design-discussion-merge
**Blocked by:** design-discussion-merge, merge-grs-6layer-stackup, merge-create-cypher-input, merge-create-cypher-output

---

## Description

Create design files for the Plugboard Board - the termination board that mates with whichever
Cypher-Input/Cypher-Output board occupies the bottom-most position of the local 2-board HID stack
beneath the Cypher Board (mirrors the Stack-Blanking board's role for the 30-rotor mini-stack
chain). Carries male connectors matching the shared Cypher Board HID Interconnect connector
template (Samtec QTS/QSS-025-01-L-D-A-GP-K family, center-GND-bar).

**Architecture clarified 2026-08-16 (DEC-088):** the Plugboard board's electrical role is
**passive HID-chain termination only** - it carries no plugboard-signal-specific pins at all, on
either connector. The physical plugboard patch jacks are mounted on this board but are **not
electrically connected to it** - each jack terminal is wired via a discrete spade-to-spade jumper
cable directly back to the **Cypher Board's own spade terminal bank (`J20+`)**, bypassing this
board's own circuitry and the `J4`-`J7` HID interconnect stack entirely. This board is therefore
electrically simple (passive JTAG-spoke termination, mirroring Stack-Blanking) but mechanically
hosts the plugboard jack field as a panel/fixture.

## Notes

- Connector: matches the shared "Cypher Board HID Interconnect" connector definition (owned by
  `Cypher/Board_Layout.md`) - male, mating the bottom-most board's female BL/BR connectors.
- **Left-side connector (power + reserved 5V_MAIN + LED colour/brightness broadcast):** per
  DEC-088, there are **no plugboard-specific signals to define here** - the left pair only ever
  carries 3V3_ENIG/GND, a few reserved/spare `5V_MAIN` pins (in case a future LED candidate needs
  more than 3.3V - see `merge-missing-components.md`), and the LED colour/brightness broadcast
  signals from whichever HID board is directly above. This board likely just needs to relay/
  terminate those as appropriate (exact behaviour TBD alongside `merge-cypher-board-j3j6-pinouts`)
  - it does **not** need patch-jack signal pins of any kind.
- **Right-side connector (JTAG spoke termination)** - copied from `Stack-Blanking/Design_Spec.md
  §3` (mirrors the rotor mini-stack chain's end-of-chain termination approach):
  - TCK: 10 kOhm pull-down to GND (prevents spurious clocking at JTAG spoke end)
  - TMS: 10 kOhm pull-up to 3V3_ENIG (holds JTAG TAP in Test-Logic-Reset at spoke end)
  - CPLD_RESET_N: 10 kOhm pull-up to 3V3_ENIG (holds CPLDs out of reset at chain end)
  - All 3x resistors: 10 kOhm 1% 0402, ERJ-2RKF1002X (Panasonic), DigiKey P10.0KLCT-ND, Mouser
    667-ERJ-2RKF1002X, JLCPCB C191123; placed within 3mm of the mating connector, per
    Stack-Blanking's DR-SBLK-05 pattern.
  - TTD (both lanes): left NC/unterminated for now, pending confirmation of whether a termination
    resistor is needed there too (Stack-Blanking's chain does not terminate TTD itself, only the
    broadcast/spoke signals - same logic likely applies here, but not yet confirmed with user).
- **Mechanical jack field (per DEC-088):** the physical plugboard patch jacks (see
  `Mechanical/Plugboard_Assembly/Design_Spec.md` for the historical jack-count/harness detail,
  still stale pending the full mechanical overhaul) are mounted on this board as a panel/fixture
  only - no PCB traces connect them to this board's own circuitry. Each jack terminal is wired via
  a discrete spade-to-spade jumper cable to the corresponding spade terminal on the Cypher Board's
  own `J20+` bank (bottom edge of its rear face). This harness routing is new ground for this
  board's design - not yet detailed at the individual-wire level.
- Assembly is expected to be single-sided, passive components only for the PCB's own electrical
  circuitry, mirroring Stack-Blanking's simplicity (5x 0402 resistors on that board; likely 3x
  here given only 3 broadcast spoke signals to terminate, vs Stack-Blanking's 5 which also include
  ENC_ACTIVE_N and ACTUATE_REQUEST_N, not relevant to this board). The jack-field mounting and
  harness routing are mechanical/assembly concerns layered on top of that simple PCB.
- Pin-level mapping for the Cypher-Input/Cypher-Output HID Interconnect connectors (which this
  board's connector must match) was still being iterated with the user as of 2026-08-09 - do not
  finalize this board's exact pinout until that work is confirmed and implemented in
  `Cypher/Board_Layout.md`.

## Reference Material Preserved from Encoder Module Redesign (2026-08-13)

The Encoder Module's redesign (module rename + Hirose DF40C-only interconnect; see checkpoint
covering that change) removed the following content from `Encoder_Module/Design_Spec.md` because
it described the retired spade-terminal/external-jack architecture. It is preserved here for the
Plugboard Board's own design, since the Plugboard Assembly is the successor to that jack-sensing
and harness role.

### Former spade-terminal BOM row (removed from Encoder Module BOM)

| RefDes | Specification | MPN | Manufacturer | DigiKey PN | Mouser PN | JLCPCB PN | Qty |
| --- | --- | --- | --- | --- | --- | --- | --- |
| J2-J65 (on the old single-board Encoder) | 6.35mm PCB spade blade terminals THT vertical | 1285-ST | Keystone Electronics | 36-1285-ST-ND | 534-1285-ST | C5370868 | 64 |

This part was previously fitted directly on the Encoder board (64 per board) to provide the
external jack-field interface for plugboard passes. Under the new architecture the Encoder Module
carries no spade terminals at all (see `Encoder_Module/Design_Spec.md §1`/§3); the spade-terminal
role now lives on the **Cypher Board itself** (`J20+`, `Cypher/Design_Spec.md §6`), with the
Plugboard Board hosting only the mechanical jack field wired back to it (per DEC-088) - not
carrying its own spade terminals.

### Former §7 Plugboard Jack-Sensing (removed from Encoder Module Design_Spec.md)

> The board split does not remove the requirement for plugboard insertion-state awareness, but it
> does move the implementation decision to the per-pass harness / schematic phase. Any sensing
> scheme must preserve the generic one-CPLD module footprint.
>
> For jack panel layout and harness assembly, see
> `design/Mechanical/Plugboard_Assembly/Design_Spec.md`.

This note - that plugboard patch-insertion sensing is still an open implementation decision, to be
resolved at the Plugboard Board / harness design phase rather than on the Encoder Module - should
be carried forward into this board's own design work.
