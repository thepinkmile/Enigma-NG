# Power Module (V1.0) Design Specification

**Status:** Draft
**Project:** Enigma-NG
**Author:** Izzyonstage & GitHub Copilot
**Version:** v1.0.0
**Associated Hardware Revision:** Rev A
**Last Updated:** 2026-04-05

## 1. Overview

This Power Module is a custom power board that is independently shielded and protected to ensure all power sources are filtered, controlled and monitored.
It provides the basis of the clean power rails into the controller board and other peripheral boards.
It produces 2 power rails from a common ~12V input source. These power rails are:

* **5V_MAIN** Providing up to 12A for powering the CM5 module (dual-phase interleaved LMQ61460AFSQRJRRQ1).
* **3V3_ENIG** Providing clean 3.3V power for CPLDs, USB-JTAG interface, I2C logic, status indicator logic, and the full rotor stack.

**NOTE (DEC-001):** The **3V3_SYSTEM** rail name is retired. The **3V3_ENIG** rail (generated on this Power Module by the TPS75733 LDO) is the unified 3.3V rail supplying
CPLDs, USB-JTAG logic, and system peripherals (USB, HDMI, Ethernet). 3V3_ENIG power crosses to the Controller Board via BtB Link-Alpha pins 39–44.

* **Controller Link (Link-Alpha):** 80-pin ERM8 connector for power/ethernet/telemetry handshake with the Controller Board.
  * **Provided to Controller:** 5V_MAIN, 3V3_ENIG, GBE signals, and PWR_GD.
  * **Returned by Controller (CTRL→PM via LINK-ALPHA):** Status LED drive signals (SW_LED_R, SW_LED_G, SW_LED_B / SW_LED_CTRL), Ethernet LED signals (ETH_LED_LINK, ETH_LED_ACT), and ROTOR_EN.
  * **Cross-ref:** For the exact Link-Alpha mapping and signal naming conventions, See:
    * `Controller/Design_Spec.md`

### Functional & Design Requirements

#### Functional Requirements

| ID | Functional Requirement | Notes | Satisfied By / Cross-Ref |
| :--- | :--- | :--- | :--- |
| FR-PM-01 | Convert PoE (802.3bt Type 4) input to regulated 5V and 3.3V system power rails | Primary power source for the entire system | §2 Power & UPS Hub; BOM U9 (TPS2372-4), U10 (TPS23730), U2A/U2B (LMQ61460AFSQRJRRQ1), U7 (TPS75733) |
| FR-PM-02 | Maintain system power for ≥14.5 s after mains/PoE loss | Provides controlled-shutdown window for the CM5 OS | §2 Power & UPS Hub; BOM U3 (LTC3350), C_SC1–4 (supercaps) |
| FR-PM-03 | Assert PWR_GD (active-HIGH) to CM5 while 5V_MAIN ≥ 4.5V; deassert LOW on power-loss event to trigger graceful shutdown | Enables software-initiated graceful shutdown; PWR_GD is healthy-HIGH, fault-LOW | §5 Protection & Logic; BOM U8 (MCP121T-450E) |
| FR-PM-04 | Distribute 5V_MAIN and 3V3_ENIG to the Controller Board via the Link-Alpha BtB connector | Single connector for all power and telemetry | §2 Power & UPS Hub; BOM J1 (ERM8-040) |
| FR-PM-05 | Monitor output voltage and current on each rail and report via I2C | Telemetry for runtime health monitoring | §3 Telemetry & Power Management; BOM R7, R8 (I2C pull-ups), U12 (INA219 at 0x40), R23 (10mΩ shunt) |
| FR-PM-06 | Protect downstream circuitry from overcurrent, overvoltage, and inrush | Hardware protection independent of software | §5 Protection & Logic; BOM U1 (TPS25980 eFuse), R1–R3 |

#### Design Requirements

| ID | Design Requirement | Specification | Satisfied By / Cross-Ref |
| :--- | :--- | :--- | :--- |
| DR-PM-01 | Input supply | PoE 802.3bt Type 4 (Class 8), 44–57 V, ≤72 W | §5 Protection & Logic; BOM U9 (TPS2372-4), J2 (RJ45) |
| DR-PM-02 | 5V_MAIN rail | 5.0 V ±2%, ≥5 A continuous; 9.0 A capacity via Link-Alpha (18 pins × 0.5 A/pin) | §2 Power & UPS Hub; BOM U2A/U2B (LMQ61460AFSQRJRRQ1) |
| DR-PM-03 | 3V3_ENIG rail | 3.3 V ±3%, ≤3.0 A maximum (TPS75733 LDO hard limit) | §5 Protection & Logic; BOM U7 (TPS75733) |
| DR-PM-04 | Buck converter | Dual-phase interleaved LMQ61460AFSQRJRRQ1 pair | §2 Power & UPS Hub; BOM U2A/U2B (LMQ61460AFSQRJRRQ1) |
| DR-PM-05 | LDO | TPS75733 (3.3 V, 3.0 A, TO-263 (KTT) 5-pin 10.16×15.24 mm) | §5 Protection & Logic; BOM U7 (TPS75733) |
| DR-PM-06 | eFuse | TPS25980, 7 A trip current, OVLO = 16.9 V (R_OVLO = ERA-3ARB5362V (53.6 kΩ, 0.1% thin-film)) | §5 Protection & Logic; BOM U1 (TPS25980), R1 (232kΩ), R2 (28.7kΩ), R3 (53.6kΩ) |
| DR-PM-07 | Supercapacitor bank | 4× 22 F / 2.7 V in 2S2P configuration = 22 F effective at 5.4 V | §2 Power & UPS Hub; BOM U3 (LTC3350), C_SC1–4 |
| DR-PM-08 | Backup activation threshold | 4.40 V (R14 = 26.7 kΩ, ERA-3ARB2672V) | §5 Protection & Logic; BOM R14 (26.7kΩ), R15 (10.0kΩ) |
| DR-PM-09 | Holdup duration | ≥14.5 s at 5 W load (CM5 idle power) | §2 Power & UPS Hub; BOM C_SC1–4 (22F/2.7V), U3 (LTC3350) |
| DR-PM-10 | Link-Alpha connector | ERM8-040-05.0-S-DV-K-TR (80-pin male, 0.8 mm pitch, 5.0 mm stack height) | BOM J1 (ERM8-040-05.0-S-DV-K-TR) |
| DR-PM-11 | PCB stackup | 6-layer, 2oz finished copper (JLC06161H-2116) | §1 PCB Architecture |

## 2. Design

> **NOTE:** All global rules defined in the Global_Routing_Spec.md should be applied to this design.

### 1. PCB Architecture

* **Stackup:** 6-Layer / 2oz Finished Copper (JLC06161H-2116).
  For production runs requiring verified controlled impedance, specify JLCPCB's 'Controlled Impedance'
  service (TDR-verified, ±10% tolerance). Prototype orders may omit this service per DEC-017
  (calculated trace widths within ±10% of target based on JLC06161H-2116 datasheet parameters).
* **Substrate:** High-Tg FR4 for thermal stability.
* **Finish:** ENIG (Gold) for all user-touch points and thermal pads.
* **Enclosure:** 42mm Aluminium "Power Can" with internal compression ribs.
* **Thermal:** Cross-Hatched Exposed ENIG "Thermal Halos" (2mm offset) at mesh intersections.
  * **Vias:** Type VII (Epoxy-filled & Capped) Hexagonal Thermal Via Matrix.
* **Supercap Block:** 2×2 arrangement (4 cells, 14mm centre-to-centre pitch, 2.0mm air gap between cells). Block footprint ≈ 28mm × 28mm.
  The 2.0mm gap is a 'No-Fly Zone' for all PCB traces on L1–L4 (enclosure rib clearway).
* **Routing Keep-out:** 32mm × 32mm shadow zone on L1/L2 beneath the Supercap Block — only GND_CHASSIS copper and Type VII thermal vias permitted within this zone.

### 2. Power & UPS Hub

