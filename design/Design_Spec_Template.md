# Electronics Controller: Design Spec

**Status:** Draft
**Version:** v1.0.0
**Associated Hardware Revision:** Rev A
**Last Updated:** 2024-05-22

## 1. System Overview

The Electronics Controller is the central hub of the Enigma-NG.
It coordinates communication between the input (Keyboard), encryption logic (Rotors/Plugboard), and output (Lampboard).
To maintain modularity and a low-profile wiring harness, the system relies on I2C I/O expanders.

## 2. Functional Requirements

* **FR-1:** Interface with a 26-key tactile keyboard matrix.
* **FR-2:** Drive a 26-LED lampboard display.
* **FR-3:** Monitor 13 patch-cable pairs on the physical Plugboard.
* **FR-4:** Sense and index the positions of 3-5 modular Rotors.
* **FR-5:** Provide a unified I2C bus for all peripheral modules.

## 3. Electrical Design Rules (KiCAD)

To ensure PCB manufacturing compatibility and signal integrity, the following rules are enforced in the KiCAD project:

### 3.1 Net Classes & Routing

* **Default Trace Width:** 0.25mm for signal lines.
* **Power Trace Width (VCC/GND):** 0.50mm to handle LED current spikes.
* **Clearance:** 0.20mm minimum between all copper features.
* **Via Size:** 0.6mm Diameter / 0.3mm Drill.

### 3.2 Signal Integrity & Power

* **I2C Pull-ups:** 4.7kΩ resistors required on SDA and SCL lines at the Controller hub.
* **Decoupling:** 100nF ceramic capacitor placed as close as possible to the VCC pin of every IC (MCP23017, etc.).
* **Bulk Capacitance:** 10µF tantalum or electrolytic capacitor at the main power entry point.

### 3.3 Hardware Constraints

* **Logic Level:** 3.3V (All I/O must be 5V tolerant or shifted if using older 5V logic).
* **Connectors:** Use standardized 2.54mm pitch headers for all module interconnects.

## 4. System Architecture

### 4.1 I2C Address Map

| Device | Description | Default Address |
| :--- | :--- | :--- |
| **MCP23017-1** | Keyboard Expander | 0x20 |
| **MCP23017-2** | Lampboard Expander | 0x21 |
| **Rotor-Sensing**| Custom I2C/Analog | 0x22 - 0x26 |

### 4.2 Power Budget

* **Logic (3.3V):** Peak 250mA (MCU + Expanders).
* **LEDs (3.3V/5V):** Peak 500mA (assuming 1-2 LEDs active at any time).

## 5. Bill of Materials (BOM)

| Ref | Component | Value/Part | Package | Mouser Part # | DigiKey Part # | JLCPCB Part # |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| C1, C4 | Pi-filter bulk cap (input + output) | 22µF 50V X7R | 1210 | 81-GRM32ER71H226KE5L | 490-GRM32ER71H226KE15LCT-ND | ??? |
| C2, C5 | Pi-filter mid-freq bypass | 1µF 50V X7R | 0805 | 81-GRM21BR71H105KA2L | 490-GRM21BR71H105KA12LCT-ND | C28323 |

## 6. References

* [Board Layout](./Board_Layout.md)
* [Enigma-NG Project Wiki](https://github.com)
