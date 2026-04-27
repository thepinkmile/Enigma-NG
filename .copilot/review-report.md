# Electronics Review Report

## Objective

Deep-dive review of the active electronics design documentation to verify that:

- all required circuit-support components are present in the relevant board BOMs
- IC support networks are documented completely enough for functional implementation
- connector pin mappings remain consistent across related documents

This review explicitly excludes physical PCB placement and routing-quality review.

## Method

The review is being run as explicit outer passes for auditability:

1. review pass
2. fix pass
3. re-review pass

All updates to this report are **additive**. Earlier findings and pass results must remain intact.

## Unsourced New Parts Requiring User Selection

Add any newly identified required parts here when the design evidence shows a part class, value, or
function is needed but the exact sourced MPN has not already been selected by the user. The agent must
not pick those parts autonomously.

- Rotor local FDC2114 I²C pull-up pair (`SDA` / `SCL`) is now captured as a required unsourced BOM
  placeholder population; exact resistor value / footprint / sourced MPN remains owner-selected.
- Rotor FDC2114 local `1 µF` `VDD` reservoir capacitors for populated `U2/U3/U4` are now captured as
  required unsourced BOM placeholder population; exact footprint / sourced MPN remains owner-selected.

## Pass Log

### Pass 1 — Review

- Status: in progress
- Notes: pending first review-pass output

#### Pass 1 Findings

#### Scope summary

Reviewed `design/Electronics/Consolidated_BOM.md`, all active `design/Electronics/*/Design_Spec.md` files, connector-contract sections in related `Board_Layout.md` files, and
`design/Software/Actuation_Module/Design_Spec.md`, with focus limited to BOM completeness for active circuits and connector mapping consistency. Physical placement/routing quality was not reviewed.

##### 1. Fixed by existing docs / no action

- **Severity:** info  
  **Files:** `design/Electronics/Stator/Board_Layout.md`, `design/Electronics/Extension/Board_Layout.md`, `design/Electronics/Reflector/Board_Layout.md`  
  **Issue:** The 20-pin reflector / extension connector contract is internally consistent across the owning and consuming docs: `3V3_ENIG` on pin 1, `SYS_RESET_N` on pin 2, `TTD_RETURN` on pin 15,
  and grouped `5V_MAIN` / returns on pins 17-20.  
  **Why it matters:** This is the shared cable contract for Reflector and Extension boards; a mismatch here would create immediate harness miswires.  
  **Recommended fix:** None.  
  **Status:** no action

- **Severity:** info  
  **Files:** `design/Electronics/Actuation_Module/Design_Spec.md`, `design/Software/Actuation_Module/Design_Spec.md`, `design/Electronics/Controller/Design_Spec.md`,
  `design/Electronics/Extension/Design_Spec.md`  
  **Issue:** The Actuation Module service/host mapping is consistent at the document level: AM J6 pinout and SW1/SW2 ROM-boot sequence agree with the firmware spec, and the Controller / Extension
  host-dock descriptions match the AM power/trigger split.  
  **Why it matters:** Prevents a bring-up trap on the only STM32-based module that depends on both SWD and ROM-bootloader service paths.  
  **Recommended fix:** None.  
  **Status:** no action

##### 2. Evidence-backed doc/BOM gaps suitable for a later fix pass

- **Severity:** medium  
  **Files:** `design/Electronics/Actuation_Module/Design_Spec.md`, `design/Software/Actuation_Module/Design_Spec.md`, `design/Electronics/Consolidated_BOM.md`  
  **Issue:** The AM documentation says the module provides local biasing for active-low `ACTUATE_REQUEST`, and normal boot assumes `BOOT0` is LOW at reset release, but the BOM only captures the
  home-input support network (`R4`, `C1`). There is no explicit documented support network for `ACTUATE_REQUEST`, `BOOT0`, or `NRST`.  
  **Why it matters:** These nets define whether the STM32 boots normally and whether host-trigger input state is deterministic. If the design intends to rely on internal STM32 biasing, that
  dependency is not frozen anywhere in the active docs.  
  **Recommended fix:** In a later fix pass, either document the intentional reliance on internal STM32 biasing, or add explicit AM support-part rows / refdes for the `ACTUATE_REQUEST`, `BOOT0`, and
  `NRST` networks.  
  **Status:** deferred schematic capture

- **Severity:** medium  
  **Files:** `design/Electronics/Power_Module/Design_Spec.md`  
  **Issue:** The Power Module spec requires INA219 U12 support parts (`0.1uF` decoupling plus RC filtering on `IN+` / `IN-`), but the BOM only identifies U12 and shunt R23. The capacitor groups
  listed for other ICs do not name U12, and no INA219 filter resistors/capacitors are refdes-assigned.  
  **Why it matters:** INA219 accuracy and stability depend on its local bypassing and the sense-input filter network being captured consistently; right now those support parts are design intent only,
  not procurement-ready BOM content.  
  **Recommended fix:** Add explicit U12 decoupling and input-filter rows/refdes to the Power Module BOM and roll them into the consolidated counts.  
  **Status:** pending fix pass

- **Severity:** high  
  **Files:** `design/Electronics/Stator/Design_Spec.md`, `design/Electronics/Stator/Board_Layout.md`, `design/Electronics/Consolidated_BOM.md`  
  **Issue:** Stator support-passive documentation is incomplete for non-CPLD ICs. The spec requires INA219 filtering on U2, and the board-layout doc explicitly requires local decoupling at U8, but
  the Stator BOM only lists `C1-C8` as "8 per CPLD" plus the bulk bank. That does not capture local bypassing for U2-U8 or the INA219 RC filter network.  
  **Why it matters:** The Stator hosts the routing CPLD, three MCP23017s, one INA219, one logic gate, and two muxes. Missing support-passive rows here are a real manufacturing/procurement gap, not
  just wording.  
  **Recommended fix:** Add explicit per-IC decoupling rows/refdes for U2-U8 and explicit INA219 sense-filter rows/refdes, then align the consolidated BOM.  
  **Status:** pending fix pass

- **Severity:** high  
  **Files:** `design/Electronics/Settings_Board/Design_Spec.md`  
  **Issue:** The Settings Board LED architecture is electrically underdefined/inconsistent. U2/U3 are documented as directly driving LED anodes HIGH, while the LEDs are also documented as
  common-anode parts powered from `5V_MAIN`, and only low-side BSS138 colour-rail sinks are present in the BOM. No high-side 5V anode driver stage is documented.  
  **Why it matters:** A 3.3V MCP23017 output cannot be treated as a generic 5V high-side anode source without freezing the actual LED-drive topology and current path. As written, the board-level LED
  implementation is not fully realizable from the BOM alone.  
  **Recommended fix:** Freeze one topology in the docs/BOM: either a true 3.3V-anode implementation with recalculated currents/resistors, or a separate high-side 5V anode drive stage.  
  **Status:** deferred schematic capture

- **Severity:** high  
  **Files:** `design/Electronics/Encoder/Board_Layout.md`, `design/Electronics/Stator/Board_Layout.md`  
  **Issue:** The Encoder board-layout JTAG signal-map table has incorrect connector pin numbers. `§3 Data Link Pinout` and the Stator-owned encoder-port contract place `TCK/TMS/TDO/TDI/SYS_RESET_N`
  on pins `10/12/14/16/18`, but `§4.1 Dedicated device pins` states `9/11/13/15/17`.  
  **Why it matters:** This is a real connector-map contradiction. If used during schematic capture or test-harness creation, it would shift JTAG/reset onto GND shield pins.  
  **Recommended fix:** Correct `Encoder/Board_Layout.md §4.1` to match the pin table and the Stator-owned connector contract.  
  **Status:** pending fix pass

- **Severity:** medium  
  **Files:** `design/Electronics/Consolidated_BOM.md`, `design/Electronics/Stator/Design_Spec.md`, `design/Electronics/Encoder/Design_Spec.md`  
  **Issue:** The consolidated BOM still carries stale logic-support content from superseded designs: it lists `R20` as `STATOR_CFG_RDY` pull-down, while the active Stator spec uses `CFG_APPLY_N`
  pull-up, and it still describes encoder-side external pull-up / RC filter populations that the active Encoder spec explicitly omits.  
  **Why it matters:** Consolidated_BOM is procurement-facing. Stale support-part definitions can reintroduce removed networks or incorrect resistor intent during later BOM export.  
  **Recommended fix:** Update the consolidated BOM to match the current Stator `CFG_APPLY_N` implementation and current Encoder active design assumptions.  
  **Status:** pending fix pass

##### 3. Unresolved items needing user selection or future schematic-capture work

- **Severity:** medium  
  **Files:** `design/Electronics/Rotor/Design_Spec.md`  
  **Issue:** The Rotor docs lock the FDC2114 devices but do not fully capture the required front-end support network. The active text references FDC2114-based sensing and says unused channels are
  tied off, but the BOM does not freeze the resonant front-end parts or tie-off population needed to make the channels implementable.  
  **Why it matters:** The FDC2114 is not a standalone sensor input; the channel front end is part of the circuit definition. Without a frozen support network, the rotor sensing chain remains
  design-intent only.  
  **Recommended fix:** Complete the future schematic-capture definition for the FDC2114 channel support network, including the resonant front-end and all unused-channel tie-offs, then reflect that in
  the rotor BOM.  
  **Status:** needs user selection

##### Unsourced New Parts Requiring User Selection

- Rotor FDC2114 channel front-end passive selection is not frozen in the active docs. If the intended resonant/support network requires new sourced inductors and/or trim capacitors, those parts need
explicit user selection before BOM closure.

##### Pass Result

#### Pass 1 result: not clean

### Pass 1 — Fix

- **Status:** partial fix applied

#### Files changed

- `design/Electronics/Power_Module/Design_Spec.md`
- `design/Electronics/Stator/Design_Spec.md`
- `design/Electronics/Encoder/Board_Layout.md`
- `design/Electronics/Consolidated_BOM.md`
- `.copilot/review-report.md`

#### Fixes applied

- **Closed finding 3 — Encoder `Board_Layout.md` JTAG pin-number mismatch**
  - Updated `design/Electronics/Encoder/Board_Layout.md §4.1` so `TCK/TMS/TDO/TDI/SYS_RESET_N`
    now reference connector pins `10/12/14/16/18`, matching the board's own pin table in §3 and
    the Stator-owned encoder-port contract.

- **Partially closed finding 1 — Power Module INA219 support parts missing from BOM**
  - Added `C43` in `design/Electronics/Power_Module/Design_Spec.md` for the already-documented
    U12 INA219 100nF local VCC bypass capacitor, using the existing locked 0402 decoupling part.
  - This closes the missing-decoupling portion of the finding without introducing a new unsourced
    filter-resistor part number.

- **Partially closed finding 2 — Stator non-CPLD decoupling / INA219 filter parts missing from BOM/docs**
  - Added explicit Stator-local bypass documentation in `design/Electronics/Stator/Design_Spec.md`
    and added `C14-C20` as one 100nF bypass capacitor per Stator-local IC `U2-U8`, using the
    existing locked 0402 decoupling part.
  - This closes the missing non-CPLD decoupling portion of the finding that was already evidenced by
    the active Stator docs and board-level support-IC population.

- **Closed finding 4 — Consolidated BOM stale Stator / Encoder support-part content**
  - Updated `design/Electronics/Consolidated_BOM.md` to remove the stale encoder-only external input
    RC-filter and pull-up rows that are explicitly omitted by the active Encoder design.
  - Updated the Stator R20 entry from the retired `STATOR_CFG_RDY` pull-down description to the
    active `CFG_APPLY_N` pull-up implementation, and aligned the explanatory note below that table.
  - Updated the common 100nF decoupling count row to reflect the newly explicit PM U12 and Stator
    U2-U8 bypass populations.

#### Unresolved / needs later review or user selection

- **Power Module INA219 input RC filter population remains unresolved.**
  Active docs require an INA219 `IN+` / `IN-` RC filter, but the repository does not yet freeze a
  user-selected sourced resistor part number for that filter network. I did not invent one.

- **Stator INA219 input RC filter population remains unresolved.**
  Active docs require an INA219 `IN+` / `IN-` RC filter, but the repository does not yet freeze a
  user-selected sourced resistor part number for that filter network. I did not invent one.

- **Previously deferred items remain deferred**
  - AM support network for `ACTUATE_REQUEST` / `BOOT0` / `NRST`
  - Settings Board LED topology
  - Rotor FDC2114 front-end sourcing / network definition

- **Commits:** no commits were made.

### Pass 3 — Fix

- **Status:** consolidated BOM count correction applied

#### Files changed

- `design/Electronics/Consolidated_BOM.md`
- `.copilot/review-report.md`

#### Fixes applied

- **Closed Pass 3 finding 1 — PM `0.1 µF` consolidated count lagged added `C43`**
  - Updated the `0.1 µF X7R 0402 decoupling cap — common fitted population` row in
    `design/Electronics/Consolidated_BOM.md` from PM `16` to PM `17`.
  - Updated the same row's system total from `389` to `390`.
  - Rationale: Pass 3 identified that the consolidated common-capacitor count had not been rolled forward
    after PM `C43` was added, leaving the procurement-facing summary undercounted by one fitted `0.1 µF`
    capacitor.

#### Unresolved / left unchanged

- Rotor pull-up exact sourcing remains open.
- Rotor FDC2114 `1 µF` bypass exact sourcing remains open.
- AM `ACTUATE_REQUEST` / `BOOT0` / `NRST` support network remains deferred.
- Settings Board LED topology remains deferred.
- Rotor FDC2114 resonant front-end / unused-channel support definition remains deferred.
- PM / Stator INA219 input RC filter exact sourced parts remain owner-selected and unchanged.

- **Commits:** no commits were made.

### Pass 3 — Review

#### Scope summary

Re-reviewed `design/Electronics/Consolidated_BOM.md`, all active `design/Electronics/*/Design_Spec.md`
files, related connector-contract / logical signal-map sections in `Board_Layout.md`, the AM firmware
spec at `design/Software/Actuation_Module/Design_Spec.md`, and the current report after Fix Pass 2.
Focus remained limited to BOM completeness for active circuitry and connector-map consistency only;
physical placement/routing was not reviewed.

#### Pass 3 Findings

##### 1. New findings

- **Severity:** low  
  **Files:** `design/Electronics/Consolidated_BOM.md`, `design/Electronics/Power_Module/Design_Spec.md`  
  **Issue:** The consolidated `0.1 µF` decoupling count still undercounts the Power Module by one part. Fix
  Pass 1 added PM `C43` as the INA219 `U12` local bypass capacitor in the PM BOM, so the PM now has
  `17` fitted `0.1 µF` capacitors (`C24-C39`, `C43`). `Consolidated_BOM.md` still shows PM=`16` and a
  system total of `389` for the common `0.1 µF` X7R 0402 capacitor row.  
  **Why it matters:** `Consolidated_BOM.md` is procurement-facing. Leaving the table at the pre-fix count
  creates a small but real underbuy risk on a common fitted capacitor line item.  
  **Recommended fix:** In a later fix pass, update the consolidated PM count from `16` to `17` and the
  corresponding system total from `389` to `390`.  
  **Status:** pending fix pass

##### 2. Unchanged known unresolved items

- **Severity:** medium  
  **Files:** `design/Electronics/Actuation_Module/Design_Spec.md`, `design/Software/Actuation_Module/Design_Spec.md`, `design/Electronics/Consolidated_BOM.md`  
  **Issue:** The AM support-network definition for `ACTUATE_REQUEST` / `BOOT0` / `NRST` remains in the
  same deferred state as prior passes; Pass 3 found no new repo evidence freezing those support networks.  
  **Why it matters:** These nets still determine deterministic request-input state and STM32 boot/reset
  behavior.  
  **Recommended fix:** Same as prior passes: either document intentional reliance on internal STM32
  biasing/filtering or add explicit AM support-part rows / refdes during later schematic-capture work.  
  **Status:** deferred schematic capture

- **Severity:** high  
  **Files:** `design/Electronics/Settings_Board/Design_Spec.md`  
  **Issue:** The Settings Board LED-drive topology remains underdefined/internally inconsistent; Pass 3
  found no new evidence resolving the already-known `3.3V` MCP23017-anode-drive versus `5V_MAIN`
  common-anode conflict.  
  **Why it matters:** The indicator circuit still is not fully realizable from the active docs/BOM alone.  
  **Recommended fix:** Freeze one LED-drive topology in the docs/BOM during later schematic-capture work.  
  **Status:** deferred schematic capture

- **Severity:** medium  
  **Files:** `design/Electronics/Rotor/Design_Spec.md`  
  **Issue:** The Rotor FDC2114 resonant front-end / unused-channel support network remains unfrozen; Pass 3
  found no new repository evidence resolving the already-known channel-support definition gap.  
  **Why it matters:** The rotor sensing chain is still not fully defined at the channel-support-network
  level.  
  **Recommended fix:** Complete the future schematic-capture definition for the FDC2114 channel support
  network and reflect it in the Rotor BOM once the required parts are owner-selected.  
  **Status:** needs user selection

- **Severity:** medium  
  **Files:** `design/Electronics/Power_Module/Design_Spec.md`, `design/Electronics/Stator/Design_Spec.md`, `design/Electronics/Consolidated_BOM.md`  
  **Issue:** The INA219 input RC filter exact sourced parts remain unfrozen on both the Power Module and
  Stator. Pass 3 found no new evidence that freezes the `IN+` / `IN-` filter population to sourced BOM
  rows.  
  **Why it matters:** The telemetry filter network remains not procurement-closed even though the sensing
  IC and shunt selections are otherwise documented.  
  **Recommended fix:** Add the user-approved INA219 filter resistor/capacitor population and refdes to the
  per-board BOMs and consolidated counts in a later fix pass.  
  **Status:** needs user selection

- **Severity:** medium  
  **Files:** `design/Electronics/Rotor/Design_Spec.md`, `design/Electronics/Consolidated_BOM.md`  
  **Issue:** Rotor `R6-R7` I²C pull-ups and `C15/C17/C19` `1 µF` FDC2114 bypass capacitors remain
  intentionally captured as unsourced placeholders after Fix Pass 2. Pass 3 found no new repo evidence
  that closes their owner-selected value / footprint / MPN selection.  
  **Why it matters:** The required populations are now documented, but procurement closure still depends on
  owner-selected exact parts.  
  **Recommended fix:** Leave as-is until the user selects the exact sourced parts, then roll those
  selections into the Rotor and consolidated BOMs.  
  **Status:** needs user selection

##### 3. Connector consistency check

- **Severity:** info  
  **Files:** `design/Electronics/Encoder/Board_Layout.md`, `design/Electronics/Stator/Board_Layout.md`, `design/Electronics/Extension/Board_Layout.md`, `design/Electronics/Reflector/Board_Layout.md`,
  `design/Electronics/Rotor/Design_Spec.md`, `design/Electronics/Settings_Board/Design_Spec.md`  
  **Issue:** No new connector-mapping contradictions were found in the reviewed active connector
  contracts after Fix Pass 2. The previously corrected Encoder JTAG numbering remains aligned with the
  Stator-owned contract, and the reviewed Reflector / Extension / Rotor / Settings-board mappings remain
  internally consistent.  
  **Why it matters:** Confirms the reviewed board-to-board and service connector definitions are not
  carrying a new documented miswire trap.  
  **Recommended fix:** None.  
  **Status:** clean

#### Unsourced New Parts Requiring User Selection