* **Storage:** LTC3350-managed supercap bank — 4× Tecate TPLH-2R7/22WR12X31 (22F/2.7V, −40°C to +85°C, 12mm dia × 31mm, THT radial) in 2S2P configuration on 5V_MAIN bus. Total: 22F at 5.4V. Hold-up

  energy: 72.4J (≥14.5 seconds at 5W CM5 shutdown load). Supercap manager: LTC3350 (QFN-38, 5×7mm), handles charging, cell balancing, and hold-up switchover.

* **Battery Interface:** 5-pin Locking Micro-Fit (Molex 43650-0519 — vertical THT, gold contacts, board lock).
  * Pins 1-2: VBATT (14.4V Nominal).
  * Pins 3-4: SMBus (SDA/SCL) with local ESD protection.
  * Pin 5: BATT_PRES_N (Presence Detect).
  * **BMS Charge Voltage:** Smart Battery BMS must be configured for a maximum charge voltage of **4.1V/cell (16.4V total for 4S)**. This provides a ≥0.5V margin to the TPS25980 eFuse 16.9V OVLO

    threshold, preventing nuisance latch-off at full charge. BMS configurations using 4.2V/cell (16.8V) are not compatible without OVLO re-specification.

* **Presence Logic:** Pin 5 is pulled to **3V3_ENIG** via 10kΩ resistor (R6). Battery internal shorts Pin 5 to GND.
  * Logic HIGH: Battery Disconnected.
  * Logic LOW: Battery Detected.
* **Protection:** TPD1E10B06 TVS diode on the Presence line plus a dedicated 2-channel TVS array on the SMBus lines to protect the battery interface during insertion.
* **Stabilizer:** Solder-mask opening "KLEBER-ZONE" for RTV Silicone adhesive.
* **Indicators:** Green "LOGIK-BEREIT" LED + 5.1V Zener Amber "Safety Glow" LED.
* **Z-Height:** 42mm minimum clearance for Tecate TPLH-2R7/22WR12X31 cells (31mm body + 10mm pin/clearance = 41mm). Thermal pad zone provides additional standoff clearance.
* **Interface:** Gelid GP-Ultimate (15 W/mK) pad on an **Exposed ENIG** bottom zone to Aluminium Enclosure with internal compression ribs.

### 3. Telemetry & Power Management

* **I2C Telemetry:** 4.7kΩ (1%) pull-up resistors (**R7, R8**) on SDA/SCL lines, tied to **3V3_ENIG**.
* **5V_MAIN Current Monitor:**
  * **Purpose:** Provides real-time current/voltage telemetry for the 5V_MAIN rail to the CM5.
  * **Sensor:** TI INA219AIDR (U12) zero-drift power monitor at I²C address **0x40**.
  * **Placement:** Inserted in the 5V_MAIN supply path on L1, downstream of the eFuse (TPS25980).
  * **Shunt:** CSS2H-2512R-R010ELF (10mΩ ±1% 5A, 2512 Kelvin-sense) — PM R23 instance.
    (Stator R1 is the third system CSS2H; total build qty: 3 — see `Power_Budgets.md`.)
  * **Interface:** I2C-1 Telemetry Bus, directly accessible via LINK-ALPHA to the Controller.
  * **Filtering:** 0.1µF decoupling and RC filter on IN+/IN- for supply noise suppression.
  * Satisfies FR-PM-05.
* **Reset Logic:** 10kΩ (1%) pull-up (**R9**) on SYS_RESET_N to prevent floating states.
* **Battery Detection:** Dedicated BATT_PRES_N signal routed to CM5 GPIO 23.

### 4. EMI & Filtering (The "Iron Curtain")

The input filter uses a two-stage common-mode (CM) choke cascade followed by a differential-mode (DM) Pi-filter. This architecture addresses both CM and DM conducted noise across the full EN 55032
Class B frequency range (150kHz–30MHz).

**Filter Topology (power flow left → right):**

```text
VIN_RAW ─┬─[L1: WE-CMBNC CM Choke]─[L2: WE-CMBNC HF CM Choke]─┬─[L3: 10µH DM]─┬─ VIN_BUS (to eFuse)
          │   (Nanocrystalline)       (High-Freq Ferrite)     │               │
         [C1] 22µF } input-side                              [C4] 22µF }  output-side
         [C2]  1µF }   Pi leg                                [C5]  1µF }    Pi leg
         [C3] 100nF}  (to GND)                               [C6] 100nF}   (to GND)
          │                                                   │               │
GND ──────┴───────────────────────────────────────────────────┴───────────────┴─ GND
```

> **Note:** L1 and L2 are common-mode chokes — each has two coupled windings, one in the +VIN line and one in the GND return line. C1–C3 (input) and C4–C6 (output) are single capacitors to GND
> (differential filter caps).

**Stage 1 — Primary CMC (L1: WE-CMBNC Nanocrystalline):**

