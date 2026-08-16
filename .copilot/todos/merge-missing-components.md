# Identify and select missing/supporting BOM components for new boards

**ID:** merge-missing-components
**Status:** pending
**Category:** Electronics / Procurement
**Source:** design-discussion-merge
**Blocked by:** merge-consistency-review

---

## Description

Identify all BOM components not yet sourced or with TBD MPNs across new board designs.
Select and confirm approved parts, including footprint and 3D model availability.

## Notes

- Spade tab connectors (Keystone 1285-ST confirmed; arrangement TBD at schematic time).
- Stack-Interposer IDC-header connectors (type TBD).
- MX-compatible keyboard switches and Kailh sockets (confirmed MPNs; add to new BOM rows).
- Any new passives required by the 6-layer Cypher Board routing.
- **Cypher-Input RGB LED indicator part** (D1-D26/D1-D42/D1-D12 across all 3 variants) - explicitly
  deferred here (2026-08-15) rather than sourced ad hoc mid-merge, since more parts are likely to
  need sourcing before this todo runs anyway. Placeholder/TBD in all variant BOM rows per
  `Cypher-Input/Design_Spec.md §5` and DEC-087; must physically fit under the Cherry MX2A-71NB
  keyswitch cutout (approx. "0402/0403"-class, to be verified). Current-limit resistor values
  (R1-R26/R1-R42/R1-R12, one per colour channel) are blocked on this part's per-channel V_F and
  cannot be finalised until it is selected. Not to be sourced without explicit user approval, per
  the `component-lookup` directive and established sourcing-responsibility convention.

  **Candidate part identified by user (2026-08-16): SK6812MINI-E, sold as Adafruit stock #4960.**
  Supplier part numbers (user-provided, 2026-08-16): DigiKey `1528-4960-ND`, Mouser `485-4960`,
  JLCPCB `C5331175` (consignment/basic - verify library status when sourcing is confirmed).
  Datasheet and KiCad library assets already staged locally, verified present this session:
  - Datasheet: `design/Datasheets/Adafruit-4960_SK6812MINI-E_REV02_EN.pdf` (OPSCO
    Optoelectronics, Rev 02, 18 pages). Markdown datasheet generated this session via
    `.copilot/agent-scripts/generate_markdown_datasheets.py` -
    `design/Datasheets/Adafruit-4960_SK6812MINI-E_REV02_EN.md` - and the shared
    `_generated_markdown_inventory.json` index rebuilt to include it (`same_stem` mapping).
    Use the markdown version for future lookups per the `component-lookup` directive's MD -> PDF
    -> ask-user order.
  - KiCad library zip: `src/Electronics/Library/temp/LIB_4960.zip` (Adafruit part #4960,
    downloaded 2026-08-16) - full multi-CAD export; confirmed it contains `KiCad/4960.kicad_sym`,
    `4960.kicad_mod`, `4960.lib`/`.dcm`/`.mod` (legacy), and a 3D STEP model (`3D/4960.stp`).
    Not yet imported into `SamacSys_Parts.*` - import only once the part is formally selected,
    following the existing library-import workflow (see `ctl-t1-tdk-library-import` for
    precedent).
  - **Package:** 3.2 x 2.8 x 1.78mm SMD, reverse-mount (top-view emission through the PCB, not
    off the top face) - 4-pin: `VDD`, `DOUT`, `GND`, `DIN`. This is the key opportunity the user
    flagged: because it emits *through* the board rather than off the top face, it could be
    reflow-soldered on the **rear face alongside every other rear-face component**, via a
    light-pipe cutout/via at each key position - potentially eliminating the LED hand-soldering
    step entirely and leaving **only RV1** as a manual post-PCBA fit. This would need prototype
    verification of the light-pipe cutout approach (light transmission through the board/solder
    mask, cutout size, keycap/switch stack-up clearance) before committing - likely a small
    trial-board exercise, consistent with the user's own "may need a few trial and error boards"
    expectation. Do not assume this works without physical verification.
  - **Critical open concern - supply voltage:** datasheet specifies `VDD` = +3.7V to +5.5V
    (Electrical Parameters, §8). The system's `3V3_ENIG` rail (3.3V nominal) is **below this
    minimum** as documented. This needs explicit resolution before the part can be adopted -
    options include confirming an undocumented lower-voltage tolerance with the manufacturer,
    sourcing from a different (boosted or dedicated) rail, or ruling the part out if neither is
    viable. Flagging prominently - this is not yet resolved.
  - **This is an addressable ("NeoPixel"-style) LED, not a simple 3-channel RGB LED** - it has an
    integrated constant-current driver and a single-wire digital protocol (unipolar
    NRZ/one-wire, ~800 kbps, per the datasheet's Switching Characteristics/Timing Waveform
    sections), not separate analogue R/G/B drive lines. Each pixel receives 24 bits (8 bits per
    channel, **GRB bit order** per the datasheet's Data Structure section - not RGB) on `DIN`,
    latches its own value, and forwards the remainder out `DOUT` to the next pixel in the chain
    (`DIN`->`DOUT` daisy-chain wiring between pixels, per the datasheet's Connection Mode
    diagram). A ~500 Ohm series resistor on the data line is recommended by the datasheet for
    signal integrity.
  - **Confirmed design impact - the current drive circuit is not compatible and would need to be
    replaced, not just re-sourced:** the existing `Design_Spec.md §5` architecture (U4 GPIO ->
    `RED_DRIVE_N`/`GREEN_DRIVE_N`/`BLUE_DRIVE_N` -> R1-Rxx current-limit resistors -> U5-U7
    P-channel MOSFET colour banks, plus the 64-Character variant's U9 mux/D9/R9 Shift-sense
    circuit) is built entirely around simple analogue RGB LEDs with externally-switched colour
    channels. None of that drive circuitry applies to an addressable LED - R1-Rxx, U5-U7, and
    (on the 64-Character variant) U9/D9/R9 would all be removed if this part is adopted, replaced
    by: per-pixel daisy-chain wiring, one data-line series resistor per chain (or per pixel, TBD),
    and **something to generate/drive the single-wire protocol** - this board currently has no
    component capable of that (the ENC module CPLD is dedicated to the cipher pipeline; U4 is a
    plain I2C GPIO expander with no PWM/protocol generation capability). Candidates to evaluate:
    a small dedicated microcontroller, spare CPLD I/O bit-banging the protocol (see the
    `enc-cpld-spare-pins-rule` precedent), or driving it from the CM5 (raised by the user in the
    "independent per-channel RGB PWM" discussion, `cypher-input-led-independent-rgb-pwm-review`
    todo) - CM5 userspace GPIO bit-banging is unlikely to meet the sub-microsecond timing
    tolerances in the datasheet's Data Transmission Time table without PIO/DMA-backed hardware
    support, so this needs real investigation, not an assumption that it "just works" over a
    GPIO pin.
  - **Also brings full 24-bit RGB colour mixing "for free"** (256 levels per channel, not just an
    on/off palette) - this would fully satisfy the separately-tracked
    `cypher-input-led-independent-rgb-pwm-review` per-channel-PWM concern as a side effect, if
    adopted, since PWM-equivalent colour depth is generated internally by the LED's own driver
    rather than needing external per-channel PWM circuitry on this board.
  - **Not yet approved for sourcing or import** - this is a candidate under evaluation, not a
    decision. Do not import into `SamacSys_Parts.*`, update any BOM row, or change the drive
    circuit in `Design_Spec.md`/variant files until the user explicitly confirms adoption,
    including resolution of the VDD/`3V3_ENIG` concern above.
