# Enigma-NG Design Decision Log

**Status:** Active
**Project:** Enigma-NG
**Author:** Izzyonstage & GitHub Copilot
**Version:** v1.0.0
**Associated Hardware Revision:** Rev A
**Last Updated:** 2026-04-05

This file records key architectural and component decisions made during the design of the Enigma-NG system. Each entry captures the decision taken, the rationale behind it, the alternatives that were
considered, and any constraints or caveats that future designers should be aware of.

Entries are numbered sequentially as **DEC-NNN**. Where a decision supersedes a previous one, the earlier entry is updated with a cross-reference.

---

## DEC-001 — 3V3_ENIG Used Throughout; 3V3_SYSTEM Removed from BtB Interconnect

- **Status:** Decided
- **Date:** 2025
- **Category:** Electrical
- **Area:** Power Module, Controller Board, Link-Alpha connector

### Decision

The `3V3_SYSTEM` rail (sourced from the CM5 on the Controller Board) is **not** routed to the Power Module over the Link-Alpha BtB connector. All 3.3V logic within the Power Module (RJ45 LED anodes,
I2C pull-ups, BATT_PRES_N pull-up, reset pull-up) is powered by `3V3_ENIG`, generated locally by the Power Module LDO (U7).

### Rationale

- `3V3_SYSTEM` is a CM5-derived rail intended only for external peripheral interfaces (Ethernet, HDMI, USB 3.0 ports). Using it to power internal power-module logic would create a cross-domain

  dependency and complicate sequencing.

- Generating `3V3_ENIG` locally on the Power Module gives a clean, independently-controlled 3.3V supply that is always present when the Power Module is powered, regardless of CM5 boot state.
- Removing `3V3_SYSTEM` from the Link-Alpha connector freed pins 21–24, which were reallocated to extend the 5V_MAIN delivery cluster and GND return path.

### Alternatives Considered

- Route `3V3_SYSTEM` from CM5 over Link-Alpha and use it for RJ45 logic. Rejected: cross-domain dependency, sequencing risk, wasted connector pins.
- Use a second small LDO on the Controller Board to produce a local 3.3V for CM5-adjacent logic. Rejected: unnecessary complexity given `3V3_ENIG` already exists.

### Impact

- Pins 21–22: Reassigned from 3V3_SYSTEM → **5V_MAIN** (supplemental power pins)
- Pins 23–24: Reassigned from 3V3_SYSTEM → **GND** (supplemental return path)
- Combined 5V_MAIN capacity: 18 pins × 0.5A = **9A** (was 16 pins = 8A)
- Diagnostic Bank-Alpha Pin 14: Reassigned from 3V3_SYSTEM → **SW_LED_CTRL (GPIO 24)** (subsequently updated; see DEC-009)

---

## DEC-002 — PoE Option A2 Selected: Coilcraft POE600F-12LD

- **Status:** Decided
- **Date:** 2025
- **Category:** Electrical
- **Area:** Power Module PoE subsystem, T2 transformer, TPS23730 feedback network

### Decision

The PoE transformer T2 uses a **Coilcraft POE600F-12LD** off-the-shelf ACF transformer (12V output, 60W, 200kHz, ≥1500Vrms isolation, SMT package). The remainder of the PoE chain uses TPS2372-4
(802.3bt Type 4 PD interface) and TPS23730 (ACF controller), with TPS23730 feedback resistors adjusted for the 12V output.

### Rationale

- Replaces a custom-wound transformer design (Option A: 15V, 8–16 week lead time, ~£35–46 BOM) with a catalogue part available from Coilcraft Direct.
- Off-the-shelf: **£3.54 qty-1, ~£1.86 volume**, in stock. Lead time: days not weeks.
- Same ACF topology as the custom design — only feedback resistors change. No PCB layout changes to high-current paths.
- 12V output falls within the TPS25980 eFuse UVLO/OVLO window (11V – 16.9V) with no additional buck stage needed.

### Alternatives Considered

- **Option A (Custom T2, 15V):** Higher voltage headroom. Rejected: custom winding, long lead time, cost.
- **Option C (Silvertel Ag59812-LPB integrated module):** Higher integration, 95% efficiency, ~£19–27. Rejected: higher cost, fixed form factor, less flexibility for thermal management, vendor

  lock-in.

- **Kinetic Technologies KPM5912:** 85W, 93% efficiency. Rejected: not stocked by any UK/EU distributor.

### Key Parameters

| Parameter | Value |
| --- | --- |
| Part | Coilcraft POE600F-12LD |
| Output | 12V nominal |
| Power | 60W (Type 4 PD, 72W class) |
| Isolation | ≥1500Vrms |
| Topology | Active Clamp Flyback (ACF) |
| Package | SMT |
| Price (qty-1) | ~£3.54 |

---

## DEC-003 — PoE Output 12V; OR-ing Priority Logic Required

- **Status:** Decided
- **Date:** 2025
- **Category:** Electrical
- **Area:** Power Module PoE output, OR-ing diode (LM74700-Q1), eFuse input

### Decision

PoE outputs 12V (not 15V) into the OR-ing stage. Because 12V < 15V USB-C input, passive OR-ing would always prefer USB-C and ignore PoE. Active enable logic is implemented: the TPS2372-4 `/PG` signal
drives the LM74700-Q1 gate control low when PoE is live, disabling the USB-C path.

### Rationale

- PoE is the primary field power source when no USB-C adapter is connected. It must not be silently overridden by USB-C passthrough.
- TPS2372-4 `/PG` (power good, active low) is a clean indicator of a live 802.3bt PoE session.
- LM74700-Q1 already provides the USB-C ideal diode function; gating its enable is a minimal-change approach.

### Constraints

- PoE UVLO: 11V. eFuse UVLO: 11V. No margin at UVLO floor — PoE cable must be within 1V drop budget.
- eFuse ILIM utilisation at 12V worst case: 4.67A / 7A = **66.7%** ✓ (within 75% derating target).

---

## DEC-004 — Supercap Charge Current 0.5A Under PoE

- **Status:** Decided
- **Date:** 2025
- **Category:** Electrical
- **Area:** LTC3350 supercap charger, PoE power budget

### Decision

When running on PoE (802.3bt Type 4, 72W budget), the supercap charge current is reduced to **0.5A** (vs. up to 2A on USB-C/Battery).
This limits peak PoE utilisation to 73.9% (53.2W / 72W) — within the 75% design rule ✓ (see Certification_Evidence §3.5).

### Rationale

- Full 2A supercap charging on PoE would push utilisation to ~98%, leaving <2W margin for transient loads.
- 0.5A charge current charges the 6× 22F supercap bank in approximately 3 minutes from depleted.
- Normal system usage is expected to exceed 30–45 minutes per session (startup + configuration + use), making a 2-minute charge time acceptable.
- This limitation should be documented in the User Manual with guidance that maximum system load is not recommended during the initial PoE power-up window.

### Constraints

- Steady-state PoE load (after caps charged): 50.3W / 72W = **69.9%** utilisation ✓

---

## DEC-005 — TPS25980 eFuse Replaces TPS259474L

- **Status:** Decided
- **Date:** 2025
- **Category:** Electrical
- **Area:** Power Module eFuse (U1)

### Decision

The input eFuse uses a **TPS25980** (7A ILIM, silicon-fixed 16.9V OVLO) rather than the originally considered TPS259474L (5.5A ILIM).

### Rationale

- TPS259474L 5.5A limit is insufficient for worst-case USB-C 15V path at 75W: 75W / 15V = 5.0A + 10% derating = 5.5A — already at the device limit with no headroom.
- TPS25980 (TPS259804ONRGER) provides 7A ILIM (programmed via R3 = 210 Ω) and silicon-fixed 16.9V OVLO, which neatly caps the battery charge voltage window.

### OVLO Constraint

- eFuse OVLO is **16.9V silicon-fixed** (TPS259804ONRGER — no external programming resistor).
- BMS must be configured for **4.1V/cell maximum charge (16.4V for 4S)** to maintain a ≥0.5V margin.
- BMS configurations using 4.2V/cell (16.8V) are not compatible with this eFuse and must not be used.

---

## DEC-006 — STUSB4500 Negotiates 15V/5A (75W)

- **Status:** Decided
- **Date:** 2025
- **Category:** Electrical
- **Area:** Power Module USB-C PD handshake (STUSB4500), USB-C adapter requirement

### Decision

The STUSB4500 standalone PD sink is programmed to negotiate **15V/5A (75W)** from the wall adapter or USB-C PD source. Earlier documentation incorrectly stated 15V/3A.

### Rationale

- 3A (45W) is insufficient for worst-case system load (CM5 at 25W + rotors + supercap charging).
- 5A (75W) provides headroom and aligns with the 75% derating target at the eFuse.
- Users must use a USB-C PD adapter rated for at least 75W (15V/5A or 20V/5A with appropriate negotiation cap).

---

## DEC-007 — Dual Interleaved LMQ61460-Q1 5V Buck (12A)

- **Status:** Decided
- **Date:** 2025
- **Category:** Electrical
- **Area:** Power Module 5V Buck (U2A/U2B)

### Decision

Two **LMQ61460-Q1** buck regulators are used in a **dual interleaved** configuration, providing a combined **12A** output at 5V. Earlier documentation referenced a single LM61460-Q1 (6A).

### Rationale

- Single 6A device is insufficient for CM5 at 25W (5A) + other 5V loads.
- Interleaved dual phase reduces input/output ripple and distributes thermal load.
- 12A capacity aligns with the 9A+ delivery capability of the updated Link-Alpha pin cluster.

---

## DEC-008 — TPS25750 Emulates 5V/5A PD Profile to CM5

> ⚠️ **Superseded by DEC-012** — TPS25750 replaced with TPS25751DREFR. See DEC-012.

- **Status:** Superseded by DEC-012
- **Date:** 2025
- **Category:** Electrical
- **Area:** CM5 USB-C PD emulator (TPS25750)

### Decision

The TPS25750 PD emulator advertises a **5V/5A** profile to the CM5 internal USB-C port.

