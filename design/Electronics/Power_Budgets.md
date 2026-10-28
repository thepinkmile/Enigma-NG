# Enigma-NG Power Budgets

**Status:** Draft
**Version:** v.0.1.0
**Associated Hardware Revision:** Rev A
**Last Updated:** 2026-10-28

---

## Design Constraint Hierarchy

1. **TPS75733KTTRG3 LDO** (Power Module U7): **3.0A maximum output** - hard limit, component not to be changed.
2. **PM dock `J1` 3V3_ENIG allocation:** `2 x 3V3_ENIG` contacts at 6A/contact - comfortably above the LDO limit.
3. **Cypher Board dock `J5` 3V3_ENIG allocation:** signal-pitch contacts carry `3V3_ENIG`, rated well above the LDO limit - connector is not the bottleneck, the LDO is.
4. **Available to Cypher Board + Rotor stack:** LDO output minus Controller-local consumption (CM5 GPIO reference, pull-ups, and local housekeeping) ≈ 2.95A (Controller overhead ≤ 50mA).

---

## 3V3_ENIG Load Analysis

### Per-Device Current (Programmable Hardware IC [CPLD/FPGA] - Cypher Board, Encoder Modules, Rotor x30 @ 3.3V)

| Operating condition | ICC (core) | Source |
| :--- | :--- | :--- |
| Static (no switching) | ~5 mA | Intel MAX II Datasheet ICC_STATIC |
| Typical cipher logic (50 MHz toggle) | ~25 mA | Intel MAX II Power Estimator (50% toggle, 50% resource use) |
| Worst-case (100 MHz, 80% resource use) | ~80 mA | MAX II Datasheet ICC_DYNAMIC worst case |

**Design value used:** 50 mA per CPLD (conservative typical - accounts for VHDL cipher switching without
being an unachievable worst-case peak).

### Per-Device Current (TI FDC2114RGHR Capacitive Sensor IC @ 3.3V)

| Condition | ICC |
| :--- | :--- |
| Active | 2.1 mA typ |

---

## 3V3_ENIG Allocation Table

| Consumer | Count | Per-unit (mA) | Total (mA) | Notes |
| :--- | :---: | :---: | :---: | :--- |
| Cypher Board CPLD (U1, EPM570T100I5N) | 1 | 50 | 50 | JTAG forwarding + ENC signal routing |
| HID Encoder Modules (Cypher-Input + Cypher-Output, 1 each) | 2 | 50 | 100 | Keyboard encode + lightboard decode CPLDs |
| Cypher Board Plugboard-pass Encoder Modules (Pass A) | 2 | 50 | 100 | Stecker pass A encode/decode pair |
| Cypher Board Plugboard-pass Encoder Modules (Pass B) | 2 | 50 | 100 | Stecker pass B encode/decode pair |
| FT232H (Cypher Board USB-JTAG bridge; VREGIN+VCCD+VCCIO+VPLL+VPHY, all 3V3_ENIG) | 1 | 100 | 100 | Self-powered, Rev C silicon, 3.0-3.6V `VREGIN`; see DEC-102 |
| Rotor CPLDs (EPM570T100I5N x30) | 30 | 50 | 1500 | All rotors cipher-active simultaneously |
| Rotor FDC2114RGHR capacitive sensor ICs (U2/U3 or U2/U4, 2 ICs per rotor, 60 ICs total) | 60 | 2.1 | 126 | Continuous position polling; two ICs per rotor add 4.2 mA to the 50 mA CPLD budget, giving 54.2 mA typ / 55 mA budget per rotor |
| INA219 current monitor (Cypher Board) | 1 | 1 | 1 | Negligible |
| INA219 current monitor (Power Module) | 1 | 1 | 1 | Negligible |
| Cypher Board GPIO expanders (MCP23017 x3) | 3 | 10 | 30 | `U6`, `U7`, `U8` on `I2C1`; monitor / control overhead only |
| PM-local GPIO expander (PCA9534A x1) | 1 | 5 | 5 | `U14 @ 0x3F`; PM status + SW1 runtime RGB handoff control |
| User Settings Module colour-value store logic | 1 | 10 | 10 | `U1 @ 0x39` (TBD part) on `I2C2`; placeholder. LED banks are driven by the Cypher-Input/Cypher-Output boards (see the `5V_MAIN Load Analysis` table below), not locally on this board; buzzer path (`BZ1`) is still a placeholder, see `User_Settings_Module/Design_Spec.md §3` |
| Stack-Input JTAG buffer ICs (SN74LVC2G125DCUR, one per mini-stack) | 6 | 2 | 12 | TCK/TMS re-drive for each mini-stack's 5-rotor chain; negligible load |
| Stack-Input STM32G071K8T3TR MCUs (native Actuation Module, one per mini-stack) | 6 | 5 | 30 | Placeholder conservative estimate (Run mode ~2.9 mA typ @ 24 MHz per local `stm32g071.md` Table `IDD(Run)`, rounded up for GPIO/peripheral overhead); actual figure TBD once firmware clock configuration and solenoid driver circuit are finalised - see `Stack-Input/Design_Spec.md §4` |
| Controller-local housekeeping | - | - | 50 | Controller overhead subtracted before Cypher Board distribution |
| **Typical total** | | | **2,215 mA** | |
| **Rounded budget** | | | **≤ 2.22 A** | |

