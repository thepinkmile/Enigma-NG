# Power Module: Board Layout Visualisations

**Status:** Draft
**Project:** Enigma-NG
**Author:** Izzyonstage & GitHub Copilot
**Version:** v1.0.0
**Associated Hardware Revision:** Rev A
**Last Updated:** 2026-04-05

---

## Component Areas

```text
TOP VIEW (L1) - 6-Layer / 2oz Copper
 _____________________________________________________________________________ 
| [R] [R] [R]  <-- 2.0mm Filleted Corners                                     |
|  |   |   |                                                                  |
| (Bulkhead Area - Rear Exit)                                                 |
|  __________    __________    __________                                     |
| |  RJ45    |  |  USB-C   |  | BATT-IN  | <--- Protruding Through Enclosure  |
| |  (PoE+)  |  |  (15V)   |  | (Locking)|                                    |
| |__________|  |__________|  |__________|                                    |
|      |              |              |                                        |
|   [CMC L1]       [CHOKE L2]   [BATT DIODE+ESD] <--- EMI / Input Protection  |
|______|______________|______________|________________________________________|
|                                                                             |
|   [  TCO F1  ] <--- 72°C Thermal Cutoff (In Series)                         |
|                                                                             |
|   [ eFuse U1 ] <--- TPS25980 + [0603 Thin-Film Ladder]                      |
|                                                                             |
|    ______________________             __________________________            |
|   |   [C_SC1]  [C_SC2]   |           |                          |           |
|   |   [C_SC3]  [C_SC4]   |           |  [ Amber "Safety Glow" ] |           |
|   | (22F/5.4V Supercap)  |           |  [ J3 Molex 43650-0519 ] |           |
|   | (22F×4 cells, 2S2P)  |           |__________________________|           |
|   |______________________|                                                  |
|                |                                                            |
|         [ THERMAL HUB ] <--- Type VII Hex-Matrix Vias to Bottom Slug        |
|_____________________________________________________________________________|
|                                                                             |
|  [ LOGIK-BEREIT ] <--- Green LED         [ SICHERHEITS-PROBE ] <--- V+ Pad  |
|                                          [ ERDE-PROBE        ] <--- GND Pad |
|                                                                             |
|   __________________________                                                |
|  |   SAMTEC ERM8 HEADER     | <--- Gold-Plated BtB Link to Controller       |
|  | (Slotted Align Pins)     |      (Includes PWR_GD Handshake)              |
|  |__________________________|                                               |
|_____________________________________________________________________________|
| [R] [R] [R]                                                      (V1.0) [R] |
|_____________________________________________________________________________|
```

## Simplified

```text
 _____________________________________________________________________________ 
| [RJ45]      [USB-C]      [BATT] <------- Bulkhead Zone (THT/SMT Mix)        |
|    |           |           |                                                |
| [D4/D5 ESD] [USB-C ESD] [BATT ESD] <----- Input protection per source       |
|    |           |           |                                                |
|   [LM74700-Q1 + Q1-Q3 OR-ING] <-------- Priority source selection           |
|_____________________________________________________________________________|
|                                                                             |
|   [  TCO F1  ]   [ eFuse U1 ]   [ U2A/U2B 5V BUCK ×2 ]   [ U7 3V3 LDO ]     |
|   [ U9 TPS2372-4 + U10 TPS23730 PoE DC-DC ]  [ T2 ACF XFMR ]                |
|                                                                             |
|   ( All Passives/Caps/Inductors Cluster around their ICs on Top )           |
|_____________________________________________________________________________|
|                                                                             |
|          [ U3 LTC3350 ]  [ C_SC1-4: 2×2 SUPERCAP BLOCK (on 5V_MAIN) ]       |
|                                                                             |
|      (Thermal Hex-Matrix Vias scattered underneath these high-heat zones)   |
|_____________________________________________________________________________|
|                                                                             |
|   [ SAMTEC ERM8 HEADER ]      [ DIAGNOSTIC PADS ]      [ V1.0 DATA PLATE ]  |
|_____________________________________________________________________________|
```

## PAS Coupon

