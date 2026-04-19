# Power Module: Board Layout Visualisations

**Status:** Draft
**Project:** Enigma-NG
**Author:** Izzyonstage & GitHub Copilot
**Version:** v1.0.0
**Associated Hardware Revision:** Rev A
**Last Updated:** 2026-04-19

---

## 1. Functional Role

The Power Module is no longer the system I/O edge board. It is now a removable power cartridge that:

- accepts **local USB-C PD input**
- accepts **local smart-battery input**
- accepts a **regulated PoE-derived auxiliary feed** from the Controller
- ORs / filters / protects those inputs
- generates `5V_MAIN` and `3V3_ENIG`
- provides supercap-backed hold-up and direct `PWR_BUT` / `PWR_GD` support

The RJ45, Ethernet ESD, magnetics, and PoE PD / ACF front-end now live on the Controller.

---

## 2. Edge / Bulkhead Zones

```text
TOP VIEW

 [USB-C] [BATT] [J1A] [J1B] [J1C]

 USB-C   battery   regulated rails   PoE aux   low-speed control
 local   local     to Controller     from Ctrl to Controller
```

- **J1A:** regulated `5V_MAIN` / `3V3_ENIG` / `GND`
- **J1B:** `VIN_POE_12V` + `GND` from the Controller PoE front-end
- **J1C:** `I2C1_SDA`, `I2C1_SCL`, `PM_IO_INT_N`, `PWR_GD`, `ROTOR_EN`, `PWR_BUT`, guarded by `GND`

All three dock connectors use the same TE family:

- Controller side: `1-1674231-1`
- Power Module side: `1123684-7`

---

## 3. Power Flow

```text
Controller J1B VIN_POE_12V ----.
USB-C PD (local) --------------+--> OR-ing --> EMI filter --> eFuse --> 5V buck --> 5V_MAIN
Battery (local) ---------------'                                   \-> LDO -> 3V3_ENIG

5V_MAIN / 3V3_ENIG -> J1A -> Controller
```

The PM remains the sole board that bonds `GND` to `GND_CHASSIS` at the clean/dirty boundary before the
eFuse.

---

## 4. SW1 RGB Control Block

```text
pre-boot hardware path:
MIC1555 U11 -> Q4 -> D6/D7 -> Red + Green only  -> orange flash

runtime path:
PCA9534A U16 -> Rgates -> Q6/Q7/Q8 -> R/G/B cathodes
                         ^
                    SW_LED_CTRL output
```

- **D6 / D7** isolate the hardware boot path on the **red and green channels only**
- **blue** is runtime-only and is not part of the hardware flash path
- **Q6 / Q7 / Q8** are the full runtime RGB low-side sink stages
- **U16 (`PCA9534APWR`, 0x3F)** handles:
  - inputs: `POE_STAT`, `SYS_FAULT`, `BATT_PRES_N`, `USB_STAT`
  - outputs: `SW_LED_R`, `SW_LED_G`, `SW_LED_B`, `SW_LED_CTRL`

`PWR_GD`, `ROTOR_EN`, and `PWR_BUT` remain direct signals on J1C.

---

## 5. Major Placement Areas

```text
 ______________________________________________________________________
| [ USB-C ] [ BATT ] [ J1A ][ J1B ][ J1C ]                            |
|----------------------------------------------------------------------|
| [ OR-ing FETs / controllers ]  [ EMI filters ]  [ TPS259804 eFuse ] |
|----------------------------------------------------------------------|
| [ dual 5V buck ] [ TPS75733 ] [ U16 PM expander ] [ supervisor ]    |
|----------------------------------------------------------------------|
| [ LTC3350 ] [ supercap bank 2S4P ] [ switch spade tabs / test pads ] |
|______________________________________________________________________|
```

The controller-dock connectors replace the former single 80-pin Samtec link and can now be positioned
to suit service clearance rather than blind-mate dual-board insertion constraints.

---

## 6. Notes for Schematic / PCB Capture

1. Keep the `VIN_POE_12V` path electrically separate from the local USB-C and battery entries until the
   intended OR-ing node.
2. Keep `PM_IO_INT_N` routed as a clean low-speed logic net back to the Controller.
3. Reuse the Settings Board RGB sink-stage pattern on the PM:
   - `BSS138`
   - `1kΩ` gate resistor per colour
   - gate pull-down resistor per colour
4. Do not recreate any local RJ45 or Ethernet LED circuitry on the Power Module.
