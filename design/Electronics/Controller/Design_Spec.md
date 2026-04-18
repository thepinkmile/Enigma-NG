# Controller Board (V1.0) Design Specification

**Status:** Draft
**Project:** Enigma-NG
**Author:** Izzyonstage & GitHub Copilot
**Version:** v1.0.0
**Associated Hardware Revision:** Rev A
**Last Updated:** 2026-04-17

---

## 1. Overview

The Controller Board is a custom carrier board for the Raspberry Pi Compute Module 5 (CM5), providing the
central processing and supervisory function for the Enigma-NG system. It interfaces with the Power Module
and Stator board via the 80-pin Link-Alpha and 40-pin Link-Beta board-to-board connectors respectively,
and hosts the JTAG Daughterboard hat connectors for debug access.

* **Module:** Raspberry Pi Compute Module 5 (CM5).
* **Role:** Master traffic controller for Power (Alpha) and Encryption Logic (Beta).
* **Stackup:** 6-Layer / 2oz Finished Copper (JLC06161H-2116) for 5Gbps differential pair integrity.
* **Shielding:** High-speed signals (Ethernet, USB 3.0, HDMI) routed as Striplines on L3, shielded by L2/L5 GND planes
  and L4 (Internal) for High-Current Power Plane (5V_MAIN / 3V3_ENIG).
* **USB-C:** Power delivery handled by the Power Module via Link-Alpha (J1). The Controller has no direct USB-C connector.
* **Status LED:** Hardware heartbeat (1Hz pulse, generated on Power Module) triggers on power-up before CM5 boot for instant status confirmation.

### Functional & Design Requirements

#### Functional Requirements

| ID | Functional Requirement | Notes | Satisfied By / Cross-Ref |
| :--- | :--- | :--- | :--- |
| FR-CTL-01 | Host the Raspberry Pi Compute Module 5 as the system master processor | CM5 runs the Linux OS and all application logic | BOM U1 (CM5) |
| FR-CTL-02 | Receive power from the Power Module and distribute to the CM5 and peripherals | Via Link-Alpha (J1) | §2 Dual-Link Interface; BOM J1 (ERF8-040) |
| FR-CTL-03 | Provide external I/O interfaces for system management | GbE, HDMI, USB 3.0 | §8 Connectivity; BOM J3 (USB 3.0), J4 (HDMI) |
| FR-CTL-04 | Provide JTAG programming capability for all 37 CPLDs in the system | Via JTAG Daughterboard and Link-Beta | §3 JTAG Programming Subsystem; BOM J2 (Link-Beta) |
| FR-CTL-05 | Monitor system power and load telemetry via I²C and report discrete power status signals to CM5 via GPIO | Telemetry: INA219 ×2 (PM U12 @ 0x40 for 5V_MAIN; Stator U2 @ 0x45 for rotor stack) and LTC3350 @ 0x09; Discrete: PoE presence, battery presence, USB fault, PWR_GD | §4 Telemetry & Logic; §6 CM5 GPIO Mapping Matrix |
| FR-CTL-06 | Maintain RTC operation across power cycles using a CR2032 backup battery | Non-rechargeable; service by disassembly | §5 RTC Backup Battery; BOM BT1, D1 (BAT54) |
| FR-CTL-07 | Route Link-Beta signals between the CM5/JTAG Daughterboard and the Stator board | Via J2 | §2 Dual-Link Interface; BOM J2 (ERF8-020) |
| FR-CTL-08 | Provide DSI1 display interface connector for optional lid-mounted touchscreen add-on | DSI1 4-lane FPC connector (J_DSI1) on Controller Board; display add-on board to be designed separately | §8 Connectivity; BOM J_DSI1 |

#### Design Requirements

| ID | Design Requirement | Specification | Satisfied By / Cross-Ref |
| :--- | :--- | :--- | :--- |
| DR-CTL-01 | PCB stackup | 6-layer, 2oz finished copper (JLC06161H-2116) | §9 PCB Fabrication & Stackup |
| DR-CTL-02 | CM5 module | Raspberry Pi Compute Module 5 (SO-DIMM form factor). Minimum spec: 8 GB RAM, 4 GB eMMC. CM5 Lite (no onboard wireless, no onboard flash) is NOT permitted. BOM reference: various (e.g. CM5008032). | BOM U1 |
| DR-CTL-03 | Link-Alpha connector | J1 = ERF8-040-05.0-S-DV-K-TR (80-pin female, 0.8 mm pitch) | BOM J1 (ERF8-040-05.0-S-DV-K-TR) |
| DR-CTL-04 | Link-Beta connector | J2 = ERF8-020-05.0-S-DV-K-TR (40-pin female, 0.8 mm pitch) | BOM J2 (ERF8-020-05.0-S-DV-K-TR) |
| ~~DR-CTL-05~~ | ~~Reserved / deleted~~ | ~~—~~ | ~~—~~ |
| DR-CTL-06 | USB current limit | 1.6 A via TPS2065C; fault output to GPIO 22 (USB_FAULT) | BOM U2 (TPS2065C); §6 GPIO Mapping (GPIO 22) |
| DR-CTL-07 | RTC battery holder | BT1 = Keystone 3034 (THT horizontal CR2032 holder) | §5 RTC Backup Battery; BOM BT1 (Keystone 3034) |
| DR-CTL-08 | RTC protection | D1 = Nexperia BAT54 Schottky diode (blocks PMIC VBAT charge path) | §5 RTC Backup Battery; BOM D1 (BAT54) |
| DR-CTL-09 | RTC bypass capacitor | C6 = 100 nF 0402 on CM5 VBAT (Pin 95, Hirose DF40 200-pin) | §5 RTC Backup Battery; BOM C6 |
| DR-CTL-10 | RGB LED interface | Controller must provide PWM-capable GPIO outputs for SW1 RGB LED (3 channels: SW_LED_R, SW_LED_G, SW_LED_B) and a separate logic output (SW_LED_CTRL) to arbitrate firmware vs hardware LED control. Pin-level details in §6 GPIO matrix. | §6 CM5 GPIO Mapping Matrix |
| DR-CTL-11 | OS/firmware configuration | All firmware configuration requirements (including RTC charging disable) are specified in the Linux OS design spec. See `design/Software/Linux_OS/`. | design/Software/Linux_OS/ |
| DR-CTL-12 | DSI1 connector | J_DSI1 = 15-pin 1.0mm pitch ZIF/FPC (TBD MPN — confirm against CM5 DSI1 pin mapping at schematic phase); DSI1 4-lane: CLK+/−, D0+/−, D1+/−, D2+/−, D3+/− = 10 differential signals; 100 Ω differential impedance; route on L3 (stripline, same as HDMI); capacitive touch I²C routed via I²C-1 bus (SDA/SCL on J_DSI1 power connector) | §8 Connectivity; BOM J_DSI1 |

