# Rotor Detailed Design

The Enigma-NG uses a 30-rotor stack. Unlike the original mechanical rotors, these are **Smart Digital Rotors** where the internal scrambled wiring is emulated by a dedicated logic chip on each module.
The outer rotating mechanism works like the outer ring of a bearing around the central static ring (this is the rotor PCB and enclosure).
There are also sensors used to detect the current position of the outer ring using a single-track grey encoder.

## Basic Design

### 1. Position Sensing (The "Zero-Wear" System)

* **Sensor:** [AS5600 Magnetic Encoder](https://www.ams-osram.com).
* **Decision:** We avoid mechanical wipers/brushes (the main failure point of original Enigmas) in favour of contactless magnetic sensing.
* **Precision:** 6-bit resolution allows the CM5 to detect if a rotor is "between" characters and flag a mechanical jam.

### 2. Logic & Transposition

* **Logic:** The Altera **EPM240T100C** CPLD emulates the 64x64 cross-wiring.
* **Role:** Performs the instantaneous dual 6-bit parallel transposition (substitution cipher) for the forward and backward signal paths.
* **Memory:** Stores the 26-position wiring table for any historical rotor (I-VIII, Beta, Gamma) selectable via the CM5.
* **Latency:** Sub-10ns transposition time, ensuring the entire 30-rotor "trip" happens well within one CPU clock cycle.
* **Configuration:** CM5 loads the "Rotor Type" (e.g., Rotor I, II, III) into the CPLD's SRAM at boot via the JTAG Chain.

### 3. Mechanical Details

* **Mounting:** Each rotor PCB has two **M2.5 alignment holes**.
* **Retention:** Once slotted into the Stator, a **threaded rod** (mimicking the original Enigma spindle) passes through the center of all 30 rotors to lock them into a single, rigid block.
* **Hot-Swappable:** The Samtec Edge-Rate connectors are rated for high mating cycles, allowing individual rotors to be pulled for "repair" or reconfiguration without tools.

## Rotor Electrical Design Requirements

### 1. Power Management

* **Input:** 3.3V/150mA per rotor (sourced from the Controller Board's **Island C**).
* **Filtering:** Local **Ferrite Beads** and a **10µF X7R** capacitor bank to suppress switching noise from the 30-rotor chain.

### 2. Communication Bus

* **The Data Path:** 12-bit parallel bus (D0-D11) passes through every rotor in a daisy-chain or star-bus configuration.
* **Control:** Shared I2C bus for position telemetry.
* **JTAG:** Pass-through JTAG lines allow the **USB Blaster** on the Controller Board to program the entire 30-rotor stack in one "daisy-chain" operation.

### 3. Signal Integrity

* **Impedance:** 50Ω single-ended traces for the 12-bit data bus to prevent "ringing" across the 30-module length.
* **Shielding:** 4-layer PCB with solid GND planes (L2/L3) to isolate digital switching from the high-accuracy magnetic encoder.

### 4. PCB Fabrication (JLCPCB Specs)

* **Layers:** 4-Layer (JLC04161H-7628).
* **Finish:** ENIG (Gold) for the edge-rate connector pads.
* **Aesthetics:** Dark Green Solder Mask with Typewriter font labeling (e.g., "WALZE I").

### 5. BOM (Key Components per Rotor)

* **Logic:** Altera EPM240T100C.
* **Encoder:** ams-OSRAM AS5600.
* **Connector:** Samtec ERM8 Series (0.8mm Pitch).
* **Passives:** 0402 X7R 10V Capacitors (Minimum 2.5x derating).
