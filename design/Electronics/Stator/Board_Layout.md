# Stator V1.0 Master Pinout

## J5: REFLECTOR / EXTENSION LINK (20-PIN)

* **Pins 1-4:** 3V3_ENIG / GND Power Bus (2oz Copper)
* **Pins 5-10:** ENC_IN [0:5] (Shielded 1:1 with GND)
* **Pins 11-16:** ENC_OUT [0:5] (Shielded 1:1 with GND)
* **Pin 17:** TDO_RETURN (JTAG return path)
* **Pin 18:** GND (TDO Shield)
* **Pins 19-20:** GND (Electrical end-stop)
* **Note:** The ENC_IN/ENC_OUT arrangement implements the same bit ordering as the Encoder Data Link and Reflector 16-pin interconnect pinouts (split odd/even ribbon rows for physical 2x8 headers).

## J2-J4: SATELLITE LINKS (40-PIN)

* **Pins 1-4:** 3V3_ENIG / GND Power
* **Pins 5-18:** ENC_IN [0:5] (Symmetrical GND shielding)
* **Pins 21-32:** ENC_OUT [0:5] (Symmetrical GND shielding)
* **Pins 33-40:** JTAG IN/OUT Loop (Shielded TCK/TMS/TDI/TDO)

## LINK-BETA (80-PIN ERF8) Explicit Mapping

* **Pins 1-9:** JTAG + Reset (GND|TCK|GND|TMS|GND|TDI|GND|RST|GND)
* **Pins 10-20:** Ground isolation bank
* **Pins 21-24:** 3V3_SYSTEM / status power paths (control signals to controller)
* **Pins 25-26:** ETH_LED_LINK / ETH_LED_ACT
* **Pins 27-30:** GND
* **Pins 31-34:** Status I/O / PWR_GD / I2C_return
* **Pins 35-38:** I2C1 (SDA/SCL) telemetry chain
* **Pins 39-44:** 3V3_ENIG input from Power Module (via Controller pass-through)
* **Pins 41-46:** ENC_IN [0:5] (sniffer from Controller)
* **Pins 47-52:** ENC_OUT [0:5] (sniffer to Controller)
* **Pins 54-60:** 3V3_ENIG output to Stator power tree
* **Pins 49-80:** 5V_MAIN / additional GND (not typically used by Stator logic)

## Telemetry Layout

```text
[ LINK-BETA (ERF8) ] --(3V3_ENIG)--> [ 20mΩ SHUNT ] --(CLEAN 3V3)--> [ ROTOR BUS ]
              |                         |
              +-- (I2C-1) -- [ INA219 ]-+
```
