# Enigma-NG CPLD-Driven I/O Module

### Project Description
A high-performance 64-node interface board. Unlike static expanders, this module uses dual Altera MAX II CPLDs to handle real-time reciprocal encryption for the plugboard and de-bouncing for the 64-key QWERTY keyboard.

### Core Logic
*   **Logic:** 2x [EPM240T100C5N](https://www.intel.com) (100-pin TQFP).
*   **Capacity:** 240 Logic Elements (LEs) per chip, providing 80 user I/O pins.
*   **Bus:** 12-bit Parallel Data Bus (D0-D11) interface.

### JTAG Integration
*   **Chain Position:** The I/O CPLDs sit at the start of the JTAG chain, followed by the 30 Rotor FPGAs.
*   **Programming:** Allows for "In-System Sources and Probes" debugging via the CM5 GUI.
