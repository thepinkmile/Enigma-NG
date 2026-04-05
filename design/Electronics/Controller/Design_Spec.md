# Controller Board (V1.0) Design Specification

**Status:** Draft
**Version:** v1.0.0
**Associated Hardware Revision:** Rev A
**Last Updated:** 2026-04-04

---

## 1. Overview

* **Module:** Raspberry Pi Compute Module 5 (CM5).
* **Role:** Master traffic controller for Power (Alpha) and Encryption Logic (Beta).
* **Stackup:** 6-Layer / 2oz Finished Copper (JLC06161H-2116) for 5Gbps differential pair integrity.
* **Shielding:** High-speed signals (Ethernet, USB 3.0, HDMI) routed as Striplines on L3, shielded by L2/L5 GND planes
  and L4 (Internal) for 6A Power Plane.
* **USB-C:** 16-pin "Power Only" to maximize mechanical durability in classroom settings.
* **Status LED:** **MIC1555 Hardware Heartbeat** (1Hz pulse) triggers on power-up before CM5 boot for instant status
  confirmation.

> **Full design decision history:** See `design/Design_Log.md` for all formal design decisions (DEC-xxx) applicable
> to this board.

## 2. Dual-Link Interface (Samtec ERx8)

> **Assembly Note:** Both BtB connectors (J1 and J2) use ERF8 **female** sockets. This is a deliberate mechanical
> choice — the Controller slides into the enclosure and simultaneously blind-mates with the Power Module (J1) and
> Stator (J2) along the back edge in a single insertion motion. See DEC-014.

* **Link-Alpha (Power/Entry):** ERF8 Female Socket 80-pin Power/Ethernet/Telemetry entry from Power Module.
  * Receives: 5V/6A, 3V3_ENIG, GBE and PWR_GD Data from Power Module.
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
    * **Pins 25–27:** TDO_RETURN + GND shields.
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
* **Interface:** Asymmetrical 1x6 (Power/USB) and 1x10 (Shielded JTAG) 2.54mm ENIG headers.
* **Shielding:** 1:1 Signal-to-Ground ratio on JTAG header to prevent clock crosstalk.
* **Diagnostic Looped Probe Pad Bank:** 2x8 2.54mm grid with gold-plated loops, positioned in-line with the BtB
  header for clean logic analyzer probing.
* **JTAG Chain Flow:**
    1. **CM5 USB 2.0** → **FT232H Daughterboard**.
    2. **JTAG Out** → **Stator CPLD (Intel MAX II EPM240T100C5N)** — first device in chain.
    3. **JTAG Chain** → **HID Encoder (Dual Intel MAX II EPM240T100C5N CPLD)** via Stator J6.
    4. **JTAG Chain** → **Plugboard Encoder #1 (Dual Intel MAX II EPM240T100C5N CPLD)** via Stator J7.
    5. **JTAG Chain** → **Plugboard Encoder #2 (Dual Intel MAX II EPM240T100C5N CPLD)** via Stator J8.
    6. **JTAG Chain** → **30x Rotor CPLDs (Intel MAX II EPM240T100C5N)** via Stator Backplane.
    7. **TDO_RETURN** ← Reflector → Extension Port → Stator J5 pin 15 → LINK-BETA pin 26 → FT232H.
* **Signal Integrity:** **74LVC1G125** buffers on TCK/TMS lines to drive the heavy 37-device load across the machine.
* **JTAG Series Termination:** 33Ω series resistors (R4–R6) placed within 2 mm of each 74LVC1G125
  output on TCK, TMS, and TDI before LINK-BETA. Matches source impedance to 50Ω PCB traces
  (Zo ≈ 53Ω). See `design/Electronics/JTAG_Integrity.md` and DEC-016.
* **Cross-ref:** See `JTAG_Daughterboard/Design_Spec.md` for FT232H module schematics and assembly details.

## 4. Telemetry & Logic (INA219 + SMBus)

