# Settings Board V1.0 Layout & Pinout

**Status:** Draft
**Project:** Enigma-NG
**Author:** Izzyonstage & GitHub Copilot
**Version:** v1.0.0
**Associated Hardware Revision:** Rev A
**Last Updated:** 2026-04-14

---

## 1. Board Overview

The Settings Board is a landscape-orientation panel-mount PCB. Switch bodies mount through the
enclosure top-face panel cutouts; the PCB sits directly behind the panel. A 4-wire I²C ribbon
cable (J_I2C) exits to the left toward the Stator Board J_CFG.

```text
TOP VIEW (L1) — 4-Layer / 2oz Copper (JLC04161H-7628)
                     ENCLOSURE PANEL FACE  ←  switches protrude through here
╔══╦═══╦═══╦═══╦═══╦═╦══╦═══╦═══╦═══╦═══╦═══╦═══╦═══╗
║  ║   ║   ║   ║   ║ ║  ║   ║   ║   ║   ║   ║   ║[■]║
║ J║SW ║SW ║SW ║SW ║ ║SW║SW ║SW ║SW ║SW ║SW ║SW ║CFG║
║ _║B1 ║B1 ║B1 ║B1 ║ ║B2║B2 ║B2 ║B2 ║B2 ║B2 ║B2 ║APL║
║I2║EN ║[0]║[1]║[2]║[3]║EN║[0]║[1]║[2]║[3]║[4]║[5]║   ║
║C ║   ║   ║   ║   ║ ║  ║   ║   ║   ║   ║   ║   ║   ║
╠══╬═══╩═══╩═══╩═══╩═╬══╩═══╩═══╩═══╩═══╩═══╩═══╬═══╣
║  ║                  ║                           ║   ║
║  ║  U_EXP_SW_IN     ║     U_EXP_LED             ║Q×4║
║  ║  MCP23017 @0x26  ║     MCP23017 @0x27        ║   ║
║  ║  (SOIC-28)       ║     (SOIC-28)             ║   ║
║  ║                  ║                           ║   ║
╚══╩══════════════════╩═══════════════════════════╩═══╝
 J_I2C           [decoupling caps sprinkled throughout]
 (4-pin JST PH)

  ←─── BANK 1 (Plugboard Routing) ───→←── BANK 2 (Reflector Mapping) ─────→
  EN   bit0 bit1 bit2 bit3           EN  bit0 bit1 bit2 bit3 bit4 bit5
```

---

## 2. Component Zones

```text
┌─────────────────────────────────────────────────────────────────────────────┐
│  ZONE A         │  ZONE B               │  ZONE C          │  ZONE D        │
│  ─────────────  │  ───────────────────  │  ──────────────  │  ──────────    │
│  J_I2C          │  U_EXP_SW_IN          │  U_EXP_LED       │  Q_BNK1_G      │
│  (I²C ribbon    │  (MCP23017 @ 0x26)    │  (MCP23017 @     │  Q_BNK1_R      │
│  to Stator)     │  Switch input reader  │  0x27)           │  Q_BNK2_G      │
│                 │  + pull-down Rs       │  LED cathode +   │  Q_BNK2_R      │
│                 │  + R_CA1, C_CA1       │  colour rail     │  (SOT-23 PNP)  │
│                 │  (CFG_APPLY RC)       │  transistor Rdrs │  SW_CFG_APPLY  │
└─────────────────┴───────────────────────┴──────────────────┴────────────────┘
```

### Placement Notes

- **Switches (Bank 1 + Bank 2):** Along the full top edge of the board, spaced to match panel
  cutout pitch. Bank 1 (5 switches) left-of-centre; Bank 2 (7 switches) right-of-centre.
- **SW_CFG_APPLY:** Rightmost position at the top edge; clearly separated from Bank 2.
- **J_I2C:** Left edge of board. Cable exits toward Stator Board J_CFG.
- **U_EXP_SW_IN (Zone B):** Left half of PCB, centred. GPA faces toward Bank 1 switches;
  GPB faces toward Bank 2 switches and CFG_APPLY button to minimise trace length.
- **U_EXP_LED (Zone C):** Right half of PCB, centred. GPA cathode outputs face Bank 1 switches;
  GPB cathode outputs face Bank 2 switches.