```text
      MAIN POWER MODULE (V1.0)              V-SCORE LINE       PAS PROXY TAB (REMOVABLE)
 _______________________________________     ............     ___________________________ 
|                                       |    :          :    |                           |
| [ 5V / 12A DUAL BUCK ] <--------------|----:  5V/GND  :----|--> [ USB-C CLIENT PORT ]  |
|                                       |    :          :    |    (Power to Pi 5)        |
| [ TPS25751 PD EMULATOR ] <------------|----:  CC1/2   :    |                           |
|                                       |    :          :    |                           |
| [ TELEMETRY I2C ] <-------------------|----:  I2C/GND :----|--> [ 40-PIN PI HEADER ]   |
| [ SW1 RGB SWITCH LED ] <--------------|----:  GPIO    :----|    (Logic to CM5)         |
|                                       |    :          :    |                           |
| [ U7 3V3_ENIG LDO ] <-----------------|----:----------:----|--> [ 3V3 TEST POINTS ]    |
|_______________________________________|    :..........:    |___________________________|
                                               V-SCORE
```

## Ethernet Power

```text
[ J2 RJ45 MAGJACK ]       [ ESD FIREWALL ]      [ PoE DISCRETE DC-DC ]                  [ INPUT SELECTOR ]
 ____________________      _________________     ________________________________         __________________
|                    |    |                 |   |                                |       |                 |
| RJ45 (Wurth        |    | [D4 TPD4E05U06] |   | [U9 TPS2372-4]                 |       | [U6 LM74700-Q1] |
| 7499111121A)       |--->| [D5 TPD4E05U06] |-->|  Type 4 PD / Hotswap           |       | (OR-ing Input)  |
| (4-pair 37-57V CT) |    |________|________|   |  ↓                             |       |_________________|
|                    |             |            | [U10 TPS23730 ACF DC-DC]       |
| CONNECTOR SHIELD --|-------------|----------  |  + [T2: POE600F-12LD]          |
|____________________|             V            |  Coilcraft / 60W / 12V out     |-----> [ 12V_POE  ]
                             [ GND_CHASSIS ]    |  >=1500Vrms / 200kHz / 60W     |       (to OR-ing)
                                                |________________________________|

Note: T2 is the Coilcraft POE600F-12LD -- off-the-shelf 60W ACF PoE transformer (12V out, 36-72V in, 200kHz, >=1500Vrms). Order direct: coilcraft.com.
```

## USB-C Power

```text
[ USB-C BULKHEAD (J4) ]         [ ESD & FILTERING ]               [ INPUT SELECTOR ]            [   BtB Connector  ]
 _____________________           ____________________                                            __________________
|                     |         |                    |                                          |                  |
| VBUS (4 PINS) ------|-------->| [ TPD4E05U06 ESD ] |             _____________________        | [ SAMTEC ERM8 ]  |
|                     |         |         |          |            |                     |       |                  |
| GND (4 PINS)  ------|-------->| [ WE-CMBNC L2  ] --|----------->| [U6 LM74700QDBVRQ1] |       |                  |
|                     |         |                    |            | (OR-ing Input)      |       |                  |
|                     |         |                    |            |_____________________|       |                  |
| CC1 / CC2     ------|--[PD]-->| [U5 STUSB4500LQTR] |-I2C------------------------------------->| PIN 35 (I2C SDA) |
| (Handshake)         |         | (Negotiates 15V)   |                                          | PIN 36 (I2C SCL) |
|_____________________|         |____________________|                                          |__________________|
```

## Power Flow

