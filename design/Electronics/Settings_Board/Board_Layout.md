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
the Stator via a 6-wire harness on `J_I2C`.

The active architecture is:

- `U_EXP_SW_IN` (`MCP23017 @ 0x23`) reads all toggle-switch states plus `CFG_APPLY`
- `U_LED_B1` (`MCP23017 @ 0x24`) drives the 5 Bank 1 LED anodes plus the Bank 1 RGB rails
- `U_LED_B2` (`MCP23017 @ 0x25`) drives the 7 Bank 2 LED anodes plus the Bank 2 RGB rails
- `Q_BNK1_R/G/B` and `Q_BNK2_R/G/B` provide the shared low-side colour rails under CM5 control

All three LED colour channels are routed and driven; CM5 selects the active bank colour according to
mode or diagnostic state.

```text
TOP EDGE / ENCLOSURE PANEL FACE

  [SW_B1_EN] [SW_B1_0] [SW_B1_1] [SW_B1_2] [SW_B1_3]   [SW_B2_EN] [SW_B2_0] [SW_B2_1] [SW_B2_2] [SW_B2_3] [SW_B2_4] [SW_B2_5] [CFG]
      |          |         |         |         |            |          |         |         |         |         |         |        |
   [LED]      [LED]     [LED]     [LED]     [LED]        [LED]      [LED]     [LED]     [LED]     [LED]     [LED]     [LED]   [PB]

   J_I2C        U_EXP_SW_IN (0x23)          U_LED_B1 (0x24)          U_LED_B2 (0x25)       Q_BNK1_R/G/B Q_BNK2_R/G/B
   left edge        centre-left                 centre                     centre-right             right edge
```

---

## 2. Placement Zones

- **Top edge:** 12 toggle switches, 12 indicator LEDs, and the `SW_CFG_APPLY` actuator position
- **Left edge:** `J_I2C` 6-pin JST PH connector, cable exit toward Stator `J_CFG`
- **Centre-left:** `U_EXP_SW_IN`, switch pull-downs, `R_CA1`, `C_CA1`
- **Centre / centre-right:** `U_LED_B1` and `U_LED_B2`, LED series resistors, and anode-routing fanout
- **Right edge:** 6 RGB BSS138 rail transistors with adjacent gate resistors

---

## 3. J_I2C — Stator Harness Connector

**Connector:** `B6B-PH-K-S(LF)(SN)` — 6-pin JST PH 2.0mm, vertical THT  
**Mating connector:** Stator `J_CFG`  
**Cable:** 6-wire harness, 100mm recommended

| Pin | Signal | Notes |
| :--- | :--- | :--- |
| 1 | `3V3_ENIG` | Logic supply for the three MCP23017 devices |
| 2 | `5V_MAIN` | Indicator power feed from the Controller via Stator `J_CFG` / `J4` |
| 3 | `GND` | Logic return only; no local GND_CHASSIS bond |
| 4 | `SDA` | Shared I2C-1 data |
| 5 | `SCL` | Shared I2C-1 clock |
| 6 | `GND` | Indicator-current return paired with pin 2 |

> Use 28AWG for pins 2 and 6, and 30AWG for pins 1, 3, 4, and 5.

---

## 4. U_EXP_SW_IN — MCP23017 @ 0x23

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

### U_LED_B1 — MCP23017 @ 0x24

| Port | Pin | Signal | Direction | Description |
| :--- | :--- | :--- | :--- | :--- |
| GPA | [0] | `LED_B1_EN_A` | Output | Bank 1 enable LED anode |
| GPA | [1] | `LED_B1_0_A` | Output | Bank 1 bit 0 LED anode |
| GPA | [2] | `LED_B1_1_A` | Output | Bank 1 bit 1 LED anode |
| GPA | [3] | `LED_B1_2_A` | Output | Bank 1 bit 2 LED anode |
| GPA | [4] | `LED_B1_3_A` | Output | Bank 1 bit 3 LED anode |
| GPA | [5] | `BNK1_R` | Output | Drives `Q_BNK1_R` gate |
| GPA | [6] | `BNK1_G` | Output | Drives `Q_BNK1_G` gate |
| GPA | [7] | `BNK1_B` | Output | Drives `Q_BNK1_B` gate |
| GPB | [0:7] | — | — | Spare |

### U_LED_B2 — MCP23017 @ 0x25

| Port | Pin | Signal | Direction | Description |
| :--- | :--- | :--- | :--- | :--- |
| GPA | [0] | `LED_B2_EN_A` | Output | Bank 2 enable LED anode |
| GPA | [1] | `LED_B2_0_A` | Output | Bank 2 bit 0 LED anode |
| GPA | [2] | `LED_B2_1_A` | Output | Bank 2 bit 1 LED anode |
| GPA | [3] | `LED_B2_2_A` | Output | Bank 2 bit 2 LED anode |
| GPA | [4] | `LED_B2_3_A` | Output | Bank 2 bit 3 LED anode |
| GPA | [5] | `LED_B2_4_A` | Output | Bank 2 bit 4 LED anode |
| GPA | [6] | `LED_B2_5_A` | Output | Bank 2 bit 5 LED anode |
| GPA | [7] | `BNK2_R` | Output | Drives `Q_BNK2_R` gate |
| GPB | [0] | `BNK2_G` | Output | Drives `Q_BNK2_G` gate |
| GPB | [1] | `BNK2_B` | Output | Drives `Q_BNK2_B` gate |
| GPB | [2:7] | — | — | Spare |

