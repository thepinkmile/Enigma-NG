# Rotor Detailed Design Decisions & BOM

### 1. Position Sensing (The "Zero-Wear" System)
*   **Sensor:** [AS5600 Magnetic Encoder](https://www.ams-osram.com).
*   **Decision:** We avoid mechanical wipers/brushes (the main failure point of original Enigmas) in favour of contactless magnetic sensing.
*   **Precision:** 12-bit resolution allows the CM5 to detect if a rotor is "between" characters and flag a mechanical jam.

### 2. Logic & Transposition
*   **Logic:** The iCE40 FPGA emulates the 26x26 cross-wiring.
*   **Latency:** Sub-10ns transposition time, ensuring the entire 30-rotor "trip" happens well within one CPU clock cycle.
*   **Configuration:** CM5 loads the "Rotor Type" (e.g., Rotor I, II, III) into the FPGA's SRAM at boot via the I2C bus.

### 3. BOM (Key Components per Rotor)
*   **Logic:** Lattice iCE40UP5K-SG48.
*   **Encoder:** ams-OSRAM AS5600.
*   **Connector:** Samtec ERM8 Series (0.8mm Pitch).
*   **Passives:** 0402 X7R 10V Capacitors (Minimum 2.5x derating).

### 4. PCB Fabrication (JLCPCB Specs)
*   **Layers:** 4-Layer (JLC04161H-7628).
*   **Finish:** ENIG (Gold) for the edge-rate connector pads.
*   **Aesthetics:** Dark Green Solder Mask with Typewriter font labeling (e.g., "WALZE I").
