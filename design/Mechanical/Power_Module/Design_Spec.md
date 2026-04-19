# Power Module Mechanical Design Specification

**Status:** Draft
**Project:** Enigma-NG
**Author:** Izzyonstage & GitHub Copilot
**Version:** v1.0.0
**Associated Hardware Revision:** Rev A
**Last Updated:** 2026-04-14

## 1. Form Factor

* **Geometry:** Dedicated rectangular Power Module PCB mounted in the chassis base and docked to the
  Controller via the 3-way TE board-to-board connector cluster (`J1A/J1B/J1C`).
* **Mounting:** 4x M3 plated mounting holes bonded to chassis ground.
* **Role:** Houses the system power-entry, source-selection, supercap UPS, and 3V3_ENIG generation
  functions; it is not a CM5 carrier board.

## 2. Connectivity

* **Controller Interconnect:** TE **1123684-7** dock headers on the Power Module mate with the
  Controller Board **1-1674231-1** receptacles. `J1A` carries the regulated rails, `J1B` carries the
  Controller-fed `VIN_POE_12V` auxiliary feed, and `J1C` carries low-speed control / telemetry.
* **External I/O:** USB-C receptacle (power only), 5-pin Molex Micro-Fit battery connector, rugged
  panel-mount SW1 power toggle with RGB ring LED, and separate SW2 CM5 power button. The Ethernet /
  PoE RJ45 entry is Controller-owned, not Power-Module-owned.
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
* **Connector keep-out:** Maintain cable bend and mating clearance around USB-C, battery connector,
  and the SW1/SW2 harness entry points, plus the `J1A/J1B/J1C` dock insertion volume.
* **Docked-board clearance:** Preserve the TE dock mating volume and keep components clear of the
  `J1A/J1B/J1C` insertion / extraction envelope.

## 5. Assembly Guidance

* **Order of assembly:** Fit the Power Module to the chassis before engaging the Controller Board onto
  the TE dock cluster.
* **Harnessing:** Route battery, SW1, and SW2 harnesses away from the dock connectors and the supercap
  block to avoid service interference.
* **Cross-check:** Final enclosure dimensions and exact keep-outs must remain aligned with
  `design/Electronics/Power_Module/Board_Layout.md`.

## 6. Cross-References

| Document | Description |
| :--- | :--- |
| `design/Electronics/Power_Module/Design_Spec.md` | Electrical design specification |