### Rationale

- The CM5 Linux OS will generate a "low power" warning if PD negotiation does not complete at or above 5V/5A (25W).
- 5V/5A is the minimum advertisement to suppress this warning and allow unrestricted CPU/GPU boost operation.

---

## DEC-009 — Diagnostic Bank-Alpha Pin 14 Reassigned to SW_LED_CTRL

- **Status:** Decided
- **Date:** 2025 (GND); superseded by final design (SW_LED_CTRL)
- **Category:** Electrical
- **Area:** Controller Board Diagnostic Bank-Alpha connector

### Decision

Diagnostic Bank-Alpha pin 14 was initially reassigned from `3V3_SYSTEM` to **GND**, following the removal of the `3V3_SYSTEM` rail from all BtB interconnects (see DEC-001).
In the subsequent design pass that added `SW_LED_CTRL` (GPIO 24) to the Link-Alpha signal set,
pin 14 was reallocated to **SW_LED_CTRL** to expose the LED-arbitration handshake at the diagnostic header.

**Final assignment:** Bank-Alpha Pin 14 = `SW_LED_CTRL` (GPIO 24, CTRL → PM, HIGH = CM5 in control of SW1 RGB LED).

### Rationale

- `3V3_SYSTEM` is no longer available at the Power Module side of this debug header.
- `SW_LED_CTRL` is a useful diagnostic probe point — it shows whether the CM5 has taken control of the RGB LED from the hardware oscillator fallback path.
- GND is freely available on pins 19–20; a redundant GND at pin 14 added no diagnostic value.

---

## DEC-010 — INC-14 DEFERRED: Diagnostic Bank ESD Protection (Post-Prototype)

- **Status:** Deferred — Accepted risk for prototype stage
- **Date:** 2025
- **Category:** Electrical
- **Area:** Controller Board Diagnostic Bank-Alpha / Bank-Beta connectors

### Decision

ESD protection on the diagnostic bank connectors is **deferred** to post-prototype evaluation. No TVS diodes or series resistors are added to diagnostic header signals at this stage.

### Rationale

- Diagnostic headers are internal, accessed only by engineers with ESD precautions during development.
- Adding ESD protection to every diagnostic pin adds cost, board space, and complexity before there is validated evidence that it is needed.
- Risk accepted for prototype: controlled lab environment, trained operators, no field exposure.

### Post-Prototype Action Required

- During first prototype test phase, evaluate signal integrity and ESD sensitivity on diagnostic lines.
- If any diagnostic lines are exposed to field conditions (e.g., external test connectors), add series 33Ω + TVS per line.
- Document findings and update this log with the final resolution.

---

## DEC-011 — All Power Rails on Power Module; 3V3_ENIG Serves Rotor Stack

- **Status:** ✅ RESOLVED
- **Date:** 2025
- **Category:** Electrical
- **Area:** Power Module islands, Controller Board routing, rotor stack power source

### Decision

All power rails are generated on the **Power Module**. The Controller Board's role is purely to **route** power rails onward to downstream boards — it does not generate any rails itself. The rotor
stack is powered by the existing **3V3_ENIG** rail (TPS75733KTTRG3 LDO, 3A). There is no separate Rotor Buck; the erroneous "3.3V/5A Rotor Buck" specification was a confusion with the 5V/5A CM5 rail and
has been removed.

### Rationale

- Centralising all power generation on the Power Module simplifies thermal management (all heat dissipation in one shielded enclosure with dedicated thermal zone).
- Reduces the risk of ground loops and cross-domain sequencing issues.
- The Controller Board as a routing layer keeps its design cleaner and easier to revise independently.
- 3V3_ENIG (3A) covers all 3.3V consumers: CPLDs, USB-JTAG, I2C logic, status indicators, and the rotor stack.
- ROTOR_EN (CM5 GPIO 16) enables/disables the 3V3_ENIG LDO for sequenced rotor power-up — a control signal only.

### Architectural Rule (permanent)

> All power rails are generated on the Power Module. The Controller Board routes rails to downstream boards only. No buck converters, LDOs, or other power-generating components belong on the
> Controller Board.

### Impact

- `README.md`: Removed erroneous "Dedicated 3.3V/5A Buck" from Controller Board section; 3V3_ENIG correctly listed as Power Module output serving CPLDs, logic, and rotor stack.
- `Power_Module/Design_Spec.md`: 3V3_ENIG scope updated to include rotor stack; 3-island Power Plane retained.
- `Controller/Design_Spec.md`: ROTOR_EN clarified as LDO enable signal to Power Module.
- `Rotor/Design_Spec.md`: Power source updated from "Controller Board Island C" to "Power Module 3V3_ENIG rail".

### Previously Conflicting References (now corrected)

- `README.md` placed the Rotor Buck under the Controller Board section.
- `Rotor/Design_Spec.md` said "sourced from the Controller Board's Island C".

---

## DEC-012 — U4 TPS25750 Replaced with TPS25751DREFR (NRND Resolution)

- **Status:** ✅ RESOLVED
- **Date:** 2026-04-03
- **Category:** Electrical
- **Area:** Power Module U4, schematic, PCB footprint

### Decision

Replace **TPS25750** (NRND — Not Recommended for New Designs) with **TPS25751DREFR** (PD3.1 certified DRP controller, WQFN-38 6×4mm).

### Rationale

- PD emulation for U4 is required: the Raspberry Pi CM5 must negotiate a 5V/5A (25W) contract from the USB-C PD source to prevent the OS from issuing under-voltage warnings and throttling the system.
- The TPS25751D variant includes the integrated 20V/5A bi-directional power path and a 5V/3A source switch in one package — appropriate for DRP operation that can advertise and deliver the 5V/5A

  profile to the CM5.