## 2. Dual-Link Interface (Samtec ERx8)

> **Assembly Note:** Both BtB connectors (J1 and J2) use ERF8 **female** sockets. This is a deliberate mechanical
> choice — the Controller slides into the enclosure and simultaneously blind-mates with the Power Module (J1) and
> Stator (J2) along the back edge in a single insertion motion. See DEC-014.

* **Link-Alpha (Power/Entry):** ERF8 Female Socket 80-pin Power/Ethernet/Telemetry entry from Power Module.
  * Receives: 5V_MAIN, 3V3_ENIG, GbE, I²C Telemetry bus, and PWR_GD from Power Module.
  * Provides to PM: SW_LED_R, SW_LED_G, SW_LED_B (RGB LED channels), ETH_LED_LINK, ETH_LED_ACT (Ethernet status LEDs), ROTOR_EN (LDO enable), SW_LED_CTRL (LED arbitration).
  * **Cross-ref:** See `Power_Module/Design_Spec.md` and `Power_Module/Board_Layout.md` for the matching Link-Alpha
    pin allocation and power flow definitions.
* **Link-Beta (Logic/Stator):** ERF8 Female Socket 40-pin Encryption/JTAG interface to Stator Board.
  * Provides: JTAG and 3V3_ENIG to Stator.
  * **Cross-ref:** See `Stator/Design_Spec.md` and `Stator/Board_Layout.md` for explicit pin mapping and connector
    compliance. See DEC-015 for 40-pin reduction rationale and poka-yoke safety note.
* **3V3_ENIG:** The Controller is an active consumer of 3V3_ENIG — CM5 VDD_GPIO_REF and on-board peripherals are powered from this rail via the LINK-ALPHA tap node.
  Bulk X7R decoupling capacitors are required at the 3V3_ENIG tap node on the Controller (DEC-TBD — new decision required; specific values deferred to detailed design phase).
  The 2oz copper L3 highway continues to link Alpha and Beta for the rotor stack pass-through.

### 2.1. Connectivity & Bus (on Link-Alpha)

* **High-Speed Interconnect (BtB Samtec):**
  * **Connector:** Samtec ERF8-040 (Female Socket, 80-pin, 0.8mm pitch). See DEC-014.
  * **Mating Style:** Board-to-Board vertical stack; SMT reflow. Mates with ERM8-040 (Male) on Power Module.
  * **Pin Summary:**
    * **Pins 1–20:** GbE MDI diff pairs (4 pairs + GND shields), 100Ω stripline on L3.
    * **Pins 21–24:** 5V_MAIN power entry (supplemental) + GND return.
    * **Pins 25–26:** ETH_LED_LINK / ETH_LED_ACT (active-low).
    * **Pins 27–28:** GND isolation moat.
    * **Pins 29–38:** Status/control signals (SYS_FAULT, POE_STAT, SW_LED_R/G/B, PWR_GD, I2C1, USB_STAT).
    * **Pins 39–44:** 3V3_ENIG power (6 pins × 0.5A = 3.0A capacity).
    * **Pins 45–48:** Mixed control (BATT_PRES_N, ROTOR_EN, SW_LED_CTRL, PWR_BUT).
    * **Pins 49–80:** 5V_MAIN high-current entry (32 pins interleaved: 16× 5V_MAIN + 16× GND; 16 × 0.5A = 8A from this cluster; combined with pins 21–22 = 9A total).
  * **Power Vias:** 4-via "Power Clusters" (0.3mm drill) per Samtec power pin for thermal stability.
  * **Full pin table:** See `Controller/Board_Layout.md` LINK-ALPHA section.
* **Ethernet:** 100Ω Stripline pairs on L3, shielded by L2/L5 ground planes (GbE MDI).

### 2.2. Connectivity & Bus (on Link-Beta)

* **High-Speed Interconnect (BtB Samtec):**
  * **Connector:** Samtec ERF8-020 (Female Socket, 40-pin, 0.8mm pitch). See DEC-015.
  * **Mating Style:** Board-to-Board vertical stack; SMT reflow. Mates with ERM8-020 (Male) on Stator.
  * **Pin Summary:**
    * **Pins 1–9:** JTAG chain only, GND-shielded (6 internal GND pins; pin 8 now tied to GND).
    * **Pins 10–11:** GND isolation moat.
    * **Pins 12–13:** I2C1_SDA / I2C1_SCL extend the CM5 I²C-1 bus onto the Stator for U_EXP1/U_EXP2/U_EXP4, INA219, PCA9685, and the downstream Settings Board expanders.
    * **Pins 14–17:** 5V_MAIN grouped power delivery (4× pins for current sharing,
      0.5A per pin = 2.0A total capacity). Routed to the Stator for the Settings Board
      indicator rail (`5V_MAIN`, 240mA max), J_SERVO servo motor power
      (5V_MAIN, up to 500mA), and future 5V headroom.
    * **Pin 18:** GND return moat for the grouped 5V_MAIN cluster.
    * **Pins 19–21:** Additional 3V3_ENIG feed (3× pins) added after DEC-031 freed the
      former ENC_OUT monitor block.
    * **Pins 22–24:** Additional GND return cluster paired with the grouped power block.
    * **Pins 25–27:** GND / TTD_RETURN / GND shield cluster (TTD_RETURN on pin 26 only).
    * **Pins 28–35:** 3V3_ENIG power (8 pins × 0.5A = 4.0A capacity; combined with pins
      19–21 this makes LINK-BETA 3V3_ENIG overprovisioned relative to the 3.0A LDO limit).
    * **Pins 36–40:** GND power return (5 pins).
  * **Full pin table:** See `Controller/Board_Layout.md` LINK-BETA section.
