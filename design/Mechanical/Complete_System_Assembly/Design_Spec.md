# Complete System Assembly — Mechanical Design Specification

**Status:** Stub — pending detailed mechanical design
**Project:** Enigma-NG
**Author:** Izzyonstage & GitHub Copilot
**Version:** v0.1.0
**Associated Hardware Revision:** Rev A
**Last Updated:** 2026-04-14

## Overview

The complete system assembly brings together all Enigma-NG sub-assemblies into the finished machine.
This document will serve as the top-level mechanical reference for maintenance and user assembly guides.
Content to be populated during detailed mechanical design phase.

## Sub-Assembly Index

| Sub-Assembly | Description |
| :--- | :--- |
| `Main_Enclosure/Design_Spec.md` | Main enclosure, Controller Board, Stator Board, rotor stack |
| `Rotor_Actuation_Assembly/Design_Spec.md` | Depression bar, pivot lever, actuation arm, sprung retention bar |
| `Rotor/Design_Spec.md` | Individual rotor module (shroud, bearings, encoder slots) |
| `HID_Assembly/Design_Spec.md` | Keyboard panel, lightboard panel, Encoder PCB |
| `Plugboard_Assembly/Design_Spec.md` | Plugboard jack panel, Encoder PCBs, patch cables |
| `Power_Module/Design_Spec.md` | Power Module standalone sub-assembly |
| `Extension/Design_Spec.md` | Extension board sub-assembly |
| `Reflector/Design_Spec.md` | Reflector sub-assembly |

## Notes

* The **JTAG Daughterboard (JDB)** is a PCB hat that mounts directly on the Controller Board. It has
  no independent mechanical assembly — it is installed as part of the Main Enclosure assembly step
  for the Controller Board. See `design/Electronics/JTAG_Daughterboard/Design_Spec.md` for
  electrical details.

## Cross-References

| Document | Description |
| :--- | :--- |
| `design/Guides/Maintenance_Guide.md` | Maintenance procedures referencing assembly steps |
| `design/Guides/User_Manual.md` | User-facing assembly and operation guide |
