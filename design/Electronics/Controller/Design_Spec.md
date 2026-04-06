# Controller Board (V1.0) Design Specification

**Status:** Draft
**Project:** Enigma-NG
**Author:** Izzyonstage & GitHub Copilot
**Version:** v1.0.0
**Associated Hardware Revision:** Rev A
**Last Updated:** 2026-04-05

---

## 1. Overview

* **Module:** Raspberry Pi Compute Module 5 (CM5).
* **Role:** Master traffic controller for Power (Alpha) and Encryption Logic (Beta).
* **Stackup:** 6-Layer / 2oz Finished Copper (JLC06161H-2116) for 5Gbps differential pair integrity.
* **Shielding:** High-speed signals (Ethernet, USB 3.0, HDMI) routed as Striplines on L3, shielded by L2/L5 GND planes
  and L4 (Internal) for High-Current Power Plane (5V_MAIN / 3V3_ENIG).
* **USB-C:** 16-pin "Power Only" to maximize mechanical durability in classroom settings.
* **Status LED:** **MIC1555 Hardware Heartbeat** (1Hz pulse) triggers on power-up before CM5 boot for instant status
  confirmation.

> **Full design decision history:** See `design/Design_Log.md` for all formal design decisions (DEC-xxx) applicable
> to this board.

### Functional & Design Requirements

#### Functional Requirements

| ID | Functional Requirement | Notes | Satisfied By / Cross-Ref |
| :--- | :--- | :--- | :--- |
| FR-CTL-01 | Host the Raspberry Pi Compute Module 5 as the system master processor | CM5 runs the Linux OS and all application logic | BOM U1 (CM5) |
| FR-CTL-02 | Receive power from the Power Module and distribute to the CM5 and peripherals | Via Link-Alpha (J1) | §2 Dual-Link Interface; BOM J1 (ERF8-040) |
| FR-CTL-03 | Provide external I/O interfaces for system management | GbE, HDMI, USB 3.0 | §2 Connectivity; BOM J3 (USB 3.0), J4 (HDMI) |
| FR-CTL-04 | Provide JTAG programming capability for all 37 CPLDs in the system | Via JTAG Daughterboard and Link-Beta | §3 JTAG Programming Subsystem; BOM J2 (Link-Beta) |
| FR-CTL-05 | Monitor system power status and report to CM5 via GPIO | PoE presence, battery presence, USB fault, PWR_GD | §6 CM5 GPIO Mapping Matrix; §4 Telemetry & Logic |
| FR-CTL-06 | Maintain RTC operation across power cycles using a CR2032 backup battery | Non-rechargeable; service by disassembly | §5 RTC Backup Battery; BOM BT1, D1 (BAT54) |
| FR-CTL-07 | Route Link-Beta signals between the CM5/JTAG Daughterboard and the Stator board | Via J2 | §2 Dual-Link Interface; BOM J2 (ERF8-020) |

#### Design Requirements