### Headroom vs LDO Limit

| Limit | Value | Margin |
| :--- | :--- | :--- |
| LDO hard limit | 3.00 A | - |
| Typical worst-case load | 2.22 A | **+0.78 A (26%)** |
| Controller↔Cypher Board dock capacity | Above 3.00 A | Not the constraint |

> ✔ **Conclusion:** The 3A TPS75733KTTRG3 LDO provides ~26% headroom above the full downstream
> worst-case typical load.
> No LDO upgrade is required for the current 30-rotor design.
> **Telemetry note:** The Cypher Board INA219 / shunt path still measures the rotor-stack
> distribution branch at about **2.05 A typical**. The extra **~170 mA** above that figure is the
> User Settings Module colour-value store's placeholder logic load, the Stack-Input JTAG buffer
> and STM32G071 MCU placeholders, and the FT232H's full 3.3V-`VREGIN` draw on the shared
> `3V3_ENIG` rail.

---

### INA219 Shunt Selection

The rotor-stack and 5V_MAIN current-telemetry paths both use a **10 mΩ
CSS2H-2512R-R010ELF** shunt (Bourns 2512 Kelvin-sense, 10mΩ ±1%, 5A):

* V_drop at 2.05A: 2.05 x 0.010 = **20.5 mV** - within INA219 ±80 mV PGA range.
* V_drop at 3.00A max: 3.00 x 0.010 = **30 mV** - within ±80 mV range.
* Resolution: with 12-bit ADC at ±80 mV range, LSB = 2x80mV/4096 ≈ **39 µV/LSB** → I_LSB = 39µV/0.010Ω ≈ **4 mA** current resolution.
* Power dissipation at 2.05A: 2.05² x 0.010 = **42 mW** - 2512 Kelvin package (rated ≥0.5W) is adequate with >10x margin.
* Power dissipation at 3.00A max: 3.00² x 0.010 = **90 mW** - 2512 Kelvin package ≥0.5W still OK.
* CAL register: 0x0400 (1024). CAL = 0.04096 / (Current_LSB x R_SHUNT) = 0.04096 / (0.004 x 0.010) = 1024 ✔
* Part: CSS2H-2512R-R010ELF. Used on **PM R10** (LTC3350 RSENSE), **PM R16** (INA219 U10, 0x40, 5V_MAIN monitoring) and **Cypher Board R1**
  (INA219 U2, 0x40, rotor-stack monitoring — same address as PM's U10, safe since the two devices are on independent I²C buses; see DEC-101).
  Total build qty: 3.

---

## 5V_MAIN Load Analysis

| Consumer | Current | Notes |
| :--- | :--- | :--- |
| CM5 (Raspberry Pi Compute Module 5) | 5.0 A max | CM5 boot-to-load current profile; 25W at 5V = 5A |
| 3V3_ENIG LDO quiescent (TPS75733KTTRG3) | 2.05 A | Sourced from 5V_MAIN; P_in = 5V x 2.05A = 10.25W |
| Status LEDs, RJ45, misc. | 0.1 A | |
| USB 3.0 external devices (TPS2065C rated max) | 1.60 A | System boundary: connected USB device load; TPS2065C hard-limits output |
| HDMI sink device | 0.05 A | System boundary: connected HDMI sink; AP2331W-limited |
| User Settings Module audio/logic rail (via Cypher Board Hub Connector Template) | TBD | LED banks are driven by the Cypher-Input/Cypher-Output boards (see the LED bank rows below), not locally on this board; this board's own local draw is the colour-value store logic (already counted in the `3V3_ENIG Allocation Table` above) plus the still-undecided buzzer (`BZ1`) - see `User_Settings_Module/Design_Spec.md §3`. Treated as negligible (≤0.05 A) until the buzzer part is selected; revisit once `.copilot/todos/usm-buzzer-audio-options.md` is resolved |
| Cypher-Input LED bank (via Cypher Board dock, 64-Character variant worst case) | 1.26 A | 42 LEDs x 3 colour channels x 10mA, all channels simultaneously active (mixed colour, e.g. white/yellow/cyan); broadcast onward to whichever Cypher-Output board is installed - see `Cypher-Input/Design_Spec.md §5`/§7 |
| Cypher-Output LED bank (via Cypher Board dock, any variant - worst case is variant-independent) | 0.03 A | Only one lens position is ever lit at a time (one-hot decode); 1 lens x 3 colour channels x 10mA, all channels simultaneously active (mixed colour); local `5V_MAIN`-sourced colour-bank switching (U1-U3) - see `Cypher-Output/Design_Spec.md §4`/§7 |
| Stack-Input Board solenoid actuation (via Cypher Board `J4` power dock → mini-stack `5V_MAIN`, one native instance per mini-stack) | 0.50 A | Placeholder worst-case figure; solenoid driver circuit and actual current are still TBD in `Stack-Input/Design_Spec.md §4` pending a future design discussion - revisit once finalised |
| **Total 5V_MAIN worst case (system boundary)** | **10.59 A** | |
| **LMQ61460-Q1 dual-phase capacity** | **12.0 A** | 88.3% utilisation (10.59/12.0) - reduced margin, see note below |

> **Scope note:** The 7.15 A board-level budget (internal consumers: CM5 + LDO + misc) covers internal consumers only.
> External device loads (USB 3.0 + HDMI) plus the Cypher-Input and Cypher-Output LED bank loads
> and the Stack-Input solenoid load add 3.44 A, giving a system total of 10.59 A.
> Component utilisation figures (e.g. LMQ61460-Q1) are calculated against the 10.59 A system total.
>
> **Reduced margin note:** the Cypher-Input LED bank's worst-case 1.26 A (64-Character variant,
> all 3 colour channels simultaneously active) accounts for the majority of the system's LMQ61460-Q1
> dual-phase utilisation. This worst case assumes a mixed colour (not a single primary channel) is
> selected and every LED position is populated (64-Character variant, the largest); the 26-Char
> Classic and 10-Numeric variants draw proportionally less (0.78 A and 0.36 A worst case
> respectively). Cypher-Output's own LED bank adds only a further 0.03 A worst case, since only
> one Cypher-Output lens is ever lit at a time regardless of variant (unlike Cypher-Input's
> whole-key-bank illumination). Current utilisation is **88.3%** - still within capacity, but with
> materially less headroom than the board's other consumers alone would require. Revisit this
> margin once the LED part is confirmed (see `merge-missing-components.md`) and actual per-channel
> current is finalised - 10mA/channel is a target, not a measured figure.
>
> **Cypher Board dock 5V margin:** The Cypher-Board-facing 5V branch uses signal-pitch `5V_MAIN`
> contacts on the dedicated Molex `J4` dock, with additional return capacity in the companion
> ground contacts / guards. The current downstream budget remains **0.74 A**, so the dock is not
> the limiting factor for Cypher-Board-side 5V peripherals.
