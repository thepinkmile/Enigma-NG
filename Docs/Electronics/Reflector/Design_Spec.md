# Reflector Board (V1.0) Design Specification

## 1. System Role: The "Turnaround"

The Reflector Board sits at the far end of the 30-rotor stack. Its primary role is to receive the signals from the final rotor and return them back through the stack via a different electrical path.

* **Logic Type:** Passive (Loopback).
* **Routing Logic:** All signal mapping is handled remotely by the **EPM240 CPLD** located on the Stator Board.
* **Signal Path:** Rotor 30 Out → Reflector Contacts → 60-pin FPC → Stator CPLD → 60-pin FPC → Reflector Contacts → Rotor 30 In.

## 2. Connectivity & Interconnect

* **The Interface:** 1x 60-pin High-Density **Hirose DF40** "Press-Fit" connector.
* **Secure Mounting:** Features **metal reinforcement tabs** soldered to GND_CHASSIS for industrial-grade retention.
* **The Cable:** 60-way Shielded **Flex-PCB (FPC)**, secured to the machine floor with conductive EMI tape.

## 3. Diagnostic & Monitoring

To ensure the signal has successfully navigated the 30-rotor stack, a dedicated monitoring bank is included.

* **Bank Configuration:** 2x8 Gold-plated (ENIG) Diagnostic Probe Bank.
* **Standard:** Matches the **Controller Board** 2.54mm (0.1") pitch standard for unified system debugging.
* **Labelling:** `REFLEKTOR-DIAGNOSE [Reflector Diag]` in ALL-CAPS German typewriter font.

## 4. PCB & Mechanical Specs

* **Stackup:** 2-Layer / 1oz Copper.
* **Contacts:** 26x Gold-plated friction pads matching the Rotor Module pitch.
* **Fillets:** 2.0mm Rounded PCB corners for consistent "Museum-Grade" enclosure fit.
* **Routing:** Global **0.5mm Fixed-Radius Circular Arcs** for all loopback traces.

## 5. Branding & Traceability

* **Data Plate:** Inverted white silkscreen "Data Plate" on Bottom (L2) containing the Enigma silhouette, "ENIGMA-NG" text, and JLC Serial Number block.
* **Label:** `REFLEKTOR-EINHEIT [Reflector Unit]` in ALL-CAPS German typewriter font.