| ID | Design Requirement | Specification | Satisfied By / Cross-Ref |
| :--- | :--- | :--- | :--- |
| DR-CTL-01 | PCB stackup | 6-layer, 2oz finished copper (JLC06161H-2116) | §9 PCB Fabrication & Stackup |
| DR-CTL-02 | CM5 module | Raspberry Pi Compute Module 5 (SO-DIMM form factor) | BOM U1 (CM5) |
| DR-CTL-03 | Link-Alpha connector | J1 = ERF8-040-05.0-S-DV-K-TR (80-pin female, 0.8 mm pitch) | BOM J1 (ERF8-040-05.0-S-DV-K-TR) |
| DR-CTL-04 | Link-Beta connector | J2 = ERF8-020-05.0-S-DV-K-TR (40-pin female, 0.8 mm pitch) | BOM J2 (ERF8-020-05.0-S-DV-K-TR) |
| DR-CTL-05 | JTAG signal buffer | U5 = SN74LVC2G125DCUR relocated to JDB (see DEC-023); Controller JTAG lines are pass-through — no active components | §3 JTAG Programming Subsystem; JDB Design_Spec BOM U5 |
| DR-CTL-06 | USB current limit | 1.6 A via TPS2065C; fault output to GPIO 22 (USB_FAULT) | BOM U2 (TPS2065C); §6 GPIO Mapping (GPIO 22) |
| DR-CTL-07 | RTC battery holder | BT1 = Keystone 3034 (THT horizontal CR2032 holder) | §5 RTC Backup Battery; BOM BT1 (Keystone 3034) |
| DR-CTL-08 | RTC protection | D1 = Nexperia BAT54 Schottky diode (blocks PMIC VBAT charge path) | §5 RTC Backup Battery; BOM D1 (BAT54) |
| DR-CTL-09 | RTC bypass capacitor | C6 = 100 nF 0402 on CM5 VBAT (Pin 95, Hirose DF40 200-pin) | §5 RTC Backup Battery; BOM C6 |
| DR-CTL-10 | GPIO mapping | GPIO 20 = POE_STAT (active-low), GPIO 22 = USB_FAULT, GPIO 23 = BATT_PRES_N, GPIO 24 = SW_LED_CTRL, GPIO 25 = SYS_FAULT (active-low), GPIO 26 = SYS_RESET_N (active-low output), GPIO 27 = PWR_GD | §6 CM5 GPIO Mapping Matrix |
| DR-CTL-11 | RTC configuration | `dtparam=rtc_bbat_vchg` must NOT be set in `/boot/firmware/config.txt` | §5 RTC Backup Battery §5.1 |

## 2. Dual-Link Interface (Samtec ERx8)

> **Assembly Note:** Both BtB connectors (J1 and J2) use ERF8 **female** sockets. This is a deliberate mechanical
> choice — the Controller slides into the enclosure and simultaneously blind-mates with the Power Module (J1) and
> Stator (J2) along the back edge in a single insertion motion. See DEC-014.

* **Link-Alpha (Power/Entry):** ERF8 Female Socket 80-pin Power/Ethernet/Telemetry entry from Power Module.
  * Receives: 5V/9.0A, 3V3_ENIG, GBE and PWR_GD Data from Power Module.
  * Provides: 3V3_ENIG for RJ45 Power and Status LED signals.
  * **Cross-ref:** See `Power_Module/Design_Spec.md` and `Power_Module/Board_Layout.md` for the matching Link-Alpha
    pin allocation and power flow definitions.
* **Link-Beta (Logic/Stator):** ERF8 Female Socket 40-pin Encryption/JTAG interface to Stator Board.
  * Provides: JTAG, Reset, and 3V3_ENIG to Stator.
  * **Cross-ref:** See `Stator/Design_Spec.md` and `Stator/Board_Layout.md` for explicit pin mapping and connector
    compliance. See DEC-015 for 40-pin reduction rationale and poka-yoke safety note.
* **3V3_ENIG Bridge:** Passive 2oz copper highway on L3, directly linking Alpha and Beta for noise isolation.

### 2.1. High-Speed Routing (on Link-Alpha)

* **Ethernet:** 100Ω Stripline pairs on L3, shielded by L2/L5 ground planes.
* **Power Vias:** 4-via "Power Clusters" (0.3mm) per Samtec power pin for thermal stability.

### 2.2. Connectivity & Bus (on Link-Beta)

* **High-Speed Interconnect (BtB Samtec):**
  * **Connector:** Samtec ERF8-020 (Female Socket, 40-pin, 0.8mm pitch). See DEC-015.
  * **Mating Style:** Board-to-Board vertical stack; SMT reflow. Mates with ERM8-020 (Male) on Stator.
  * **Pin Summary:**
    * **Pins 1–9:** JTAG chain + Reset, GND-shielded (5 internal GND pins).
    * **Pins 10–11:** GND isolation moat.
    * **Pins 12–24:** ENC_IN[0:5] and ENC_OUT[0:5] (interleaved with GND shields).
    * **Pins 25–27:** TTD_RETURN + GND shields.
    * **Pins 28–35:** 3V3_ENIG power (8 pins × 0.5A = 4.0A capacity).
    * **Pins 36–40:** GND power return (5 pins).
  * **Full pin table:** See `Controller/Board_Layout.md` LINK-BETA section.
