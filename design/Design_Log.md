# Enigma-NG Design Decision Log

This file records key architectural and component decisions made during the design of the Enigma-NG system. Each entry captures the decision taken, the rationale behind it, the alternatives that were considered, and any constraints or caveats that future designers should be aware of.

Entries are numbered sequentially as **DEC-NNN**. Where a decision supersedes a previous one, the earlier entry is updated with a cross-reference.

---

## DEC-001 — 3V3_ENIG Used Throughout; 3V3_SYSTEM Removed from BtB Interconnect

**Date:** 2025  
**Affects:** Power Module, Controller Board, Link-Alpha connector

**Decision:**  
The `3V3_SYSTEM` rail (sourced from the CM5 on the Controller Board) is **not** routed to the Power Module over the Link-Alpha BtB connector. All 3.3V logic within the Power Module (RJ45 LED anodes, I2C pull-ups, BATT_PRES_N pull-up, reset pull-up) is powered by `3V3_ENIG`, generated locally by the Power Module LDO (U7).

**Rationale:**  
- `3V3_SYSTEM` is a CM5-derived rail intended only for external peripheral interfaces (Ethernet, HDMI, USB 3.0 ports). Using it to power internal power-module logic would create a cross-domain dependency and complicate sequencing.
- Generating `3V3_ENIG` locally on the Power Module gives a clean, independently-controlled 3.3V supply that is always present when the Power Module is powered, regardless of CM5 boot state.
- Removing `3V3_SYSTEM` from the Link-Alpha connector freed pins 21–24, which were reallocated to extend the 5V_MAIN delivery cluster and GND return path.

**Alternatives Considered:**  
- Route `3V3_SYSTEM` from CM5 over Link-Alpha and use it for RJ45 logic. Rejected: cross-domain dependency, sequencing risk, wasted connector pins.
- Use a second small LDO on the Controller Board to produce a local 3.3V for CM5-adjacent logic. Rejected: unnecessary complexity given `3V3_ENIG` already exists.

**Impact on Link-Alpha Pin Map:**  
- Pins 21–22: Reassigned from 3V3_SYSTEM → **5V_MAIN** (supplemental power pins)
- Pins 23–24: Reassigned from 3V3_SYSTEM → **GND** (supplemental return path)
- Combined 5V_MAIN capacity: 18 pins × 0.5A = **9A** (was 16 pins = 8A)
- Diagnostic Bank-Alpha Pin 14: Reassigned from 3V3_SYSTEM → **GND**

---

## DEC-002 — PoE Option A2 Selected: Coilcraft POE600F-12LD

**Date:** 2025  
**Affects:** Power Module PoE subsystem, T2 transformer, TPS23730 feedback network

**Decision:**  
The PoE transformer T2 uses a **Coilcraft POE600F-12LD** off-the-shelf ACF transformer (12V output, 60W, 200kHz, ≥1500Vrms isolation, SMT package). The remainder of the PoE chain uses TPS2372-4 (802.3bt Type 4 PD interface) and TPS23730 (ACF controller), with TPS23730 feedback resistors adjusted for the 12V output.

**Rationale:**  
- Replaces a custom-wound transformer design (Option A: 15V, 8–16 week lead time, ~£35–46 BOM) with a catalogue part available from Coilcraft Direct.
- Off-the-shelf: **£3.54 qty-1, ~£1.86 volume**, in stock. Lead time: days not weeks.
- Same ACF topology as the custom design — only feedback resistors change. No PCB layout changes to high-current paths.
- 12V output falls within the TPS25980 eFuse UVLO/OVLO window (11V – 16.9V) with no additional buck stage needed.

**Alternatives Considered:**  
- **Option A (Custom T2, 15V):** Higher voltage headroom. Rejected: custom winding, long lead time, cost.
- **Option C (Silvertel Ag59812-LPB integrated module):** Higher integration, 95% efficiency, ~£19–27. Rejected: higher cost, fixed form factor, less flexibility for thermal management, vendor lock-in.
- **Kinetic Technologies KPM5912:** 85W, 93% efficiency. Rejected: not stocked by any UK/EU distributor.