---

## 6. LED Colour-Rail Topology

Each indicator LED is common-anode and uses one individually switched anode from `U_LED_B1` or
`U_LED_B2` plus three shared cathode rails per bank (red, green, blue).

| Transistor | Gate source | Function |
| :--- | :--- | :--- |
| `Q_BNK1_R` | `U_LED_B1.GPA[5]` via `R_GATE1` | Pull Bank 1 red rail low |
| `Q_BNK1_G` | `U_LED_B1.GPA[6]` via `R_GATE2` | Pull Bank 1 green rail low |
| `Q_BNK1_B` | `U_LED_B1.GPA[7]` via `R_GATE3` | Pull Bank 1 blue rail low |
| `Q_BNK2_R` | `U_LED_B2.GPA[7]` via `R_GATE4` | Pull Bank 2 red rail low |
| `Q_BNK2_G` | `U_LED_B2.GPB[0]` via `R_GATE5` | Pull Bank 2 green rail low |
| `Q_BNK2_B` | `U_LED_B2.GPB[1]` via `R_GATE6` | Pull Bank 2 blue rail low |

CM5 firmware normally selects one colour rail per bank at a time:

- **Green** = switch-defined configuration
- **Red** = CM5-defined override

---

## 7. Switch / LED Mapping

| Physical control | Switch input | LED anode output | Bank colour rail source |
| :--- | :--- | :--- | :--- |
| `SW_B1_EN` | `U_EXP_SW_IN.GPA[0]` | `U_LED_B1.GPA[0]` | `U_LED_B1.GPA[5:7]` |
| `SW_B1[0]` | `U_EXP_SW_IN.GPA[1]` | `U_LED_B1.GPA[1]` | `U_LED_B1.GPA[5:7]` |
| `SW_B1[1]` | `U_EXP_SW_IN.GPA[2]` | `U_LED_B1.GPA[2]` | `U_LED_B1.GPA[5:7]` |
| `SW_B1[2]` | `U_EXP_SW_IN.GPA[3]` | `U_LED_B1.GPA[3]` | `U_LED_B1.GPA[5:7]` |
| `SW_B1[3]` | `U_EXP_SW_IN.GPA[4]` | `U_LED_B1.GPA[4]` | `U_LED_B1.GPA[5:7]` |
| `SW_B2_EN` | `U_EXP_SW_IN.GPB[0]` | `U_LED_B2.GPA[0]` | `U_LED_B2.GPA[7]` / `GPB[0:1]` |
| `SW_B2[0]` | `U_EXP_SW_IN.GPB[1]` | `U_LED_B2.GPA[1]` | `U_LED_B2.GPA[7]` / `GPB[0:1]` |
| `SW_B2[1]` | `U_EXP_SW_IN.GPB[2]` | `U_LED_B2.GPA[2]` | `U_LED_B2.GPA[7]` / `GPB[0:1]` |
| `SW_B2[2]` | `U_EXP_SW_IN.GPB[3]` | `U_LED_B2.GPA[3]` | `U_LED_B2.GPA[7]` / `GPB[0:1]` |
| `SW_B2[3]` | `U_EXP_SW_IN.GPB[4]` | `U_LED_B2.GPA[4]` | `U_LED_B2.GPA[7]` / `GPB[0:1]` |
| `SW_B2[4]` | `U_EXP_SW_IN.GPB[5]` | `U_LED_B2.GPA[5]` | `U_LED_B2.GPA[7]` / `GPB[0:1]` |
| `SW_B2[5]` | `U_EXP_SW_IN.GPB[6]` | `U_LED_B2.GPA[6]` | `U_LED_B2.GPA[7]` / `GPB[0:1]` |
| `SW_CFG_APPLY` | `U_EXP_SW_IN.GPB[7]` | — | — |

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

### Routing guidance

- Keep `SDA` / `SCL` as a matched short pair from `J_I2C` to the three expanders
- Route the `5V_MAIN` feed and pin-6 return wider than logic traces
- Place one 100nF decoupler at each MCP23017 supply pin cluster
- Keep gate resistors directly adjacent to the six BSS138 devices

---

## 9. Cross-References

| Document | Description |
| :--- | :--- |
| `design/Electronics/Settings_Board/Design_Spec.md` | Full electrical specification and BOM |
| `design/Electronics/Stator/Design_Spec.md` | `J_CFG` definition and CPLD configuration ownership |
| `design/Electronics/Stator/Board_Layout.md` | Mating connector definition for `J_CFG` |
| `design/Mechanical/Main_Enclosure/Design_Spec.md` | Panel cutout and actuator constraints |