* **Programming:** Internal USB 2.0 link to the JTAG Daughterboard.
* **Encryption Sniffer Bus**
  * **Logic:** 12-bit binary encoded bus (6-in / 6-out) for 64-character alphabet monitoring.
  * **ENC_IN [0:5]:** GPIO 0-5 (Binary input from Keyboard CPLD).
  * **ENC_OUT [0:5]:** GPIO 6-11 (Binary output from Reflector/Stator).
  * **Reset:** GPIO 26 (SYS_RESET_N) triggers a hardware clear on all Intel MAX II EPM240T100C5N CPLDs.

### 2.3. Physical Connector Placement

1. **Top Edge:** Order from Left to Right
    * **Stator Link:** 40-pin Samtec ERF8-020 (Flush with edge, LINK-BETA) to Stator Board.
    * **Power In:** 80-pin Samtec (Flush with edge) from Power Module (USB-C, PoE+ & Smart Battery).
2. **Right Edge:** Order from Top to Bottom to follow CM5 pinout flow:
    * **USB 3.0:** Dual-Stacked Type-A (Molex 48406-0003) with 5.0mm overhang.
    * **HDMI:** Full-Size Type-A (TE 2007435-1) with 5.0mm overhang.
    * **Current Limiting:** TPS2065C (1.6A USB Limit + GPIO 22 Fault) and AP2331W (50mA HDMI Limit).
    * **ESD:** TPD4E05U06 TVS arrays on all external data pins.
    * **Telemetry:** USB Power Fault reported to CM5 GPIO 22.

## 3. JTAG Programming Subsystem (USB Blaster)

* **Bridge Architecture:** Dedicated **FT232H** (High-Speed USB 2.0 to JTAG/MPSSE).
* **Module Type:** Removable **Daughterboard** (2.54mm header) for future-proofing and ease of repair.
* **Interface:** Asymmetrical 1×5 (Power/USB) and 1×10 (Shielded JTAG) 2.54mm ENIG headers.
* **Shielding:** 1:1 Signal-to-Ground ratio on JTAG header to prevent clock crosstalk.
* **Diagnostic Looped Probe Pad Bank:** 2x8 2.54mm grid with gold-plated loops, positioned in-line with the BtB
  header for clean logic analyzer probing.
* **JTAG Chain Flow:**
    1. **CM5 USB 2.0** → **FT232H Daughterboard**.
    2. **JTAG Out** → **Stator CPLD (Intel MAX II EPM240T100C5N)** — first device in chain.
    3. **JTAG Chain** → **HID Encoder (Dual Intel MAX II EPM240T100C5N CPLD)** via Stator J4.
    4. **JTAG Chain** → **Plugboard Encoder #1 (Dual Intel MAX II EPM240T100C5N CPLD)** via Stator J5.
    5. **JTAG Chain** → **Plugboard Encoder #2 (Dual Intel MAX II EPM240T100C5N CPLD)** via Stator J6.
    6. **JTAG Chain** → **30x Rotor CPLDs (Intel MAX II EPM240T100C5N)** via Stator Backplane.
    7. **TTD_RETURN** ← Reflector → Extension Port → Stator J7 pin 15 → LINK-BETA pin 26 → FT232H.
* **Signal Integrity (JDB):** All JTAG buffering and series termination is located on the JDB (see DEC-023).
  The SN74LVC2G125DCUR dual-channel buffer (U5) drives TCK and TMS for the 37-device chain load.
  Series damping resistors (R6 TCK, R7 TMS after U5; R8 TDI direct from FT232H) are placed before
  the J2 JTAG header on JDB, matching the 50 Ω PCB trace impedance on LINK-BETA (BtB, no cable).
* **Controller Pass-Through:** JTAG lines (TCK, TMS, TDI, TTD_RETURN, VREF) are routed directly
  from the JDB hat-header (J_JDB) to LINK-BETA (J2) on the Controller board without any active
  components. No buffer or series resistors reside on the Controller for JTAG signals.
* **Cross-ref:** See `JTAG_Daughterboard/Design_Spec.md` for FT232H module schematics and assembly details.
  See DEC-016, DEC-023.

