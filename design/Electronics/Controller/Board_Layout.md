# Controller Board Layout Visualisations

**Status:** Draft
**Project:** Enigma-NG
**Author:** Izzyonstage & GitHub Copilot
**Version:** v1.0.0
**Associated Hardware Revision:** Rev A
**Last Updated:** 2026-04-05

---

## CM5 Master GPIO & BtB Mapping

### LINK-ALPHA (To Power Module)

> **Connector Definition Owner:** `Power_Module/Board_Layout.md — LINK-ALPHA`.
> The pin table below is reproduced here for layout reference. In case of conflict, the Power Module definition is authoritative.

* **Pins 1-20:** Gigabit Ethernet (GND-Shielded: GND|DA+/-|GND|DB+/-|GND...)
* **Pins 21-22:** 5V_MAIN additional power (supplements pins 49-80 delivery cluster; combined 18 pins × 0.5A = 9A capacity)
* **Pins 23-24:** GND additional return path
* **Pins 25-26:** ETH_LED_LINK / ETH_LED_ACT (Active Low indicators)
* **Pins 27-28:** GND Isolation Moat
* **Pin 29:** SYS_FAULT (eFuse fault from TPS25980; PM → CTRL; CM5 GPIO 25)
* **Pin 30:** POE_STAT (PoE live status from TPS2372-4 /PG; PM → CTRL; CM5 GPIO 20)
* **Pins 31-34:** SW_LED_R/G/B (RGB switch) + PWR_GD
* **Pins 35-37:** I2C-1 Telemetry (SDA/SCL/GND — to PD/eFuse/STUSB4500)
* **Pin 38:** USB_STAT (USB-C PD negotiated status from STUSB4500; PM → CTRL; CM5 GPIO 21)
* **Pins 39-44:** 3V3_ENIG (Input from Power Module LDO — 6 pins, 3.0A capacity)
* **Pin 45:** BATT_PRES_N (Battery Presence Detection — Active Low, CM5 GPIO 23)
* **Pin 46:** ROTOR_EN (LDO enable signal — CM5 GPIO 16 → TPS75733KTTRG3 EN pin on Power Module)
* **Pin 47:** SW_LED_CTRL (CM5 GPIO 24 → LED arbitration; CTRL → PM)
* **Pin 48:** GND (logic/power zone boundary separator)
* **Pins 49-80:** 5V_MAIN / GND (9A Delivery Cluster — interleaved; combined with pins 21-22; 4-via Thermal Clusters)

#### Full 80-Pin Map

