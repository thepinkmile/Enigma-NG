# Controller Board (V1.0) Design Specification

**Status:** Draft
**Project:** Enigma-NG
**Author:** Izzyonstage & GitHub Copilot
**Version:** v1.0.0
**Associated Hardware Revision:** Rev A
**Last Updated:** 2026-04-25

---

## 1. Overview

The Controller Board is a custom carrier board for the Raspberry Pi Compute Module 5 (CM5), providing the
central processing and supervisory function for the Enigma-NG system. It is the fixed mechanical
motherboard of the enclosure: the removable Power Module and Stator daughtercards both dock into the
Controller, and all enclosure-edge I/O is grouped on the Controller side.

* **Module:** Raspberry Pi Compute Module 5 (CM5).
* **Role:** Master traffic controller for power, external I/O, and encryption logic.
* **Stackup:** 6-Layer / 2oz Finished Copper (JLC06161H-2116) for 5Gbps differential pair integrity.
* **Shielding:** High-speed signals (Ethernet, USB 3.0, HDMI) routed as Striplines on L3, shielded by L2/L5 GND planes
  and L4 (Internal) for High-Current Power Plane (5V_MAIN / 3V3_ENIG).
* **RJ45 / PoE:** Ethernet entry, magnetics, ESD, and the PoE front-end are hosted locally on the Controller.
  The PoE front-end delivers its regulated auxiliary output to the Power Module over `J2`.
* **Power from PM:** The Controller receives `5V_MAIN` and `3V3_ENIG` from the Power Module over `J1`.
* **Status LED:** The Controller can override the PM status LED with full-colour control via the I2C connection over `J3`.

### GND_CHASSIS Single-Point Bond

Per `design/Standards/Global_Routing_Spec.md §5`, the Controller implements a local
`GND_CHASSIS` net tied to its mounting hardware, connector-shield / EMI landing features, and any
other deliberate enclosure-contact points, but it does **not** implement a local
GND-to-GND_CHASSIS bond. The system's only galvanic GND ↔ GND_CHASSIS bond remains on the Power
Module at the common power-entry point immediately before the eFuse, regardless of which input
source is active.

### Functional & Design Requirements

#### Functional Requirements

| ID | Functional Requirement | Notes | Satisfied By / Cross-Ref |
| :--- | :--- | :--- | :--- |
| FR-CTL-01 | Host the Raspberry Pi Compute Module 5 as the system master processor | CM5 runs the Linux OS and all application logic | BOM U1 (CM5) |
| FR-CTL-02 | Receive regulated rails from the Power Module and distribute them to the CM5, Stator, and local peripherals | Via PM dock `J1` and Stator docks `J4/J5` | §2 Dock Interfaces; BOM J1–J3, J4/J5 |
| FR-CTL-03 | Provide the system's enclosure-edge external I/O interfaces | GbE / PoE entry, HDMI, USB 3.0 | §8 Connectivity; BOM J6, J7, J8 |
| FR-CTL-04 | Provide JTAG programming capability for all 37 CPLDs in the system | Via JTAG Daughterboard and the `J5` Stator logic dock | §3 JTAG Programming Subsystem; BOM J4, J5 |
| FR-CTL-05 | Monitor system power and PM status via I²C, with only essential direct PM handshakes kept as dedicated pins | Telemetry: LTC3350 @ 0x09, STUSB4500 @ 0x28, PCA9534A @ 0x3F, INA219 ×2 (PM U12 @ 0x40; Stator U2 @ 0x45); Direct handshakes: `PWR_GD`, `ROTOR_EN`, `PWR_BUT`, `LED_nPWR` | §4 Telemetry & Logic; §6 CM5 GPIO Mapping Matrix |
| FR-CTL-06 | Maintain RTC operation across power cycles using a CR2032 backup battery | Non-rechargeable; service by disassembly | §5 RTC Backup Battery; BOM BT1, D1 (BAT54) |
| FR-CTL-07 | Route power, JTAG, and I²C between the Controller and the Stator board | Via `J4/J5` hybrid docks | §2 Dock Interfaces; BOM J4/J5 |
| FR-CTL-08 | Provide DSI1 display interface connector for optional lid-mounted touchscreen add-on | DSI1 4-lane FPC connector (J9) on Controller Board; display add-on board to be designed separately | §8 Connectivity; BOM J9 |
| FR-CTL-09 | Provide the local servo actuation electrical interface and home sensing for the rotor depression bar | Direct CM5 GPIO on the Controller provides local PWM output and home-switch input; no expander-owned servo path | §6 CM5 GPIO Mapping Matrix; §8 Connectivity; BOM J11, SW3, R4, C12 |

