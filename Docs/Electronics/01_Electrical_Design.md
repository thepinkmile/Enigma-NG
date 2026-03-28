# Electrical Design Requirements

### 1. Power Architecture
*   **Input Range:** 11.0V – 17.0V (The "Enigma Rail").
*   **Priority Logic:** LTC4412 Ideal Diodes (PoE+ is primary; Battery is tertiary).
*   **Protection:** TPS259474L eFuse with 5.5A hard-limit and 16.5V OVP.
*   **Islands:** 4-island L3 Power Plane (15V Enigma, 5V System, 3.3V/5A Rotors, 3.3V/Logic).

### 2. Signal Integrity
*   **USB 3.0:** 90Ω Differential Pairs (Layer 1) with <0.1mm intra-pair skew.
*   **Ethernet/HDMI:** 100Ω Differential Pairs (Layer 1).
*   **Data Bus:** 12-bit parallel bus (Layer 6) shielded by L5 GND.

### 3. Safety & EMC
*   **ESD:** TPD12S016 (HDMI) and TPD4E05U06 (USB) protection on all external ports.
*   **Grounding:** 4-layer GND_CHASSIS ring with 2.5mm staggered via-stitching.
*   **Isolation:** 1500V Galvanic isolation via Ag5300 PoE+ Module.
