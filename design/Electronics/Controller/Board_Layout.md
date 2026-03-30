# Board Layout Visualisations
---

## CM5 Master GPIO & BtB Mapping

### LINK-ALPHA (Power & Entry)

* **Pins 1-20:** Gigabit Ethernet (GND-Shielded Pairs)
* **Pins 21-24:** 3.3V_SYSTEM (Output to Power Module RJ45 Logic)
* **Pins 25-30:** GND Isolation Bank
* **Pins 31-34:** Status LEDs (STATUS_AMBER / STATUS_GREEN)
* **Pins 35-40:** I2C-1 Telemetry (SDA/SCL)
* **Pins 41-44:** 3.3V_ENIG (Input from Power Module)
* **Pins 49-80:** 5V_MAIN / GND (6A DC Delivery Cluster)

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

[ PINS 49 - 80 ] ------------------------> [ 2oz POWER ] -> [ 5V_MAIN (6A DELIVERY)  ]
 (4-Via Thermal Clusters)                  (BULK DC)        (To CM5 VCC_IN)

### LINK-BETA (Encryption & JTAG)

* **Pins 1-12:** JTAG & Reset (GND-Shielded: TCK, TMS, TDI, TDO, RST)
* **Pins 13-20:** GND Isolation Bank
* **Pins 41-46:** ENC_IN [0:5] (6-bit Sniffer Input)
* **Pins 47-52:** ENC_OUT [0:5] (6-bit Sniffer Output)
* **Pins 54-60:** 3.3V_ENIG (Pass-Through Output to Stator)

        LINK-BETA (80-PIN SAMTEC)            SIGNAL TYPE          FUNCTION
_______________________________________    _____________    _____________________________

[ PINS 01 - 12 ] ------------------------> [ 3.3V LOGIC] -> [ JTAG CHAIN & RESET     ]
 (Pattern: GND|TCK|TMS|TDI|TDO|RST|GND)    (SHIELDED)       (To 33+ EPM240 CPLDs)

[ PINS 13 - 20 ] ------------------------> [ ISOLATION ] -> [ MASTER GND BANK        ]

[ PINS 41 - 46 ] ------------------------> [ 3.3V LOGIC] -> [ ENC_IN [0:5] (SNIFFER) ]
 (6-bit Binary Input)                      (SHIELDED)       (Monitoring Keyboard)

[ PINS 47 - 52 ] ------------------------> [ 3.3V LOGIC] -> [ ENC_OUT [0:5] (SNIFFER)]
 (6-bit Binary Output)                     (SHIELDED)       (Monitoring Reflector)

[ PINS 54 - 60 ] ------------------------> [ 2oz POWER ] -> [ 3V3_ENIG (OUTPUT)      ]
 (Direct 2oz Bridge from Alpha)            (CLEAN OUT)      (To Stator/Rotor Logic)