- TPS25751 is USB-IF PD3.1 certified (TID#10306); TPS25750 was PD2.0 only and is NRND.
- STUSB4500 (U5) handles the USB-C sink path; TPS25751 (U4) handles the source/emulation path. These are separate and complementary roles.

### Impact

- ⚠️ **Package change**: TPS25750 was QFN-28; TPS25751DREFR is WQFN-38 6×4mm. Schematic symbol and PCB footprint must both be updated.
- Mouser: `595-TPS25751DREFR`; DigiKey: `TPS25751DREFR-ND`.

---

## DEC-013 — L3 EMI Inductor Changed to Bourns SRP1265A-100M

- **Status:** ✅ RESOLVED
- **Date:** 2026-04-03
- **Category:** Electrical
- **Area:** Power Module L3, PCB footprint

### Decision

Replace **Würth 7447789100** with **Bourns SRP1265A-100M** as L3 (EMI DM Pi-filter inductor).

### Rationale

- Würth 7447789100 is not available in any public distributor catalog (not found at DigiKey, Mouser, Farnell, or on the Würth public website). Sourcing without a Würth rep contact is not feasible.
- Bourns SRP1265A-100M is a direct functional equivalent: 10µH, **15.5A Isat** (exceeds 14.5A target with 21% headroom), DCR=16.5mΩ max (better than the original 20mΩ spec), shielded molded SMD.
- Widely stocked: Farnell ~2,741 pcs; Mouser (`652-SRP1265A-100M`); DigiKey (`SRP1265A-100MCT-ND`).

### Impact

- ⚠️ **Package footprint change**: SRP1265A-100M is 13.5×12.5×6.2mm vs 7447789100's 12.5×12.5×6.0mm. PCB land pattern for L3 must use the Bourns 13.5×12.5mm footprint. Clearance to adjacent

  components should be checked during layout.

---

## DEC-014 — Controller Board Uses ERF8 (Female) on Both BtB Connectors for Blind-Mate Assembly

- **Status:** ✅ RESOLVED
- **Date:** 2026-04-04
- **Category:** Electrical
- **Area:** Controller J1 (Link-Alpha), Controller J2 (Link-Beta), Consolidated BOM connector inventory

### Decision

Both BtB connectors on the Controller Board use the ERF8 female socket: J1 (Link-Alpha) uses **ERF8-040-05.0-S-DV-K-TR** and J2 (Link-Beta) uses **ERF8-020-05.0-S-DV-K-TR**.
The mating male plugs are fitted to the Power Module (J1, ERM8-040) and the Stator Board (J8, ERM8-020-05.0-S-DV-K-TR) respectively.

### Rationale

During mechanical assembly, the Controller Board slides into the enclosure and must simultaneously engage with two boards along its back edge
— the Power Module (J1) to one side and the Stator (J2) to the other.
Using female sockets on the Controller allows guided blind-mate engagement in a single insertion motion,
with the mating male pins on the peripheral boards providing positive alignment.
Placing male headers on the Controller would require both peripheral boards to be precisely pre-positioned before the Controller could be inserted,
significantly complicating assembly.

### Connector Assignment Summary

| Board | Connector | Gender | Part |
| :--- | :--- | :--- | :--- |
| Controller | J1 (Link-Alpha, from Power Module) | Female | ERF8-040-05.0-S-DV-K-TR |
| Controller | J2 (Link-Beta, to Stator Board) | Female | ERF8-020-05.0-S-DV-K-TR |
| Power Module | J1 (Link-Alpha plug) | Male | ERM8-040-05.0-S-DV-K-TR |
| Stator Board | J8 (Link-Beta plug) | Male | ERM8-020-05.0-S-DV-K-TR |

### Impact

- Controller BOM J2 updated from ERM8 (male) to ERF8 (female); JLCPCB C-number to be verified.
- Controller §2 narrative updated to reflect ERF8 on Link-Beta.
- No electrical impact — connector is signal-transparent; pin assignments unchanged.

---

## DEC-015 — LINK-BETA Connector Reduced from 80-pin to 40-pin (ERF8-020 / ERM8-020)

- **Status:** ✅ RESOLVED
- **Date:** 2026-04-04
- **Category:** Electrical
- **Area:** Controller Board (J2), Stator Board (J8), Consolidated BOM

### Decision

The LINK-BETA Board-to-Board connector is reduced from 80-pin (ERF8-040 / ERM8-040) to **40-pin
(ERF8-020-05.0-S-DV-K-TR / ERM8-020-05.0-S-DV-K-TR)**. The full 40-pin allocation is as follows:

| Pin | Signal | Direction | Notes |
| :--- | :--- | :--- | :--- |
| 1 | GND | — | JTAG leading shield |
| 2 | TCK | CTRL→Stator | JTAG clock |
| 3 | GND | — | TCK/TMS inter-pin shield |
| 4 | TMS | CTRL→Stator | JTAG mode select |
| 5 | GND | — | TMS/TDI inter-pin shield |
| 6 | TDI | CTRL→Stator | JTAG data in |
| 7 | GND | — | TDI/SYS_RESET_N inter-pin shield |
| 8 | SYS_RESET_N | CTRL→Stator | SYS_RESET_N (active-low) |
| 9 | GND | — | JTAG trailing shield |
| 10 | GND | — | Isolation moat pin 1 |
| 11 | GND | — | Isolation moat pin 2 |
| 12 | ENC_IN[0] | CTRL→Stator | Encoder input bit 0 |
| 13 | ENC_IN[1] | CTRL→Stator | Encoder input bit 1 |
| 14 | ENC_IN[2] | CTRL→Stator | Encoder input bit 2 |
| 15 | ENC_IN[3] | CTRL→Stator | Encoder input bit 3 |
| 16 | ENC_IN[4] | CTRL→Stator | Encoder input bit 4 |
| 17 | ENC_IN[5] | CTRL→Stator | Encoder input bit 5 |
| 18 | GND | — | ENC_IN / ENC_OUT inter-group shield |
| 19 | ENC_OUT[0] | Stator→CTRL | Encoder output bit 0 |
| 20 | ENC_OUT[1] | Stator→CTRL | Encoder output bit 1 |
| 21 | ENC_OUT[2] | Stator→CTRL | Encoder output bit 2 |
| 22 | ENC_OUT[3] | Stator→CTRL | Encoder output bit 3 |
| 23 | ENC_OUT[4] | Stator→CTRL | Encoder output bit 4 |
| 24 | ENC_OUT[5] | Stator→CTRL | Encoder output bit 5 |
| 25 | GND | — | ENC_OUT / TTD_RETURN shield |
| 26 | TTD_RETURN | Stator→CTRL | JTAG TDO short-path return (bypasses rotor stack) |
| 27 | GND | — | TTD_RETURN shield |
| 28–35 | 3V3_ENIG | PM→Stator | Power pass-through from Link-Alpha; 8 pins × 0.5A = 4.0A |
| 36–40 | GND | — | Power return (5 pins) |

### Rationale

Logic boards downstream of the Stator (Encoder, Reflector, Extension) are 3V3-only — they require
no 5V_MAIN rail. Removing 5V_MAIN from LINK-BETA and rationalising the signal set results in exactly
40 signals. The JTAG block has 5 internal GND shield pins (self-shielded at low-moderate MHz), so only
a 2-pin GND moat is needed between JTAG and the data zone. 8 × 3V3_ENIG pins deliver 4.0A — adequate
for the worst-case 30-rotor stack (2.20 A per Power_Budgets.md). 5 GND return pins plus the 10 other GND pins throughout the
connector provide adequate return paths.

### Poka-Yoke Safety Note

The 80-pin LINK-ALPHA (ERF8-040) and 40-pin LINK-BETA (ERF8-020) on the Controller Board are
**physically incompatible** — the mating connectors cannot be inserted into the wrong socket. This
provides a mechanical safeguard against mismating during prototype bring-up.

### Alternatives Considered

Keeping 80-pin connector with unused pins. Rejected: unnecessary connector cost and PCB area; larger
connector on the Stator increases stack height with no benefit.

### Impact

- Controller J2: ERF8-040 → ERF8-020-05.0-S-DV-K-TR (female, 40-pin)
- Stator J8: ERM8-040 → ERM8-020-05.0-S-DV-K-TR (male, 40-pin)
- DEC-014 connector table updated (see cross-ref below).

### Cross-ref

DEC-014 (gender assignment rationale remains valid; part numbers updated).

---

## DEC-016 — JTAG Controlled Impedance and Series Termination

- **Status:** ✅ ADOPTED
- **Date:** 2026-04-05
- **Category:** Electrical
- **Area:** Controller Board, Stator Board, Encoder Board, Reflector Board (noted), Extension Board (noted)

### Decision

All JTAG signal traces on 4-layer and 6-layer PCBs are specified at **50 Ω controlled impedance**
(0.127 mm / 5 mil trace width on outer layers over a contiguous GND plane). Series termination
resistors are added at every cable-driving JTAG output using **75 Ω** (to match the ~100 Ω
impedance of alternating-GND IDC ribbon cable), and at every intra-board or BtB-driving JTAG output
using **33 Ω** (to match the 50 Ω PCB trace impedance).

Full signal-swing analysis confirms the destination CPLD receives full logic swing (3.3 V) in all
cases. The open-circuit reflection at the high-impedance CPLD input doubles the incoming wave back
to full voltage; the series resistor controls the return reflection, not the final voltage.

### Full analysis, all options considered, and trace width calculations

See `design/Electronics/Investigations/JTAG_Integrity.md`.

### Summary of additions per board

| Board | Refs | Value | Purpose |
| :--- | :--- | :--- | :--- |
| Controller | R4, R5, R6 | 33 Ω 0603 | ~~TCK / TMS / TDI series R after 74LVC2G125 buffer, before LINK-BETA~~ **Moved to JDB — see DEC-024** |
| Stator | R7–R9 | 75 Ω 0603 | TCK → J4 / J5 / J6 encoder port outputs |
| Stator | R10–R12 | 75 Ω 0603 | TMS → J4 / J5 / J6 encoder port outputs |
| Stator | R13–R15 | 75 Ω 0603 | TDI chain drive: Stator CPLD TDO→J4, J4 return→J5, J5 return→J6 |
| Encoder | R7 | 33 Ω 0402 | CPLD1 TDO → CPLD2 TDI (intra-board, match 50 Ω PCB trace) |
| Encoder | R8 | 75 Ω 0402 | CPLD2 TDO → J2 connector (ribbon cable drive back to Stator) |
| JDB | R6, R7, R8 | 33 Ω 0402 | TCK / TMS (after U5 buffer) / TDI series damping — before J2 JTAG header |

> **Update (detailed design):** U5 (SN74LVC2G125DCUR buffer) and series damping resistors relocated
> from Controller to JDB during detailed design. LINK-BETA is confirmed as a direct Board-to-Board
> connector (no cable), so 33 Ω series damping applies throughout (not 75 Ω cable-driving rule).
> Controller JTAG lines (TCK, TMS, TDI, TTD_RETURN, VREF) are pass-through — routed directly from
> JDB hat-header to LINK-BETA without active components. See DEC-024.

**Trace width rule added to all 4-layer and 6-layer boards:** 0.127 mm (5 mil) for all JTAG signal
traces on outer layers over a GND plane.

**2-layer boards (Reflector, Extension):** Controlled impedance not practical — 50 Ω would require
a 2.82 mm trace (see `design/Electronics/Investigations/JTAG_Integrity.md §4`). Series termination at cable-driving ends of adjacent
boards provides sufficient protection. Existing Reflector R1 (22 Ω) retained as end-of-chain damping.

> **Superseded (partial):** The Reflector and Extension 2-layer limitations above are superseded by
> DEC-017, which upgrades both boards to 4-Layer JLC04161H-7628. Both boards now have a solid L2 GND
> plane and route JTAG on L1 at 0.127 mm (50 Ω), consistent with all other 4-layer boards.

### Rationale

Achieving 100 Ω PCB traces (to perfectly match the IDC ribbon cable impedance) is physically
impossible on JLCPCB standard 4-layer/6-layer stackups — the required trace width is negative
(see calculation in `design/Electronics/Investigations/JTAG_Integrity.md §4`). The 50 Ω + 75 Ω hybrid approach provides the best
achievable impedance match to the cable while remaining within manufacturing design rules.

### Alternatives Considered

- **No termination (Option A):** Rejected — multiple re-reflections at 10 MHz risk false TCK edges.
- **50 Ω PCB + 33 Ω series R (Option B):** Acceptable but leaves 33% reflection at PCB-to-cable
  transition unabsorbed.
- **100 Ω PCB + 82 Ω series R (Option C, ideal):** Rejected — not achievable on standard stackup.

### Cost Impact

Additional BOM cost per full system < £0.05. No JLCPCB impedance certification required for
prototype; trace widths self-calculated and within ±10% of target. See `design/Electronics/Investigations/JTAG_Integrity.md §9`.

---

## DEC-017 — Minimum 4-Layer Stackup for All Non-Controller Boards

- **Status:** ✅ ADOPTED
- **Date:** 2026-04-05
- **Category:** Electrical
- **Area:** Reflector Board, Extension Board (all other boards already compliant)

### Decision

All PCBs in the Enigma-NG system shall use a minimum of **4-layer stackup** (JLCPCB
JLC04161H-7628). The Controller Board and the Power Module Board are the only exceptions
and retain their 6-layer JLC06161H-2116 stackup: the Controller for high-speed 5 Gbps
differential pair requirements, and the Power Module for high-current power delivery.

### Standard 4-layer layer mapping for all non-Controller boards

| Layer | Function |
| :--- | :--- |
| L1 | Signal (JTAG, data routing) — top |
| L2 | GND plane — solid contiguous copper |
| L3 | 3V3_ENIG power plane |
| L4 | Signal (data routing, branding data plate) — bottom |

> **Exception — JTAG Daughterboard:** The JDB uses an inverted stackup: L1=GND plane + SMT
> component pads (component side, faces Controller), L2=signal traces, L3=power pours,
> L4=GND shield (exterior face). This inversion places components on the face that mates
> with the Controller Board hat-headers, consistent with single-side JLCPCB assembly.
> See `JTAG_Daughterboard/Design_Spec.md §4`.

### Boards affected (updated)

| Board | Previous | New |
| :--- | :--- | :--- |
| Reflector | 2-Layer 1.6mm FR4 / 1oz | 4-Layer JLC04161H-7628 / 2oz |
| Extension | Layer count unspecified | 4-Layer JLC04161H-7628 / 2oz |

### Boards already compliant (no change)

| Board | Stackup | Notes |
| :--- | :--- | :--- |
| Stator | 4-Layer JLC04161H-7628 | ✅ Unchanged |
| Encoder | 4-Layer JLC04161H-7628 | ✅ Unchanged |
| Rotor | 4-Layer JLC04161H-7628 | ✅ Unchanged |
| Controller | 6-Layer JLC06161H-2116 | ✅ Exception — high-speed stackup retained |
| Power Module | 6-Layer JLC06161H-2116 | ✅ Exception — high-current power delivery stackup retained |

### Impact

The "2-layer uncontrolled impedance" notes for Reflector and Extension in DEC-016 are superseded.
Both boards now have a solid L2 GND plane and can route JTAG on L1 at 0.127 mm (50 Ω controlled
impedance), consistent with all other 4-layer boards. `design/Electronics/Investigations/JTAG_Integrity.md §3.1`, `§3.3` (now
historical), and `§8` trace table have been updated accordingly.

### Rationale

1. **Uniform stackup:** Consistent JLC04161H-7628 across all non-Controller boards eliminates
   stackup-dependent trace impedance variation, reducing signal behaviour differences between boards.
2. **Solid GND on every board:** All boards now have a contiguous L2 GND plane, enabling 50 Ω
   controlled impedance JTAG routing across the entire system.
3. **EMC/EMI improvement:** Solid GND and power planes on all boards reduce radiated emissions and
   improve common-mode noise rejection across the rotor stack and encoder cabling.
4. **Manufacturing speed:** JLC04161H-7628 is JLCPCB's most common 4-layer stackup, with higher
   stock availability and faster turnaround than 2-layer special orders or less common stackups.
5. **Cost:** Marginal price difference between 2-layer and 4-layer at JLCPCB prototype quantities;
   outweighed by signal integrity and EMC benefits.

### Alternatives Considered

- **Retain 2-layer Reflector/Extension:** Rejected — inconsistent stackup creates impedance
  discontinuities in the JTAG chain and leaves an uncontrolled segment at the reflector end.
- **Use different 4-layer stackup per board:** Rejected — non-uniform dielectric parameters would
  require separate trace width calculations per board and add unnecessary design complexity.

---

## DEC-018 — Connector Pinout Ownership Model

- **Status:** Adopted
- **Date:** 2026-04-05
- **Category:** Electrical
- **Area:** All Boards — Documentation Architecture

### Decision

Each multi-board connector interface shall have a single **Definition Owner** — the board whose
`Board_Layout.md` (or `Design_Spec.md` where no Board_Layout exists) contains the authoritative
pin-by-pin table for that interface. All other boards that mate with that connector must
**not** duplicate the pin table; instead they include a short cross-reference note of the form:

> **Connector Definition Owner:** `[OwnerBoard]/Board_Layout.md — [Section]`. This board uses the
> mating connector. See BOM for part number.

This rule prevents the class of drift errors where two boards define the same connector differently
(e.g. Pin 2 = GND on one board, SYS_RESET_N on another). When a conflict is found, the owner's
definition is authoritative.

### Ownership Register

| Interface | Connector(s) | Definition Owner | Authoritative Section |
| :--- | :--- | :--- | :--- |
| **LINK-ALPHA** | PM J1 ↔ Controller J1 (80-pin ERM8/ERF8) | **Power Module** | `Power_Module/Board_Layout.md — LINK-ALPHA` |
| **LINK-BETA** | Controller J2 ↔ Stator J8 (40-pin ERM8/ERF8) | **Controller** | `Controller/Board_Layout.md — LINK-BETA` |
| **Reflector/Extension Link** | Stator J7 ↔ Extension J7/J8 ↔ Reflector J4 (16-pin 2×8) | **Stator** | `Stator/Board_Layout.md — J7` |
| **Encoder Ports** | Stator J4/J5/J6 ↔ Encoder J2 (26-pin 2×13) | **Stator** | `Stator/Board_Layout.md — J4–J6` |
| **Rotor Interface** | Stator J1–J3 ↔ Rotor 1 → … → Rotor 30 → Reflector J1–J3 (serial chain; Extension J1–J6 at group boundaries) | **Rotor** | `Rotor/Design_Spec.md §3.4` |
| **JTAG Daughterboard headers** | JDB J1 (USB 5-pin) + J2 (JTAG 10-pin) | **JTAG Daughterboard** | `JTAG_Daughterboard/Board_Layout.md` |

### Rationale

- **LINK-ALPHA → Power Module:** The Power Module is the upstream power provider; it defines what
  rails and signals it places on the cable. The Controller is the downstream consumer.
- **LINK-BETA → Controller:** The Controller is the JTAG chain master. It originates TCK, TMS, TDI,
  SYS_RESET_N, and the ENC data bus. The Stator is the passive backplane receiver.
- **Reflector/Extension Link → Stator:** The Stator is the signal origin for all ENC data, power,
  and TTD_RETURN carried on this cable. Extension and Reflector are passive pass-throughs or endpoints.
- **Encoder Ports → Stator:** The Stator drives all three encoder cables and has the complete chain
  routing logic for TDI/TDO sequencing across J4/J5/J6. The Encoder boards are the downstream receivers.
- **Rotor Interface → Rotor:** The Rotor defines its own physical interface — both the connector
  type (mechanical) and the signal mapping. Stator, Extension, and Reflector must comply with the
  Rotor's mechanical interface, not the other way round.
- **JTAG Daughterboard → itself:** Self-contained module with no cross-board mating conflicts.

### Alternatives Considered

- **Central `Interfaces.md` document:** Rejected — separates pin definitions from the board they belong
  to, making it harder to keep in sync during incremental design changes. Per-board ownership with
  cross-references is more maintainable.
- **Both sides document the full table:** Rejected — this is the exact pattern that caused the REF-03
  Pin 2 conflict and the REF-01 16/20-pin mismatch found in the April 2026 deep-dive review.

---

## DEC-019 — PoE Transformer Topology: ACF (Option A) Selected

- **Status:** ✅ Adopted
- **Date:** 2026-04-05
- **Category:** Electrical
- **Area:** Power Module — T2 transformer, TPS23730 operating mode, input EMI filter

### Decision

The Power Module retains the **Active Clamp Flyback (ACF)** topology with the **Coilcraft POE600F-12LD**
transformer. The TPS23730 operates in ACF mode, driving an external active clamp MOSFET complementary
to the primary switch. The Coilcraft transformer is procured order-direct from `coilcraft.com` and
supplied to JLCPCB as a consignment part.

No change is made to the T2 transformer, the TPS23730 mode configuration, or the active clamp circuit.

**Full investigation detail:** `design/Electronics/Investigations/PoE_Investigation.md`

### Rationale

A thorough search confirmed that **no ACF PoE isolation transformer for 60W / 36–57V input is stocked
by any mainstream authorised distributor** (DigiKey, Mouser, Farnell, Arrow). The Coilcraft POE600F
family was co-developed with TI specifically for the TPS23730 reference design; no competing catalogue
part exists.

The only standard-distributor alternative identified was the **Bourns PDC060-FD20A12S** — a standard
flyback transformer available from DigiKey. Switching to this part (Option B) would have required:

- Disabling TPS23730 `ACF_GD` (ACF gate drive pin)
- Removing the active clamp MOSFET and capacitor
- Adding an RCD clamp (3 SMD components)
- Verifying PSR auxiliary winding compatibility (unconfirmed)

After detailed EMI/EMC analysis, Option B was rejected on technical grounds. Key findings:

| Criterion | Option A (ACF) | Option B (Flyback) |
| :--- | :--- | :--- |
| Primary switching | ZVS — no hard dV/dt event | Hard switching — fast dV/dt |
| Drain spike at turn-off | None — energy recycled by clamp | Present — RCD clamp clips but does not eliminate |
| CM/DM conducted EMI | Low | 15–25 dB higher before input filter |
| Input EMI filter size | Smaller / fewer components | Larger / more complex |
| CISPR 32 Class B margin | Comfortable | Tight — may require design iteration |
| Efficiency | 88–92% | 85–90% |
| Extra dissipation | — | ~1–2W at full load |
| PSR aux winding verified | ✅ TI reference design | ⚠️ Unverified for Bourns PDC060 |

The Coilcraft direct-order model is accepted as a specialist procurement path, consistent with
industry practice for catalogue magnetics.

### Alternatives Considered

- **Bourns PDC060-FD20A12S (Option B — flyback PSR):** Rejected — hard-switching topology causes
  significantly higher conducted and radiated EMI, requires a larger input EMI filter, does not
  eliminate procurement complexity (shifts effort from transformer sourcing to filter design),
  and adds ~1–2W thermal load to an already thermally constrained module.
- **Würth WE-FB range:** Rejected — entire range has a maximum input voltage of 36V (insufficient
  for PoE 36–57V input) and is keyed to Linear Technology LT-series controllers.
- **Change PoE controller ecosystem:** Not evaluated — would constitute a major redesign and is
  out of scope.

---

## DEC-020 — GND_CHASSIS Rib Clearway ENIG Bond

- **Status:** Accepted — 2026-04-08
- **Date:** 2026-04-08
- **Category:** Electrical
- **Area:** Power Module — Supercap Block Assembly & Board Layout
- **References:** QUE-001, Certification_Evidence.md §2.2

### Decision

The 3.0mm rib clearway gaps between supercap cells shall have:

1. **Exposed ENIG strip (L1):** Solder mask opened in the rib clearway gap on the top copper layer (L1),
   connected to the GND_CHASSIS net. Minimum strip width 1.5mm, running the full depth of the rib contact zone.
   The aluminium enclosure rib makes direct electrical contact with the PCB GND_CHASSIS copper, providing a
   distributed HF chassis ground bond at the supercap block location.

2. **Polyimide (Kapton) tape on supercap bodies:** Each supercap cell shall be wrapped with a minimum of
   one layer of 2-mil (50µm) polyimide tape prior to installation, to electrically insulate the cell body
   from the aluminium compression ribs and prevent short circuits.

3. **Conductive elastomer gasket strip:** A self-adhesive conductive elastomer or conductive foam gasket strip
   (≤3mm wide, full rib contact depth) shall be applied to the rib face or PCB contact zone to accommodate
   manufacturing tolerances and ensure positive, reliable electrical contact under compression.
   Part to be selected at mechanical design phase when rib geometry is confirmed.

### Rationale

The combined structure — aluminium Can lid, compression ribs, conductive gasket, PCB ENIG strip, and
GND_CHASSIS copper pour — forms a near-complete Faraday cage around the supercap block, improving
shielding of the high-capacitance energy storage element from the rest of the board.

### Compatibility with single-point GND_CHASSIS bond rule

The single-point rule governs signal GND → GND_CHASSIS crossings. Rib contact bonds are
enclosure-to-GND_CHASSIS connections — both within the chassis domain — and do not create additional
signal-to-chassis bonds. The rule is maintained.

### Other boards

Deferred pending mechanical design documentation. Controller Board Mechanical_Design.md §3 notes the
prototype uses a 3D-printed chassis (no conductive rib contact); this decision will be revisited when
metal chassis dimensions are finalised. Stator/Encoder/Rotor mechanical designs are not yet written.

---

## DEC-021 — Supercapacitor Bank Upgrade: 2×2 2S2P → 2×3 2S3P

- **Status:** Accepted — 2026-04-08
- **Date:** 2026-04-08
- **Category:** Electrical
- **Area:** Power Module — Supercap Bank, Board Layout, Hold-up Specification
- **References:** DR-PM-07, DR-PM-09, DEC-020

### Decision

The supercapacitor bank is upgraded from a 2×2 (4-cell, 2S2P) to a **2×3 (6-cell, 2S3P)** arrangement,
with the inter-cell air gap increased from 2.0mm to **3.0mm**.

| Parameter | Previous | New |
| :--- | :--- | :--- |
| Cell count | 4 (C_SC1–4) | 6 (C_SC1–6) |
| Arrangement | 2×2 | 2×3 |
| Configuration | 2S2P | 2S3P |
| Inter-cell gap | 2.0mm | 3.0mm |
| Cell pitch | 14mm | 15mm |
| Block footprint | 28mm × 28mm | 30mm × 45mm |
| Shadow zone | 32mm × 32mm | 34mm × 49mm |
| Effective capacitance | 22F at 5.4V | 33F at 5.4V |
| Hold-up energy | 72.4J | 108.6J |
| Hold-up duration @ 5W | ≥14.5s | ≥21.7s |
| Charge time (depleted) | ~2 min | ~3 min |

### Rationale

- **50% more hold-up:** 33F vs 22F provides ≥21.7 seconds at 5W — a more comfortable shutdown window
  and headroom for higher CM5 load profiles at prototype bring-up.
- **LTC3350 compatibility:** No IC change required. LTC3350 is configured for 2 cells in series;
  each series position now has 3×22F in parallel (66F per position). CELLS register unchanged.
  RICHARGE (0.5A charge current limit) unchanged; charge time increases ~3 minutes from depleted.
- **Wider gap (3mm):** The increased inter-cell gap from 2.0mm to 3.0mm provides adequate clearance
  for the 2-mil Kapton tape wrap (DEC-020), the conductive elastomer gasket strip, and the aluminium
  enclosure compression ribs, while maintaining margin for manufacturing tolerances.
- **Board space:** The Power Module board dimensions are not yet fixed; the design is being built
  around this component block. The increased footprint (30mm × 45mm vs 28mm × 28mm) is accepted.

---

## DEC-022 — JDB FT232H Clock Source: Dedicated 12MHz SMD Crystal Selected

- **Status:** Decided
- **Date:** 2026-04-06
- **Category:** Electrical
- **Area:** JTAG Daughterboard — Clock Source (FT232H)

### Decision

Dedicated 12MHz SMD passive crystal (Y1) on the JDB PCB. CM5 GPCLK0 option rejected.

### Context

During JDB detailed design review, two issues were identified:

1. The original design incorrectly specified a **24MHz HC-49 through-hole crystal**. The FT232H datasheet requires a **12MHz**
   reference — its internal PLL multiplies 12MHz × 40 to generate 480MHz for USB Hi-Speed operation. 24MHz is outside specification.
2. An alternative was considered: routing a clock from the **CM5 GPCLK0 output (GPIO4)** to the FT232H OSCI pin instead of a dedicated on-board crystal.

### Options Considered

| Option | Description | Verdict |
| :--- | :--- | :--- |
| A | CM5 GPCLK0 (GPIO4) routed through Controller hat-header to FT232H OSCI | **Rejected** |
| B | Dedicated 12MHz passive SMD crystal (Y1) on JDB PCB | **Selected** |

**Option A — Rejected reasons:**

- Signal path: CM5 GPIO4 → Controller board → hat-header pin → JDB OSCI is long and noise-prone
- GPIO clock jitter from BCM is unsuitable as a USB PLL reference clock
- Creates a CM5 boot-order dependency — FT232H cannot enumerate on USB until CM5 configures GPCLK0
- Adds routing and firmware complexity with no benefit over a $0.07 crystal

**Option B — Selected:**

- Standard FTDI reference design approach; clean stable clock source
- No boot dependency; FT232H enumerates immediately on USB connect
- Component: **YXC X322512MSB4SI** (JLCPCB C9002), SMD3225-4P, 12MHz, 20pF, ±20ppm, Basic part
- Crystal load capacitors: C10–C11 = 33pF C0G 0402 (sets 20pF load capacitance)

### Impact

- `design/Electronics/JTAG_Daughterboard/Design_Spec.md`: Y1 corrected to 12MHz SMD3225-4P (C9002); C10–C11 added; text references updated.

---

## DEC-023 — JDB GND_CHASSIS Omitted; Mounting Holes Tied to GND

- **Status:** Decided
- **Date:** 2026-04-06
- **Category:** Electrical
- **Area:** JTAG Daughterboard — Grounding & EMC

### Decision

The JTAG Daughterboard (JDB) does **not** implement a `GND_CHASSIS` net. Mounting holes are included
for mechanical stability via conductive standoffs to the Controller board; the copper pours around
those mounting holes are tied to **GND** (circuit return). No dedicated chassis bond pad, stitching
via, or `GND_CHASSIS` net is present on the JDB.

### Rationale

`GND_CHASSIS` exists to bond a PCB to the metal enclosure for EMC shielding, ESD protection, and safety earth. None of those functions apply to the JDB because:

1. **No chassis surface** — the JDB is an internal daughterboard that floats above the Controller
   board on hat-header pins and conductive standoffs. It has no metal enclosure surface it can
   directly bond to.
2. **EMC envelope already provided** — the Controller board beneath it carries a correctly implemented `GND_CHASSIS` net bonded to the system enclosure. The JDB sits entirely within that envelope.
3. **No external connections** — the JDB has no cables or connectors that exit the enclosure, so there are no ESD entry points that would require chassis bonding at the JDB level.
4. **Low-EMI device** — the FT232H operates at USB 2.0 speeds on an internal point-to-point link. It generates no significant conducted or radiated emissions that would require additional chassis shielding.
5. **Daisy-chaining adds no value** — connecting JDB `GND_CHASSIS` via standoffs to Controller
   `GND_CHASSIS` would create an additional path to chassis earth but no new bond point, adding
   PCB complexity for zero measurable EMC benefit.

### Implementation

- Include **mounting holes** on the JDB for mechanical stability.
- Standoffs are conductive (metal); this incidentally bonds the JDB mounting hole copper pours to the Controller board mechanically.
- Mounting hole copper pours connect to **GND** (circuit return) — not to a separate `GND_CHASSIS` net.
- This is consistent with standard practice for small internal sub-modules (e.g. Arduino shields, FPGA daughter cards).

### Alternatives Considered

- **Standoff bonding to Controller GND_CHASSIS:** Technically implementable but adds a separate net, a copper pour, and design rules for no measurable EMC gain on a low-EMI internal board. Rejected.
- **No mounting holes at all:** Rejected — mechanical retention via standoffs is required to prevent the board from flexing on the hat-headers during connector insertion/removal.

---

## DEC-024 — JDB is Complete JTAG Master; Controller JTAG Lines Are Pass-Through

- **Status:** Decided
- **Date:** 2026-04-06
- **Category:** Electrical
- **Area:** JTAG Architecture — Controller and JTAG Daughterboard

### Decision

The JTAG Daughterboard (JDB) is the complete JTAG master. The SN74LVC2G125DCUR dual-channel
buffer (U5) for TCK and TMS, and all 33 Ω series damping resistors (R6 TCK after U5, R7 TMS after
U5, R8 TDI direct from FT232H) are located on the JDB, before the J2 JTAG header. The Controller
board routes JTAG lines (TCK, TMS, TDI, TTD_RETURN, VREF) as pass-through from the JDB hat-header
to the LINK-BETA BtB connector without any active components.

LINK-BETA is a direct Board-to-Board connector (no cable). Therefore 33 Ω series damping (matched
to 50 Ω PCB trace impedance) applies throughout — not the 75 Ω cable-driving resistors specified
for ribbon cable connections. See DEC-016 for the full 75 Ω / 33 Ω rationale.

### Rationale

- **Simpler Controller BOM:** Removing U5, R4, R5, R6 from the Controller reduces complexity and
  potential assembly errors on the main board.
- **Cohesive JTAG subsystem:** All JTAG active components and termination are co-located on the JDB,
  which is the natural owner of the JTAG function.
- **BtB confirmation:** LINK-BETA is a Samtec ERF8-020 / ERM8-020 direct board-to-board stack (no
  ribbon cable). The 33 Ω source termination after U5 is the correct value for 50 Ω PCB traces.

### Impact

- `Controller/Design_Spec.md`: U5 removed from BOM; R4, R5, R6 removed; §3 updated to reflect
  pass-through routing; DR-CTL-05 updated; FR-CTL-04 reference to U5 removed.
- `JTAG_Daughterboard/Design_Spec.md`: U5 added to BOM; R6, R7, R8 (33 Ω 0402) added.
- `Electronics/Consolidated_BOM.md`: SN74LVC2G125DCUR moved from CTL column to JDB column;
  33 Ω 0402 count increased in JDB; 33 Ω 0603 row removed from CTL.
- `Electronics/Investigations/JTAG_Integrity.md`: §7.4 and §8 updated to reflect JDB location.
- `Design_Log.md DEC-016`: Update note added.

---

## DEC-025 — CM5 Shutdown Mechanism: Interrupt-Driven via Custom Linux Driver (Deferred)

- **Status:** Deferred — Software PoC Stage
- **Date:** 2026-04-09
- **Category:** Software
- **Area:** Software / Linux OS — CM5 Power Management Shutdown Path

### Decision

The final implementation of the CM5 graceful shutdown mechanism — triggered by the LTC3350 BACKUP
signal — is deferred to the **Software PoC stage**, pending hardware availability for integration
testing. The real implementation will use a **custom Linux kernel driver** that registers the BACKUP
signal as a hardware interrupt, rather than a userspace polling daemon.

The PWR_GD GPIO (GPIO 27, MCP121T-450E) remains the hard-backstop interrupt and requires no driver
development — it is handled by the standard gpio-shutdown device tree overlay.

### Rationale

- The custom driver approach eliminates polling latency entirely (interrupt response is effectively
  immediate vs. up to 500 ms for a 2 Hz poll cycle).
- Driver development requires the physical hardware to be available for testing and validation.
  Writing and verifying kernel interrupt handlers against simulated hardware is impractical.
- The system is designed for operational sessions of 15–30 minutes or longer. The hold-up window
  (>=21.7 s) is a generous safety margin; an unplanned shutdown from a fully-charged state is expected
  to be harmless. Deferring the driver to the PoC stage does not create a risk for hardware bring-up.
- Placeholder pseudocode in design/Software/Linux_OS/Power_Management.md documents the intended
  behaviour for reference; it is not a specification.

### Impact

- design/Software/Linux_OS/Power_Management.md Phase 1: Polling daemon pseudocode replaced with
  deferred-decision note referencing DEC-025. The PWR_GD gpio-shutdown backstop (Phase 2) is
  unchanged and remains the active hardware protection path until the driver is written.

---

## Open Questions

Questions raised during design review that are deferred pending further investigation or a future decision.

---

## QUE-001 — Exposed ENIG on Rib Clearway for GND_CHASSIS EMI Bonding

- **Status:** Closed — resolved by DEC-020 (2026-04-08)
- **Raised:** 2026-04-04
- **Area:** Power Module / All Boards — PCB Finish & EMC

### Background

The Power Module enclosure uses internal aluminium compression ribs that locate the PCB within the "Power Can".
The supercap block §4 defines a **2.0mm rib clearway** (14mm pitch, 12mm cell body) as a no-fly zone for traces on all layers.
A separate GND_CHASSIS copper pour already exists in the supercap shadow zone beneath the cells (§5).

The question is whether the rib clearway should have an **explicit solder mask opening (exposed ENIG)** on the top copper layer, connected to the GND_CHASSIS net,
so that when the PCB seats in the enclosure the aluminium ribs make direct electrical contact with the board's chassis ground.
This is a standard EMC bonding technique used in Eurocard/VME card-cage designs.

### What the change would involve

If accepted, the following updates would be made:

1. **Power Module Design_Spec.md §4** — Add bullet:
   > - **Rib Clearway ENIG Bond:** A solder mask opening (exposed ENIG) is placed in the 2.0mm rib clearway gap on the top copper layer, connected to GND_CHASSIS.
   >   Contact with the aluminium enclosure rib creates a distributed chassis ground bond at the supercap block location.

2. **Power Module Board_Layout.md** — Add keepout note:
   > Rib clearway gap: solder mask open, GND_CHASSIS copper strip, min 1.5mm wide × full rib depth.

3. **All other boards (Controller, Stator, Encoder)** — Assess whether their enclosure ribs also warrant the same treatment and add matching callouts if so.

4. **DEC-020** — Create a decision entry recording the EMC rationale, referencing the single-point GND_CHASSIS bond rule in Certification_Evidence.md §2.2.

### Considerations

| Factor | Note |
| ------ | ---- |
| Contact reliability | ENIG is ideal — hard, oxidation-resistant, consistent contact resistance |
| Enclosure material | Aluminium — no galvanic corrosion risk with ENIG |
| GND_CHASSIS topology | Single-point bond already defined (Cert_Evidence §2.2); rib contact adds distributed HF bond — compatible if star-point rule maintained for DC |
| Mechanical tolerance | Rib must be tight-fitting or spring-loaded to ensure reliable electrical contact |
| Other boards | Only applies where enclosure ribs contact the PCB — needs mechanical review per board |

### Resolution

Accepted. See DEC-020. Decision: expose ENIG on rib clearway zones, add minimum 2-mil polyimide (Kapton)
tape on supercap bodies, and add conductive elastomer gasket strip at the rib-to-PCB contact interface.
Other boards deferred pending mechanical design documentation (rib presence unconfirmed for Stator/Encoder/Rotor;
Controller noted as using 3D-printed prototype chassis with future metal chassis EMI gaskets per Mechanical_Design.md §3).

---

## QUE-002 — Prototype Bench-Testing Cable Strategy for Rotor Stack Connectors

- **Status:** CLOSED — 2026-04-08
- **Raised:** 2026-04-05
- **Area:** All Boards — Rotor Interface Connectors (ERF8/ERM8 0.8mm pitch) & Extension/Reflector Links

### Resolution

**Break-off PCB coupons** are to be included on the Rotor, Stator, Extension, and Reflector boards.
Each coupon is a small PCB tab attached to the main board by mousebite perforations. One coupon per
ERx8 connector. Each coupon fans out the 0.8mm pitch Samtec ERx8 pads to a standard **2.54mm pitch
shrouded IDC box header**, allowing standard ribbon cable assemblies to be used for initial bench
testing without full stack assembly.

**Coupon types required:**

| ERx8 Connector | Pins | IDC Header |
| :--- | :---: | :--- |
| ERM8-005 / ERF8-005 | 10 (2×5) | 2×5 IDC box header, 2.54mm pitch |
| ERM8-010 / ERF8-010 | 20 (2×10) | 2×10 IDC box header, 2.54mm pitch |
| ERM8-020 / ERF8-020 | 40 (2×20) | 2×20 IDC box header, 2.54mm pitch |

**Per-board coupon provision:**

- **Rotor:** 6 coupons — J1 (ERM8-005), J2 (ERM8-005), J3 (ERM8-010), J4 (ERF8-005), J5 (ERF8-005), J6 (ERF8-010)
- **Stator:** 4 coupons — J8 (ERM8-020) + J1/J2/J3 for Slot 1 test (ERF8-005 ×2, ERF8-010 ×1)
- **Extension:** 6 coupons — J1 (ERM8-005), J2 (ERM8-005), J3 (ERM8-010), J4 (ERF8-005), J5 (ERF8-005), J6 (ERF8-010)
- **Reflector:** 3 coupons — J1 (ERM8-005), J2 (ERM8-005), J3 (ERM8-010)

For final assembly the coupons are snapped off at the mousebite perforations and the ERx8 connectors mate
directly board-to-board. Coupon IDC connector selection (shrouded box header part numbers) and exact
PCB fanout geometry to be defined at schematic/layout phase.

### Background

The rotor-to-rotor, rotor-to-Stator, and rotor-to-Reflector/Extension connections all use the Samtec
Edge-Rate ERF8/ERM8 0.8mm pitch family, which are direct board-to-board connectors with no off-the-shelf
cable assembly equivalent at standard distributors. During prototype bench testing it will not always be
practical to have all boards physically stacked.

The Extension/Reflector link (J7 on Stator, J7/J8 on Extension, J4 on Reflector) and the Encoder ports
(Stator J4-J6) use 2.54mm pitch shrouded IDC headers for which standard ribbon cable assemblies are
readily available.

### Questions to Resolve Before Prototype Build

1. **ERF8/ERM8 0.8mm pitch:** Are Samtec ERCD/ERCC cable assemblies available and stocked at DigiKey
   or Mouser for the ERF8-005 and ERF8-010 series? If not, what is the preferred bench-testing strategy
   (e.g., small bridge PCBs, short rigid extender boards, or FPC/FFC with pitch adapter)?
2. **Connector selection review:** Confirm that ERF8/ERM8 is still the correct family for the final
   design before committing to prototype PCB orders — alternative connector families may offer
   cable-assembly options without changing the electrical design.
3. **2.54mm IDC cables:** Confirm standard IDC ribbon cable lengths and sources for Stator J7
   (16-pin 2×8) and Stator J4-J6 encoder ports (26-pin 2×13).

### Note

This question was deferred to prioritise getting the connector definitions consolidated. The connector
designators and signal assignments are considered stable (pending QUE-002 resolution). If a connector
family change is required for prototype cabling, the affected documents are:
`Stator/Design_Spec.md`, `Extension/Design_Spec.md`, `Reflector/Design_Spec.md`, `Rotor/Design_Spec.md`,
`Consolidated_BOM.md`, and the Design_Log connector inventory.

---

## INC Review History

This section records all INC (inconsistency) items tracked during the design process. Each item was identified during design review, verified, and resolved. All items are closed.

| INC | Area | Description | Original Value | Corrected Value | Status |
| ----- | ------ | ------------- | ---------------- | ----------------- | -------- |
| INC-01 | Power Module eFuse | UVLO/OVLO thresholds inconsistent between README and Design_Spec | README: 12V UVLO / 16V OVP | 11.0V UVLO / 16.9V OVLO (per Design_Spec §5) | ✅ Resolved — README corrected |
| INC-02 | Power Module eFuse | eFuse current limit insufficient for 75W USB-C path. TPS259474L max 5.5A with no headroom at 5.0A worst case | TPS259474L (5.5A ILIM) | TPS25980 (7A ILIM, 16.9V OVLO, VQFN-24). See DEC-005 | ✅ Resolved — DEC-005 |
| INC-03 | Power Module 5V Buck | Single buck insufficient for CM5 25W + other loads | LM61460-Q1 (6A) | Dual LMQ61460-Q1 interleaved (12A total). See DEC-007 | ✅ Resolved — DEC-007 |
| INC-04 | Power Module PD Emulator | TPS25750 PDO listed as "5V/6A" — not a valid USB-C PD current at 5V | "5V/6A" (invalid) | 5V/5A (25W maximum at 5V per USB-C PD spec). See DEC-008 | ✅ Resolved — DEC-008 |
| INC-05 | Link-Alpha BtB Connector | 3V3_SYSTEM routed from CM5 to Power Module on pins 21–24 for RJ45 LED anodes — cross-domain dependency | 3V3_SYSTEM on pins 21–24 (input from CM5) | Removed. 3V3_ENIG generated locally on Power Module. Pins 21–22 → 5V_MAIN; pins 23–24 → GND. See DEC-001 | ✅ Resolved — DEC-001 |
| INC-06 | Power Module PoE | Ag5300 PoE module only supports 802.3at (25.5W PD) — insufficient for full system load ~42W | Ag5300 (802.3at, 25.5W) | Discrete: TPS2372-4 + TPS23730 + Coilcraft POE600F-12LD (802.3bt Type 4 / Class 8, 72W system; T2 transformer = 60W). See DEC-002 | ✅ Resolved — DEC-002 |
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
| INC-19 | Power Module PoE | Ag5300/Ag53000 is 802.3at only (25.5W PD). No 802.3bt Type 4 PCB module found. Architecture change required: Type 3 (51W) insufficient; Type 4 (72W) required | Ag5300/Ag53000 (802.3at SIL module) | Discrete two-stage: TPS2372-4 (PD) + TPS23730 + POE600F-12LD (ACF transformer). See DEC-002 | ✅ Resolved — DEC-002 |
| INC-20 | Power Module Supercap | Supercap charge path had no current limiting — would cause excessive inrush and violate 75% utilisation rule under PoE | Supercap directly on 5V_MAIN bus | LTC3350 soft-charge via RICHARGE resistor; 0.5A limit under PoE. See DEC-004 | ✅ Resolved — DEC-004 |
| INC-21 | Power Module J2 | Component selection locked: RJ45 MagJack | — | Würth 7499111121A (SMT, shielded, 2-LED, 10/100/1000) | ✅ Locked |
| INC-22 | Power Module ESD | Component selection locked: Ethernet ESD arrays | — | 2× TI TPD4E05U06DRYR (0.8pF, ±15kV, −40°C to +125°C, U-DFN-10) per port | ✅ Locked |
| INC-23 | Power Module Bob Smith | Component selection locked: Bob Smith termination network | — | 4× 75Ω 0402 ±1% resistors + 1× 10nF Y1-class capacitor to GND_CHASSIS | ✅ Locked |

---

## Board Connector Inventory

The following table lists all physical connectors across every board in the Enigma-NG system. This list should be manually verified against the original intended design to confirm no specification
changes have inadvertently altered connector placement, orientation, or mating requirements.

### Power Module

| Ref | Description | Part / Series | MPN | Mouser PN | DigiKey PN | Notes |
| ----- | ------------- | --------------- | ----- | ----------- | ------------ | ------- |
| J1 | Link-Alpha BtB — 80-pin socket to Controller Board | Samtec ERM8-040-05.0-S-DV-K-TR | ERM8-040 | 200-ERM8040050SDVKTR | SAM8613CT-ND | Male header (ERM8). Mating female on Controller (ERF8). Gold-plated, 0.5A/pin |
| J2 | RJ45 MagJack with integrated magnetics | Würth 7499111121A | 7499111121A | 710-7499111121A | 1297-1070-5-ND | SMT, shielded, 2 integrated LEDs (green/yellow), 10/100/1000 PoE compatible |
| J3 | Battery connector — 5-pin Micro-Fit 3.0 THT vertical | Molex 43650-0519 | 43650-0519 | 538-43650-0519 | WM14587-ND | 5-circuit, 1-row, gold contacts, board lock, 3mm pitch. ⚠️ MPN corrected (43045-0512 does not exist) |

### Controller Board

| Ref | Description | Part / Series | MPN | Mouser PN | DigiKey PN | Notes |
| ----- | ------------- | --------------- | ----- | ----------- | ------------ | ------- |
| J1 | Link-Alpha BtB — 80-pin socket to Power Module | Samtec ERF8-040-05.0-S-DV-K-TR | ERF8-040 | 200-ERF8040050SDVKTR | SAM8621CT-ND | Female socket (ERF8). Mating male on Power Module (ERM8) |
| J2 | Link-Beta BtB — 40-pin socket to Stator Board | Samtec ERF8-020-05.0-S-DV-K-TR | ERF8-020 | 200-ERF8020050SDVKTR | SAM8619CT-ND | Female socket (ERF8). Mating male on Stator (ERM8-020). 40-pin per DEC-015 |
| J3 | USB 3.0 — Dual-stacked Type-A port | Molex 48406-0003 | 48406-0003 | 538-0484060003 | WM1394-ND | Dual-stack Type-A, 5.0mm protrusion through chassis |
| J4 | HDMI — Full-size Type-A | TE Connectivity 2007435-1 | 2007435-1 | 571-2007435-1 | A125057-ND | Full-size HDMI Type-A, 5.0mm protrusion through chassis |
| — | Diagnostic Bank-Alpha | 2×10 ENIG Gold looped probe pads | — | — | — | 2.54mm pitch, placed behind BtB header. Not a separate connector; probed directly with logic analyser clips |
| — | Diagnostic Bank-Beta | 2×10 ENIG Gold looped probe pads | — | — | — | 2.54mm pitch, L1 layer. Monitors 12-bit Sniffer, JTAG, SYS_RESET_N |
| — | JTAG Daughterboard link (to FT232H board) | 1×5 INPUT header + 1×10 JTAG header | — | — | — | 2.54mm ENIG male headers on Controller. JDB female headers mate here. USB 2.0 to CM5 internally |

### Stator Board

| Ref | Description | Part / Series | MPN | Mouser PN | DigiKey PN | Notes |
| ----- | ------------- | --------------- | ----- | ----------- | ------------ | ------- |
| J1-J3 | Rotor 1 interface sockets (1 slot × 3 connectors: JTAG ERF8-005, Power ERF8-005, ENC ERF8-010) — cross-ref Rotor/Design_Spec.md §3.4 | ERF8-005 (J1+J2) / ERF8-010 (J3) | 200-ERF8005050SDVKTR (J1+J2) / 200-ERF8010050SDVKTR (J3) | SAM13517CT-ND (J1+J2 CT) / SAM8618CT-ND (J3 CT) | C7273978 (J1+J2) / C3646170 (J3) | ERF8 0.8mm pitch female sockets. Rotor 1 input side only (serial chain — not 30 slots). J1 pin 6 = TTD (outgoing TDI). |
| J4-J6 | Encoder Port headers (×3: HID J4, Plugboard A J5, Plugboard B J6) — 26-pin 2×13 shrouded box header | Molex 22-23-2261 (2×13, 2.54mm) | 22-23-2261 | 538-22-23-2261 | WM2913-ND | THT, shrouded, keyed. Pinout definition owner — see Stator/Board_Layout.md J4–J6 |
| J7 | Extension/Reflector Link — 16-pin shrouded box header | Molex 22-23-2161 (2×8, 2.54mm) | 22-23-2161 | 538-22-23-2161 | WM2907-ND | THT, shrouded. Power, ENC_DATA, TTD_RETURN (pin 15). Pinout definition owner — see Stator/Board_Layout.md J7 |
| J8 | Link-Beta BtB — 40-pin plug to Controller Board | Samtec ERM8-020-05.0-S-DV-K-TR | ERM8-020 | 200-ERM8020050SDVKTR | SAM8611CT-ND | Male plug (ERM8). Mating female on Controller (ERF8-020). 40-pin per DEC-015 |
| — | JTAG Aux header | 2×5 2.54mm shrouded | — | — | — | Pin pattern: GND\|TCK\|GND\|TMS\|GND\|TDI\|GND\|SYS_RESET_N\|GND |

### Rotor Board (×30)

| Ref | Description | Part / Series | MPN | Mouser PN | DigiKey PN | JLCPCB Part # | Notes |
| ----- | ------------- | --------------- | ----- | ----------- | ------------ | ------- | ------- |
| J1 | JTAG input — ERM8 male header (input side; plugs into Stator J1 ERF8 or Extension J4 ERF8) | Samtec ERM8-005-05.0-S-DV-K-TR (10-pin, 0.8mm pitch) | ERM8-005 | 200-ERM8005050SDVKTR | 612-ERM8-005-05.0-S-DV-K-TRCT-ND | C3649741 | Male (ERM8). Input side. Authority: Rotor/Design_Spec.md §3.4 |
| J2 | Power input — ERM8 male header (3V3_ENIG ×5, GND ×5) | Samtec ERM8-005-05.0-S-DV-K-TR (10-pin, 0.8mm pitch) | ERM8-005 | 200-ERM8005050SDVKTR | 612-ERM8-005-05.0-S-DV-K-TRCT-ND | C3649741 | Male (ERM8). Input power side |
| J3 | ENC Data input — ERM8 male header (ENC_IN/ENC_OUT + GND) | Samtec ERM8-010-05.0-S-DV-K-TR (20-pin, 0.8mm pitch) | ERM8-010 | 200-ERM8010050SDVKTR | SAM8610CT-ND | C374877 | Male (ERM8). Input ENC data |
| J4 | JTAG output — ERF8 female socket (output side; receives next Rotor J1, Reflector J1, or Extension J1 ERM8 male) | Samtec ERF8-005-05.0-S-DV-K-TR (10-pin, 0.8mm pitch) | ERF8-005 | 200-ERF8005050SDVKTR | SAM13517CT-ND | C7273978 | Female (ERF8). Output side. R1 (75Ω) in TTD output path |
| J5 | Power output — ERF8 female socket (3V3_ENIG ×5, GND ×5) | Samtec ERF8-005-05.0-S-DV-K-TR (10-pin, 0.8mm pitch) | ERF8-005 | 200-ERF8005050SDVKTR | SAM13517CT-ND | C7273978 | Female (ERF8). Output power side |
| J6 | ENC Data output — ERF8 female socket (ENC_IN/ENC_OUT + GND) | Samtec ERF8-010-05.0-S-DV-K-TR (20-pin, 0.8mm pitch) | ERF8-010 | 200-ERF8010050SDVKTR | SAM8618CT-ND | C3646170 | Female (ERF8). Output ENC data |

### Encoder Board

| Ref | Description | Part / Series | MPN | Mouser PN | DigiKey PN | Notes |
| ----- | ------------- | --------------- | ----- | ----------- | ------------ | ------- |
| J1 (×64) | Plugboard cipher jack sockets (one per key/lamp position) | 6.35mm (¼″) mono switched panel-mount jack socket — already purchased (eBay: SaiBuy.Ltd item 334364197440) | — | — | — | THT panel-mount. 64× per board (26 input + 26 output + 10 plugboard positions + 2 spare). Purchased. |
| J2 | Data link to Stator — 26-pin 2×13 shrouded box header | Molex 22-23-2261 (2×13, 2.54mm) | 22-23-2261 | 538-22-23-2261 | WM2913-ND | Mating connector for Stator J4/J5/J6. Cross-ref: Stator/Board_Layout.md J4–J6 |
| J3 | Diagnostic looped probe pads | 2×8 ENIG Gold pads | — | — | — | 2.54mm pitch. Not a separate connector; probed directly |

### Reflector Board

| Ref | Description | Part / Series | MPN | Mouser PN | DigiKey PN | JLCPCB Part # | Notes |
| ----- | ------------- | --------------- | ----- | ----------- | ------------ | ------- | ------- |
| J1 | Rotor 30 output — JTAG (ERM8-005, 10-pin **male**, 0.8mm pitch) | Samtec ERM8-005-05.0-S-DV-K-TR | ERM8-005-05.0-S-DV-K-TR | 200-ERM8005050SDVKTR | 612-ERM8-005-05.0-S-DV-K-TRCT-ND | C3649741 | Plugs into Rotor 30 J4 (ERF8-005 female). Definition owner: Rotor/Design_Spec.md §3.4 |
| J2 | Rotor 30 output — Power (ERM8-005, 10-pin **male**, 0.8mm pitch) | Samtec ERM8-005-05.0-S-DV-K-TR | ERM8-005-05.0-S-DV-K-TR | 200-ERM8005050SDVKTR | 612-ERM8-005-05.0-S-DV-K-TRCT-ND | C3649741 | Plugs into Rotor 30 J5 (ERF8-005 female). Definition owner: Rotor/Design_Spec.md §3.4 |
| J3 | Rotor 30 output — ENC Data (ERM8-010, 20-pin **male**, 0.8mm pitch) | Samtec ERM8-010-05.0-S-DV-K-TR | ERM8-010-05.0-S-DV-K-TR | 200-ERM8010050SDVKTR | SAM8610CT-ND | C374877 | Plugs into Rotor 30 J6 (ERF8-010 female). Definition owner: Rotor/Design_Spec.md §3.4 |
| J4 | Interconnect to Stator/Extension — 16-pin shrouded box header | Molex 22-23-2161 (2×8, 2.54mm) | 22-23-2161 | 538-22-23-2161 | WM2907-ND | N/A — Molex Milli-Grid, not stocked at JLCPCB; order from Mouser/DigiKey | Mating connector for **Stator J7** (or Extension J7/J8). Carries TTD_RETURN on pin 15. |
| J5 | Diagnostic looped probe pads | 2×8 ENIG Gold pads | — | — | — | N/A | 2.54mm pitch. Not a separate connector; probed directly |

### Extension Board

| Ref | Description | Part / Series | MPN | Mouser PN | DigiKey PN | JLCPCB Part # | Notes |
| ----- | ------------- | --------------- | ----- | ----------- | ------------ | ------- | ------- |
| J1 | Rotor group input — JTAG (ERM8-005, 10-pin **male**, 0.8mm pitch) | Samtec ERM8-005-05.0-S-DV-K-TR | ERM8-005-05.0-S-DV-K-TR | 200-ERM8005050SDVKTR | 612-ERM8-005-05.0-S-DV-K-TRCT-ND | C3649741 | Plugs into previous rotor group's last rotor J4 (ERF8-005 female). Cross-ref: Rotor/Design_Spec.md §3.4 |
| J2 | Rotor group input — Power (ERM8-005, 10-pin **male**, 0.8mm pitch) | Samtec ERM8-005-05.0-S-DV-K-TR | ERM8-005-05.0-S-DV-K-TR | 200-ERM8005050SDVKTR | 612-ERM8-005-05.0-S-DV-K-TRCT-ND | C3649741 | Plugs into previous rotor group's last rotor J5 (ERF8-005 female). |
| J3 | Rotor group input — ENC Data (ERM8-010, 20-pin **male**, 0.8mm pitch) | Samtec ERM8-010-05.0-S-DV-K-TR | ERM8-010-05.0-S-DV-K-TR | 200-ERM8010050SDVKTR | SAM8610CT-ND | C374877 | Plugs into previous rotor group's last rotor J6 (ERF8-010 female). |
| J4 | Rotor group output — JTAG (ERF8-005, 10-pin female, 0.8mm pitch) | Samtec ERF8-005-05.0-S-DV-K-TR | ERF8-005-05.0-S-DV-K-TR | 200-ERF8005050SDVKTR | SAM13517CT-ND | C7273978 | Receives next rotor group's first rotor J1 (ERM8-005 male). Cross-ref: Rotor/Design_Spec.md §3.4 |
| J5 | Rotor group output — Power (ERF8-005, 10-pin female, 0.8mm pitch) | Samtec ERF8-005-05.0-S-DV-K-TR | ERF8-005-05.0-S-DV-K-TR | 200-ERF8005050SDVKTR | SAM13517CT-ND | C7273978 | Receives next rotor group's first rotor J2 (ERM8-005 male). |
| J6 | Rotor group output — ENC Data (ERF8-010, 20-pin female, 0.8mm pitch) | Samtec ERF8-010-05.0-S-DV-K-TR | ERF8-010-05.0-S-DV-K-TR | 200-ERF8010050SDVKTR | SAM8618CT-ND | C3646170 | Receives next rotor group's first rotor J3 (ERM8-010 male). |
| J7 | Extension Port IN — 16-pin 2×8 shrouded box header | Molex 22-23-2161 (2×8, 2.54mm) | 22-23-2161 | 538-22-23-2161 | WM2907-ND | N/A — Molex Milli-Grid, not stocked at JLCPCB; order from Mouser/DigiKey | Mating connector for Stator J7 (or previous Extension J8). Cross-ref: Stator/Board_Layout.md J7 |
| J8 | Extension Port OUT — 16-pin 2×8 shrouded box header | Molex 22-23-2161 (2×8, 2.54mm) | 22-23-2161 | 538-22-23-2161 | WM2907-ND | N/A — Molex Milli-Grid, not stocked at JLCPCB; order from Mouser/DigiKey | Feeds next Extension J7 or Reflector J4. Cross-ref: Stator/Board_Layout.md J7 |
| J9 | Diagnostic looped probe pads | 2×8 ENIG Gold pads | — | — | — | — | 2.54mm pitch. Not a separate connector |

### JTAG Daughterboard (FT232H)

| Ref | Description | Part / Series | Notes |
| ----- | ------------- | --------------- | ------- |
| J1 | INPUT header — 5V_USB, 3V3_ENIG, D+, D−, GND | 1×5 2.54mm female IDC | Power in (5V_USB + 3V3_ENIG) + internal USB 2.0 to CM5 via hat-header |
| J2 | JTAG OUTPUT header (10-pin interleaved GND) | 1×10 2.54mm female IDC | TCK/GND/TDI/GND/TDO/GND/TMS/GND/VREF/GND |

---

> **Note for manual review:** Items marked `???` or `⚠️ verify` require confirmation before the BOM is finalised for procurement. In particular: Encoder J1 plug/jack type has not been selected;
> Controller J1 (ERF8) DigiKey PN SAM8621CT-ND (confirmed); Power Module J3 (43650-0519) DigiKey WM14587-ND (confirmed).

---

## Open Work Items

The following items have been identified as future tasks. They are not yet scheduled but must not be forgotten.

### OWI-001 — Test Coupons per Board

Add test coupon footprints to each board design to simplify manufacturing test and functional verification.
Each board must be specified independently, as the relevant test signals and accessible nets will differ per board.

### OWI-002 — PAS Definitions per Board

Define Provisional Acceptance Specifications (PAS) for each board, covering:

- **Basic board testing** — power-on checks, continuity, short detection.
- **Functional testing via coupons** — using coupon connections to real external devices to verify board functionality
  end-to-end (e.g. JTAG chain continuity, signal integrity, CPLD programming verification).

Each board must be specified independently.

### OWI-003 — VHDL Pseudo-Code and CPLD Configuration Plans

For each CPLD in the system, create:

- A configuration plan describing the intended logical function, I/O assignments, and state machine behaviour.
- Pseudo-code or annotated VHDL stubs ready for handoff to software development.
- Notes on how the VHDL can be exercised during PAS testing (OWI-002) to verify functional correctness.

Boards with CPLDs requiring this work: Encoder (×2), Stator (×1), Rotor (×1 per rotor, ×30 total).
