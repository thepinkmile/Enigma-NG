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
  - **Cypher-Output uses the same LED part as Cypher-Input (2026-08-16) - update both boards
    together.** `Cypher-Output/Design_Spec.md §2`/§4 and `Cypher-Output/Board_Layout.md` (all 3
    variant files) currently document the LED bank as top-face, hand-soldered, mirroring
    Cypher-Input's own placeholder wording - with an explicit open-item note in each board's
    `Design_Spec.md` flagging that the mounting face is provisional pending this todo. If the
    reverse-mount candidate (or any other rear-face-mountable part) is adopted, both boards'
    `Design_Spec.md` (§2 Architecture, LED Specification section) and `Board_Layout.md`
    (Orientation Convention, top/rear face component lists) need updating in the same pass, not
    just Cypher-Input's. Cypher-Output has no colour-select mux/Shift-sense circuitry to remove
    (unlike Cypher-Input's 64-Character variant U9/D9/R9), but does have its own per-position
    select MOSFETs (Q1-Qxx) whose gate wiring would be unaffected by a mounting-face change -
    only the LED footprint/orientation and hand-soldering step would change.
  - **Critical open concern - `5V_MAIN` power budget headroom is tight and highly sensitive to the
    final part's actual per-channel current (flagged 2026-08-17):** every current-limit resistor
    and system power-budget figure for both boards' LED banks (`Power_Budgets.md` 5V_MAIN Load
    Analysis) is currently based on a **10mA/channel design target, not a measured value** -
    because no LED part is selected yet. The system-level `5V_MAIN` rail (LMQ61460-Q1, 12.0A
    dual-phase capacity) is already at **89.9% utilisation (10.79A)** with this 10mA/channel
    assumption, leaving only **~1.21A of headroom**. This headroom is consumed almost entirely by
    **Cypher-Input**, not Cypher-Output: Cypher-Input lights its **entire key bank simultaneously**
    (up to 42 keys x 3 channels on the 64-Character variant), so its contribution scales as
    `keys x 3 x per-channel mA` - any increase in the final part's actual per-channel current is
    amplified ~126x on that variant. Cypher-Output, by contrast, only ever lights **one lens
    position at a time** (one-hot decode), so its contribution stays negligible (30mA at
    10mA/channel, still only 60mA even at 20mA/channel) regardless of the part chosen - it is not
    a concern here.

    **Sensitivity check (64-Character variant, current 10.79A/12.0A = 89.9%):**

    | Actual current/channel | Cypher-Input load | New system total | Utilisation |
    | :--- | :--- | :--- | :--- |
    | 10mA (current assumption) | 1.26 A | 10.79 A | 89.9% |
    | 15mA | 1.89 A | 11.42 A | 95.2% |
    | 20mA | 2.52 A | 12.05 A | **exceeds LMQ61460-Q1 capacity** |

    **When selecting the final LED part, explicitly re-run this calculation using the part's real
    recommended/typical drive current for the desired brightness** (not just its absolute max
    rating) before approving it. Prefer candidates that hit the desired brightness at or below
    ~10mA/channel to preserve system margin; if a higher-current part is otherwise the best fit,
    flag the resulting utilisation to the user explicitly - do not silently accept a figure that
    pushes the LMQ61460-Q1 near or over its 12.0A capacity. Note that an addressable/constant-
    current part (e.g. the SK6812MINI-E candidate above) has its **own internal current source**
    per the datasheet, which may make this calculation different in kind (fixed per-pixel current
    draw rather than a resistor-set target) - re-derive the worst-case figure from that part's
    actual datasheet current, not the 10mA assumption, if it is the part ultimately adopted.
    Update `Power_Budgets.md` 5V_MAIN Load Analysis and this note together once the real figure is
    known.
  - **Options considered to reduce this power draw (discussed with user 2026-08-17), in
    descending order of impact vs. architectural disruption:**
    1. **Row/column scanning (multiplexed, not all-on-at-once)** - light only a fraction of keys
       at any instant, cycling fast enough (>100Hz) for persistence-of-vision; each LED runs
       briefly brighter to compensate. Cuts *instantaneous* `5V_MAIN` draw roughly in proportion
       to the fraction of keys lit at once, at the same perceived brightness. Requires a scan
       controller (spare CPLD I/O bit-banging, or a small MCU) and is a real change to
       Cypher-Input's current "light the whole bank simultaneously" architecture (§5 Drive
       Topology would need a full redesign, not a part swap).
    2. **Higher-efficacy LED part** - some parts reach usable backlight brightness at 2-5mA
       instead of 10mA, cutting the budget with no architecture change. A factor to weigh
       alongside VDD/package/mounting-face concerns already tracked above.
    3. **Cap max brightness below 100% duty cycle** (firmware or hardware limit on the existing
       555 dimmer / addressable-LED brightness value) - cheap, but gives up top-end brightness
       headroom permanently.
    4. **Move the LED bank onto its own dedicated regulator**, off the shared `5V_MAIN`/
       LMQ61460-Q1 rail - doesn't reduce total system power, but stops LEDs competing with
       CM5/USB/HDMI for the same regulator's headroom. Adds a component, otherwise non-invasive.
    5. **Addressable LEDs (SK6812MINI-E candidate) enable options 1 and 3 in firmware** - being
       software-addressable means scanning/brightness-capping can be done in software once the
       protocol driver exists, without extra scan-driver hardware beyond what option 1 already
       needs.
  - **User's current direction (2026-08-17, not yet a final decision):** leaning towards the
    SK6812MINI-E (candidate above) combined with **option 1 (row/column scanning)** to reduce the
    constant `5V_MAIN` load, with **option 3 (capped max brightness)** as a possible further
    reduction depending on how bright the scanned/multiplexed result actually looks in practice.
  - **Next step - proof-of-concept test board required before committing to this direction:**
    build a small, cheap PoC board carrying a handful of SK6812MINI-E pixels (enough to exercise
    the daisy-chain protocol and a representative scan/mux pattern, not a full 26/40/12-position
    board) with **explicit current-measurement test probe hooks** (e.g. a shunt/Kelvin-sense
    test point pair in series with the LED supply rail, matching the approach already used
    elsewhere in the system - see `Power_Budgets.md` CSS2H-2512R-R010ELF precedent - and/or simple
    unpopulated 0R link footprints that can be swapped for a sense resistor) so actual current
    draw and perceived brightness can be measured directly, rather than assumed. This PoC must
    resolve, before the real board design is finalised: (a) real per-pixel current at a usable
    brightness level, feeding back into the sensitivity table above; (b) whether the reverse-mount
    rear-face light-pipe approach actually transmits enough light through the PCB; (c) whether the
    chosen scan rate/duty pattern gives acceptable perceived brightness without visible flicker;
    and (d) resolution of the VDD/`3V3_ENIG` supply-voltage concern already flagged above. Do not
    finalise the Cypher-Input/Cypher-Output LED drive circuit redesign until this PoC's results are
    reviewed with the user.
    - **Also populate Kailh PG151101S11 hot-swap sockets (confirmed MPN, see the top-level note
      above) on the PoC board, with real Cherry MX2A-71NB switches and keycaps fitted** - this
      lets the PoC test the full real-world stack-up (switch + keycap physically over/around the
      reverse-mount LED and its light-pipe cutout), not just the LED/protocol/current behaviour in
      isolation. This is needed to properly judge (b) and (c) above under realistic conditions
      (light transmission through the actual cutout with a keycap fitted, and perceived
      brightness/flicker as the operator would actually see it, not on a bare board), and to
      catch any mechanical clearance issues between the switch/keycap stack-up and the reverse-
      mount package before committing to it on the real boards.
