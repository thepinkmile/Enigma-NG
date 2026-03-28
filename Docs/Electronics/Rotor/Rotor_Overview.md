# Enigma-NG Rotor Module Architecture

The Enigma-NG uses a 30-rotor stack. Unlike the original mechanical rotors, these are **Smart Digital Rotors** where the internal scrambled wiring is emulated by a dedicated logic chip on each module.

### 1. Core Logic (The Digital Brain)
*   **Chip:** Lattice [iCE40 UltraPlus FPGA](https://www.latticesemi.com) or similar CPLD.
*   **Role:** Performs the instantaneous 12-bit parallel transposition (substitution cipher) for the forward and backward signal paths.
*   **Memory:** Stores the 26-position wiring table for any historical rotor (I-VIII, Beta, Gamma) selectable via the CM5.

### 2. Mechanical Interface
*   **Vertical Mating:** Each rotor features a **Samtec 0.8mm Edge Rate** connector on the bottom, allowing it to "slot" into the Stator Board.
*   **Rotational Feedback:** A high-resolution **Magnetic Hall-Effect Encoder** (e.g., [AS5600](https://www.ams-osram.com)) tracks the physical thumbwheel position.

### 3. Visuals
*   **Display:** Each rotor has an integrated **0.42" OLED** or 7-segment display behind the thumbwheel to show the current character (A-Z) and ring setting (Ringstellung).
