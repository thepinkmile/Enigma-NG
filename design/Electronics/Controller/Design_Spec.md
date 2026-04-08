# Controller Board (V1.0) Design Specification

**Status:** Draft
**Project:** Enigma-NG
**Author:** Izzyonstage & GitHub Copilot
**Version:** v1.0.0
**Associated Hardware Revision:** Rev A
**Last Updated:** 2026-04-05

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
* **USB-C:** 16-pin "Power Only" to maximize mechanical durability in classroom settings.
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
  * Provides: JTAG, Reset, and 3V3_ENIG to Stator.
  * **Cross-ref:** See `Stator/Design_Spec.md` and `Stator/Board_Layout.md` for explicit pin mapping and connector
    compliance. See DEC-015 for 40-pin reduction rationale and poka-yoke safety note.
* **3V3_ENIG:** The Controller is an active consumer of 3V3_ENIG — CM5 VDD_GPIO_REF and on-board peripherals are powered from this rail via the LINK-ALPHA tap node.
  Bulk X7R decoupling capacitors are required at the 3V3_ENIG tap node on the Controller (DEC-024 candidate; specific values deferred to detailed design phase).
  The 2oz copper L3 highway continues to link Alpha and Beta for the rotor stack pass-through.

### 2.1. Connectivity & Bus (on Link-Alpha)

* **High-Speed Interconnect (BtB Samtec):**
  * **Connector:** Samtec ERF8-040 (Female Socket, 80-pin, 0.8mm pitch). See DEC-007.
  * **Mating Style:** Board-to-Board vertical stack; SMT reflow. Mates with ERM8-040 (Male) on Power Module.
  * **Pin Summary:**
    * **Pins 1–20:** GbE MDI diff pairs (4 pairs + GND shields), 100Ω stripline on L3.
    * **Pins 21–24:** 5V_MAIN power entry (supplemental) + GND return.
    * **Pins 25–26:** ETH_LED_LINK / ETH_LED_ACT (active-low).
    * **Pins 27–28:** GND isolation moat.
    * **Pins 29–38:** Status/control signals (SYS_FAULT, POE_STAT, SW_LED_R/G/B, PWR_GD, I2C1, USB_STAT).
    * **Pins 39–44:** 3V3_ENIG power (6 pins × 0.5A = 3.0A capacity).
    * **Pins 45–48:** Mixed control (BATT_PRES_N, ROTOR_EN, SW_LED_CTRL, GND).
    * **Pins 49–80:** 5V_MAIN high-current entry (32 pins × 0.5A = 16A; actual ≤9A).
  * **Power Vias:** 4-via "Power Clusters" (0.3mm drill) per Samtec power pin for thermal stability.
  * **Full pin table:** See `Controller/Board_Layout.md` LINK-ALPHA section.