**Key Parameters:**  
| Parameter | Value |
|---|---|
| Part | Coilcraft POE600F-12LD |
| Output | 12V nominal |
| Power | 60W (Type 4 PD, 72W class) |
| Isolation | ≥1500Vrms |
| Topology | Active Clamp Flyback (ACF) |
| Package | SMT |
| Price (qty-1) | ~£3.54 |

---

## DEC-003 — PoE Output 12V; OR-ing Priority Logic Required

**Date:** 2025  
**Affects:** Power Module PoE output, OR-ing diode (LM74700-Q1), eFuse input

**Decision:**  
PoE outputs 12V (not 15V) into the OR-ing stage. Because 12V < 15V USB-C input, passive OR-ing would always prefer USB-C and ignore PoE. Active enable logic is implemented: the TPS2372-4 `/PG` signal drives the LM74700-Q1 gate control low when PoE is live, disabling the USB-C path.

**Rationale:**  
- PoE is the primary field power source when no USB-C adapter is connected. It must not be silently overridden by USB-C passthrough.
- TPS2372-4 `/PG` (power good, active low) is a clean indicator of a live 802.3bt PoE session.
- LM74700-Q1 already provides the USB-C ideal diode function; gating its enable is a minimal-change approach.

**Constraints:**  
- PoE UVLO: 11V. eFuse UVLO: 11V. No margin at UVLO floor — PoE cable must be within 1V drop budget.
- eFuse ILIM utilisation at 12V worst case: 4.55A / 7A = **65.0%** ✓ (within 75% derating target).

---

## DEC-004 — Supercap Charge Current 0.5A Under PoE

**Date:** 2025  
**Affects:** LTC3350 supercap charger, PoE power budget

**Decision:**  
When running on PoE (802.3bt Type 4, 72W budget), the supercap charge current is reduced to **0.5A** (vs. up to 2A on USB-C/Battery). This limits peak PoE utilisation to 71.8% (51.7W / 72W).

**Rationale:**  
- Full 2A supercap charging on PoE would push utilisation to ~98%, leaving <2W margin for transient loads.
- 0.5A charge current charges the 4× 10F supercap bank in approximately 2 minutes from depleted.
- Normal system usage is expected to exceed 30–45 minutes per session (startup + configuration + use), making a 2-minute charge time acceptable.
- This limitation should be documented in the User Manual with guidance that maximum system load is not recommended during the initial PoE power-up window.

**Constraints:**  
- Steady-state PoE load (after caps charged): 48.9W / 72W = **67.9%** utilisation ✓

---

## DEC-005 — TPS25980 eFuse Replaces TPS259474L

**Date:** 2025  
**Affects:** Power Module eFuse (U1)

**Decision:**  
The input eFuse uses a **TPS25980** (7A ILIM, adjustable OVLO) rather than the originally considered TPS259474L (5.5A ILIM).

**Rationale:**  
- TPS259474L 5.5A limit is insufficient for worst-case USB-C 15V path at 75W: 75W / 15V = 5.0A + 10% derating = 5.5A — already at the device limit with no headroom.
- TPS25980 provides 7A ILIM and a fixed 16.9V OVLO, which neatly caps the battery charge voltage window.

**OVLO Constraint:**  
- eFuse OVLO is fixed at **16.9V**.
- BMS must be configured for **4.1V/cell maximum charge (16.4V for 4S)** to maintain a ≥0.5V margin.
- BMS configurations using 4.2V/cell (16.8V) are not compatible with this eFuse and must not be used.

---

## DEC-006 — STUSB4500 Negotiates 15V/5A (75W)

**Date:** 2025  
**Affects:** Power Module USB-C PD handshake (STUSB4500), USB-C adapter requirement