* **Rotor Shunt:** **20mΩ (1206, 1%, 0.25W)** metal strip resistor on Stator board (Stator owns this component — see `Stator/Design_Spec.md`).
* **Sensing:** **Kelvin-connection (4-wire)** with 10Ω/0.1µF RC noise filtering.
* **Shunt Resistor:** 20mΩ (1206, 1%, 0.25W). Firmware must use R_SHUNT = 0.020Ω in the INA219 current calculation (I = V_shunt / R_shunt).
  * At 3A max: V_drop = 60mV — fits the INA219 ±80mV PGA range; 3.0A resolution ÷ 2¹² = 0.73mA/LSB.
* **Filtering:** 10Ω + 0.1µF RC filter on sensing lines to suppress rotor switching noise.
* **I2C Map:**
  * **INA219 Power Module Monitor**: I2C @ 0x40 on Power Module.
  * **INA219 Rotor Monitor**: I2C @ 0x45 on Stator (rotor stack current/voltage).
  * **STUSB4500 (PD Controller):** I2C @ 0x28 on Power Module.
  * **Smart Battery (SMBus):** I2C @ 0x0B on Power Module.

## 5. CM5 GPIO Mapping Matrix (Enigma-NG)

All GPIOs are referenced to **+3V3_ENIG**. Total current draw is limited to <50mA across all pins.

