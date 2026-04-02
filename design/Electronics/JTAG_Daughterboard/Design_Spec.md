# JTAG Daughterboard (V1.0) Design Specification

A high-speed USB-to-JTAG bridge module that allows the CM5 to natively program the 30-rotor CPLDs and the 4 I/O CPLDs.
This module replicates the functionality of an **Intel (Altera) USB Blaster II** on a tiny daughterboard.

## 1. Core Logic

* **Role:** Converts the CM5's USB 2.0 signals into high-speed JTAG (TCK, TMS, TDI, TDO) commands.
* **Bridge IC:** [FT232H](https://ftdichip.com/wp-content/uploads/2023/09/DS_FT232H.pdf) High-Speed USB 2.0 to MPSSE.
* **Function:** Dedicated JTAG programmer for the global chain (30x Rotor CPLDs + 3x Encoder CPLDs + 1x Stator CPLD).
* **Configuration:** 12MHz crystal-controlled for high-speed programming via the CM5 GUI.
* **Integrated Driver:** Compatible with `OpenOCD` or `Quartus` via a custom Linux driver on the CM5.

## 2. Interface & Wiring

* **USB:** Internal 4-pin header to the Controller Board's USB 2.0 Hub.
* **JTAG Pinout (MPSSE Mode):**
  * AD0 -> **TCK** (Clock)
  * AD1 -> **TDI** (Data In)
  * AD2 -> **TDO** (Data Out)
  * AD3 -> **TMS** (State Machine)
* **Voltage:** 3.3V logic level with 5V-tolerant I/O.

## 3. Aesthetics & Mounting

* **Visibility:** Completely hidden internally.
* **Mounting:** Small 2-layer PCB mounted via 3M VHB tape or standoffs near the Controller.

## 4. Electrical Requirements

* **Voltage:** Powered by the `+3V3_SYSTEM` Logic Rail from the CM5 on the Controller Board.
* **Bulk Entry Bank Rule:** Use **5x 10uF X7R 50V** bulk decoupling capacitors near the USB/power-entry pins in a **Symmetrical Star/Spoke pattern**.
* **Clocking:** Dedicated 24MHz crystal for the FT232H to ensure JTAG clock stability across the 37-device chain.

---

## Bill of Materials

| Ref | Component | Value | Package | Mouser Part # | DigiKey Part # | JLCPCB Part # |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| C1-C4 | Decoupling | 0.1µF | 0402 | 81-GRM155R71A104KE1D | 311-1424-1-ND | C49678 |
| C5-C9 | Bulk entry decoupling bank (star/spoke) | 10uF X7R 50V | 1206 | 187-CL31B106KBHNNNE | 1276-6767-1-ND | CL31B106KBHNNNE |
| J1 | USB header | 4-pin | 2.54mm | 538-22-23-2041 | WM2897-ND | ??? |
| J2 | JTAG header | 10-pin | 2.54mm | 538-22-23-2101 | WM2901-ND | ??? |
| R1, R2 | Series resistors | 22Ω | 0603 | 667-ERJ-3EKF2200V | P22.0BYCT-ND | C25805 |
| U1 | FT232H | USB 2.0 to MPSSE | QFN-56 | 895-FT232HL-REEL | 768-1014-ND | C123467 |
| Y1 | Crystal | 24MHz | HC-49 | 520-ABL-24.000MHZ-B2 | 644-1053-1-ND | C123468 |
