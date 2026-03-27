# Detailed Design: Shielded Power Module (V1.0)

### 1. Hardware Specifications
*   **PCB Stackup:** 4-Layer / 2oz Finished Copper (JLC04201H-7628).
*   **Substrate:** High-Tg FR4 for thermal stability.
*   **Finish:** ENIG (Gold) for all user-touch points and thermal pads.

### 2. EMI & Filtering (The "Iron Curtain")
*   **Dual-Choke Entry:** 
    *   Primary: [WE-CMBNC Nanocrystalline CMC](https://www.we-online.com) (Broadband).
    *   Secondary: [Laird CM5022 High-Freq Choke](https://uk.farnell.com).
*   **Differential Filtering:** High-current Pi-filters (Molded Inductors + 50V X7R Caps).
*   **Shielding:** Vintage Silver Aluminium enclosure screwed to `GND_CHASSIS` ears.

### 3. UPS & Safety
*   **Energy Storage:** 2.5F Supercap Bank (2x3 Block) providing ~30s hold-time @ 5W.
*   **Thermal Interface:** Gelid GP-Ultimate (15 W/mK) pad on an **Exposed ENIG** bottom zone.
*   **Active Safety:** TPS259474L eFuse (11V-17V) with 1A Soft-Charge for supercaps.
*   **Passive Safety:** 72°C SMD Thermal Cutoff (Bourns AC) in series with the main rail.
*   **Indicator:** 5.1V Zener "Safety Glow" (Amber LED) active during capacitor discharge.

### 4. Traceability & Manufacturing
*   **Assembly:** Single-side (Top) population for JLCPCB SMT service.
*   **Serialization:** JLC Serial Number service block on the bottom layer.
*   **Identification:** Laser-etched **Blitzpfeil** and Proxy QR code (`enigma-ng.link/docs`).