## 4. Telemetry & Logic (INA219 + SMBus)

* **Rotor Shunt:** **20mΩ (1206, 1%, 0.5W preferred; ≥0.25W minimum)** metal strip resistor on Stator board (Stator owns this component — see `Stator/Design_Spec.md`).
* **Sensing:** **Kelvin-connection (4-wire)** with 10Ω/0.1µF RC noise filtering.
* **Shunt Resistor:** 20mΩ (1206, 1%, 0.5W preferred; ≥0.25W minimum). Firmware must use R_SHUNT = 0.020Ω in the INA219 current calculation (I = V_shunt / R_shunt).
  * At 3A max: V_drop = 60mV — fits the INA219 ±80mV PGA range; 3.0A resolution ÷ 2¹² = 0.73mA/LSB.
* **Filtering:** 10Ω + 0.1µF RC filter on sensing lines to suppress rotor switching noise.
* **I2C Map:**
  * **INA219 Power Module Monitor**: I2C @ 0x40 on Power Module.
  * **INA219 Rotor Monitor**: I2C @ 0x45 on Stator (rotor stack current/voltage).
  * **STUSB4500 (PD Controller):** I2C @ 0x28 on Power Module.
  * **Smart Battery (SMBus):** I2C @ 0x0B on Power Module.

## 5. RTC Backup Battery

The CM5's MXL7704 PMIC contains an integrated RTC. To maintain timekeeping through power cycles,
a 3V coin cell is required on the CM5's VBAT pin (**Pin 95** on the CM5 Hirose DF40 200-pin connector).

### 5.1. Circuit Design

* **Battery (BT1):** Keystone 3034 CR2032 THT horizontal click-in holder. CR2032 = 3.0V, 220mAh.
  Estimated service life >25 years at <1µA RTC quiescent draw.
* **Protection Diode (D1):** Nexperia BAT54 Schottky diode (SOT-23, 30V, 200mA).
  Connected in series: BT1(+) → D1(anode), D1(cathode) → CM5 VBAT (Pin 95). Vf ≈ 0.3V @ 100µA; delivers
  ~2.7V to VBAT pin (within MXL7704 VBAT operating range). **This diode is mandatory with a CR2032 —
  it physically prevents the PMIC charging circuit from reaching the battery.**
* **Bypass Cap (C6):** 100nF X7R 0402 (Samsung CL05B104KB5NNNC) from VBAT to GND, placed within 5mm
  of the CM5 DF40 connector Pin 95.

> ⚠️ **Do NOT substitute ML2032 for CR2032 without removing D1.** The ML2032 is rechargeable and
> must connect directly to VBAT (no diode). The software charging-disable note in
> `Software/Linux_OS/Power_Management.md` also applies.

### 5.2. Placement

* **BT1:** Left edge of board, minimum 20mm from any high-speed trace (GbE pairs, USB 3.0, HDMI).
  Orient so the battery ejects away from the board centre for service access.
* **Battery replacement:** Classified as a **service-by-disassembly** task — not field-replaceable in-situ.
  Expected interval: >25 years under normal use. See `design/Guides/Maintenance_Guide.md`.

## 6. CM5 GPIO Mapping Matrix (Enigma-NG)

All GPIOs are referenced to **+3V3_ENIG**. Total current draw is limited to <50mA across all pins.

> **CM5 VDD_GPIO_REF:** The CM5 module VDD_GPIO_REF pin on the Hirose DF40 200-pin module connector
> must be connected to **3V3_ENIG** (not to the CM5-internal 3V3_SYSTEM rail, which is not used as a
> logic reference on this board). This ensures GPIO logic levels match all 3V3_ENIG-powered peripherals
> (CPLDs, FT232H VCCIO, etc.). Failure to connect VDD_GPIO_REF to 3V3_ENIG will result in incorrect
> GPIO logic levels for the entire system.

