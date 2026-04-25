# Settings Board V1.0 Layout & Pinout

**Status:** Draft
**Project:** Enigma-NG
**Author:** Izzyonstage & GitHub Copilot
**Version:** v1.0.0
**Associated Hardware Revision:** Rev A
**Last Updated:** 2026-04-20

---

## 1. Board Overview

The Settings Board is a landscape-orientation panel-mount PCB. The switch bodies mount through the
enclosure top-face panel cutouts, while the PCB sits directly behind the panel and connects back to
the Stator via a 6-wire harness on `J1`.

The active architecture is:

- `U1` (`MCP23017 @ 0x23`) reads all toggle-switch states plus `CFG_APPLY`
- `U2` (`MCP23017 @ 0x24`) drives the 5 Bank 1 LED anodes plus the Bank 1 RGB rails
- `U3` (`MCP23017 @ 0x25`) drives the 7 Bank 2 LED anodes plus the Bank 2 RGB rails
- `Q1/G/B` and `Q4/G/B` provide the shared low-side colour rails under CM5 control

All three LED colour channels are routed and driven; CM5 selects the active bank colour according to
mode or status state.

```text
TOP EDGE / ENCLOSURE PANEL FACE

  [SW_B1_EN] [SW_B1_0] [SW_B1_1] [SW_B1_2] [SW_B1_3]   [SW_B2_EN] [SW_B2_0] [SW_B2_1] [SW_B2_2] [SW_B2_3] [SW_B2_4] [SW_B2_5] [CFG]
      |          |         |         |         |            |          |         |         |         |         |         |        |
   [LED]      [LED]     [LED]     [LED]     [LED]        [LED]      [LED]     [LED]     [LED]     [LED]     [LED]     [LED]   [PB]

   J1        U1 (0x23)          U2 (0x24)          U3 (0x25)       Q1/G/B Q4/G/B
   left edge        centre-left                 centre                     centre-right             right edge
```

---

## 2. Placement Zones

- **Top edge:** 12 toggle switches, 12 indicator LEDs, and the `SW11` actuator position
- **Left edge:** `J1` 6-pin JST PH connector, cable exit toward Stator `J13`
- **Centre-left:** `U1`, switch pull-downs, `R11`, `C4`
- **Centre / centre-right:** `U2` and `U3`, LED series resistors, and anode-routing fanout
- **Right edge:** 6 RGB BSS138 rail transistors with adjacent gate resistors

---

## 3. J1 — Stator Harness Connector

**Connector:** `B6B-PH-K-S(LF)(SN)` — 6-pin JST PH 2.0mm, vertical THT  
**Mating connector:** Stator `J13`  
**Cable:** 6-wire harness, 100mm recommended

| Pin | Signal | Notes |
| :--- | :--- | :--- |
| 1 | `3V3_ENIG` | Logic supply for the three MCP23017 devices |
| 2 | `5V_MAIN` | Indicator power feed from the Controller via Stator `J13` / `J11` |
| 3 | `GND` | Logic return only; no local GND_CHASSIS bond |
| 4 | `SDA` | Shared I2C-1 data |
| 5 | `SCL` | Shared I2C-1 clock |
| 6 | `GND` | Indicator-current return paired with pin 2 |

> Use 28AWG for pins 2 and 6, and 30AWG for pins 1, 3, 4, and 5.

---

## 4. U1 — MCP23017 @ 0x23

**Package:** SOIC-28  
**Role:** Reads Bank 1, Bank 2, and `CFG_APPLY`

