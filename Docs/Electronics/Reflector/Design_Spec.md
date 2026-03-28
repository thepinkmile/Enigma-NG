# Reflector Board (V1.0) Design Specification

## 1. System Role: The "Turnaround"

The Reflector Board sits at the far end of the 30-rotor stack. Its primary role is to receive the 12-bit (or 26-char equivalent) signal from the final rotor and return it back through the stack via a different electrical path.

* **Logic Type:** Passive (Loopback).
* **Routing Logic:** All signal mapping is handled remotely by the **EPM240 CPLD** located on the Stator Board.
* **Signal Path:** Rotor 30 Out → Reflector Contacts → 60-pin FPC → Stator CPLD → 60-pin FPC → Reflector Contacts → Rotor 30 In.

## 2. Connectivity & Interconnect

* **The Interface:** 1x 60-pin High-Density **Hirose DF40** "Press-Fit" connector.
* **Secure Mounting:** The connector features **metal reinforcement tabs** soldered to GND_CHASSIS for industrial-grade retention.
* **The Cable:** 60-way Shielded **Flex-PCB (FPC)**, secured to the machine floor with conductive EMI tape to ensure zero interference with the mechanical rotor pawls.

## 3. PCB & Mechanical Specs

* **Stackup:** 2-Layer / 1oz Copper (Standard).
* **Contacts:** 26x Spring-loaded or gold-plated friction contacts (matching the Rotor Module pitch).
* **Fillets:** 2.0mm Rounded PCB corners to ensure a perfect fit within the mechanical "End-Cap" assembly.
* **Routing:** Global **0.5mm Fixed-Radius Circular Arcs** for all loopback traces.

## 4. Branding & Traceability

* **Data Plate:** Inverted white silkscreen "Data Plate" on Bottom (L2) containing the Enigma silhouette, "ENIGMA-NG" text, and JLC Serial Number block.
* **Label:** `REFLEKTOR-EINHEIT [Reflector Unit]` in ALL-CAPS German typewriter font.
