# Rotor Actuation Assembly — Mechanical Design Specification

**Status:** Draft
**Project:** Enigma-NG
**Author:** Izzyonstage & GitHub Copilot
**Version:** v0.1.0
**Associated Hardware Revision:** Rev A
**Last Updated:** 2026-04-17

---

## 1. Overview

The Rotor Actuation Assembly translates each keypress — whether initiated by a human operator or
by a CM5-generated virtual keypress — into a single, precisely-stepped advance of the rotor stack.
The mechanism is modelled directly on the original Enigma machine's stepping mechanism, preserving
the authentic carry behaviour while accommodating the additional servo actuation path for
autonomous operation.

---

## 2. Depression Bar

A horizontal bar runs across the base of the main enclosure. This bar is the **common activation
point** for both human keypresses and CM5 servo actuation.

* Each keyboard key has a "dangling lever" that contacts the depression bar when the key is
  pressed; the lever pushes the bar downward.
* The CM5 servo arm also contacts the same depression bar, providing an independent actuation
  path for CM5-initiated virtual keypresses.
* The depression bar ensures that regardless of the actuation source (human or servo), the
  downstream stepping mechanism receives a single, consistent input motion.

---

## 3. Keyboard Key Levers

Each of the 40 physical HID keys has a mechanical lever that extends downward from the key body to
contact the depression bar.

* A keypress causes the lever to push the depression bar downward by the actuation stroke
  distance.
* All 40 levers are geometrically identical to ensure uniform actuation force and stroke across
  the keyboard panel.
* Lever geometry must be designed so that the depression bar deflects by the same distance
  regardless of which key (and therefore which lever position) is pressed.

---

## 4. Servo Actuation

The **Miuzei Metal Gearbox 90 servo** (4.8–6V, mounted on the Stator PCB) provides the CM5
actuation path.

* The servo drives an arm that contacts the same depression bar as the keyboard key levers.
* A **0° → 180° → 0° sweep** constitutes one full actuation cycle, equivalent to one keypress
  for rotor stepping purposes.
* The servo arm geometry must be designed so that the mid-stroke depression (at 90°) matches the
  full-actuation depression of a human keypress on the bar.
* The SERVO_HOME position (0°) is detected by the SERVO_HOME switch mounted on the Stator PCB.
  See `design/Electronics/Stator/Design_Spec.md` for servo electrical interface and homing logic.

---

## 5. Pivot Lever and Actuation Arm

The depression bar connects to a **pivot lever** that converts the bar's downward motion into a
single-step advance of the rotor stack.

* The pivot point geometry is designed to produce the correct angular travel of the actuation arm
  for one rotor step, from the available depression bar stroke.
* The **actuation arm** extends from the pivot lever to the rotor stepping ratchet, transferring
  the converted motion to advance the rotor by exactly one position.
* Pivot point location and arm lengths are to be determined during detailed mechanical design to
  match the rotor step angle and available keypress stroke.

---

## 6. Sprung Retention Bar

A spring-loaded retention bar is located at the rear of the rotor stack, acting as a **detent
mechanism**.

* The retention bar engages with the stepping notches machined into each rotor shroud.
* After each actuation, the retention bar ensures the rotor advances to exactly the next full
  step position and does not stop in an intermediate position.
* Spring preload must be sufficient to hold the rotor at rest against any expected disturbance,
  while not resisting the actuation stroke excessively.
* This mechanism is functionally identical to the original Enigma machine's sprung retention
  mechanism.

---

## 7. Carry Mechanism

Rotor carry — the advance of higher-order rotors when a lower-order rotor completes a full
revolution — is **purely mechanical**.

* Carry is triggered by the notch positions machined on each rotor shroud, engaging with the
  carry mechanism of the adjacent higher-order rotor.
* No electronic or software logic is involved in the carry mechanism.
* This is identical in function and principle to the original Enigma machine's carry mechanism.

---

## 8. Cross-References

| Document | Description |
| :--- | :--- |
| `design/Electronics/Stator/Design_Spec.md` | Stator PCB; servo motor mounted here; SERVO_HOME switch |
| `design/Mechanical/Rotor/Design_Spec.md` | Rotor module mechanical specification (shroud, bearings, encoder slots, stepping notches) |
