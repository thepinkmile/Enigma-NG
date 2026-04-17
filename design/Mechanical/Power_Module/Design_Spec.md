# Power Module Mechanical Design Specification

**Status:** Draft
**Project:** Enigma-NG
**Author:** Izzyonstage & GitHub Copilot
**Version:** v1.0.0
**Associated Hardware Revision:** Rev A
**Last Updated:** 2026-04-14

## 1. Form Factor

* **Geometry:** Dedicated rectangular Power Module PCB mounted in the chassis base and stacked to the
  Controller via the 80-pin Link-Alpha board-to-board connector.
* **Mounting:** 4x M3 plated mounting holes bonded to chassis ground.
* **Role:** Houses the system power-entry, source-selection, supercap UPS, and 3V3_ENIG generation
  functions; it is not a CM5 carrier board.

## 2. Connectivity

* **Controller Interconnect:** Samtec **ERM8-040-05.0-S-DV-K-TR** 80-pin male board-to-board header
  (Link-Alpha) mating to the Controller Board ERF8-040 female socket.
* **External I/O:** RJ45 (PoE/data), USB-C receptacle (power only), 5-pin Molex Micro-Fit battery
  connector, rugged panel-mount SW1 power toggle with RGB ring LED, and separate SW2 CM5 power button.
* **Service Access:** External connectors and switch/button harness terminations must remain accessible
  from the enclosure perimeter without removing the Controller Board.

## 3. Thermal Management & Electrical Bonding

* **High-current area:** The eFuse, dual buck regulators, OR-ing FETs, and supercap manager require
  copper area and via stitching per the electrical design and board layout documents.
* **Airflow:** Provide free air volume above the supercap bank and the main power stage; avoid placing
  enclosure ribs or brackets directly over the hottest power components.
* **Chassis Bond:** Mounting holes provide the primary chassis-ground bond and mechanical retention.

## 4. Component Clearances

* **Supercap keep-out:** Reserve vertical clearance for the 8-cell 2S4P supercap block and its assembly
  tolerances.
* **Connector keep-out:** Maintain cable bend and mating clearance around RJ45, USB-C, battery
  connector, and the SW1/SW2 harness entry points.
* **Stacked-board clearance:** Preserve the 5.0 mm Samtec stack height and keep components clear of the
  Link-Alpha mating volume.

## 5. Assembly Guidance

* **Order of assembly:** Fit the Power Module to the chassis before engaging the Controller Board onto
  Link-Alpha.
* **Harnessing:** Route battery, SW1, and SW2 harnesses away from the BtB connector and the supercap
  block to avoid service interference.
* **Cross-check:** Final enclosure dimensions and exact keep-outs must remain aligned with
  `design/Electronics/Power_Module/Board_Layout.md`.

## 6. Cross-References

| Document | Description |
| :--- | :--- |
| `design/Electronics/Power_Module/Design_Spec.md` | Electrical design specification |