| GPIO | Function | Type | Logic Level | Description |
| :--- | :--- | :--- | :--- | :--- |
| **0 / 1** | **ID_EEPROM** | I2C | 3.3V | Reserved for CM5 HAT ID. |
| **2 / 3** | **I2C1_SDA/SCL** | I2C | 3.3V | **Main Bus:** INA219, STUSB4500, Smart Battery. |
| **4–15** | **DATA_BUS** | Output | 3.3V | **12-bit Parallel Bus** (D0-D11) to Stator/Rotors. |
| **16** | **ROTOR_EN** | Output | 3.3V | Enable signal to Power Module 3V3_ENIG LDO for sequenced rotor stack power-up. |
| **17** | **SW_LED_R** | PWM | 3.3V | RGB switch (SW1) — Red channel. Fault / graceful shutdown indicator. |
| **18** | **SW_LED_G** | PWM | 3.3V | RGB switch (SW1) — Green channel. USB-C active power source. |
| **19** | **SW_LED_B** | PWM | 3.3V | RGB switch (SW1) — Blue channel. PoE active power source. |
| **20** | **POE_STAT** | Input | 3.3V | Active Low: PoE live — LOW when PoE power good (TPS2372-4 /PG open-drain, per DEC-003). |
| **21** | **USB_STAT** | Input | 3.3V | Active Low: 12V/15V PD Negotiated. |
| **22** | **USB_FAULT** | Input | 3.3V | Active Low: USB power fault from on-board TPS2065C (local to Controller; no BtB pin required). |
| **23** | **BATT_PRES_N** | Input | 3.3V | Active Low: Battery present (via BtB pin 45; from Power Module J3 presence detect circuit R6/TPD1E10B06). |
| **24** | **SW_LED_CTRL** | Output | 3.3V | Drive HIGH when CM5 firmware is ready to control SW1 RGB LED; disables hardware MIC1555 orange-flash path on Power Module. |
| **25** | **SYS_FAULT** | Input | 3.3V | Active Low: eFuse fault interrupt from TPS25980 FAULT pin on Power Module (via BtB pin 29). Triggers OS fault handler in power monitor daemon; useful for power dashboard diagnostics even during graceful shutdown. |
| **26** | **SYS_RESET_N** | Output | 3.3V | Active Low: system-wide CPLD reset. Broadcast to all Intel MAX II EPM240T100C5N CPLDs via LINK-BETA pin 8 (Stator), Extension Ports, and Encoder Ports. On-board CPLDs (HID Encoder, Plugboard #1/#2) driven directly. |
| **27** | **PWR_GD** | Input | 3.3V | Active High: power-good signal from MCP121T-450E (4.50V threshold). HIGH = 5V_MAIN stable; deasserts on power loss, triggering graceful shutdown daemon. Arrives via Link-Alpha pin 34. |

## 7. Protection & EMI

* **External Links:** All inputs (Status) feature 10kΩ series resistors to protect CM5 pins from transient spikes.
* **Voltage:** 5V signals are strictly forbidden on these pins.
* **ESD Protection:** [TPD12S016](https://www.ti.com) (HDMI) and [TPD4E05U06](https://www.ti.com) (USB 3.0) on Layer 1.
* **Bulk Entry Bank Rule:** Use **5x 10uF X7R 50V** bulk decoupling capacitors at the Link-Alpha power-entry pins.
* **Capacitor Bank Geometry:** Place in a **Symmetrical Star/Spoke pattern**
  (one hub capacitor at entry, four spoke capacitors around it) to minimize input-rail impedance and reduce
  brown-out risk during current transients.
* **Status LED:** MIC1555-based 1Hz heartbeat flasher (Bilingual label: ACHTUNG: HEISS!).
* **Ferrite Beads:** Moved exclusively to the **Stator Board** to keep rotor switching noise isolated from the
  Controller logic.

## 8. Connectivity

### Link-Beta Connector (Samtec ERF8-020)

* **Part:** ERF8-020-05.0-S-DV-K-TR (Female Socket, 40-pin, 0.8mm pitch, 5.0mm stack height).
* **Mating Part (Stator):** ERM8-020-05.0-S-DV-K-TR (Male Header).
* **Pitch:** 0.8mm.
* **Stack Height:** 5.0mm.
* **Assembly:** SMT reflow; no THR clips required.
* **Decision:** See DEC-015 for 80→40 pin reduction rationale and poka-yoke safety note.

## 9. PCB Fabrication & Stackup

### PCB Fabrication (JLCPCB Specs)

* **Layers:** **6-Layer** (JLC06161H-2116 stackup).
  For production runs requiring verified controlled impedance (differential pairs: USB/HDMI/GbE),
  specify JLCPCB's 'Controlled Impedance' service (TDR-verified, ±10% tolerance). Prototype orders
  may omit this per DEC-017.
* **Finish:** **ENIG (Gold)** for all pads and diagnostic loops.
* **Solder Mask:** **Dark Green** (Vintage Industrial Lacquer aesthetic).
* **Silkscreen:** **White**, **Typewriter-style font**, Bilingual (ALL-CAPS GERMAN / Sentence-case English).
* **Branding:** Top-Left corner features the **Shielded Enigma-NG Square Emblem** (Exposed ENIG Gold tied to
  GND_CHASSIS).

### Advanced Layer Stackup (6-Layer / 2oz) [JLCPCB JLC06161H-2116]

* **L1 (Top):** SMT Components, I2C + PWR Control GPIOs & Shielded Ground Pour.
* **L2 (Internal):** Primary GND Plane (Logic Reference).
* **L3 (Internal):** High-Speed Data Striplines (USB/HDMI/GBE).
  * 90Ω Diff: 5.5 mil width / 7.5 mil gap (USB 3.0).
  * 100Ω Diff: 4.5 mil width / 8.5 mil gap (HDMI, Ethernet).
* **L4 (Internal):** High-Current Power Plane (5V_MAIN / 3V3_ENIG).
* **L5 (Internal):** Secondary GND Plane (Shielding).
* **L6 (Bottom):** Diagnostic Bank, Enigma 12-bit Data Bus, JTAG & Global Data Plate.

### Trace Widths & Impedance

| Net Class | Target Impedance | Width / Spacing | Layer |
| :--- | :--- | :--- | :--- |
| **USB 3.0** | 90Ω Differential | 5.5 mil / 7.5 mil | L3 (Stripline) |
| **Ethernet/HDMI** | 100Ω Differential | 4.5 mil / 8.5 mil | L3 (Stripline) |
| **JTAG signals** | 50Ω Single-ended | **5.0 mil (0.127 mm)** | L6 |
| **Power Rails (5V_MAIN / 3V3_ENIG)** | N/A (Low Drop) | 60.0 mil (Min) — 8.85A worst-case system / 12A LMQ capacity | L4 Island |
| **Logic/I2C** | N/A | 6.0 mil | L4 / L6 |
| **USB 2.0** | 90Ω Differential | TBD | TBD — pending trace-width-analysis investigation |
| **3V3_ENIG power** | N/A | TBD | TBD — pending trace-width-analysis investigation at 2.20A worst-case |

### Vias & Teardrops

* **VIPPO (Via-in-Pad):** 0.2mm Drill / 0.45mm Diameter (Plugged & Capped).
* **Standard Via:** 0.3mm Drill / 0.6mm Diameter (Staggered zigzag pattern).
  * **Spec-A (Premium):** Blind/Buried Vias (L1-L3) and Back-drilling for all 5Gbps differential pairs to eliminate
    stubs.
  * **Spec-B (Standard):** Through-hole Vias using **POFV (Via-in-Pad)**. Vias MUST be **Epoxy Filled and Capped**
    (IPC-4761 Type VII) to provide a flat solderable surface for CM5/Samtec pads.
* **Teardrops:** Enabled on all signal and power pads to reduce stress and impedance steps.
* **Copper:** 2oz Finished Copper (L1-L6).
* **Finish:** **ENIG (Electroless Nickel Immersion Gold)** mandatory for 0.4mm pitch integrity.

## 10. Thermal, Branding & Diagnostics

### Thermal & Branding

* **Logo:** Top-left 10mm "Enigma-NG" shielded gold emblem.
* **eFuse:** Top-right near power inputs with dedicated "Caution: Hot" silkscreen.

### Diagnostics & Aesthetics

* **Bank:** 2x8 ENIG Gold Diagnostic Looped Probe Pad Bank for real-time bus monitoring.
  * **Placement:** 2x8 2.54mm ENIG Gold Looped Probe Pad Bank placed directly behind the BtB header.
  * **Orientation:** Facing Upwards for easy logic analyser ribbon cable connection.
  * **Visuals:** Typewriter-style bilingual silkscreen legend on the bottom layer.
* **Silkscreen:** Dark Green mask with White Bilingual Typewriter font.
* **Branding:** Inverted Master Data Plate (Silhouette + JLC Serial Block) on L6 (Bottom).

#### Symmetrical Diagnostics

* **Bank-Alpha (Power/Entry):** 2x10 ENIG Gold Looped Probe Pads (L1). Monitors 5V/3.3V, I2C Telemetry, Status LEDs,
  and BATT_PRES.
* **Bank-Beta (Logic/Exit):** 2x10 ENIG Gold Looped Probe Pads (L1). Monitors 12-bit Sniffer (ENC_IN/OUT), JTAG, and
  SYS_RESET_N.
* **JTAG Shielding:** JTAG_TCK (Pin 15) isolated from TDI/TMS via GND buffer (Pin 16).

## 11. Bill of Materials

| Ref | Component | Value | Package | Mouser Part # | DigiKey Part # | JLCPCB Part # |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| C1-C5 | Bulk entry decoupling bank (star/spoke) | 10uF X7R 50V | 1206 | 187-CL31B106KBHNNNE | 1276-6767-1-ND | CL31B106KBHNNNE |
| C6 | VBAT bypass cap | 100nF X7R 50V | 0402 | 187-CL05B104KB5NNNC | 1276-1005-1-ND | CL05B104KB5NNNC |
| BT1 | CR2032 coin cell holder (RTC backup) | Keystone 3034 | THT horizontal | 534-3034 | 36-3034-ND | C70377 |
| D1 | VBAT Schottky protection (blocks CR2032 charge path) | Nexperia BAT54 | SOT-23 | 771-BAT54215 | 1727-1064-1-ND | C8598 |
| J1 | Link-Alpha 80-pin Socket | ERF8-040-05.0-S-DV-K-TR (female) | Samtec | 200-ERF8040050SDVKTR | SAM8621-ND | C3640808 |
| J2 | Link-Beta 40-pin Socket | ERF8-020-05.0-S-DV-K-TR (female) | Samtec | 200-ERF8020050SDVKTR | SAM8619CT-ND (CT) / SAM8619TR-ND (T&R) / SAM8619DKR-ND (DKR) | C6034565 |
| J3 | USB 3.0 Type-A | Dual-Stack | Molex 48406-0003 | 538-0484060003 | WM1394-ND | C123458 |
| J4 | HDMI Type-A | Full-Size | TE 2007435-1 | 571-2007435-1 | A125057-ND | C123459 |
| R1 | Pull-up for reset | 10kΩ | 0603 | 667-ERJ-3EKF1002V | P10.0KBYCT-ND | C25804 |
| R2 | Termination for differential | 100Ω | 0603 | 667-ERJ-3EKF1000V | P100BYCT-ND | C25806 |
| R3 | PWR_GD GPIO pull-up (to 3V3_ENIG) | 10kΩ 1% | 0603 | 667-ERJ-3EKF1002V | P10.0KBYCT-ND | C25804 |
| U1 | Raspberry Pi Compute Module 5 (CM5) | N/A | CM5 | CM5 | N/A — source from RPi distributors | N/A — not stocked at JLCPCB |
| U2 | USB power switch | TPS2065C | SOIC-8 | 595-TPS2065CDBVR | 296-TPS2065CDBVRCT-ND | C123460 |
| U3 | HDMI power switch | AP2331W | SOT-23 | 621-AP2331W-7 | AP2331W-7DICT-ND | C123461 |
| U4 | USB/HDMI ESD | TPD4E05U06 | VQFN | 595-TPD4E05U06DBVR | 296-TPD4E05U06DBVRCT-ND | C123462 |

### BOM Notes

Telemetry shunt specifications and Kelvin-sensing notes are detailed in §4. Protection, ESD, and bulk decoupling
capacitor placement rules are detailed in §7. Mating header assembly specifications are in §8.
