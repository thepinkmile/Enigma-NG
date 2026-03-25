# I/O CPLD Detailed Design Decisions & BOM

### 1. JTAG Chain Integrity
*   **Buffering:** [74LVC1G125](https://www.ti.com) buffers on the TCK and TMS lines to maintain signal integrity across the long chain (2x I/O CPLDs + 30 Rotor FPGAs).
*   **Termination:** 47Ω series resistors on the JTAG data lines to prevent reflections.

### 2. Key Mapping (64-Way QWERTY)
*   **Layout:** Standard QWERTY + Numbers + Symbols + Shift.
*   **Debouncing:** Digital de-bounce implemented in the CPLD VHDL/Verilog, eliminating mechanical "key chatter."

### 3. BOM (Key Components)
*   **Logic:** 2x Altera EPM240T100.
*   **Voltage Reg:** [TLV755P](https://www.ti.com) (Low-dropout regulator for CPLD core).
*   **Switches:** Mechanical "Clicky" switches (e.g., Cherry MX) for the Keyboard mode.
*   **Sockets:** 3.5mm or 4mm Jack-Sensing sockets for Plugboard mode.

### 4. PCB Specs (JLCPCB)
*   **Layers:** 4-Layer (JLC04161H-7628).
*   **Finish:** ENIG (Gold) for TQFP-100 pads.
*   **Aesthetics:** Dark Green Solder Mask; Typewriter font (ALL-CAPS GERMAN).