- None newly identified in Pass 3.
- Previously known unresolved user-selection items remain unchanged:
  - Rotor FDC2114 resonant / front-end support-network parts
  - Power Module INA219 input RC filter sourced parts
  - Stator INA219 input RC filter sourced parts
  - Rotor `R6-R7` I²C pull-up exact value / package / MPN
  - Rotor `C15/C17/C19` `1 µF` bypass exact package / MPN

#### Pass Result

#### Pass 3 result: not clean

Reason: one new evidence-backed consolidated-BOM count discrepancy remains (`0.1 µF` PM count / total),
even though no new connector-map contradictions were found and all previously deferred/user-selection
items remain unchanged.

### Pass 2 — Review

#### Scope summary

Re-reviewed `design/Electronics/Consolidated_BOM.md`, all active `design/Electronics/*/Design_Spec.md`
files, related connector-contract / logical signal-map sections in `Board_Layout.md`, the AM firmware
spec at `design/Software/Actuation_Module/Design_Spec.md`, and the current report. Focus remained on
BOM completeness for active circuits and connector-map consistency only; placement/routing was not
reviewed. Fix Pass 1 changes were verified in-repo before this pass: the Encoder JTAG pin-number table
is corrected, PM U12 decoupling is now explicit, Stator U2-U8 bypass caps are now explicit, and the
stale Consolidated_BOM Stator/Encoder content is cleaned up.

#### Pass 2 Findings

- **Severity:** info  
  **Files:** `design/Electronics/Encoder/Board_Layout.md`, `design/Electronics/Stator/Board_Layout.md`, `design/Electronics/Extension/Board_Layout.md`, `design/Electronics/Reflector/Board_Layout.md`,
  `design/Electronics/Rotor/Design_Spec.md`  
  **Issue:** No remaining connector pin-map contradictions were found in the reviewed active connector contracts after Fix Pass 1. The previously-broken Encoder JTAG numbering now matches the
  Stator-owned port definition, and the reviewed Reflector / Extension / Rotor-facing contracts remain internally consistent.  
  **Why it matters:** This confirms the harness and board-to-board interface definitions are no longer carrying an obvious miswire trap in the reviewed docs.  
  **Recommended fix:** None.  
  **Status:** clean

- **Severity:** high  
  **Files:** `design/Electronics/Rotor/Design_Spec.md`, `design/Electronics/Consolidated_BOM.md`, `design/Datasheets/fdc2112-datasheet.md`  
  **Issue:** The Rotor local sensor I²C bus still has no explicit `SDA` / `SCL` pull-up population. The Rotor spec says the CPLD polls FDC2114 devices over a local I²C bus, including the Board A ↔
  Board B `H_SENS` link, but the Rotor BOM only captures JTAG pull resistors (`R2-R5`) plus CPLD-only decoupling (`C1-C8`). The in-repo FDC2114 datasheet explicitly assumes external pull-up current
  on `SCL` / `SDA`. No Rotor or consolidated BOM row captures that network.  
  **Why it matters:** Without a frozen pull-up network, the local sensor bus idle-high / ACK behavior is undocumented and can fail at bring-up. This is a real circuit-support omission, not just a
  wording issue.  
  **Recommended fix:** Add explicit Rotor-local `SDA` / `SCL` pull-up rows / refdes for the FDC2114 bus and align the consolidated BOM, or explicitly document a different intended bias method if that
  is truly the approved design.  
  **Status:** pending fix pass

- **Severity:** medium  
  **Files:** `design/Electronics/Rotor/Design_Spec.md`, `design/Electronics/Consolidated_BOM.md`, `design/Datasheets/fdc2112-datasheet.md`  
  **Issue:** The Rotor BOM still does not capture the FDC2114 local bypass network. Board A and Board B list no FDC-specific decoupling; the only 0402 decouplers called out are `C1-C8` "8 per CPLD",
  and the consolidated BOM still counts only 8 × `0.1 µF` caps per rotor. The in-repo FDC2114 datasheet recommends `0.1 µF` and `1 µF` bypass capacitors at `VDD` for each device.  
  **Why it matters:** This leaves the populated sensing ICs without documented local supply support parts in the procurement-facing BOM set. It is a remaining BOM-completeness gap independent of the
  separately deferred resonant front-end definition.  
  **Recommended fix:** Add explicit per-device FDC2114 local bypass rows / refdes for populated `U2` / `U3` / `U4` instances and roll those counts into the consolidated BOM. Keep this separate from
  the still-deferred resonant front-end / unused-channel support capture.  
  **Status:** pending fix pass

- **Severity:** medium  
  **Files:** `design/Electronics/Actuation_Module/Design_Spec.md`, `design/Software/Actuation_Module/Design_Spec.md`, `design/Electronics/Consolidated_BOM.md`  
  **Issue:** The AM support-network gap for `ACTUATE_REQUEST` / `BOOT0` / `NRST` remains unresolved. Pass 2 found no new repository evidence that freezes those nets beyond the already-known deferred
  state.  
  **Why it matters:** These nets still determine normal boot behavior and deterministic request-input state on the only MCU-based module in the design.  
  **Recommended fix:** Same as Pass 1: either document intentional reliance on internal STM32 biasing, or add explicit AM support-part rows / refdes for those networks during a later
  fix/schematic-capture pass.  
  **Status:** deferred schematic capture

- **Severity:** high  
  **Files:** `design/Electronics/Settings_Board/Design_Spec.md`  
  **Issue:** The Settings Board LED-drive topology remains underdefined/internally inconsistent exactly as noted in Pass 1. Pass 2 found no new evidence resolving the 3.3V MCP23017-anode-drive versus
  `5V_MAIN` common-anode implementation conflict.  
  **Why it matters:** The indicator circuit still is not fully realizable from the active docs/BOM alone.  
  **Recommended fix:** Freeze one LED-drive topology in the docs/BOM during a later schematic-capture pass.  
  **Status:** deferred schematic capture

- **Severity:** medium  
  **Files:** `design/Electronics/Rotor/Design_Spec.md`  
  **Issue:** The Rotor FDC2114 resonant front-end / unused-channel support network remains unfrozen. Pass 2 found no new evidence resolving the already-known missing channel-front-end definition.  
  **Why it matters:** The rotor sensing chain is still not fully defined at the channel-support-network level.  
  **Recommended fix:** Complete the future schematic-capture definition for the FDC2114 channel support network and reflect it in the Rotor BOM once the required parts are owner-selected.  
  **Status:** needs user selection

- **Severity:** medium  
  **Files:** `design/Electronics/Power_Module/Design_Spec.md`, `design/Electronics/Stator/Design_Spec.md`, `design/Electronics/Consolidated_BOM.md`  
  **Issue:** The INA219 input RC filter exact sourced parts remain unfrozen on both the Power Module and Stator. Fix Pass 1 closed the missing decoupling portions, but Pass 2 found no new evidence
  that freezes the `IN+` / `IN-` filter population to sourced BOM rows.  
  **Why it matters:** The telemetry filter network is still not procurement-closed even though the sensing IC and shunt selections are otherwise documented.  
  **Recommended fix:** Add the user-approved INA219 filter resistor/capacitor population and refdes to the per-board BOMs and consolidated counts in a later fix pass.  
  **Status:** needs user selection

#### Unsourced New Parts Requiring User Selection

- None newly identified in Pass 2.
- Previously known unresolved user-selection items remain unchanged:
  - Rotor FDC2114 resonant / front-end support-network parts
  - Power Module INA219 input RC filter sourced parts
  - Stator INA219 input RC filter sourced parts

#### Pass Result

#### Pass 2 result: not clean

### Pass 2 — Fix

- **Status:** targeted rotor documentation/BOM fix applied

#### Files changed

- `design/Electronics/Rotor/Design_Spec.md`
- `design/Electronics/Consolidated_BOM.md`
- `.copilot/review-report.md`

#### Fixes applied

- **Closed Pass 2 finding 1 — Rotor local FDC2114 I²C bus missing explicit `SDA` / `SCL` pull-up population**
  - Added explicit Rotor Board A BOM row `R6-R7` in `design/Electronics/Rotor/Design_Spec.md` for the
    required local FDC2114 I²C pull-up pair to `3V3_ENIG`, covering the common rotor-local bus used by
    `U2` plus the variant-dependent second FDC (`U3` on Board A for N=26, `U4` over `H_SENS` for N=64).
  - Added matching unsourced consolidated-BOM summary row in `design/Electronics/Consolidated_BOM.md`
    with `2` pull-up resistors per rotor / `60` per full 30-rotor build.
  - Rationale: the in-repo FDC2114 datasheet accounts for external `SCL` / `SDA` pull-up current, and
    the active Rotor docs already freeze this as a local I²C bus. Exact resistor value / footprint / MPN
    remain intentionally owner-selected rather than agent-chosen.

- **Closed Pass 2 finding 2 — Rotor FDC2114 local bypass network missing from BOM capture**
  - Added explicit Rotor BOM rows `C14/C16/C18` for the datasheet-recommended `0.1 µF` local `VDD`
    bypass capacitors at populated FDC2114 positions `U2/U3/U4`, using the already-locked common 0402
    decoupling capacitor.
  - Added explicit Rotor BOM rows `C15/C17/C19` for the datasheet-recommended `1 µF` local `VDD`
    reservoir capacitors at those same FDC positions, with unsourced procurement placeholders because the
    exact owner-approved part / footprint is not yet frozen in-repo.
  - Updated `design/Electronics/Consolidated_BOM.md` so the common `0.1 µF` fitted-population count now
    includes the two populated FDC decouplers per rotor (`10` per rotor, `300` total), and added a
    separate unsourced Rotor-only `1 µF` reservoir-capacitor summary row (`2` per rotor, `60` total).
  - Added Rotor spec text explicitly separating these `VDD` support parts from the still-deferred
    resonant front-end / unused-channel support definition, so the fix does not over-claim closure of the
    front-end finding.

#### Unresolved / left for later review, user selection, or schematic capture

- **Rotor pull-up exact sourcing remains open.** `R6-R7` are now documented as required population, but
  exact resistor value, package, and sourced MPN still require owner selection.
- **Rotor FDC2114 `1 µF` bypass exact sourcing remains open.** `C15/C17/C19` are now documented as
  required population, but exact package / footprint and sourced MPN still require owner selection.
- **Still deferred from earlier review passes**
  - AM `ACTUATE_REQUEST` / `BOOT0` / `NRST` support network
  - Settings Board LED topology
  - Rotor FDC2114 resonant front-end / unused-channel support definition
  - PM / Stator INA219 input RC filter exact sourced parts

- **Commits:** no commits were made.

### Pass 4 — Review

#### Scope summary

Re-reviewed `design/Electronics/Consolidated_BOM.md`, all active `design/Electronics/*/Design_Spec.md`
files, related logical signal-map / connector-contract sections in `Board_Layout.md`, the AM firmware
spec at `design/Software/Actuation_Module/Design_Spec.md`, and the current report after Fix Pass 3.
Focus remained limited to BOM completeness for active circuitry support parts and connector-map
consistency only; physical placement/routing was not reviewed.

#### Pass 4 Findings

##### 1. New findings

- **Severity:** high  
  **Files:** `design/Electronics/Consolidated_BOM.md`, `design/Electronics/Power_Module/Design_Spec.md`  
  **Issue:** The consolidated BOM common summary still misses part of the Power Module SW1/SW2 LED
  sink-stage support population. `Power_Module/Design_Spec.md` lists PM `R31-R33` and `R37-R38` as
  five fitted `1kΩ` 0402 gate resistors, plus `R34-R36` and `R39-R40` as five fitted `10kΩ` 0402
  gate pull-downs. In `Consolidated_BOM.md`, the common matrix has no PM-counted `1kΩ` 0402 summary
  row for those five parts, and the common `10kΩ 0402` row still shows PM=`2`, which only covers
  `R25` and `R27` rather than all seven PM `10kΩ 0402` parts.  
  **Why it matters:** This is a procurement-facing undercount on active gate-support parts for the PM
  LED sink stages (`Q6-Q10`). A build driven from the consolidated summary can underbuy both the
  fitted `1kΩ` gate resistors and five of the fitted `10kΩ` pull-downs.  
  **Recommended fix:** In a later fix pass, align the consolidated summary with the frozen PM BOM:
  capture the five fitted PM `1kΩ 0402` gate resistors in the consolidated summary and update the PM
  `10kΩ 0402` fitted count from `2` to `7`.  
  **Status:** pending fix pass

- **Severity:** medium  
  **Files:** `design/Electronics/Extension/Design_Spec.md`  
  **Issue:** The Extension spec still states `ESD: TVS diode on exposed signal lines` in §5, but the
  board BOM in §6 contains no TVS / ESD protection device.  
  **Why it matters:** This is an evidence-backed spec/BOM contradiction on an exposed interconnect
  boundary. Either a real protection device is missing from the BOM, or the stated ESD strategy is
  stale and can mislead later schematic capture / procurement review.  
  **Recommended fix:** In a later fix pass, resolve the contradiction explicitly: either add the
  intended TVS / ESD device to the Extension BOM or remove / rewrite the stale ESD sentence if the
  approved design does not populate that protection locally.  
  **Status:** pending fix pass

- **Severity:** low  
  **Files:** `design/Electronics/JTAG_Daughterboard/Board_Layout.md`, `design/Electronics/JTAG_Daughterboard/Design_Spec.md`, `design/Electronics/Consolidated_BOM.md`  
  **Issue:** The JTAG Daughterboard layout doc still describes `J2` as a `10-Pin Shrouded Header
  (Asymmetrical)`, while the design spec and consolidated BOM lock `J2` to Adam Tech `PH1-10-UA`,
  a single-row open `1×10` 2.54mm male pin header mating with `RS1-10-G`.  
  **Why it matters:** This is not a pin-map contradiction, but it is still a connector-definition
  inconsistency in a layout-facing document and could drive the wrong footprint family during PCB
  capture.  
  **Recommended fix:** Update the JDB layout doc to describe `J2` as the locked single-row open
  `1×10` pin header so all docs match the approved MPN.  
  **Status:** pending fix pass

##### 2. Unchanged known unresolved items

- **Severity:** medium  
  **Files:** `design/Electronics/Actuation_Module/Design_Spec.md`, `design/Software/Actuation_Module/Design_Spec.md`, `design/Electronics/Consolidated_BOM.md`  
  **Issue:** The AM support-network definition for `ACTUATE_REQUEST` / `BOOT0` / `NRST` remains
  unchanged; Pass 4 found no new repository evidence freezing those support networks.  
  **Why it matters:** These nets still determine deterministic request-input state and STM32
  boot/reset behaviour.  
  **Recommended fix:** Same as prior passes: either document intentional reliance on internal STM32
  biasing/filtering or add explicit support-part rows / refdes during later schematic-capture work.  
  **Status:** deferred schematic capture

- **Severity:** high  
  **Files:** `design/Electronics/Settings_Board/Design_Spec.md`  
  **Issue:** The Settings Board LED-drive topology remains underdefined/internally inconsistent; Pass 4
  found no new evidence resolving the already-known `3.3V` MCP23017-anode-drive versus `5V_MAIN`
  common-anode conflict.  
  **Why it matters:** The indicator circuit still is not fully realizable from the active docs/BOM
  alone.  
  **Recommended fix:** Freeze one LED-drive topology in the docs/BOM during later schematic-capture
  work.  
  **Status:** deferred schematic capture

- **Severity:** medium  
  **Files:** `design/Electronics/Rotor/Design_Spec.md`  
  **Issue:** The Rotor FDC2114 resonant front-end / unused-channel support network remains unfrozen;
  Pass 4 found no new repository evidence resolving that already-known channel-support definition gap.  
  **Why it matters:** The rotor sensing chain is still not fully defined at the front-end /
  unused-channel-support level.  
  **Recommended fix:** Complete the future schematic-capture definition for the FDC2114 channel
  support network and reflect it in the Rotor BOM once the required parts are owner-selected.  
  **Status:** needs user selection

- **Severity:** medium  
  **Files:** `design/Electronics/Power_Module/Design_Spec.md`, `design/Electronics/Stator/Design_Spec.md`, `design/Electronics/Consolidated_BOM.md`  
  **Issue:** The INA219 input RC filter exact sourced parts remain unfrozen on both the Power Module
  and Stator; Pass 4 found no new repository evidence closing those user-selection items.  
  **Why it matters:** The telemetry filter networks are still not procurement-closed even though the
  sensing ICs and shunts are otherwise documented.  
  **Recommended fix:** Add the user-approved INA219 filter resistor/capacitor populations and refdes to
  the per-board BOMs and consolidated counts in a later fix pass.  
  **Status:** needs user selection

- **Severity:** medium  
  **Files:** `design/Electronics/Rotor/Design_Spec.md`, `design/Electronics/Consolidated_BOM.md`  
  **Issue:** Rotor `R6-R7` I²C pull-ups and `C15/C17/C19` `1 µF` FDC2114 bypass capacitors remain
  intentionally captured as unsourced placeholders after earlier fixes; Pass 4 found no new repo
  evidence closing their owner-selected value / footprint / MPN selection.  
  **Why it matters:** Those required populations are documented, but procurement closure still depends
  on owner-selected exact parts.  
  **Recommended fix:** Leave as-is until the user selects the exact sourced parts, then roll those
  selections into the Rotor and consolidated BOMs.  
  **Status:** needs user selection

##### 3. Connector consistency check

- **Severity:** info  
  **Files:** `design/Electronics/Controller/Design_Spec.md`, `design/Electronics/Controller/Board_Layout.md`, `design/Electronics/Extension/Board_Layout.md`,
  `design/Electronics/JTAG_Daughterboard/Design_Spec.md`, `design/Electronics/Rotor/Design_Spec.md`, `design/Electronics/Stator/Board_Layout.md`  
  **Issue:** Pass 4 found no new connector pin-mapping contradictions in the reviewed active connector
  contracts. The new JDB `J2` finding above is a connector-description mismatch, not a pin-allocation
  mismatch.  
  **Why it matters:** Confirms the reviewed board-to-board and service connector signal assignments are
  still not carrying a newly introduced documented miswire trap.  
  **Recommended fix:** None.  
  **Status:** clean

#### Unsourced New Parts Requiring User Selection

- No newly proven required part was closed to a specific unsourced component by Pass 4 evidence alone.
- Conditional unresolved item only: if `design/Electronics/Extension/Design_Spec.md §5` is intended to
  remain true, the missing Extension-board TVS / ESD protection device on exposed signal lines will
  require explicit user selection before BOM closure.

#### Pass Result

#### Pass 4 result: not clean

Reason: no new connector pin-mapping contradictions were found, but Pass 4 identified new
evidence-backed BOM/spec inconsistencies in the active approved-state docs, so the clean-pass
definition is not met.

### Pass 4 — Fix

#### Files changed

- `design/Electronics/Consolidated_BOM.md`
- `design/Electronics/Extension/Design_Spec.md`
- `design/Electronics/JTAG_Daughterboard/Board_Layout.md`

#### Exact fixes applied

- **Closed Pass 4 finding #1 (PM SW1/SW2 LED sink support resistor undercount).**
  - Updated `design/Electronics/Consolidated_BOM.md` common-passives matrix so the PM
    `10 kΩ 1% 0402` fitted count now matches the active PM spec (`7`, not `2`), covering `R25`,
    `R27`, `R34-R36`, and `R39-R40`.
  - Added the missing common-summary row for the fitted PM/SBD `1 kΩ 1% 0402` gate resistors,
    capturing PM `R31-R33` + `R37-R38` and Settings Board `R12-R17`.
  - **Rationale:** aligns the procurement-facing consolidated summary with the already-defined active
    PM LED sink support population for `Q6-Q10`.