```text
       INPUT A: PoE+             INPUT B: USB-C            INPUT C: Battery
     [ J2 RJ45 MagJack ]        [ J4 USB-C 15V ]          [ J3 Locking Conn ]
            |                          |                          |
  [D4/D5 ESD + L1 CMC  ]    [D3 ESD + L2 CMC    ]           [D1/D2 ESD]
  [U9 TPS2372-4 PD ctrl]    [U5 STUSB4500 PD ctrl]                |
  [U10 TPS23730 ACF+T2 ]      (negotiates 15V/5A USB-C PD)        |
    (48V->12V ACF converter)                                      |
            |                          |                          |
            \__________________________|__________________________/
                                       |
                          [U6 LM74700QDBVRQ1 + Q1/Q2/Q3]
                            (ideal-diode priority OR-ing)
                                       |
                                [F1 TCO 72°C]
                              (in-series thermal cutoff)
                                       |
                           [U1 TPS25980 eFuse]
                           (7A / 11V UVLO / 16.9V OVLO)
                                       |
                     [U2A/U2B LMQ61460-Q1 Dual Buck x2]
                      (7-17V pre-reg input -> 5V / 12A)
                                       |
                               [ 5V_MAIN BUS ]
          +---------------------------+-------------+--------------------+
          |                           |             |                    |
 [U3 LTC3350 Supercap Mgr]  [U4 TPS25751     ]  [U7 TPS75733KTTRG3]  [U8 MCP121T-450E]
 [C_SC1-4: 22F / 5.4V    ]   PD Emulator         3.3V LDO          Supervisor
 (4x Tecate 22F/2.7V 2S2P) -> CM5 5V/5A          -> 3V3_ENIG        -> PWR_GD
                              (via J1 BtB)         (3A / 3.3V)      (open-drain)
```

* Thermal Matrix vias sit beneath the supercap and eFuse thermal island for heat-spreading only; they are not part of the electrical power path.

## Power Handshake

```text
   POWER MODULE (INTERNAL)             SAMTEC BTB INTERFACE             CONTROLLER BOARD
 ___________________________          ___________________________          ___________________ 
| [U1: eFuse / OR-ing]      |        |                           |        |                   |
|                           |        |  [ PINS 1-20: GbE ] ------|------->| [ GbE Ethernet ]  |
| [U2A/U2B: 5V BUCK×2 (12A)]|--------|--[ PINS 21-22: 5V ] ------|------->| [ 5V_MAIN  ]      |
|                           |--------|--[ PINS 49-80: 5V+GND ] --|------->|   (9A cluster)    |
|                           |        |                           |        |                   |
| [U7: TPS75733KTTRG3 3.3V LDO] |--------|--[ PINS 39-44: 3V3_ENIG ] |------->| [ 3V3_ENIG ]      |
|                           |        |                           |        |                   |
| [J2: RJ45 LEDs] <---------|--------|  [ PINS 25-26: ETH_LEDs ] |<-------| [ ETH_LED_L/A ]   |
| (LED anodes: 3V3_ENIG)    |        |   (from CM5 GbE PHY)      |        |                   |
|                           |        |                           |        |                   |
| [U8: MCP121T Supervisor] -|--------|--[ PIN 34: PWR_GD ] ------|------->| [ PWR_GD ]        |
|                           |        |                           |        |  (Handshake)      |
| [U1: TPS25980 FAULT pin] -|--------|--[ PIN 29: SYS_FAULT ] ---|------->| [ CM5 GPIO 25 ]   |
| [U9: TPS2372-4 /PG ]     -|--------|--[ PIN 30: POE_STAT ]  ---|------->| [ CM5 GPIO 24 ]   |
| [U5: STUSB4500 PG ]      -|--------|--[ PIN 38: USB_STAT ]  ---|------->| [ CM5 GPIO 21 ]   |
|                           |        |                           |        |                   |
| [U7 EN pin] <-------------|--------|--[ PIN 46: ROTOR_EN ] <---|--------| [ CM5 GPIO 16 ]   |
| SW_LED circuit <----------|--------|--[ PIN 47: SW_LED_CTRL]<--|--------| [ CM5 GPIO 20 ]   |
|                           |        |                           |        |                   |
|___________________________|        |___________________________|        |___________________|
```

## Trace Connections

