# KiCad 9 Design Rules & Manufacturing Specs

### 1. JLCPCB 6-Layer Stackup (JLC06161H-2116)
*   **Layer 1 (Top):** High-speed Signals (USB 3.0, HDMI, Ethernet).
*   **Layer 2:** Solid GND Plane.
*   **Layer 3:** Power Islands (Split for 15V, 5V, 3.3V_Rotors, 3.3V_Logic).
*   **Layer 4:** Internal Logic (I2C, Control).
*   **Layer 5:** Solid GND Plane.
*   **Layer 6 (Bottom):** Enigma 12-bit Data Bus & JTAG.

### 2. Trace Widths & Impedance

| Net Class | Target Impedance | Width / Spacing | Layer |
| :--- | :--- | :--- | :--- |
| **USB 3.0** | 90Ω Differential | 10.0 mil / 6.0 mil | L1 |
| **Ethernet/HDMI**| 100Ω Differential | 10.0 mil / 8.0 mil | L1 |
| **5A Power Rail**| N/A (Low Drop) | 60.0 mil (Min) | L3 Island |
| **Logic/I2C** | N/A | 6.0 mil | L4 / L6 |

### 3. Vias & Teardrops
*   **Standard Via:** 0.3mm Drill / 0.6mm Diameter (Staggered zigzag pattern).
*   **VIPPO (Via-in-Pad):** 0.2mm Drill / 0.45mm Diameter (Plugged & Capped).
*   **Teardrops:** Enabled on all signal and power pads to reduce stress and impedance steps.