- **Closed Pass 4 finding #2 at the board-spec/BOM level (Extension TVS / ESD contradiction).**
  - Updated `design/Electronics/Extension/Design_Spec.md §5` so the ESD statement now explicitly says
    the protection is required but the exact protected nets, device count, footprint, and sourced MPN
    remain owner-selected.
  - Added a matching unsourced BOM placeholder row (`D1 (owner-selected)`) in
    `design/Electronics/Extension/Design_Spec.md §6`.
  - **Rationale:** removes the spec-vs-BOM contradiction without inventing an unsupported TVS part or
    frozen channel count.
  - **Status:** partially closes the Pass 4 concern; exact ESD device selection remains unresolved.

- **Closed Pass 4 finding #3 (JDB `J2` connector description mismatch).**
  - Updated `design/Electronics/JTAG_Daughterboard/Board_Layout.md` to describe `J2` as the locked
    single-row open `1×10` header, matching the approved `PH1-10-UA` MPN already frozen in the JDB
    design spec and consolidated BOM.
  - Updated that layout doc's `Last Updated` date to reflect the fix.
  - **Rationale:** removes the remaining footprint-family wording trap from the layout-facing JDB
    document.

#### Unresolved findings left unchanged

- Extension-board TVS / ESD exact device count, protected-net allocation, footprint, and MPN remain
  owner-selected; no sourced part was added because the active docs still do not freeze those details.
- Previously deferred non-Pass-4 items remain unchanged:
  - AM `ACTUATE_REQUEST` / `BOOT0` / `NRST` support network
  - Settings Board LED topology
  - Rotor FDC2114 resonant front-end / unused-channel support definition
  - PM / Stator INA219 input RC filter exact sourced parts
  - Rotor owner-selected pull-up / reservoir-capacitor placeholders

- **Commits:** no commits were made.

### Pass 5 — Review

**Date:** 2026-04-26  
**Type:** Read-only review after Fix Pass 4  
**Reviewer:** Copilot Electronics Review Agent

#### Scope Summary

Re-reviewed active electronics design documentation for BOM completeness and connector-mapping
consistency, with emphasis on whether each active circuit has its documented support parts
(decoupling, biasing, pull-ups/pull-downs, filters, protection, and related support components)
and whether connector pin mappings remain consistent across related docs. Physical placement and
routing were excluded. Pass 4 fix closures were also re-checked.

Files inspected in this pass included:

- `design/Electronics/Consolidated_BOM.md`
- Active board specs under `design/Electronics/*/Design_Spec.md`
- Connector / signal-map sections in related `Board_Layout.md` files as needed
- `design/Software/Actuation_Module/Design_Spec.md`
- `design/Design_Log.md` where needed
- `.copilot/review-report.md`

#### Pass 4 Fix Closures Re-Verified

| Fix | File | Result |
| :--- | :--- | :--- |
| PM consolidated resistor-count correction | `design/Electronics/Consolidated_BOM.md` | clean |
| Extension ESD / TVS moved to owner-selected wording with BOM placeholder | `design/Electronics/Extension/Design_Spec.md` | clean |
| JTAG Daughterboard `J2` layout description corrected to single-row `1×10` header | `design/Electronics/JTAG_Daughterboard/Board_Layout.md` | clean |

#### Remaining Findings — New in Pass 5

| Severity | Files | Issue | Why it matters | Recommended fix | Status |
| :--- | :--- | :--- | :--- | :--- | :--- |
| medium | `design/Electronics/Encoder/Board_Layout.md`; cross-check: `design/Electronics/Stator/Board_Layout.md` | `Encoder/Board_Layout.md §5.2` still says `U1 TDO -> R6 -> J2 pin 13`, but the authoritative corrected connector map in `Encoder/Board_Layout.md §4.1` defines `TDO` on `J2 pin 14` and `pin 13` as GND. `Stator/Board_Layout.md §4.4` independently agrees that pin 13 is GND and pin 14 is TDO. | This is a real schematic-capture trap: following the stale §5.2 note would route TDO onto a GND-assigned pin and break the JTAG chain. | Update the §5.2 routing note to `U1 TDO -> R6 -> J2 pin 14` so all Encoder connector references agree. | pending fix pass |

#### Remaining Findings — Unchanged Known Unresolved Items

These were already known before this pass and remain unresolved; they are not counted as new Pass 5
findings.

| Severity | Files | Issue | Why it matters | Recommended fix | Status |
| :--- | :--- | :--- | :--- | :--- | :--- |
| medium | `design/Electronics/Actuation_Module/Design_Spec.md`; `design/Software/Actuation_Module/Design_Spec.md` | AM support network remains incompletely frozen: `ACTUATE_REQUEST` local biasing is referenced but not fully BOM-defined, and `BOOT0` / `NRST` support treatment remains deferred. | Reset / boot-entry behavior must be deterministic before schematic capture and BOM freeze. | Resolve during schematic capture and add the exact support network components to the active AM spec/BOM once frozen. | deferred schematic capture |
| medium | `design/Electronics/Settings_Board/Design_Spec.md` | Settings Board LED topology remains internally unresolved between the connector/power description and the LED-drive description. | LED biasing topology affects current-setting resistor values and whether the documented control scheme is electrically valid. | Freeze the actual LED topology during schematic capture, then align the spec and BOM to that topology. | deferred schematic capture |
| medium | `design/Electronics/Rotor/Design_Spec.md` | Rotor FDC2114 resonant front-end / unused-channel support definition remains explicitly deferred. | The sensor IC cannot be considered fully BOM-complete until the resonant front-end and unused-channel treatment are frozen. | Complete the deferred schematic-capture definition and add the finalized support parts to the Rotor BOM. | deferred schematic capture |
| low | `design/Electronics/PM/Design_Spec.md`; `design/Electronics/Stator/Design_Spec.md`; `design/Electronics/Consolidated_BOM.md` | INA219 input RC filter exact sourced parts remain unresolved for PM and Stator. | The measurement front-end support network is called for at the spec level but not yet fully sourced into the BOM set. | Freeze the exact filter population and add the sourced resistor/capacitor entries to the board BOMs and consolidated BOM. | deferred schematic capture |
| low | `design/Electronics/Rotor/Design_Spec.md` | Rotor local I2C pull-ups remain intentionally placeholder / owner-selected. | The bus support network is not fully sourceable until the placeholder parts are selected. | User/owner to choose the exact sourced pull-up parts, then update the Rotor BOM. | needs user selection |
| low | `design/Electronics/Rotor/Design_Spec.md` | Rotor 1uF FDC2114 bypass / reservoir capacitor placeholders remain intentionally owner-selected. | The IC support network is not fully sourceable until the placeholder capacitor parts are selected. | User/owner to choose the exact sourced capacitor parts, then update the Rotor BOM. | needs user selection |
| low | `design/Electronics/Extension/Design_Spec.md` | Extension TVS / ESD protection exact device count, protected nets, footprint, and MPN remain intentionally owner-selected. | Protection intent is documented, but procurement and final schematic capture cannot fully freeze until the exact device choice is made. | User/owner to choose the exact protection implementation and update the Extension BOM/spec accordingly. | needs user selection |

#### Unsourced New Parts Requiring User Selection

No newly identified unsourced parts requiring user selection were found in Pass 5.

Previously known owner-selection items remain unchanged:

- Rotor local I2C pull-up parts
- Rotor FDC2114 1uF bypass / reservoir capacitor parts
- Extension TVS / ESD protection device selection

#### Pass Result

#### Not clean

Pass 5 found one new evidence-backed issue: a remaining connector-mapping contradiction in
`design/Electronics/Encoder/Board_Layout.md §5.2` where the TDO routing note still references
`J2 pin 13` instead of the corrected `J2 pin 14`.

Per the clean-pass definition:

- **No new connector-mapping contradictions** → **not met**
- **No new evidence-backed BOM/spec omissions for already-frozen circuitry** → met
- Previously documented deferred / user-selection items remain, but only as unchanged known
  unresolved items

### Pass 5 — Fix

#### Files changed

- `design/Electronics/Encoder/Board_Layout.md`
- `.copilot/review-report.md`

#### Exact fix applied

- Updated `design/Electronics/Encoder/Board_Layout.md §5.2` so the routing note now reads
  `U1 TDO -> R6 -> J2 pin 14` instead of `J2 pin 13`.
- **Rationale:** `Encoder/Board_Layout.md §3` and `§4.1` already define `J2 pin 13` as `GND` and
  `J2 pin 14` as `TDO`; this removes the stale board-layout contradiction and closes the Pass 5
  review finding for the Encoder JTAG TDO connector mapping.

#### Unresolved findings left unchanged

- AM `ACTUATE_REQUEST` / `BOOT0` / `NRST` support network
- Settings Board LED topology
- Rotor FDC2114 resonant front-end / unused-channel support definition
- PM / Stator INA219 input RC filter exact sourced parts
- Rotor local I2C pull-up owner-selected parts
- Rotor 1uF FDC2114 bypass / reservoir capacitor owner-selected parts
- Extension TVS / ESD exact device count, protected nets, footprint, and MPN selection

- **Commits:** no commits were made.

### Pass 6 — Review

#### Scope summary

Re-reviewed `design/Electronics/Consolidated_BOM.md`, all active
`design/Electronics/*/Design_Spec.md` files, related logical signal-map / connector-contract sections in
`Board_Layout.md`, `design/Software/Actuation_Module/Design_Spec.md`, and the current report after Fix
Pass 5. Focus remained limited to BOM completeness for active circuit-support components and connector-map
consistency. Physical PCB placement/routing was not reviewed.

#### Remaining Findings — New in Pass 6

| Severity | Files | Issue | Why it matters | Recommended fix | Status |
| :--- | :--- | :--- | :--- | :--- | :--- |
| medium | `design/Electronics/Encoder/Design_Spec.md`; cross-check: `design/Electronics/Encoder/Board_Layout.md`, `design/Electronics/Stator/Board_Layout.md` | `Encoder/Design_Spec.md` still contains stale `TDO` connector references to `J2 pin 13`: `§5 JTAG Chain Integrity` says `R6` is before `J2 pin 13`, and the BOM row for `R6` repeats `U1 TDO -> J2 pin 13`. The authoritative active connector map still places `TDO` on `J2 pin 14` and `pin 13` is `GND`. | This remains a real connector-mapping contradiction in an active design spec. If schematic capture or review follows the stale spec/BOM text instead of the corrected board-layout contract, `TDO` can be routed onto a ground-assigned pin. | Update the stale `Encoder/Design_Spec.md` `R6` references to `J2 pin 14` so the spec, BOM row, and board-layout pin tables all agree. | pending fix pass |
| medium | `design/Electronics/Power_Module/Design_Spec.md`, `design/Electronics/Consolidated_BOM.md`; evidence: `design/Datasheets/TI-sn74lvc1g175-datasheet.md`, `design/Datasheets/TI-sn74lvc1g08-datasheet.md` | The PM BOM explicitly captures local `100 nF` bypass caps for `U3/U4/U5/U6a/U6b/U6c/U8/U9/U10/U11/U12/U13/U14/U15/U16`, but the active SW2 support-logic ICs `U17/U18/U19` still have no documented local bypass population. The in-repo TI logic datasheets for `U18` and `U19` call for a local `0.1 µF` bypass capacitor per `VCC` terminal. | This leaves the PM SW2 hardware state / shutdown-indicator logic cluster not fully support-part-complete in the procurement-facing BOM. Local rail disturbance on that small logic chain can create avoidable bring-up or shutdown-indication instability. | Add explicit local `100 nF` bypass rows / refdes for the `U17/U18/U19` logic cluster using the already-locked common 0402 decoupling capacitor, then roll the PM and system totals forward in `Consolidated_BOM.md`. | pending fix pass |

#### Remaining Findings — Unchanged Known Unresolved Items

These items were already known before Pass 6 and remain unresolved; no new repository evidence in this
pass changed their status.

| Severity | Files | Issue | Why it matters | Recommended fix | Status |
| :--- | :--- | :--- | :--- | :--- | :--- |
| medium | `design/Electronics/Actuation_Module/Design_Spec.md`; `design/Software/Actuation_Module/Design_Spec.md` | AM support network for `ACTUATE_REQUEST` / `BOOT0` / `NRST` remains incompletely frozen. | Boot / reset behavior and request-input determinism still depend on later schematic capture closure. | Freeze the exact support network and add the corresponding BOM rows/refdes once approved. | deferred schematic capture |
| medium | `design/Electronics/Settings_Board/Design_Spec.md` | Settings Board LED topology remains underdefined between the documented MCP23017 anode-driving description and the common-anode `5V_MAIN` LED implementation. | LED current path and validity of the indicator-drive scheme remain unresolved. | Freeze one electrical topology and align the spec/BOM to it during later schematic capture. | deferred schematic capture |
| medium | `design/Electronics/Rotor/Design_Spec.md` | Rotor FDC2114 resonant front-end / unused-channel support definition remains explicitly deferred. | The sensing chain is still not fully circuit-complete at the channel front-end level. | Complete the deferred support-network definition and add the finalized support parts to the Rotor BOM. | deferred schematic capture |
| low | `design/Electronics/Power_Module/Design_Spec.md`; `design/Electronics/Stator/Design_Spec.md`; `design/Electronics/Consolidated_BOM.md` | PM / Stator INA219 input RC filter exact sourced parts remain unresolved. | The telemetry front-end support networks are still not procurement-closed. | Add the user-approved sourced resistor/capacitor filter population and roll those parts into the board and consolidated BOMs. | needs user selection |
| low | `design/Electronics/Rotor/Design_Spec.md`; `design/Electronics/Consolidated_BOM.md` | Rotor local I2C pull-up placeholders remain intentionally owner-selected. | The local sensor bus support network is documented but not fully sourceable. | User/owner to select the exact pull-up parts, then update the Rotor and consolidated BOMs. | needs user selection |
| low | `design/Electronics/Rotor/Design_Spec.md`; `design/Electronics/Consolidated_BOM.md` | Rotor `1 µF` FDC2114 bypass / reservoir capacitor placeholders remain intentionally owner-selected. | The documented FDC supply-support network is not yet fully sourceable. | User/owner to select the exact capacitor parts, then update the Rotor and consolidated BOMs. | needs user selection |
| low | `design/Electronics/Extension/Design_Spec.md`; `design/Electronics/Consolidated_BOM.md` | Extension TVS / ESD exact device count, protected nets, footprint, and MPN remain intentionally owner-selected. | Protection intent is documented, but final procurement / schematic closure is still open. | User/owner to choose the exact protection implementation and update the Extension BOM/spec accordingly. | needs user selection |

#### Unsourced New Parts Requiring User Selection

No newly identified unsourced parts requiring user selection were found in Pass 6.

#### Pass Result

#### Not clean

Pass 6 found:

- one new connector-mapping contradiction still present in an active design spec
- one new evidence-backed support-part omission for already-frozen PM circuitry

Per the clean-pass definition:

- **No new connector-mapping contradictions** → **not met**
- **No new evidence-backed BOM/spec omissions for already-frozen circuitry** → **not met**
- Previously documented deferred / user-selection items remain, but only as unchanged known unresolved
  items

### Pass 6 — Fix

#### Files changed

- `design/Electronics/Encoder/Design_Spec.md`
- `design/Electronics/Power_Module/Design_Spec.md`
- `design/Electronics/Consolidated_BOM.md`
- `.copilot/review-report.md`

#### Exact fixes applied

- Closed Pass 6 finding 1 in `design/Electronics/Encoder/Design_Spec.md` by correcting both stale `R6`
  references from `J2 pin 13` to `J2 pin 14` in `§5 JTAG Chain Integrity` and the local BOM row. This
  aligns the Encoder design spec with the active Encoder/Stator connector contract where `J2 pin 14` is
  `TDO` and `J2 pin 13` is `GND`.
- Closed Pass 6 finding 2 in `design/Electronics/Power_Module/Design_Spec.md` by explicitly adding
  local `100nF` VCC bypass capture for the PM SW2 logic cluster:
  - `C44` for `U17`
  - `C45` for `U18`
  - `C46` for `U19`
  using the already-locked Samsung `CL05B104KB5NNNC` / JLC `C1525` common decoupler part.
- Strengthened the same PM capture by adding the corresponding `VCC bypass` references into the `U17`,
  `U18`, and `U19` BOM descriptions and by updating the PM capacitor-family bookkeeping note from
  `C21–C42` / `C24–C39` to `C21–C46` / `C24–C39 and C43–C46`.
- Aligned `design/Electronics/Consolidated_BOM.md` with those PM changes by updating the common `0.1 µF`
  0402 decoupling row from `PM 17 / System 390` to `PM 20 / System 393`, and by expanding the PM
  detailed capacitor capture from `C24-C39, C43` to `C24-C39, C43-C46`.

#### Unresolved findings left unchanged

- `design/Electronics/Actuation_Module/Design_Spec.md`; `design/Software/Actuation_Module/Design_Spec.md` — AM support network for `ACTUATE_REQUEST` / `BOOT0` / `NRST` still deferred to schematic
capture.
- `design/Electronics/Settings_Board/Design_Spec.md` — Settings Board LED topology still unresolved.
- `design/Electronics/Rotor/Design_Spec.md` — Rotor FDC2114 resonant front-end / unused-channel support still deferred.
- `design/Electronics/Power_Module/Design_Spec.md`; `design/Electronics/Stator/Design_Spec.md`; `design/Electronics/Consolidated_BOM.md` — PM / Stator INA219 input RC filter exact sourced parts still
unresolved.
- `design/Electronics/Rotor/Design_Spec.md`; `design/Electronics/Consolidated_BOM.md` — Rotor local I2C pull-up placeholders still owner-selected.
- `design/Electronics/Rotor/Design_Spec.md`; `design/Electronics/Consolidated_BOM.md` — Rotor `1 µF` FDC2114 bypass / reservoir capacitor placeholders still owner-selected.
- `design/Electronics/Extension/Design_Spec.md`; `design/Electronics/Consolidated_BOM.md` — Extension TVS / ESD implementation still owner-selected.

**Note:** No commits were made.

### Pass 7 — Review

#### Scope summary

Re-reviewed `design/Electronics/Consolidated_BOM.md`, all active
`design/Electronics/*/Design_Spec.md` files, related logical signal-map / connector-contract sections in
`Board_Layout.md`, `design/Software/Actuation_Module/Design_Spec.md`, and the current report after Fix
Pass 6. Focus remained limited to BOM completeness for active circuit-support components and connector-map
consistency. Physical PCB placement/routing was not reviewed.

#### Remaining Findings — New in Pass 7

| Severity | Files | Issue | Why it matters | Recommended fix | Status |
| :--- | :--- | :--- | :--- | :--- | :--- |
| major | `design/Electronics/Settings_Board/Design_Spec.md`; `design/Electronics/Settings_Board/Board_Layout.md`; `design/Electronics/Consolidated_BOM.md` | The Settings Board switch population and MCP23017 GPIO allocation are still contradicted across active docs. `Design_Spec.md` freezes a 10-switch implementation (`SW1-SW10`, `R1-R10`) with `CFG_ROUTE[3:0]` on `GPA[3:0]`, `CFG_REFMAP[5:0]` on `GPB[5:0]`, and `GPA4` spare. `Board_Layout.md` still describes 12 toggles with `SW_B1_EN` / `SW_B2_EN` bank-enable functions and uses more GPIOs. `Consolidated_BOM.md` is internally split: 12 toggle switches are counted, but only 10 pull-down resistors are captured. | This is a real procurement and schematic-capture trap. Two extra switches can be ordered without matching support resistors or a consistent frozen GPIO assignment, and `GPA4` cannot be both spare and an active switch input. | Choose one Settings Board switch architecture, then align `Design_Spec.md`, `Board_Layout.md`, and `Consolidated_BOM.md` to the same switch count, GPIO map, and pull-down population in the next fix pass. | pending fix pass |

