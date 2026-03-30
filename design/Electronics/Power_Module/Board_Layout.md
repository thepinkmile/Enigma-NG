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
|   [CMC L1]       [CHOKE L2]     [PI-FILTER] <--- EMI Bulkhead Zone          |
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
| [RJ45]      [USB-C]      [BATT]  <-- Bulkhead Zone (THT/SMT Mix)            |
|    |           |           |                                                |
| [DIODES]   [DIODES]   [PI-FILTER] <-- Ideal Diode ORing (LM74700 + FETs)    |
|_____________________________________________________________________________|
|                                                                             |
|   [  TCO F1  ]       [ eFuse U1 ]     [ 5V BUCK U2 ]   [ 3.3V LDO U3 ]      |
|                                                                             |
|   ( All Passives/Caps/Inductors Cluster around their ICs on Top )           |
|_____________________________________________________________________________|
|                                                                             |
|               [ 2x3 SUPERCAP VERTICAL BLOCK ]                               |
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
| [ 3V3_ENIG LDO ] <--------------------|----:----------:----|--> [ 3V3 TEST POINTS ]    |
|_______________________________________|    :..........:    |___________________________|
                                               V-SCORE
```

## Ethernet Power

```text
[ RJ45 BULKHEAD (J2) ]         [ ESD FIREWALL ]                [ PoE+ LOGIC ]
 ____________________           _______________                 _______________ 
|                    |         |               |               |               |
| DATA PAIR 1-4 -----|-------->| [RClamp0502B] |---[Magjack]-->| [ +15V PoE+ ] |
| (Differential)     |         | (TVS Shunt)   |   (7499111)   | [  Signals  ] |
|                    |         |_______|_______|               |_______|_______|
|                    |                 |                               |
| CONNECTOR SHIELD --|-----------------|-------------------------------|
|____________________|                 V
                                [ GND_CHASSIS ] <--- Main Enclosure Ground
```

## USB-C Power

```text
[ USB-C BULKHEAD (J3) ]         [ POWER LOGIC ISLAND ]         [  POWER SELECTOR   ]        [   BtB Connector  ]
 _____________________           ____________________                                        __________________ 
|                     |         |                    |                                      |                  |
| VBUS (4 PINS) ------|-------->| [ LAIRD CHOKE L2 ] |          ___________________         | [ SAMTEC ERM8 ]  |
|                     |         |         |          |         |                   |        |                  |
| GND (4 PINS)  ------|-------->| [  eFUSE U1  ] ----|---------|-> 15V Buck Conv --|------->| PINS 11-16 (15V) |
|                     |         |         |          |         |___________________|        |                  |
|                     |         |         |          |                                      |                  |
| CC1 / CC2     ------|--[PD]-->| [STUSB4500 IC] ----|------------------------------------->| PIN 32 (I2C SDA) |
| (Handshake)         |         | (Negotiates 15V)   |                                      | PIN 34 (I2C SCL) |
|_____________________|         |____________________|                                      |__________________|
```

## Power Flow

```text
BULKHEAD ENTRY         OR-ing & PROTECTION         UPS & REGULATION                SAMTEC EXIT
_________________      ____________________       ____________________            _____________

[RJ45 PoE+] ---------> [Ideal Diode 1] --+         [ 2.5F SUPERCAPS ]     +-----> [ +5V BUCK ]
                                         |                 |              |
[USB-C 15V] ---------> [Ideal Diode 2] --+-------> [ TPS259474L EFUSE ] --+-----> [ +3.3V LDO]
                                         |                 |              |
[BATTERY  ] -----------------------------+         [ THERMAL MATRIX ]     +-----> [ PWR_GD   ]
```

## Power Handshake

```text
   POWER MODULE (INTERNAL)             SAMTEC BTB INTERFACE             CONTROLLER BOARD
 ___________________________          _______________________          ___________________ 
| [U1: eFuse 15V IN]        |        |                       |        |                   |
|           |               |        | [ GOLD PINS 1-10 ] ---|------->| [ SYSTEM GND ]    |
| [U2: 5V BUCK (6A)] -------|--------| [ GOLD PINS 11-18 ] --|------->| [ +5V_MAIN ]      |
|           |               |        |                       |        |                   |
| [U3: 3.3V LDO (ENIG)] ----|--------| [ GOLD PINS 19-22 ] --|------->| [ +3V3_ENIG ]     |
|                           |        |                       |        |                   |
| [J2: RJ45 MAGJACK] <------|--------| [ GOLD PINS 23-24 ] <-|--------| [ +3V3_SYSTEM ]   |
| (PoE+ Logic)              |        |                       |        | (Input from CM5)  |
|                           |        |                       |        |                   |
| [U4: SUPERVISOR] ---------|--------| [ GOLD PIN  26 ] -----|------->| [ PWR_GD ]        |
|                           |        |                       |        | (Handshake)       |
|___________________________|        |_______________________|        |___________________|
```

## Trace Connections

```text
EXTERNAL PORTS (REAR)           INTERNAL PROTECTION & STORAGE          CONTROLLER LINK (BTB)
_______________________         _____________________________        _________________________
|                     |         |                           |        |                       |
| [RJ45 PoE+] (48V) --|--[PD]-->| [WE-CMBNC]                |        | [ SAMTEC ERM8 GOLD ]  |
|                     |         |    |                      |        |                       |
| [USB-C] (15V PD) ---|-------->| [CM5022 CHOKE]            |        | PINS 1-10: GND (PWR)  |
|                     |         |    |                      |        | PINS 11-16: +15V RAW  |
| [BATT] (14.4V) -----|-------->| [F1: 72°C TCO]            |        | PINS 17-20: +5V LOGIC |
|_____________________|         |    |                      |        | PINS 21-24: +3.3V LDO |
                                | [U1: TPS259474L eFuse]    |        | PIN  26: PWR_GD (OUT) |
       LADDER RESISTORS:        |    |                      |        | PINS 30-40: I2C/ALARM |
       R1: 732k (UVLO) ---------|--->|                      |        |_______________________|
       R2: 28.7k (OVLO) --------|--->|                      |                    ^
       R3: 53.6k (GND) ---------|--->|                      |                    |
                                |    |                      |                    |
                                | [SUPERCAP BANK (15F x6)] -|----[5V BUCK]-------|
                                |    | (2x3 Block)          |   |[3.3V LDO]------|
                                |    |                      |   |[SUPERVISOR]----|
                                |    |                      |                    |
                                | [5.1V ZENER GLOW] --------|--->[AMBER LED EXT] |
                                |___________________________|        (SAFETY)
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