```text
EXTERNAL PORTS (REAR)           INTERNAL PROTECTION & STORAGE          CONTROLLER LINK (BTB)
 _____________________           ___________________________          _____________________________
|                     |         |                           |        |                             |
| [RJ45 PoE+] (48V) --|--[PD]-->| [WE-CMBNC]                |        | PINS 1-20: Gb Ethernet      |
|                     |         |    |                      |        | PINS 21-22: 5V_MAIN (+suppl)|
| [USB-C] (15V PD) ---|-------->| [WE-CMBNC L2]             |        | PINS 23-24: GND (+suppl)    |
|                     |         |    |                      |        | PIN  25: ETH_LED_LINK       |
| [BATT] (14.4V) -----|-------->| [F1: 72°C TCO]            |        | PIN  26: ETH_LED_ACT        |
|_____________________|         |    |                      |        | PINS 27-28: GND (isolation) |
                                | [U1: TPS25980 eFuse]      |        | PIN  29:    SYS_FAULT        |
       LADDER RESISTORS:        |    |                      |        | PIN  30:    POE_STAT         |
       R1: 232k (UVLO_HI) ------|--->|                      |        | PINS 31-33: SW_LED_R/G/B    |
       R2: 28.7k (UVLO_LO) -----|--->|                      |        | PIN  34:    PWR_GD           |
       R3: 53.6k (OVLO) --------|--->|                      |        | PINS 35-37: I2C Telemetry    |
                                |    |                      |        | PIN  38:    USB_STAT         |
                                |    |                      |        | PINS 39-44: 3V3_ENIG         |
                                |    |                      |        | PIN  45:    BATT_PRES_N      |
                                |    |                      |        | PIN  46:    ROTOR_EN         |
                                |    |                      |        | PIN  47:    SW_LED_CTRL      |
                                |    |                      |        | PIN  48:    GND (separator)  |
                                |    |                      |        | PINS 49-80: 5V_MAIN / GND   |
                                |    |                      |        |_____________________________|
                                |    |                      |                       ^
                                | [5V_MAIN]-----------------|-------[U2A/U2B BUCK]--|
                                |    |                      |       [U7 3.3V LDO]---|
                                | [LTC3350 + C_SC1-4]-------|                       |
                                |    | ( 2x2 Block on )     |                       |
                                |    | ( 5V_MAIN )          |       |[SUPERVISOR]---|
                                |    |                      |                       |
                                | [5.1V ZENER GLOW] --------|--->[AMBER LED EXT]----+
                                |___________________________|      (SAFETY)
```

## Interface Protrusions

```text
SIDE VIEW (CROSS-SECTION)

   [ OUTER MACHINE CHASSIS ] <--- Laser Engraved Face
              |
   [ POWER CAN "BOWL" WALL ] <--- Gasket Sealed
              |
       _______|_______
      |               |  <-- Connector Protrusion (Flush with Chassis)
      |   INTERFACE   |
      |______(X)______|  <-- (X) Mechanical Stop / Gasket Point
              |
   ___________|___________________________________________________
  |  [PCB]    | <-- 5mm Overhang Area (No components here)        |
  |           |                                                   |
  |  [L1/L4 2oz Copper]                                           |
  |_______________________________________________________________|
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
|                           |        |                           |           | 3V3_ENIG (local) -> |
|___________________________|        |___________________________|           | [ LED ANODES ]      |
                                                                             |_____________________|
                                                                      (R) = 330Ω Resistors
```

## LINK-ALPHA (80-Pin ERM8 — To Controller Board)

> **Connector Definition Owner:** This board. All other boards using this connector cross-reference here.

**Connector:** Samtec ERM8-040-05.0-S-DV-K-TR (Male, 80-pin). Mating ERF8-040 female on Controller Board J1.

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
| 30 | POE_STAT | PM → CTRL | PoE live status from TPS2372-4 /PG (CM5 GPIO 24); active-low (LOW = PoE live, per DEC-003) |
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
| 47 | SW_LED_CTRL | CTRL → PM | SW1 LED handoff: HIGH = CM5 in control; disables MIC1555 hardware path (CM5 GPIO 20) |
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
**Monitoring signals:** Pin 29 = SYS_FAULT (GPIO 25, active-low), Pin 30 = POE_STAT (GPIO 24, active-low — LOW = PoE live), Pin 38 = USB_STAT (GPIO 21, active-low) — all PM → CTRL.
**GND count:** Pins 1,4,7,10,13–20 (GbE block) + 23,24 + 27,28 + 37 + 48 + 50,52,54…80 (power cluster evens) = adequate return path for all rails. ✓

---

## §9 Routing — Trace Width Specifications