#### Remaining Findings — Unchanged Known Unresolved Items

These items were already known before Pass 7 and remain unresolved; no new repository evidence in this
pass changed their status.

| Severity | Files | Issue | Why it matters | Recommended fix | Status |
| :--- | :--- | :--- | :--- | :--- | :--- |
| medium | `design/Electronics/Actuation_Module/Design_Spec.md`; `design/Software/Actuation_Module/Design_Spec.md` | AM support network for `ACTUATE_REQUEST` / `BOOT0` / `NRST` remains incompletely frozen. | Boot / reset behavior and request-input determinism still depend on later schematic capture closure. | Freeze the exact support network and add the corresponding BOM rows/refdes once approved. | deferred schematic capture |
| medium | `design/Electronics/Settings_Board/Design_Spec.md` | Settings Board LED topology remains underdefined between the documented MCP23017 anode-driving description and the common-anode `5V_MAIN` LED implementation. | LED current path and validity of the indicator-drive scheme remain unresolved. | Freeze one electrical topology and align the spec/BOM to it during later schematic capture. | deferred schematic capture |
| medium | `design/Electronics/Rotor/Design_Spec.md` | Rotor FDC2114 resonant front-end / unused-channel support definition remains explicitly deferred. | The sensing chain is still not fully circuit-complete at the channel front-end level. | Complete the deferred support-network definition and add the finalized support parts to the Rotor BOM. | deferred schematic capture |
| low | `design/Electronics/Power_Module/Design_Spec.md`; `design/Electronics/Stator/Design_Spec.md`; `design/Electronics/Consolidated_BOM.md` | PM / Stator INA219 input RC filter exact sourced parts remain unresolved. | The telemetry front-end support networks are still not procurement-closed. | Add the user-approved sourced resistor/capacitor filter population and roll those parts into the board and consolidated BOMs. | needs user selection |
| low | `design/Electronics/Rotor/Design_Spec.md`; `design/Electronics/Consolidated_BOM.md` | Rotor local I2C pull-up placeholders remain intentionally owner-selected. | The local sensor bus support network is documented but not fully sourceable. | User/owner to select the exact pull-up parts, then update the Rotor and consolidated BOMs. | needs user selection |
| low | `design/Electronics/Rotor/Design_Spec.md`; `design/Electronics/Consolidated_BOM.md` | Rotor `1 µF` FDC2114 bypass / reservoir capacitor placeholders remain intentionally owner-selected. | The documented FDC supply-support network is not yet fully sourceable. | User/owner to select the exact capacitor parts, then update the Rotor and consolidated BOMs. | needs user selection |
| low | `design/Electronics/Extension/Design_Spec.md`; `design/Electronics/Consolidated_BOM.md` | Extension TVS / ESD exact device count, protected nets, footprint, and MPN remain intentionally owner-selected. | Protection intent is documented, but final procurement / schematic closure is still open. | User/owner to choose the exact protection implementation and update the Extension BOM/spec accordingly. | needs user selection |

#### Connector Consistency Check

- No new connector-mapping contradictions were found in Pass 7.
- The previously corrected Encoder `J2 pin 14` `TDO` mapping remains aligned across the active
  Encoder/Stator connector contract and the Encoder design spec.
- The reviewed Settings Board power / I2C connector contract remains consistent where referenced; the new
  Pass 7 issue is the switch/GPIO definition mismatch, not a connector pinout mismatch.

#### Unsourced New Parts Requiring User Selection

No newly identified unsourced parts requiring user selection were found in Pass 7.

Previously known unresolved user-selection items remain unchanged:

- PM / Stator INA219 input RC filter exact sourced parts
- Rotor local I2C pull-up exact sourced parts
- Rotor `1 µF` FDC2114 bypass / reservoir capacitor exact sourced parts
- Extension TVS / ESD exact implementation

#### Pass Result

#### Not clean

Pass 7 found:

- no new connector-mapping contradictions
- one new evidence-backed BOM/spec inconsistency for already-frozen Settings Board circuitry

Per the clean-pass definition:

- **No new connector-mapping contradictions** → met
- **No new evidence-backed BOM/spec omissions for already-frozen circuitry** → **not met**
- Previously documented deferred / user-selection items remain, but only as unchanged known unresolved
  items

### Pass 7 — Fix

#### Files changed

- `design/Electronics/Settings_Board/Design_Spec.md`
- `design/Electronics/Settings_Board/Board_Layout.md`
- `design/Electronics/Consolidated_BOM.md`

#### Exact fix applied

- Closed the Pass 7 Settings Board switch/GPIO-definition mismatch by aligning all three target files to the already-frozen 10-toggle architecture used by the active Settings/Stator design specs:
  - `CFG_ROUTE[3:0]` on `U1.GPA[3:0]`
  - `CFG_REFMAP[5:0]` on `U1.GPB[5:0]`
  - `U1.GPA[4:7]` spare, `U1.GPB[6]` spare
  - `CFG_APPLY_N` on `U1.GPB[7]`
- `design/Electronics/Settings_Board/Board_Layout.md` was updated from the obsolete 12-toggle / bank-enable-switch description to the approved 10-toggle mapping, including the top-level overview, U1
GPIO table, U2/U3 source-status LED naming, and the switch/LED mapping table.
- `design/Electronics/Consolidated_BOM.md` was updated so the Settings Board toggle-switch population now matches the frozen design (`10`, not `12`), and the descriptive summary now states the
correct U1 GPIO allocation instead of "all 12 switch states".
- Directly dependent bookkeeping wording was also aligned where this finding touched it: `CFG_APPLY_N` naming was normalized in the affected Settings Board/BOM rows, and the 12 LED resistor rows were
relabeled as per-indicator rather than per-switch because the board has 10 toggles but 12 indicators.
- `design/Electronics/Settings_Board/Design_Spec.md` already held the approved 10-toggle GPIO allocation; it was only adjusted for dependent wording/bookkeeping consistency (`SW5-SW10` naming for
`CFG_REFMAP[5:0]`, per-indicator LED wording, and `CFG_APPLY_N` wording in the affected summary rows).

#### Rationale / finding closed

- This closes Pass 7's major finding that the Settings Board switch population, pull-down population, and MCP23017 GPIO allocation were contradicted across `Design_Spec.md`, `Board_Layout.md`, and
`Consolidated_BOM.md`.

#### Unresolved findings left unchanged

- Settings Board LED topology remains deferred schematic-capture work and was not changed in this fix.
- All previously listed non-Settings-Board unresolved items remain unchanged.

**Note:** No commits were made.

### Pass 8 — Review

#### Scope summary

Re-reviewed `design/Electronics/Consolidated_BOM.md`, all active
`design/Electronics/*/Design_Spec.md` files, related connector-contract / logical signal-map sections in
`Board_Layout.md`, `design/Software/Actuation_Module/Design_Spec.md`, and the current report after Fix
Pass 7. Focus remained limited to BOM completeness for active circuit-support parts and connector-mapping
consistency. Physical PCB placement/routing was not reviewed.

#### Remaining Findings — New in Pass 8

| Severity | Files | Issue | Why it matters | Recommended fix | Status |
| :--- | :--- | :--- | :--- | :--- | :--- |
| medium | `design/Electronics/Stator/Design_Spec.md`; cross-check: `design/Electronics/Consolidated_BOM.md` | `Stator/Design_Spec.md §8 Thermal & ESD` still states `TVS diode protection on external-facing signal lines`, but the Stator BOM has no TVS / ESD device row and the consolidated BOM carries no Stator-side TVS population. | This leaves the active Stator docs internally contradictory at an exposed cable/interface boundary: either protection is required but not BOM-captured, or the ESD sentence is stale and can mislead later schematic capture and procurement review. | In the next fix pass, resolve the contradiction explicitly: either add owner-selected Stator TVS / ESD placeholder rows with protected-net / footprint intent and align the consolidated BOM, or remove / qualify the stale ESD sentence if no local protection is part of the approved design. | pending fix pass |

#### Remaining Findings — Unchanged Known Unresolved Items

These items were already known before Pass 8 and remain unresolved; no new repo evidence in this pass
changed their status.

| Severity | Files | Issue | Why it matters | Recommended fix | Status |
| :--- | :--- | :--- | :--- | :--- | :--- |
| medium | `design/Electronics/Actuation_Module/Design_Spec.md`; `design/Software/Actuation_Module/Design_Spec.md` | AM support network for `ACTUATE_REQUEST` / `BOOT0` / `NRST` remains incompletely frozen. | Boot / reset behavior and request-input determinism still depend on later schematic-capture closure. | Freeze the exact support network and add the corresponding BOM rows / refdes once approved. | deferred schematic capture |
| medium | `design/Electronics/Settings_Board/Design_Spec.md`; `design/Electronics/Settings_Board/Board_Layout.md` | Settings Board LED topology remains underdefined between the documented MCP23017 anode-driving description and the common-anode `5V_MAIN` LED implementation. | LED current path and validity of the indicator-drive scheme remain unresolved. | Freeze one electrical topology and align the spec / BOM to it during later schematic capture. | deferred schematic capture |
| medium | `design/Electronics/Rotor/Design_Spec.md` | Rotor FDC2114 resonant front-end / unused-channel support definition remains explicitly deferred. | The sensing chain is still not fully circuit-complete at the channel front-end level. | Complete the deferred support-network definition and add the finalized support parts to the Rotor BOM. | deferred schematic capture |
| low | `design/Electronics/Power_Module/Design_Spec.md`; `design/Electronics/Stator/Design_Spec.md`; `design/Electronics/Consolidated_BOM.md` | PM / Stator INA219 input RC filter exact sourced parts remain unresolved. | The telemetry front-end support networks are still not procurement-closed. | Add the user-approved sourced resistor/capacitor filter population and roll those parts into the board and consolidated BOMs. | needs user selection |
| low | `design/Electronics/Rotor/Design_Spec.md`; `design/Electronics/Consolidated_BOM.md` | Rotor local I2C pull-up placeholders remain intentionally owner-selected. | The local sensor bus support network is documented but not fully sourceable. | User/owner to select the exact pull-up parts, then update the Rotor and consolidated BOMs. | needs user selection |
| low | `design/Electronics/Rotor/Design_Spec.md`; `design/Electronics/Consolidated_BOM.md` | Rotor `1 µF` FDC2114 bypass / reservoir capacitor placeholders remain intentionally owner-selected. | The documented FDC supply-support network is not yet fully sourceable. | User/owner to select the exact capacitor parts, then update the Rotor and consolidated BOMs. | needs user selection |
| low | `design/Electronics/Extension/Design_Spec.md`; `design/Electronics/Consolidated_BOM.md` | Extension TVS / ESD exact device count, protected nets, footprint, and MPN remain intentionally owner-selected. | Protection intent is documented, but final procurement / schematic closure is still open. | User/owner to choose the exact protection implementation and update the Extension BOM/spec accordingly. | needs user selection |

#### Connector Consistency Check

| Severity | Files | Issue | Why it matters | Recommended fix | Status |
| :--- | :--- | :--- | :--- | :--- | :--- |
| info | `design/Electronics/Stator/Board_Layout.md`; `design/Electronics/Extension/Design_Spec.md`; `design/Electronics/Reflector/Design_Spec.md`; `design/Electronics/Rotor/Design_Spec.md`; `design/Electronics/Settings_Board/Design_Spec.md`; `design/Electronics/Actuation_Module/Design_Spec.md`; `design/Software/Actuation_Module/Design_Spec.md` | No new connector-mapping contradictions were found in Pass 8. The reviewed Reflector / Extension `J10` contract, Rotor stack interfaces, Settings `J1` ↔ Stator `J13` harness, and AM host/module pin contracts remain aligned at the document level. | Confirms this pass did not uncover a new documented miswire trap. | None. | clean |

#### Unsourced New Parts Requiring User Selection

- Newly identified in Pass 8:
  - If `design/Electronics/Stator/Design_Spec.md §8` is intended to remain true, the missing Stator-board
    TVS / ESD protection device population on external-facing signal lines will require explicit user
    selection of protected nets, device count, footprint, and MPN before BOM closure.

- Previously known unresolved user-selection items remain unchanged:
  - PM / Stator INA219 input RC filter exact sourced parts
  - Rotor local I2C pull-up exact sourced parts
  - Rotor `1 µF` FDC2114 bypass / reservoir capacitor exact sourced parts
  - Extension TVS / ESD exact implementation

#### Pass Result

#### Not clean

Pass 8 found no new connector-mapping contradictions, but it did find one new evidence-backed
spec/BOM contradiction on Stator interface protection. Therefore the clean-pass definition is not met.

### Pass 8 — Fix

#### Files changed

- `design/Electronics/Stator/Design_Spec.md`
- `design/Electronics/Consolidated_BOM.md`

#### Exact fix applied

- Closed the Pass 8 Stator TVS / ESD spec-to-BOM contradiction by updating `Stator/Design_Spec.md §8`
  to state that local protection is required specifically at the documented exposed Stator signal-line
  boundaries (`J10`, `J12`, `J13`) while keeping the exact protected nets, device count, working
  voltage, package, and MPN explicitly owner-selected.
- Added a matching unsourced placeholder BOM row to `Stator/Design_Spec.md §9`:
  `D1 (owner-selected) | External signal-line TVS / ESD protection required by §8 (`J10`,`J12`,`J13`) | ...`
- Added the dependent `design/Electronics/Consolidated_BOM.md` usage-summary placeholder row:
  `UNSOURCED — Stator external signal-line TVS / ESD protection required by Stator/Design_Spec.md §8 ...`
  so the consolidated BOM now captures the active Stator protection requirement instead of silently
  omitting it.

#### Rationale / finding closed

- This closes Pass 8 finding `medium` at `design/Electronics/Stator/Design_Spec.md`; cross-check:
  `design/Electronics/Consolidated_BOM.md` about Stator TVS / ESD protection being claimed in the
  spec but absent from both the Stator BOM and consolidated BOM.

#### Unresolved findings left unchanged

- Exact Stator TVS / ESD implementation details remain intentionally owner-selected (`protected nets`,
  `device count`, `working voltage`, `package`, `MPN`); this is now documented as an explicit
  unsourced placeholder rather than an untracked BOM gap.
- All other previously listed unresolved findings remain unchanged.

**Note:** No commits were made.

### Pass 9 — Review

#### Scope summary

Re-reviewed `design/Electronics/Consolidated_BOM.md`, all active
`design/Electronics/*/Design_Spec.md` files, related connector-contract / logical signal-map sections in
`Board_Layout.md`, `design/Software/Actuation_Module/Design_Spec.md`, and the current report after Fix
Pass 8. Focus remained limited to BOM completeness for active circuit-support parts and connector-mapping
consistency. Physical PCB placement/routing was not reviewed.

#### Remaining Findings — New in Pass 9

| Severity | Files | Issue | Why it matters | Recommended fix | Status |
| :--- | :--- | :--- | :--- | :--- | :--- |
| medium | `design/Electronics/Extension/Design_Spec.md`; `design/Electronics/Consolidated_BOM.md` | The Extension board spec/BOM now captures owner-selected TVS / ESD protection (`D1`), but the procurement-facing consolidated BOM still has no matching Extension placeholder row. | A required exposed-interface protection implementation can still disappear from consolidated purchasing review even though the board spec now requires it. | Add an unsourced Extension TVS / ESD placeholder row to `Consolidated_BOM.md`, aligned to the Extension spec, while keeping protected nets, device count, footprint, and MPN owner-selected. | pending fix pass |
| medium | `design/Electronics/Stator/Board_Layout.md`; cross-check: `design/Electronics/Stator/Design_Spec.md`, `design/Electronics/Extension/Design_Spec.md`, `design/Electronics/Reflector/Board_Layout.md` | The Stator-owned `J10` connector table still labels pin 2 `SYS_RESET_N` as `CTRL->Ext`, while the active Stator design uses a Stator-managed `SYS_RESET_N` broadcast on that boundary. Pin number is consistent, but source/direction ownership is not. | The owner connector contract is what later schematic capture and harness/test docs are likely to follow. Wrong source/direction wording can mis-state reset ownership even without changing pin allocation. | Update the `J10` pin-2 direction/note in `Stator/Board_Layout.md` to reflect Stator-originated active-low reset broadcast. | pending fix pass |

#### Remaining Findings — Unchanged Known Unresolved Items

These items were already known before Pass 9 and remain unresolved; no new repository evidence in this
pass changed their status.

| Severity | Files | Issue | Why it matters | Recommended fix | Status |
| :--- | :--- | :--- | :--- | :--- | :--- |
| medium | `design/Electronics/Actuation_Module/Design_Spec.md`; `design/Software/Actuation_Module/Design_Spec.md` | AM support network for `ACTUATE_REQUEST` / `BOOT0` / `NRST` remains incompletely frozen. | Boot / reset behavior and request-input determinism still depend on later schematic-capture closure. | Freeze the exact support network and add the corresponding BOM rows / refdes once approved. | deferred schematic capture |
| medium | `design/Electronics/Settings_Board/Design_Spec.md`; `design/Electronics/Settings_Board/Board_Layout.md` | Settings Board LED topology remains underdefined between the documented MCP23017 anode-driving description and the common-anode `5V_MAIN` LED implementation. | LED current path and validity of the indicator-drive scheme remain unresolved. | Freeze one electrical topology and align the spec / BOM to it during later schematic capture. | deferred schematic capture |
| medium | `design/Electronics/Rotor/Design_Spec.md` | Rotor FDC2114 resonant front-end / unused-channel support definition remains explicitly deferred. | The sensing chain is still not fully circuit-complete at the channel front-end level. | Complete the deferred support-network definition and add the finalized support parts to the Rotor BOM. | deferred schematic capture |
| low | `design/Electronics/Power_Module/Design_Spec.md`; `design/Electronics/Stator/Design_Spec.md`; `design/Electronics/Consolidated_BOM.md` | PM / Stator INA219 input RC filter exact sourced parts remain unresolved. | The telemetry front-end support networks are still not procurement-closed. | Add the user-approved sourced resistor/capacitor filter population and roll those parts into the board and consolidated BOMs. | needs user selection |
| low | `design/Electronics/Rotor/Design_Spec.md`; `design/Electronics/Consolidated_BOM.md` | Rotor local I2C pull-up placeholders remain intentionally owner-selected. | The local sensor bus support network is documented but not fully sourceable. | User/owner to select the exact pull-up parts, then update the Rotor and consolidated BOMs. | needs user selection |
| low | `design/Electronics/Rotor/Design_Spec.md`; `design/Electronics/Consolidated_BOM.md` | Rotor `1 µF` FDC2114 bypass / reservoir capacitor placeholders remain intentionally owner-selected. | The documented FDC supply-support network is not yet fully sourceable. | User/owner to select the exact capacitor parts, then update the Rotor and consolidated BOMs. | needs user selection |
| low | `design/Electronics/Extension/Design_Spec.md`; `design/Electronics/Consolidated_BOM.md` | Extension TVS / ESD exact device count, protected nets, footprint, and MPN remain intentionally owner-selected. The new Pass 9 finding above is about missing consolidated placeholder capture, not about changing this owner-selection status. | Protection intent is documented, but final implementation details are still open. | User/owner to choose the exact protection implementation after the consolidated placeholder is added. | needs user selection |
| low | `design/Electronics/Stator/Design_Spec.md`; `design/Electronics/Consolidated_BOM.md` | Stator TVS / ESD exact device count, protected nets, footprint, and MPN remain intentionally owner-selected, but placeholder capture is now present. | Protection intent is documented, but final implementation details are still open. | User/owner to choose the exact protection implementation. | needs user selection |

