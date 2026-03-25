# Detailed Design Decisions

### 1. Component Rules (The "Gold Standard")
*   **Dielectric:** X7R for all ceramic capacitors (No Y5V or Z5U permitted).
*   **Derating:** 2.5x Voltage rating for all power caps (e.g., 50V caps on 15V rails).
*   **Tolerance:** 1% precision resistors for eFuse ladders and INA219 shunts.
*   **Vias:** Teardrops on all vias; 0.3mm drill standard; VIPPO for high-density pads.

### 2. PCB Fabrication (JLCPCB Specs)
*   **Layers:** 6-Layer (JLC06161H-2116 stackup).
*   **Finish:** ENIG (Electroless Nickel Immersion Gold).
*   **Solder Mask:** Dark Green (Authentic Industrial Lacquer aesthetic).
*   **Silkscreen:** White, Typewriter-style font, Bilingual (ALL-CAPS GERMAN / Sentence-case English).

### 3. Decision Log
*   **Ferrite Beads:** Moved to Stator Board to snuff EMI at the source (rotors).
*   **USB-C:** 16-pin "Power Only" to simplify routing and increase durability.
*   **Diagnostic Bank:** 2x8 2.54mm pitch grid to allow Logic Analyser IDC cable connection.
*   **Logo:** Top-Left ENIG "Enigma-NG" emblem tied to GND_CHASSIS for shielding.