| Pin | Signal | Direction | Notes |
| :--- | :--- | :--- | :--- |
| 1 | GND | — | GbE shield return |
| 2 | MDI0+ | Bidir | GbE Pair A positive (100Ω diff) |
| 3 | MDI0− | Bidir | GbE Pair A negative |
| 4 | GND | — | GbE inter-pair shield |
| 5 | MDI1+ | Bidir | GbE Pair B positive (100Ω diff) |
| 6 | MDI1− | Bidir | GbE Pair B negative |
| 7 | GND | — | GbE inter-pair shield |
| 8 | MDI2+ | Bidir | GbE Pair C positive (100Ω diff) |
| 9 | MDI2− | Bidir | GbE Pair C negative |
| 10 | GND | — | GbE inter-pair shield |
| 11 | MDI3+ | Bidir | GbE Pair D positive (100Ω diff) |
| 12 | MDI3− | Bidir | GbE Pair D negative |
| 13 | GND | — | GbE trailing shield |
| 14 | GND | — | GbE extra return |
| 15 | GND | — | GbE extra return |
| 16 | GND | — | GbE extra return |
| 17 | GND | — | GbE extra return |
| 18 | GND | — | GbE extra return |
| 19 | GND | — | GbE extra return |
| 20 | GND | — | GbE extra return |
| 21 | 5V_MAIN | PM → CTRL | Supplemental power; 2oz trace; 0.5A/pin |
| 22 | 5V_MAIN | PM → CTRL | Supplemental power; 2oz trace; 0.5A/pin |
| 23 | GND | — | Supplemental return |
| 24 | GND | — | Supplemental return |
| 25 | ETH_LED_LINK | CTRL → PM | Active-Low ETH link status LED |
| 26 | ETH_LED_ACT | CTRL → PM | Active-Low ETH activity LED |
| 27 | GND | — | Isolation moat |
| 28 | GND | — | Isolation moat |
| 29 | SYS_FAULT | PM → CTRL | eFuse fault from TPS25980 FAULT pin (CM5 GPIO 25); active-low |
| 30 | POE_STAT | PM → CTRL | PoE live status from TPS2372-4 /PG (CM5 GPIO 20); active-low (LOW = PoE live, per DEC-003) |
| 31 | SW_LED_R | CTRL → PM | SW1 RGB switch red channel (CM5 GPIO 17) |
| 32 | SW_LED_G | CTRL → PM | SW1 RGB switch green channel (CM5 GPIO 18) |
| 33 | SW_LED_B | CTRL → PM | SW1 RGB switch blue channel (CM5 GPIO 19) |
| 34 | PWR_GD | PM → CTRL | Power-good signal from MCP121T-450E |
| 35 | I2C1_SDA | Bidir | I2C Telemetry bus data (CM5 GPIO 2; 4.7kΩ pull-up on PM) |
| 36 | I2C1_SCL | Bidir | I2C Telemetry bus clock (CM5 GPIO 3; 4.7kΩ pull-up on PM) |
| 37 | GND | — | I2C shield return |
| 38 | USB_STAT | PM → CTRL | USB-C PD negotiated from STUSB4500 (CM5 GPIO 21); active-low |
| 39 | 3V3_ENIG | PM → CTRL | Logic rail from TPS75733KTTRG3 LDO; 0.5A/pin |
| 40 | 3V3_ENIG | PM → CTRL | Logic rail; 0.5A/pin |
| 41 | 3V3_ENIG | PM → CTRL | Logic rail; 0.5A/pin |
| 42 | 3V3_ENIG | PM → CTRL | Logic rail; 0.5A/pin |
| 43 | 3V3_ENIG | PM → CTRL | Logic rail; 0.5A/pin |
| 44 | 3V3_ENIG | PM → CTRL | Logic rail; 0.5A/pin; combined 6 pins = 3.0A |
| 45 | BATT_PRES_N | PM → CTRL | Battery presence; active-low; CM5 GPIO 23 |
| 46 | ROTOR_EN | CTRL → PM | LDO enable for 3V3_ENIG rail; CM5 GPIO 16 → TPS75733KTTRG3 EN (active-LOW) |
| 47 | SW_LED_CTRL | CTRL → PM | SW1 LED handoff: HIGH = CM5 in control; LED arbitration (CM5 GPIO 24) |
| 48 | GND | — | Logic/power zone boundary separator |
| 49 | 5V_MAIN | PM → CTRL | Interleaved power; 2oz; 0.5A/pin |
| 50 | GND | — | Interleaved return |
| 51 | 5V_MAIN | PM → CTRL | Interleaved power |
| 52 | GND | — | Interleaved return |
| 53 | 5V_MAIN | PM → CTRL | Interleaved power |
| 54 | GND | — | Interleaved return |
| 55 | 5V_MAIN | PM → CTRL | Interleaved power |
| 56 | GND | — | Interleaved return |
| 57 | 5V_MAIN | PM → CTRL | Interleaved power |
| 58 | GND | — | Interleaved return |
| 59 | 5V_MAIN | PM → CTRL | Interleaved power |
| 60 | GND | — | Interleaved return |
| 61 | 5V_MAIN | PM → CTRL | Interleaved power |
| 62 | GND | — | Interleaved return |
| 63 | 5V_MAIN | PM → CTRL | Interleaved power |
| 64 | GND | — | Interleaved return |
| 65 | 5V_MAIN | PM → CTRL | Interleaved power |
| 66 | GND | — | Interleaved return |
| 67 | 5V_MAIN | PM → CTRL | Interleaved power |
| 68 | GND | — | Interleaved return |
| 69 | 5V_MAIN | PM → CTRL | Interleaved power |
| 70 | GND | — | Interleaved return |
| 71 | 5V_MAIN | PM → CTRL | Interleaved power |
| 72 | GND | — | Interleaved return |
| 73 | 5V_MAIN | PM → CTRL | Interleaved power |
| 74 | GND | — | Interleaved return |
| 75 | 5V_MAIN | PM → CTRL | Interleaved power |
| 76 | GND | — | Interleaved return |
| 77 | 5V_MAIN | PM → CTRL | Interleaved power |
| 78 | GND | — | Interleaved return |
| 79 | 5V_MAIN | PM → CTRL | Interleaved power; last 5V_MAIN pin |
| 80 | GND | — | Interleaved return; last pin |

