# Electrical Design Requirements

### 1. Component Rules (The "Museum-Grade" Standard)
*   **Dielectric:** **X7R** for all ceramic capacitors (Strictly no Y5V or Z5U).
*   **Derating:** **2.5x Voltage rating** for all power capacitors (e.g., 50V caps on 15V rails).
*   **Tolerance:** **1% precision resistors** for eFuse ladders and INA219 current-sense shunts.
*   **Vias:** **Teardrops** on all signal/power vias; **0.3mm drill** standard; **VIPPO (Via-In-Pad)** for high-density CM5/eFuse pads to prevent solder wicking.