* **Programming:** Internal USB 2.0 link to the JTAG Daughterboard.
* **Encryption Sniffer Bus**
  * **Purpose:** ENC_IN/ENC_OUT monitoring has been migrated from CM5 GPIO to MCP23017 U_EXP1
    (@ 0x20, Stator) via I²C. CM5 GPIO 4–15 are now freed for future use. See DEC-031.
  * **Naming convention:** Signal names are relative to the **Enigma machine**, not the CM5.
    `ENC_IN` = the plaintext character entering the machine (from the Keyboard/Encoder board);
    `ENC_OUT` = the encrypted character exiting the machine (to the Lightboard).
  * **ENC_IN [0:5]:** Now read via MCP23017 U_EXP1 GPA[0:5] @ 0x20 (Stator) over I²C-1.
  * **ENC_OUT [0:5]:** Now read via MCP23017 U_EXP1 GPB[0:5] @ 0x20 (Stator) over I²C-1.
  * **Reset:** SYS_RESET_N migrated to MCP23017 U_EXP2 GPA[7] @ 0x21 (Stator) via I²C.
    R6 pull-up (10kΩ to 3V3_ENIG) on Stator keeps CPLDs out of reset at power-up. See DEC-031.
  * **Software cross-reference:**
    * GUI application real-time display logic: `design/Software/GUI_App/Design_Spec.md`
    * Linux OS power management, I²C telemetry, and system daemon: `design/Software/Linux_OS/Power_Management.md`

### 2.3. CM5 Module Keep-Out Zone

The area directly beneath the mounted CM5 module (55mm × 40mm footprint) shall be designated
a **component keep-out zone** on all layers:

* No active or passive components, tall features, or exposed via pads may be placed in this area.
* Copper fills, signal routing, and power planes are permitted beneath the module.
* Enforced in KiCad via a keepout region on the `User.Courtyard` layer covering the full CM5 footprint.
* Minimum clearance beneath the CM5: **2.5mm** (set by Amphenol 10164227-1004A1RLF 4.0mm stacking height minus 1.5mm CM5 PCB thickness).

### 2.4. Physical Connector Placement

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

The Controller provides JTAG pass-through only. All JTAG chain architecture, device ordering, buffering, termination, and timing specifications are defined in the JDB Design_Spec.

* **Controller Pass-Through:** JTAG lines (TCK, TMS, TDI, TTD_RETURN, VREF) are routed directly from the JDB hat-header (J_JDB) to LINK-BETA (J2) on the Controller board without any active
  components. No buffer or series resistors reside on the Controller for JTAG signals.
* **Cross-ref:** See `JTAG_Daughterboard/Design_Spec.md` for all JTAG chain architecture, FT232H module schematics, buffering, and assembly details. See DEC-016, DEC-024.

## 4. Telemetry & Logic (INA219 + SMBus)

Current monitoring for both rails is managed via the I2C-1 bus (CM5 GPIO 2/3) and is
implemented on the respective boards — not on the Controller:

* **INA219 U12 (0x40) — 5V_MAIN monitor:** Power Module. See `Power_Module/Design_Spec.md §3 Telemetry`.
* **INA219 U2 (0x45) — Rotor-stack monitor:** Stator board. See `Stator/Design_Spec.md §5. Power Telemetry`.

For DT bindings and driver configuration for both INA219 devices, see
`Software/Linux_OS/Power_Management.md §INA219 Rotor Stack Current Monitor`.

### 4.1. I²C Bus Topology

All I²C devices share the single I²C-1 bus (CM5 GPIO 2/3) routed through to the Power Module (LINK-ALPHA) and Stator (LINK-BETA).

| Address | Device | Location | Function |
| :--- | :--- | :--- | :--- |
| 0x09 | LTC3350 | Power Module | Supercap charger/monitor |
| 0x0B | Smart Battery | Power Module | SMBus battery monitoring |
| 0x28 | STUSB4500 | Power Module | USB-C PD controller |
| 0x40 | INA219 (U12) | Power Module | 5V_MAIN current/power telemetry |
| 0x45 | INA219 (U2) | Stator | Rotor stack current/power telemetry |
| 0x20 | MCP23017 (U_EXP1) | Stator | ENC_IN/ENC_OUT monitoring (16 GPIO) |
| 0x21 | MCP23017 (U_EXP2) | Stator | Virtual keypress injection, SOURCE_SEL, SYS_RESET_N, servo control |
| 0x22 | MCP23017 (U_EXP4) | Stator | CPLD config output driver (DEC-032) |
| 0x23 | MCP23017 (U_EXP_SW_IN) | Settings Board | Switch input reader (DEC-032) |
| 0x24 | MCP23017 (U_LED_B1) | Settings Board | Bank 1 LED controller: 5× anodes + RGB bank-rail drivers (DEC-034) |
| 0x25 | MCP23017 (U_LED_B2) | Settings Board | Bank 2 LED controller: 7× anodes + RGB bank-rail drivers (DEC-034) |
| 0x60 | PCA9685 (U_EXP3) | Stator | Servo PWM driver (Ch0 = 50Hz SERVO_PWM) |

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

All GPIOs are referenced to **3V3_ENIG**. BCM2712 silicon limit: 50mA aggregate per GPIO bank.

