# Controller Board (V1.0) Design Specification

### 1. Core Processing
*   **Module:** Raspberry Pi Compute Module 5 (CM5).
*   **Stackup:** 6-Layer (JLC06161H-2116) for 5Gbps differential pair integrity.
*   **Handshake:** Receives PWR_GD from Power Module via Gold-plated Samtec ERM8 link.

### 2. Connectivity & Bus
*   **High-Speed Interconnect (BtB Samtec):**
    *   **Connector:** [Samtec FTSH-RA](https://www.samtec.com) (Right-Angle).
    *   **Mating Style:** Flush-edge mounting with **Staggered THR (Through-Hole Reflow) Slotted Clips**.
    *   **Pin Mapping:**
        *   **Pins 1–8:** Ganged for **5A Rotor Rail** (Symmetrical Star Pattern capacitors).
        *   **Pins 9–32:** 12-bit Parallel Data Bus + JTAG signals (Interleaved with GND shields).
*   **Programming:** Internal USB 2.0 link to the JTAG Daughterboard.
*   **Interface:** Samtec FTSH Gold-flashed headers for high-speed data distribution to the Stator.

### 3. Connector Stacks
1. **Top Edge:** Order from Left to Right
    *   **Stator Link:** 40-pin Samtec (Flush with edge).
    *   **Power In:** From Power Module (USB-C, PoE+ & Smart Battery).
2. **Right Edge:** Order from Top to Bottom to follow CM5 pinout flow:
    *   **Video:** Full-size HDMI.
    *   **Data:** Stacked USB 3.0.

### 4. JTAG Programming Subsystem (USB Blaster)
*   **Bridge Architecture:** Dedicated **FT232H** (High-Speed USB 2.0 to JTAG/MPSSE).
*   **Module Type:** Removable **Daughterboard** (2.54mm header) for future-proofing and ease of repair.
*   **JTAG Chain Flow:**
    1.  **CM5 USB 2.0** → **FT232H Daughterboard**.
    2.  **JTAG Out** → **HID Encoder (Dual EPM240T100C CPLD)**.
    3.  **JTAG Chain** → **Plugboard Encoder #1 (Dual EPM240T100C CPLD)**.
    3.  **JTAG Chain** → **Plugboard Encoder #2 (Dual EPM240T100C CPLD)**.
    3.  **JTAG Chain** → **Stator (EPM240T100C CPLD)**.
    4.  **JTAG Chain** → **30x Rotor CPLDs (EPM240T100C CPLD)** via Stator Backplane.
*   **Signal Integrity:** **74LVC1G125** buffers on TCK/TMS lines to drive the heavy 32-device load across the machine.

### 5. Telemetry & Logic (INA219 + SMBus)
*   **Rotor Shunt:** **10mΩ (1206, 1%, 1W)** metal strip resistor.
*   **Sensing:** **Kelvin-connection (4-wire)** with 10Ω/0.1µF RC noise filtering.
*   **I2C Map:**
    *   **INA219 (Telemetry):** 0x40
    *   **STUSB4500 (PD Controller):** 0x28
    *   **Smart Battery (SMBus):** 0x0B
    *   **AS5600 (Rotor Encoders):** 0x36 (One per rotor via I2C Mux).

### 6. CM5 GPIO Mapping Matrix (Enigma-NG)

All GPIOs are referenced to **+3V3_SYSTEM**. Total current draw is limited to <50mA across all pins.

| GPIO | Function | Type | Logic Level | Description |
| :--- | :--- | :--- | :--- | :--- |
| **0 / 1** | **ID_EEPROM** | I2C | 3.3V | Reserved for CM5 HAT ID. |
| **2 / 3** | **I2C1_SDA/SCL** | I2C | 3.3V | **Main Bus:** INA219, STUSB4500, Smart Battery. |
| **4–15** | **DATA_BUS** | Output | 3.3V | **12-bit Parallel Bus** (D0-D11) to Stator/Rotors. |
| **16** | **ROTOR_EN** | Output | 3.3V | Enable for 3.3V_Rotor Buck Converter. |
| **17** | **LED_RED** | PWM | 3.3V | RGB LED - Red Channel (Status/Fault). |
| **18** | **LED_GRN** | PWM | 3.3V | RGB LED - Green Channel (Heartbeat/PoE). |
| **19** | **LED_BLU** | PWM | 3.3V | RGB LED - Blue Channel (USB-C). |
| **20** | **POE_STAT** | Input | 3.3V | Active High: Powered via Ag5300. |
| **21** | **USB_STAT** | Input | 3.3V | Active Low: 12V/15V PD Negotiated. |
| **22** | **BATT_STAT** | Input | 3.3V | Active Low: Battery Present. |
| **23** | **SYS_FAULT** | Input | 3.3V | Active Low: eFuse Fault Interrupt. |

### 7. Protection Notes
*   **External Links:** All inputs (Status) feature 10kΩ series resistors to protect CM5 pins from transient spikes.
*   **Voltage:** 5V signals are strictly forbidden on these pins.

---

## PCB Details

### 1. PCB Fabrication (JLCPCB Specs)
*   **Layers:** **6-Layer** (JLC06161H-2116 stackup).
*   **Finish:** **ENIG (Gold)** for all pads and diagnostic loops.
*   **Solder Mask:** **Dark Green** (Vintage Industrial Lacquer aesthetic).
*   **Silkscreen:** **White**, **Typewriter-style font**, Bilingual (ALL-CAPS GERMAN / Sentence-case English).
*   **Branding:** Top-Left corner features the **Shielded Enigma-NG Square Emblem** (Exposed ENIG Gold tied to GND_CHASSIS).

### 2. JLCPCB 6-Layer Stackup (JLC06161H-2116)
*   **Layer 1 (Top):** High-speed Signals (USB 3.0, HDMI, Ethernet).
*   **Layer 2:** Solid GND Plane.
*   **Layer 3:** Power Islands (Split for 15V, 5V, 3.3V_Rotors, 3.3V_Logic).
*   **Layer 4:** Internal Logic (I2C, Control).
*   **Layer 5:** Solid GND Plane.
*   **Layer 6 (Bottom):** Enigma 12-bit Data Bus & JTAG.

### 3. Trace Widths & Impedance

| Net Class | Target Impedance | Width / Spacing | Layer |
| :--- | :--- | :--- | :--- |
| **USB 3.0** | 90Ω Differential | 10.0 mil / 6.0 mil | L1 |
| **Ethernet/HDMI**| 100Ω Differential | 10.0 mil / 8.0 mil | L1 |
| **5A Power Rail**| N/A (Low Drop) | 60.0 mil (Min) | L3 Island |
| **Logic/I2C** | N/A | 6.0 mil | L4 / L6 |

### 4. Vias & Teardrops
*   **Standard Via:** 0.3mm Drill / 0.6mm Diameter (Staggered zigzag pattern).
*   **VIPPO (Via-in-Pad):** 0.2mm Drill / 0.45mm Diameter (Plugged & Capped).
*   **Teardrops:** Enabled on all signal and power pads to reduce stress and impedance steps.

### 5. Thermal & Branding
*   **Logo:** Top-left 10mm "Enigma-NG" shielded gold emblem.
*   **eFuse:** Top-right near power inputs with dedicated "Caution: Hot" silkscreen.

### 6. Diagnostics & Aesthetics
*   **Bank:** 2x8 Gold-plated ENIG Diagnostic Probe Bank for real-time bus monitoring.
    *   **Placement:** 2x8 2.54mm ENIG Gold Bank placed directly behind the BtB header.
    *   **Orientation:** Facing Upwards for easy logic analyser ribbon cable connection.
    *   **Visuals:** Typewriter-style bilingual silkscreen legend on the bottom layer.
*   **Silkscreen:** Dark Green mask with White Bilingual Typewriter font.
*   **Branding:** Inverted Master Data Plate (Silhouette + JLC Serial Block) on L6 (Bottom).

---

## BOM

### 1. Power Gatekeeper (TPS259474L eFuse)
*   **Calculated Values (11V–17V Window):**
    *   **R1 (Top):** 1.07 MΩ (1%)
    *   **R2 (Mid):** 46.2 kΩ (1%)
    *   **R3 (Bot):** 84.7 kΩ (1%)
*   **Current Limit ($R_{ILIM}$):** 86.6 kΩ for 5.5A hard-trip.
*   **Thermal:** 3x3 VIPPO heatsink grid connected to internal GND planes.
*   **Bilingual Silk:** ACHTUNG: HEISS! (Caution: Hot!).

### 2. Telemetry (INA219 + Shunt)
*   **Shunt Resistor:** 10mΩ (1206, 1%, 1W).
*   **Configuration:** Kelvin-sensing (4-wire) directly to pins for high-current accuracy.
*   **Filtering:** 10Ω + 0.1µF RC filter on sensing lines to suppress rotor switching noise.

### 3. Protection & EMI
*   **ESD Protection:** [TPD12S016](https://www.ti.com) (HDMI) and [TPD4E05U06](https://www.ti.com) (USB 3.0) on Layer 1.
*   **Capacitor Bank:** 50V-rated X7R capacitors (2.5x voltage derating) in a Symmetrical Star pattern.
*   **Status LED:** MIC1555-based 1Hz heartbeat flasher (Bilingual label: ACHTUNG: HEISS!).

### 4. Mating Header (Samtec FTSH)
*   **Specs:** [FTSH-120-01-L-DH](https://uk.rs-online.com/web/p/pcb-headers/7676792) (Right-angle, SMT pins, Through-hole reflow clips).
*   **Pins:** 40-position, 1.27mm pitch.
*   **Decision:** THR (Through-Hole Reflow) slots for automated museum-grade assembly strength.

---

## Decision Log
*   **Ferrite Beads:** Moved exclusively to the **Stator Board** to keep rotor switching noise isolated from the Controller logic.
*   **USB-C:** 16-pin "Power Only" to maximize mechanical durability in classroom settings.
*   **Diagnostic Bank:** 2x8 2.54mm grid with gold-plated loops, positioned in-line with the BtB header for clean logic analyzer probing.
*   **Status LED:** **MIC1555 Hardware Heartbeat** (1Hz pulse) triggers on power-up before CM5 boot for instant status confirmation.