**5V_MAIN pin count:** Pins 21–22 (2) + Pins 49, 51, 53…79 (16 odd pins) = **18 pins × 0.5A = 9.0A total capacity** ✓
**3V3_ENIG pin count:** Pins 39–44 (6 pins) = **6 × 0.5A = 3.0A total capacity** ✓ (matches TPS75733KTTRG3 3A max output)
**ROTOR_EN:** Single logic signal at pin 46; 3.3V, driven by CM5 GPIO 16.
**Monitoring signals:** Pin 29 = SYS_FAULT (GPIO 25), Pin 30 = POE_STAT (GPIO 20), Pin 38 = USB_STAT (GPIO 21) — all PM → CTRL, active-low/high per signal definition.
**GND count:** Pins 1,4,7,10,13–20 (GbE block) + 23,24 + 27,28 + 37 + 48 + 50,52,54…80 (power cluster evens) = adequate return path for all rails. ✓

```text
       LINK-ALPHA (80-PIN SAMTEC)           SIGNAL TYPE          FUNCTION
_______________________________________    _____________    _____________________________

[ PINS 01 - 20 ] ------------------------> [ 100Ω DIFF ] -> [ GIGABIT ETHERNET (GBE)     ]
 (Pattern: GND|DA+/-|GND|DB+/-|GND...)     (SHIELDED)       (To External RJ45)

[ PINS 21 - 22 ] ------------------------> [ 2oz POWER ] -> [ 5V_MAIN (SUPPLEMENTAL)     ]
                                           (BULK DC)        (Adds 2 pins to delivery cluster)

[ PINS 23 - 24 ] ------------------------> [ 2oz POWER ] -> [ GND (SUPPLEMENTAL RETURN)  ]
                                           (BULK DC)        (Adds 2 pins to return path)

[ PINS 25 - 26 ] ------------------------> [ 2oz POWER ] -> [ ETH_LED_LINK / ETH_LED_ACT ]
                                           (GPIO OUT)       (Active Low indicators)

[ PINS 27 - 28 ] ------------------------> [ ISOLATION ] -> [ MASTER GND BANK            ]

[ PIN  29      ] ------------------------> [ 3.3V LOGIC] -> [ SYS_FAULT                  ]
                                           (GPIO IN)        (PM → CTRL, active-low)

[ PIN  30      ] ------------------------> [ 3.3V LOGIC] -> [ POE_STAT                   ]
                                           (GPIO IN)        (PM → CTRL, active-low)

[ PINS 31 - 33 ] ------------------------> [ 3.3V LOGIC] -> [ SW_LED_R/G/B (RGB switch) ]
                                           (GPIO OUT)       (SW1 RGB LED channels)

[ PIN 34       ] ------------------------> [ 3.3V LOGIC] -> [ PWR_GD                     ]
                                           (GPIO IN)        (From Power Module MCP121T)

[ PINS 35 - 38 ] ------------------------> [ I2C BUS   ] -> [ TELEMETRY (SDA/SCL)        ]
                                           (SHIELDED)       (To PD Emulator/eFuse)

[ PINS 39 - 44 ] ------------------------> [ 2oz POWER ] -> [ 3V3_ENIG (INPUT)           ]
                                           (CLEAN IN)       (From Power Module LDO)

[ PIN  45      ] ------------------------> [ 3.3V LOGIC] -> [ BATT_PRES_N                ]
                                           (GPIO IN)        (From Power Module Batt)

[ PIN  46      ] ------------------------> [ 3.3V LOGIC] -> [ ROTOR_EN                   ]
                                           (GPIO OUT)       (CM5 GPIO 16 → TPS75733KTTRG3 EN (active-LOW))

[ PIN 47       ] ------------------------> [ 3.3V LOGIC] -> [ SW_LED_CTRL                ]
                                           (GPIO OUT)       (CM5 GPIO 24 — HIGH = CM5 in control of SW1 RGB)

[ PIN 48       ] ------------------------> [ GND       ] -> [ GND (ZONE BOUNDARY)        ]

[ PINS 49 - 80 ] ------------------------> [ 2oz POWER ] -> [ 5V_MAIN (9A DELIVERY)      ]
 (16× 5V + 16× GND interleaved)           (BULK DC)        (To CM5 VCC_IN; incl. pins 21-22)
```

