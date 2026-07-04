# Historical Specification: SIGABA Electromechanical Stepping Design
## System Architecture and Control Network Theory

This document provides a highly detailed breakdown of the original United States SIGABA cipher machine (also known as the ECM Mark II by the Navy). It describes how the machine bypassed traditional mechanical odometer-style stepping by using a completely independent electrical control network to actuate its primary cipher rotors.

---

## 1. System Topology and Banking Layout

The SIGABA architecture split its cryptographic and control functions across 15 total code wheels divided into three separate, independent physical banks. Each bank contained 5 rotors:

* **The Cipher Bank (K-Rotors):** 5 interchangeable 26-contact rotors (designated K1 to K5 from right to left). These rotors were solely responsible for the encryption and decryption of the plaintext/ciphertext message signals.
* **The Control Bank (C-Rotors):** 5 interchangeable 26-contact rotors (designated C1 to C5). These rotors encrypted a static input current to output a pseudo-randomised electrical control pattern on every single keystroke.
* **The Index Bank (I-Rotors):** 5 stationary, smaller code wheels (designated I1 to I5). Unlike the other banks, the Index rotors contained only 10 contacts per side and did not step during operations. Their internal wiring was fixed and served to compress and distribute the control signals.

---

## 2. The Stepping Control Circuit (Signal Flow)

Every time an operator pressed a key on the keyboard, two distinct electrical operations happened simultaneously. Before the plaintext letter was routed through the Cipher Bank, an independent "stepping phase" was initiated:

### 2.1 Input Injection
A continuous 4-wire live power source injected constant electrical current into four specific input pins on the entry side of the Control Bank. These inputs were mapped to non-overlapping paths to guarantee that a live current would always emerge on the output side without causing digital dead-ends or internal short-circuits.

### 2.2 Control-to-Index Permutation
1. The 4 live currents wound their way through the 26-contact wiring matrices of the 5 Control Rotors (C1 to C5), permuting their positions based on the current physical rotation of those wheels.
2. The currents exited the Control Bank on 4 out of 26 possible output terminals.
3. These 26 output terminals were hardwired directly down to the 10 inputs of the stationary Index Bank (I1 to I5).
4. The signals passed through the 10-contact Index matrices, scrambling the paths one final time before emerging on a subset of the 10 final output pins.

### 2.3 The 10-to-4 Wire Grouping Matrix
To translate the 10 potential index output pins into targeted actuation instructions for the cipher rotors, the 10 pins were physically tied together into four distinct output groups, known as **Shift Signal Lines** (~F1~, ~F2~, ~F3~, ~F4~). 

The historical hardwired grouping configuration mapped the 10 output terminals into pairs and triplets:
* **Line ~F1~:** Connected to Index Output Pins **9** and **1**
* **Line ~F2~:** Connected to Index Output Pins **8**, **2**, and **3**
* **Line ~F3~:** Connected to Index Output Pins **7** and **4**
* **Line ~F4~:** Connected to Index Output Pins **6**, **5**, and **0**

Because 4 active lines were injected at the start of the control network, the combined configuration meant that anywhere from **one to four** of these ~Fn~ Shift Lines would carry a high electrical voltage (logic 1) on any single keystroke.

---

## 3. Electromechanical Actuator Interfacing

SIGABA rejected the rigid mechanical pawl-and-ratchet "odometer" systems seen in the German Enigma. Instead, it utilized an electromechanical system driven by switching electromagnets (solenoids) paired with a continuously running internal motor.

### 3.1 Cipher Rotor Assignment Truth Table
The four master Shift Signal Lines (~F1~ through ~F4~) directly dictated the movement of four out of the five Cipher Rotors. The middle cipher rotor (~K3~) had no independent shift line; it relied on combined circuit density logic.

| Active Shift Line | Target Actuator | Historical Cipher Rotor Actuated |
| :--- | :--- | :--- |
| **~F1~ is HIGH** | Electromagnet 1 | Steps **K1** (Far Right / Fastest Cipher Rotor) |
| **~F2~ is HIGH** | Electromagnet 2 | Steps **K2** (Inner Right Cipher Rotor) |
| **~F3~ is HIGH** | Electromagnet 4 | Steps **K4** (Inner Left Cipher Rotor) |
| **~F4~ is HIGH** | Electromagnet 5 | Steps **K5** (Far Left / Slowest Cipher Rotor) |

### 3.2 Middle Rotor (~K3~) Parity Logic
The electromagnet for the middle cipher rotor (~K3~) was wired directly to the auxiliary contacts of the other magnets. It triggered if **more than one** of the primary shift lines carried a high signal simultaneously, or if specific patterns were met. 

Mathematically, its activation condition followed a boolean population weight (Hamming density) check:
~Solenoid_3 = (F1 AND F2) OR (F3 AND F4) OR (F1 AND F4)~

---

## 4. Physical Stepping Execution (The Mechanical Step)

When the logic resolved, the physical advancement of a triggered cipher rotor occurred via a distinct, 5-step electromechanical sequence:

1. **The Electrical Pulse:** Current from an activated Shift Line was delivered to the switching electromagnet associated with that specific rotor.
2. **Tripping the Latch:** When energized, the electromagnet pulled a magnetic armature downward against a heavy mechanical return spring. This movement rotated a small physical latch out of its resting position.
3. **Engaging the Drive Pawl:** Releasing the latch allowed a spring-loaded driving pawl to drop forward into the mechanical drive path.
4. **Motor-Driven Advancement:** SIGABA housed an internal electric motor that continuously drove a heavy mechanical bar back and forth. If a pawl had been dropped by its magnet, the moving bar caught that specific pawl on its stroke, pushing it forward.
5. **Advancing the Code Wheel Gear:** The driven pawl engaged a tooth on the code wheel's perimeter gear, physically rotating the entire cipher rotor precisely **one step forward**. 

If an electromagnet received no current during a keystroke, its latch remained locked, the drive pawl was held clear of the moving motor bar, and that specific cipher rotor remained completely stationary.

---
### End of Historical Specification