**Board specs:** 6-layer / 2oz finished copper (JLC06161H-2116).
All widths below are for external layers (L1/L6). Inner power planes use uninterrupted copper pours.

**IPC-2221A basis (2oz copper, external, 10°C rise, 25°C ambient):**
For 2oz external: ~0.15 mm per amp (derived from IPC-2221A: I = 0.048 × ΔT^0.44 × (w×2.76)^0.725;
solving for w at I=1A, ΔT=10°C gives w ≈ 0.15 mm). See Global_Routing_Spec.md §1.1 for the full table.

### Trace Width Table

| Net | Peak Current | IPC Calc (2oz ext) | Design Min | **Specified Width** | Layer | Notes |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Signal (I2C, GPIO, LED ctrl, status) | < 50 mA | 0.008 mm | 0.20 mm | **0.20 mm** | L1 | General 3.3 V logic |
| Supercap charge (LTC3350 → C_SC1–4) | 0.5 A | 0.075 mm | 0.50 mm | **0.50 mm** | L1 | Soft-charge limited by LTC3350 RICHARGE |
| 3V3_ENIG (LDO output → LINK-ALPHA pins 39–44) | 3.0 A | 0.45 mm | 0.80 mm | **0.80 mm** | L1 | Medium-power supply; extra margin for 3 A upper bound |
| 12V_POE (ACF transformer output → OR-ing U6) | 4.58 A | 0.69 mm | 1.00 mm | **1.00 mm** | L1 | 54.9 W PoE budget ÷ 12 V = 4.58 A peak |
| Battery input (J3 → OR-ing U6) | 4.82 A | 0.72 mm | 1.00 mm | **1.00 mm** | L1 | TPS25980 ILIM-limited; 14.4 V nominal battery |
| USB-C VBUS input (J4 → OR-ing U6) | 5.0 A | 0.75 mm | 1.00 mm | **1.00 mm** | L1 | 15 V / 5 A STUSB4500-negotiated PD limit |
| VIN_RAW (OR-ing output → TCO F1 → eFuse U1) | 7.0 A | 1.05 mm | 1.00 mm | **1.50 mm** | L1 | TPS25980 ILIM = 7 A; high-current path |
| VIN_SAFE (eFuse output → Buck U2A/U2B) | 7.0 A | 1.05 mm | 1.00 mm | **1.50 mm** | L1 | Post-eFuse buck input; same ILIM ceiling |
| 5V_MAIN bus (Buck output → BtB/LDO/supercap) | 9.05 A | 1.36 mm | 2.00 mm | **2.00 mm + pour** | L1 + inner | Very high current; L1 traces **2.00 mm minimum**; inner power pour mandatory |
| GND return pours | — | — | pour | **copper pour** | L2 + L6 | Solid uninterrupted 2oz GND planes |
| 5V_MAIN inner power pour | 9.05 A | — | pour | **copper pour** | L3 or L4 | Dedicated inner 2oz layer for primary bus |

### High-Current Design Rules (PM-specific)

* **5V_MAIN (9.05 A):** Classified Very High Current (> 5.5 A threshold per Global_Routing_Spec §1.1).
  All vias from L1 surface traces to the inner 5V_MAIN plane must use **POFV (IPC-4761 Type VII)**
  in 4-via thermal clusters. Teardrop fillets mandatory on all 5V_MAIN pads and vias.
  Thermal relief spokes on high-current pads: **20 mil (0.5 mm) wide, 4-spoke orthogonal** per §2.1.
* **VIN_RAW / VIN_SAFE (7 A):** Teardrops required. No acute-angle bends — arcs ≥ 1.0 mm radius per §1.
* **3V3_ENIG pour:** The TPS75733KTTRG3 (TO-263 KTT, 5-pin 10.16×15.24mm) requires standard thermal pad soldering and local ground vias only — the ≥200mm² copper pour requirement of the previous WSON-12 design is removed (P_diss ≤0.45W worst-case).
* **INA219 shunt (R23, CSS2H 10 mΩ):** Force and sense traces must be independent **0.20 mm** 4-wire
  Kelvin routes to avoid trace resistance corrupting the 10 mΩ measurement (1 mΩ trace = 10% error).