### DIAGNOSTIC BANK-ALPHA (Top-Right)

| Pin | Signal | Direction | Description |
| :--- | :--- | :--- | :--- |
| 1 | 5V_MAIN | PM → CTRL | 5V power rail probe point |
| 2 | 5V_MAIN | PM → CTRL | 5V power rail (redundant) |
| 3 | 3V3_ENIG | PM → CTRL | 3.3V logic rail probe point |
| 4 | 3V3_ENIG | PM → CTRL | 3.3V logic rail (redundant) |
| 5 | I2C1_SDA | Bidir | I²C Telemetry bus data |
| 6 | I2C1_SCL | Bidir | I²C Telemetry bus clock |
| 7 | ETH_LED_LINK | CTRL → PM | Ethernet link status LED |
| 8 | ETH_LED_ACT | CTRL → PM | Ethernet activity LED |
| 9 | SW_LED_G | CTRL → PM | RGB LED green channel (GPIO 18) |
| 10 | SW_LED_R | CTRL → PM | RGB LED red channel (GPIO 17) |
| 11 | SW_LED_B | CTRL → PM | RGB LED blue channel (GPIO 19) |
| 12 | PWR_GD | PM → CTRL | Power-good signal (GPIO 27) |
| 13 | BATT_PRES_N | PM → CTRL | Battery presence active-low (GPIO 23) |
| 14 | SW_LED_CTRL | CTRL → PM | LED arbitration HIGH = CM5 in control (GPIO 24) |
| 15 | SPARE | — | Reserved for future use |
| 16 | SPARE | — | Reserved for future use |
| 17 | SPARE | — | Reserved for future use |
| 18 | SPARE | — | Reserved for future use |
| 19 | GND_CHASSIS | — | Chassis ground reference |
| 20 | GND | — | Signal/power ground return |

> **Note:** RGB channel order in Diagnostic Bank (pins 9/10/11 = G/R/B) differs from BtB Link-Alpha order (pins 31/32/33 = R/G/B).
> This is intentional for PCB routing convenience. Silkscreen legend must label each pad individually to avoid probe confusion during bring-up.

### LINK-BETA (To Stator Board)

**Connector:** Samtec ERF8-020-05.0-S-DV-K-TR (Female, 40-pin). Mating ERM8-020 male on Stator Board J8.

> **Connector Definition Owner:** This board. All other boards using this connector cross-reference here.
>
> ⚠️ **Poka-Yoke:** The 80-pin LINK-ALPHA (ERF8-040) and 40-pin LINK-BETA (ERF8-020) on this board are
> physically incompatible — the mating connectors cannot be inserted into the wrong socket. This prevents
> LINK-ALPHA and LINK-BETA mismating during prototype bring-up. See DEC-015.