- **PNP transistors Q_BNK1_G, Q_BNK1_R, Q_BNK2_G, Q_BNK2_R (Zone D):** Clustered at right edge near U_EXP_LED GPA[5:7]/GPB[7]
  colour-rail outputs. Base resistors placed adjacent to each transistor base pin.
- **Decoupling caps (0.1µF X7R 0402):** One per MCP23017 VDD pin, placed within 1mm.
- **Pull-down resistors (R_SW1–R_SW12):** Grouped per bank, placed between the switch pads
  and U_EXP_SW_IN GPIO pins.

---

## 3. J_I2C — Stator I²C Ribbon Connector

**Connector:** B4B-PH-K-S(LF)(SN) — 4-pin JST PH 2.0mm, THT, right-angle or vertical.
**Mating connector on Stator:** J_CFG (matching 4-pin JST PH socket).
**Cable:** 4-wire ribbon or Dupont cable, maximum 150mm length.

```text
J_I2C  (viewed from PCB top, pin 1 keyed)

  ┌─────────────────────┐
  │  1   2   3   4      │ ← to Stator J_CFG
  └─────────────────────┘
    │   │   │   │
    │   │   │   └─ SCL  ─── Stator I²C-1 clock
    │   │   └───── SDA  ─── Stator I²C-1 data
    │   └───────── GND  ─── Signal return / GND_CHASSIS bond
    └───────────── 3V3_ENIG ── Board power (from Stator)

PIN | SIGNAL    | NOTES
----|-----------|--------------------------------------------------
 1  | 3V3_ENIG  | Board power supply from Stator (via J_CFG pin 1)
 2  | GND       | GND_CHASSIS single-point bond at this connector
 3  | SDA       | I²C-1 data — shared with all Stator I²C devices
 4  | SCL       | I²C-1 clock — shared with all Stator I²C devices
```

---

## 4. U_EXP_SW_IN — MCP23017 @ 0x26 (Switch Input Reader)

**Package:** SOIC-28 | **Address:** A2=H, A1=H, A0=L → 0x26

All GPIO pins configured as inputs. All switch signal inputs (GPA[0:4], GPB[0:6]) use 10kΩ
pull-down resistors to GND: open switch = logic-0. CFG_APPLY (GPB[7]) uses 10kΩ pull-up to
3V3_ENIG + 100nF debounce cap: unpressed = logic-1, pressed = logic-0.

