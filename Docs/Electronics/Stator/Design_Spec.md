# Enigma-NG Stator Board (Backplane)

### Project Description
The Stator Board is the mechanical and electrical backbone of the rotor stack. It provides the high-current distribution and signal routing for the 30 modular rotors.

### Core Features
*   **Modular Slots:** 30x [Samtec CLP Series](https://www.samtec.com) low-profile female sockets.
*   **EMI Filtering:** 30x SMD **Ferrite Beads** (one per rotor slot) to prevent switching noise from the iCE40 FPGAs from "polluting" the main Enigma Rail.
*   **Power Tree:** A massive 2oz copper pour for the `+3V3_ROTORS` rail to handle the **5A peak** load without voltage sag.

### 2. Connectors
*   **Controller Link:** The matching **40-pin Samtec CLP-RA** (Right-Angle) receptacle for the Controller Board.
*   **Encoder Interconnects:** 3x 12-pin high-density Hirose DF40 "Press-Fit" connectors for the Keyboard, Lampboard, and Plugboard cable harnesses.
*   **Reflector Interconnect:** 12-pin high-density Hirose DF40 "Press-Fit" connector for the Reflector Board.

### 2. Interconnects
*   **Routing:** Flat Flexible Cable (FFC) secured to the chassis floor with conductive EMI tape for the Interconnects.
