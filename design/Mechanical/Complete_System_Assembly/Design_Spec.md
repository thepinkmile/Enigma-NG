# Complete System Assembly — Mechanical Design Specification

**Status:** Draft
**Project:** Enigma-NG
**Author:** Izzyonstage & GitHub Copilot
**Version:** v0.2.0
**Associated Hardware Revision:** Rev A
**Last Updated:** 2026-04-14

## Overview

This is the top-level General Assembly document for the Enigma-NG machine. It defines the complete
set of mechanical and electromechanical components that constitute the finished machine and provides
the authoritative assembly sequence guidance for build and maintenance activities.

All sub-assembly details, tolerances, and part-level instructions are contained in the
sub-assembly documents listed in §3. This document provides the integration view: what assembles
where, in what order, and with what dependencies.

## Component Index

The following table lists every component category present in the assembled machine.

| Category | Qty | Description | Sub-Assembly Document |
| :--- | :--- | :--- | :--- |
| Rotors | 30 | Individual rotor modules (shroud, bearings, encoder slots, ERM8 male headers) | `Rotor/Design_Spec.md` |
| Stator Board | 1 | PCB backplane: rotor stack, JTAG hub, encryption routing, I²C expanders, servo | `Stator/Design_Spec.md` (Electronics) |
| Rotor Actuation Assembly | 1 | Depression bar, pivot lever, actuation arm, sprung retention bar, servo motor | `Rotor_Actuation_Assembly/Design_Spec.md` |
| HID Assembly | 1 | Keyboard panel, lightboard panel, HID Encoder PCB | `HID_Assembly/Design_Spec.md` |
| Plugboard Assembly | 1 | Plugboard jack panel, Encoder PCBs (×2), patch cables | `Plugboard_Assembly/Design_Spec.md` |
| Reflector | 1 | Reflector sub-assembly (or internal Stator CPLD reflector map — see SW2) | `Reflector/Design_Spec.md` |
| Extension (optional) | 0–N | Extension board for multi-stack rotor configurations | `Extension/Design_Spec.md` |
| Power Module | 1 | Standalone power supply sub-assembly (LTC3350, eFuse, INA219, supercaps) | `Power_Module/Design_Spec.md` |
| Controller Board | 1 | CM5 carrier board (CM5 module, JDB hat, Link-Alpha/Beta connectors) | `Controller/Design_Spec.md` (Electronics) |
| Main Enclosure | 1 | Chassis, panels, cable routing, EMI bonding, fan | `Main_Enclosure/Design_Spec.md` |
| Servo Motor | 1 | Miuzei Metal Gearbox 90 (5V, 3-pin, PCB-mount on Stator) | `Rotor_Actuation_Assembly/Design_Spec.md` |
| SERVO_HOME Switch | 1 | SPST NO momentary (Omron SS-01GL13), PCB-mount on Stator | `Stator/Design_Spec.md` (Electronics) |
| Settings Board | 1 | Panel-mount configuration switch PCB (12× illuminated RGB rockers + CFG_APPLY button); mounts to right side top face of Main Enclosure; connects to Stator via I²C ribbon | `Settings_Board/Design_Spec.md` (Electronics) |
| Cable Harnesses | TBD | LINK-ALPHA, LINK-BETA, encoder IDC ribbons, reflector cable, fan cable, Settings Board I²C ribbon | Each sub-assembly doc |
| Connectors | TBD | ERF8/ERM8 BtB, JST PH servo, JST SH fan, Molex IDC encoder, etc. | Per sub-assembly BOM |

## Assembly Sequence Overview

The following is the recommended assembly order for a complete machine build. Sub-assembly build
steps are detailed in each referenced document; this section defines integration dependencies only.