| Port | Pin | Signal | Direction | Pull | Description |
| :--- | :--- | :--- | :--- | :--- | :--- |
| GPA | [0] | `SW_B1_EN` | Input | 10k pull-down | Bank 1 enable |
| GPA | [1] | `SW_B1[0]` | Input | 10k pull-down | Bank 1 config bit 0 |
| GPA | [2] | `SW_B1[1]` | Input | 10k pull-down | Bank 1 config bit 1 |
| GPA | [3] | `SW_B1[2]` | Input | 10k pull-down | Bank 1 config bit 2 |
| GPA | [4] | `SW_B1[3]` | Input | 10k pull-down | Bank 1 config bit 3 |
| GPA | [5:7] | — | — | — | Spare |
| GPB | [0] | `SW_B2_EN` | Input | 10k pull-down | Bank 2 enable |
| GPB | [1] | `SW_B2[0]` | Input | 10k pull-down | Bank 2 config bit 0 |
| GPB | [2] | `SW_B2[1]` | Input | 10k pull-down | Bank 2 config bit 1 |
| GPB | [3] | `SW_B2[2]` | Input | 10k pull-down | Bank 2 config bit 2 |
| GPB | [4] | `SW_B2[3]` | Input | 10k pull-down | Bank 2 config bit 3 |
| GPB | [5] | `SW_B2[4]` | Input | 10k pull-down | Bank 2 config bit 4 |
| GPB | [6] | `SW_B2[5]` | Input | 10k pull-down | Bank 2 config bit 5 |
| GPB | [7] | `CFG_APPLY` | Input | 10k pull-up | Active-low momentary pushbutton |

---

## 5. LED Drive Expanders

### 5.1 U2 — MCP23017 @ 0x24

| Port | Pin | Signal | Direction | Description |
| :--- | :--- | :--- | :--- | :--- |
| GPA | [0] | `LED_B1_EN_A` | Output | Bank 1 enable LED anode |
| GPA | [1] | `LED_B1_0_A` | Output | Bank 1 bit 0 LED anode |
| GPA | [2] | `LED_B1_1_A` | Output | Bank 1 bit 1 LED anode |
| GPA | [3] | `LED_B1_2_A` | Output | Bank 1 bit 2 LED anode |
| GPA | [4] | `LED_B1_3_A` | Output | Bank 1 bit 3 LED anode |
| GPA | [5] | `BNK1_R` | Output | Drives `Q1` gate |
| GPA | [6] | `BNK1_G` | Output | Drives `Q2` gate |
| GPA | [7] | `BNK1_B` | Output | Drives `Q3` gate |
| GPB | [7:0] | — | — | Spare |

### 5.2 U3 — MCP23017 @ 0x25

| Port | Pin | Signal | Direction | Description |
| :--- | :--- | :--- | :--- | :--- |
| GPA | [0] | `LED_B2_EN_A` | Output | Bank 2 enable LED anode |
| GPA | [1] | `LED_B2_0_A` | Output | Bank 2 bit 0 LED anode |
| GPA | [2] | `LED_B2_1_A` | Output | Bank 2 bit 1 LED anode |
| GPA | [3] | `LED_B2_2_A` | Output | Bank 2 bit 2 LED anode |
| GPA | [4] | `LED_B2_3_A` | Output | Bank 2 bit 3 LED anode |
| GPA | [5] | `LED_B2_4_A` | Output | Bank 2 bit 4 LED anode |
| GPA | [6] | `LED_B2_5_A` | Output | Bank 2 bit 5 LED anode |
| GPA | [7] | `BNK2_R` | Output | Drives `Q4` gate |
| GPB | [0] | `BNK2_G` | Output | Drives `Q5` gate |
| GPB | [1] | `BNK2_B` | Output | Drives `Q6` gate |
| GPB | [2:7] | — | — | Spare |

---

## 6. LED Colour-Rail Topology

Each indicator LED is common-anode and uses one individually switched anode from `U2` or
`U3` plus three shared cathode rails per bank (red, green, blue).