#### Design Requirements

| ID | Design Requirement | Specification | Satisfied By / Cross-Ref |
| :--- | :--- | :--- | :--- |
| DR-CTL-01 | PCB stackup | 6-layer, 2oz finished copper (JLC06161H-2116) | §9 PCB Fabrication & Stackup |
| DR-CTL-02 | CM5 module | Raspberry Pi Compute Module 5 (SO-DIMM form factor). Multiple current CM5 variants are acceptable. Minimum spec: 4 GB RAM and 8 GB eMMC; on-board Wi-Fi may be fitted or omitted. CM5 Lite (no onboard eMMC) is NOT permitted. BOM reference: various CM5 SKUs. | BOM U1 |
| DR-CTL-03 | Controller-to-Power-Module dock connectors | `J1/J2/J3` = TE `1-1674231-1` 10-position 2.5mm receptacles | BOM J1–J3 |
| DR-CTL-04 | Controller-to-Stator dock connectors | `J4/J5` = Molex `2195630015` hybrid receptacles (5 power + 15 signal) | BOM J4, J5 |
| DR-CTL-05 | USB current limit | 1.6 A via TPS2065C; fault output to GPIO 6 (USB_FAULT) | BOM U2 (TPS2065C); §6 GPIO Mapping (GPIO 6) |
| DR-CTL-06 | RTC battery holder | BT1 = Keystone 3034TR (THT horizontal CR2032 holder; `TR` = tape-reel packaging) | §5 RTC Backup Battery; BOM BT1 (Keystone 3034TR) |
| DR-CTL-07 | RTC protection | D1 = BAT54 Schottky diode (blocks PMIC VBAT charge path) | §5 RTC Backup Battery; BOM D1 (BAT54) |
| DR-CTL-08 | RTC bypass capacitor | C6 = 100 nF 0402 on CM5 VBAT (Pin 76, Hirose DF40 200-pin) | §5 RTC Backup Battery; BOM C6 |
| DR-CTL-09 | PM status / SW1 LED interface | Controller must expose the shared `I2C-1` bus plus one optional interrupt input (`PM_IO_INT_N`) to the PM-local `PCA9534A @ 0x3F`, which virtualises `POE_STAT`, `USB_STAT`, `BATT_PRES_N`, `SYS_FAULT`, and runtime `SW_LED_R/G/B + SW_LED_CTRL`. | §4.1 I²C Bus Topology; §6 CM5 GPIO Mapping Matrix |
| DR-CTL-10 | OS/firmware configuration | All firmware configuration requirements (including RTC charging disable) are specified in the Linux OS design spec. See `design/Software/Linux_OS/`. | design/Software/Linux_OS/ |
| DR-CTL-11 | DSI1 connector | J9 = Amphenol F52Q-1A7H1-11015, 15-pin 1.0mm pitch right-angle ZIF/FPC connector; DSI1 4-lane: CLK+/−, D0+/−, D1+/−, D2+/−, D3+/− = 10 differential signals; 100 Ω differential impedance; route on L3 (stripline, same as HDMI); capacitive touch I²C may share the existing I²C-1 controller interface when the deferred display add-on is defined | §8 Connectivity; BOM J9 |
| DR-CTL-12 | Servo connector | J11 = 3-pin JST PH 2.0mm connector; pins: `5V_MAIN`, `GND`, `SERVO_PWM`; mounted on the Controller adjacent to the rotor actuation linkage | §8 Connectivity; BOM J11 |
| DR-CTL-13 | SERVO_HOME switch | SW3 = SPST normally-open momentary; active-low; 10kΩ pull-up to `3V3_ENIG` + 100nF X7R debounce cap to GND (RC τ = 1ms); connected directly to a CM5 GPIO on the Controller | §6 CM5 GPIO Mapping Matrix; §8 Connectivity; BOM SW3, R4, C12 |
| DR-CTL-14 | Direct servo GPIO usage | `SERVO_PWM` uses PWM-capable CM5 GPIO 12; `SERVO_HOME` uses direct CM5 GPIO 17 input. No I²C expander or external PWM driver is used for the servo path. | §6 CM5 GPIO Mapping Matrix |