| Pin | Signal | Direction | Notes |
| :--- | :--- | :--- | :--- |
| 1 | GND | — | JTAG leading shield |
| 2 | TCK | CTRL→Stator | JTAG clock |
| 3 | GND | — | TCK/TMS inter-pin shield |
| 4 | TMS | CTRL→Stator | JTAG mode select |
| 5 | GND | — | TMS/TDI inter-pin shield |
| 6 | TDI | CTRL→Stator | JTAG data in |
| 7 | GND | — | TDI/RST inter-pin shield |
| 8 | SYS_RESET_N | CTRL→Stator | Active-low system reset; clears all CPLDs in stack |
| 9 | GND | — | JTAG trailing shield |
| 10 | GND | — | Isolation moat pin 1 |
| 11 | GND | — | Isolation moat pin 2 |
| 12 | ENC_IN[0] | CTRL→Stator | Encoder input bit 0 |
| 13 | ENC_IN[1] | CTRL→Stator | Encoder input bit 1 |
| 14 | ENC_IN[2] | CTRL→Stator | Encoder input bit 2 |
| 15 | ENC_IN[3] | CTRL→Stator | Encoder input bit 3 |
| 16 | ENC_IN[4] | CTRL→Stator | Encoder input bit 4 |
| 17 | ENC_IN[5] | CTRL→Stator | Encoder input bit 5 |
| 18 | GND | — | ENC_IN / ENC_OUT inter-group shield |
| 19 | ENC_OUT[0] | Stator→CTRL | Encoder output bit 0 |
| 20 | ENC_OUT[1] | Stator→CTRL | Encoder output bit 1 |
| 21 | ENC_OUT[2] | Stator→CTRL | Encoder output bit 2 |
| 22 | ENC_OUT[3] | Stator→CTRL | Encoder output bit 3 |
| 23 | ENC_OUT[4] | Stator→CTRL | Encoder output bit 4 |
| 24 | ENC_OUT[5] | Stator→CTRL | Encoder output bit 5 |
| 25 | GND | — | ENC_OUT / TTD_RETURN shield |
| 26 | TTD_RETURN | Stator→CTRL | JTAG TDO short-path return (bypasses rotor stack) |
| 27 | GND | — | TTD_RETURN shield |
| 28 | 3V3_ENIG | PM→Stator | Power pass-through from Link-Alpha (2oz copper) |
| 29 | 3V3_ENIG | PM→Stator | Power pass-through from Link-Alpha (2oz copper) |
| 30 | 3V3_ENIG | PM→Stator | Power pass-through from Link-Alpha (2oz copper) |
| 31 | 3V3_ENIG | PM→Stator | Power pass-through from Link-Alpha (2oz copper) |
| 32 | 3V3_ENIG | PM→Stator | Power pass-through from Link-Alpha (2oz copper) |
| 33 | 3V3_ENIG | PM→Stator | Power pass-through from Link-Alpha (2oz copper) |
| 34 | 3V3_ENIG | PM→Stator | Power pass-through from Link-Alpha (2oz copper) |
| 35 | 3V3_ENIG | PM→Stator | Power pass-through from Link-Alpha (2oz copper) |
| 36 | GND | — | Power return |
| 37 | GND | — | Power return |
| 38 | GND | — | Power return |
| 39 | GND | — | Power return |
| 40 | GND | — | Power return |

**Power capacity:** 8 × 3V3_ENIG pins × 0.5A/pin = 4.0A total — adequate for the 30-rotor worst case (2.20 A per Power_Budgets.md).

### DIAGNOSTIC BANK-BETA (Top-Left)

| Pin | Signal | Direction | Description |
| :--- | :--- | :--- | :--- |
| 1 | ENC_IN[0] | CTRL → Stator | Encoder input bit 0 |
| 2 | ENC_IN[1] | CTRL → Stator | Encoder input bit 1 |
| 3 | ENC_IN[2] | CTRL → Stator | Encoder input bit 2 |
| 4 | ENC_IN[3] | CTRL → Stator | Encoder input bit 3 |
| 5 | ENC_IN[4] | CTRL → Stator | Encoder input bit 4 |
| 6 | ENC_IN[5] | CTRL → Stator | Encoder input bit 5 |
| 7 | SYS_RESET_N | CTRL → Stator | Active-low system reset (GPIO 26) |
| 8 | GND | — | Ground reference |
| 9 | ENC_OUT[0] | Stator → CTRL | Encoder output bit 0 |
| 10 | ENC_OUT[1] | Stator → CTRL | Encoder output bit 1 |
| 11 | ENC_OUT[2] | Stator → CTRL | Encoder output bit 2 |
| 12 | ENC_OUT[3] | Stator → CTRL | Encoder output bit 3 |
| 13 | ENC_OUT[4] | Stator → CTRL | Encoder output bit 4 |
| 14 | ENC_OUT[5] | Stator → CTRL | Encoder output bit 5 |
| 15 | JTAG_TCK | JDB → Stator | JTAG clock (isolated from TDI/TMS) |
| 16 | GND | — | TCK shield / clock return |
| 17 | TMS | JDB → Stator | JTAG mode select |
| 18 | TDI | JDB → Stator | JTAG data in |
| 19 | TDO | Stator → JDB | JTAG data out (TTD_RETURN) |
| 20 | GND | — | JTAG trailing shield |

