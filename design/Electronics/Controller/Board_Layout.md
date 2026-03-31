# Board Layout Visualisations

---

## CM5 Master GPIO & BtB Mapping

### LINK-ALPHA (To Power Module)

* **Pins 1-20:** Gigabit Ethernet (GND-Shielded: GND|DA+/-|GND|DB+/-|GND...)
* **Pins 21-24:** 3.3V_SYSTEM (Output from CM5 to Power Module RJ45 Logic)
* **Pins 25-30:** GND Isolation Moat
* **Pins 31-34:** Status LEDs (STATUS_AMBER / STATUS_GREEN)
* **Pins 35-40:** I2C-1 Telemetry (SDA/SCL to PD/eFuse)
* **Pins 41-44:** 3.3V_ENIG (Input from Power Module - Pass-Through)
* **Pin 45:** BATT_PRES_N (Battery Presence Detection - Active Low)
* **Pins 49-80:** 5V_MAIN / GND (6A Delivery Cluster - 4-via Thermal Clusters)

```text
       LINK-ALPHA (80-PIN SAMTEC)           SIGNAL TYPE          FUNCTION
_______________________________________    _____________    _____________________________

[ PINS 01 - 20 ] ------------------------> [ 100Ω DIFF ] -> [ GIGABIT ETHERNET (GBE) ]
 (Pattern: GND|DA+/-|GND|DB+/-|GND...)     (SHIELDED)       (To External RJ45)

[ PINS 21 - 24 ] ------------------------> [ 2oz POWER ] -> [ 3V3_SYSTEM (RETURN)    ]
                                           (CLEAN OUT)      (Powers PoE+ Logic)

[ PINS 25 - 30 ] ------------------------> [ ISOLATION ] -> [ MASTER GND BANK        ]

[ PINS 31 - 34 ] ------------------------> [ 3.3V LOGIC] -> [ STATUS AMBER / GREEN   ]
                                           (GPIO OUT)       (To Power Module LEDs)

[ PINS 35 - 40 ] ------------------------> [ I2C BUS   ] -> [ TELEMETRY (SDA/SCL)    ]
                                           (SHIELDED)       (To PD Emulator/eFuse)

[ PINS 41 - 44 ] ------------------------> [ 2oz POWER ] -> [ 3V3_ENIG (INPUT)       ]
                                           (CLEAN IN)       (From Power Module LDO)

[ PIN  45      ] ------------------------> [ 3.3V LOGIC] -> [ BATT_PRES_N            ]
                                           (GPIO IN)        (From Power Module Batt)

[ PINS 49 - 80 ] ------------------------> [ 2oz POWER ] -> [ 5V_MAIN (6A DELIVERY)  ]
 (4-Via Thermal Clusters)                  (BULK DC)        (To CM5 VCC_IN)
```

### LINK-BETA (To Stator Board)

* **Pins 1-9:** JTAG & Reset (GND-Shielded: GND|TCK|GND|TMS|GND|TDI|GND|RST|GND)
* **Pins 10-20:** GND Isolation Bank
* **Pins 41-46:** ENC_IN [0:5] (6-bit Sniffer Input)
* **Pins 47-52:** ENC_OUT [0:5] (6-bit Sniffer Output)
* **Pins 54-60:** 3.3V_ENIG (Pass-Through Output to Stator)

```text
  LINK-BETA (80-PIN SAMTEC)                         SIGNAL TYPE       FUNCTION
_______________________________________________    _____________    _____________________________

[ PINS 01 - 09 ] --------------------------------> [ 3.3V LOGIC] -> [ JTAG CHAIN & RESET     ]
 (Pattern: GND|TCK|GND|TMS|GND|TDI|GND|RST|GND)    (SHIELDED)       (To 33+ EPM240 CPLDs)

[ PINS 10 - 20 ] --------------------------------> [ ISOLATION ] -> [ MASTER GND BANK        ]

[ PINS 41 - 46 ] --------------------------------> [ 3.3V LOGIC] -> [ ENC_IN [0:5] (SNIFFER) ]
 (6-bit Binary Input)                              (SHIELDED)       (Monitoring Keyboard)

[ PINS 47 - 52 ] --------------------------------> [ 3.3V LOGIC] -> [ ENC_OUT [0:5] (SNIFFER)]
 (6-bit Binary Output)                             (SHIELDED)       (Monitoring Reflector)

[ PINS 54 - 60 ] --------------------------------> [ 2oz POWER ] -> [ 3V3_ENIG (OUTPUT)      ]
 (Direct 2oz Bridge from Alpha)                    (CLEAN OUT)      (To Stator/Rotor Logic)
```

### BtB Connectivity Routing

```text
      REAR INTERFACE (POWER & ENTRY)                     CONTROLLER CORE (L1-L6)                   RIGHT-BANK (USER I/O)
 _____________________________________________        ________________________________        _____________________________
| [R]                                     [R] |      |                                |      |                         [R] |
| (O) [  LINK-ALPHA (ERF8-040)  ] --(5V/GBE)--|----->| [ CM5 COMPUTE MODULE ]         |      | (O)                         |
| (1)  (Female Socket / 80-pin)               |      |  (Wireless/8GB/32GB)           |      | (3)                         |
|        |                 |                  |      |                                |      |                             |
|  [ +3V3_ENIG ]     [ SNIFFER BUS (12-bit) ] |<---->| [ 12-bit GPIO ]  [ 100Ω HDMI ] |      |                             |
|  (2oz L3 BRIDGE)   (6-In / 6-Out Binary)    |      |                        |       |      |                             |
|       |                                     |      |                  [ AP2331W   ] |      |                             |
|       |       [ JTAG DAUGHTERBOARD ]        |      |                  [ TPD4E05U06] |------|------> [ HDMI TYPE-A  ]     |
|       |        (1x6 & 1x10 Headers)         |      |                                |      |        [   2007435-1  ]     |
|       |           |            |            |      |                [ 90Ω USB 3.0 ] |      |        [  (PROTRUDES) ]     |
|       |       [ JTAG BUS ]  [ USB 2.0 ] ----|----->|                        |       |      |        [ 5.0mm OVER   ]     |
|       |           |                         |      |                [ TPS2065C ]    |      |                             |
|    [  LINK-BETA  (ERM8-040)  ]              |      |                [ TPD4E05U06 ]  |------|------> [ USB 3.0 DUAL ]     |
|      (Male Header / 80-pin)                 |      |                                |      |        [   STACKED    ]     |
|                                             |      |                                |      |        [   48406-0003 ]     |
|                                             |      |                                |      |        [  (PROTRUDES) ]     |
| (O)                    [ DIAG BANK (2x8) ]  |      |                                |      |        [ 5.0mm OVER   ]     |
| (4)                      (Exposed ENIG)     |      |                                |      | (O)   (V1.0) DATA PLATE (2) |
|_____________________________________________|      |________________________________|      |_____________________________|
 (O) = M3 Star-Burst Grounding PTH                   [R] = 2.0mm Fillet Corner               (1-4) = Star-Pattern Torque Sequence
```

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