## 2. Dock Interfaces

The Controller is the fixed motherboard of the enclosure and carries both removable-board docks.

### 2.1. Controller ↔ Power Module Dock

The Controller connects to the Power Module through the `J1` / `J2` / `J3` TE dock set.
See §8.1 for the connector family, link allocations, reference PDFs, and the `J2`
current-sharing rationale.

### 2.2. Controller ↔ Stator Dock

The Controller connects to the Stator through the `J4` / `J5` Molex hybrid dock pair.
See §8.2 for the connector family, link allocations, reference PDFs, and the `J5`
logic-domain grouping rationale.

### 2.3. CM5 Module Under-Body Placement Envelope

The area directly beneath the mounted CM5 module (55mm × 40mm footprint) shall observe a
**height-limited placement envelope** rather than a total component keep-out:

* Low-profile **passive components only** may be placed within the CM5 shadow area.
* Maximum installed component height beneath the CM5: **2.0mm** above the Controller PCB surface.
* Active components, connectors, test points, tall features, and exposed via pads are prohibited within
  this area.
* Copper fills, signal routing, and power planes are permitted beneath the module.
* The mechanical envelope beneath the CM5 remains **2.5mm** using Amphenol `10164227-1004A1RLF`
  (4.0mm stack height). The 2.0mm component-height rule preserves ~0.5mm assembly margin within that
  official clearance.
* The CM5 footprint shadow should still be shown in KiCad on `User.Courtyard`, but as a placement
  reference boundary for the height rule rather than as a hard no-component keep-out.

### 2.4. Physical Connector Placement

1. **Top Edge:** Order from Left to Right
    * **Stator Dock:** `J4` + `J5` Molex hybrid connectors to the removable Stator daughterboard.
    * **PM Dock:** `J1` + `J2` + `J3` TE 10-position connectors to the removable Power Module.
2. **Right Edge:** Order from Top to Bottom to follow CM5 pinout flow:
    * **RJ45 / PoE Entry:** Long-body magnetics jack. The PoE front-end is local to the Controller.
    * **USB 3.0:** Dual-Stacked Type-A (Molex 48406-0003).
    * **HDMI:** Full-Size Type-A (TE 2007435-1).

**Right-edge support circuitry note:** The USB and HDMI current-limit switches, the edge-I/O ESD
protection network, and the `USB_FAULT` telemetry path are all local support circuitry for these
interfaces, but they are not enclosure-protruding connectors and do not define the external connector
order.

**External-face note:** Controller right-edge external connectors follow the global **2.0mm nominal
overhang** rule defined in `design/Standards/Global_Routing_Spec.md §4.1`.

## 3. JTAG Programming Subsystem (USB Blaster)

The Controller provides JTAG pass-through only. All JTAG chain architecture, device ordering, buffering, termination, and timing specifications are defined in the JDB Design_Spec.

* **Controller Pass-Through:** JTAG lines (TCK, TMS, TDI, TTD_RETURN, VREF) are routed directly
  from the JDB hat-headers (`J12`/`J13`) to the Stator logic dock (`J5`) on the Controller board without any active
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

All I²C devices share the single I²C-1 bus (CM5 GPIO 2/3) routed to the Power Module over `J3` and to
the Stator over `J5`.

| Address | Device | Location | Function |
| :--- | :--- | :--- | :--- |
| 0x09 | LTC3350 | Power Module | Supercap charger/monitor |
| 0x0B | Smart Battery | Power Module | SMBus battery monitoring |
| 0x20 | MCP23017 (U6) | Stator | ENC_IN/ENC_OUT monitoring (16 GPIO) |
| 0x21 | MCP23017 (U7) | Stator | Virtual keypress injection, SOURCE_SEL, SYS_RESET_N, spare GPIO |
| 0x22 | MCP23017 (U8) | Stator | CPLD config output driver (DEC-032) |
| 0x23 | MCP23017 (U1) | Settings Board | Switch input reader (DEC-032) |
| 0x24 | MCP23017 (U2) | Settings Board | Bank 1 LED controller: 5× anodes + RGB bank-rail drivers (DEC-034) |
| 0x25 | MCP23017 (U3) | Settings Board | Bank 2 LED controller: 7× anodes + RGB bank-rail drivers (DEC-034) |
| 0x28 | STUSB4500 | Power Module | USB-C PD controller |
| 0x3F | PCA9534A (U16) | Power Module | PM-local status inputs + SW1 RGB handoff control |
| 0x40 | INA219 (U12) | Power Module | 5V_MAIN current/power telemetry |
| 0x45 | INA219 (U2) | Stator | Rotor stack current/power telemetry |