```text
                   U_EXP_SW_IN (MCP23017 @ 0x26)
                   ┌──────────────────────────┐
  3V3_ENIG ───────►│ VDD        (pin 9 / 28)  │
  GND      ────────│ VSS        (pin 10)       │
  SDA      ────────│ SDA                       │
  SCL      ────────│ SCL                       │
  3V3_ENIG ──┤ ├──►│ RESET_N    (pin 18)       │ (10kΩ pull-up)
   3V3_ENIG ──┤A2├──►│ A2  HIGH                 │
   3V3_ENIG ──┤A1├──►│ A1  HIGH                 │
  GND      ──┤A0└──►│ A0  LOW                  │
             │                                 │
  SW_B1_EN ──┼─────►│ GPA[0]   pull-down 10kΩ  │ ← Bank 1 enable switch
  SW_B1[0] ──┼─────►│ GPA[1]   pull-down 10kΩ  │ ← Routing config bit 0
  SW_B1[1] ──┼─────►│ GPA[2]   pull-down 10kΩ  │ ← Routing config bit 1
  SW_B1[2] ──┼─────►│ GPA[3]   pull-down 10kΩ  │ ← Routing config bit 2
  SW_B1[3] ──┼─────►│ GPA[4]   pull-down 10kΩ  │ ← Routing config bit 3
       spare ──────►│ GPA[5]   (reserved)      │
       spare ──────►│ GPA[6]   (reserved)      │
       spare ──────►│ GPA[7]   (reserved)      │
             │                                 │
  SW_B2_EN ──┼─────►│ GPB[0]   pull-down 10kΩ  │ ← Bank 2 enable switch
  SW_B2[0] ──┼─────►│ GPB[1]   pull-down 10kΩ  │ ← Reflector config bit 0
  SW_B2[1] ──┼─────►│ GPB[2]   pull-down 10kΩ  │ ← Reflector config bit 1
  SW_B2[2] ──┼─────►│ GPB[3]   pull-down 10kΩ  │ ← Reflector config bit 2
  SW_B2[3] ──┼─────►│ GPB[4]   pull-down 10kΩ  │ ← Reflector config bit 3
  SW_B2[4] ──┼─────►│ GPB[5]   pull-down 10kΩ  │ ← Reflector config bit 4
  SW_B2[5] ──┼─────►│ GPB[6]   pull-down 10kΩ  │ ← Reflector int-enable bit
  CFG_APPLY ─┼─────►│ GPB[7]   pull-UP  10kΩ   │ ← Active-low momentary btn
             └──────┴──────────────────────────┘

  Pull-down resistor map (all 10kΩ 0603, to GND):
  R_SW1 → GPA[0] (SW_B1_EN)      R_SW7  → GPB[1] (SW_B2[0])
  R_SW2 → GPA[1] (SW_B1[0])      R_SW8  → GPB[2] (SW_B2[1])
  R_SW3 → GPA[2] (SW_B1[1])      R_SW9  → GPB[3] (SW_B2[2])
  R_SW4 → GPA[3] (SW_B1[2])      R_SW10 → GPB[4] (SW_B2[3])
  R_SW5 → GPA[4] (SW_B1[3])      R_SW11 → GPB[5] (SW_B2[4])
  R_SW6 → GPB[0] (SW_B2_EN)      R_SW12 → GPB[6] (SW_B2[5])

  Pull-UP resistor (10kΩ 0603, to 3V3_ENIG):
  R_CA1 → GPB[7] (CFG_APPLY)

  Debounce cap (100nF X7R 0402, to GND):
  C_CA1 → GPB[7] (CFG_APPLY)  [RC τ = R_CA1 × C_CA1 = 10kΩ × 100nF = 1ms]
```

---

## 5. U_EXP_LED — MCP23017 @ 0x27 (LED Cathode + Colour Rail Driver)

**Package:** SOIC-28 | **Address:** A2=H, A1=H, A0=H → 0x27

All GPIO pins configured as outputs. Cathode outputs: LOW = LED lit; HIGH = LED off.
Colour-rail outputs: LOW = transistor ON.

```text
                   U_EXP_LED (MCP23017 @ 0x27)
                   ┌──────────────────────────────────────────────┐
  3V3_ENIG ───────►│ VDD                                          │
  GND      ────────│ VSS                                          │
  SDA      ────────│ SDA                                          │
  SCL      ────────│ SCL                                          │
  3V3_ENIG ──┤ ├──►│ RESET_N (10kΩ pull-up)                      │
  3V3_ENIG ────────│ A2  HIGH                                     │
  3V3_ENIG ────────│ A1  HIGH                                     │
  3V3_ENIG ────────│ A0  HIGH                                     │
             │                                                    │
             │◄────│ GPA[0]  SW_B1_CAT[0]  │─────→ SW_B1_EN  LED cathode
             │◄────│ GPA[1]  SW_B1_CAT[1]  │─────→ SW_B1[0]  LED cathode
             │◄────│ GPA[2]  SW_B1_CAT[2]  │─────→ SW_B1[1]  LED cathode
             │◄────│ GPA[3]  SW_B1_CAT[3]  │─────→ SW_B1[2]  LED cathode
             │◄────│ GPA[4]  SW_B1_CAT[4]  │─────→ SW_B1[3]  LED cathode
             │◄────│ GPA[5]  BNK1_G        │──R──→ base Q_BNK1_G (green rail, Bank 1)
             │◄────│ GPA[6]  BNK1_R        │──R──→ base Q_BNK1_R (red  rail, Bank 1)
             │◄────│ GPA[7]  BNK2_G        │──R──→ base Q_BNK2_G (green rail, Bank 2)
             │                             │
             │◄────│ GPB[0]  SW_B2_CAT[0]  │─────→ SW_B2_EN  LED cathode
             │◄────│ GPB[1]  SW_B2_CAT[1]  │─────→ SW_B2[0]  LED cathode
             │◄────│ GPB[2]  SW_B2_CAT[2]  │─────→ SW_B2[1]  LED cathode
             │◄────│ GPB[3]  SW_B2_CAT[3]  │─────→ SW_B2[2]  LED cathode
             │◄────│ GPB[4]  SW_B2_CAT[4]  │─────→ SW_B2[3]  LED cathode
             │◄────│ GPB[5]  SW_B2_CAT[5]  │─────→ SW_B2[4]  LED cathode
             │◄────│ GPB[6]  SW_B2_CAT[6]  │─────→ SW_B2[5]  LED cathode
             │◄────│ GPB[7]  BNK2_R        │──R──→ base Q_BNK2_R (red  rail, Bank 2)
             └──────┴──────────────────────┘

  Base resistors (1kΩ 0603) placed adjacent to each transistor:
  R_BASE1_G → GPA[5] to Q_BNK1_G base    R_BASE2_G → GPA[7] to Q_BNK2_G base
  R_BASE1_R → GPA[6] to Q_BNK1_R base    R_BASE2_R → GPB[7] to Q_BNK2_R base
```