> **CM5 VDD_GPIO_REF:** The CM5 module VDD_GPIO_REF pin on the Hirose DF40 200-pin module connector
> must be connected to **3V3_ENIG** (not to the CM5-internal 3V3_SYSTEM rail, which is not used as a
> logic reference on this board). This ensures GPIO logic levels match all 3V3_ENIG-powered peripherals
> (CPLDs, FT232H VCCIO, etc.). Failure to connect VDD_GPIO_REF to 3V3_ENIG will result in incorrect
> GPIO logic levels for the entire system.

| GPIO | Function | Type | Logic Level | Description |
| :--- | :--- | :--- | :--- | :--- |
| **2 / 3** | **I2C1_SDA/SCL** | I2C | 3.3V | **Main Bus:** LTC3350 @ 0x09, Smart Battery @ 0x0B, STUSB4500 @ 0x28, INA219 (PM U12) @ 0x40, INA219 (Stator U2) @ 0x45, MCP23017 U_EXP1 @ 0x20, MCP23017 U_EXP2 @ 0x21, MCP23017 U_EXP4 @ 0x22, MCP23017 U_EXP_SW_IN @ 0x23, MCP23017 U_LED_B1 @ 0x24, MCP23017 U_LED_B2 @ 0x25, PCA9685 U_EXP3 @ 0x60. |
| **4–9** | *(freed)* | — | — | **Previously ENC_IN[0:5].** Monitoring migrated to MCP23017 U_EXP1 GPA[0:5] @ 0x20 (Stator) via I²C. GPIO 4–9 are now available for future use. See DEC-031. |
| **10–15** | *(freed)* | — | — | **Previously ENC_OUT[0:5].** Monitoring migrated to MCP23017 U_EXP1 GPB[0:5] @ 0x20 (Stator) via I²C. GPIO 10–15 are now available for future use. See DEC-031. |
| **16** | **ROTOR_EN** | Output | 3.3V | Enable signal to Power Module 3V3_ENIG LDO for sequenced rotor stack power-up. |
| **17** | **SW_LED_R** | PWM | 3.3V | RGB switch (SW1) — Red channel. Fault / graceful shutdown indicator. |
| **18** | **SW_LED_G** | PWM | 3.3V | RGB switch (SW1) — Green channel. USB-C active power source. |
| **19** | **SW_LED_B** | PWM | 3.3V | RGB switch (SW1) — Blue channel. PoE active power source. |
| **20** | **SW_LED_CTRL** | Output | 3.3V | Drive HIGH when CM5 firmware is ready to control SW1 RGB LED; disables hardware LED fallback path on Power Module. Groups LED signals with GPIOs 17–19. |
| **21** | **USB_STAT** | Input | 3.3V | Active Low: 15V/5A PD Negotiated (STUSB4500). |
| **22** | **USB_FAULT** | Input | 3.3V | Active Low: USB power fault from on-board TPS2065C (local to Controller; no BtB pin required). |
| **23** | **BATT_PRES_N** | Input | 3.3V | Active Low: Battery present (via BtB pin 45; from Power Module J3 presence detect circuit R6/TPD1E10B06DYARQ1). |
| **24** | **POE_STAT** | Input | 3.3V | Active Low: PoE live — LOW when PoE power good (TPS2372-4 /PG open-drain, per DEC-003). |
| **25** | **SYS_FAULT** | Input | 3.3V | Active Low: eFuse fault interrupt from TPS25980 FAULT pin on Power Module (via BtB pin 29). Triggers OS fault handler in power monitor daemon; useful for power dashboard diagnostics even during graceful shutdown. |
| **26** | *(freed)* | — | — | **Previously SYS_RESET_N.** System-wide CPLD reset migrated to MCP23017 U_EXP2 GPA[7] @ 0x21 (Stator) via I²C. R6 pull-up (10kΩ to 3V3_ENIG) on Stator ensures CPLDs remain out of reset at power-up. GPIO 26 is now available for future use. See DEC-031. |
| **27** | **PWR_GD** | Input | 3.3V | Rail-health telemetry only — HIGH while 5V_MAIN ≥ 4.50V; does NOT trigger shutdown. Arrives via Link-Alpha pin 34. |

## 7. Protection & EMI