**Decision:**  
The STUSB4500 standalone PD sink is programmed to negotiate **15V/5A (75W)** from the wall adapter or USB-C PD source. Earlier documentation incorrectly stated 15V/3A.

**Rationale:**  
- 3A (45W) is insufficient for worst-case system load (CM5 at 25W + rotors + supercap charging).
- 5A (75W) provides headroom and aligns with the 75% derating target at the eFuse.
- Users must use a USB-C PD adapter rated for at least 75W (15V/5A or 20V/5A with appropriate negotiation cap).

---

## DEC-007 — Dual Interleaved LMQ61460-Q1 5V Buck (12A)

**Date:** 2025  
**Affects:** Power Module 5V Buck (U2A/U2B)

**Decision:**  
Two **LMQ61460-Q1** buck regulators are used in a **dual interleaved** configuration, providing a combined **12A** output at 5V. Earlier documentation referenced a single LM61460-Q1 (6A).

**Rationale:**  
- Single 6A device is insufficient for CM5 at 25W (5A) + other 5V loads.
- Interleaved dual phase reduces input/output ripple and distributes thermal load.
- 12A capacity aligns with the 9A+ delivery capability of the updated Link-Alpha pin cluster.

---

## DEC-008 — TPS25750 Emulates 5V/5A PD Profile to CM5

**Date:** 2025  
**Affects:** CM5 USB-C PD emulator (TPS25750)

**Decision:**  
The TPS25750 PD emulator advertises a **5V/5A** profile to the CM5 internal USB-C port.

**Rationale:**  
- The CM5 Linux OS will generate a "low power" warning if PD negotiation does not complete at or above 5V/5A (25W).
- 5V/5A is the minimum advertisement to suppress this warning and allow unrestricted CPU/GPU boost operation.

---

## DEC-009 — Diagnostic Bank-Alpha Pin 14 Reassigned to GND

**Date:** 2025  
**Affects:** Controller Board Diagnostic Bank-Alpha connector

**Decision:**  
Diagnostic Bank-Alpha pin 14 is reassigned from `3V3_SYSTEM` to **GND**, following the removal of the `3V3_SYSTEM` rail from all BtB interconnects (see DEC-001).

**Rationale:**  
- `3V3_SYSTEM` is no longer available at the Power Module side of this debug header.
- Assigning pin 14 to GND gives the diagnostic header a clean reference without leaving a floating or unconnected pin.

---

## DEC-010 — INC-14 DEFERRED: Diagnostic Bank ESD Protection (Post-Prototype)

**Date:** 2025  
**Status:** ⚠️ DEFERRED — Accepted risk for prototype stage  
**Affects:** Controller Board Diagnostic Bank-Alpha / Bank-Beta connectors

**Decision:**  
ESD protection on the diagnostic bank connectors is **deferred** to post-prototype evaluation. No TVS diodes or series resistors are added to diagnostic header signals at this stage.

**Rationale:**  
- Diagnostic headers are internal, accessed only by engineers with ESD precautions during development.
- Adding ESD protection to every diagnostic pin adds cost, board space, and complexity before there is validated evidence that it is needed.
- Risk accepted for prototype: controlled lab environment, trained operators, no field exposure.

**Post-Prototype Action Required:**  
- During first prototype test phase, evaluate signal integrity and ESD sensitivity on diagnostic lines.
- If any diagnostic lines are exposed to field conditions (e.g., external test connectors), add series 33Ω + TVS per line.
- Document findings and update this log with the final resolution.

---

## DEC-011 — All Power Rails on Power Module; 3V3_ENIG Serves Rotor Stack

**Date:** 2025  
**Status:** ✅ RESOLVED  
**Affects:** Power Module islands, Controller Board routing, rotor stack power source

**Decision:**  
All power rails are generated on the **Power Module**. The Controller Board's role is purely to **route** power rails onward to downstream boards — it does not generate any rails itself. The rotor stack is powered by the existing **3V3_ENIG** rail (TPS7A8333P LDO, 3A). There is no separate Rotor Buck; the erroneous "3.3V/5A Rotor Buck" specification was a confusion with the 5V/5A CM5 rail and has been removed.