* Part: **Würth WE-CMBNC**, nanocrystalline core, ≥10A rated, ≥1.5mH CM inductance (e.g. 748441440 or equivalent — verify from Würth REDEXPERT tool; mouser.co.uk search: "WE-CMBNC 10A

  nanocrystalline").

* Function: Broadband CM attenuation from ~1kHz to >10MHz. Nanocrystalline core maintains high permeability (µ_r > 50,000) well into the MHz range, providing >60dB CM insertion loss at 150kHz.

**Stage 2 — Secondary HF CMC (L2: Würth WE-CMBNC 7448031002):**

* Part: **Würth WE-CMBNC 7448031002** — same part as L1 (nanocrystalline CMC, THT, ≥10A). Original Laird CM5022 is discontinued (Laird EMC passives absorbed by TE Connectivity 2019). Twin

  nanocrystalline CMC approach provides broadband CM coverage 1kHz–30MHz. ⚠️ Re-evaluate at EMC pre-compliance test.

* Function: Supplementary CM attenuation above ~10MHz where nanocrystalline core permeability falls off. Provides a second CM filter pole to ensure >40dB CM attenuation to 30MHz+.

* **Fallback option:** If WE-CMBNC 7448031002 becomes unavailable, a ferrite-core CMC (e.g. Würth WE-CMB 744860220 or equivalent ≥10A ferrite THT CMC) may be substituted for L2 only.
  Ferrite CMCs have lower CM inductance below ~10kHz but perform equivalently above 1MHz. ⚠️ Re-verify CM insertion loss at 150kHz with the ferrite substitute before schematic freeze
  — add an external X2 cap (e.g. 10nF Y1-rated) across the CM choke if >6dB insertion loss is lost at 150kHz.

**Stage 3 — Differential Mode Pi-filter (L3, C1–C6):**

*Component selection:*

* **L3** — Bourns `SRP1265A-100M`: 10µH, 15.5A I_sat, 10A I_rms, DCR = 16.5mΩ max, 13.5×12.5×6.2mm shielded molded SMD. ⚠️ Footprint differs from original Würth 7447789100 (12.5×12.5mm); update PCB

  land pattern.

* **C1, C4** — 22µF, 25V, X7R, 1210 (Samsung CL32B226KAJNNNE or equiv).
* **C2, C5** — 1µF, 50V, X7R, 0805 (Kemet C0805C105K5RACTU or equiv).
* **C3, C6** — 100nF, 50V, X7R, 0402 (Samsung CL05B104KB5NNNC or equiv).

*Filter performance calculations:*

* Effective capacitance per Pi leg: C₁‖C₂‖C₃ = 22µF + 1µF + 100nF ≈ **23.1µF** (capacitors in parallel).
* Pi-filter −3dB corner frequency: `f_c = 1/(2π√(L3 × C)) = 1/(2π × √(10µH × 23.1µF))` = **10.5kHz**.
* DM attenuation at 150kHz (EN 55032 Class B lower limit): 40dBdec × log(150k/10.5k) ≈ **−46dB** ✓
* DM attenuation at 200kHz (TPS23730 ACF switching): ≈ **−51dB** ✓
* DM attenuation at 400kHz (LMQ61460AFSQRJRRQ1 buck switching): ≈ **−63dB** ✓
* Combined with dual CMC stages: total insertion loss well exceeds EN 55032 Class B limits across 150kHz–10MHz.

*Broadband capacitor stack rationale:*

* C1/C4 (22µF): bulk DM filtering at f_c and 2nd–3rd harmonics.
* C2/C5 (1µF): mid-frequency bypass; bridges impedance gap between 22µF ceramic SRF (~3MHz) and 100nF.
* C3/C6 (100nF): HF bypass; low impedance at >10MHz where bulk caps become inductive.
* All caps: 50V rating provides >3× voltage margin over 17V max input; X7R stable over −55°C to +125°C.

**Shielding:** Vintage Silver Aluminium enclosure screwed to `GND_CHASSIS` ears — provides a Faraday shield for the entire Power Module, supplementing conducted filtering with radiated attenuation.

> **Note on L1/L2 placement:** L1 and L2 are cascaded common-mode chokes on the **combined post-OR-ing bus** (VIN_RAW), not per-input filters.
> All three input sources (PoE, USB-C, Battery) are OR-ed first via Q1–Q3 and U6a/U6b/U6c, then the combined rail passes through L1→L2→L3 before reaching the eFuse (U1).
> Only the Battery input (J3) has no dedicated input-side ESD filter — D1/D2 provide transient protection at the connector.

### 5. Protection & Logic

* **External Handshake:** STUSB4500 (Standalone Sink) negotiates **15V/5A** (75W) from Wall adapter or USB-C PD source.
* **Internal Handshake:** TPS25751 PD Emulator (U4) provides **5V/5A** "Clean PD" profile to CM5.
* **Protection:** LM74700-Q1 controls the triple-input OR-ing network and drives Q1-Q3 PowerPAK ideal-diode FETs.
* **OR-ing Priority:** PoE (12V) is the lowest-voltage source and would be silently bypassed by passive OR-ing in favour of USB-C (15V). The LM74700-Q1 USB-C path enable pin is driven by the

  TPS2372-4 `/PG` signal — when PoE is live, the USB-C path is actively disabled. Battery path activates only if both PoE and USB-C are absent.

* **eFuse:** TPS25980 (16.9V OVLO fixed variant, VQFN 4×4mm) — 7A ILIM, 11.0V UVLO, 16.9V OVLO, 3mΩ RON (typ.).
  * R-Ladder: 232kΩ R_UVLO_HI, 28.7kΩ R_UVLO_LO, 53.6kΩ R_OVLO — all 0.1% Thin-Film 0603.
  * **Latch-off Recovery:** TPS25980 latches off on OVLO, UVLO, or sustained overcurrent. Recovery requires pulling the EN pin LOW (>1ms) then HIGH.
    **SW1 (power toggle rocker) achieves this** — flip SW1 to OFF (EN pulled to GND via SW1 → eFuse latch reset), fix the fault condition,
    then flip SW1 back to ON (EN pulled HIGH via R22 → normal operation resumes). At least one input source (PoE, USB-C, or
    Battery) must remain present so VIN_BUS is available when the eFuse re-enables.
  * ⚠️ If all three input sources are simultaneously absent, the supercap bank must be recharged before the system will restart. No dedicated reset button is needed beyond SW1.
* **Supercap Manager:** LTC3350 (QFN-38, 5×7mm) on 5V_MAIN bus. Manages 4-cell bank (2S2P, 22F/5.4V); provides 0.5A soft-charge current limit; automatic hold-up switchover on 5V_MAIN loss.
  * **RICHARGE calculation:** `ICH = VICHARGE / (RICHARGE × RSENSE)` where:
    * `VICHARGE = 1.485V` (LTC3350 internal reference).
    * `RSENSE = 10mΩ` (R_SENSE, 2512 package, in charging path).
    * For `ICH = 0.5A`: `RICHARGE = 1.485V / (0.5A × 0.010Ω) = 297Ω → use 301Ω (E96, 0.1%, 0603)`.

  * ⚠️ **RICHARGE tolerance:** VICHARGE = 1.485V ±0.5% (LTC3350 spec); RICHARGE (301Ω) should be 0.1% E96 Thin-Film to keep combined error ≤±0.6%
    → charge current error ≤±3mA at 500mA target. This is negligible for supercap charging.
  * ⚠️ Verify RSENSE value against LTC3350 datasheet once layout is frozen; **R12 (RSENSE) must be a 4-terminal Kelvin-sense resistor**
    with independent sense traces to avoid trace resistance adding to the measured value (even 1mΩ trace adds 10% error on a 10mΩ sense resistor).
  * **Backup Trigger:** LTC3350 BACKUP pin activates hold-up mode when 5V_MAIN drops below the programmed threshold
    (resistor divider R14/R15 from 5V_MAIN to BACKUP pin; threshold = 1.2V × (R14+R15)/R15).
    * **Applied values (PM-06 fix):** R14=26.7kΩ (ERA-3ARB2672V) / R15=10.0kΩ → threshold = **4.40V** — 100mV below PWR_GD assertion (4.50V),
      ensuring the CM5 receives the PWR_GD warning before backup hold-up engages.
    * ⚠️ **Design note:** The original as-drawn value of R14=30.1kΩ set a threshold of 4.81V — above the PWR_GD assertion voltage (4.50V),
      causing a dead-zone where backup could engage without the CM5 receiving a warning. This was resolved in PM-06.
      See BOM R14 entry and the R14/R15 BOM note for details.
    * Hold-up duration from fully-charged bank: ≥14.5 seconds at 5W CM5 graceful-shutdown load.

* **PoE Subsystem:**
  * **PD Interface:** TPS2372-4 (U9, VQFN-20) — IEEE 802.3bt Type 4 PD interface, Autoclass enabled. Autoclass handles the 4-event multi-power-level classification internally; no external RCLASS

    resistor is required.

  * **MPS Programming (RMPS):** An external resistor from the TPS2372-4 IMPS pin to GND programs the MPS (Maintain Power Signature) pulsed current amplitude required to keep the PSE port active.

    Formula: `RMPS = VIMPS / IMPS` where `VIMPS = 1.205V`. For target `IMPS = 10mA` (providing margin above the 7mA IEEE 802.3bt Type 4 minimum): `RMPS = 1.205 / 0.010 = 120.5kΩ → use 121kΩ (E96,
0.1%, 0603)`.

    * ⚠️ Confirm IMPS target (7–15mA range acceptable) against TPS2372-4 datasheet before schematic freeze.
  * **DC-DC Controller:** TPS23730 (U10, WQFN-20) — ACF (Active Clamp Flyback) controller.
    * Configured for **Primary-Side Regulation (PSR)** using the VS pin and the POE600F-12LD auxiliary winding. PSR eliminates the need for an external TL431 shunt regulator and optocoupler on the

      secondary side.

    * Output voltage (12V nominal) is set by the POE600F-12LD transformer turns ratio, which Coilcraft has designed for 12V output in TPS23730 PSR mode.
    * Soft-start capacitor on SS pin: 10nF (5ms ramp-up, **C24**).
* **LDO Enable (ROTOR_EN):**
  * CM5 GPIO 16 (ROTOR_EN, 3.3V drive) drives the TPS75733 (U7) EN pin. The TPS75733 has an **active-LOW enable** (EN LOW = enabled, EN HIGH = shutdown) — no level-shifting required.
  * A 10kΩ pull-**down** resistor from the EN pin to **GND** ensures the LDO is ON by default during power-up (EN=LOW=enabled).
  * When CM5 GPIO 16 drives HIGH → LDO shuts down (ROTOR_EN de-asserted = LDO disabled).
  * When CM5 GPIO 16 drives LOW (or GPIO released) → LDO enabled.
  * **Note:** Firmware must invert the GPIO 16 logic vs the original design intent — GPIO 16 HIGH now disables the LDO; GPIO 16 LOW enables it.
    Alternatively, the enable logic can be inverted at schematic capture using a small signal inverter or by adopting active-LOW ROTOR_EN signal naming.
  * ROTOR_EN HIGH → LDO **disabled** → 3V3_ENIG off (all rotor and CPLD loads de-energised).
  * ROTOR_EN LOW → LDO **enabled** → 3V3_ENIG present (CPLDs + rotor stack powered).
  * **Thermal Budget (TPS75733):**
    * V_dropout ≈ 0.18V (TPS75733 typical at 1.85A). Typical dissipation: **~0.33W** (1.85A load, Vdo≈0.18V).
    * At worst-case 2.2A load: P_diss ≈ 0.22V × 2.2A ≈ **~0.45W** worst-case.
    * Standard TO-263 package thermal pad and ground vias are sufficient at this dissipation level. The ≥200mm² copper pour requirement from the previous WSON-12 design is removed.
    * At 40°C ambient with standard PCB copper: T_J well within 125°C limit. ✓

* **Monitoring:** MCP121T-450E supervisor asserts PWR_GD to the CM5 once the regulated 5V rail is stable.
  * "LOGIK-BEREIT" Green LED + 5.1V Zener "Safety Glow" (Amber LED) remains active during capacitor discharge.
* **Hardware Status Oscillator:** MIC1555 (U11, SOT-23-5) — CMOS timer providing the 1Hz hardware "Initialising" heartbeat pulse for the orange status LED, operating entirely independently of CM5

  firmware. Active from power-on until CM5 firmware takes control of the status LED GPIO. Also serves as a visible supercap state-of-charge indicator during hold-up mode. Timing network: R16
(R_A=10kΩ), R17 (R_B=715kΩ), C23 (C_OSC=1µF) → f=1Hz, ~50% duty cycle.

### 6. Traceability & Manufacturing

* **Assembly:** Single-side (Top) population for JLCPCB SMT service.
* **Serialization:** JLC Serial Number service block on the bottom layer.
* **Identification:** Laser-etched **Blitzpfeil** and Proxy QR code (`enigma-ng.link/docs`).
* **Branding:** Inverted white silkscreen "Data Plate" on L4 (Bottom) containing the Enigma silhouette, "ENIGMA-NG" text, near the JLC Serial Number block.

### 7. Signal Integrity & Safety

* **Ethernet (GbE):** 100Ω Differential Pairs (Layer 1); critical for link-layer signal integrity at 1 Gbps.

> **Note:** The USB-C port (J4) is power-delivery only (PD negotiation via U4 TPS25751DREFR). No USB data lines are routed on this board. HDMI is not present on the Power Module.

* **ESD Protection:**
  * 2× TPD4E05U06 (D4, D5) at the RJ45 entry — one per two GbE differential pairs.
  * TPD4E05U06 (D3) at the USB-C entry.
  * TPD2E2U06 (D2) on the Battery SMBus lines (SDA/SCL).
  * TPD1E10B06 (D1) on the BATT_PRES_N Presence Detect line.
* **Grounding:** 4-layer GND_CHASSIS ring with 2.5mm staggered via-stitching around the board perimeter.
* **Single-Point GND Bond:** Signal/power reference GND connects to GND_CHASSIS at one point only — located between the OR-ing diode network output
  and the eFuse input (the clean/dirty power boundary). See `Standards/Global_Routing_Spec.md §5` and `Standards/Certification_Evidence.md §2.2` for full rationale.
* **Galvanic Isolation:** 1500V isolation via T2 ACF transformer (Coilcraft POE600F-12LD, ≥1500Vrms rated) between the PoE PD input and the 12V secondary bus.

---

## 3. Power Sequencing & Hardware Reset

### 1. The "Safe-Start" Logic

To prevent the CM5 from attempting to boot during the 12V-15V "Enigma Rail" ramp-up, we use an automated voltage supervisor combined with a manual override.

* **Power Toggle (SW1):** Panel-mount latching SPST rocker switch (Marquardt 1800 series, RGB LED —
  *Open item — select during mechanical design phase*) connected to the TPS25980 eFuse **EN pin**, not the main VIN_BUS power line. When SW1
  is open (ON position), R22 (10kΩ to 3V3_ENIG) holds EN HIGH → eFuse enabled. When SW1 is closed
  (OFF position), EN is pulled to GND → eFuse output cut, all downstream power off.
  * **Current rating:** Low-current logic signal only (EN pin draws microamps) — no high-current switch
    rating required. Any 50mA+ rated switch is suitable.
  * **RGB LED circuit:** SW1 integrates an RGB LED status indicator. The LED is driven by a hardware
    handoff circuit: before CM5 boot, the MIC1555 oscillator (U11) drives the Red and Green channels
    via Q4 (BSS138 NMOSFET gate) to produce a 1Hz orange flash (R+G simultaneously). Once CM5
    firmware asserts SW_LED_CTRL (BtB pin 47, CM5 GPIO 24) HIGH, Q4 is disabled and CM5 drives
    SW_LED_R/G/B (BtB pins 31/32/33, CM5 GPIOs 17/18/19) directly.
  * **LED colour scheme:** Orange flash = booting; Solid green = USB-C active; Solid blue = PoE active;
    Solid orange = Battery active; Red = fault or graceful shutdown in progress.
  * **Hardware path isolation:** BAT54 Schottky diodes (D6, D7) isolate the MIC1555/Q4 hardware
    path from the CM5 GPIO outputs to prevent back-driving.
* **Supervisor IC:** [MCP121T-450E](https://www.microchip.com) (4.50V Threshold).
* **Trigger:** The supervisor monitors the **5V_MAIN** rail. It holds the `GLOBAL_EN` (PMIC_EN) pin LOW until the rail is stable.
* **Manual Reset (SW2):** A high-quality tactile button wired in parallel to the supervisor output.
  * **Action:** Pressing the button pulls `GLOBAL_EN` to GND, forcing a hard PMIC reset of the CM5
    without cycling the 12V-15V Rotor Rail. Use after a clean OS shutdown to re-start the CM5.

### 2. Startup Timeline

1. **Input:** 11–17V enters via PoE (TPS2372-4/TPS23730 + Coilcraft POE600F-12LD, regulated 12V), USB-C (STUSB4500 negotiated 15V), or Battery (11–16.8V). All three sources are within the TPS25980

   eFuse window (UVLO 11V / OVLO 16.9V).

2. **Gate:** TPS25980 eFuse validates voltage (11V–16.9V) and current (≤7A); TCO F1 provides thermal protection.
3. **Bucks:** Dual LMQ61460AFSQRJRRQ1 5V interleaved buck regulators (U2A/U2B, 180° DRSS phase offset) and TPS75733 3V3_ENIG LDO (U7) start.
4. **Supercap charging:** LTC3350 begins managed soft-charge of the 4-cell supercap bank (22F/5.4V) from 5V_MAIN, current-limited to 0.5A (RICHARGE programmed accordingly). Charge duration from fully

   depleted state: approximately 2 minutes. Once fully charged, the bank provides ≥14.5 seconds of hold-up at the 5W CM5 graceful shutdown load.

5. **Supervisor:** Once 5V_MAIN hits 4.5V, MCP121T-450E asserts GLOBAL_EN HIGH after a 200ms delay.
6. **Release:** CM5 PMIC begins internal 1.8V/1.1V sequencing.
7. **Heartbeat:** MIC1555 starts the 1Hz Orange "Initialising" pulse.

### 3. Graceful Shutdown Sequence

The following sequence ensures the CM5 filesystem is clean and all loads are de-energised safely:

1. **Trigger:** User initiates shutdown (OS command, Safe Shutdown Button, or remote API call).
2. **OS Shutdown:** CM5 OS saves state, syncs filesystems, and executes `halt`.
3. **ROTOR_EN HIGH:** CM5 GPIO 16 is asserted HIGH before halt completes, disabling the TPS75733 LDO (active-LOW EN: HIGH = shutdown) → 3V3_ENIG off (CPLDs and rotor stack de-energised).
4. **CM5 PMIC halt:** CM5 internal PMIC drops 1.8V/1.1V rails. Total time from trigger to PMIC halt: ~10–15 seconds.
5. **5V_MAIN sag:** 5V_MAIN begins to fall as CM5 load ceases. LTC3350 holds the rail up via supercap discharge for ≥14.5 seconds.
6. **PWR_GD drop:** Once 5V_MAIN falls below 4.5V, MCP121T-450E deasserts PWR_GD.
7. **Rail collapse:** After CM5 load is gone, 5V_MAIN falls to 0V. LTC3350 stops discharge.
8. **Power source removed:** User removes PoE cable, USB-C adapter, or battery. eFuse input drops to 0V.
9. **System fully off:** All rails at 0V; no residual charge path.

> **Note:** The "Safe Shutdown" button wired to CM5 GPIO (interrupt input) should trigger a software-debounced (100ms) shutdown command in the system daemon. The MCP121T manual reset pin provides a
> **hard PMIC reset only** (not a graceful shutdown); it must not be used for normal shutdown.

### 4. eFuse Latch-Off Recovery

TPS25980 latches OFF under the following fault conditions:

* **Overvoltage (OV):** Input > 16.9V (OVLO threshold).
* **Overcurrent (OC):** Output > 7A (ILIM threshold).
* **Thermal (TCO F1):** TCO opens at 72°C board temperature.

**Recovery procedure:**

1. Identify and resolve the root fault (e.g., faulty PSE port, overcurrent load, ambient overtemperature).
2. Remove **all** input sources (PoE cable, USB-C, battery).
3. Wait ≥3 seconds for the input bulk capacitors to fully discharge.
4. Re-apply a single known-good source.
5. eFuse will re-enable automatically if the input voltage is within the UVLO–OVLO window and no fault condition is present.

> ⚠️ If the eFuse repeatedly latches, do not continue cycling power. Diagnose with a bench power supply and current meter before connecting to the system.

---

## 4. Thermal Budget

Estimated power dissipation at system peak load (PoE input, all rails at full utilisation):

| Component | Normal Dissipation | Worst Case | Notes |
| :--- | :--- | :--- | :--- |
| U1 TPS25980 eFuse | 0.56W | 0.65W (7A) | 3mΩ Ron (typ.) + ~0.5W quiescent |
| U2A + U2B LMQ61460-Q1 (×2) | 5.2W total | 6.7W (15V USB-C, 90% η) | 2.6W per device at 92% η; exposed pads to GND vias |
| U7 TPS75733 LDO | 0.33W (1.85A load) | 0.45W (2.2A load, Vdo≈0.22V) | Vdo≈0.18V at 1.85A; TO-263 (KTT) 5-pin — standard thermal pad and ground vias sufficient; ≥200mm² copper pour requirement removed |
| T2 POE600F-12LD | 5.1W | 5.7W | At 90–88% efficiency, 51–57W load |
| U3 LTC3350 | 0.3W | 0.5W | Charge path only (0.5A); low concern |
| U9 TPS2372-4 | ~0.2W | ~0.3W | VQFN-20 thermal pad to GND pour |
| U10 TPS23730 | ~0.3W | ~0.5W | WQFN thermal pad to GND pour |
| **Total** | **~14.8W** | **~19.5W** | Dissipated into 42mm Al 'Power Can' enclosure via bottom thermal pad |

**Thermal Notes:**

* The LDO (U7 TPS75733) dissipates ≤0.45W worst-case (TO-263 KTT package). Standard thermal pad soldering and local ground vias are sufficient; no large copper pour required.
* The previous TPS7A8333P (WSON-12) LDO required ≥200mm² copper pour at up to 5.1W dissipation — this requirement is removed with the TPS75733 (TO-263).
* The dedicated heat zone (shared with supercap bank area) connects via thermal pad to the metal enclosure, acting as a heatsink for the bottom of the board.

---

## 5. Bill of Materials

| Ref | Component | Value/Part | Package | Mouser Part # | DigiKey Part # | JLCPCB Part # |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| C1, C4 | Pi-filter bulk cap (input + output) — **2× in parallel per position** | 22µF 25V X7R | 1210 | 187-CL32B226KAJNNNE | 1276-3392-1-ND | C309062 |
| C2, C5 | Pi-filter mid-freq bypass | 1µF 50V X7R | 0805 | 80-C0805C105K5R | 399-C0805C105K5RACTUCT-ND | C3018567 |
| C3, C6 | Pi-filter HF bypass | 100nF 50V X7R | 0402 | 187-CL05B104KB5NNNC | 1276-1009-1-ND | C1525 |
| C7, C8 | 5V Buck input bulk cap (U2A IN, U2B IN) — **2× in parallel per position** | 22µF 25V X7R | 1210 | 187-CL32B226KAJNNNE | 1276-3392-1-ND | C309062 |
| C9, C10 | 5V Buck output bulk cap (U2A OUT, U2B OUT) | 22µF 25V X7R | 1210 | 187-CL32B226KAJNNNE | 1276-3392-1-ND | C309062 |
| C11 | eFuse input bulk cap (U1 VIN) — **2× in parallel** | 22µF 25V X7R | 1210 | 187-CL32B226KAJNNNE | 1276-3392-1-ND | C309062 |
| C12 | eFuse output bulk cap (U1 VOUT) — **2× in parallel** | 22µF 25V X7R | 1210 | 187-CL32B226KAJNNNE | 1276-3392-1-ND | C309062 |
| C13 | LDO input cap (U7 VIN from 5V_MAIN) | 10µF 25V X7R | 1206 | 80-C1206C106K3R | 399-C1206C106K3RACTUCT-ND | C2168111 |
| C14 | LDO output cap (U7 VOUT — 3V3_ENIG) | 22µF 25V X7R | 1210 | 187-CL32B226KAJNNNE | 1276-3392-1-ND | C309062 |
| C15–C21 | IC VCC bypass (one per: U3, U4, U5, U6a, U8, U9, U10) | 100nF 50V X7R | 0402 | 187-CL05B104KB5NNNC | 1276-1009-1-ND | C1525 |
| C22 | MIC1555 VCC bypass (U11) | 100nF 50V X7R | 0402 | 187-CL05B104KB5NNNC | 1276-1009-1-ND | C1525 |
| C23 | MIC1555 timing capacitor (C_OSC, 1Hz) | 1µF 50V X7R | 0805 | 80-C0805C105K5R | 399-C0805C105K5RACTUCT-ND | C3018567 |
| C24 | TPS23730 soft-start cap (C_SS, SS pin) | 10nF 50V X7R | 0402 | 187-CL05B103KB5NNNC | 1276-1005-1-ND | C57112 |
| C_SC1–4 | Supercaps (4× cells, 2S2P) | Tecate TPLH-2R7/22WR12X31 / 22F 2.7V −40°C to +85°C | THT Radial 12×31mm | N/A — DigiKey only | 2085-TPLH-2R7/22WR12X31-ND | N/A — consign via DigiKey |
| D1 | BATT_PRES ESD | TPD1E10B06 | SOD-923 | 595-TPD1E10B06QDCKR | 296-TPD1E10B06QDCKRQ1CT-ND | C284765 |
| D2 | Battery SMBus ESD | TPD2E2U06DRLR | SOT-553 (DRL) | 595-TPD2E2U06DRLR | 296-38361-1-ND | — |
| D3 | USB-C ESD | TPD4E05U06 | U-DFN-10 | 595-TPD4E05U06DBVR | 296-TPD4E05U06DBVRCT-ND | C123462 |
| D4 | RJ45 ESD (MDI0/MDI1) | TPD4E05U06 | U-DFN-10 | 595-TPD4E05U06DQAR | 296-TPD4E05U06DQARCT-ND | C123462 |
| D5 | RJ45 ESD (MDI2/MDI3) | TPD4E05U06 | U-DFN-10 | 595-TPD4E05U06DQAR | 296-TPD4E05U06DQARCT-ND | C123462 |
| R18–R21 | RJ45 Bob Smith termination resistors (×4) | 75Ω ±1% 0402 | 0402 | 667-ERJ-2RKF75R0X | P75.0LCT-ND | C413061 |
| C25 | RJ45 Bob Smith termination capacitor (⚠️ Y1-class 0402 is rare; 100V X7R acceptable proxy for EMC transient margin — Ethernet ESD discharge path to chassis) | 10nF 100V X7R 0402 | 0402 | 80-C0402C103J1RAUTO | 399-C0402C103J1RACAUTOCT-ND | C19862706 |
| C26, C27 | IC VCC bypass for U6b and U6c (LM74700-Q1 OR-ing controllers — USB-C and Battery paths) | 100nF 50V X7R | 0402 | 187-CL05B104KB5NNNC | 1276-1009-1-ND | C1525 |
| F1 | TCO | 72°C SMD Thermal Cutoff | N/A | 652-AC72ABD | AC72ABD-ND | — |
| J1 | BtB Link (MALE header — mates with ERF8-040 female socket on Controller) | Samtec ERM8-040-05.0-S-DV-K-TR | 80-pin Gold ERM8 | 200-ERM8040050SDVKTR | SAM8613CT-ND | C5358550 |
| J2 | PoE+ Port | Wurth 7499111121A | Long-Body THT RJ45 | 710-7499111121A | 1297-1070-5-ND | C5523983 |
| J3 | Battery Conn ⚠️ **REVIEW: confirm suitability for battery application** | Molex 0436500519 (43650-0519) — full PN 0436500519; vertical THT, 5-circuit, 1-row, gold contacts, board lock, 3mm pitch | 5-pin Micro-Fit 3.0 THT vertical | 538-43650-0519 | WM14587-ND | C563849 |
| J4 | USB-C Power Input | GCT USB4135-GF-A — **6-position** USB Type-C right-angle SMT receptacle (power/PD only). Connects CC1 and CC2 to STUSB4500 (U5) for PD negotiation; VBUS to OR-ing circuit. Right-angle (board-edge mount) with retention pins. ⚠️ **Mechanical note**: connector must penetrate Power Module enclosure wall and sit flush with outer machine enclosure — verify clearance at prototype stage. See BOM note for details | SMT right-angle (board-edge) | 640-USB4135-GF-A | 2073-USB4135-GF-A-ND | C5438410 |
| L1 | EMI Primary CMC (CM filter, broadband) | Würth WE-CMBNC 7448031002 — 10A, 2mH, nanocrystalline, 6.3mΩ DCR, 24×17×25mm THT | THT | 710-7448031002 | 732-5584-ND | C1519839 |
| L2 | EMI Secondary CMC (HF, >10MHz) | Würth WE-CMBNC 7448031002 — same as L1 (**CM5022 discontinued**, Laird absorbed by TE Connectivity 2019; no ≥10A HF ferrite equivalent found). Twin nanocrystalline CMC approach provides adequate broadband coverage 1kHz–30MHz. ⚠️ Re-evaluate at EMC pre-compliance test. | THT | 710-7448031002 | 732-5584-ND | C1519839 |
| L3 | EMI DM Pi-filter Inductor | Bourns SRP1265A-100M — 10µH, 15.5A Isat, 10A Irms, DCR=16.5mΩ max, shielded molded. Replaces Würth 7447789100 (not in public catalog). ⚠️ Package 13.5×12.5×6.2mm — footprint differs from 7447789100 (12.5×12.5×6mm); update PCB land pattern accordingly | 13.5×12.5×6.2mm SMT | 652-SRP1265A-100M | SRP1265A-100MCT-ND (CT) / SRP1265A-100MTR-ND (T&R) / SRP1265A-100MDKR-ND (DKR) | C840531 |
| Q1, Q2, Q3 | OR-ing ideal-diode N-ch MOSFET (one per power input: PoE, USB-C, Battery) | TI CSD17483F4T — 30V V_DSS, 10A I_D continuous, R_ds(on)=8.4mΩ @ V_gs=10V. Driven by LM74700-Q1 (U6a/U6b/U6c — one IC per MOSFET) charge-pump gate drive (+7V above source). Provides lossless ideal-diode OR-ing between three input sources. | SON-8 3.3×3.3mm | 595-CSD17483F4T | 296-CSD17483F4TCT-ND | — |
| R1 | eFuse UVLO upper resistor (R_UVLO_HI) | 232kΩ 0.1% Thin-Film | 0603 | 667-ERA-3ARB2323V | P232KBYCT-ND | — |
| R2 | eFuse UVLO lower resistor | 28.7kΩ 0.1% Thin-Film | 0603 | 667-ERA-3ARB2872V | P28.7KBYCT-ND | — |
| R3 | eFuse OVLO set resistor | 53.6kΩ 0.1% Thin-Film | 0603 | 667-ERA-3ARB5362V | P53.6KBYCT-ND | — |
| R4, R5 | ETH Activity LEDs | 330Ω 1% Thick-Film | 0603 | 667-ERJ-3EKF3300V | P330BYCT-ND | C25803 |
| R6 | BATT_PRES_N Pull-up (to 3V3_ENIG) | 10kΩ 1% | 0603 | 667-ERJ-3EKF1002V | P10.0KBYCT-ND | C25804 |
| R7, R8 | I2C SDA/SCL Pull-ups (to 3V3_ENIG) | 4.7kΩ 1% | 0603 | 667-ERJ-3EKF4701V | P4.7KBYCT-ND | — |
| R9 | SYS_RESET_N Pull-up (to 3V3_ENIG) | 10kΩ 1% | 0603 | 667-ERJ-3EKF1002V | P10.0KBYCT-ND | C25804 |
| R10 | ROTOR_EN Pull-down (EN to GND) | 10kΩ 1% | 0603 | 667-ERJ-3EKF1002V | P10.0KBYCT-ND | C25804 |
| R11 | LTC3350 RICHARGE (charge current set) | 301Ω 1% [calc: ICH=0.5A, VICHARGE=1.485V, RSENSE=10mΩ → R=297Ω → E96=301Ω] | 0603 | 667-ERJ-3EKF3010V | P301HCT-ND | — |
| R12 | LTC3350 RSENSE (Kelvin sense, charge path) | 10mΩ ±1% 5A | 2512 Kelvin | 652-CSS2H-2512R-R010ELF | CSS2H-2512R-R010ELF-ND | — |
| R13 | TPS2372-4 RMPS (MPS current set) | 121kΩ 1% [calc: IMPS=10mA, VIMPS=1.205V → R=120.5kΩ → E96=121kΩ] | 0603 | 667-ERJ-3EKF1213V | P121KBYCT-ND | — |
| R14 | LTC3350 BACKUP divider upper (R_TOP) — **UPDATED per PM-06 fix** | 26.7kΩ 0.1% Thin-Film [calc: V_thr=1.2V, V_trigger=4.40V → R_TOP/R_BOT=(4.40/1.2)−1=2.667 → R_BOT=10kΩ → R_TOP=26.67kΩ → E96=26.7kΩ → actual trigger: 4.40V, 100mV below PWR_GD at 4.50V] | 0603 | 667-ERA-3ARB2672V | P26.7KBYCT-ND | — |
| R15 | LTC3350 BACKUP divider lower (R_BOT) | 10.0kΩ 0.1% Thin-Film [pairs with R14; use 0.1% for threshold accuracy] | 0603 | 667-ERA-3ARB1002V | P10.0KBYCT-ND | — |
| R16 | MIC1555 timing resistor R_A | 10.0kΩ 1% [calc: f=1.44/((R_A+2R_B)×C); R_B=715kΩ, C=1µF → f=1Hz, duty≈50%] | 0603 | 667-ERJ-3EKF1002V | P10.0KBYCT-ND | C25804 |
| R17 | MIC1555 timing resistor R_B | 715kΩ 1% E96 [pairs with R16 and C23 to set 1Hz, ~50% duty-cycle oscillation] | 0603 | 667-ERJ-3EKF7153V | P715KBYCT-ND | — |
| SW1 | Main Power Toggle + RGB Status | Marquardt 1800 series panel-mount latching SPST rocker with RGB LED — *Open item — select during mechanical design phase* (select variant with red/green/blue capable LED insert and black body). Connects to TPS25980 eFuse EN pin (low-current, logic-level only). Connected via Keystone 1285 spade blade terminals for SW contacts; RGB LED pins connect directly to PCB pads. | Panel-mount | *Open item — select during mechanical design phase* | *Open item — select during mechanical design phase* | — |
| SW2 | CM5 Hard Reset | Tactile SMT pushbutton, momentary SPST, in parallel with MCP121T-450E (U8) RESET output on GLOBAL_EN line. Pulls GLOBAL_EN to GND on press. No pull-up needed (R9 on GLOBAL_EN line serves this purpose). | 6×6mm SMT tactile | 688-SKRPACE010 | CKN9085CT-ND | C318884 |
| R22 | eFuse EN pull-up (SW1 circuit) | 10kΩ 1% Thick-Film | 0603 | 667-ERJ-3EKF1002V | P10.0KBYCT-ND | C25804 |
| R23 | INA219 5V_MAIN Kelvin-sense shunt | 10mΩ ±1% 5A | 2512 Kelvin | 652-CSS2H-2512R-R010ELF | CSS2H-2512R-R010ELF-ND | — |
| D6 | SW1 RGB hardware path isolation — Red channel | BAT54 Schottky diode | SOD-323 | 771-BAT54215 | BAT54-7-FCT-ND | C8598 |
| D7 | SW1 RGB hardware path isolation — Green channel | BAT54 Schottky diode | SOD-323 | 771-BAT54215 | BAT54-7-FCT-ND | C8598 |
| Q4 | SW1 hardware LED path gate (MIC1555 → R+G channels) | BSS138 N-channel MOSFET — 50V, 200mA, logic-level gate | SOT-23 | 512-BSS138 | BSS138CT-ND | C112233 |
| T2 | PoE ACF Isolation Transformer | Coilcraft POE600F-12LD / 60W / 12V out / 36–72V in / 200kHz / ACF topology / ≥1500Vrms / SMT / RoHS | SMT | — (order direct: coilcraft.com) | — | — |
| U1 | eFuse | TPS259803ONRGER (16.9V OVLO) | VQFN-24 4×4mm | 595-TPS259803ONRGER | 296-TPS259803ONRGERCT-ND | C2866563 |
| U2A, U2B | 5V Buck ×2 (180° interleaved) | LMQ61460AFSQRJRRQ1 | VQFN-HR (RJR) 14-pin 4×3.5mm | 595-Q61460AFSQRJRRQ1 | 296-LMQ61460AFSQRJRRQ1CT-ND | C1518767 |
| U3 | Supercap Manager | LTC3350EUHF#PBF | QFN-38 (5×7mm) | 584-LTC3350EUHF#PBF | LTC3350EUHF#TRPBFCT-ND | — |
| U4 | PD Emulator (DRP, PD3.1) | TPS25751DREFR — PD3.1 certified DRP controller with integrated 20V/5A bi-directional + 5V/3A source power paths. Replaces NRND TPS25750. ⚠️ Package is WQFN-38 6×4mm (REF) — **different from TPS25750 QFN-28; schematic and PCB footprint update required** | WQFN-38 6×4mm | 595-TPS25751DREFR | TPS25751DREFR-ND | — |
| U5 | USB-C Sink Controller | STUSB4500LQTR | QFN-24 | 511-STUSB4500LQTR | 497-STUSB4500LQCT-ND | C506650 |
| U6a, U6b, U6c | OR-ing Controllers (×3, one per power input: PoE, USB-C, Battery) | LM74700QDBVRQ1 | SOT-23-6 | 595-LM74700QDBVRQ1; alt T&R: 595-LM74700QDBVTQ1 | 296-LM74700QDBVRQ1CT-ND | C2941042 |
| U7 | 3V3_ENIG LDO | TPS75733KTTRG3 (fixed 3.3V, active-LOW EN) | TO-263 (KTT) 5-pin 10.16×15.24mm | 595-TPS75733KTTRG3 | 296-50559-1-ND | C3749924 |
| U8 | Voltage Supervisor | MCP121T-450E/LB (4.5V trip) | SC70-3 | 579-MCP121T-450E/LB | MCP121T-450E/LBCT-ND | C52146050 |
| U9 | PoE PD Interface (Type 4) | TPS2372-4 | VQFN-20 | 595-TPS2372-4RGWR | 296-52795-1-ND | — |
| U10 | PoE DC-DC Controller (ACF) | TPS23730RMTR — PSR mode; 12V output set by POE600F-12LD transformer turns ratio; VS pin to aux winding; no external feedback divider required. | WQFN-20 | 595-TPS23730RMTR | 296-TPS23730RMCT-ND | — |
| U11 | Hardware status LED oscillator | MIC1555YM5-TR — CMOS timer IC, 2–10V supply, SOT-23-5. Generates 1Hz hardware "Initialising" heartbeat pulse for the orange status LED. Operates independently of CM5 firmware (pure hardware indicator). Also reflects supercap state of charge during hold-up. Timing set by R16 (R_A=10kΩ), R17 (R_B=715kΩ), C23 (C_OSC=1µF) → f=1Hz, ~50% duty cycle. | SOT-23-5 | 579-MIC1555YM5TR | MIC1555YM5-TRCT-ND | C431119 |
| U12 | 5V_MAIN Current Monitor | INA219AIDR — Zero-Drift Current/Power Monitor (I²C 0x40) | SOIC-8 | 595-INA219AIDR | 296-23978-1-ND | C138706 |

> **BOM Notes:**
>
> * **U1 TPS259803ONRGER** — `TPS25980RPWR` was the original placeholder; confirmed `TPS259803ONRGER` as the 16.9V OVLO VQFN-24 variant.
>   PNs verified: Mouser 595-TPS259803ONRGER, DigiKey 296-TPS259803ONRGERCT-ND, JLCPCB C2866563.
> * **U3 LTC3350EUHF#PBF** — Package is **QFN-38 (5×7mm)**, not QFN-28. Footprint and courtyard on PCB must use the 38-lead 5×7mm QFN (UHF package code). DigiKey T&R: `LTC3350EUHF#TRPBFCT-ND`; also
> available Farnell 4029939.
> * **U4 TPS25751DREFR** — Replaces NRND TPS25750. TPS25751 is PD3.1 USB-IF certified (TID#10306); D-variant integrates the full bi-directional 20V/5A power path required to source 5V/5A (25W) to the
> CM5 and prevent OS throttling. **Package changed to WQFN-38 6×4mm (REF)** — schematic pins and PCB footprint must be updated from the TPS25750 QFN-28 layout. Mouser: `595-TPS25751DREFR`; DigiKey:
> `TPS25751DREFR-ND`.
> * **U5 STUSB4500LQTR** — JLCPCB C506650 confirmed in stock (L-variant). Both are pin-compatible; non-L variant STUSB4500QTR has slightly higher Iq (~210µA vs 160µA).
> * **U7 TPS75733KTTRG3** — Replaces TPS7A8333PRMWR. Fixed 3.3V output, 3A continuous, TO-263 (KTT) 5-pin 10.16×15.24mm package. **Active-LOW enable:** EN LOW = LDO enabled; EN HIGH = shutdown.
> R10 changed to pull-down (10kΩ to GND) to ensure LDO is ON by default at power-up. Firmware must drive GPIO 16 HIGH to disable the LDO (inverted vs original TPS7A8333P logic).
> Thermal dissipation greatly improved: ~0.33W typical (1.85A, Vdo≈0.18V) vs 3.1W with the previous part — ≥200mm² copper pour requirement removed.
> Mouser: `595-TPS75733KTTRG3`; DigiKey: `296-50559-1-ND`; JLCPCB: `C3749924`.
> * **U8 MCP121T-450E/LB** — Package updated to **SC70-3** (`/LB` suffix) from SOT-23-3 (`/TT`). Ensure PCB footprint uses SC70-3. If SOT-23-3 footprint is preferred, use `MCP121T-450E/TT` (Mouser
> 579-MCP121T-450ETTDITR) instead. JLCPCB C52146050 confirmed; note JLCPCB lists this device with a TP prefix on the MPN but is the same device.
> * **U10 TPS23730RMTR** — `PWPR` suffix (HTSSOP-20) was previously in error; correct WQFN-20 manufacturer PN is `TPS23730RMTR`. DigiKey catalogues as `296-TPS23730RMCT-ND`. Verify against TI's
> product page before ordering.
> * **U11 MIC1555YM5-TR** — CMOS timer (Microchip). Timing components: R16=10.0kΩ (R_A), R17=715kΩ (R_B), C23=1µF (C_OSC) → 1Hz, ~50% duty cycle via formula f=1.44/((R_A+2R_B)×C). VCC bypass: C22
> (100nF). Note: the 715kΩ E96 resistor (R17) is not common at all distributors — confirm stock at Mouser (667-ERJ-3EKF7153V) before BOM freeze.
> * **Q1–Q3 CSD17483F4T** — N-channel MOSFET for LM74700-Q1 ideal-diode OR-ing. One per power input (PoE, USB-C, Battery).
> Three LM74700-Q1 instances (U6a, U6b, U6c) are required — one IC per MOSFET for correct per-channel ideal-diode gate drive
> (+7V above source via internal charge pump). Confirm U6a/U6b/U6c footprints at schematic capture.
> * **J1 ERM8-040-05.0-S-DV-K-TR (Power Module) + ERF8-040-05.0-S-DV-K-TR (Controller)** — Samtec BtB connector pair.
>   **ERM8 = MALE header (pins pointing up)** on Power Module; **ERF8 = FEMALE socket** on Controller. Both are Samtec proprietary parts, NOT in JLCPCB/LCSC catalog.
>   Assembly paths: (a) JLCPCB customer-supplied component service — procure from Mouser and select "consigned components" option; (b) Hand-solder after PCB assembly.
>   Current rating: **0.5A per pin** continuous (design derating per Certification_Evidence.md §5; 2oz copper applied —
>   18 power pins × 0.5A = 9.0A total capacity) — ensure adequate VBUS/GND pin count per Power_Module/Board_Layout.md LINK-ALPHA table.
>   Stack height "05.0" in PN refers to individual header height; total PCB-to-PCB gap ≈ 7mm mated (ERM8 5mm + ERF8 2mm).
>   ⚠️ Verify exact ERF8 mating height at schematic capture to confirm enclosure fit.
> * **J4 USB4135-GF-A** — GCT **6-position, right-angle SMT** USB-C receptacle (confirmed via Octopart; JLCPCB C5438410 verified by user).
>   The 6 positions cover VBUS(×2), GND(×2), CC1, CC2 — exactly what STUSB4500 needs for PD negotiation.
>   **Right-angle (R/A) mounting**: connector sits on the board edge with the USB-C port facing outward — correct for the Power Module's panel-mount power input.
>   ⚠️ **Mechanical caveat**: the connector must penetrate the Power Module enclosure wall and sit flush with the outer machine enclosure.
>   Verify protrusion depth vs enclosure wall thickness at prototype stage — may need a panel cutout with bezel, a panel-mount USB-C extension, or a revised connector with longer reach.
>   Available at DigiKey (2073-USB4135-GF-A-ND) and JLCPCB (C5438410). CC1 and CC2 pins connect
> to STUSB4500 (U5) for PD 15V negotiation.
> * **R14/R15 BACKUP divider** — **UPDATED (PM-06 fix):** R14 changed from 30.1kΩ to **26.7kΩ** (ERA-3ARB2672V).
>   Sets LTC3350 BACKUP comparator trigger at **4.40V** (V_thr=1.2V, R_TOP=26.7kΩ, R_BOT=10.0kΩ).
>   This fires **after** PWR_GD asserts at 4.50V — supercap backup engages 100mV below PWR_GD, preventing the dead-zone that the original 4.81V threshold created.
>   Use 0.1% tolerance on both R14 and R15 for threshold accuracy.
> * **C7–C14 bulk/bypass caps** — All 22µF caps use Samsung CL32B226KAJNNNE (22µF **25V** X7R 1210) as C1/C4. The original 22µF 50V 1210 spec (Murata GRM32ER71H226KE15L) was not available
> from any distributor — 22µF at 50V in 1210 does not appear to be a commercial catalogue part. Maximum actual bus voltage on the hardest-stressed positions (C1, C4, C7, C8, C11, C12) is ~16.4V
> (4S battery, 4.1V/cell max per DEC-005), giving 1.5× voltage derating at 25V rating. ⚠️ Note: X7R capacitors exhibit DC bias
> derating; at 16V on a 25V-rated part (~64% of Vrated), single-cap effective capacitance is approximately 50–65% of nominal (≈11–14µF).
> **To recover this derating, C1, C4, C7, C8, C11, and C12 are each populated as 2× CL32B226KAJNNNE in parallel; effective capacitance at 16V becomes ≈22–28µF, meeting the nominal 22µF design target.**
> C9, C10 (5V bus — ~20% Vrated, negligible derating) and C14 (3V3_ENIG bus) remain at 1× per position. BOM total for CL32B226KAJNNNE: 6 positions × 2 + 3 single = **15 units** per PM.
> C13 uses a different 10µF part.
> DigiKey 1276-3392-1-ND; JLCPCB C309062 (confirmed — Samsung CL32B226KAJNNNE 22µF 25V X7R 1210).
> * **C15–C25 IC bypass and timing caps** — C15–C22 (100nF bypass) share the same Samsung CL05B104KB5NNNC as C3/C6.
> C15–C21 covers U3, U4, U5, U6a, U8, U9, U10; C26 and C27 (100nF bypass for U6b and U6c respectively) are now formally
> defined in the BOM table above (same Samsung CL05B104KB5NNNC / C1525). C23 (1µF timer) shares the same Kemet C0805C105K5RACTU as C2/C5. C24 (10nF C_SS)
> is a new part (Samsung CL05B103KB5NNNC).
> * **J3 0436500519 (43650-0519)** — Full Molex PN: `0436500519`; short form `43650-0519`. 5-circuit, 1-row, vertical THT, gold contacts, board lock, 3mm pitch.
>   Confirmed stock: Farnell ~1,143 pcs (£1.18 each); Heilind 756 pcs.
> Mouser: `538-43650-0519`; DigiKey: `WM14587-ND` (confirmed); JLCPCB: `C563849` (confirmed).
> ⚠️ **REVIEW REQUIRED:** Confirm Molex 43650-0519 Micro-Fit 3.0 is suitable for battery connector application
> — verify current rating, connector type, and locking mechanism meet battery safety requirements.
> * **R1 ERA-3ARB2323V (232kΩ)** — Corrected from 732kΩ (calculation error). R1 = 28700 × (11/1.21 − 1) = 232kΩ
> for 11V UVLO threshold with R2 = 28.7kΩ. E96 standard value 232kΩ. Confirm stock at Mouser
> (667-ERA-3ARB2323V, Panasonic ERA-3ARB2323V) or DigiKey (P232KBYCT-ND) before BOM freeze.
> * **R4–R13 ERJ-3EKF series** — These are Panasonic **1% thick-film** resistors (corrected from "0.1% Thin-Film" in earlier drafts). The ERA-3ARB series (R1–R3) remains 0.1% thin-film for precision
> UVLO/OVLO dividers. For pull-ups, LED limiters, and charge current set resistors, 1% tolerance is fully adequate.
> * **R12 CSS2H-2512R-R010ELF** — **Critical PN correction**: the original `L100ELF` suffix codes 100µΩ (L-prefix = µΩ range); for 10mΩ (0.010Ω) the correct Bourns code is `R010ELF` (R-prefix = Ω
> range). Mouser: 652-CSS2H-2512R-R010ELF; DigiKey: CSS2H-2512R-R010ELF-ND.
> * **L1/L2 WE-CMBNC 7448031002** — Both L1 and L2 use the same Würth nanocrystalline CMC. L2 was originally Laird CM5022 but that part is **discontinued** (Laird EMC passives absorbed by TE
> Connectivity in 2019). No equivalent ≥10A HF ferrite CMC was found in current catalogs. Twin nanocrystalline CMCs provide adequate broadband CM attenuation from 1kHz–30MHz. Re-evaluate at EMC
> pre-compliance testing. Available from: Würth direct, Mouser (710-7448031002), DigiKey (732-5584-ND), and JLCPCB (C1519839).
> * **L3 SRP1265A-100M** — Replaces Würth 7447789100 (not available in public catalog). Bourns SRP1265A-100M: 10µH, **15.5A Isat** (21% headroom over 12A DC), 16.5mΩ DCR (better than original 20mΩ
> spec), 13.5×12.5×6.2mm SMD. ⚠️ Package is 13.5×12.5mm vs 7447789100's 12.5×12.5mm — update PCB land pattern. Farnell stock confirmed ~2,741 pcs; Mouser: `652-SRP1265A-100M`; DigiKey:
> `SRP1265A-100MCT-ND`.
