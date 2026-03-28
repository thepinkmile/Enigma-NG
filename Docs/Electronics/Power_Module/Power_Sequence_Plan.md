# Power Sequencing & Hardware Reset Plan

### 1. The "Safe-Start" Logic
To prevent the CM5 from attempting to boot during the 12V-15V "Enigma Rail" ramp-up, we use an automated voltage supervisor combined with a manual override.

*   **Supervisor IC:** [MCP121T-450E](https://www.microchip.com) (4.50V Threshold).
*   **Trigger:** The supervisor monitors the **+5V_SYSTEM** rail. It holds the `GLOBAL_EN` (PMIC_EN) pin LOW until the rail is stable.
*   **Manual Reset:** A high-quality tactile button is wired in parallel to the supervisor output. 
    *   **Action:** Pressing the button pulls `GLOBAL_EN` to GND, forcing a hard PMIC reset of the CM5 without cycling the 12V-15V Rotor Rail.

### 2. Startup Timeline
1.  **Input:** 12V-15V enters via PoE+/USB-C/Battery.
2.  **Gate:** TPS259474L eFuse validates voltage and current.
3.  **Bucks:** 5V and 3.3V_Rotor converters start.
4.  **Supervisor:** Once 5V hits 4.5V, a 200ms delay timer starts.
5.  **Release:** `GLOBAL_EN` goes HIGH; CM5 PMIC begins internal 1.8V/1.1V sequencing.
6.  **Heartbeat:** MIC1555 starts the 1Hz Green "Initialising" pulse.