## 5. RTC Backup Battery

The CM5's MXL7704 PMIC contains an integrated RTC. To maintain timekeeping through power cycles,
a 3V coin cell is required on the CM5's VBAT pin (**Pin 76** on the CM5 Hirose DF40 200-pin connector).

### 5.1. Circuit Design

* **Battery (BT1):** Keystone 3034TR CR2032 THT horizontal click-in holder (`TR` = tape-reel packaging). CR2032 = 3.0V, 220mAh.
  Estimated service life >25 years at <1µA RTC quiescent draw.
* **Protection Diode (D1):** BAT54 Schottky diode (SOT-23, 30V, 200mA).
  Connected in series: BT1(+) → D1(anode), D1(cathode) → CM5 VBAT (Pin 76). Vf ≈ 0.3V @ 100µA; delivers
  ~2.7V to VBAT pin (within MXL7704 VBAT operating range). **This diode is mandatory with a CR2032 —
  it physically prevents the PMIC charging circuit from reaching the battery.**
* **Bypass Cap (C6):** 100nF X7R 0402 (Samsung CL05B104KB5NNNC) from VBAT to GND, placed within 5mm
  of the CM5 DF40 connector Pin 76.

> ⚠️ **Do NOT substitute ML2032 for CR2032 without removing D1.** The ML2032 is rechargeable and
> must connect directly to VBAT (no diode). The software charging-disable note in
> `Software/Linux_OS/Power_Management.md` also applies.
>
### 5.2. Placement

* **BT1:** Left edge of board, minimum 20mm from any high-speed trace (GbE pairs, USB 3.0, HDMI).
  Orient so the battery ejects away from the board centre for service access.
* **Battery replacement:** Classified as a **service-by-disassembly** task — not field-replaceable in-situ.
  Expected interval: >25 years under normal use. See `design/Guides/Maintenance_Guide.md`.

## 6. CM5 GPIO Mapping Matrix (Enigma-NG)

All GPIOs are referenced to **3V3_ENIG**. BCM2712 silicon limit: 50mA aggregate per GPIO bank.

> **CM5 VDD_GPIO_REF:** The CM5 module VDD_GPIO_REF pin on the Hirose DF40 200-pin module connector
> must be connected to **3V3_ENIG** (not to the CM5-internal `CM5 3V3` rail, which is not used as a
> logic reference on this board). This ensures GPIO logic levels match all 3V3_ENIG-powered peripherals
> (CPLDs, FT232H VCCIO, etc.). Failure to connect VDD_GPIO_REF to 3V3_ENIG will result in incorrect
> GPIO logic levels for the entire system.

| GPIO | Function | Type | Logic Level | Description |
| :--- | :--- | :--- | :--- | :--- |
| **2 / 3** | **I2C1_SDA/SCL** | I2C | 3.3V | System I2C-1 shared with the devices listed in §4.1. |
| **4** | **ROTOR_EN** | Output | 3.3V | Direct enable signal to the Power Module `3V3_ENIG` LDO for sequenced rotor-stack power-up. Routed on `J3`. |
| **5** | **PM_IO_INT_N** | Input | 3.3V | Optional interrupt input from the PM-local `PCA9534A @ 0x3F`, used to wake the power-management daemon for PM status changes. |
| **6** | **USB_FAULT** | Input | 3.3V | Active Low: USB power fault from on-board TPS2065C (local to Controller; no BtB pin required). |
| **7** | **PWR_GD** | Input | 3.3V | Direct PM rail-health telemetry only — HIGH while `5V_MAIN` ≥ 4.50V; does NOT trigger shutdown. Routed on `J3`. |
| **12** | **SERVO_PWM** | Output (PWM) | 3.3V | Direct Controller-local servo PWM output. Configure for 50Hz pulse generation during actuation cycles. |
| **17** | **SERVO_HOME** | Input | 3.3V | Active-low Controller-local servo home switch input with local pull-up and RC debounce. |

## 7. Protection & EMI