* **External Links:** All inputs (Status) feature 10kΩ series resistors to protect CM5 pins from transient spikes.
* **Voltage:** 5V signals are strictly forbidden on: CM5 GPIO pins, I²C SDA/SCL lines, JTAG (TDI/TDO/TCK/TMS), and all logic-level signals on LINK-ALPHA.
* **ESD Protection:** [TPD4E05U06](https://www.ti.com) (U4 — USB/HDMI ESD arrays) on Layer 1.
* **5V_MAIN Bulk Entry:** 5× 10µF X7R 50V at LINK-ALPHA 5V_MAIN entry pins per `design/Standards/Global_Routing_Spec.md §3` Bulk Entry Bank Rule.
* **3V3_ENIG Tap Decoupling:** Bulk X7R decoupling capacitors are required at the 3V3_ENIG tap node on the Controller (DEC-TBD — new decision required; specific values deferred to detailed design
  phase). These are distinct from the 5V_MAIN entry bank above.
* **Hardware LED Fallback:** The hardware LED fallback path (MIC1555 oscillator) is located on the Power Module.
  See `Power_Module/Design_Spec.md §Design §5. Protection & Logic` for the full SW1 RGB LED handoff circuit detail.

## 8. Connectivity

### 8.1. Link-Alpha Connector (Samtec ERF8-040)

* **Part:** ERF8-040-05.0-S-DV-K-TR (Female Socket, 80-pin, 0.8mm pitch, 5.0mm stack height).
* **Mating Part (Power Module):** ERM8-040-05.0-S-DV-K-TR (Male Header).
* **Full Pin Table:** See `Controller/Board_Layout.md` LINK-ALPHA section for the authoritative 80-pin table.
* **Pin Summary:**

| Pins | Signal | Direction | Description |
| :--- | :--- | :--- | :--- |
| 1–20 | GbE (MDI0±/MDI1±/MDI2±/MDI3±) + GND | Bidir | 100Ω diff pairs, GND-shielded |
| 21–22 | 5V_MAIN | PM → CTRL | Supplemental power entry |
| 23–24 | GND | — | Supplemental return |
| 25 | ETH_LED_LINK | CTRL → PM | Active-low Ethernet link LED |
| 26 | ETH_LED_ACT | CTRL → PM | Active-low Ethernet activity LED |
| 27–28 | GND | — | Isolation moat |
| 29 | SYS_FAULT | PM → CTRL | eFuse fault (active-low, CM5 GPIO 25) |
| 30 | POE_STAT | PM → CTRL | PoE live status (active-low, CM5 GPIO 24) |
| 31 | SW_LED_R | CTRL → PM | RGB LED red channel (CM5 GPIO 17) |
| 32 | SW_LED_G | CTRL → PM | RGB LED green channel (CM5 GPIO 18) |
| 33 | SW_LED_B | CTRL → PM | RGB LED blue channel (CM5 GPIO 19) |
| 34 | PWR_GD | PM → CTRL | Power-good from MCP121T-450E (CM5 GPIO 27) |
| 35 | I2C1_SDA | Bidir | I²C bus data (CM5 GPIO 2) |
| 36 | I2C1_SCL | Bidir | I²C bus clock (CM5 GPIO 3) |
| 37 | GND | — | I²C shield return |
| 38 | USB_STAT | PM → CTRL | USB-C PD status (CM5 GPIO 21) |
| 39–44 | 3V3_ENIG | PM → CTRL | Logic rail, 6 pins = 3.0A |
| 45 | BATT_PRES_N | PM → CTRL | Battery presence (active-low, CM5 GPIO 23) |
| 46 | ROTOR_EN | CTRL → PM | LDO enable (CM5 GPIO 16) |
| 47 | SW_LED_CTRL | CTRL → PM | LED arbitration (CM5 GPIO 20) |
| 48 | PWR_BUT | PM → CTRL | CM5 PMIC power-button input (active LOW). Driven by MIC1555 one-shot (3 s pulse on backup) or SW2 (manual press). CM5 module integrates 10kΩ pull-up. |
| 49–80 | 5V_MAIN / GND (interleaved) | PM → CTRL | 9A delivery cluster |

### 8.2. JDB Hat Connectors

The JTAG Daughterboard mounts as a hat on the Controller via two 2.54mm headers.

#### J_JDB_PWR — Power/USB Header (1×5, 2.54mm)

* **Part:** Adam Tech RS1-05-G (Female Socket, 1×5, 2.54mm pitch, vertical THT). Mouser 737-RS1-05-G, DigiKey 2057-RS1-05-G-ND, JLCPCB C3321119.
* **Mating Part (JDB J1):** Adam Tech PH1-05-UA — 1×5 2.54mm male pin header (JLCPCB C5374051). See `JTAG_Daughterboard/Design_Spec.md §3`.
* **Full Pin Table:** See `Controller/Board_Layout.md` JDB Hat Connectors section for the authoritative pinout.
* **Pin Summary:**

| Pin | Signal | Direction | Description |
| :--- | :--- | :--- | :--- |
| 1 | 5V_USB | CTRL → JDB | 5V USB power (from TPS2065C rail) |
| 2 | 3V3_ENIG | CTRL → JDB | 3.3V logic rail (JTAG signal reference) |
| 3 | USB_D+ | Bidir | USB 2.0 D+ to CM5 |
| 4 | USB_D− | Bidir | USB 2.0 D− to CM5 |
| 5 | GND | — | Power/signal return |

#### J_JDB_JTAG — JTAG Output Header (1×10, 2.54mm)

* **Part:** Adam Tech RS1-10-G (Female Socket, 1×10, 2.54mm pitch, vertical THT). Mouser 737-RS1-10-G, DigiKey 2057-RS1-10-G-ND, JLCPCB C3320525.
* **Mating Part (JDB J2):** Adam Tech PH1-10-UA — 1×10 2.54mm male pin header (JLCPCB C3330527). See `JTAG_Daughterboard/Design_Spec.md §3`.
* **Full Pin Table:** See `Controller/Board_Layout.md` JDB Hat Connectors section for the authoritative pinout.
* **Pin Summary:**

| Pin | Signal | Direction | Description |
| :--- | :--- | :--- | :--- |
| 1 | TCK | JDB → CTRL | JTAG clock (buffered via U5) |
| 2 | GND | — | Ground |
| 3 | TDI | JDB → CTRL | JTAG data in |
| 4 | GND | — | Ground |
| 5 | TDO | CTRL → JDB | JTAG data out (TTD_RETURN) |
| 6 | GND | — | Ground |
| 7 | TMS | JDB → CTRL | JTAG mode select (buffered via U5) |
| 8 | GND | — | Ground |
| 9 | VREF (3V3_ENIG) | CTRL → JDB | Voltage reference for JTAG logic |
| 10 | GND | — | Ground |

### 8.3. Link-Beta Connector (Samtec ERF8-020)

* **Part:** ERF8-020-05.0-S-DV-K-TR (Female Socket, 40-pin, 0.8mm pitch, 5.0mm stack height).
* **Mating Part (Stator):** ERM8-020-05.0-S-DV-K-TR (Male Header).
* **Pitch:** 0.8mm.
* **Stack Height:** 5.0mm.
* **Assembly:** SMT reflow; no THR clips required.
* **Decision:** See DEC-015 for 80→40 pin reduction rationale and poka-yoke safety note.
* **Full Pin Table:** See `Controller/Board_Layout.md` LINK-BETA section for the authoritative 40-pin table.
* **Pin Summary:**

| Pins | Signal | Direction | Description |
| :--- | :--- | :--- | :--- |
| 1 | GND | — | JTAG leading shield |
| 2 | TCK | CTRL → Stator | JTAG clock |
| 3 | GND | — | TCK/TMS inter-pin shield |
| 4 | TMS | CTRL → Stator | JTAG mode select |
| 5 | GND | — | TMS/TDI inter-pin shield |
| 6 | TDI | CTRL → Stator | JTAG data in |
| 7 | GND | — | TDI/GND inter-pin shield |
| 8 | GND | — | Extra JTAG trailing/guard ground; reassigned from former SYS_RESET_N spare in DEC-036 |
| 9–11 | GND | — | JTAG trailing shield + isolation moat |
| 12 | I2C1_SDA | Bidir | I²C-1 data extension to Stator/Settings bus (mirrors Link-Alpha pin 35 / CM5 GPIO 2). |
| 13 | I2C1_SCL | Bidir | I²C-1 clock extension to Stator/Settings bus (mirrors Link-Alpha pin 36 / CM5 GPIO 3). |
| 14–17 | 5V_MAIN | PM → Stator | Grouped supplemental 5V feed; 4 pins = 2.0A total capacity for servo + Settings rail + future margin |
| 18 | GND | — | 5V_MAIN return moat / inter-group shield |
| 19–21 | 3V3_ENIG | PM → Stator | Additional 3V3_ENIG feed pins added after DEC-031 freed the former monitor block |
| 22–24 | GND | — | Additional grouped return pins paired with the 5V_MAIN / 3V3_ENIG expansion cluster |
| 25 | GND | — | ENC_OUT / TTD_RETURN shield |
| 26 | TTD_RETURN | Stator → CTRL | JTAG TDO short-path return (bypasses rotor stack) |
| 27 | GND | — | TTD_RETURN shield |
| 28–35 | 3V3_ENIG | PM → Stator | Power pass-through (8 pins = 4.0A; combined LINK-BETA total = 11 pins = 5.5A connector capacity) |
| 36–40 | GND | — | Power return |

### 8.4. Fan Connector (J_FAN)

* **Part:** JST SM04B-SRSS-TB(LF)(SN) — 4-pin JST SH 1.0mm pitch right-angle header
* **Mating Part:** JST SHR-04V-S (female crimp housing)
* **JLCPCB:** C160404 | **Mouser:** 306-SM04BSRSSTBLFSN | **DigiKey:** 455-SM04B-SRSS-TBCT-ND
* **Pinout:**

| Pin | Signal | Source |
| --- | ------ | ------ |
| 1 | 5V_MAIN | Controller 5V_MAIN rail |
| 2 | GND | Controller GND |
| 3 | FAN_TACH | CM5 module connector Pin 16 |
| 4 | FAN_PWM | CM5 module connector Pin 19 |

* FAN_TACH and FAN_PWM connect directly from the CM5 module DF40 connector (dedicated BCM2712 fan controller interface). No GPIO allocation required.
* Mating fan cable: JST SHR-04V-S housing with 4× JST SSH-003T-P0.2 crimp terminals.

### 8.5. DSI1 Display Connector (J_DSI1)

* **DSI1 Display (J_DSI1):** 15-pin 1.0mm pitch ZIF/FPC connector (TBD MPN). Breaks out DSI1
  4-lane interface from CM5 for optional lid-mounted touchscreen add-on. Display add-on board
  design is deferred (see DEC-033). Connector placed near CM5 mezzanine socket on L1.
  Touch I²C routed on I²C-1 bus shared with other Stator/Controller peripherals.
* **Interface:** MIPI DSI1 — 4-lane differential (CLK+/−, D0+/−, D1+/−, D2+/−, D3+/−).
* **Impedance:** 100 Ω differential; route on L3 (stripline) — same rule as HDMI/Ethernet.
* **MPN:** TBD — confirm against CM5 DSI1 pin mapping at schematic phase.
* **Power:** Display power (5V_MAIN backlight, **3V3_ENIG** panel logic) via a separate 4-pin power header adjacent to J_DSI1 (TBD at schematic phase).

## 9. PCB Fabrication & Stackup

### 9.1. PCB Fabrication (JLCPCB Specs)

* **Layers:** **6-Layer** (JLC06161H-2116 stackup).
  For production runs requiring verified controlled impedance (differential pairs: USB/HDMI/GbE),
  specify JLCPCB's 'Controlled Impedance' service (TDR-verified, ±10% tolerance). Prototype orders
  may omit this per DEC-017.
* **Finish:** **ENIG (Gold)** for all pads and diagnostic loops.
* **Solder Mask:** **Dark Green** (Vintage Industrial Lacquer aesthetic).
* **Silkscreen:** White, Typewriter-style font, Bilingual (ALL-CAPS GERMAN / Sentence-case English).

### 9.2. Advanced Layer Stackup (6-Layer / 2oz) [JLCPCB JLC06161H-2116]

* **L1 (Top):** SMT Components, I2C + PWR Control GPIOs & Shielded Ground Pour.
* **L2 (Internal):** Primary GND Plane (Logic Reference).
* **L3 (Internal):** High-Speed Data Striplines (USB/HDMI/GBE).
  * 90Ω Diff: 5.5 mil width / 7.5 mil gap (USB 3.0).
  * 100Ω Diff: 4.5 mil width / 8.5 mil gap (HDMI, Ethernet).
* **L4 (Internal):** High-Current Power Plane (5V_MAIN / 3V3_ENIG).
* **L5 (Internal):** Secondary GND Plane (Shielding).
* **L6 (Bottom):** JTAG/Data Plate (Signal/Copper Pour).

### 9.3. Trace Widths & Impedance

| Net Class | Target Impedance | Width / Spacing | Layer |
| :--- | :--- | :--- | :--- |
| **USB 3.0** | 90Ω Differential | 5.5 mil / 7.5 mil | L3 (Stripline) |
| **Ethernet/HDMI** | 100Ω Differential | 4.5 mil / 8.5 mil | L3 (Stripline) |
| **JTAG signals** | 50Ω Single-ended | 5.0 mil (0.127 mm) | L6 |
| **5V_MAIN power rail** | N/A (Low Drop) | 78.7 mil (2.00 mm) min + inner pour — 8.76A worst-case; Very High Current (> 5.5A) per Global_Routing_Spec §1.1 | L1 surface + L4 inner pour |
| **Logic/I2C** | N/A | 6.0 mil | L1 |
| **USB 2.0** | 90Ω Differential | 5.5 mil / 7.5 mil | L3 (Stripline) — same geometry as USB 3.0 |
| **3V3_ENIG power** | N/A (Power) | 0.80 mm (31.5 mil) — 3.0A LDO max output; consistent with PM §9 and Global_Routing_Spec §1.1 Medium supply (1.0–3.0A); 2oz copper system-wide | L1 surface + L4 inner pour |

## 10. Thermal, Branding & Diagnostics

### 10.1. Thermal

* **LINK-ALPHA Power Entry:** The LINK-ALPHA connector carries 5V_MAIN at up to 9A. Add a **"Caution: High Current"** silkscreen label adjacent to the connector.
* **CM5 Module Thermal Management:**
  * **Heatsink:** Mount the [Raspberry Pi CM5 Cooler](https://www.raspberrypi.com/products/cm5-cooler/)
    (SC1144, passive aluminium heatsink, ~41×56×12.7mm, conductive silicone pad) directly onto the CM5 module.
    Fasten with the four corner mounting screws for secure thermal contact.
  * **Active Fan Header (J_FAN):** A 4-pin JST SH (1.0mm pitch) fan connector is provided on the Controller
    board, matching the CM5IO J14 standard. Supports 5V PWM-controlled fans.
    Board part: JST SM04B-SRSS-TB(LF)(SN) (JLCPCB C160404, Mouser 306-SM04BSRSSTBLFSN, DigiKey 455-SM04B-SRSS-TBCT-ND).
    Pinout: Pin 1 = 5V_MAIN, Pin 2 = GND, Pin 3 = TACH (CM5 Pin 16), Pin 4 = PWM (CM5 Pin 19).
    FAN_TACH and FAN_PWM are dedicated BCM2712 fan controller pins on the CM5 module connector
    — no GPIO allocation required.

### 10.2. Diagnostics & Aesthetics

* **Placement:** 2×10 2.54mm ENIG Gold Looped Probe Pad Banks placed on L1, directly behind their respective BtB connectors.
* **Orientation:** Facing upwards for easy logic analyser ribbon cable connection.
* **Silkscreen:** Dark Green mask with White Bilingual Typewriter font. Silkscreen legend must label each pad individually.
* **Branding:** Top-left 10mm "Enigma-NG" shielded gold emblem (Exposed ENIG Gold tied to GND_CHASSIS). Inverted Master Data Plate (Silhouette + JLC Serial Block) on L6 (Bottom).
  See `design/Standards/Global_Routing_Spec.md §6` for full branding specification.

#### Diagnostic Bank-Alpha (Power/Entry) — 2×10

Monitors 5V_MAIN, 3V3_ENIG, I²C Telemetry, Status LEDs, and BATT_PRES.

| Pin | Signal | Direction | Description |
| :--- | :--- | :--- | :--- |
| 1 | 5V_MAIN | PM → CTRL | 5V power rail probe point |
| 2 | 5V_MAIN | PM → CTRL | 5V power rail (redundant) |
| 3 | 3V3_ENIG | PM → CTRL | 3.3V logic rail probe point |
| 4 | 3V3_ENIG | PM → CTRL | 3.3V logic rail (redundant) |
| 5 | I2C1_SDA | Bidir | I²C Telemetry bus data |
| 6 | I2C1_SCL | Bidir | I²C Telemetry bus clock |
| 7 | ETH_LED_LINK | CTRL → PM | Ethernet link status LED |
| 8 | ETH_LED_ACT | CTRL → PM | Ethernet activity LED |
| 9 | SW_LED_G | CTRL → PM | RGB LED green channel (GPIO 18) |
| 10 | SW_LED_R | CTRL → PM | RGB LED red channel (GPIO 17) |
| 11 | SW_LED_B | CTRL → PM | RGB LED blue channel (GPIO 19) |
| 12 | PWR_GD | PM → CTRL | Power-good signal (GPIO 27) |
| 13 | BATT_PRES_N | PM → CTRL | Battery presence active-low (GPIO 23) |
| 14 | SW_LED_CTRL | CTRL → PM | LED arbitration HIGH = CM5 in control (GPIO 20) |
| 15 | SPARE | — | Reserved for future use |
| 16 | SPARE | — | Reserved for future use |
| 17 | SPARE | — | Reserved for future use |
| 18 | SPARE | — | Reserved for future use |
| 19 | GND_CHASSIS | — | Chassis ground reference |
| 20 | GND | — | Signal/power ground return |

> **Note:** RGB channel order in Bank-Alpha (pins 9/10/11 = G/R/B) differs from BtB LINK-ALPHA order (pins 31/32/33 = R/G/B). This is intentional for PCB routing
> convenience. Silkscreen legend must label each pad individually.

#### Diagnostic Bank-Beta (Logic/Exit) — 2×10

Monitors the grouped Link-Beta power rails, I²C extension, and JTAG return path after the DEC-036 rail rebalance.

| Pin | Signal | Direction | Description |
| :--- | :--- | :--- | :--- |
| 1 | 5V_MAIN_A | PM → Stator | Probe for Link-Beta pin 14 |
| 2 | 5V_MAIN_B | PM → Stator | Probe for Link-Beta pin 15 |
| 3 | 5V_MAIN_C | PM → Stator | Probe for Link-Beta pin 16 |
| 4 | 5V_MAIN_D | PM → Stator | Probe for Link-Beta pin 17 |
| 5 | 3V3_ENIG_A | PM → Stator | Probe for Link-Beta pin 19 |
| 6 | 3V3_ENIG_B | PM → Stator | Probe for Link-Beta pin 20 |
| 7 | 3V3_ENIG_C | PM → Stator | Probe for Link-Beta pin 21 |
| 8 | GND | — | Ground reference |
| 9 | I2C1_SDA | Bidir | Probe for Link-Beta pin 12 / shared Stator-Settings I²C bus |
| 10 | I2C1_SCL | Bidir | Probe for Link-Beta pin 13 / shared Stator-Settings I²C bus |
| 11 | GND_RET_A | — | Probe for grouped Link-Beta return cluster |
| 12 | GND_RET_B | — | Probe for grouped Link-Beta return cluster |
| 13 | GND_RET_C | — | Probe for grouped Link-Beta return cluster |
| 14 | GND_RET_D | — | Probe for grouped Link-Beta return cluster |
| 15 | JTAG_TCK | JDB → Stator | JTAG clock (isolated from TDI/TMS) |
| 16 | GND | — | TCK shield / clock return |
| 17 | TMS | JDB → Stator | JTAG mode select |
| 18 | TDI | JDB → Stator | JTAG data in |
| 19 | TDO | Stator → JDB | JTAG data out (TTD_RETURN) |
| 20 | GND | — | JTAG trailing shield |

## 11. Bill of Materials

| Ref | Component | Value | Package | Mouser Part # | DigiKey Part # | JLCPCB Part # |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| C1-C5 | Bulk entry decoupling bank (star/spoke) | 10uF X7R 50V | 1206 | 187-CL31B106KBHNNNE | 1276-6767-1-ND | C89632 |
| C6 | VBAT bypass cap | 100nF X7R 50V | 0402 | 187-CL05B104KB5NNNC | 1276-1009-1-ND | C1525 |
| BT1 | CR2032 coin cell holder (RTC backup) | Keystone 3034 | THT horizontal | 534-3034 | 36-3034-ND | C70377 |
| D1 | VBAT Schottky protection (blocks CR2032 charge path) | BAT54 (Diotec) | SOT-23 | 637-BAT54 | 4878-BAT54CT-ND | C25835522 |
| J1 | Link-Alpha 80-pin Socket | ERF8-040-05.0-S-DV-K-TR (female) | Samtec | 200-ERF8040050SDVKTR | SAM8621CT-ND | C3640808 |
| J2 | Link-Beta 40-pin Socket | ERF8-020-05.0-S-DV-K-TR (female) | Samtec | 200-ERF8020050SDVKTR | SAM8619CT-ND (CT) / SAM8619TR-ND (T&R) / SAM8619DKR-ND (DKR) | C6034565 |
| J3 | USB 3.0 Type-A | Dual-Stack | Molex 48406-0003 | 538-48406-0003 | WM10420-ND | C565298 |
| J4 | HDMI Type-A | Full-Size | TE 2007435-1 | 571-2007435-1 | A141617-ND | C195051 |
| J_DSI1 | DSI1 display FPC connector (15-pin 1.0mm pitch ZIF) | TBD — confirm against CM5 DSI1 pinout at schematic phase | 15-pin ZIF, 1.0mm pitch | TBD | TBD | TBD |
| J_FAN | JST SH 4-pin 1.0mm fan header | JST SM04B-SRSS-TB(LF)(SN) | SMT 1.0mm pitch | 306-SM04BSRSSTBLFSN | 455-SM04B-SRSS-TBCT-ND | C160404 |
| J_JDB_PWR | JDB hat power/USB header (female socket) | Adam Tech RS1-05-G — 1×5 2.54mm female | THT | 737-RS1-05-G | 2057-RS1-05-G-ND | C3321119 |
| J_JDB_JTAG | JDB hat JTAG header (female socket) | Adam Tech RS1-10-G — 1×10 2.54mm female | THT | 737-RS1-10-G | 2057-RS1-10-G-ND | C3320525 |
| J_CM5_A | Amphenol 100-pin B2B socket 4.0mm height (DigiKey: 609-10164227-1004A1RLFCT-ND, Mouser: 649-101642271004RLF) | 10164227-1004A1RLF | CM5 SO-DIMM | 649-101642271004RLF | 609-10164227-1004A1RLFCT-ND | C7435219 |
| J_CM5_B | Amphenol 100-pin B2B socket 4.0mm height (DigiKey: 609-10164227-1004A1RLFCT-ND, Mouser: 649-101642271004RLF) | 10164227-1004A1RLF | CM5 SO-DIMM | 649-101642271004RLF | 609-10164227-1004A1RLFCT-ND | C7435219 |
| MH1–MH4 | CM5 brass standoff M2.5 × 4.0mm SMT (Würth 9774040151R) × 4 | M2.5 × 4.0mm | SMT | 710-9774040151R | 732-7089-1-ND | C5182034 |
| R1 | Pull-up for reset | 10kΩ | 0603 | 667-ERJ-3EKF1002V | P10.0KBYCT-ND | C25804 |
| R2 | Termination for differential | 100Ω | 0603 | 667-ERJ-3EKF1000V | P100BYCT-ND | C25806 |
| R3 | PWR_GD GPIO pull-up (to 3V3_ENIG) | 10kΩ 1% | 0603 | 667-ERJ-3EKF1002V | P10.0KBYCT-ND | C25804 |
| U1 | Raspberry Pi Compute Module 5 (CM5) — 8GB RAM / 4GB eMMC minimum; CM5 Lite NOT permitted | N/A | CM5 (SO-DIMM) | various (e.g. CM5008032) | N/A — source from RPi distributors | N/A — not stocked at JLCPCB |
| U2 | USB power switch | TPS2065C | SOT-23-5 | 595-TPS2065CDBVR | 296-TPS2065CDBVRCT-ND | C123460 |
| U3 | HDMI power switch | AP2331W | SOT-23-5 | 621-AP2331W-7 | AP2331W-7DICT-ND | C123461 |
| U4 | USB/HDMI ESD | TPD4E05U06QDQARQ1 — 4-ch ESD array, ±15kV, U-DFN-10 | U-DFN-10 | 595-PD4E05U06QDQARQ1 | 296-40696-1-ND | C81353 |

### BOM Notes

Telemetry shunt specifications and Kelvin-sensing notes are detailed in §4. Protection, ESD, and bulk decoupling
capacitor placement rules are detailed in §7. Mating header assembly specifications are in §8.