| Step | Sub-Assembly | Notes |
| :--- | :--- | :--- |
| 1 | Power Module | Standalone build; test on bench before integration. Delivers 5V_MAIN and 3V3_ENIG. |
| 2 | Stator Board | Install ICs (CPLD, MCP23017 ×3, PCA9685, INA219), passives, connectors. Mount servo + SERVO_HOME switch. Bench-test I²C expanders before stack assembly. |
| 3 | Rotors (×30) | Build all 30 rotor modules. Verify ERM8 header alignment and encoder slot clearance before stacking. |
| 4 | Rotor stack onto Stator | Press Rotor 1 ERM8 headers into Stator ERF8 sockets. Add Rotors 2–30 in sequence. Verify JTAG daisy-chain continuity. |
| 5 | Rotor Actuation Assembly | Install depression bar, pivot lever, actuation arm, sprung retention bar. Connect servo 3-pin JST to Stator J_SERVO. Verify SERVO_HOME switch actuation. |
| 6 | HID Assembly | Build keyboard panel + lightboard panel + HID Encoder PCB. Connect IDC ribbon to Stator J4. |
| 7 | Plugboard Assembly | Build plugboard jack panel + Encoder PCBs. Connect IDC ribbons to Stator J5/J6. |
| 8 | Reflector | Install Reflector sub-assembly. Connect 16-pin Molex cable to Stator J7. (Skip if using Stator CPLD internal reflector via SW2.) |
| 9 | Extension (if used) | Daisy-chain Extension boards between Rotor 30 and Reflector for multi-stack configurations. |
| 10 | Controller Board + JDB Hat | Install JDB hat on Controller. Mount Controller in Main Enclosure. Connect LINK-ALPHA to Power Module (J1). Connect LINK-BETA to Stator (J2/J8). |
| 11 | Settings Board | Mount Settings Board PCB to Main Enclosure right side top panel. Route 4-wire I²C ribbon cable (SDA, SCL, 3V3_ENIG, GND) to Stator J_CFG. Verify switch and LED function via CM5 I²C scan before final panel closure. |
| 12 | Main Enclosure final assembly | Route all cable harnesses. Install panels. Fit fan. Secure EMI bonding. Final torque fasteners. |

> **Note on the JTAG Daughterboard (JDB):** The JDB is a PCB hat that mounts directly on the
> Controller Board. It has no independent mechanical assembly step — it is installed as part of
> Step 10 (Controller Board install) before the Controller is fitted in the Main Enclosure.
> See `design/Electronics/JTAG_Daughterboard/Design_Spec.md` for electrical details.

## Sub-Assembly Reference Table

| Sub-Assembly | Document | Status |
| :--- | :--- | :--- |
| Main Enclosure | `Main_Enclosure/Design_Spec.md` | Draft |
| Rotor Actuation Assembly | `Rotor_Actuation_Assembly/Design_Spec.md` | Draft |
| Rotor | `Rotor/Design_Spec.md` | Draft |
| HID Assembly | `HID_Assembly/Design_Spec.md` | Draft |
| Plugboard Assembly | `Plugboard_Assembly/Design_Spec.md` | Draft |
| Power Module | `Power_Module/Design_Spec.md` | Draft |
| Extension | `Extension/Design_Spec.md` | Draft |
| Reflector | `Reflector/Design_Spec.md` | Draft |
| Settings Board | `design/Electronics/Settings_Board/Design_Spec.md` | Draft |

## Cross-References

| Document | Description |
| :--- | :--- |
| `design/Electronics/Settings_Board/Design_Spec.md` | Settings Board electrical specification — panel switches, LED expanders, I²C interface |
| `design/Electronics/Stator/Design_Spec.md` | Stator Board electrical specification — J_CFG I²C connector to Settings Board |
| `design/Mechanical/Main_Enclosure/Design_Spec.md` | Main Enclosure — Settings Board panel cutout requirements |
| `design/Guides/Maintenance_Guide.md` | Maintenance procedures referencing assembly steps |
| `design/Guides/User_Manual.md` | User-facing assembly and operation guide |
