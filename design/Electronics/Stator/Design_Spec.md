# Enigma-NG Stator Board (Backplane)

The Stator Board is the mechanical and electrical backbone of the rotor stack. It provides the high-current distribution and signal routing for the 30 modular rotors.

## 1. Core Features

* **Modular Slots:** 30x [Samtec CLP Series](https://www.samtec.com) low-profile female sockets.
* **Power Tree:** A massive 2oz copper pour for the `+3V3_ENIG` rail to handle the **5A peak** load without voltage sag.

## 2. Logic

* **CPLD:** Intel MAX II EPM240T100C5N manages the routing of the encryption path.
* **Reset:** Pin 100 (DEV_CLRN) tied to the global SYS_RESET_N rail for synchronous restarts.

## 3. Connectors

* **Controller Link (Link-Beta):** The matching **40-pin Samtec CLP-RA** (Right-Angle) receptacle for the Controller Board (ERF8 Female Socket).
  * **Data In:** Receives JTAG, Reset from Controller.
  * **Data Out:** Transmits 12-bit Sniffer data to Controller.
  * **Power:** Receives 3.3V_ENIG via the Controller pass-through for all backplane CPLDs.
* **Encoder Interconnects:** 3x 12-pin high-density Hirose DF40 "Press-Fit" connectors for the Keyboard, Lampboard, and Plugboard cable harnesses.
* **Reflector Interconnect:** 12-pin high-density Hirose DF40 "Press-Fit" connector for the Reflector Board.

## 4. Interconnects

* **Routing:** Flat Flexible Cable (FFC) secured to the chassis floor with conductive EMI tape for the Interconnects.
