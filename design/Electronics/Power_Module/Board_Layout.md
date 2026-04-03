# Board Layout Visualisations

---

## Component Areas

```text
TOP VIEW (L1) - 4-Layer / 2oz Copper
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
|   [ eFuse U1 ] <--- TPS259474L + [0603 Thin-Film Ladder]                    |
|                                                                             |
|    ______________________             __________________________            |
|   |   [C1]  [C2]  [C3]   |           |  [ Amber "Safety Glow" ] |           |
|   |   [C4]  [C5]  [C6]   |           |  [  JST-PH Connector   ] |           |
|   | (15F Supercap Block) |           |__________________________|           |
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
|   [ U9 TPS2372-4 + U10 TPS23730 PoE DC-DC ]  [ T2 ACF XFMR ]                  |
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
| [ 5V / 6A BUCK ] <--------------------|----:  5V/GND  :----|--> [ USB-C CLIENT PORT ]  |
|                                       |    :          :    |    (Power to Pi 5)        |
| [ TPS25750 PD EMULATOR ] <------------|----:  CC1/2   :    |                           |
|                                       |    :          :    |                           |
| [ TELEMETRY I2C ] <-------------------|----:  I2C/GND :----|--> [ 40-PIN PI HEADER ]   |
| [ STATUS LEDS  ] <--------------------|----:  GPIO    :----|    (Logic to Pi 5)        |
|                                       |    :          :    |                           |
| [ U7 3V3_ENIG LDO ] <-----------------|----:----------:----|--> [ 3V3 TEST POINTS ]    |
|_______________________________________|    :..........:    |___________________________|
                                               V-SCORE
```

## Ethernet Power

```text
[ J2 RJ45 MAGJACK ]      [ ESD FIREWALL ]      [ PoE DISCRETE DC-DC ]                  [ INPUT SELECTOR ]
 ____________________      _________________     ________________________________         __________________
|                    |    |                 |   |                                |       |                 |
| RJ45 (Wurth        |    | [D4 TPD4E05U06] |   | [U9 TPS2372-4]                 |       | [U6 LM74700-Q1] |
| 7499111121A)       |--->| [D5 TPD4E05U06] |-->|  Type 4 PD / Hotswap          |       | (OR-ing Input)  |
| (4-pair 37-57V CT) |    |________|________|   |  ↓                             |       |_________________|
|                    |             |            | [U10 TPS23730 ACF DC-DC]       |
| CONNECTOR SHIELD --|-------------|----------  |  + [T2: POE600F-12LD]          |
|____________________|             V            |  Coilcraft / 60W / 12V out     |-----> [ +12V_POE ]
                             [ GND_CHASSIS ]   |  >=1500Vrms / 200kHz / 51W     |       (to OR-ing)
                                               |________________________________|

Note: T2 is the Coilcraft POE600F-12LD -- off-the-shelf 60W ACF PoE transformer (12V out, 36-72V in, 200kHz, >=1500Vrms). Order direct: coilcraft.com.
```

## USB-C Power

```text
[ USB-C BULKHEAD (J3) ]         [ ESD & FILTERING ]               [ INPUT SELECTOR ]        [   BtB Connector  ]
 _____________________           ____________________                                        __________________
|                     |         |                    |                                      |                  |
| VBUS (4 PINS) ------|-------->| [ TPD4E05U06 ESD ] |             _________________        | [ SAMTEC ERM8 ]  |
|                     |         |         |          |            |                 |       |                  |
| GND (4 PINS)  ------|-------->| [ LAIRD CHOKE L2 ] |----------->| [U5 LM74700-Q1] |       |                  |
|                     |         |                    |            | (OR-ing Input)  |       |                  |
|                     |         |                    |            |_________________|       |                  |
| CC1 / CC2     ------|--[PD]-->| [U4 STUSB4500 ] ---|-I2C--------------------------------->| PIN 32 (I2C SDA) |
| (Handshake)         |         | (Negotiates 15V)   |                                      | PIN 34 (I2C SCL) |
|_____________________|         |____________________|                                      |__________________|
```

## Power Flow

