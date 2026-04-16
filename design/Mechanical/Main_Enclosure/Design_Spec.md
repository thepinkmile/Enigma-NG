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
cutouts for the 12 Settings Board toggle switches, 12 matching RGB indicator LEDs, and 1 CFG_APPLY
pushbutton.

| Feature | Quantity | Location | Notes |
| :--- | :---: | :--- | :--- |
| Toggle switch cutouts (Bank 1 — Plugboard Routing) | 5 | Right side, top face, near rotors | Bank 1 enable + SW_B1[0:3] — panel-mount SPDT toggle |
| Toggle switch cutouts (Bank 2 — Reflector Mapping) | 7 | Right side, top face, near rotors | Bank 2 enable + SW_B2[0:5] — panel-mount SPDT toggle |
| RGB LED apertures (Bank 1 indicators) | 5 | Adjacent to Bank 1 toggles | One 5mm indicator LED per switch position |
| RGB LED apertures (Bank 2 indicators) | 7 | Adjacent to Bank 2 toggles | One 5mm indicator LED per switch position |
| CFG_APPLY pushbutton cutout | 1 | Right side, top face | Momentary pushbutton; triggers CPLD config re-latch |

The Settings Board PCB mounts internally to the enclosure panel, with the toggles, LEDs, and the
pushbutton protruding through their panel cutouts. The board connects to the Stator Board via a
4-wire I²C ribbon cable (SDA, SCL, 3V3_ENIG, GND). Final toggle-hole, LED-hole, and stand-off /
spacer geometry are to be defined at detailed mechanical design phase based on the selected parts.

See `design/Electronics/Settings_Board/Design_Spec.md` for the electrical specification of the
Settings Board.

### Lid Display — Optional Touchscreen Add-on

The machine lid must be designed to accommodate an optional touchscreen display add-on (see DEC-033).
Specific mounting dimensions are deferred pending display size selection (up to 10" supported via DSI1).
The following provisions must be made at detailed mechanical design phase:

| Feature | Notes |
| :--- | :--- |
| Display aperture in lid | Sized for chosen display (TBD — up to 10"); flush-mount or recessed bezel |
| Display mounting frame / bracket | Secures display panel against lid inner face |
| FPC hinge routing | Clear path for DSI1 FPC cable from lid through hinge to Controller Board J_DSI1 |
| Touch controller power | 5V_MAIN + **3V3_ENIG** routed alongside FPC via power cable through hinge |

See `design/Electronics/Controller/Design_Spec.md` (J_DSI1) and `design/Electronics/Settings_Board/Design_Spec.md` for electrical context.

## Cross-References

| Document | Description |
| :--- | :--- |
| `design/Electronics/Controller/Design_Spec.md` | Controller Board electrical specification |
| `design/Electronics/Controller/Design_Spec.md` | Controller Board — DSI1 connector J_DSI1 for lid display |
| `design/Electronics/Stator/Design_Spec.md` | Stator Board electrical specification — includes I²C interface to Settings Board |
| `design/Electronics/Settings_Board/Design_Spec.md` | Settings Board electrical specification — panel switch and LED expanders |
| `design/Mechanical/Complete_System_Assembly/Design_Spec.md` | Complete system assembly including all sub-assemblies |
