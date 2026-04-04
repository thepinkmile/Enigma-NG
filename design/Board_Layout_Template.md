# Board_Layout.md

**Status:** Draft
**Version:** v1.0.0
**Associated Hardware Revision:** Rev A
**Last Updated:** 2024-05-22

---

## 1. Physical Constraints

* **Dimensions:** 100mm x 80mm (Standard 2-layer PCB).
* **Mounting:** 4x M3 holes, 5mm offset from corners.
* **Orientation:** Main MCU positioned centrally; I/O connectors on the perimeter for clean cable management.
* **Enclosure Clearance:** Ensure 15mm vertical clearance for stacked header connectors.

## 2. Component Layout Overview

* **Top Left:** Power Input (PWR_IN).
* **Top Center:** J1 Keyboard Header (2x13).
* **Top Right:** J2 Lampboard Header (2x13).
* **Center:** Main Controller (CM5 / MCU).
* **Left/Right Flanks:** MCP23017 I2C Expanders (U1 & U2).
* **Bottom Right:** Rotor Interfaces (J3/J4) and Reset Button.

‘’’text
+-------------------------------------------------------------+
|                                                             |
| [PWR_IN]   [J1: KEYBOARD]           [J2: LAMPBOARD]         |
|   |   |        (2x13 HDR)               (2x13 HDR)          |
|   +---+                                                     |
|                                                             |
|  [MCP23017_U1]                      [MCP23017_U2]           |
|  (Keyboard I2C)                     (Lampboard I2C)         |
|                                                             |
|             +-------------------------+                     |
|             |                         |      [J3: ROTORS]   |
|             |      MAIN CONTROLLER    |       (1x6 HDR)     |
|             |         (CM5 / MCU)     |                     |
|             |                         |      [J4: ROTORS]   |
|             +-------------------------+       (1x6 HDR)     |
|                                                             |
|  [PLUGBOARD_CON]                                            |
|    (2x13 HDR)           [I2C_BUS_EXP]         [RESET_BTN]   |
|                                                             |
+-------------------------------------------------------------+
‘’’

## 3. Connector Pin Mappings

### 3.1 J1: Keyboard Connector (26-Pin)

| Pin # | Label | Expander Pin | Net Name | Function |
| :--- | :--- | :--- | :--- | :--- |
| 1 | KEY_A | U1: GPA0 | KB_A | Input |
| 2 | KEY_B | U1: GPA1 | KB_B | Input |
| ... | ... | ... | ... | ... |
| 26 | KEY_Z | U1: GPB7 | KB_Z | Input |

### 3.2 J2: Lampboard Connector (26-Pin)

| Pin # | Label | Expander Pin | Net Name | Function |
| :--- | :--- | :--- | :--- | :--- |
| 1 | LED_A | U2: GPA0 | LAMP_A | Output (3.3V) |
| 2 | LED_B | U2: GPA1 | LAMP_B | Output (3.3V) |
| ... | ... | ... | ... | ... |
| 26 | LED_Z | U2: GPB7 | LAMP_Z | Output (3.3V) |

### 3.3 J3/J4: Rotor Interface (6-Pin)

| Pin # | Name | Description |
| :--- | :--- | :--- |
| 1 | VCC | 3.3V Supply |
| 2 | GND | Ground |
| 3 | SDA | I2C Data |
| 4 | SCL | I2C Clock |
| 5 | INT | Interrupt (Rotor Index) |
| 6 | AUX | Reserved / Type ID |

## 4. Interconnect Matrix

* **I2C Bus:** All modules (Expanders, Rotor Sensors) share the primary I2C bus connected to MCU GPIO 2 (SDA) and GPIO 3 (SCL).
* **Address Selection:**
  * MCP23017-U1: 0x20 (A0, A1, A2 tied to GND).
  * MCP23017-U2: 0x21 (A0 tied to 3.3V; A1, A2 tied to GND).
* **Plugboard Logic:** The plugboard uses a standard 2.54mm 2x13 header. Pins are mapped to a high-impedance sensing net to detect manual character "jumps".

## 5. Critical KiCAD Layout Notes

1. **I2C Pull-ups:** R1 and R2 (4.7k) must be placed within 10mm of the MCU SDA/SCL pins.
2. **Power Planes:** Use a dedicated Ground Plane on the bottom copper layer (B.Cu).
3. **Trace Routing:** Keep high-current LED traces (Lampboard) away from high-speed I2C clock lines to prevent cross-talk.
4. **Bypass Caps:** Each MCP23017 must have a 100nF capacitor immediately adjacent to the VDD pin.

## 6. References

* [Design Specification](./Design_Spec.md)
* [KiCAD Project Files](../Hardware/Electronics_Controller_RevA/)
* [Enigma-NG Wiki Main Page](https://github.com)