* **Ethernet:** 100Ω Stripline pairs on L3, shielded by L2/L5 ground planes (GbE MDI).

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
  * **Reset:** GPIO 26 (SYS_RESET_N) triggers a hardware clear on all Intel MAX II EPM240T100I5N CPLDs.

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
* **Cross-ref:** See `JTAG_Daughterboard/Design_Spec.md` for all JTAG chain architecture, FT232H module schematics, buffering, and assembly details. See DEC-016, DEC-023.

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
| **2 / 3** | **I2C1_SDA/SCL** | I2C | 3.3V | **Main Bus:** LTC3350 @ 0x09, Smart Battery @ 0x0B, STUSB4500 @ 0x28, INA219 (PM U12) @ 0x40, INA219 (Stator U2) @ 0x45. |
| **4–15** | **DATA_BUS** | Output | 3.3V | **12-bit Parallel Bus** (D0-D11) to Stator/Rotors. |
| **16** | **ROTOR_EN** | Output | 3.3V | Enable signal to Power Module 3V3_ENIG LDO for sequenced rotor stack power-up. |
| **17** | **SW_LED_R** | PWM | 3.3V | RGB switch (SW1) — Red channel. Fault / graceful shutdown indicator. |
| **18** | **SW_LED_G** | PWM | 3.3V | RGB switch (SW1) — Green channel. USB-C active power source. |
| **19** | **SW_LED_B** | PWM | 3.3V | RGB switch (SW1) — Blue channel. PoE active power source. |
| **20** | **POE_STAT** | Input | 3.3V | Active Low: PoE live — LOW when PoE power good (TPS2372-4 /PG open-drain, per DEC-003). |
| **21** | **USB_STAT** | Input | 3.3V | Active Low: 15V/5A PD Negotiated (STUSB4500). |
| **22** | **USB_FAULT** | Input | 3.3V | Active Low: USB power fault from on-board TPS2065C (local to Controller; no BtB pin required). |
| **23** | **BATT_PRES_N** | Input | 3.3V | Active Low: Battery present (via BtB pin 45; from Power Module J3 presence detect circuit R6/TPD1E10B06). |
| **24** | **SW_LED_CTRL** | Output | 3.3V | Drive HIGH when CM5 firmware is ready to control SW1 RGB LED; disables hardware LED fallback path on Power Module. Groups LED signals with GPIOs 17–19. |
| **25** | **SYS_FAULT** | Input | 3.3V | Active Low: eFuse fault interrupt from TPS25980 FAULT pin on Power Module (via BtB pin 29). Triggers OS fault handler in power monitor daemon; useful for power dashboard diagnostics even during graceful shutdown. |
| **26** | **SYS_RESET_N** | Output | 3.3V | Active Low: system-wide CPLD reset. Broadcast to all Intel MAX II EPM240T100I5N CPLDs via LINK-BETA pin 8 (Stator), Extension Ports, and Encoder Ports. On-board CPLDs (HID Encoder, Plugboard #1/#2) driven directly. |
| **27** | **PWR_GD** | Input | 3.3V | Active High: power-good signal from MCP121T-450E (4.50V threshold). HIGH = 5V_MAIN stable; deasserts on power loss, triggering graceful shutdown daemon. Arrives via Link-Alpha pin 34. |

## 7. Protection & EMI

* **External Links:** All inputs (Status) feature 10kΩ series resistors to protect CM5 pins from transient spikes.
* **Voltage:** 5V signals are strictly forbidden on: CM5 GPIO pins, I²C SDA/SCL lines, JTAG (TDI/TDO/TCK/TMS), and all logic-level signals on LINK-ALPHA.
* **ESD Protection:** [TPD12S016](https://www.ti.com) (HDMI) and [TPD4E05U06](https://www.ti.com) (USB 3.0) on Layer 1.
* **5V_MAIN Bulk Entry:** 5× 10µF X7R 50V at LINK-ALPHA 5V_MAIN entry pins per `design/Standards/Global_Routing_Spec.md §3` Bulk Entry Bank Rule.
* **3V3_ENIG Tap Decoupling:** Bulk X7R decoupling capacitors are required at the 3V3_ENIG tap node on the Controller (DEC-024 candidate; specific values deferred to detailed design
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
| 30 | POE_STAT | PM → CTRL | PoE live status (active-low, CM5 GPIO 20) |
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
| 47 | SW_LED_CTRL | CTRL → PM | LED arbitration (CM5 GPIO 24) |
| 48 | GND | — | Zone boundary separator |
| 49–80 | 5V_MAIN / GND (interleaved) | PM → CTRL | 9A delivery cluster |

### 8.2. JDB Hat Connectors

The JTAG Daughterboard mounts as a hat on the Controller via two 2.54mm headers.

#### J_JDB_PWR — Power/USB Header (1×5, 2.54mm)

* **Part:** Würth 61300511021 (Male Pin Header, 1×5, 2.54mm pitch, vertical THT).
* **Mating Part (JDB J1):** 1×5 2.54mm female IDC socket (JLCPCB C50950). See `JTAG_Daughterboard/Design_Spec.md §3`.
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

* **Part:** Würth 61301011021 (Male Pin Header, 1×10, 2.54mm pitch, vertical THT).
* **Mating Part (JDB J2):** 1×10 2.54mm female IDC socket (JLCPCB C2337). See `JTAG_Daughterboard/Design_Spec.md §3`.
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
| 7 | GND | — | TDI/RST inter-pin shield |
| 8 | SYS_RESET_N | CTRL → Stator | Active-low system reset; clears all CPLDs in stack (CM5 GPIO 26) |
| 9–11 | GND | — | JTAG trailing shield + isolation moat |
| 12–17 | ENC_IN[0:5] | CTRL → Stator | Encoder input 6-bit bus (CM5 GPIOs 4–9) |
| 18 | GND | — | ENC_IN / ENC_OUT inter-group shield |
| 19–24 | ENC_OUT[0:5] | Stator → CTRL | Encoder output 6-bit bus (CM5 GPIOs 10–15) |
| 25 | GND | — | ENC_OUT / TTD_RETURN shield |
| 26 | TTD_RETURN | Stator → CTRL | JTAG TDO short-path return (bypasses rotor stack) |
| 27 | GND | — | TTD_RETURN shield |
| 28–35 | 3V3_ENIG | PM → Stator | Power pass-through (8 pins = 4.0A; 2oz copper highway) |
| 36–40 | GND | — | Power return |

### 8.4. Fan Connector (J_FAN)

* **Part:** JST SM04B-SRSS-TB(LF)(SN) — 4-pin JST SH 1.0mm pitch right-angle header
* **Mating Part:** JST SHR-04V-S (female crimp housing)
* **JLCPCB:** C160390 | **Mouser:** 538-SM04B-SRSS-TB
* **Pinout:**

| Pin | Signal | Source |
| --- | ------ | ------ |
| 1 | 5V_MAIN | Controller 5V_MAIN rail |
| 2 | GND | Controller GND |
| 3 | FAN_TACH | CM5 module connector Pin 16 |
| 4 | FAN_PWM | CM5 module connector Pin 19 |

* FAN_TACH and FAN_PWM connect directly from the CM5 module DF40 connector (dedicated BCM2712 fan controller interface). No GPIO allocation required.
* Mating fan cable: JST SHR-04V-S housing with 4× JST SSH-003T-P0.2 crimp terminals.

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
* **L6 (Bottom):** Diagnostic Bank, Enigma 12-bit Data Bus, JTAG & Global Data Plate.

### 9.3. Trace Widths & Impedance

| Net Class | Target Impedance | Width / Spacing | Layer |
| :--- | :--- | :--- | :--- |
| **USB 3.0** | 90Ω Differential | 5.5 mil / 7.5 mil | L3 (Stripline) |
| **Ethernet/HDMI** | 100Ω Differential | 4.5 mil / 8.5 mil | L3 (Stripline) |
| **JTAG signals** | 50Ω Single-ended | 5.0 mil (0.127 mm) | L6 |
| **5V_MAIN power rail** | N/A (Low Drop) | 78.7 mil (2.00 mm) min + inner pour — 9.05A worst-case; Very High Current (> 5.5A) per Global_Routing_Spec §1.1 | L1 surface + L4 inner pour |
| **Logic/I2C** | N/A | 6.0 mil | L4 / L6 |
| **USB 2.0** | 90Ω Differential | 5.5 mil / 7.5 mil | L3 (Stripline) — same geometry as USB 3.0 |
| **3V3_ENIG power** | N/A (Power) | 0.80 mm (31.5 mil) — 3.0A LDO max output; consistent with PM §9 and Global_Routing_Spec §1.1 Medium supply (1.0–3.0A); 2oz copper system-wide | L1/L6 or L4 Power Plane |

## 10. Thermal, Branding & Diagnostics

### 10.1. Thermal

* **LINK-ALPHA Power Entry:** The LINK-ALPHA connector carries 5V_MAIN at up to 9A. Add a **"Caution: High Current"** silkscreen label adjacent to the connector.
* **CM5 Module Thermal Management:**
  * **Heatsink:** Mount the [Raspberry Pi CM5 Cooler](https://www.raspberrypi.com/products/cm5-cooler/)
    (SC1144, passive aluminium heatsink, ~41×56×12.7mm, conductive silicone pad) directly onto the CM5 module.
    Fasten with the four corner mounting screws for secure thermal contact.
  * **Active Fan Header (J_FAN):** A 4-pin JST SH (1.0mm pitch) fan connector is provided on the Controller
    board, matching the CM5IO J14 standard. Supports 5V PWM-controlled fans.
    Board part: JST SM04B-SRSS-TB(LF)(SN) (JLCPCB C160390, Mouser 538-SM04B-SRSS-TB).
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
| 14 | SW_LED_CTRL | CTRL → PM | LED arbitration HIGH = CM5 in control (GPIO 24) |
| 15 | SPARE | — | Reserved for future use |
| 16 | SPARE | — | Reserved for future use |
| 17 | SPARE | — | Reserved for future use |
| 18 | SPARE | — | Reserved for future use |
| 19 | GND_CHASSIS | — | Chassis ground reference |
| 20 | GND | — | Signal/power ground return |

> **Note:** RGB channel order in Bank-Alpha (pins 9/10/11 = G/R/B) differs from BtB LINK-ALPHA order (pins 31/32/33 = R/G/B). This is intentional for PCB routing
> convenience. Silkscreen legend must label each pad individually.

#### Diagnostic Bank-Beta (Logic/Exit) — 2×10

Monitors 12-bit Sniffer bus (ENC_IN/ENC_OUT), SYS_RESET_N, and JTAG signals.

| Pin | Signal | Direction | Description |
| :--- | :--- | :--- | :--- |
| 1 | ENC_IN[0] | CTRL → Stator | Encoder input bit 0 |
| 2 | ENC_IN[1] | CTRL → Stator | Encoder input bit 1 |
| 3 | ENC_IN[2] | CTRL → Stator | Encoder input bit 2 |
| 4 | ENC_IN[3] | CTRL → Stator | Encoder input bit 3 |
| 5 | ENC_IN[4] | CTRL → Stator | Encoder input bit 4 |
| 6 | ENC_IN[5] | CTRL → Stator | Encoder input bit 5 |
| 7 | SYS_RESET_N | CTRL → Stator | Active-low system reset (GPIO 26) |
| 8 | GND | — | Ground reference |
| 9 | ENC_OUT[0] | Stator → CTRL | Encoder output bit 0 |
| 10 | ENC_OUT[1] | Stator → CTRL | Encoder output bit 1 |
| 11 | ENC_OUT[2] | Stator → CTRL | Encoder output bit 2 |
| 12 | ENC_OUT[3] | Stator → CTRL | Encoder output bit 3 |
| 13 | ENC_OUT[4] | Stator → CTRL | Encoder output bit 4 |
| 14 | ENC_OUT[5] | Stator → CTRL | Encoder output bit 5 |
| 15 | JTAG_TCK | JDB → Stator | JTAG clock (isolated from TDI/TMS) |
| 16 | GND | — | TCK shield / clock return |
| 17 | TMS | JDB → Stator | JTAG mode select |
| 18 | TDI | JDB → Stator | JTAG data in |
| 19 | TDO | Stator → JDB | JTAG data out (TTD_RETURN) |
| 20 | GND | — | JTAG trailing shield |

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
| J_FAN | JST SH 4-pin 1.0mm fan header | JST SM04B-SRSS-TB(LF)(SN) | SMT 1.0mm pitch | 538-SM04B-SRSS-TB | N/A | C160390 |
| J_CM5_A | Amphenol 100-pin B2B socket 4.0mm height (DigiKey: 609-10164227-1004A1RLFCT-ND, Mouser: 649-101642271004RLF) | 10164227-1004A1RLF | CM5 SO-DIMM | 649-101642271004RLF | 609-10164227-1004A1RLFCT-ND | C7435219 |
| J_CM5_B | Amphenol 100-pin B2B socket 4.0mm height (DigiKey: 609-10164227-1004A1RLFCT-ND, Mouser: 649-101642271004RLF) | 10164227-1004A1RLF | CM5 SO-DIMM | 649-101642271004RLF | 609-10164227-1004A1RLFCT-ND | C7435219 |
| MH1–MH4 | CM5 brass standoff M2.5 × 4.0mm SMT (Würth 9774040151R) × 4 | M2.5 × 4.0mm | SMT | 710-9774040151R | 732-7089-1-ND | C5182034 |
| R1 | Pull-up for reset | 10kΩ | 0603 | 667-ERJ-3EKF1002V | P10.0KBYCT-ND | C25804 |
| R2 | Termination for differential | 100Ω | 0603 | 667-ERJ-3EKF1000V | P100BYCT-ND | C25806 |
| R3 | PWR_GD GPIO pull-up (to 3V3_ENIG) | 10kΩ 1% | 0603 | 667-ERJ-3EKF1002V | P10.0KBYCT-ND | C25804 |
| U1 | Raspberry Pi Compute Module 5 (CM5) — 8GB RAM / 4GB eMMC minimum; CM5 Lite NOT permitted | N/A | CM5 (SO-DIMM) | various (e.g. CM5008032) | N/A — source from RPi distributors | N/A — not stocked at JLCPCB |
| U2 | USB power switch | TPS2065C | SOIC-8 | 595-TPS2065CDBVR | 296-TPS2065CDBVRCT-ND | C123460 |
| U3 | HDMI power switch | AP2331W | SOT-23 | 621-AP2331W-7 | AP2331W-7DICT-ND | C123461 |
| U4 | USB/HDMI ESD | TPD4E05U06 | VQFN | 595-TPD4E05U06DBVR | 296-TPD4E05U06DBVRCT-ND | C123462 |

### BOM Notes

Telemetry shunt specifications and Kelvin-sensing notes are detailed in §4. Protection, ESD, and bulk decoupling
capacitor placement rules are detailed in §7. Mating header assembly specifications are in §8.
