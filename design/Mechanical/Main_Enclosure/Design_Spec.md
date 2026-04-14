# Main Enclosure Mechanical Design Specification

**Status:** Stub — pending detailed mechanical design
**Project:** Enigma-NG
**Author:** Izzyonstage & GitHub Copilot
**Version:** v0.1.0
**Associated Hardware Revision:** Rev A
**Last Updated:** 2026-04-14

## Overview

Mechanical design specification for the main Enigma-NG enclosure. This encompasses the physical
housing of the Controller Board, Stator Board, rotor stack, keyboard panel, lightboard panel, and
the user-accessible Settings Board panel switches.

Content to be populated during detailed mechanical design phase.

## Panel Cutout Requirements

### Settings Board — Configuration Switch Panel

The right side of the enclosure **top face**, positioned near the rotor stack, must provide panel
cutouts for the 12 illuminated RGB rocker switches and 1 CFG_APPLY pushbutton of the Settings Board.

| Feature | Quantity | Location | Notes |
| :--- | :---: | :--- | :--- |
| Rocker switch cutouts (Bank 1 — Plugboard Routing) | 5 | Right side, top face, near rotors | Bank 1 enable + SW_B1[0:3] — panel-mount SPDT illuminated rocker |
| Rocker switch cutouts (Bank 2 — Reflector Mapping) | 7 | Right side, top face, near rotors | Bank 2 enable + SW_B2[0:5] — panel-mount SPDT illuminated rocker |
| CFG_APPLY pushbutton cutout | 1 | Right side, top face | Momentary pushbutton; triggers CPLD config re-latch |

The Settings Board PCB mounts internally to the enclosure panel, with switches and the pushbutton
protruding through the panel cutouts. The board connects to the Stator Board via a 4-wire I²C
ribbon cable (SDA, SCL, 3V3_ENIG, GND). Panel cutout dimensions and switch bezel clearances are
to be defined at detailed mechanical design phase based on the selected switch part.

See `design/Electronics/Settings_Board/Design_Spec.md` for the electrical specification of the
Settings Board.

## Cross-References

| Document | Description |
| :--- | :--- |
| `design/Electronics/Controller/Design_Spec.md` | Controller Board electrical specification |
| `design/Electronics/Stator/Design_Spec.md` | Stator Board electrical specification — includes I²C interface to Settings Board |
| `design/Electronics/Settings_Board/Design_Spec.md` | Settings Board electrical specification — panel switch and LED expanders |
| `design/Mechanical/Complete_System_Assembly/Design_Spec.md` | Complete system assembly including all sub-assemblies |