#### Connector Consistency Check

| Severity | Files | Issue | Why it matters | Recommended fix | Status |
| :--- | :--- | :--- | :--- | :--- | :--- |
| info | `design/Electronics/Stator/Board_Layout.md`; `design/Electronics/Extension/Board_Layout.md`; `design/Electronics/Reflector/Board_Layout.md`; `design/Electronics/Settings_Board/Design_Spec.md`; `design/Electronics/Actuation_Module/Design_Spec.md`; `design/Software/Actuation_Module/Design_Spec.md` | No new connector pin-number contradictions were found in Pass 9. Reflector / Extension `J10` pin allocation, Settings `J1` ↔ Stator `J13`, and AM host/module dock pinouts remain aligned. The only connector issue found this pass is the Stator `J10` `SYS_RESET_N` source/direction wording above. | Confirms this pass did not uncover a new documented miswire at the pin-number level. | None. | clean |

#### Unsourced New Parts Requiring User Selection

- None newly identified in Pass 9.
- Existing owner-selected items remain unchanged:
  - PM / Stator INA219 input RC filter exact sourced parts
  - Rotor local I2C pull-up exact sourced parts
  - Rotor `1 µF` FDC2114 bypass / reservoir capacitor exact sourced parts
  - Extension TVS / ESD exact implementation
  - Stator TVS / ESD exact implementation

### Pass 15 — Fix

- **Status:** fix applied

#### Files changed

- `design/Electronics/Consolidated_BOM.md`
- `.copilot/review-report.md`

#### Fixes applied

- **Closed Pass 15 finding 1 — `10 kΩ 0603` consolidated system total arithmetic drift**
  - Corrected the common `10 kΩ 1% 0603` fitted-resistor summary row system total from `41` to `38`.
  - The per-board columns were already correct at `PM 6`, `CTL 5`, `STA 16`, and `SBD 11`; only the
    aggregate total was wrong.

- **Closed Pass 15 finding 2 — Settings Board LED series resistors missing from top consolidated summary**
  - Added a dedicated top-summary row for the Settings Board `12 × 150 Ω 1% 0603` red LED
    current-limit resistors (`ERJ-3EKF1500V / C400650`).
  - Added a dedicated top-summary row for the Settings Board `24 × 100 Ω 1% 0603` green/blue LED
    current-limit resistors (`ERJ-3EKF1000V / C193336`).
  - This leaves the existing `100 Ω 0603 differential termination` row intact, while making the
    Settings Board indicator resistor population visible in the procurement-facing consolidated summary.

#### Unresolved / left unchanged

- AM `ACTUATE_REQUEST` / `BOOT0` / `NRST` support network remains deferred schematic-capture work.
- Settings Board LED topology remains deferred schematic-capture work.
- Rotor FDC2114 resonant front-end / unused-channel support remains owner-selected / unresolved.
- PM / Stator INA219 input RC filter exact sourced parts remain owner-selected / unresolved.
- Rotor I2C pull-up and `1 µF` FDC2114 bypass exact sourced parts remain owner-selected / unresolved.
- Extension and Stator TVS/ESD exact implementation details remain owner-selected / unresolved.

- **Commits:** no commits were made.

#### Pass Result

#### Not clean

Pass 9 found no new connector pin-number contradictions, but it still found one new evidence-backed
consolidated-BOM omission and one Stator-owned connector source/direction inconsistency. The clean-pass
definition is therefore not met.

### Pass 9 — Fix

#### Files changed

- `design/Electronics/Consolidated_BOM.md`
- `design/Electronics/Stator/Board_Layout.md`
- `.copilot/review-report.md`

#### Exact fixes applied

- Closed the Pass 9 Extension protection bookkeeping gap by adding the missing consolidated placeholder
  row to `design/Electronics/Consolidated_BOM.md`:
  `UNSOURCED — Extension exposed signal-line TVS / ESD protection required by Extension/Design_Spec.md §5 ...`
  This aligns the procurement-facing consolidated BOM to the already-documented Extension owner-selected
  TVS / ESD requirement without inventing a part, protected-net list, footprint, or MPN.
- Closed the Pass 9 Stator `J10` ownership wording inconsistency by updating
  `design/Electronics/Stator/Board_Layout.md` pin 2 from `CTRL->Ext` to
  `Stator -> Reflector / Ext`, and by making the note explicit that `SYS_RESET_N` is the active-low
  CPLD reset broadcast from the Stator. This preserves the existing pin assignment and electrical intent
  while aligning the owner connector contract to the active architecture.

#### Rationale / findings closed

- This closes the Pass 9 `medium` finding at
  `design/Electronics/Extension/Design_Spec.md`; cross-check:
  `design/Electronics/Consolidated_BOM.md` about the Extension TVS / ESD requirement being present in
  the board spec/BOM but absent from the consolidated BOM.
- This closes the Pass 9 `medium` finding at `design/Electronics/Stator/Board_Layout.md`; cross-check:
  `design/Electronics/Stator/Design_Spec.md`, `design/Electronics/Extension/Design_Spec.md`,
  `design/Electronics/Reflector/Board_Layout.md` about `J10` pin 2 `SYS_RESET_N` source/direction
  wording still implying controller ownership instead of the documented Stator-managed broadcast.

#### Unresolved findings left unchanged

- Exact Extension TVS / ESD implementation details remain intentionally owner-selected (`protected nets`,
  `device count`, `working voltage`, `package`, `MPN`); this fix only adds the missing consolidated BOM
  placeholder.
- All previously listed deferred schematic-capture and user-selection items remain unchanged.

**Note:** No commits were made.

### Pass 10 — Review

#### Scope summary

Re-reviewed `design/Electronics/Consolidated_BOM.md`, all active
`design/Electronics/*/Design_Spec.md` files, related connector-contract / logical signal-map sections in
`Board_Layout.md`, `design/Software/Actuation_Module/Design_Spec.md`, and the current report after Fix
Pass 9. Focus remained limited to BOM completeness for active circuit-support parts and connector-mapping
consistency. Physical PCB placement/routing was not reviewed.

#### Remaining Findings — New in Pass 10

| Severity | Files | Issue | Why it matters | Recommended fix | Status |
| :--- | :--- | :--- | :--- | :--- | :--- |
| medium | `design/Electronics/Consolidated_BOM.md`; cross-check: `design/Electronics/Stator/Design_Spec.md`, `design/Electronics/Settings_Board/Design_Spec.md`, `design/Electronics/Power_Module/Design_Spec.md`, `design/Electronics/Encoder/Design_Spec.md`, `design/Electronics/Rotor/Design_Spec.md`, `design/Electronics/JTAG_Daughterboard/Design_Spec.md` | The consolidated resistor summary still miscounts several fitted rows against the active per-board BOMs: the `10 kΩ 1% 0603` row shows `SBD=13` even though the active Settings BOM documents only `R1-R10` plus `R11` (`11` total); the `10 kΩ 1% 0402` row shows `STA=1` even though the active Stator BOM has no fitted `10 kΩ 0402` resistors; and the `75 Ω 1% 0603` row shows `STA=9` even though the active Stator BOM documents `R7-R12`, `R27-R32`, and `R33-R38` (`18` total). | `Consolidated_BOM.md` is procurement-facing. These count errors can underbuy Stator JTAG series parts and mis-state the fitted pull-resistor populations used for current board builds. | In a later fix pass, align the three consolidated rows to the active board BOMs: `10 kΩ 0603` -> `SBD=11`, `System Total=35`; `10 kΩ 0402` -> `STA=0`, `System Total=153`; `75 Ω 0603` -> `STA=18`, `System Total=18`. | pending fix pass |

#### Remaining Findings — Unchanged Known Unresolved Items

| Severity | Files | Issue | Why it matters | Recommended fix | Status |
| :--- | :--- | :--- | :--- | :--- | :--- |
| medium | `design/Electronics/Actuation_Module/Design_Spec.md`; `design/Software/Actuation_Module/Design_Spec.md` | AM support network for `ACTUATE_REQUEST` / `BOOT0` / `NRST` remains incompletely frozen. | Boot / reset behavior and request-input determinism still depend on later schematic-capture closure. | Freeze the exact support network and add the corresponding BOM rows / refdes once approved. | deferred schematic capture |
| medium | `design/Electronics/Settings_Board/Design_Spec.md`; `design/Electronics/Settings_Board/Board_Layout.md` | Settings Board LED topology remains underdefined between the documented MCP23017 anode-driving description and the common-anode `5V_MAIN` LED implementation. | LED current path and validity of the indicator-drive scheme remain unresolved. | Freeze one electrical topology and align the spec / BOM to it during later schematic capture. | deferred schematic capture |
| medium | `design/Electronics/Rotor/Design_Spec.md` | Rotor FDC2114 resonant front-end / unused-channel support definition remains explicitly deferred. | The sensing chain is still not fully circuit-complete at the channel front-end level. | Complete the deferred support-network definition and add the finalized support parts to the Rotor BOM. | deferred schematic capture |
| low | `design/Electronics/Power_Module/Design_Spec.md`; `design/Electronics/Stator/Design_Spec.md`; `design/Electronics/Consolidated_BOM.md` | PM / Stator INA219 input RC filter exact sourced parts remain unresolved. | The telemetry front-end support networks are still not procurement-closed. | Add the user-approved sourced resistor/capacitor filter population and roll those parts into the board and consolidated BOMs. | needs user selection |
| low | `design/Electronics/Rotor/Design_Spec.md`; `design/Electronics/Consolidated_BOM.md` | Rotor local I2C pull-up placeholders remain intentionally owner-selected. | The local sensor bus support network is documented but not fully sourceable. | User/owner to select the exact pull-up parts, then update the Rotor and consolidated BOMs. | needs user selection |
| low | `design/Electronics/Rotor/Design_Spec.md`; `design/Electronics/Consolidated_BOM.md` | Rotor `1 µF` FDC2114 bypass / reservoir capacitor placeholders remain intentionally owner-selected. | The documented FDC supply-support network is not yet fully sourceable. | User/owner to select the exact capacitor parts, then update the Rotor and consolidated BOMs. | needs user selection |
| low | `design/Electronics/Extension/Design_Spec.md`; `design/Electronics/Consolidated_BOM.md` | Extension TVS / ESD exact device count, protected nets, footprint, and MPN remain intentionally owner-selected. | Protection intent is documented, but final implementation details are still open. | User/owner to choose the exact protection implementation. | needs user selection |
| low | `design/Electronics/Stator/Design_Spec.md`; `design/Electronics/Consolidated_BOM.md` | Stator TVS / ESD exact device count, protected nets, footprint, and MPN remain intentionally owner-selected, with placeholder capture present. | Protection intent is documented, but final implementation details are still open. | User/owner to choose the exact protection implementation. | needs user selection |

#### Connector Consistency Check

| Severity | Files | Issue | Why it matters | Recommended fix | Status |
| :--- | :--- | :--- | :--- | :--- | :--- |
| info | `design/Electronics/Stator/Board_Layout.md`; `design/Electronics/Extension/Board_Layout.md`; `design/Electronics/Reflector/Board_Layout.md`; `design/Electronics/Settings_Board/Design_Spec.md`; `design/Electronics/Settings_Board/Board_Layout.md`; `design/Electronics/Actuation_Module/Design_Spec.md`; `design/Software/Actuation_Module/Design_Spec.md` | No new connector-mapping contradictions were found in Pass 10. The Stator-owned `J10` reflector / extension contract remains aligned with the Extension and Reflector docs after Fix Pass 9, Settings `J1` remains aligned with Stator `J13`, and the AM host/module dock split remains consistent across the hardware and firmware specs. | Confirms this pass did not uncover a new documented miswire trap at the reviewed board-to-board or service interfaces. | None. | clean |

#### Unsourced New Parts Requiring User Selection

- None newly identified in Pass 10.
- Existing owner-selected items remain unchanged:
  - PM / Stator INA219 input RC filter exact sourced parts
  - Rotor local I2C pull-up exact sourced parts
  - Rotor `1 µF` FDC2114 bypass / reservoir capacitor exact sourced parts
  - Extension TVS / ESD exact implementation
  - Stator TVS / ESD exact implementation

#### Pass Result

#### Not clean

Pass 10 found no new connector-mapping contradictions, but it did find a new evidence-backed
procurement-summary mismatch in `design/Electronics/Consolidated_BOM.md`. The clean-pass definition is
therefore not met.

### Pass 10 — Fix

- **Status:** consolidated resistor-summary bookkeeping fix applied

#### Files changed

- `design/Electronics/Consolidated_BOM.md`
- `.copilot/review-report.md`

#### Exact fixes applied

- **Closed Pass 10 finding 1 — consolidated resistor summary miscounts**
  - Updated `design/Electronics/Consolidated_BOM.md` `10 kΩ 1% 0603` row from `SBD=13` / `System Total=37`
    to `SBD=11` / `System Total=35`, matching the active Settings Board BOM evidence:
    `R1-R10` switch pull-downs plus `R11` `CFG_APPLY_N` pull-up in
    `design/Electronics/Settings_Board/Design_Spec.md`.
  - Updated `design/Electronics/Consolidated_BOM.md` `10 kΩ 1% 0402` row from `STA=1` / `System Total=154`
    to `STA=0` / `System Total=153`, matching the active Stator BOM evidence: no fitted `10 kΩ 0402`
    resistor row is present in `design/Electronics/Stator/Design_Spec.md`.
  - Updated `design/Electronics/Consolidated_BOM.md` `75 Ω 1% 0603` row from `STA=9` / `System Total=9`
    to `STA=18` / `System Total=18`, matching the active Stator BOM evidence:
    `R7-R12`, `R27-R32`, and `R33-R38` in `design/Electronics/Stator/Design_Spec.md`.

#### Unresolved findings left unchanged

- AM support network for `ACTUATE_REQUEST` / `BOOT0` / `NRST` remains deferred schematic-capture work.
- Settings Board LED topology remains deferred schematic-capture work.
- Rotor FDC2114 resonant front-end / unused-channel support definition remains deferred schematic-capture work.
- PM / Stator INA219 input RC filter exact sourced parts remain owner-selected.
- Rotor local I2C pull-up exact sourced parts remain owner-selected.
- Rotor `1 µF` FDC2114 bypass / reservoir capacitor exact sourced parts remain owner-selected.
- Extension TVS / ESD exact implementation remains owner-selected.
- Stator TVS / ESD exact implementation remains owner-selected.

**Note:** No commits were made.

### Pass 11 — Review

#### Scope summary

Re-reviewed `design/Electronics/Consolidated_BOM.md`, all active
`design/Electronics/*/Design_Spec.md` files, the related logical signal-map / connector-contract
sections in `Board_Layout.md` where needed, `design/Software/Actuation_Module/Design_Spec.md`, and
the current report after Fix Pass 10. Focus remained limited to BOM completeness for active
circuit-support parts and connector-mapping consistency only. Physical PCB placement/routing was not
reviewed.

#### Remaining Findings — New in Pass 11

| Severity | Files | Issue | Why it matters | Recommended fix | Status |
| :--- | :--- | :--- | :--- | :--- | :--- |
| medium | `design/Electronics/Consolidated_BOM.md`; cross-check: `design/Electronics/Actuation_Module/Design_Spec.md` | The consolidated `Component Usage Summary` still excludes documented Actuation Module support-part populations from several system totals because the summary matrix has no AM column even though the same file later freezes **2 fitted AM modules** for Rev A. Evidence-backed undercounts remain on already-documented support rows: the common `0.1 µF X7R 0402` row shows `393` but the AM BOM adds `C1-C3` = `6` more parts total; the `4.7 µF X7R 1210` row shows `1` but the AM BOM adds `C4` = `2` more; the `10 kΩ 1% 0402 pull resistor` row shows `153` but the AM BOM adds `R4` = `2` more; and the `330 Ω 1% 0402 LED current-limit resistor` row shows `6` but the AM BOM adds `R1-R3` = `6` more. | `Consolidated_BOM.md` is procurement-facing. Leaving the shared AM support network outside the top-level usage totals creates a real underbuy / review blind spot on common fitted passives that are already frozen elsewhere in the same BOM. | In the next fix pass, align the consolidated usage-summary accounting with the documented AM population: either add an AM column to the matrix or add explicit AM-inclusive roll-up rows so the system totals include the shared module's fitted support parts. | pending fix pass |

#### Remaining Findings — Unchanged Known Unresolved Items

| Severity | Files | Issue | Why it matters | Recommended fix | Status |
| :--- | :--- | :--- | :--- | :--- | :--- |
| medium | `design/Electronics/Actuation_Module/Design_Spec.md`; `design/Software/Actuation_Module/Design_Spec.md` | AM support network for `ACTUATE_REQUEST` / `BOOT0` / `NRST` remains incompletely frozen. | Boot / reset behaviour and request-input determinism still depend on later schematic-capture closure. | Freeze the exact support network and add the corresponding BOM rows / refdes once approved. | deferred schematic capture |
| medium | `design/Electronics/Settings_Board/Design_Spec.md`; `design/Electronics/Settings_Board/Board_Layout.md` | Settings Board LED topology remains underdefined between the documented MCP23017 anode-driving description and the common-anode `5V_MAIN` LED implementation. | LED current path and validity of the indicator-drive scheme remain unresolved. | Freeze one electrical topology and align the spec / BOM to it during later schematic capture. | deferred schematic capture |
| medium | `design/Electronics/Rotor/Design_Spec.md` | Rotor FDC2114 resonant front-end / unused-channel support definition remains explicitly deferred. | The sensing chain is still not fully circuit-complete at the channel front-end level. | Complete the deferred support-network definition and add the finalized support parts to the Rotor BOM. | deferred schematic capture |
| low | `design/Electronics/Power_Module/Design_Spec.md`; `design/Electronics/Stator/Design_Spec.md`; `design/Electronics/Consolidated_BOM.md` | PM / Stator INA219 input RC filter exact sourced parts remain unresolved. | The telemetry front-end support networks are still not procurement-closed. | Add the user-approved sourced resistor/capacitor filter population and roll those parts into the board and consolidated BOMs. | needs user selection |
| low | `design/Electronics/Rotor/Design_Spec.md`; `design/Electronics/Consolidated_BOM.md` | Rotor local I2C pull-up placeholders remain intentionally owner-selected. | The local sensor bus support network is documented but not fully sourceable. | User/owner to select the exact pull-up parts, then update the Rotor and consolidated BOMs. | needs user selection |
| low | `design/Electronics/Rotor/Design_Spec.md`; `design/Electronics/Consolidated_BOM.md` | Rotor `1 µF` FDC2114 bypass / reservoir capacitor placeholders remain intentionally owner-selected. | The documented FDC supply-support network is not yet fully sourceable. | User/owner to select the exact capacitor parts, then update the Rotor and consolidated BOMs. | needs user selection |
| low | `design/Electronics/Extension/Design_Spec.md`; `design/Electronics/Consolidated_BOM.md` | Extension TVS / ESD exact device count, protected nets, footprint, and MPN remain intentionally owner-selected. | Protection intent is documented, but final implementation details are still open. | User/owner to choose the exact protection implementation. | needs user selection |
| low | `design/Electronics/Stator/Design_Spec.md`; `design/Electronics/Consolidated_BOM.md` | Stator TVS / ESD exact device count, protected nets, footprint, and MPN remain intentionally owner-selected, with placeholder capture present. | Protection intent is documented, but final implementation details are still open. | User/owner to choose the exact protection implementation. | needs user selection |