### BtB Connectivity Routing

```text
      REAR INTERFACE (POWER & ENTRY)                     CONTROLLER CORE (L1-L6)                   RIGHT-BANK (USER I/O)
 _____________________________________________        ________________________________        _____________________________
| [R]                                     [R] |      |                                |      |                         [R] |
| (O) [  LINK-ALPHA (ERF8-040)  ] --(5V/GBE)--|----->| [ CM5 COMPUTE MODULE ]         |      | (O)                         |
| (1)  (Female Socket / 80-pin)               |      |  (Wireless/8GB/32GB)           |      | (3)                         |
|        |                 |                  |      |                                |      |                             |
|  [ 3V3_ENIG  ]     [ SNIFFER BUS (12-bit) ] |<---->| [ 12-bit GPIO ]  [ 100Ω HDMI ] |      |                             |
|  (2oz L3 BRIDGE)   (6-In / 6-Out Binary)    |      |                        |       |      |                             |
|       |                                     |      |                  [ AP2331W   ] |      |                             |
|       |       [ JTAG DAUGHTERBOARD ]        |      |                  [ TPD4E05U06] |------|------> [ HDMI TYPE-A  ]     |
|       |        (1x5 & 1x10 Headers)         |      |                                |      |        [   2007435-1  ]     |
|       |           |            |            |      |                [ 90Ω USB 3.0 ] |      |        [  (PROTRUDES) ]     |
|       |       [ JTAG BUS ]  [ USB 2.0 ] ----|----->|                        |       |      |        [ 5.0mm OVER   ]     |
|       |           |                         |      |                [ TPS2065C ]    |      |                             |
|    [  LINK-BETA  (ERF8-020)  ]              |      |                [ TPD4E05U06 ]  |------|------> [ USB 3.0 DUAL ]     |
|      (Female Socket / 40-pin)               |      |                                |      |        [   STACKED    ]     |
|                                             |      |                                |      |        [   48406-0003 ]     |
|                                             |      |                                |      |        [  (PROTRUDES) ]     |
| (O)                    [ DIAG BANK (2x10)]  |      |                                |      |        [ 5.0mm OVER   ]     |
| (4)                      (Exposed ENIG)     |      |                                |      | (O)   (V1.0) DATA PLATE (2) |
|_____________________________________________|      |________________________________|      |_____________________________|
 (O) = M3 Star-Burst Grounding PTH                   [R] = 2.0mm Fillet Corner               (1-4) = Star-Pattern Torque Sequence
```

```text
       TOP VIEW (BtB INTERFACES)
 ____________________________________________________________________
| (O) [R]    [ LINK-BETA (ERF8-020) ]  [ LINK-ALPHA (ERF8-040) ]   [R] (O) |
|            (Stator / Logic Out)      (Power / Ethernet In)           |
|                   |                          |                     |
|            [ DIAG BANK-B  ]        [ DIAG BANK-A      ]            |
|            [ (ENCRYPTION) ]        [ (POWER & STATUS) ]            |
|               |      |                       |                (O)  |
|          (JTAG Link) |                       |                     |
|               |      |               [  CM5 MODULE  ]    [ USB3 ]  |
|               |      |               [ (RIGHT-SIDE) ]    [STACK ]  |--- PROTRUDES
|   [ JTAG DAUGHTER ]  |               [              ]----[ PORT ]  |
|   [  MOUNT (2x10) ]  +--(6-In/6-Out)-[ (GPIO 0-11)  ]              |
|               |                      [              ]              |
|               +------(USB 2.0)-------[ (HDMI/USB3)  ]----[ HDMI ]  |
|                                      |______________|    [ FULL ]  |--- PROTRUDES
|                                                          [ TYPEA ] |
|                                                                    |
| (O)                                                            (O) |
|____________________________________________________________________|

```