**Rationale:**  
- Centralising all power generation on the Power Module simplifies thermal management (all heat dissipation in one shielded enclosure with dedicated thermal zone).
- Reduces the risk of ground loops and cross-domain sequencing issues.
- The Controller Board as a routing layer keeps its design cleaner and easier to revise independently.
- 3V3_ENIG (3A) covers all 3.3V consumers: CPLDs, USB-JTAG, I2C logic, status indicators, and the rotor stack.
- ROTOR_EN (CM5 GPIO 16) enables/disables the 3V3_ENIG LDO for sequenced rotor power-up — a control signal only.

**Architectural Rule (permanent):**  
> All power rails are generated on the Power Module. The Controller Board routes rails to downstream boards only. No buck converters, LDOs, or other power-generating components belong on the Controller Board.

**Files Updated:**  
- `README.md`: Removed erroneous "Dedicated 3.3V/5A Buck" from Controller Board section; 3V3_ENIG correctly listed as Power Module output serving CPLDs, logic, and rotor stack.
- `Power_Module/Design_Spec.md`: 3V3_ENIG scope updated to include rotor stack; 3-island Power Plane retained.
- `Controller/Design_Spec.md`: ROTOR_EN clarified as LDO enable signal to Power Module.
- `Rotor/Design_Spec.md`: Power source updated from "Controller Board Island C" to "Power Module 3V3_ENIG rail".

**Previously Conflicting References (now corrected):**  
- `README.md` placed the Rotor Buck under the Controller Board section.
- `Rotor/Design_Spec.md` said "sourced from the Controller Board's Island C".

---

## DEC-012 — U4 TPS25750 Replaced with TPS25751DREFR (NRND Resolution)

**Date:** 2026-04-03  
**Status:** ✅ RESOLVED  
**Affects:** Power Module U4, schematic, PCB footprint

**Decision:**  
Replace **TPS25750** (NRND — Not Recommended for New Designs) with **TPS25751DREFR** (PD3.1 certified DRP controller, WQFN-38 6×4mm).

