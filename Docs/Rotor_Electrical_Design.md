# Rotor Electrical Design Requirements

### 1. Power Management
*   **Input:** 3.3V/150mA per rotor (sourced from the Controller Board's **Island C**).
*   **Filtering:** Local **Ferrite Beads** and a **10µF X7R** capacitor bank to suppress switching noise from the 30-rotor chain.

### 2. Communication Bus
*   **The Data Path:** 12-bit parallel bus (D0-D11) passes through every rotor in a daisy-chain or star-bus configuration.
*   **Control:** Shared I2C bus for position telemetry and OLED updates.
*   **JTAG:** Pass-through JTAG lines allow the **USB Blaster** on the Controller Board to program the entire 30-rotor stack in one "daisy-chain" operation.

### 3. Signal Integrity
*   **Impedance:** 50Ω single-ended traces for the 12-bit data bus to prevent "ringing" across the 30-module length.
*   **Shielding:** 4-layer PCB with solid GND planes (L2/L3) to isolate digital switching from the high-accuracy magnetic encoder.