---

## 6. LED Colour-Rail Circuit

Each bank has two PNP colour-rail transistors (Green and Red). Only one colour rail is
active per bank at a time; the CM5 daemon sets the appropriate rail based on whether the
bank is in switch-defined (green) or CM5-defined (red) mode.

```text
  COLOUR-RAIL CIRCUIT (per bank — shown for Bank 1 Green):

  3V3_ENIG
     │
     ├──[R_LED_BNK1_G (TBD)]──┬── BNK1_G anode rail
     │                        │       │        │
     │                   (Green LED   │    (Green LED
     │                    of switch   │    of another
     │                    SW_B1_EN)   │    switch...)
     │                        │       │
     │                   [cathode]  [cathode]
     │                        │       │
     │                   SW_B1_CAT[0]  SW_B1_CAT[1...]
     │                   (U_EXP_LED GPA[0]) (GPA[1...])
     │
     │   Q_BNK1_G (MMBT3906 PNP SOT-23)
     │   ┌─────────┐
     └──►│ Emitter │  ← 3V3_ENIG
         │         │
         │Collector│──── BNK1_G anode rail (switches Green rail ON when base LOW)
         │         │
         │  Base   │◄──[R_BASE1_G 1kΩ]──── U_EXP_LED GPA[5] (BNK1_G signal)
         └─────────┘

  PNP sourcing topology: GPIO LOW = transistor ON = colour rail sourced from 3V3_ENIG.
  GPIO HIGH = transistor OFF = colour rail floating/off.
  Current-limiting resistor R_LED_BNKx value to be confirmed at schematic phase
  based on selected switch LED forward voltage (Vf) and target current (If).
```

---

## 7. Switch-to-GPIO Connection Map

This table is the authoritative wiring reference from each physical switch to its
corresponding GPIO expander pin and LED driver pin.

