# Detailed Design: Extension Board (V1.0)

## 1. Modular "Mini-Stack" Logic

* **Role:** Mechanical anchor and Power Injection for 5-rotor groups.
* **Capacity:** Supports a 30-rotor maximum stack via modular 5-rotor increments.

## 2. Connectivity

* **Bus Interface:** Dual 20-pin (2x10) Vertical Shrouded Headers (IN/OUT).
* **Power Injection:** Receives 3V3_ENIG and GND daisy-chain to prevent voltage sag across long stacks.
* **JTAG:** Pass-through for the serial chain; carries TDO_RETURN via dedicated Pin 16.
* **Cross-ref:** See `Stator/Design_Spec.md` and `Reflector/Design_Spec.md` for interconnect pinouts on power (3V3_ENIG/GND), ENC_IN/ENC_OUT, and JTAG TDO_RETURN lines used for reflector loopback/plugboard mapping.

## 3. Diagnostics & Branding

* **Diagnostics:** Integrated 2x8 ENIG Gold Diagnostic Bank (Mid-Stack troubleshooting).
* **Identity:** 2oz Copper / Inverted White Data Plate (V1.0 traceability).
