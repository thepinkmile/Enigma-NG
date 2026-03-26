# CM5 GPIO Mapping Matrix (Enigma-NG)

All GPIOs are referenced to **+3V3_SYSTEM**. Total current draw is limited to <50mA across all pins.


| GPIO | Function | Type | Logic Level | Description |
| :--- | :--- | :--- | :--- | :--- |
| **0 / 1** | **ID_EEPROM** | I2C | 3.3V | Reserved for CM5 HAT ID. |
| **2 / 3** | **I2C1_SDA/SCL** | I2C | 3.3V | **Main Bus:** INA219, STUSB4500, Smart Battery. |
| **4–15** | **DATA_BUS** | Output | 3.3V | **12-bit Parallel Bus** (D0-D11) to Stator/Rotors. |
| **16** | **SHIFT_L** | Input | 3.3V | Left Shift Key (Pull-up). |
| **17** | **SHIFT_R** | Input | 3.3V | Right Shift Key (Pull-up). |
| **18** | **ROTOR_EN** | Output | 3.3V | Enable for 3.3V_Rotor Buck Converter. |
| **19** | **LED_RED** | PWM | 3.3V | RGB LED - Red Channel (Status/Fault). |
| **20** | **LED_GRN** | PWM | 3.3V | RGB LED - Green Channel (Heartbeat/PoE). |
| **21** | **LED_BLU** | PWM | 3.3V | RGB LED - Blue Channel (USB-C). |
| **22** | **POE_STAT** | Input | 3.3V | Active High: Powered via Ag5300. |
| **23** | **USB_STAT** | Input | 3.3V | Active Low: 12V/15V PD Negotiated. |
| **24** | **BATT_STAT** | Input | 3.3V | Active Low: Battery Present. |
| **25** | **SYS_FAULT** | Input | 3.3V | Active Low: eFuse Fault Interrupt. |

### 3. Protection Notes
*   **External Links:** All inputs (Shift Keys/Status) feature 10kΩ series resistors to protect CM5 pins from transient spikes.
*   **Voltage:** 5V signals are strictly forbidden on these pins.