* **External Links:** All inputs (Status) feature 10kΩ series resistors to protect CM5 pins from transient spikes.
* **Voltage:** 5V signals are strictly forbidden on: CM5 GPIO pins, I²C SDA/SCL lines, JTAG (TDI/TDO/TCK/TMS), and all low-speed PM / Stator dock signals.
* **ESD Protection:** [TPD4E05U06](https://www.ti.com) (U4 — USB/HDMI ESD arrays) on Layer 1.
* **5V_MAIN Bulk Entry:** 5× 10µF X7R 50V at the `J1` `5V_MAIN` entry region per `design/Standards/Global_Routing_Spec.md §3` Bulk Entry Bank Rule.
* **3V3_ENIG Tap Decoupling:** The `J1` `3V3_ENIG` entry on the Controller shall follow the
  global bulk-entry bank rule: **5× 10uF X7R 50V** placed at the tap node in a
  **symmetrical star/spoke pattern** per `design/Standards/Global_Routing_Spec.md §3`.
  This applies because `3V3_ENIG` is the Controller's canonical logic rail; the
  CM5-local `CM5 3V3` rail is not used as the board logic reference.

## 8. Connectivity

### 8.1. Controller ↔ Power Module Dock

The Power Module dock uses three copies of the TE 10-position 2.5 mm connector family:

* **Controller side:** `1-1674231-1`
* **Power Module side:** `1123684-7`

**Reference PDFs:** [`TE-1-1674231-1-datasheet.pdf`](../../Datasheets/TE-1-1674231-1-datasheet.pdf),
[`TE-1123684-7-datasheet.pdf`](../../Datasheets/TE-1123684-7-datasheet.pdf)

| Link | Allocation | Description |
| :--- | :--- | :--- |
| `J1` | `3 × 5V_MAIN`, `2 × 3V3_ENIG`, `5 × GND` | Main regulated rails from PM to Controller |
| `J2` | `3 × VIN_POE_12V`, `7 × GND` | Regulated PoE-derived auxiliary feed from Controller PoE front-end into PM OR-ing stage |
| `J3` | `I2C1_SDA`, `I2C1_SCL`, `PM_IO_INT_N`, `PWR_GD`, `ROTOR_EN`, `PWR_BUT`, `LED_nPWR`, `3 × GND` | Low-speed control / telemetry connector |

`5V_MAIN` and `3V3_ENIG` both enter the Controller on `J1`. The Controller then distributes those rails
to the CM5, local peripherals, and the Stator docks.

`J2` intentionally uses only three positive `VIN_POE_12V` contacts because the TE dock family is rated
at 6 A/contact and the regulated PoE auxiliary feed is a 60 W / 12 V class source (~5 A worst case).
The positive side is therefore already heavily overprovisioned, while the additional ground contacts
reduce return impedance and spread the shared current path into the PM OR-ing stage.

### 8.2. Controller ↔ Stator Dock

The Stator dock uses the Molex EXTreme Guardian HD hybrid pair:

* **Controller side:** `2195630015` receptacle
* **Stator side:** `2195620015` plug

**Reference PDFs:** [`Molex-2195630015-datasheet.pdf`](../../Datasheets/Molex-2195630015-datasheet.pdf),
[`Molex-2195630015-drawings.pdf`](../../Datasheets/Molex-2195630015-drawings.pdf),
[`Molex-2195620015-datasheet.pdf`](../../Datasheets/Molex-2195620015-datasheet.pdf),
[`Molex-2195620015-drawings.pdf`](../../Datasheets/Molex-2195620015-drawings.pdf),
[`Molex-ExtremeGuardianHD-2141130000-PS-000-specification.pdf`](../../Datasheets/Molex-ExtremeGuardianHD-2141130000-PS-000-specification.pdf)

| Link | Allocation | Description |
| :--- | :--- | :--- |
| `J4` | `4 × 5V_MAIN` blades, `1 × GND` blade, signal field = `GND` returns / guards | 5V-biased dock |
| `J5` | `4 × 3V3_ENIG` blades, `1 × GND` blade, guarded `TCK`, `TMS`, `TDI`, `TTD_RETURN`, `I2C1_SDA`, `I2C1_SCL`, remaining signal contacts = `GND` | 3V3 / logic dock |

The `J5` connector deliberately groups the JTAG cluster and `TTD_RETURN` with the logic-domain `3V3_ENIG` feed.

### 8.3. JDB Hat Connectors

The JTAG Daughterboard mounts as a hat on the Controller via two 2.54mm headers.

#### J12 — Power/USB Header (1×5, 2.54mm)

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

#### J13 — JTAG Output Header (1×10, 2.54mm)

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

### 8.4. Fan Connector (J10)

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

### 8.5. DSI1 Display Connector (J9)

* **DSI1 Display (J9):** Amphenol **F52Q-1A7H1-11015** 15-pin 1.0mm pitch ZIF/FPC connector.
  Breaks out DSI1
  4-lane interface from CM5 for optional lid-mounted touchscreen add-on. Display add-on board
  design is deferred (see DEC-033). Connector placed near CM5 mezzanine socket on L1.
  Touch I²C routed on I²C-1 bus shared with other Stator/Controller peripherals.
* **Interface:** MIPI DSI1 — 4-lane differential (CLK+/−, D0+/−, D1+/−, D2+/−, D3+/−).
* **Impedance:** 100 Ω differential; route on L3 (stripline) — same rule as HDMI/Ethernet.
* **MPN:** Amphenol **F52Q-1A7H1-11015**. See `Consolidated_BOM.md` and
  `design/Datasheets/amphenol_ffc_fpc_100mm_f52q_f52r-datasheet.pdf`.
* **Power / deferred scope boundary:** `J9` is the only Controller-side display connector fixed in
  the current design scope. No separate display power header is defined on the Controller at this
  stage; any future display power and touch-side auxiliary wiring stays deferred with the display
  add-on definition.

### 8.6. Servo Connector (J11)

* **Part:** JST B3B-PH-K-S(LF)(SN) — 3-pin JST PH 2.0mm through-hole header.
* **Pinout:** `5V_MAIN`, `GND`, `SERVO_PWM`.
* **Control path:** `SERVO_PWM` is driven directly from CM5 GPIO 12 on the Controller. No external I²C
  PWM device is used.
* **Placement intent:** Adjacent to the local rotor actuation linkage so the servo body and cable stay
  close to the depression bar mechanism.

### 8.7. SERVO_HOME Switch (SW3)

* **Part:** Omron SS-01GL13 — SPST normally-open momentary switch.
* **Electrical interface:** Active-low to CM5 GPIO 17 with local **R4 = 10kΩ** pull-up to `3V3_ENIG`
  and **C12 = 100nF X7R** debounce capacitor to GND.
* **Role:** Detects the 0° reference position of the Controller-mounted servo actuation assembly.

## 9. PCB Fabrication & Stackup

### 9.1. PCB Fabrication (JLCPCB Specs)

* **Layers:** **6-Layer** (JLC06161H-2116 stackup).
  For production runs requiring verified controlled impedance (differential pairs: USB/HDMI/GbE),
  specify JLCPCB's 'Controlled Impedance' service (TDR-verified, ±10% tolerance). Prototype orders
  may omit this per DEC-017.
* **Finish:** **ENIG (Gold)** for all pads.
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
| **3V3_ENIG power** | N/A (Power) | 0.80 mm (31.5 mil) — 3.0A LDO max output; consistent with PM §9 and Global_Routing_Spec §1.1 Medium supply (1.0–3.0A); 2oz copper system-wide | L1 surface + L4 inner pour |
| **5V_MAIN power rail** | N/A (Low Drop) | 78.7 mil (2.00 mm) min + inner pour — 8.76A worst-case; Very High Current (> 5.5A) per Global_Routing_Spec §1.1 | L1 surface + L4 inner pour |
| **Ethernet/HDMI** | 100Ω Differential | 4.5 mil / 8.5 mil | L3 (Stripline) |
| **JTAG signals** | 50Ω Single-ended | 5.0 mil (0.127 mm) | L6 |
| **Logic/I2C** | N/A | 6.0 mil | L1 |
| **USB 2.0** | 90Ω Differential | 5.5 mil / 7.5 mil | L3 (Stripline) |
| **USB 3.0** | 90Ω Differential | 5.5 mil / 7.5 mil | L3 (Stripline) |

## 10. Thermal & Branding

### 10.1. Thermal

Estimated Controller-local power dissipation at system peak load:

| Component | Normal Dissipation | Worst Case | Notes |
| :--- | :--- | :--- | :--- |
| U9 TPS2372-4 + U10 TPS23730 + T2 POE600F-12L | ~5.1W | ~5.7W | Controller-owned PoE front-end. Loss is dominated by the PoE ACF stage / transformer path at ~51-57W PoE load; see `Electronics/Investigations/PoE_Investigation.md §3.5`. |
| **Total** | **~5.1W** | **~5.7W** | Fixed Controller-local dissipation only; excludes the CM5 SOM and any optional fan load because those depend on the fitted module SKU and runtime workload. |

* **PM Dock Power Entry:** `J1` carries the grouped regulated rail entry for the Controller. Add a **"Caution: High Current"** silkscreen label adjacent to the PM dock cluster.
* **CM5 Module Thermal Management:**
  * **Heatsink:** Mount the [Raspberry Pi CM5 Cooler](https://www.raspberrypi.com/products/cm5-cooler/)
    (SC1144, passive aluminium heatsink, ~41×56×12.7mm, conductive silicone pad) directly onto the CM5 module.
    Fasten with the four corner mounting screws for secure thermal contact.
  * **Active Fan Header (J10):** A 4-pin JST SH (1.0mm pitch) fan connector is provided on the Controller
    board, matching the CM5IO J14 standard. Supports 5V PWM-controlled fans.
    See §8.4 for the connector pinout and mating-cable definition. FAN_TACH and FAN_PWM connect
    directly to the dedicated BCM2712 fan-controller pins on the CM5 module connector — no GPIO
    allocation required.

### 10.2. Aesthetics

* **Silkscreen:** Dark Green mask with White Bilingual Typewriter font. Silkscreen legend must label each pad individually.
* **Branding:** Top-left 10mm "Enigma-NG" shielded gold emblem (Exposed ENIG Gold tied to GND_CHASSIS). Inverted Master Data Plate (Silhouette + JLC Serial Block) on L6 (Bottom).
  See `design/Standards/Global_Routing_Spec.md §6` for full branding specification.

## 11. Bill of Materials

| Ref | Component | Value | Package | Mouser Part # | DigiKey Part # | JLCPCB Part # |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| C1-C5 | `5V_MAIN` bulk entry decoupling bank (star/spoke) | 10uF X7R 50V | 1206 | 187-CL31B106KBHNNNE | 1276-6767-1-ND | C89632 |
| C6 | VBAT bypass cap | 100nF X7R 50V | 0402 | 187-CL05B104KB5NNNC | 1276-1009-1-ND | C1525 |
| C7-C11 | `3V3_ENIG` bulk entry decoupling bank (star/spoke) | 10uF X7R 50V | 1206 | 187-CL31B106KBHNNNE | 1276-6767-1-ND | C89632 |
| C12 | SERVO_HOME RC debounce capacitor | 100nF 50V X7R 0402 | 0402 | 187-CL05B104KB5NNNC | 1276-1009-1-ND | C1525 |
| BT1 | CR2032 coin cell holder (RTC backup) | Keystone 3034TR | THT horizontal | 534-3034TR | 36-3034CT-ND | C5213768 |
| D1 | VBAT Schottky protection (blocks CR2032 charge path) | BAT54 | SOT-23 | 637-BAT54 | 4878-BAT54CT-ND | C49435667 |
| J1-J3 | Power Module dock receptacles (×3) | TE 1-1674231-1 | 10-position 2.5mm vertical receptacle | 571-1-1674231-1 | A119250-ND | C3683260 |
| J4, J5 | Stator dock hybrid receptacles (×2) | Molex 2195630015 | 5 power + 15 signal press-fit receptacle | 538-219563-0015 | 900-2195630015-ND | Global sourcing / consignment |
| J6 | USB 3.0 Type-A | Dual-Stack | Molex 48406-0003 | 538-48406-0003 | WM10420-ND | C565298 |
| J7 | HDMI Type-A | Full-Size | TE 2007435-1 | 571-2007435-1 | A141617-ND | C195051 |
| J8 | RJ45 with integrated magnetics / PoE entry | Wurth 7499111121A | Long-Body THT RJ45 | 710-7499111121A | 1297-1070-5-ND | C5523983 |
| J9 | DSI1 display FPC connector (15-pin 1.0mm pitch ZIF) | Amphenol F52Q-1A7H1-11015 | 15-pin ZIF, 1.0mm pitch | 649-F52Q-1A7H1-11015 | 609-F52Q-1A7H1-11015CT-ND | C3169095 |
| J10 | JST SH 4-pin 1.0mm fan header | JST SM04B-SRSS-TB(LF)(SN) | SMT 1.0mm pitch | 306-SM04BSRSSTBLFSN | 455-SM04B-SRSS-TBCT-ND | C160404 |
| J11 | Servo connector (3-pin JST PH 2.0mm) | JST B3B-PH-K-S(LF)(SN) | THT | 306-B3BPHKSLFSNP | 455-1705-ND | C131339 |
| J12 | JDB hat power/USB header (female socket) | Adam Tech RS1-05-G — 1×5 2.54mm female | THT | 737-RS1-05-G | 2057-RS1-05-G-ND | C3321119 |
| J13 | JDB hat JTAG header (female socket) | Adam Tech RS1-10-G — 1×10 2.54mm female | THT | 737-RS1-10-G | 2057-RS1-10-G-ND | C3320525 |
| J14 | Amphenol 100-pin B2B socket 4.0mm height (DigiKey: 609-10164227-1004A1RLFCT-ND, Mouser: 649-101642271004RLF) | 10164227-1004A1RLF | CM5 SO-DIMM | 649-101642271004RLF | 609-10164227-1004A1RLFCT-ND | C7435219 |
| J15 | Amphenol 100-pin B2B socket 4.0mm height (DigiKey: 609-10164227-1004A1RLFCT-ND, Mouser: 649-101642271004RLF) | 10164227-1004A1RLF | CM5 SO-DIMM | 649-101642271004RLF | 609-10164227-1004A1RLFCT-ND | C7435219 |
| MH1–MH4 | CM5 brass standoff M2.5 × 4.0mm SMT (Würth 9774040151R) × 4 | M2.5 × 4.0mm | SMT | 710-9774040151R | 732-7089-1-ND | C5182034 |
| R1 | Pull-up for reset | 10kΩ | 0603 | 667-ERJ-3EKF1002V | P10.0KHCT-ND | C191124 |
| R2 | Termination for differential | 100Ω | 0603 | 667-ERJ-3EKF1000V | P100HCT-ND | C193336 |
| R3 | PWR_GD GPIO pull-up (to 3V3_ENIG) | 10kΩ 1% | 0603 | 667-ERJ-3EKF1002V | P10.0KHCT-ND | C191124 |
| R4 | SERVO_HOME pull-up resistor | 10kΩ 1% 0402 | 0402 | 667-ERJ-2RKF1002X | P10.0KLCT-ND | C191123 |
| SW3 | SERVO_HOME homing switch (SPST NO momentary, PCB-mount) | Omron SS-01GL13 | THT | 653-SS-01GL13 | SW865-ND | C3822088 |
| U1 | Raspberry Pi Compute Module 5 (CM5) — multiple acceptable non-Lite variants; minimum 4GB RAM / 8GB eMMC; Wi-Fi optional | N/A | CM5 (SO-DIMM) | various CM5 SKUs | N/A — source from RPi distributors | N/A — not stocked at JLCPCB |
| U2 | USB power switch | TPS2065CDBVR | SOT-23-5 | 595-TPS2065CDBVR | 296-39353-1-ND | C353882 |
| U3 | HDMI power switch | AP2331W-7 | SOT-23-5 | 621-AP2331W-7 | AP2331W-7DICT-ND | C460346 |
| U4 | USB/HDMI ESD | TPD4E05U06QDQARQ1 — 4-ch ESD array, ±15kV, U-DFN-10 | U-DFN-10 | 595-PD4E05U06QDQARQ1 | 296-40696-1-ND | C81353 |

### BOM Notes

Telemetry shunt specifications and Kelvin-sensing notes are detailed in §4. Protection, ESD, and bulk
decoupling capacitor placement rules are detailed in §7. Dock-connector ownership and mating-part
specifications are in §8. The matching PM dock plugs are `TE 1123684-7`; the matching Stator dock plugs
are `Molex 2195620015`.

The Controller also owns the Ethernet / PoE front-end (`TPS2372-4RGWR`, `TPS23730RMTR`, `POE600F-12L`, and
the Ethernet-entry ESD arrays). Those parts are tracked as Controller-owned in
`design/Electronics/Consolidated_BOM.md`; only the externally visible connector and generic local ESD
rows are repeated here until the Controller schematic refdes are frozen.

The servo motor itself (Miuzei Metal Gearbox 90) is a purchased mechanical item and is therefore not
listed in the electronic BOM.