```text
 BULKHEAD ENTRY         INPUT PROTECTION             OR-ING / SELECT           UPS & REGULATION                                                                     SAMTEC EXIT
_________________      ____________________         ___________________        _________________________________________                                            _____________

[RJ45 PoE+] ---> [D4+D5 TPD4E05U06 ESD] ---> [U9 TPS2372-4 + U10 TPS23730 + T2 ACF] --\
                                                (PoE Type 4 discrete DC-DC, 12V/51W)      \
[USB-C 15V] ---> [TPD4E05U06 ESD] -------------------------------------------------------+---> [U6 LM74700-Q1 + Q1-Q3] -> [F1 TCO] -> [U1 TPS25980 eFuse]
                                                                                          /           (Priority OR-ing)                      (7A / 11V / 16.9V)
[BATTERY  ] ---> [D1+D2 ESD] ------------------------------------------------------------/                                                         |
                                                                                                                                                    |
                                                                    +-------------------------------------------------------------------> [U2A/U2B LMQ61460-Q1 Dual Buck]
                                                                    |                                                                              |
                                                                    |                                                                         [ 5V_MAIN BUS ]
                                                                    |                                                                              |
                                                                    |                              +---------------------------------------------> [U3 LTC3350]
                                                                    |                              |  (supercap manager)                           |
                                                                    |                              |                                          [C_SC1-4 Supercaps]
                                                                    |                              |                                          (4× Tecate 22F/2.7V, 2S2P)
                                                                    |                              |                                          (11F / 5.4V on 5V_MAIN)
                                                                    |                              |
                                                                    |                              +---------------------------------------------> [U4 TPS25750 PD Emu] ---> [ CM5 5V/5A ]
                                                                    |                              |
                                                                    |                              +---------------------------------------------> [U7 TPS7A8333P LDO] --> [ +3V3_ENIG ]
                                                                    |                              |
                                                                    |                              +---------------------------------------------> [U8 MCP121T-450E] --> [ PWR_GD ]
```

* Thermal Matrix vias sit beneath the supercap and eFuse thermal island for heat-spreading only; they are not part of the electrical power path.

## Power Handshake

```text
   POWER MODULE (INTERNAL)             SAMTEC BTB INTERFACE             CONTROLLER BOARD
 ___________________________          _______________________          ___________________ 
| [U1: eFuse 15V IN]        |        |                       |        |                   |
|           |               |        | [ GOLD PINS 1-10 ] ---|------->| [ SYSTEM GND ]    |
| [U2A/U2B: 5V BUCK×2 (12A)] -----|--------| [ GOLD PINS 11-18 ] --|------->| [ +5V_MAIN ]      |
|           |               |        |                       |        |                   |
| [U7: TPS7A8333P 3.3V LDO] ----|--------| [ GOLD PINS 19-22 ] --|------->| [ +3V3_ENIG ]     |
|                           |        |                       |        |                   |
| [J2: RJ45 MAGJACK] <------|--------| [ GOLD PINS 23-24 ] <-|--------| [ +3V3_SYSTEM ]   |
| (PoE+ Logic)              |        |                       |        | (Input from CM5)  |
|                           |        |                       |        |                   |
| [U6: SUPERVISOR] ---------|--------| [ GOLD PIN  26 ] -----|------->| [ PWR_GD ]        |
|                           |        |                       |        | (Handshake)       |
|___________________________|        |_______________________|        |___________________|
```

## Trace Connections

```text
EXTERNAL PORTS (REAR)           INTERNAL PROTECTION & STORAGE          CONTROLLER LINK (BTB)
 _____________________           ___________________________          _____________________________
|                     |         |                           |        |                             |
| [RJ45 PoE+] (48V) --|--[PD]-->| [WE-CMBNC]                |        |    [ SAMTEC ERM8 GOLD ]     |
|                     |         |    |                      |        |                             |
| [USB-C] (15V PD) ---|-------->| [CM5022 CHOKE]            |        | PINS 1-20: Gb Ethernet      |
|                     |         |    |                      |        | PINS 21-24: 3V3_SYSTEM      |
| [BATT] (14.4V) -----|-------->| [F1: 72°C TCO]            |        | PIN  25: ETH_LED_LINK       |
|_____________________|         |    |                      |        | PIN  26: ETH_LED_ACT        |
                                | [U1: TPS25980 eFuse]      |        | PINS 27-30: GND             |
       LADDER RESISTORS:        |    |                      |        | PINS 31-34: Status LEDs     |
       R1: 732k (UVLO) ---------|--->|                      |        | PINS 35-40: I2C Telemetry   |
       R2: 28.7k (OVLO) --------|--->|                      |        | PINS 41-44: 3V3_ENIG        |
       R3: 53.6k (GND) ---------|--->|                      |        | PIN  45: BATT_PRES_N        |
                                |    |                      |        | PINS 49-80: 5V_SYSTEM / GND |
                                |    |                      |        |_____________________________|
                                |    |                      |                       ^
                                | [5V_MAIN]-----------------|-------[U2A/U2B BUCK]--|
                                |    |                      |       [U7 3.3V LDO]--|
                                | [LTC3350 + C_SC1-4]-------|                      |
                                |    | (2x2 Block on 5V_MAIN|                      |
                                |    |                      |       |[SUPERVISOR]---|
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
| [ LED_ACT  PIN ] --(A)----|------->| [ PIN 27: ETH_LED_ACT   ] |---->(R)-->| [ LED 2 (YELLOW)]   |
|                           |        |                           |           |                     |
| [ 3V3_SYSTEM ] -----------|------->| [ PIN 21: 3V3_SYS_RAIL  ] |---------->| [ LED ANODES ]      |
|___________________________|        |___________________________|           |_____________________|
                                                                      (R) = 330Ω Resistors
```