#### Connector Consistency Check

| Severity | Files | Issue | Why it matters | Recommended fix | Status |
| :--- | :--- | :--- | :--- | :--- | :--- |
| info | `design/Electronics/Stator/Board_Layout.md`; `design/Electronics/Extension/Board_Layout.md`; `design/Electronics/Reflector/Board_Layout.md`; `design/Electronics/Settings_Board/Design_Spec.md`; `design/Electronics/Settings_Board/Board_Layout.md`; `design/Electronics/Actuation_Module/Design_Spec.md`; `design/Software/Actuation_Module/Design_Spec.md`; `design/Electronics/Rotor/Design_Spec.md` | No new connector-mapping contradictions were found in Pass 11. The Stator-owned `J10` reflector / extension contract remains aligned with the Extension and Reflector docs, Settings `J1` remains aligned with Stator `J13`, the AM host/module dock split remains aligned across hardware and firmware docs, and the rotor interface ownership remains consistent with the boards that cross-reference it. | Confirms this pass did not uncover a new documented miswire trap. | None. | clean |

#### Unsourced New Parts Requiring User Selection

- None newly identified in Pass 11.
- Existing owner-selected items remain unchanged:
  - PM / Stator INA219 input RC filter exact sourced parts
  - Rotor local I2C pull-up exact sourced parts
  - Rotor `1 µF` FDC2114 bypass / reservoir capacitor exact sourced parts
  - Extension TVS / ESD exact implementation
  - Stator TVS / ESD exact implementation

#### Pass Result

#### Not clean

Pass 11 found no new connector-mapping contradictions, but it did find one new evidence-backed
consolidated-BOM accounting omission affecting already-frozen Actuation Module support-part
populations. The clean-pass definition is therefore not met.

### Pass 11 — Fix

#### Files changed

- `design/Electronics/Consolidated_BOM.md`
- `.copilot/review-report.md`

#### Exact fixes applied

- Closed the Pass 11 shared Actuation Module support-part undercount in
  `design/Electronics/Consolidated_BOM.md` by updating the top `Component Usage Summary`
  `System Total` cells to include the already-frozen Rev A two-module AM population from
  `### Shared Actuation Module / Host Interface Components`:
  - `0.1 µF X7R 0402 decoupling cap` from `393` to `399` (`+6`, matching AM `C1-C3`)
  - `10 µF X7R 50 V 1206 bulk decoupling` from `200` to `202` (`+2`, matching AM `C5`)
  - `4.7 µF X7R 1210 entry filter` from `1` to `3` (`+2`, matching AM `C4`)
  - `10 kΩ 1% 0402 pull resistor` from `153` to `155` (`+2`, matching AM `R4`)
  - `330 Ω 1% 0402 LED current-limit resistor` from `6` to `12` (`+6`, matching AM `R1-R3`)
- Added a summary note above the matrix stating that `System Total` includes the shared Rev A
  two-module Actuation Module passive support-part population where the same common sourced part is
  already frozen in §4c. This keeps the existing board-column layout intact while making the
  adjusted totals traceable.

#### Rationale / findings closed

- This closes the Pass 11 `medium` finding at `design/Electronics/Consolidated_BOM.md`; cross-check:
  `design/Electronics/Actuation_Module/Design_Spec.md`, about the top procurement summary omitting
  already-frozen shared Actuation Module support-part counts from Rev A system totals.

#### Unresolved findings left unchanged

- AM support network for `ACTUATE_REQUEST` / `BOOT0` / `NRST` remains deferred schematic-capture work.
- Settings Board LED topology remains deferred schematic-capture work.
- Rotor FDC2114 resonant front-end / unused-channel support definition remains deferred schematic-capture work.
- PM / Stator INA219 input RC filter exact sourced parts remain owner-selected.
- Rotor local I2C pull-up exact sourced parts remain owner-selected.
- Rotor `1 µF` FDC2114 bypass / reservoir capacitor exact sourced parts remain owner-selected.
- Extension TVS / ESD exact implementation remains owner-selected.
- Stator TVS / ESD exact implementation remains owner-selected.

**Note:** No commits were made.

### Pass 12 — Review

#### Scope summary

