# Mechanical Design Requirements

**Status:** Draft
**Version:** v1.0.0
**Associated Hardware Revision:** Rev A
**Last Updated:** 2026-03-30

## 1. Form Factor

* **Geometry:** Rectangular Controller Board designed to sit flush in front of the rotor stack.
* **Mounting:** 4x M3 Plated Mounting Holes (Chassis GND) for high-torque retention.

## 2. Connectivity

* **Mating:** Flush-edge 40-pin Samtec ERF8-020-05.0-S-DV-K-TR female socket (40-pin 2×20, 0.8mm pitch).
* **Retention:** Slotted Through-Hole Reflow (THR) clips for high shear strength.
* **I/O Stack:** Vertical "No-Cross" stack on the Right Edge (HDMI, USB, RJ45).

## 3. Thermal Management & Electrical Bonding

* **Cooling:** Internal copper heatsink (VIPPO) for the eFuse, sinking into L2/L5 planes.
* **Airflow:** Designed for 3D-printed prototype cooling with future metal chassis EMI gaskets.
* **Thermal Cage:** Type VII Hex-Matrix vias must be placed exactly at the 45-degree intersections of the Exposed ENIG mesh for optimal vertical heat transfer.
* **Chassis Bond:** M3 Mounting Holes (PTH) must use a 'Star-Burst' radial copper pattern (8 spokes) to provide mechanical flex during high-torque (0.8 Nm) sealing.
* **Alignment:** V-Score 'TRENNLINIE' [Cut Line] must be inspected for 0.5mm copper pullback before snapping.

## 4. Component Clearances

* **Logic Zone:** Max component height 5.0mm (All SMT).
* **Power Zone:** 42mm clearance for Supercap Block.
* **Rib Keep-out:** Zero components permitted in the descent path of the Aluminium ribs.

## 5. Assembly Torque Protocol

* **Pattern:** Star-Pattern (1-4) using M3 PTH bonded to GND_CHASSIS.
* **Pass 1:** Finger-tight.
* **Pass 2:** 0.4 Nm (Seating).
* **Pass 3:** 0.8 Nm (Final Seal).