| Transistor | Gate source | Function |
| :--- | :--- | :--- |
| `Q1` | `U2.GPA[5]` via `R12` | Pull Bank 1 red rail low |
| `Q2` | `U2.GPA[6]` via `R13` | Pull Bank 1 green rail low |
| `Q3` | `U2.GPA[7]` via `R14` | Pull Bank 1 blue rail low |
| `Q4` | `U3.GPA[7]` via `R15` | Pull Bank 2 red rail low |
| `Q5` | `U3.GPB[0]` via `R16` | Pull Bank 2 green rail low |
| `Q6` | `U3.GPB[1]` via `R17` | Pull Bank 2 blue rail low |

CM5 firmware normally selects one colour rail per bank at a time:

- **Green** = switch-defined configuration
- **Red** = CM5-defined override

---

## 7. Switch / LED Mapping

| Physical control | Switch input | LED anode output | Bank colour rail source |
| :--- | :--- | :--- | :--- |
| `SW_B1_EN` | `U1.GPA[0]` | `U2.GPA[0]` | `U2.GPA[5:7]` |
| `SW_B1[0]` | `U1.GPA[1]` | `U2.GPA[1]` | `U2.GPA[5:7]` |
| `SW_B1[1]` | `U1.GPA[2]` | `U2.GPA[2]` | `U2.GPA[5:7]` |
| `SW_B1[2]` | `U1.GPA[3]` | `U2.GPA[3]` | `U2.GPA[5:7]` |
| `SW_B1[3]` | `U1.GPA[4]` | `U2.GPA[4]` | `U2.GPA[5:7]` |
| `SW_B2_EN` | `U1.GPB[0]` | `U3.GPA[0]` | `U3.GPA[7]` / `GPB[0:1]` |
| `SW_B2[0]` | `U1.GPB[1]` | `U3.GPA[1]` | `U3.GPA[7]` / `GPB[0:1]` |
| `SW_B2[1]` | `U1.GPB[2]` | `U3.GPA[2]` | `U3.GPA[7]` / `GPB[0:1]` |
| `SW_B2[2]` | `U1.GPB[3]` | `U3.GPA[3]` | `U3.GPA[7]` / `GPB[0:1]` |
| `SW_B2[3]` | `U1.GPB[4]` | `U3.GPA[4]` | `U3.GPA[7]` / `GPB[0:1]` |
| `SW_B2[4]` | `U1.GPB[5]` | `U3.GPA[5]` | `U3.GPA[7]` / `GPB[0:1]` |
| `SW_B2[5]` | `U1.GPB[6]` | `U3.GPA[6]` | `U3.GPA[7]` / `GPB[0:1]` |
| `SW11` | `U1.GPB[7]` | — | — |

---

## 8. PCB Stackup & Routing Notes

**Manufacturer:** JLCPCB  
**Layer count:** 4-layer  
**Stackup:** JLC04161H-7628  
**Copper:** 2oz outer  
**Finish:** ENIG

| Layer | Role | Notes |
| :--- | :--- | :--- |
| L1 | Signals + components | Switch inputs, I2C, LED anodes, rail gates |
| L2 | GND plane | Solid reference plane |
| L3 | Power | `3V3_ENIG` and local `5V_MAIN` distribution |
| L4 | Secondary routing + silkscreen | Low-speed routing only |

### 8.1 Routing guidance

- Keep `SDA` / `SCL` as a matched short pair from `J1` to the three expanders
- Route the `5V_MAIN` feed and pin-6 return wider than logic traces
- Place one 100nF decoupler at each MCP23017 supply pin cluster
- Keep gate resistors directly adjacent to the six BSS138 devices

---

## 9. Cross-References

| Document | Description |
| :--- | :--- |
| `design/Electronics/Settings_Board/Design_Spec.md` | Full electrical specification and BOM |
| `design/Electronics/Stator/Design_Spec.md` | `J13` definition and CPLD configuration ownership |
| `design/Electronics/Stator/Board_Layout.md` | Mating connector definition for `J13` |
| `design/Mechanical/Main_Enclosure/Design_Spec.md` | Panel cutout and actuator constraints |