```text
┌─────────────────┬───────────────────┬──────────────────────────┬──────────────────────────┐
│ Switch / Button │ Signal Name       │ U_EXP_SW_IN (@0x26) Pin  │ U_EXP_LED (@0x27) Pin    │
├─────────────────┼───────────────────┼──────────────────────────┼──────────────────────────┤
│ SW_B1_EN        │ Bank 1 enable     │ GPA[0]  (pull-down R_SW1)│ GPA[0] SW_B1_CAT[0]      │
│ SW_B1[0]        │ Routing bit 0     │ GPA[1]  (pull-down R_SW2)│ GPA[1] SW_B1_CAT[1]      │
│ SW_B1[1]        │ Routing bit 1     │ GPA[2]  (pull-down R_SW3)│ GPA[2] SW_B1_CAT[2]      │
│ SW_B1[2]        │ Routing bit 2     │ GPA[3]  (pull-down R_SW4)│ GPA[3] SW_B1_CAT[3]      │
│ SW_B1[3]        │ Routing bit 3     │ GPA[4]  (pull-down R_SW5)│ GPA[4] SW_B1_CAT[4]      │
├─────────────────┼───────────────────┼──────────────────────────┼──────────────────────────┤
│ SW_B2_EN        │ Bank 2 enable     │ GPB[0]  (pull-down R_SW6)│ GPB[0] SW_B2_CAT[0]      │
│ SW_B2[0]        │ Reflector bit 0   │ GPB[1]  (pull-down R_SW7)│ GPB[1] SW_B2_CAT[1]      │
│ SW_B2[1]        │ Reflector bit 1   │ GPB[2]  (pull-down R_SW8)│ GPB[2] SW_B2_CAT[2]      │
│ SW_B2[2]        │ Reflector bit 2   │ GPB[3]  (pull-down R_SW9)│ GPB[3] SW_B2_CAT[3]      │
│ SW_B2[3]        │ Reflector bit 3   │ GPB[4] (pull-down R_SW10)│ GPB[4] SW_B2_CAT[4]      │
│ SW_B2[4]        │ Reflector bit 4   │ GPB[5] (pull-down R_SW11)│ GPB[5] SW_B2_CAT[5]      │
│ SW_B2[5]        │ Int. refl. enable │ GPB[6] (pull-down R_SW12)│ GPB[6] SW_B2_CAT[6]      │
├─────────────────┼───────────────────┼──────────────────────────┼──────────────────────────┤
│ SW_CFG_APPLY    │ Config apply btn  │ GPB[7]  (pull-UP  R_CA1) │ — (no LED)               │
└─────────────────┴───────────────────┴──────────────────────────┴──────────────────────────┘

  Colour-rail transistor control (U_EXP_LED outputs only — no switch input):
  ┌──────────────┬──────────────────────────┬────────────────────────────────┐
  │ Transistor   │ U_EXP_LED Pin            │ Effect when **LOW**               │
  ├──────────────┼──────────────────────────┼────────────────────────────────┤
  │ Q_BNK1_G     │ GPA[5]  (via R_BASE1_G)  │ Bank 1 switches illuminate GREEN│
  │ Q_BNK1_R     │ GPA[6]  (via R_BASE1_R)  │ Bank 1 switches illuminate RED  │
  │ Q_BNK2_G     │ GPA[7]  (via R_BASE2_G)  │ Bank 2 switches illuminate GREEN│
  │ Q_BNK2_R     │ GPB[7]  (via R_BASE2_R)  │ Bank 2 switches illuminate RED  │
  └──────────────┴──────────────────────────┴────────────────────────────────┘
```

---

## 8. PCB Stackup & Routing Notes

**Manufacturer:** JLCPCB
**Layer count:** 4-layer
**Stackup:** JLC04161H-7628 (standard 4-layer, 2oz copper — system default per Global_Routing_Spec.md)
**Board thickness:** 1.6mm
**Copper weight:** 2oz outer (system-wide standard)
**Surface finish:** ENIG
**Min trace/space:** 0.15mm / 0.15mm

| Layer | Role | Notes |
| :--- | :--- | :--- |
| L1 (Top) | Signal routing — I²C, GPIO, LED cathode lines, switch signals | All active components on L1 |
| L2 | GND pour (flood fill) | Solid GND reference plane |
| L3 | 3V3_ENIG power plane | Dedicated power distribution |
| L4 (Bottom) | GND pour + Data Plate silkscreen | B.Silkscreen Data Plate; GND_CHASSIS bond |

### Trace Width Guidance

| Net | Specified Width | Layer | Notes |
| :--- | :--- | :--- | :--- |
| I²C (SDA, SCL) | 0.20 mm | L1 | Low-frequency signal; standard logic trace |
| GPIO signals (cathodes, colour-rail, switch inputs) | 0.20 mm | L1 | Low-current logic signals |
| 3V3_ENIG supply trace | 0.50 mm | L1 | Board total load < 200mA — ample margin |
| GND | Flood fill | L2, L4 | Solid GND reference planes |

> No controlled-impedance or high-speed routing requirements. Standard signal routing rules apply.

---

## 9. Cross-References

| Document | Description |
| :--- | :--- |
| `design/Electronics/Settings_Board/Design_Spec.md` | Full electrical specification, FR/DR, BOM |
| `design/Electronics/Stator/Design_Spec.md` | Stator J_CFG connector (mates with J_I2C); U_EXP4 CPLD config driver |
| `design/Electronics/Stator/Board_Layout.md` | Stator connector layout reference |
| `design/Mechanical/Main_Enclosure/Design_Spec.md` | Panel cutout requirements for switches |
