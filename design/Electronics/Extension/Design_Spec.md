# Detailed Design: Extension Board (V1.0)

## 1. Modular "Mini-Stack" Logic

* **Role:** Mechanical anchor and Power Injection for 5-rotor groups.
* **Capacity:** Supports a 30-rotor maximum stack via modular 5-rotor increments.

## 2. Connectivity

* **Bus Interface:** Dual 20-pin (2x10) Vertical Shrouded Headers (IN/OUT).
* **Power Injection:** Receives 3.3V_ENIG and GND daisy-chain to prevent voltage sag across long stacks.
* **JTAG:** Pass-through for the serial chain; carries TDO_RETURN via dedicated Pin 16.

## 3. Diagnostics & Branding

* **Diagnostics:** Integrated 2x8 ENIG Gold Diagnostic Bank (Mid-Stack troubleshooting).
* **Identity:** 2oz Copper / Inverted White Data Plate (V1.0 traceability).