**Rationale:**  
- PD emulation for U4 is required: the Raspberry Pi CM5 must negotiate a 5V/5A (25W) contract from the USB-C PD source to prevent the OS from issuing under-voltage warnings and throttling the system.
- The TPS25751D variant includes the integrated 20V/5A bi-directional power path and a 5V/3A source switch in one package — appropriate for DRP operation that can advertise and deliver the 5V/5A profile to the CM5.
- TPS25751 is USB-IF PD3.1 certified (TID#10306); TPS25750 was PD2.0 only and is NRND.
- STUSB4500 (U5) handles the USB-C sink path; TPS25751 (U4) handles the source/emulation path. These are separate and complementary roles.

**Impact:**  
- ⚠️ **Package change**: TPS25750 was QFN-28; TPS25751DREFR is WQFN-38 6×4mm. Schematic symbol and PCB footprint must both be updated.
- Mouser: `595-TPS25751DREFR`; DigiKey: `TPS25751DREFR-ND`.

---

## DEC-013 — L3 EMI Inductor Changed to Bourns SRP1265A-100M

**Date:** 2026-04-03  
**Status:** ✅ RESOLVED  
**Affects:** Power Module L3, PCB footprint

**Decision:**  
Replace **Würth 7447789100** with **Bourns SRP1265A-100M** as L3 (EMI DM Pi-filter inductor).

**Rationale:**  
- Würth 7447789100 is not available in any public distributor catalog (not found at DigiKey, Mouser, Farnell, or on the Würth public website). Sourcing without a Würth rep contact is not feasible.
- Bourns SRP1265A-100M is a direct functional equivalent: 10µH, **15.5A Isat** (exceeds 14.5A target with 21% headroom), DCR=16.5mΩ max (better than the original 20mΩ spec), shielded molded SMD.
- Widely stocked: Farnell ~2,741 pcs; Mouser (`652-SRP1265A-100M`); DigiKey (`SRP1265A-100MCT-ND`).

**Impact:**  
- ⚠️ **Package footprint change**: SRP1265A-100M is 13.5×12.5×6.2mm vs 7447789100's 12.5×12.5×6.0mm. PCB land pattern for L3 must use the Bourns 13.5×12.5mm footprint. Clearance to adjacent components should be checked during layout.

---

## INC Review History

This section records all INC (inconsistency) items tracked during the design process. Each item was identified during design review, verified, and resolved. All items are closed.

| INC | Area | Description | Original Value | Corrected Value | Status |
|-----|------|-------------|----------------|-----------------|--------|
| INC-01 | Power Module eFuse | UVLO/OVLO thresholds inconsistent between README and Design_Spec | README: 12V UVLO / 16V OVP | 11.0V UVLO / 16.9V OVLO (per Design_Spec §5) | ✅ Resolved — README corrected |
| INC-02 | Power Module eFuse | eFuse current limit insufficient for 75W USB-C path. TPS259474L max 5.5A with no headroom at 5.0A worst case | TPS259474L (5.5A ILIM) | TPS25980 (7A ILIM, 16.9V OVLO, VQFN-24). See DEC-005 | ✅ Resolved — DEC-005 |
| INC-03 | Power Module 5V Buck | Single buck insufficient for CM5 25W + other loads | LM61460-Q1 (6A) | Dual LMQ61460-Q1 interleaved (12A total). See DEC-007 | ✅ Resolved — DEC-007 |
| INC-04 | Power Module PD Emulator | TPS25750 PDO listed as "5V/6A" — not a valid USB-C PD current at 5V | "5V/6A" (invalid) | 5V/5A (25W maximum at 5V per USB-C PD spec). See DEC-008 | ✅ Resolved — DEC-008 |
| INC-05 | Link-Alpha BtB Connector | 3V3_SYSTEM routed from CM5 to Power Module on pins 21–24 for RJ45 LED anodes — cross-domain dependency | 3V3_SYSTEM on pins 21–24 (input from CM5) | Removed. 3V3_ENIG generated locally on Power Module. Pins 21–22 → 5V_MAIN; pins 23–24 → GND. See DEC-001 | ✅ Resolved — DEC-001 |
| INC-06 | Power Module PoE | Ag5300 PoE module only supports 802.3at (25.5W PD) — insufficient for full system load ~42W | Ag5300 (802.3at, 25.5W) | Discrete: TPS2372-4 + TPS23730 + Coilcraft POE600F-12LD (802.3bt Type 4, 51W). See DEC-002 | ✅ Resolved — DEC-002 |
| INC-07 | Power Module / Controller | "3.3V/5A Rotors Buck" placed on Controller Board in README; contradicts central power generation principle | README: Rotor Buck on Controller Board | All rails on Power Module. Rotor stack uses 3V3_ENIG. See DEC-011 | ✅ Resolved — DEC-011 |
| INC-08 | Power Module I2C | I2C pull-ups (SDA/SCL 4.7kΩ) tied to 3V3_SYSTEM — invalid once 3V3_SYSTEM removed from Power Module | Pull-ups to 3V3_SYSTEM | Pull-ups moved to 3V3_ENIG | ✅ Resolved |
| INC-09 | Power Module Design_Spec | Internal conflict: §1 stated "16.5V OVP"; §5 stated "17V OVLO" — two different values in same document | §1: 16.5V OVP | 16.9V OVLO (consistent with TPS25980 fixed OVLO variant; §1 corrected) | ✅ Resolved — auto-resolved (16.5V reference not found in any current file) |
| INC-10 | Power Module BOM | Reference designator collision: R1–R3 used for both eFuse ladder resistors AND I2C/reset pull-ups in the same document | R1–R3 dual-use | eFuse ladder: R1/R2/R3. I2C pull-ups: R7/R8. Reset pull-up: R9 | ✅ Resolved — designators renamed |
| INC-11 | Power Module Battery | BATT_PRES_N pull-up R6 tied to 3V3_SYSTEM — invalid once 3V3_SYSTEM removed | R6 pull-up to 3V3_SYSTEM | R6 pull-up moved to 3V3_ENIG | ✅ Resolved |
| INC-12 | Link-Alpha BtB Connector | Power cluster labelled "6A Delivery Cluster" — outdated after dual 12A buck upgrade and pin reallocation | "6A Delivery Cluster" (16 pins) | 9A delivery (18 pins × 0.5A/pin after reallocation). Label updated | ✅ Resolved |
| INC-13 | Power Module USB-C | STUSB4500 specified to negotiate 15V/3A (45W) — only 56.7% eFuse utilisation violation at worst-case 42.5W load | STUSB4500: 15V/3A (45W) | STUSB4500: 15V/5A (75W). See DEC-006 | ✅ Resolved — DEC-006 |
| INC-14 | Controller Diagnostic Banks | Diagnostic Bank-Alpha and Bank-Beta have no ESD protection; exposed ENIG pads treated as external interfaces | No ESD on diagnostic banks | Deferred to post-prototype. Accept risk for prototype stage. See DEC-010 | ✅ Resolved — DEC-010 (deferred) |
| INC-15 | Controller/Power Module | Internal conflict in Board_Layout.md: bullet list said I2C=pins 35–40, 3V3_ENIG=pins 41–44; ASCII diagram said I2C=35–38, 3V3_ENIG=39–44 | Bullets: I2C 35–40; 3V3_ENIG 41–44 | ASCII diagram authoritative: I2C 35–38, 3V3_ENIG 39–44 (6 pins at 51.4% utilisation) | ✅ Resolved — ASCII diagram is authoritative |
| INC-16 | Board_Layout.md ETH LED diagram | ETH LED diagram showed PIN 27 = ETH_LED_ACT; main pin map shows pins 27–30 = GND Isolation Moat | Diagram: PIN 27 = ETH_LED_ACT | Correct: PIN 26 = ETH_LED_ACT; PIN 27 = GND Moat | ✅ Resolved |
| INC-17 | Power Module Battery | eFuse OVLO margin: with 16.9V OVLO and 4.2V/cell BMS (16.8V max), only 0.1V margin — risk of nuisance trips | BMS max 4.2V/cell (16.8V); OVLO 16.9V; margin 0.1V | BMS must use 4.1V/cell max (16.4V total for 4S), giving 0.5V margin. Added to Design_Spec §2. See DEC-005 | ✅ Resolved |
| INC-18 | Power Module Design_Spec | Battery BMS charge voltage not specified in design spec — required to protect against OVLO nuisance trips | No BMS charge spec | Added: "BMS max charge voltage = 4.1V/cell (16.4V for 4S)" to Power Module §2 Battery Interface | ✅ Resolved |
| INC-19 | Power Module PoE | Ag5300/Ag53000 is 802.3at only (25.5W PD). No 802.3bt Type 4 PCB module found. Architecture change required for 51W PoE | Ag5300/Ag53000 (802.3at SIL module) | Discrete two-stage: TPS2372-4 (PD) + TPS23730 + POE600F-12LD (ACF transformer). See DEC-002 | ✅ Resolved — DEC-002 |
| INC-20 | Power Module Supercap | Supercap charge path had no current limiting — would cause excessive inrush and violate 75% utilisation rule under PoE | Supercap directly on 15V bus | LTC3350 soft-charge via RICHARGE resistor; 0.5A limit under PoE. See DEC-004 | ✅ Resolved — DEC-004 |
| INC-21 | Power Module J2 | Component selection locked: RJ45 MagJack | — | Würth 7499111121A (SMT, shielded, 2-LED, 10/100/1000) | ✅ Locked |
| INC-22 | Power Module ESD | Component selection locked: Ethernet ESD arrays | — | 2× TI TPD4E1U06DBVR (0.8pF, ±15kV, −40°C to +125°C) per port | ✅ Locked |
| INC-23 | Power Module Bob Smith | Component selection locked: Bob Smith termination network | — | 4× 75Ω 0402 ±1% resistors + 1× 10nF Y1-class capacitor to GND_CHASSIS | ✅ Locked |

---

## Board Connector Inventory

The following table lists all physical connectors across every board in the Enigma-NG system. This list should be manually verified against the original intended design to confirm no specification changes have inadvertently altered connector placement, orientation, or mating requirements.

### Power Module

| Ref | Description | Part / Series | MPN | Mouser PN | DigiKey PN | Notes |
|-----|-------------|---------------|-----|-----------|------------|-------|
| J1 | Link-Alpha BtB — 80-pin socket to Controller Board | Samtec ERM8-040-05.0-S-DV-K-TR | ERM8-040 | 200-ERM8040050SDVKTR | SAM12064-ND | Male header (ERM8). Mating female on Controller (ERF8). Gold-plated, 0.5A/pin |
| J2 | RJ45 MagJack with integrated magnetics | Würth 7499111121A | 7499111121A | 710-7499111121A | 732-2174-ND | SMT, shielded, 2 integrated LEDs (green/yellow), 10/100/1000 PoE compatible |
| J3 | Battery connector — 5-pin Micro-Fit 3.0 THT vertical | Molex 43650-0519 | 43650-0519 | 538-43650-0519 | WM7843-ND ⚠️ verify | 5-circuit, 1-row, gold contacts, board lock, 3mm pitch. ⚠️ MPN corrected (43045-0512 does not exist) |

### Controller Board

| Ref | Description | Part / Series | MPN | Mouser PN | DigiKey PN | Notes |
|-----|-------------|---------------|-----|-----------|------------|-------|
| J1 | Link-Alpha BtB — 80-pin socket to Power Module | Samtec ERF8-040-05.0-S-DV-K-TR | ERF8-040 | 200-ERF8040050SDVKTR | SAM8621-ND ⚠️ verify | Female socket (ERF8). Mating male on Power Module (ERM8) |
| J2 | Link-Beta BtB — 80-pin header to Stator Board | Samtec ERM8-040-05.0-S-DV-K-TR | ERM8-040 | 200-ERM8040050SDVKTR | SAM12064-ND | Male header. Encryption/JTAG exit. Provides JTAG, Reset, 3V3_ENIG to Stator |
| J3 | USB 3.0 — Dual-stacked Type-A port | Molex 48406-0003 | 48406-0003 | 538-0484060003 | WM1394-ND | Dual-stack Type-A, 5.0mm protrusion through chassis |
| J4 | HDMI — Full-size Type-A | TE Connectivity 2007435-1 | 2007435-1 | 571-2007435-1 | A125057-ND | Full-size HDMI Type-A, 5.0mm protrusion through chassis |
| — | Diagnostic Bank-Alpha | 2×8 ENIG Gold looped probe pads | — | — | — | 2.54mm pitch, placed behind BtB header. Not a separate connector; probed directly with logic analyser clips |
| — | Diagnostic Bank-Beta | 2×10 ENIG Gold looped probe pads | — | — | — | 2.54mm pitch, L1 layer. Monitors 12-bit Sniffer, JTAG, SYS_RESET_N |
| — | JTAG Daughterboard link (to FT232H board) | 1×6 power/USB header + 1×10 JTAG header | — | — | — | 2.54mm ENIG headers. 1:1 signal-to-ground ratio on JTAG header. USB 2.0 from CM5 |

### Stator Board

| Ref | Description | Part / Series | MPN | Mouser PN | DigiKey PN | Notes |
|-----|-------------|---------------|-----|-----------|------------|-------|
| J1 | Link-Beta BtB — 80-pin socket from Controller Board | Samtec ERM8-040-05.0-S-DV-K-TR | ERM8-040 | 200-ERM8040050SDVKTR | SAM12064-ND | Receives JTAG, Reset, 3V3_ENIG from Controller |
| J2 | Rotor/Encoder power and data — 40-pin shrouded box header | Molex 22-23-2401 (2×20, 2.54mm) | 22-23-2401 | 538-22-23-2401 | WM2921-ND | THT, shrouded, keyed. Power (3V3_ENIG/GND), ENC_DATA, JTAG to each encoder slot |
| J3 | Reflector/Extension — 20-pin shrouded box header | Molex 22-23-2201 (2×10, 2.54mm) | 22-23-2201 | 538-22-23-2201 | WM2911-ND | THT, shrouded. Power (3V3_ENIG/GND), ENC_DATA, TDO_Return |
| — | JTAG Aux header | 2×5 2.54mm shrouded | — | — | — | Pin pattern: GND\|TCK\|GND\|TMS\|GND\|TDI\|GND\|RST\|GND |

### Rotor Board (×30)

| Ref | Description | Part / Series | MPN | Mouser PN | DigiKey PN | Notes |
|-----|-------------|---------------|-----|-----------|------------|-------|
| J1 | Stator edge-rate connector — 20-pin | Samtec ERM8-020-05.0-S-DV-K-TR | ERM8-020 | 200-ERM8020050SDVKTR | SAM12065-ND | 0.8mm pitch edge-rate. ENIG pads for low-insertion-force hot-swap mating. Rated for high mating cycles |

### Encoder Board

| Ref | Description | Part / Series | MPN | Mouser PN | DigiKey PN | Notes |
|-----|-------------|---------------|-----|-----------|------------|-------|
| J1 | Plugboard jack sockets | 3.5mm / 4mm through-hole jacks | ??? | ??? | ??? | ⚠️ Part not yet selected — physical plug/jack type TBD |
| J2 | Data link to Stator — 16-pin shrouded box header | Molex 22-23-2161 (2×8, 2.54mm) | 22-23-2161 | 538-22-23-2161 | WM2907-ND | Mating connector for Stator J2 |
| J3 | Diagnostic looped probe pads | 2×8 ENIG Gold pads | — | — | — | 2.54mm pitch. Not a separate connector; probed directly |

### Reflector Board

| Ref | Description | Part / Series | MPN | Mouser PN | DigiKey PN | Notes |
|-----|-------------|---------------|-----|-----------|------------|-------|
| J1 | Interconnect from Stator — 16-pin shrouded box header | Molex 22-23-2161 (2×8, 2.54mm) | 22-23-2161 | 538-22-23-2161 | WM2907-ND | Mating connector for Stator J3 |
| J2 | Diagnostic looped probe pads | 2×8 ENIG Gold pads | — | — | — | 2.54mm pitch. Not a separate connector; probed directly |

### Extension Board

| Ref | Description | Part / Series | Notes |
|-----|-------------|---------------|-------|
| J1 | Interconnect from Stator | 20-pin 2.54mm shrouded | Mirrors Reflector/Extension slot on Stator J3 |
| J2 | Diagnostic looped probe pads | 2×8 ENIG Gold pads | Same pattern as Reflector J2 |

### JTAG Daughterboard (FT232H)

| Ref | Description | Part / Series | Notes |
|-----|-------------|---------------|-------|
| J1 | USB 2.0 link from CM5 | 1×6 2.54mm header (power + USB) | Connects to Controller Board FT232H power/USB header |
| J2 | JTAG chain output | 1×10 2.54mm shielded header | Drives HID Encoder CPLDs. 1:1 GND interleave on all JTAG signals |

---

> **Note for manual review:** Items marked `???` or `⚠️ verify` require confirmation before the BOM is finalised for procurement. In particular: Encoder J1 plug/jack type has not been selected; Controller J1 (ERF8) DigiKey PN SAM8621-ND should be confirmed; Power Module J3 (43650-0519) DigiKey WM7843-ND should be verified at digikey.co.uk.
