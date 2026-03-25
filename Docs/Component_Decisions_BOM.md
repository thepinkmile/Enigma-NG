# Component Selection & Decision Log

### 1. Power Gatekeeper (TPS259474L eFuse)
*   **Calculated Values (11V–17V Window):**
    *   **R1 (Top):** 1.07 MΩ (1%)
    *   **R2 (Mid):** 46.2 kΩ (1%)
    *   **R3 (Bot):** 84.7 kΩ (1%)
*   **Current Limit ($R_{ILIM}$):** 86.6 kΩ for 5.5A hard-trip.
*   **Thermal:** 3x3 VIPPO heatsink grid connected to internal GND planes.

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
