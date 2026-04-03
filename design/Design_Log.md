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

## DEC-011 — PENDING: Rotor Buck Placement (Controller vs Power Module)

**Date:** 2025  
**Status:** ⚠️ PENDING — Location not confirmed  
**Affects:** 3.3V/5A Rotor supply

**Decision:**  
Location of the 3.3V/5A Rotor Buck regulator has not been confirmed.

**Conflicting Evidence:**  
- `README.md` places the Rotor Buck on the **Controller Board**.
- `Power_Module/Design_Spec.md` §1 (power islands) lists "3.3V/5A Rotors" as a Power Module island.

**Action Required:**  
Confirm intended physical location of the Rotor Buck and update all references consistently.  
Options:  
1. **Controller Board** — Keeps rotor power generation close to the Stator Board (downstream consumer). Reduces long 3.3V runs over Link-Beta.  
2. **Power Module** — Centralises all power conversion in one module. Simpler cabling if rotor demand is stable.

Update this entry with the final decision and rationale when confirmed.
