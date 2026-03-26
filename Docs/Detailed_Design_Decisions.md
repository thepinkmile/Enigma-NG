# Detailed Design Decisions & BOM

### 1. Component Rules (The "Museum-Grade" Standard)
*   **Dielectric:** **X7R** for all ceramic capacitors (Strictly no Y5V or Z5U).
*   **Derating:** **2.5x Voltage rating** for all power capacitors (e.g., 50V caps on 15V rails).
*   **Tolerance:** **1% precision resistors** for eFuse ladders and INA219 current-sense shunts.
*   **Vias:** **Teardrops** on all signal/power vias; **0.3mm drill** standard; **VIPPO (Via-In-Pad)** for high-density CM5/eFuse pads to prevent solder wicking.

### 2. Power Gatekeeper (TPS259474L eFuse)
*   **Calculated Rails (11V–17V Window):**
    *   **R1 (Top):** 1.07 MΩ (1%)
    *   **R2 (Mid):** 46.2 kΩ (1%)
    *   **R3 (Bot):** 84.7 kΩ (1%)
*   **Current Limit ($R_{ILIM}$):** **86.6 kΩ** for 5.5A hard-trip.
*   **Thermal Management:** 3x3 VIPPO heatsink grid connected to internal GND planes. 
*   **Bilingual Silk:** ACHTUNG: HEISS! (Caution: Hot!).

### 3. JTAG Programming Subsystem (USB Blaster)
*   **Bridge Architecture:** Dedicated **FT232H** (High-Speed USB 2.0 to JTAG/MPSSE).
*   **Module Type:** Removable **Daughterboard** (2.54mm header) for future-proofing and ease of repair.
*   **JTAG Chain Flow:**
    1.  **CM5 USB 2.0** → **FT232H Daughterboard**.
    2.  **JTAG Out** → **I/O CPLD #1 (EPM240)**.
    3.  **JTAG Chain** → **I/O CPLD #2 (EPM240)**.
    4.  **JTAG Chain** → **30x Rotor FPGAs (iCE40)** via Stator Backplane.
*   **Signal Integrity:** **74LVC1G125** buffers on TCK/TMS lines to drive the heavy 32-device load across the machine.

### 4. Telemetry & Logic (INA219 + SMBus)
*   **Rotor Shunt:** **10mΩ (1206, 1%, 1W)** metal strip resistor.
*   **Sensing:** **Kelvin-connection (4-wire)** with 10Ω/0.1µF RC noise filtering.
*   **I2C Map:**
    *   **INA219 (Telemetry):** 0x40
    *   **STUSB4500 (PD Controller):** 0x28
    *   **Smart Battery (SMBus):** 0x0B
    *   **AS5600 (Rotor Encoders):** 0x36 (One per rotor via I2C Mux).

### 5. High-Speed Interconnect (BtB Samtec)
*   **Connector:** [Samtec FTSH-RA](https://www.samtec.com) (Right-Angle).
*   **Mating Style:** Flush-edge mounting with **Staggered THR (Through-Hole Reflow) Slotted Clips**.
*   **Pin Mapping:**
    *   **Pins 1–8:** Ganged for **5A Rotor Rail** (Symmetrical Star Pattern capacitors).
    *   **Pins 9–32:** 12-bit Parallel Data Bus + JTAG signals (Interleaved with GND shields).

### 6. PCB Fabrication (JLCPCB Specs)
*   **Layers:** **6-Layer** (JLC06161H-2116 stackup).
*   **Finish:** **ENIG (Gold)** for all pads and diagnostic loops.
*   **Solder Mask:** **Dark Green** (Vintage Industrial Lacquer aesthetic).
*   **Silkscreen:** **White**, **Typewriter-style font**, Bilingual (ALL-CAPS GERMAN / Sentence-case English).
*   **Branding:** Top-Left corner features the **Shielded Enigma-NG Square Emblem** (Exposed ENIG Gold tied to GND_CHASSIS).

### 7. Decision Log
*   **Ferrite Beads:** Moved exclusively to the **Stator Board** to keep rotor switching noise isolated from the Controller logic.
*   **USB-C:** 16-pin "Power Only" to maximize mechanical durability in classroom settings.
*   **Diagnostic Bank:** 2x8 2.54mm grid with gold-plated loops, positioned in-line with the BtB header for clean logic analyzer probing.
*   **Status LED:** **MIC1555 Hardware Heartbeat** (1Hz pulse) triggers on power-up before CM5 boot for instant status confirmation.
