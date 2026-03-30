# Encoder Module (V1.0) Design Specification

A high-performance 64-node interface board.
Unlike static expanders, this module uses dual Altera MAX II CPLDs to handle real-time reciprocal encryption for the plugboard and de-bouncing for the 64-key QWERTY keyboard.

## 1. Power Requirements

* **Core:** 3.3V (Logic) & 1.8V (Internal) if required by CPLD variant.
* **Filtering:** Dedicated 0.1µF X7R decoupling per VCC pin.
* **Protection:** AP22652 current-limited 3.3V rail from the Controller Board.

## 2. Dual-Role Architecture

* **Logic:** 2x [Intel EPM240T100C5N](https://uk.rs-online.com/web/p/cplds/6244278) MAX II CPLDs.
* **I/O Capacity:** Each CPLD provides 80 User I/O pins in a 100-pin TQFP package.
* **Roles:**
  * **HID Mode:**
    * **Keyboard:** Maps 64 mechanical plungers to the parallel data bus.
    * **Lightboard:** Maps parallel return data bus to the Lightboard (Lampboard) and CM5 for GUI feedback.
  * **Plugboard Mode:** Maps 64 "Stecker" jacks for reciprocal encryption.

## 3. Interconnects

* **Data Link:** 12-pin high-density Hirose DF40 "Press-Fit" connector.
* **Routing:** Flat Flexible Cable (FFC) secured to the chassis floor with conductive EMI tape from the Stator Board.
* **Cornering:** 2.0mm Filleted PCB corners for enclosure fit.

## 4. Aesthetics

* **Silkscreen:** Bilingual German/English typewriter font.
* **Branding:** Inverted V1.0 Data Plate with Enigma Silhouette on Bottom (L4).

## 5. JTAG Chain Integrity

* **Buffering:** [74LVC1G125](https://www.ti.com) buffers on the TCK and TMS lines to maintain signal integrity across the long chain (2x I/O CPLDs + 30 Rotor FPGAs).
* **Termination:** 47Ω series resistors on the JTAG data lines to prevent reflections.
* **Chain Position:** The I/O CPLDs sit at the start of the JTAG chain, followed by the 30 Rotor FPGAs.
* **Programming:** Allows for "In-System Sources and Probes" debugging via the CM5 GUI.

## 6. Key Mapping (64-Way QWERTY for Keyboard)

* **Layout:** Standard QWERTY + Numbers + Symbols + Shift.
* **Debouncing:** Digital de-bounce implemented in the CPLD VHDL/Verilog, eliminating mechanical "key chatter."
* **Implementation:** The Shift keys (Left/Right) act as logic-level triggers for the CPLD state machine.
* **LED Drive:** CPLDs directly drive the **Shift Status LEDs** and the 64-character lamp matrix (via MOSFET arrays).

## 7. Plugboard Jack-Sensing

* **Logic:** The CPLD monitors 64 "Interrupt" lines from the Jack-Sensing sockets.
* **Latency:** Sub-microsecond detection of "Stecker" cable insertion, updating the internal encryption matrix instantly.

## 8. Thermal & ESD

* **ESD:** TPD4E001 arrays near the JTAG and Micro-Fit headers.
* **Thermal:** Vias under the EPM240 "PowerPad" (if applicable) for heat dissipation.

## 9. BOM (Key Components)

* **Logic:** 2x Altera EPM240T100.
* **Voltage Reg:** [TLV755P](https://www.ti.com) (Low-dropout regulator for CPLD core).
* **Switches:** Mechanical "Clicky" switches (e.g., Cherry MX) for the Keyboard mode.
* **Sockets:** 3.5mm or 4mm Jack-Sensing sockets for Plugboard mode.

## 10. PCB Specs (JLCPCB)

* **Layers:** 4-Layer (JLC04161H-7628).
* **Finish:** ENIG (Gold) for TQFP-100 pads.
* **Aesthetics:** Dark Green Solder Mask; Typewriter font (ALL-CAPS GERMAN).
* **Chip Placement:** CPLD #1 (Left-side 32 keys) and CPLD #2 (Right-side 32 keys) placed on the rear of the board to allow keys/lamps/sockets on the front.
