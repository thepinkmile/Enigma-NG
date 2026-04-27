# Actuation Module Board Layout Visualisation

**Status:** Draft
**Project:** Enigma-NG
**Author:** Izzyonstage & GitHub Copilot
**Version:** v.0.1.0
**Associated Hardware Revision:** Rev A
**Last Updated:** 2026-04-26

## 1. Placement Intent

```text
TOP VIEW (L1 / component side / enclosed side; intended to mount upside-down from host board)
 ____________________________________
|           [J1 POWER DOCK]          |
|                                    |
| [D1] <-- edge-visible status LEDs  |
| [D2]                               |
| [D3]    [ U1 LOCAL CONTROLLER ]    |
|        [C2][C3][C4] [C1][R4][C5]   |
|                                    |
|             [J2 TRIGGER]           |
|____________________________________|
```

```text
BOTTOM VIEW (L4 / header-maintenance side / exterior face)
 ____________________________________
|                       [DATA-PLATE] |
| [J3 SERVO LOOM]                    |
|                           [J5 SWD] |
|                                    |
|                     [J6 UART/BOOT] |
|                         [SW1 NRST] |
|                        [SW2 BOOT0] |
| [J4 HOME LOOM]                     |
|____________________________________|
```

## 2. Layout Notes

* J1 and J2 sit on opposite sides of the module so the host power and trigger docks can be kept
  mechanically separate, as agreed for serviceability.
* J3 and J4 are bottom-edge manual-fit Dupont-style headers. They are intentionally excluded from the
  automated PCBA flow.
* J5 and J6 are manual-fit service headers. J5 is the primary SWD header and J6 is the separate
  UART/bootloader header; place them near U1, keep them adjacent, and keep both accessible before the
  module is installed on its host board. SW1 and SW2 should sit directly beside J6 so the two-button
  UART bootloader action (`BOOT0` held while reset is pressed) can be done directly at the AM.
* The upside-down mounting is driven by the single-side PCBA rule: the Samtec docks are assembled on the
  enclosed connector-facing side, while the manually fitted loom / service headers stay on the opposite
  side for post-PCBA fitting and service access.
* D1-D3 should stay on the PCBA-fitted side but be pushed to a visible board edge so the indicators can
  still be seen during maintenance without moving them onto the manual-fit side.
* The `ACTUATION_HOME` loom on J4 should use a twisted pair for pins 1-2 (`ACTUATION_HOME` + `GND`)
  because the loom is expected to run near the servo wiring.
* U1, C1, and R4 should stay close to J4 so the home input is biased and filtered at the module edge.
  J5, J6, SW1, and SW2 should also stay close to U1 so the SWD, UART, `BOOT0`, and `NRST` service
  lines remain short and unambiguous.
* C2-C3 should sit tight to the STM32 supply pins as local high-frequency decouplers. C4 should sit near
  the local `3V3_ENIG` entry / U1 supply region. C5 should sit near the `5V_MAIN` intake and servo loom
  region so the AM has a local short-burst current reservoir when the servo moves.
* C6 (100 nF NRST filter cap) shall be placed adjacent to U1's NRST pin. Keep the trace from U1 NRST to
  C6 and from C6 to GND as short as practicable to maximise noise suppression effectiveness.
* R5 (10 kΩ BOOT0 series protection resistor) shall be placed on the signal path between the SW2 / J6-pin-5
  shared node and the U1 BOOT0 pin. Place R5 in the J5/J6/SW1/SW2 service-header cluster so the service
  interconnect remains compact.
* Unlike the JDB, the AM is not purely a light logic daughterboard: it has both an MCU and a local servo
  power path. The AM therefore keeps the reduced daughterboard-capacitor approach, but adds an explicit
  5V local reservoir cap rather than relying only on upstream host-board bulk capacitance.
* The repo-local Samtec ERM8 / ERF8 drawing extracts now decode the active dock parts
  `ERM8-005-05.0-S-DV-K-TR` and `ERF8-005-05.0-S-DV-K-TR` as the `05.0` lead-style variant. Keep the
  enclosed-side AM fitted parts low profile regardless: the reviewed STM32G071K8T3TR LQFP32 package is
  1.60 mm max height and the 0402 passives / LEDs are substantially lower. Any future enclosed-side
  fitted parts must still remain within the 2.0 mm installed-height rule from `Design_Spec.md`.
* The module is electrically light and mechanically non-load-bearing; the servo must not transfer
  structural load into the AM PCB or its Samtec docks.
