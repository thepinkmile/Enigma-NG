# Enigma-NG JTAG USB Blaster Daughterboard

### Project Description
A high-speed USB-to-JTAG bridge module that allows the CM5 to natively program the 30-rotor FPGA stack and the 2 I/O CPLDs. This module replicates the functionality of an **Intel (Altera) USB Blaster II** on a tiny daughterboard.

### Core Logic
*   **Bridge Chip:** [FT232H](https://ftdichip.com) or [CY7C68013A](https://www.infineon.com) (FX2LP).
*   **Role:** Converts the CM5's USB 2.0 signals into high-speed JTAG (TCK, TMS, TDI, TDO) commands.
*   **Integrated Driver:** Compatible with `OpenOCD` or `Quartus` via a custom Linux driver on the CM5.

### 2. Electrical Requirements
*   **Voltage:** Powered by the +3.3V Logic Rail from the Controller Board.
*   **Level Shifting:** [74LVC1T45](https://www.ti.com) dual-supply buffers to match the variable I/O voltages of the rotor stack (1.8V to 3.3V).
*   **Clocking:** Dedicated 24MHz crystal for the FT232H to ensure JTAG clock stability across the 32-device chain.
