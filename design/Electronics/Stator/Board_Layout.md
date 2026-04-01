# Stator V1.0 Master Pinout

## J5: REFLECTOR / EXTENSION LINK (20-PIN)

* **Pins 1-4:** 3V3_ENIG / GND Power Bus (2oz Copper)
* **Pins 5-10:** ENC_IN [0:5] (Shielded 1:1 with GND)
* **Pins 11-16:** ENC_OUT [0:5] (Shielded 1:1 with GND)
* **Pin 17:** TDO_RETURN (JTAG return path)
* **Pin 18:** GND (TDO Shield)
* **Pins 19-20:** GND (Electrical end-stop)

## J2-J4: SATELLITE LINKS (40-PIN)

* **Pins 1-4:** 3V3_ENIG / GND Power
* **Pins 5-18:** ENC_IN [0:5] (Symmetrical GND shielding)
* **Pins 21-32:** ENC_OUT [0:5] (Symmetrical GND shielding)
* **Pins 33-40:** JTAG IN/OUT Loop (Shielded TCK/TMS/TDI/TDO)

## Telemetry Layout

```text
[ LINK-BETA (ERF8) ] --(3V3_ENIG)--> [ 20mΩ SHUNT ] --(CLEAN 3V3)--> [ ROTOR BUS ]
              |                         |
              +-- (I2C-1) -- [ INA219 ]-+
```