## RTC Battery Backup Routing

```text
        CM5 DF40 CONNECTOR                  VBAT CIRCUIT                    BT1 (BATTERY)
  ___________________________          ____________________          ____________________________
 |                           |        |                    |        |                            |
 | [ CM5 VBAT PIN 95    ] ---|------->| [ C6: 100nF ]      |        | [ BT1: Keystone 3034 ]     |
 |                           |   |    | (to GND)           |        | (CR2032 click-in holder)   |
 |___________________________|   |    |____________________|        | (Left edge of board)       |
                                 |    |                    |        |                            |
                                 +----| [ D1: BAT54 ]      |<-------| [ CR2032 (+) ]             |
                                      | (Schottky diode)   |        | 3.0V nom / 220mAh          |
                                      | (anode = BT1(+))   |        |____________________________|
                                      | (cathode = VBAT)   |        (BT1(-) → GND local pour)
                                      |____________________|
```

> **Routing rules:**
>
> * VBAT trace: 6mil minimum, L1, direct route from CM5 DF40 Pin 95 to D1 cathode; max 20mm.
> * C6 placed within 5mm of CM5 DF40 Pin 95 (before D1).
> * BT1 on left edge of board; keep VBAT trace well away from GbE, USB 3.0, and HDMI striplines.

## Interface Component Connectivity

```text
      INTERNAL LOGIC                   I/O PROTECTION                 EXTERNAL PORTS
 ____________________________         __________________          _______________________ 
|                            |       |                  |        |                       |
| [ CM5 GPIO 22 ] <--(FAULT)-|-------| [ TPS2065C IC  ] |        |                       |
| [ CM5 USB 3.0 ] <---(90Ω)--|-------| [ TPD4E05U06   ] |------->| [ STACKED USB 3.0  ]  |
|                            |       | (Current/ESD)    |        | (MOLEX 48406-0003)    |
|                            |       |                  |        |       [ ANCHORS ]-----|--> [ CHASSIS GND ]
|                            |       |__________________|        |_______________________|
|                            |       |                  |        |                       |
| [ CM5 HDMI 0  ] <--(100Ω)--|-------| [ AP2331W IC   ] |        | [ FULL-SIZE HDMI   ]  |
| [ CM5 HDMI 5V ] <---(PWR)--|-------| [ TPD4E05U06   ] |------->| (TE 2007435-1)        |
|                            |       | (Current/ESD)    |        |       [ ANCHORS ]-----|--> [ CHASSIS GND ]
|____________________________|       |__________________|        |_______________________|
```

## Ethernet Activity LEDs

```text
       CONTROLLER (CM5)                    LINK-ALPHA (80-PIN)                    POWER MODULE
 ___________________________          ___________________________             _____________________
| [ CM5 GBE PHY ]           |        |                           |           | [ RJ45 MAGJACK ]    |
|    |                      |        |                           |           | (WURTH 7499111)     |
| [ LED_LINK PIN ] --(L)----|------->| [ PIN 25: ETH_LED_LINK  ] |---->(R)-->| [ LED 1 (GREEN) ]   |
| [ LED_ACT  PIN ] --(A)----|------->| [ PIN 26: ETH_LED_ACT   ] |---->(R)-->| [ LED 2 (YELLOW)]   |
|                           |        |                           |           |                     |
| [ 3V3_ENIG ] -------------|------->| (local Power Module rail) |---------->| [ LED ANODES ]      |
|___________________________|        |___________________________|           |_____________________|
                                                                      (R) = 330Ω Resistors
```