Re-reviewed design/Electronics/Consolidated_BOM.md, all active design/Electronics/*/Design_Spec.md files, the related logical signal-map / connector-contract sections in Board_Layout.md where needed,
design/Software/Actuation_Module/Design_Spec.md, and the current report after Fix Pass 11. Focus remained limited to BOM completeness for active circuit-support parts and connector-mapping
consistency only. Physical PCB placement/routing was not reviewed.

#### Remaining Findings — New in Pass 12

None. Pass 12 did not identify any new connector-mapping contradictions or any new evidence-backed BOM/spec omissions for already-frozen circuitry.

#### Remaining Findings — Unchanged Known Unresolved Items

| Severity | Files | Issue | Why it matters | Recommended fix | Status |
| :--- | :--- | :--- | :--- | :--- | :--- |
| medium | design/Electronics/Actuation_Module/Design_Spec.md; design/Software/Actuation_Module/Design_Spec.md; design/Electronics/Consolidated_BOM.md | AM support-network definition for ACTUATE_REQUEST, BOOT0, and NRST remains incomplete. The AM spec still says the module provides local biasing for active-low ACTUATE_REQUEST, while the exact support network for that input and the boot/reset service nets is not frozen in the BOM/docs. | These nets still determine deterministic request-input state and STM32 boot/reset behavior. | Freeze the exact support network and add the corresponding BOM rows / refdes once approved. | deferred schematic capture |
| medium | design/Electronics/Settings_Board/Design_Spec.md; design/Electronics/Settings_Board/Board_Layout.md | Settings Board LED topology remains underdefined between the documented MCP23017 anode-driving description and the common-anode 5V_MAIN LED implementation. | LED current path and validity of the indicator-drive scheme remain unresolved. | Freeze one electrical topology and align the spec / BOM to it during later schematic capture. | deferred schematic capture |
| medium | design/Electronics/Rotor/Design_Spec.md | Rotor FDC2114 resonant front-end / unused-channel support definition remains explicitly deferred. | The sensing chain is still not fully circuit-complete at the channel front-end level. | Complete the deferred support-network definition and add the finalized support parts to the Rotor BOM. | deferred schematic capture |
| low | design/Electronics/Power_Module/Design_Spec.md; design/Electronics/Stator/Design_Spec.md; design/Electronics/Consolidated_BOM.md | PM / Stator INA219 input RC filter exact sourced parts remain unresolved. | The telemetry front-end support networks are still not procurement-closed. | Add the user-approved sourced resistor/capacitor filter population and roll those parts into the board and consolidated BOMs. | needs user selection |
| low | design/Electronics/Rotor/Design_Spec.md; design/Electronics/Consolidated_BOM.md | Rotor local I2C pull-up placeholders remain intentionally owner-selected. | The local sensor-bus support network is documented but not yet fully sourceable. | User/owner to select the exact pull-up parts, then update the Rotor and consolidated BOMs. | needs user selection |
| low | design/Electronics/Rotor/Design_Spec.md; design/Electronics/Consolidated_BOM.md | Rotor 1 µF FDC2114 bypass / reservoir capacitor placeholders remain intentionally owner-selected. | The documented FDC supply-support network is not yet fully sourceable. | User/owner to select the exact capacitor parts, then update the Rotor and consolidated BOMs. | needs user selection |
| low | design/Electronics/Extension/Design_Spec.md; design/Electronics/Consolidated_BOM.md | Extension TVS / ESD exact device count, protected nets, footprint, and MPN remain intentionally owner-selected. | Protection intent is documented, but final implementation details are still open. | User/owner to choose the exact protection implementation. | needs user selection |
| low | design/Electronics/Stator/Design_Spec.md; design/Electronics/Consolidated_BOM.md | Stator TVS / ESD exact device count, protected nets, footprint, and MPN remain intentionally owner-selected, with placeholder capture present. | Protection intent is documented, but final implementation details are still open. | User/owner to choose the exact protection implementation. | needs user selection |

#### Connector Consistency Check

| Severity | Files | Issue | Why it matters | Recommended fix | Status |
| :--- | :--- | :--- | :--- | :--- | :--- |
| info | design/Electronics/Stator/Board_Layout.md; design/Electronics/Extension/Board_Layout.md; design/Electronics/Reflector/Board_Layout.md; design/Electronics/Settings_Board/Design_Spec.md; design/Electronics/Settings_Board/Board_Layout.md; design/Electronics/Actuation_Module/Design_Spec.md; design/Software/Actuation_Module/Design_Spec.md; design/Electronics/Rotor/Design_Spec.md | No new connector-mapping contradictions were found in Pass 12. The Stator-owned J10 reflector / extension contract remains aligned with the Extension and Reflector docs, Settings J1 remains aligned with Stator J13, the AM host/module dock split remains aligned across hardware and firmware docs, and the rotor interface ownership remains consistent with the boards that cross-reference it. | Confirms this pass did not uncover a new documented miswire trap. | None. | clean |

#### Unsourced New Parts Requiring User Selection

- None newly identified in Pass 12.
- Existing owner-selected items remain unchanged:
  - PM / Stator INA219 input RC filter exact sourced parts
  - Rotor local I2C pull-up exact sourced parts
  - Rotor 1 µF FDC2114 bypass / reservoir capacitor exact sourced parts
  - Extension TVS / ESD exact implementation
  - Stator TVS / ESD exact implementation

#### Pass Result

#### Clean

Pass 12 found no new connector-mapping contradictions and no new evidence-backed BOM/spec omissions for already-frozen circuitry. The remaining open items are unchanged deferred schematic-capture or
owner-selection items already documented in prior passes, so the clean-pass definition is met for this review pass.

### Pass 13 — Review

#### Scope summary

Re-reviewed `design/Electronics/Consolidated_BOM.md`, all active `design/Electronics/*/Design_Spec.md`
files, the related logical signal-map / connector-contract sections in `Board_Layout.md` where needed,
`design/Software/Actuation_Module/Design_Spec.md`, `design/Design_Log.md`, and the current report after
clean Pass 12. Focus remained limited to BOM completeness for already-frozen circuit-support parts and
connector-mapping consistency only. Physical PCB placement/routing was not reviewed.

#### Remaining Findings — New in Pass 13

| Severity | Files | Issue | Why it matters | Recommended fix | Status |
| :--- | :--- | :--- | :--- | :--- | :--- |
| medium | `design/Electronics/Controller/Design_Spec.md`; `design/Electronics/Consolidated_BOM.md` | The active Controller spec still states that “all inputs (Status) feature 10kΩ series resistors to protect CM5 pins from transient spikes,” but the Controller BOM only captures `R1`, `R2`, and `R3`, and there is no explicit fitted population for those documented status-input series resistors. In the same spec, the relevant status inputs are the CM5-facing `PM_IO_INT_N`, local `USB_FAULT`, and `PWR_GD`; only `PWR_GD`'s pull-up (`R3`) is captured. | This is an evidence-backed BOM/spec omission on already-frozen Controller support circuitry. If those 10k series protectors are part of the approved design, they are not procurement-captured; if they are not part of the approved design, the protection statement is stale and can misdirect schematic capture. | In the next fix pass, either add explicit Controller BOM rows / refdes for the documented 10k status-input series resistors and roll them into the consolidated counts, or remove / narrow the stale blanket statement if those resistors are not actually part of the approved design. | pending fix pass |

#### Remaining Findings — Unchanged Known Unresolved Items

| Severity | Files | Issue | Why it matters | Recommended fix | Status |
| :--- | :--- | :--- | :--- | :--- | :--- |
| medium | `design/Electronics/Actuation_Module/Design_Spec.md`; `design/Software/Actuation_Module/Design_Spec.md`; `design/Electronics/Consolidated_BOM.md` | AM support-network definition for `ACTUATE_REQUEST`, `BOOT0`, and `NRST` remains incomplete. | These nets still determine deterministic request-input state and STM32 boot/reset behavior. | Freeze the exact support network and add the corresponding BOM rows / refdes once approved. | deferred schematic capture |
| medium | `design/Electronics/Settings_Board/Design_Spec.md`; `design/Electronics/Settings_Board/Board_Layout.md` | Settings Board LED topology remains underdefined between the documented MCP23017 anode-driving description and the common-anode `5V_MAIN` LED implementation. | LED current path and validity of the indicator-drive scheme remain unresolved. | Freeze one electrical topology and align the spec / BOM to it during later schematic capture. | deferred schematic capture |
| medium | `design/Electronics/Rotor/Design_Spec.md` | Rotor FDC2114 resonant front-end / unused-channel support definition remains explicitly deferred. | The sensing chain is still not fully circuit-complete at the channel front-end level. | Complete the deferred support-network definition and add the finalized support parts to the Rotor BOM. | deferred schematic capture |
| low | `design/Electronics/Power_Module/Design_Spec.md`; `design/Electronics/Stator/Design_Spec.md`; `design/Electronics/Consolidated_BOM.md` | PM / Stator INA219 input RC filter exact sourced parts remain unresolved. | The telemetry front-end support networks are still not procurement-closed. | Add the user-approved sourced resistor/capacitor filter population and roll those parts into the board and consolidated BOMs. | needs user selection |
| low | `design/Electronics/Rotor/Design_Spec.md`; `design/Electronics/Consolidated_BOM.md` | Rotor local I2C pull-up placeholders remain intentionally owner-selected. | The local sensor-bus support network is documented but not yet fully sourceable. | User/owner to select the exact pull-up parts, then update the Rotor and consolidated BOMs. | needs user selection |
| low | `design/Electronics/Rotor/Design_Spec.md`; `design/Electronics/Consolidated_BOM.md` | Rotor `1 µF` FDC2114 bypass / reservoir capacitor placeholders remain intentionally owner-selected. | The documented FDC supply-support network is not yet fully sourceable. | User/owner to select the exact capacitor parts, then update the Rotor and consolidated BOMs. | needs user selection |
| low | `design/Electronics/Extension/Design_Spec.md`; `design/Electronics/Consolidated_BOM.md` | Extension TVS / ESD exact device count, protected nets, footprint, and MPN remain intentionally owner-selected. | Protection intent is documented, but final implementation details are still open. | User/owner to choose the exact protection implementation. | needs user selection |
| low | `design/Electronics/Stator/Design_Spec.md`; `design/Electronics/Consolidated_BOM.md` | Stator TVS / ESD exact device count, protected nets, footprint, and MPN remain intentionally owner-selected, with placeholder capture present. | Protection intent is documented, but final implementation details are still open. | User/owner to choose the exact protection implementation. | needs user selection |

#### Connector Consistency Check

| Severity | Files | Issue | Why it matters | Recommended fix | Status |
| :--- | :--- | :--- | :--- | :--- | :--- |
| info | `design/Electronics/Stator/Board_Layout.md`; `design/Electronics/Extension/Board_Layout.md`; `design/Electronics/Reflector/Board_Layout.md`; `design/Electronics/Settings_Board/Design_Spec.md`; `design/Electronics/Settings_Board/Board_Layout.md`; `design/Electronics/Actuation_Module/Design_Spec.md`; `design/Software/Actuation_Module/Design_Spec.md`; `design/Electronics/Rotor/Design_Spec.md` | No new connector-mapping contradictions were found in Pass 13. The Stator-owned `J10` reflector / extension contract remains aligned with the Extension and Reflector docs, Settings `J1` remains aligned with Stator `J13`, the AM host/module dock split remains aligned across hardware and firmware docs, and the rotor interface ownership remains consistent with the boards that cross-reference it. | Confirms this pass did not uncover a new documented miswire trap. | None. | clean |

#### Unsourced New Parts Requiring User Selection

- None newly identified in Pass 13.
- Existing owner-selected items remain unchanged:
  - PM / Stator INA219 input RC filter exact sourced parts
  - Rotor local I2C pull-up exact sourced parts
  - Rotor `1 µF` FDC2114 bypass / reservoir capacitor exact sourced parts
  - Extension TVS / ESD exact implementation
  - Stator TVS / ESD exact implementation

#### Pass Result

#### Not clean

Pass 13 did not find any new connector-mapping contradiction, but it did find one new evidence-backed
Controller BOM/spec omission for already-frozen status-input protection circuitry. The design docs
therefore do **not** achieve a second consecutive clean pass yet.

### Pass 13 — Fix

- **Status:** fix applied

#### Files changed

- `design/Electronics/Controller/Design_Spec.md`
- `design/Electronics/Consolidated_BOM.md`
- `.copilot/review-report.md`

#### Fixes applied

- **Closed Pass 13 finding 1 — Controller status-input series resistors missing from BOM capture**
  - Narrowed the Controller protection note in `design/Electronics/Controller/Design_Spec.md` from a
    blanket "all inputs (Status)" statement to the three CM5-facing status inputs that are explicitly
    evidenced by the active docs: `PM_IO_INT_N`, `USB_FAULT`, and `PWR_GD`.
  - Added explicit Controller BOM rows `R4-R6` for those three `10 kΩ 1% 0603` series resistors,
    using the already locked common `ERJ-3EKF1002V / C191124` population.
  - Updated `design/Electronics/Consolidated_BOM.md` to add the same `R4-R6` fitted population and
    rolled the top summary count for the common `10 kΩ 0603` resistor line from Controller `6` to
    `9`, with system total `35` to `38`.
  - Broadened the consolidated summary row label from a pull-resistor-only description to a shared
    fitted `10 kΩ 0603` pull / series population so the procurement summary now matches the active
    design usage.

#### Unresolved / left unchanged

- AM `ACTUATE_REQUEST` / `BOOT0` / `NRST` support network remains deferred schematic-capture work.
- Settings Board LED topology remains deferred schematic-capture work.
- Rotor FDC2114 resonant front-end / unused-channel support remains owner-selected / unresolved.
- PM / Stator INA219 input RC filter exact sourced parts remain owner-selected / unresolved.
- Rotor I2C pull-up and `1 µF` FDC2114 bypass exact sourced parts remain owner-selected / unresolved.
- Extension and Stator TVS/ESD exact implementation details remain owner-selected / unresolved.

- **Commits:** no commits were made.

### Pass 14 — Review

#### Scope summary

Re-reviewed `design/Electronics/Consolidated_BOM.md`, all active `design/Electronics/*/Design_Spec.md`
files, the related logical signal-map / connector-contract sections in `Board_Layout.md` where needed,
`design/Software/Actuation_Module/Design_Spec.md`, and the current report after Fix Pass 13. Focus
remained limited to BOM completeness for already-frozen circuit-support parts and connector-mapping
consistency only. Physical PCB placement/routing was not reviewed.

#### Remaining Findings — New in Pass 14

| Severity | Files | Issue | Why it matters | Recommended fix | Status |
| :--- | :--- | :--- | :--- | :--- | :--- |
| medium | `design/Electronics/Consolidated_BOM.md`; cross-check: `design/Electronics/Controller/Design_Spec.md` | The Pass 13 Controller status-input BOM fix has not been fully propagated into the procurement-facing consolidated BOM. The active Controller BOM now captures `R4-R6` as three fitted `10 kΩ 1% 0603` CM5 status-input series resistors, but the consolidated common `10 kΩ 0603` row still shows `CTL = 2` and `System Total = 38`, which only covers the older Controller population and still omits those three fitted resistors. | The already-frozen `PM_IO_INT_N` / `USB_FAULT` / `PWR_GD` protection resistors can still disappear from purchasing review and aggregate passive counts even though the Controller board spec now documents them explicitly. | Update the consolidated `10 kΩ 1% 0603 fitted resistor` summary row to include the Controller's full fitted population (`R1`, `R3-R6`), i.e. `CTL = 5`, and recalculate the system total accordingly. | pending fix pass |
| medium | `design/Electronics/Consolidated_BOM.md`; cross-check: `design/Electronics/Power_Module/Design_Spec.md` | The consolidated multi-distributor PM connector section mislabels the external power connectors: it lists the Molex battery connector as `J3` and the USB-C receptacle as `J4`, while the active Power Module BOM uses `J4` = battery connector and `J5` = USB-C power input. | These are user-facing power-entry connectors. Wrong designators in the procurement/reference BOM can mislabel harness, test, and assembly documentation even if the selected parts themselves are correct. | Rename the consolidated BOM connector entries to match the active PM design spec: battery connector = `J4`, USB-C receptacle = `J5`. | pending fix pass |

#### Remaining Findings — Unchanged Known Unresolved Items

No new repository evidence in Pass 14 resolves the previously documented deferred schematic-capture or
owner-selection items below.

### Pass 14 — Fix

- **Status:** fix applied

#### Files changed

- `design/Electronics/Consolidated_BOM.md`
- `.copilot/review-report.md`

#### Fixes applied

- **Closed Pass 14 finding 1 — Controller 10 kΩ 0603 consolidated summary column undercount**
  - Corrected the consolidated common `10 kΩ 1% 0603` fitted-resistor summary row so the
    Controller column now carries the full fitted population from the active Controller BOM:
    `R1`, `R3-R6` = `CTL 5`.
  - Restored the PM column to its previously correct `6` fitted parts and updated the system
    total from `38` to `41`.
  - This closes the remaining procurement-summary lag from the Pass 13 Controller status-input
    series-resistor fix.

- **Closed Pass 14 finding 2 — PM external connector refdes drift in consolidated BOM**
  - Renamed the consolidated PM external-connector entries to match the active Power Module BOM:
    battery connector = `J4`, USB-C power receptacle = `J5`.
  - Parts, sourcing, and descriptions were left unchanged; only the stale designators were corrected.

#### Unresolved / left unchanged

- AM `ACTUATE_REQUEST` / `BOOT0` / `NRST` support network remains deferred schematic-capture work.
- Settings Board LED topology remains deferred schematic-capture work.
- Rotor FDC2114 resonant front-end / unused-channel support remains owner-selected / unresolved.
- PM / Stator INA219 input RC filter exact sourced parts remain owner-selected / unresolved.
- Rotor I2C pull-up and `1 µF` FDC2114 bypass exact sourced parts remain owner-selected / unresolved.
- Extension and Stator TVS/ESD exact implementation details remain owner-selected / unresolved.

- **Commits:** no commits were made.

| Severity | Files | Issue | Why it matters | Recommended fix | Status |
| :--- | :--- | :--- | :--- | :--- | :--- |
| medium | `design/Electronics/Actuation_Module/Design_Spec.md`; `design/Software/Actuation_Module/Design_Spec.md` | AM support network for `ACTUATE_REQUEST` / `BOOT0` / `NRST` remains incompletely frozen. | Boot / reset behavior and request-input determinism still depend on later schematic-capture closure. | Freeze the exact support network and add the corresponding BOM rows / refdes once approved. | deferred schematic capture |
| medium | `design/Electronics/Settings_Board/Design_Spec.md`; `design/Electronics/Settings_Board/Board_Layout.md` | Settings Board LED topology remains underdefined between the documented MCP23017 anode-driving description and the common-anode `5V_MAIN` LED implementation. | LED current path and validity of the indicator-drive scheme remain unresolved. | Freeze one electrical topology and align the spec / BOM to it during later schematic capture. | deferred schematic capture |
| medium | `design/Electronics/Rotor/Design_Spec.md` | Rotor FDC2114 resonant front-end / unused-channel support definition remains explicitly deferred. | The sensing chain is still not fully circuit-complete at the channel front-end level. | Complete the deferred support-network definition and add the finalized support parts to the Rotor BOM. | deferred schematic capture |
| low | `design/Electronics/Power_Module/Design_Spec.md`; `design/Electronics/Stator/Design_Spec.md`; `design/Electronics/Consolidated_BOM.md` | PM / Stator INA219 input RC filter exact sourced parts remain unresolved. | The telemetry front-end support networks are still not procurement-closed. | Add the user-approved sourced resistor/capacitor filter population and roll those parts into the board and consolidated BOMs. | needs user selection |
| low | `design/Electronics/Rotor/Design_Spec.md`; `design/Electronics/Consolidated_BOM.md` | Rotor local I2C pull-up placeholders remain intentionally owner-selected. | The local sensor bus support network is documented but not fully sourceable. | User/owner to select the exact pull-up parts, then update the Rotor and consolidated BOMs. | needs user selection |
| low | `design/Electronics/Rotor/Design_Spec.md`; `design/Electronics/Consolidated_BOM.md` | Rotor `1 µF` FDC2114 bypass / reservoir capacitor placeholders remain intentionally owner-selected. | The documented FDC supply-support network is not yet fully sourceable. | User/owner to select the exact capacitor parts, then update the Rotor and consolidated BOMs. | needs user selection |
| low | `design/Electronics/Extension/Design_Spec.md`; `design/Electronics/Consolidated_BOM.md` | Extension TVS / ESD exact device count, protected nets, footprint, and MPN remain intentionally owner-selected. | Protection intent is documented, but final implementation details are still open. | User/owner to choose the exact protection implementation. | needs user selection |
| low | `design/Electronics/Stator/Design_Spec.md`; `design/Electronics/Consolidated_BOM.md` | Stator TVS / ESD exact device count, protected nets, footprint, and MPN remain intentionally owner-selected, with placeholder capture present. | Protection intent is documented, but final implementation details are still open. | User/owner to choose the exact protection implementation. | needs user selection |

#### Connector Consistency Check

| Severity | Files | Issue | Why it matters | Recommended fix | Status |
| :--- | :--- | :--- | :--- | :--- | :--- |
| info | `design/Electronics/Stator/Board_Layout.md`; `design/Electronics/Extension/Board_Layout.md`; `design/Electronics/Reflector/Board_Layout.md`; `design/Electronics/Settings_Board/Design_Spec.md`; `design/Electronics/Settings_Board/Board_Layout.md`; `design/Electronics/Actuation_Module/Design_Spec.md`; `design/Software/Actuation_Module/Design_Spec.md`; `design/Electronics/Rotor/Design_Spec.md` | No new connector pin-allocation contradictions were found in Pass 14 across the Stator-owned `J10` contract, Settings `J1` ↔ Stator `J13`, the AM host/module docks, or the Rotor interface documents. The only connector issue found this pass is the Power Module external-connector designator mismatch in `Consolidated_BOM.md` listed above. | Confirms this pass did not uncover a new documented pin-swap / miswire trap on the reviewed connector interfaces. | None. | clean |

#### Unsourced New Parts Requiring User Selection

- None newly identified in Pass 14.
- Existing owner-selected items remain unchanged:
  - PM / Stator INA219 input RC filter exact sourced parts
  - Rotor local I2C pull-up exact sourced parts
  - Rotor `1 µF` FDC2114 bypass / reservoir capacitor exact sourced parts
  - Extension TVS / ESD exact implementation
  - Stator TVS / ESD exact implementation

#### Pass Result

#### Not clean

Pass 14 found no new connector pin-allocation contradiction, but it did find two new evidence-backed
cross-document / procurement-BOM inconsistencies: the Controller status-input resistor population is
still undercounted in the consolidated passive summary, and the Power Module battery / USB-C connector
designators are misaligned in the consolidated BOM. The clean-pass definition is therefore not met.

---

## Pass 15 — Read-Only Verification (Post-Pass-14 Consolidated BOM Bookkeeping)

**Type:** Read-only verification pass  
**Scope:** `Consolidated_BOM.md` (full component-usage matrix), `Power_Module/Design_Spec.md §5 BOM`,
`Controller/Design_Spec.md §11 BOM`, `Stator/Design_Spec.md §9 BOM`,
`Settings_Board/Design_Spec.md §9 BOM`, `Encoder/Design_Spec.md §10 BOM`,
`Rotor/Design_Spec.md §5 BOM`; cross-checked against the Pass 14 tracker.

### Scope Summary

Pass 14 applied two fixes to `Consolidated_BOM.md`:

1. Controller 10 kΩ 0603 column corrected from 2 to 5 (R1, R3–R6); system total updated 38 → 41.
2. Power Module connector designators corrected: battery J3 → J4, USB-C J4 → J5.

This pass verifies those fixes end-to-end, audits the 10 kΩ 0603 system-total arithmetic against every
board BOM, and checks the Settings Board BOM completeness.

### Verified Correct

| Item | Evidence | Result |
| :--- | :--- | :--- |
| PM J4 = battery, J5 = USB-C | `Power_Module/Design_Spec.md` FR-PM-01, DR-PM-01, §5 BOM J4/J5 lines | ✓ Pass 14 fix correctly applied |
| CTL = 5 for 10 kΩ 0603 | Controller §11 BOM: R1, R3, R4, R5, R6 = 5 × ERJ-3EKF1002V; R2 = 100 Ω (excluded) | ✓ |
| PM = 6 for 10 kΩ 0603 | PM §5 BOM: R6, R9, R10, R16, R22, R29 = 6 × ERJ-3EKF1002V; R15 (10.0 kΩ 0.1% ERA-3ARB103V) is in its own consolidated row (line 115) | ✓ |
| STA = 16 for 10 kΩ 0603 | Stator §9 BOM: R2–R6 (5) + R16–R19 (4) + R20 (1) + R21–R26 (6) = 16 | ✓ |
| SBD = 11 for 10 kΩ 0603 | SBD §9 BOM: R1–R10 pull-downs (10) + R11 CFG_APPLY_N pull-up (1) = 11 | ✓ |
| ENC = — for 10 kΩ 0603 | Encoder §10 BOM: R2–R5 are 10 kΩ **0402** (ERJ-2RKF1002X) | ✓ |
| ROT = — for 10 kΩ 0603 | Rotor §5 BOM: R2–R5 (per Board A) are 10 kΩ **0402** (ERJ-2RKF1002X); ROT Total = 120 in the 0402 row matches 4 × 30 | ✓ |
| AM contribution to 10 kΩ 0603 = 0 | AM R4 is 10 kΩ **0402** only; contributes to the 0402 row (AM = 2, total = 155 ✓) | ✓ |
| REF, EXT, JDB = — for 10 kΩ 0603 | No 10 kΩ 0603 resistors in those boards; consistent with consolidated matrix | ✓ |

### New Findings

#### BOM Correctness — Component Count / Missing Rows

| Severity | Files | Issue | Why it matters | Recommended fix | Status |
| :--- | :--- | :--- | :--- | :--- | :--- |
| medium | `design/Electronics/Consolidated_BOM.md` line 90 | 10 kΩ 1% 0603 (ERJ-3EKF1002V) system total = **41**, but the verified sum of all board columns = PM(6)+CTL(5)+STA(16)+SBD(11) = **38**. All other columns (ENC, ROT, REF, EXT, JDB) are confirmed zero for this value/footprint; AM modules contribute zero (AM uses 10 kΩ 0402). Overcount = **+3**. Root cause: the Pass 14 fix incremented the prior total (38) by +3 for the CTL 2→5 correction, but that prior total was itself already overcounted by 3 from an earlier pass arithmetic error — the ghost was never resolved. | Over-procurement by 3 units of ERJ-3EKF1002V on every system build run from the consolidated BOM. | Change the system total from `41` to `38`. | **new** |
| medium | `design/Electronics/Consolidated_BOM.md` lines 102 (and missing row); `design/Electronics/Settings_Board/Design_Spec.md §9 BOM` R18–R53 | Settings Board LED series resistors (R18–R53, **36 fitted parts** with confirmed MPNs) are absent from the consolidated BOM: (a) 12× R18–R29 **150 Ω 1% 0603 ERJ-3EKF1500V / C400650** (red per-indicator cathode) — **no consolidated row exists** for this MPN; (b) 24× R30–R53 **100 Ω 1% 0603 ERJ-3EKF1000V / C193336** (green + blue per-indicator cathode) — the existing 100 Ω 0603 row (line 102) shows SBD = `—`, total = 1 (CTL R2 differential-termination only). Neither omission is a deferred placeholder: both values carry sourced MPNs and fixed quantities in the active Settings Board BOM. | 36 confirmed-MPN, footprint-frozen parts are invisible to system procurement. Building from the consolidated BOM alone leaves a 12-unit 150 Ω 0603 and a 24-unit 100 Ω 0603 shortfall. | (a) Add a new row `150 Ω 1% 0603 LED series resistor (ERJ-3EKF1500V / C400650)` with SBD = 12, total = 12 (all other columns `—`). (b) On the existing 100 Ω 0603 row: change SBD `—` → `24`; change total `1` → `25`; broaden the row label beyond "differential termination" to cover both the CTL R2 function and the SBD R30–R53 LED series function (or add a second SBD-dedicated 100 Ω 0603 row). | **new** |

#### Known Unresolved Items (unchanged — no new repo evidence resolves any)

| Severity | Files | Issue | Why it matters | Recommended fix | Status |
| :--- | :--- | :--- | :--- | :--- | :--- |
| medium | `design/Electronics/Actuation_Module/Design_Spec.md`; `design/Software/Actuation_Module/Design_Spec.md` | AM support network for `ACTUATE_REQUEST` / `BOOT0` / `NRST` remains incompletely frozen. | Boot / reset determinism depends on later schematic-capture closure. | Freeze the exact support network and add corresponding BOM rows once approved. | deferred schematic capture |
| medium | `design/Electronics/Settings_Board/Design_Spec.md`; `design/Electronics/Settings_Board/Board_Layout.md` | Settings Board LED topology remains underdefined between MCP23017 anode-drive and common-anode 5V_MAIN implementation. | LED current path and indicator-drive validity remain unresolved. | Freeze one topology and align spec / BOM during schematic capture. | deferred schematic capture |
| medium | `design/Electronics/Rotor/Design_Spec.md` | Rotor FDC2114 resonant front-end / unused-channel support definition remains explicitly deferred. | Sensing chain not yet circuit-complete at the channel front-end level. | Complete the deferred support-network definition and add finalised support parts to the Rotor BOM. | deferred schematic capture |
| low | `design/Electronics/Power_Module/Design_Spec.md`; `design/Electronics/Stator/Design_Spec.md`; `design/Electronics/Consolidated_BOM.md` | PM / Stator INA219 input RC filter exact sourced parts remain unresolved. | Telemetry front-end support networks not procurement-closed. | Add user-approved resistor/capacitor filter parts to board and consolidated BOMs. | needs user selection |
| low | `design/Electronics/Rotor/Design_Spec.md`; `design/Electronics/Consolidated_BOM.md` | Rotor local I²C pull-up placeholders remain owner-selected. | Local sensor bus support network not fully sourceable. | User/owner to select exact pull-up parts and update Rotor and consolidated BOMs. | needs user selection |
| low | `design/Electronics/Rotor/Design_Spec.md`; `design/Electronics/Consolidated_BOM.md` | Rotor 1 µF FDC2114 bypass / reservoir capacitor placeholders remain owner-selected. | Documented FDC supply-support network not fully sourceable. | User/owner to select exact capacitor parts and update Rotor and consolidated BOMs. | needs user selection |
| low | `design/Electronics/Extension/Design_Spec.md`; `design/Electronics/Consolidated_BOM.md` | Extension TVS / ESD exact device count, protected nets, footprint, and MPN remain owner-selected. | Protection intent documented; implementation details still open. | User/owner to choose exact protection implementation. | needs user selection |
| low | `design/Electronics/Stator/Design_Spec.md`; `design/Electronics/Consolidated_BOM.md` | Stator TVS / ESD exact device count, protected nets, footprint, and MPN remain owner-selected. | Protection intent documented; implementation details still open. | User/owner to choose exact protection implementation. | needs user selection |

#### Connector Consistency Check

No new connector pin-allocation contradictions found in this pass. PM J4/J5 designator fix confirmed correctly applied.

#### Unsourced New Parts Requiring User Selection

No new unsourced items identified in Pass 15. Existing owner-selected items (INA219 RC filter, Rotor I²C pull-ups, Rotor FDC2114 reservoir caps, Extension TVS, Stator TVS) carry forward unchanged.

#### Pass Result

#### Not clean

Two new evidence-backed procurement bookkeeping errors found:

1. **P15-F1** — 10 kΩ 1% 0603 row system total is overcounted by 3 (consolidated shows 41; verified board-column sum is 38; no board or AM module accounts for the delta).
2. **P15-F2** — Settings Board 36× LED series resistors (R18–R53: 12× 150 Ω 0603 ERJ-3EKF1500V + 24× 100 Ω 0603 ERJ-3EKF1000V) are absent from the consolidated BOM — one value has no row at all; the
other value's row is missing the SBD column entry entirely.

Neither error was introduced by Pass 14. The total overcount is a residual ghost from the Pass 13/14 arithmetic chain; the LED resistor gap pre-dates the entire pass series. Both are
procurement-blocking omissions requiring a targeted fix pass (Pass 16) before the consolidated BOM can serve as a complete build document.

### Pass 15 — Review

#### Scope summary

Re-checked `design/Electronics/Consolidated_BOM.md`, all active `design/Electronics/*/Design_Spec.md`
files, related connector-contract / logical signal-map sections in `Board_Layout.md`, the AM firmware
spec at `design/Software/Actuation_Module/Design_Spec.md`, and the current report after the latest
consolidated-BOM bookkeeping fixes. Focus remained limited to circuit-support BOM completeness for
already-frozen circuitry and connector mapping consistency only; physical PCB placement/routing was not
reviewed.

#### Remaining findings

##### New findings

- **Severity:** medium  
  **Files:** `design/Electronics/Consolidated_BOM.md`  
  **Issue:** The consolidated `10 kΩ 1% 0603 fitted resistor` row still has an incorrect system total.
  The row shows `PM=6`, `CTL=5`, `STA=16`, `SBD=11`, all other board columns blank/zero, but the total
  is listed as `41` instead of the verified board-column sum `38`.  
  **Why it matters:** This is a procurement-facing bookkeeping error on an already-frozen fitted passive
  population. A build using the consolidated summary would overcount this resistor by three units.  
  **Recommended fix:** Recalculate that row from the actual board columns and change the system total from
  `41` to `38`.  
  **Status:** pending fix pass

- **Severity:** medium  
  **Files:** `design/Electronics/Consolidated_BOM.md`, `design/Electronics/Settings_Board/Design_Spec.md`  
  **Issue:** The Settings Board LED series resistor population is still not captured correctly in the
  consolidated BOM. `R18-R29` (12× `150 Ω 1% 0603`, ERJ-3EKF1500V / C400650) have no consolidated row,
  and `R30-R53` (24× `100 Ω 1% 0603`, ERJ-3EKF1000V / C193336) are not counted in the existing `100 Ω`
  row, which still shows only the Controller population.  
  **Why it matters:** These are already-frozen, sourced support parts for active indicator circuitry. If
  omitted from the consolidated BOM, procurement can underbuy 12× `150 Ω` and 24× `100 Ω` fitted
  resistors.  
  **Recommended fix:** Add a dedicated consolidated row for the 12× Settings Board `150 Ω 0603` LED
  resistors and either update the existing `100 Ω 0603` row to include the 24× Settings Board LED
  resistors or add a separate Settings-specific row.  
  **Status:** pending fix pass

##### Unchanged known unresolved items

- **Severity:** medium  
  **Files:** `design/Electronics/Actuation_Module/Design_Spec.md`, `design/Software/Actuation_Module/Design_Spec.md`  
  **Issue:** AM support network for `ACTUATE_REQUEST` / `BOOT0` / `NRST` remains unfrozen.  
  **Why it matters:** Boot / reset determinism and input-state definition still depend on later
  schematic-capture closure.  
  **Recommended fix:** Freeze the intended support network and add the corresponding BOM rows/refdes.  
  **Status:** deferred schematic capture

- **Severity:** high  
  **Files:** `design/Electronics/Settings_Board/Design_Spec.md`  
  **Issue:** Settings Board LED topology remains underdefined between the documented MCP23017 anode-drive
  description and the `5V_MAIN` common-anode implementation.  
  **Why it matters:** The LED current path is still not fully frozen at the circuit-topology level.  
  **Recommended fix:** Freeze one topology and align the board docs/BOM during later schematic capture.  
  **Status:** deferred schematic capture

- **Severity:** medium  
  **Files:** `design/Electronics/Rotor/Design_Spec.md`  
  **Issue:** Rotor FDC2114 resonant front-end / unused-channel support definition remains deferred.  
  **Why it matters:** The sensing chain is still not fully circuit-complete at the channel-support level.  
  **Recommended fix:** Complete the deferred support-network definition and add the resulting BOM content
  once approved.  
  **Status:** deferred schematic capture

- **Severity:** low  
  **Files:** `design/Electronics/Power_Module/Design_Spec.md`, `design/Electronics/Stator/Design_Spec.md`, `design/Electronics/Consolidated_BOM.md`  
  **Issue:** PM / Stator INA219 input RC filter exact sourced parts remain owner-selected.  
  **Why it matters:** Those telemetry support networks are still not procurement-closed.  
  **Recommended fix:** Add the user-approved resistor/capacitor filter parts to the per-board and
  consolidated BOMs.  
  **Status:** needs user selection

- **Severity:** low  
  **Files:** `design/Electronics/Rotor/Design_Spec.md`, `design/Electronics/Consolidated_BOM.md`  
  **Issue:** Rotor local I2C pull-up exact sourcing placeholders remain unchanged.  
  **Why it matters:** The documented local sensor-bus support network is still not fully sourceable.  
  **Recommended fix:** User/owner to select the exact pull-up parts and update Rotor and consolidated BOMs.  
  **Status:** needs user selection

- **Severity:** low  
  **Files:** `design/Electronics/Rotor/Design_Spec.md`, `design/Electronics/Consolidated_BOM.md`  
  **Issue:** Rotor `1 µF` FDC2114 bypass / reservoir capacitor exact sourcing placeholders remain
  unchanged.  
  **Why it matters:** The documented FDC supply-support network is still not fully sourceable.  
  **Recommended fix:** User/owner to select the exact capacitor parts and update Rotor and consolidated
  BOMs.  
  **Status:** needs user selection

- **Severity:** low  
  **Files:** `design/Electronics/Extension/Design_Spec.md`, `design/Electronics/Consolidated_BOM.md`  
  **Issue:** Extension TVS / ESD exact device count, protected nets, footprint, and MPN remain
  owner-selected.  
  **Why it matters:** Protection intent is documented, but final implementation details are still open.  
  **Recommended fix:** User/owner to choose the exact protection implementation.  
  **Status:** needs user selection

- **Severity:** low  
  **Files:** `design/Electronics/Stator/Design_Spec.md`, `design/Electronics/Consolidated_BOM.md`  
  **Issue:** Stator TVS / ESD exact device count, protected nets, footprint, and MPN remain
  owner-selected.  
  **Why it matters:** Protection intent is documented, but final implementation details are still open.  
  **Recommended fix:** User/owner to choose the exact protection implementation.  
  **Status:** needs user selection

#### Connector consistency check

- **Severity:** info  
  **Files:** `design/Electronics/Stator/Board_Layout.md`, `design/Electronics/Encoder/Board_Layout.md`, `design/Electronics/Reflector/Board_Layout.md`,
  `design/Electronics/Settings_Board/Design_Spec.md`, `design/Electronics/Power_Module/Design_Spec.md`, `design/Software/Actuation_Module/Design_Spec.md`  
  **Issue:** No new connector-mapping contradictions were found in this pass. The previously corrected
  Encoder JTAG numbering remains aligned with the Stator-owned contract, the Settings Board `J1` mapping
  remains consistent with the Stator-side harness definition, the Reflector connector contract remains
  internally consistent, and the PM external-connector designator fix remains aligned with the PM spec.  
  **Why it matters:** Confirms this pass did not uncover a new documented miswire trap on the reviewed
  interfaces.  
  **Recommended fix:** None.  
  **Status:** clean

#### Unsourced New Parts Requiring User Selection

- None newly identified in Pass 15.
- Existing owner-selected items remain unchanged:
  - PM / Stator INA219 input RC filter exact sourced parts
  - Rotor local I2C pull-up exact sourced parts
  - Rotor `1 µF` FDC2114 bypass / reservoir capacitor exact sourced parts
  - Extension TVS / ESD exact implementation
  - Stator TVS / ESD exact implementation

#### Pass Result

#### Pass 15 result: not clean

Reason: no new connector-mapping contradictions were found, but two evidence-backed consolidated-BOM
bookkeeping omissions remain for already-frozen circuitry, so the clean-pass definition is not met.

### Pass 16 — Review

#### Scope summary

Re-checked `design/Electronics/Consolidated_BOM.md`, all active `design/Electronics/*/Design_Spec.md`
files, related logical signal-map / connector-contract sections in `Board_Layout.md`, the AM firmware
spec at `design/Software/Actuation_Module/Design_Spec.md`, and the current report after Fix Pass 15.
Focus remained limited to materially missing circuit-support BOM content for already-frozen circuitry and
connector mapping consistency only; physical PCB placement/routing was not reviewed.

Fix Pass 15 re-check:

- The consolidated `10 kΩ 1% 0603` fitted-resistor row now shows the corrected system total `38`.
- The Settings Board LED series resistors are now captured in the consolidated BOM as:
  - `150 Ω 1% 0603` LED current-limit row with `SBD=12`, total `12`
  - `100 Ω 1% 0603` LED current-limit row with `SBD=24`, total `24`

#### Remaining findings

##### New findings

- None. Pass 16 did not identify any new connector-mapping contradictions or any new evidence-backed
  BOM/spec omissions for already-frozen circuitry.

##### Unchanged known unresolved items

- **Severity:** medium  
  **Files:** `design/Electronics/Actuation_Module/Design_Spec.md`, `design/Software/Actuation_Module/Design_Spec.md`, `design/Electronics/Consolidated_BOM.md`  
  **Issue:** The AM support-network definition for `ACTUATE_REQUEST`, `BOOT0`, and `NRST` remains unfrozen. The active AM docs still freeze the home-input RC support (`R4`, `C1`) but do not yet
  freeze the exact support treatment for the host request input and STM32 boot/reset service nets.  
  **Why it matters:** These nets still determine deterministic request-input state and STM32 boot/reset behaviour.  
  **Recommended fix:** Freeze the intended support network and add the corresponding BOM rows / refdes during later schematic capture.  
  **Status:** deferred schematic capture

- **Severity:** high  
  **Files:** `design/Electronics/Settings_Board/Design_Spec.md`, `design/Electronics/Settings_Board/Board_Layout.md`  
  **Issue:** The Settings Board LED topology remains underdefined between the documented MCP23017 anode-drive description and the `5V_MAIN` common-anode implementation.  
  **Why it matters:** The LED current path is still not fully frozen at the circuit-topology level.  
  **Recommended fix:** Freeze one topology and align the board docs / BOM during later schematic capture.  
  **Status:** deferred schematic capture

- **Severity:** medium  
  **Files:** `design/Electronics/Rotor/Design_Spec.md`  
  **Issue:** Rotor FDC2114 resonant front-end / unused-channel support definition remains deferred.  
  **Why it matters:** The sensing chain is still not fully circuit-complete at the channel-support level.  
  **Recommended fix:** Complete the deferred support-network definition and add the resulting BOM content once approved.  
  **Status:** deferred schematic capture

- **Severity:** low  
  **Files:** `design/Electronics/Power_Module/Design_Spec.md`, `design/Electronics/Stator/Design_Spec.md`, `design/Electronics/Consolidated_BOM.md`  
  **Issue:** PM / Stator INA219 input RC filter exact sourced parts remain owner-selected.  
  **Why it matters:** Those telemetry support networks are still not procurement-closed.  
  **Recommended fix:** Add the user-approved resistor/capacitor filter parts to the per-board and consolidated BOMs.  
  **Status:** needs user selection

- **Severity:** low  
  **Files:** `design/Electronics/Rotor/Design_Spec.md`, `design/Electronics/Consolidated_BOM.md`  
  **Issue:** Rotor local I2C pull-up exact sourcing placeholders remain unchanged.  
  **Why it matters:** The documented local sensor-bus support network is still not fully sourceable.  
  **Recommended fix:** User/owner to select the exact pull-up parts and update Rotor and consolidated BOMs.  
  **Status:** needs user selection

- **Severity:** low  
  **Files:** `design/Electronics/Rotor/Design_Spec.md`, `design/Electronics/Consolidated_BOM.md`  
  **Issue:** Rotor `1 µF` FDC2114 bypass / reservoir capacitor exact sourcing placeholders remain unchanged.  
  **Why it matters:** The documented FDC supply-support network is still not fully sourceable.  
  **Recommended fix:** User/owner to select the exact capacitor parts and update Rotor and consolidated BOMs.  
  **Status:** needs user selection

- **Severity:** low  
  **Files:** `design/Electronics/Extension/Design_Spec.md`, `design/Electronics/Consolidated_BOM.md`  
  **Issue:** Extension TVS / ESD exact device count, protected nets, footprint, and MPN remain owner-selected.  
  **Why it matters:** Protection intent is documented, but final implementation details are still open.  
  **Recommended fix:** User/owner to choose the exact protection implementation.  
  **Status:** needs user selection

- **Severity:** low  
  **Files:** `design/Electronics/Stator/Design_Spec.md`, `design/Electronics/Consolidated_BOM.md`  
  **Issue:** Stator TVS / ESD exact device count, protected nets, footprint, and MPN remain owner-selected.  
  **Why it matters:** Protection intent is documented, but final implementation details are still open.  
  **Recommended fix:** User/owner to choose the exact protection implementation.  
  **Status:** needs user selection

#### Connector consistency check

- **Severity:** info  
  **Files:** `design/Electronics/Stator/Board_Layout.md`, `design/Electronics/Encoder/Board_Layout.md`, `design/Electronics/Reflector/Board_Layout.md`, `design/Electronics/Extension/Design_Spec.md`,
  `design/Electronics/Settings_Board/Design_Spec.md`, `design/Electronics/Settings_Board/Board_Layout.md`, `design/Electronics/Actuation_Module/Design_Spec.md`,
  `design/Software/Actuation_Module/Design_Spec.md`, `design/Electronics/Controller/Design_Spec.md`  
  **Issue:** No new connector-mapping contradictions were found in this pass. The corrected Encoder JTAG numbering remains aligned with the Stator-owned contract, the Settings Board `J1` ↔ Stator
  `J13` harness remains consistent, the Reflector / Extension `J10` contract remains aligned with the Stator-owned definition, and the AM host / module dock split remains consistent across hardware
  and firmware docs.  
  **Why it matters:** Confirms this pass did not uncover a new documented miswire trap on the reviewed interfaces.  
  **Recommended fix:** None.  
  **Status:** clean

#### Unsourced New Parts Requiring User Selection

- None newly identified in Pass 16.
- Existing owner-selected items remain unchanged:
  - PM / Stator INA219 input RC filter exact sourced parts
  - Rotor local I2C pull-up exact sourced parts
  - Rotor `1 µF` FDC2114 bypass / reservoir capacitor exact sourced parts
  - Extension TVS / ESD exact implementation
  - Stator TVS / ESD exact implementation

#### Pass Result

#### Pass 16 result: clean

Reason: no new connector-mapping contradictions were found and no new evidence-backed BOM/spec
omissions were found for already-frozen circuitry. The remaining open items are unchanged deferred
schematic-capture or owner-selection items already documented in prior passes, so the clean-pass
definition is met for this review pass.

### Pass 17 — Review

#### Scope summary

Read-only confirmation review after clean Pass 16. Re-checked `design/Electronics/Consolidated_BOM.md`,
all active `design/Electronics/*/Design_Spec.md` files, related logical signal-map / connector-contract
sections in `Board_Layout.md`, `design/Software/Actuation_Module/Design_Spec.md`, and the current
report. Focus remained limited to materially missing circuit-support BOM content for already-frozen
circuitry (decoupling, pull-ups/pull-downs, bias / support parts, RC support, protection placeholders,
and documented series/support components) plus connector-mapping consistency. Physical PCB
placement/routing was not reviewed.

#### Remaining findings

##### New findings

- None. Pass 17 did not identify any new connector-mapping contradictions or any new evidence-backed
  BOM/spec omissions for already-frozen circuitry.

##### Unchanged known unresolved items

- **Severity:** medium  
  **Files:** `design/Electronics/Actuation_Module/Design_Spec.md`, `design/Software/Actuation_Module/Design_Spec.md`, `design/Electronics/Consolidated_BOM.md`  
  **Issue:** The AM support-network definition for `ACTUATE_REQUEST`, `BOOT0`, and `NRST` remains unfrozen. The active AM docs still freeze the home-input RC support (`R4`, `C1`) but do not yet
  freeze the exact support treatment for the host request input and STM32 boot/reset service nets.  
  **Why it matters:** These nets still determine deterministic request-input state and STM32 boot/reset behaviour.  
  **Recommended fix:** Freeze the intended support network and add the corresponding BOM rows / refdes during later schematic capture.  
  **Status:** deferred schematic capture

- **Severity:** high  
  **Files:** `design/Electronics/Settings_Board/Design_Spec.md`, `design/Electronics/Settings_Board/Board_Layout.md`  
  **Issue:** The Settings Board LED topology remains underdefined between the documented MCP23017 anode-drive description and the `5V_MAIN` common-anode implementation.  
  **Why it matters:** The LED current path is still not fully frozen at the circuit-topology level.  
  **Recommended fix:** Freeze one topology and align the board docs / BOM during later schematic capture.  
  **Status:** deferred schematic capture

- **Severity:** medium  
  **Files:** `design/Electronics/Rotor/Design_Spec.md`  
  **Issue:** Rotor FDC2114 resonant front-end / unused-channel support definition remains deferred. The BOM now captures the already-evidenced local `SDA` / `SCL` pull-up placeholders and `VDD`
  bypass parts, but the channel front-end / full unused-channel definition is still intentionally not frozen.  
  **Why it matters:** The sensing chain is still not fully circuit-complete at the channel-support level.  
  **Recommended fix:** Complete the deferred support-network definition and add the resulting BOM content once approved.  
  **Status:** deferred schematic capture

- **Severity:** low  
  **Files:** `design/Electronics/Power_Module/Design_Spec.md`, `design/Electronics/Stator/Design_Spec.md`, `design/Electronics/Consolidated_BOM.md`  
  **Issue:** PM / Stator INA219 input RC filter exact sourced parts remain owner-selected. Both boards now capture local INA219 bypassing, but the exact `IN+` / `IN-` filter population is still not
  source-closed.  
  **Why it matters:** Those telemetry support networks are still not procurement-closed.  
  **Recommended fix:** Add the user-approved resistor/capacitor filter parts to the per-board and consolidated BOMs.  
  **Status:** needs user selection

- **Severity:** low  
  **Files:** `design/Electronics/Rotor/Design_Spec.md`, `design/Electronics/Consolidated_BOM.md`  
  **Issue:** Rotor local I2C pull-up exact sourcing placeholders remain unchanged.  
  **Why it matters:** The documented local sensor-bus support network is still not fully sourceable.  
  **Recommended fix:** User/owner to select the exact pull-up parts and update Rotor and consolidated BOMs.  
  **Status:** needs user selection

- **Severity:** low  
  **Files:** `design/Electronics/Rotor/Design_Spec.md`, `design/Electronics/Consolidated_BOM.md`  
  **Issue:** Rotor `1 µF` FDC2114 bypass / reservoir capacitor exact sourcing placeholders remain unchanged.  
  **Why it matters:** The documented FDC supply-support network is still not fully sourceable.  
  **Recommended fix:** User/owner to select the exact capacitor parts and update Rotor and consolidated BOMs.  
  **Status:** needs user selection

- **Severity:** low  
  **Files:** `design/Electronics/Extension/Design_Spec.md`, `design/Electronics/Consolidated_BOM.md`  
  **Issue:** Extension TVS / ESD exact device count, protected nets, footprint, and MPN remain owner-selected.  
  **Why it matters:** Protection intent is documented, but final implementation details are still open.  
  **Recommended fix:** User/owner to choose the exact protection implementation.  
  **Status:** needs user selection

- **Severity:** low  
  **Files:** `design/Electronics/Stator/Design_Spec.md`, `design/Electronics/Consolidated_BOM.md`  
  **Issue:** Stator TVS / ESD exact device count, protected nets, footprint, and MPN remain owner-selected.  
  **Why it matters:** Protection intent is documented, but final implementation details are still open.  
  **Recommended fix:** User/owner to choose the exact protection implementation.  
  **Status:** needs user selection

##### Connector consistency check

- **Severity:** info  
  **Files:** `design/Electronics/Stator/Board_Layout.md`, `design/Electronics/Encoder/Board_Layout.md`, `design/Electronics/Reflector/Board_Layout.md`, `design/Electronics/Extension/Board_Layout.md`,
  `design/Electronics/Settings_Board/Design_Spec.md`, `design/Electronics/Settings_Board/Board_Layout.md`, `design/Electronics/Actuation_Module/Design_Spec.md`,
  `design/Software/Actuation_Module/Design_Spec.md`  
  **Issue:** No new connector-mapping contradictions were found in this pass. The corrected Encoder JTAG numbering remains aligned with the Stator-owned contract, the Settings Board `J1` ↔ Stator
  `J13` harness remains consistent, the Reflector / Extension `J10` contract remains aligned with the Stator-owned definition, and the AM `J6` / `SW1` / `SW2` bootloader path remains consistent
  across hardware and firmware docs.  
  **Why it matters:** Confirms this pass did not uncover a new documented miswire trap on the reviewed interfaces.  
  **Recommended fix:** None.  
  **Status:** clean

#### Unsourced New Parts Requiring User Selection

- None newly identified in Pass 17.
- Existing owner-selected items remain unchanged:
  - PM / Stator INA219 input RC filter exact sourced parts
  - Rotor local I2C pull-up exact sourced parts
  - Rotor `1 µF` FDC2114 bypass / reservoir capacitor exact sourced parts
  - Extension TVS / ESD exact implementation
  - Stator TVS / ESD exact implementation

#### Pass Result

#### Pass 17 result: clean

Reason: no new connector-mapping contradictions were found and no new evidence-backed BOM/spec
omissions were found for already-frozen circuitry. The remaining open items are unchanged deferred
schematic-capture or owner-selection items already documented in prior passes, so the clean-pass
definition is met again. This is the second consecutive clean review pass after clean Pass 16.