| GPIO | Function | Type | Logic Level | Description |
| :--- | :--- | :--- | :--- | :--- |
| **0 / 1** | **ID_EEPROM** | I2C | 3.3V | Reserved for CM5 HAT ID. |
| **2 / 3** | **I2C1_SDA/SCL** | I2C | 3.3V | **Main Bus:** INA219, STUSB4500, Smart Battery. |
| **4–15** | **DATA_BUS** | Output | 3.3V | **12-bit Parallel Bus** (D0-D11) to Stator/Rotors. |
| **16** | **ROTOR_EN** | Output | 3.3V | Enable signal to Power Module 3V3_ENIG LDO for sequenced rotor stack power-up. |
| **17** | **SW_LED_R** | PWM | 3.3V | RGB switch (SW1) — Red channel. Fault / graceful shutdown indicator. |
| **18** | **SW_LED_G** | PWM | 3.3V | RGB switch (SW1) — Green channel. USB-C active power source. |
| **19** | **SW_LED_B** | PWM | 3.3V | RGB switch (SW1) — Blue channel. PoE active power source. |
| **20** | **POE_STAT** | Input | 3.3V | Active High: PoE live (TPS2372-4 /PG signal asserted). |
| **21** | **USB_STAT** | Input | 3.3V | Active Low: 12V/15V PD Negotiated. |
| **22** | **USB_FAULT** | Input | 3.3V | Active Low: USB power fault from on-board TPS2065C (local to Controller; no BtB pin required). |
| **23** | **BATT_PRES_N** | Input | 3.3V | Active Low: Battery present (via BtB pin 45; from Power Module J3 presence detect circuit R6/TPD1E10B06). |
| **24** | **SW_LED_CTRL** | Output | 3.3V | Drive HIGH when CM5 firmware is ready to control SW1 RGB LED; disables hardware MIC1555 orange-flash path on Power Module. |
| **25** | **SYS_FAULT** | Input | 3.3V | Active Low: eFuse fault interrupt from TPS25980 FAULT pin on Power Module (via BtB pin 29). Triggers OS fault handler in power monitor daemon; useful for power dashboard diagnostics even during graceful shutdown. |
| **26** | **SYS_RESET_N** | Output | 3.3V | Active Low: system-wide CPLD reset. Broadcast to all Intel MAX II EPM240T100C5N CPLDs via LINK-BETA pin 8 (Stator), Extension Ports, and Encoder Ports. On-board CPLDs (HID Encoder, Plugboard #1/#2) driven directly. |

## 6. Protection & EMI

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

## 7. Connectivity

### Link-Beta Connector (Samtec ERF8-020)

* **Part:** ERF8-020-05.0-S-DV-K-TR (Female Socket, 40-pin, 0.8mm pitch, 5.0mm stack height).
* **Mating Part (Stator):** ERM8-020-05.0-S-DV-K-TR (Male Header).
* **Pitch:** 0.8mm.
* **Stack Height:** 5.0mm.
* **Assembly:** SMT reflow; no THR clips required.
* **Decision:** See DEC-015 for 80→40 pin reduction rationale and poka-yoke safety note.

## 8. PCB Fabrication & Stackup

### PCB Fabrication (JLCPCB Specs)

* **Layers:** **6-Layer** (JLC06161H-2116 stackup).
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
| **USB 3.0** | 90Ω Differential | 10.0 mil / 6.0 mil | L1 |
| **Ethernet/HDMI** | 100Ω Differential | 10.0 mil / 8.0 mil | L1 |
| **JTAG signals** | 50Ω Single-ended | **5.0 mil (0.127 mm)** | L6 |
| **5A Power Rail** | N/A (Low Drop) | 60.0 mil (Min) | L3 Island |
| **Logic/I2C** | N/A | 6.0 mil | L4 / L6 |

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

## 9. Thermal, Branding & Diagnostics

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

## 10. Bill of Materials

| Ref | Component | Value | Package | Mouser Part # | DigiKey Part # | JLCPCB Part # |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| C1-C5 | Bulk entry decoupling bank (star/spoke) | 10uF X7R 50V | 1206 | 187-CL31B106KBHNNNE | 1276-6767-1-ND | CL31B106KBHNNNE |
| J1 | Link-Alpha 80-pin Socket | ERF8 (female) | Samtec | 200-ERF8040050SDVKTR | SAM8621-ND | N/A — customer-supplied |
| J2 | Link-Beta 40-pin Socket | ERF8 (female) | Samtec | 200-ERF8020050SDVKTR | SAM8622-ND ⚠️ verify | N/A — customer-supplied |
| J3 | USB 3.0 Type-A | Dual-Stack | Molex 48406-0003 | 538-0484060003 | WM1394-ND | C123458 |
| J4 | HDMI Type-A | Full-Size | TE 2007435-1 | 571-2007435-1 | A125057-ND | C123459 |
| R1 | Pull-up for reset | 10kΩ | 0603 | 667-ERJ-3EKF1002V | P10.0KBYCT-ND | C25804 |
| R2 | Termination for differential | 100Ω | 0603 | 667-ERJ-3EKF1000V | P100BYCT-ND | C25806 |
| R3 | PWR_GD GPIO pull-up (to 3V3_ENIG) | 10kΩ 1% | 0603 | 667-ERJ-3EKF1002V | P10.0KBYCT-ND | C25804 |
| R4 | JTAG TCK series termination (after 74LVC1G125, before LINK-BETA pin 2) | 33Ω 1% | 0603 | 667-ERJ-3EKF33R0V | P33.0BYCT-ND | C25819 |
| R5 | JTAG TMS series termination (after 74LVC1G125, before LINK-BETA pin 4) | 33Ω 1% | 0603 | 667-ERJ-3EKF33R0V | P33.0BYCT-ND | C25819 |
| R6 | JTAG TDI series termination (after 74LVC1G125, before LINK-BETA pin 6) | 33Ω 1% | 0603 | 667-ERJ-3EKF33R0V | P33.0BYCT-ND | C25819 |
| U1 | Raspberry Pi Compute Module 5 (CM5) | N/A | CM5 | CM5 | ??? | ??? |
| U2 | USB power switch | TPS2065C | SOIC-8 | 595-TPS2065CDBVR | 296-TPS2065CDBVRCT-ND | C123460 |
| U3 | HDMI power switch | AP2331W | SOT-23 | 621-AP2331W-7 | AP2331W-7DICT-ND | C123461 |
| U4 | USB/HDMI ESD | TPD4E05U06 | VQFN | 595-TPD4E05U06DBVR | 296-TPD4E05U06DBVRCT-ND | C123462 |
| U5 | 74LVC1G125 | Bus Buffer | SOT-23 | 771-74LVC1G125DBVR | 296-74LVC1G125DBVRCT-ND | C123463 |

### BOM Notes

Telemetry shunt specifications and Kelvin-sensing notes are detailed in §4. Protection, ESD, and bulk decoupling
capacitor placement rules are detailed in §6. Mating header assembly specifications are in §7.
