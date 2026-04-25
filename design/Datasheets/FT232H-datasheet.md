# FT232H - Single-channel Hi-Speed USB to multipurpose UART / FIFO IC

## Source Reference

- Source PDF: [FT232H-datasheet.pdf](FT232H-datasheet.pdf)
- Source path: `design\Datasheets\FT232H-datasheet.pdf`
- Generated markdown: `FT232H-datasheet.md`
- Review note: manually checked against the source PDF; curated summary added and the raw page-by-page extraction is preserved below.

## Part Identity and Ordering

- FTDI `FT232H`, datasheet version 2.1, document `FT_000288`.
- Single-channel USB 2.0 Hi-Speed (480 Mb/s) bridge configurable as UART, FIFO, FT1248, bit-bang, fast serial, CPU-style FIFO, or MPSSE interface.
- Reviewed part / package identities:
  - `FT232HL-xxxx` - 48-pin LQFP.
  - `FT232HQ-xxxx` - 48-pin QFN.
- Packaging code note from the PDF: `xxxx` captures tray vs reel packing; LQFP is 1500 per reel or 250 per tray, QFN is 3000 per reel or 260 per tray.

## Pin / Pad Designations

- Mode-dependent bus pins on pages 9-10:
  - `ADBUS0..7` map to UART data / modem signals, FIFO data `D0..D7`, MPSSE pins, fast-serial pins, or FT1248 data lanes depending on mode.
  - `ACBUS0..9` provide mode-control, FIFO strobes, GPIO, LED, clock, and power-save options depending on EEPROM configuration.
- Common pins on page 11:
  - `VREGIN` pin 40, `VCCA` pin 37, `VCORE` pin 38, `VCCD` pin 39.
  - `VCCIO` pins 12 / 24 / 46, `VPLL` pin 8, `VPHY` pin 3.
  - `OSCI` pin 1, `OSCO` pin 2, `REF` pin 5, `DM` pin 6, `DP` pin 7.
  - `RESET#` pin 34 and `PWRSAV#` pin 31.
- `REF` requires a 12 kohm, 1% resistor to GND.

## Ratings and Operating Conditions

- USB 2.0 compliant, USB-IF Test ID `40770005`.
- Ambient operating temperature: -40 deg C to +85 deg C.
- `VCORE` operating supply: 1.62 V to 1.98 V (1.8 V nominal).
- `VCCIO` operating supply: 2.97 V to 3.63 V; I/O cells are 5 V tolerant except USB PHY pins.
- `VREGIN` supported as either 5 V input (3.6 V to 5.5 V) or 3.3 V input (3.0 V to 3.6 V, revision-dependent note in datasheet).
- Core current examples from the datasheet: about 24 mA normal, 4.3 mA reset, 330 uA suspend.
- Configurable I/O drive strength and slew control are called out in the feature list.

## Package and Mechanical Notes

- The device is offered in lead-free 48-pin LQFP and QFN packages.
- Section 8 of the PDF contains the detailed package mechanical data; the searchable raw extraction for those pages is preserved below.

## Formulas / Configuration Notes

- No primary analog design equations are central to this datasheet.
- The PDF does call out configuration-dependent USB signal timing adjustment through EEPROM settings and passive components on the USB lines.

## Applications and Reference Design Content

- Typical uses include USB-to-UART, synchronous / asynchronous FIFO, FT1248, CPU-style FIFO, and MPSSE-based serial engines.
- CBUS options include `TXDEN`, `PWREN#`, `TXLED#`, `RXLED#`, `SLEEP#`, and 30 MHz / 15 MHz / 7.5 MHz clock outputs.
- The PDF includes explicit USB bus-powered and self-powered reference configurations, including the `PWRSAV#` / EEPROM interaction used in self-powered designs.

## Searchability Note

- The raw page-by-page extraction below is intentionally preserved for local text search.
- Mode-dependent pin tables are wide and wrap heavily in plain text; verify final pin use against the PDF tables when assigning signals.

## Page-by-Page Extracted Text

### Page 1

```text
Copyright (c) Future Technology Devices International Limited  1
FT232H SINGLE CHANNEL HI-SPEED USB TO MULTIPURPOSE
UART/FIFO IC Datasheet
Version 2.1

Document No.: FT_000288 Clearance No.: FTDI #199
Future Technology
Devices International Ltd
FT232H Single Channel Hi-
Speed USB to Multipurpose
UART/FIFO IC

The FT232H is a single channel  USB 2.0 Hi -Speed
(480Mb/s) to UART/FIFO IC. It has the capability of
being configured in a variety of industry standard
serial or parallel interfaces.  The FT232H has the
following advanced features:
- Single channel USB to serial / parallel ports
with a variety of configurations.
- Entire USB protocol handled on the chip.  No
USB specific firmware programming required.
- USB 2.0 Hi -Speed (480Mbits/Second) and Full
Speed (12Mbits/Second) compatible.
- Multi-Protocol Synchronous Serial Engine
(MPSSE) to simplify synchronous serial protocol
(USB to JTAG, I 2C, SPI (MASTER) or bit-bang)
design.
- UART transfer data rate up to 12Mbaud.
(RS232 Data Rate limited by external level
shifter).
- USB to asynchronous 245 FIFO mode for
transfer data rate up to 8 Mbyte/Sec.
- USB to synchronous 245 parallel FIFO mode for
transfers up to 40 Mbytes/Sec
- Supports a proprietary half duplex FT1248
interface with a configurable width, bi-
directional data bus (1, 2, 4 or 8 bits wide).
- CPU-style FIFO interface mode simplifies CPU
interface design.
- Fast serial interface option.
- FTDI's royalty-free Virtual Com Port (VCP) and
Direct (D2XX) drivers eliminate the
requirement for USB driver development in
most cases.
- Adjustable receive buffer timeout.

- Option for transmit and receive LED drive
signals.
- Bit-bang Mode interface option with RD# and
WR# strobes
- Highly integrated design includes 5V to
3.3/+1.8V LDO regulator for VCORE, integrated
POR function
- Asynchronous serial UART interface option with
full hardware handshaking and modem
interface signals.
- Fully assisted hardware or X -On / X -Off
software handshaking.
- UART Interface supports 7/8 bit data, 1/2 stop
bits, and Odd/Even/Mark/Space/No Parity.
- Auto transmit enable control for RS485 serial
applications using the TXDEN pin.
- Operational mode  configuration and USB
Description strings configurable in exter nal
EEPROM over the USB interface.
- Configurable I/O drives strength (4, 8, 12 or
16mA) and slew rate.
- Low operating and USB suspend current.
- Supports self-powered, bus powered and high -
power bus powered USB configurations.
- UHCI/OHCI/EHCI host controller compatible.
- USB Bulk data transfer mode (512 byte packets
in Hi-Speed mode).
- +1.8V (chip core) and +3.3V I/O interfacing
(+5V Tolerant).
- Extended -40 degC to 85 degC industrial operating
temperature range.
- Compact 48 -pin Lead Free LQFP or QFN
package
- Configurable ACBUS I/O pins.

Neither the whole nor any part of the information contained in, or the product described in this
manual, may be adapted or re produced
in any material or electronic form without the prior written consent of the copyright holder. This
product and its documen tation are
supplied on an as-is basis and no warranty as to their suitability for any particular purpose is
either made or implied. Future Technology
Devices International Ltd will not accept any claim for damages howsoever arising as a result of use
or fa ilure of this product. Your
statutory rights are not affected. This product or any variant of it is not intended for use in any
medical appliance, device  or system in
which the failure of the product might reasonably be expected to result in personal injur y. This
document provides preliminary
information that may be subject to change without notice. No freedom to use patents or other
intellectual property rights is implied by
the publication of this document. Future Technology Devices International Ltd, Uni t 1, 2 Seaward
Place, Centurion Business Park,
Glasgow G41 1HH United Kingdom. Scotland Registered Company Number: SC136640
```

### Page 2

```text
Copyright (c) Future Technology Devices International Limited  2
FT232H SINGLE CHANNEL HI-SPEED USB TO MULTIPURPOSE
UART/FIFO IC Datasheet
Version 2.1

Document No.: FT_000288 Clearance No.: FTDI #199
1 Typical Applications
- Single chip USB to UART (RS232, RS422 or
RS485)
- USB to FIFO
- USB to FT1248
- USB to JTAG
- USB to SPI
- USB to I2C
- USB to Bit-Bang
- USB to Fast Serial Interface
- USB to CPU target interface (as memory)

- USB Instrumentation
- USB Industrial Control
- USB EPOS Control
- USB MP3 Player Interface
- USB FLASH Card Reader / Writers
- Set Top Box - USB interface
- USB Digital Camera Interface
- USB Bar Code Readers
1.1 Driver Support
The FT232H requires USB device drivers (listed below), available free from http://www.ftdichip.com,
to
operate. The VCP version of the driver creates a Virtual COM Port allowing legacy serial port
applications
to operate over USB e.g. serial emulator application TTY. Another FTDI USB driver, the D2XX driver,
can
also be used with application software to directly access the FT232H through a DLL.

Royalty free VIRTUAL COM PORT
(VCP) DRIVERS for...
- Windows 10 and Windows 10 64-bit
- Windows 8 and Windows 8 64-bit
- Windows 7 and Windows 7 64-bit
- Windows Vista and Vista 64-bit
- Windows XP and XP 64-bit
- Windows XP Embedded
- Windows 2000, Server 2003, Server 2008
- Windows CE 4.2, 5.0, 5.2 and 6.0
- Mac OS-X
- Linux (2.6.39 or later)

Royalty free D2XX Direct Drivers
(USB Drivers + DLL S/W Interface)
- Windows 10 and Windows 10 64-bit
- Windows 8 and Windows 8 64-bit
- Windows 7 and Windows 7 64-bit
- Windows Vista and Vista 64-bit
- Windows XP and XP 64-bit
- Windows XP Embedded
- Windows 2000, Server 2003, Server 2008
- Windows CE 4.2, 5.0, 5.2 and 6.0
- Mac OS-X
- Linux (2.6.32 or later)
```

### Page 3

```text
Copyright (c) Future Technology Devices International Limited  3
FT232H SINGLE CHANNEL HI-SPEED USB TO MULTIPURPOSE
UART/FIFO IC Datasheet
Version 2.1

Document No.: FT_000288 Clearance No.: FTDI #199
1.2 Part Numbers
Part Number Package
FT232HL -xxxx 48 Pin LQFP
FT232HQ-xxxx 48 Pin QFN

Note: Packaging codes for xxxx is:

- Reel: Taped and Reel (LQFP = 1500 pieces per reel, QFN = 3000 pieces per reel)
- Tray: Tray packing, (LQFP = 250 pieces per tray, QFN =260 pieces per tray)

Please refer to section 8 for all package mechanical parameters.

1.3 USB Compliant
The FT2 32H is fully compliant with the USB 2.0 specification and has been given the USB -IF Test
-ID
(TID) 40770005.

The timing of the rise/fall time of the USB signals is not only dependant on the USB signal drivers,
it is
also dependant system and is affected by factors such as PCB layout, external components and any
transient protection present on the USB signals. For  USB compliance these may require a slight
adjustment.  This timing can be modified through a programmable setting stored in the same external
EEPROM that is used for the USB descriptors.   Timing can also be changed by adding appropriate
passive
components to the USB signals.
```

### Page 4

```text
Copyright (c) Future Technology Devices International Limited  4
FT232H SINGLE CHANNEL HI-SPEED USB TO MULTIPURPOSE
UART/FIFO IC Datasheet
Version 2.1

Document No.: FT_000288 Clearance No.: FTDI #199
2 FT232H Block Diagram

Figure 2.1 FT232H Block Diagram

A full description of each function is available in section 4.
```

### Page 5

```text
Copyright (c) Future Technology Devices International Limited  5
FT232H SINGLE CHANNEL HI-SPEED USB TO MULTIPURPOSE
UART/FIFO IC Datasheet
Version 2.1

Document No.: FT_000288 Clearance No.: FTDI #199
Table of Contents
1 Typical Applications ....................................................... 2
1.1 Driver Support ........................................................................... 2
1.2 Part Numbers ............................................................................. 3
1.3 USB Compliant ........................................................................... 3
2 FT232H Block Diagram .................................................. 4
3 Device Pin Out and Signal Descriptions ......................... 8
3.1 Schematic Symbol ...................................................................... 8
3.2 FT232H  Pin Descriptions ........................................................... 9
3.3 Signal Description .................................................................... 11
3.4 ACBUS Signal Option ................................................................ 13
3.5 Pin Configurations ................................................................... 14
3.5.1 FT232H pins used in an UART interface ........................................................
14
3.5.2 FT232H Pins used in an FT245 Synchronous FIFO Interface ............................ 14
3.5.3 FT232H Pins used in an FT245 Style aynchronous FIFO Interface .................... 15
3.5.4 FT232H Configured as a Synchronous or Asynchronous Bit-Bang Interface ....... 16
3.5.5 FT232H Pins used in an MPSSE
................................................................... 16
3.5.6 FT232H Pins used as a Fast Serial Interface ..................................................
17
3.5.7 FT232H Pins Configured as a CPU-style FIFO Interface ................................... 18
3.5.8 FT232H Pins Configured as a FT1248 Interface ............................................. 18
4 Function Description ................................................... 19
4.1 Key Features ............................................................................ 19
4.2 Functional Block Descriptions .................................................. 20
4.3 FT232 UART Interface Mode Description .................................. 21
4.3.1 RS232 Configuration
.................................................................................. 21
4.3.2 RS422 Configuration
.................................................................................. 22
4.3.3 RS485 Configuration
.................................................................................. 23
4.4 FT245 Synchronous FIFO Interface Mode Description .............. 24
4.4.1 FT245 Synchronous FIFO Read Operation ..................................................... 25
4.4.2 FT245 Synchronous FIFO Write Operation .................................................... 25
4.5 FT245 Style Asynchronous FIFO Interface Mode Description ... 26
4.6 FT1248 Interface Mode Description ......................................... 27
4.6.1 Bus Width Protocol Decode
......................................................................... 28
4.6.2 FT1248: 1-bit interface
.............................................................................. 29
4.7 Synchronous and Asynchronous Bit-Bang Interface Mode ....... 30
```

### Page 6

```text
Copyright (c) Future Technology Devices International Limited  6
FT232H SINGLE CHANNEL HI-SPEED USB TO MULTIPURPOSE
UART/FIFO IC Datasheet
Version 2.1

Document No.: FT_000288 Clearance No.: FTDI #199
4.7.1 Asynchronous Bit-Bang Mode
...................................................................... 30
4.7.2 Synchronous Bit-Bang Mode
....................................................................... 30
4.8 MPSSE Interface Mode Description .......................................... 32
4.8.1 MPSSE Adaptive Clocking
........................................................................... 33
4.9 Fast Serial Interface Mode Description .................................... 34
4.9.1 Outgoing Fast Serial Data
.......................................................................... 35
4.9.2 Incoming Fast Serial Data
.......................................................................... 35
4.9.3 Fast Serial Data Interface Example
.............................................................. 36
4.10 CPU-style FIFO Interface Mode Description ........................... 36
4.11 RS232 UART Mode LED Interface Description ........................ 38
4.12 Send Immediate/Wake Up (SIWU#) ..................................... 39
4.13 FT232H Mode Selection ......................................................... 40
4.14 Modes Configuration ............................................................. 40
5 Devices Characteristics and Ratings ............................ 41
5.1 Absolute Maximum Ratings ...................................................... 41
5.2 DC Characteristics .................................................................... 41
5.3 ESD Tolerance .......................................................................... 43
6 FT232H Configurations ................................................ 44
6.1 USB Bus Powered Configuration .............................................. 44
6.2 USB Self Powered Configuration .............................................. 45
6.2.1 Self-Powered Application Example 1
............................................................ 45
6.2.2 Self-Powered Application Example 2
............................................................ 46
6.3 Oscillator Configuration ........................................................... 47
7 EEPROM Configuration................................................. 48
7.1 EEPROM Interface .................................................................... 48
7.2 Default EEPROM Configuration ................................................. 48
8 Package Parameters .................................................... 50
FT232HQ, QFN-48 Package Dimensions ...................................... 50
8.1
...................................................................................................
50
8.2 FT232HL, LQFP-48 Package Dimensions .................................. 51
8.3 Solder Reflow Profile ............................................................... 52
9 Contact Information .................................................... 54
Appendix A - References ................................................... 55
Document References ...................................................................... 55
```

### Page 7

```text
Copyright (c) Future Technology Devices International Limited  7
FT232H SINGLE CHANNEL HI-SPEED USB TO MULTIPURPOSE
UART/FIFO IC Datasheet
Version 2.1

Document No.: FT_000288 Clearance No.: FTDI #199
Acronyms and Abbreviations ............................................................ 55
Appendix B - List of Figures and Tables ............................. 56
List of Tables ....................................................................................
56
List of Figures ..................................................................................
57
Appendix C - Revision History ........................................... 58
```

### Page 8

```text
Copyright (c) Future Technology Devices International Limited  8
FT232H SINGLE CHANNEL HI-SPEED USB TO MULTIPURPOSE
UART/FIFO IC Datasheet
Version 2.1

Document No.: FT_000288 Clearance No.: FTDI #199
3 Device Pin Out and Signal Descriptions
The 48-pin LQFP and 48-pin QFN have the same pin numbering for specific functions. This pin
numbering
is illustrated in the schematic symbol shown in Figure 3.1.

3.1 Schematic Symbol

Figure 3.1 FT232H Schematic Symbol
```

### Page 9

```text
Copyright (c) Future Technology Devices International Limited  9
FT232H SINGLE CHANNEL HI-SPEED USB TO MULTIPURPOSE
UART/FIFO IC Datasheet
Version 2.1

Document No.: FT_000288 Clearance No.: FTDI #199
3.2 FT232H  Pin Descriptions
This section describes the operation of the FT232H pins. Both the LQFP and the QFN packages have the
same function on each pin. The function of many pins is determined by the configuration of the
FT232H.
The following table details the function of each pin  dependent on the configuration of the
interface. Each
of the functions is described in the following table (Note: The convention used throughout this
document
for active low signals is the signal name followed by #).

Pins marked * require an EEPROM for assignment to these functions.  Default is Tristate, Pull-Up

Pins marked ** default to tri-stated inputs with an internal 75Kohm (approx.) pull up resistor to
VCCIO.

Pin marked *** default to GPIO line with an internal 75Kohm pull down resistor to GND. Using the
EEPROM
this pin can be enabled USBVCC mode instead of GPIO mode.

FT232H
Pin Pin functions (depends on configuration)
Pin
#
Pin
Name
ASYNC
Serial
(RS232)
SYNC
245
FIFO
STYLE
ASYNC
245
FIFO
ASYNC
Bit-bang
SYNC
Bit-bang MPSSE
Fast
Serial
 interface
CPU
Style
 FIFO
FT1248
13 ADBUS
0 TXD D0 D0 D0 D0 TCK/SK FSDI D0 MIOSI0
14 ADBUS
1 RXD D1 D1 D1 D1 TDI/DO FSCLK D1 MIOSI1
15 ADBUS
2 RTS# D2 D2 D2 D2 TDO/DI FSDO D2 MIOSI2
16 ADBUS
3 CTS# D3 D3 D3 D3 TMS/CS FSCTS D3 MIOSI3
17 ADBUS
4 DTR# D4 D4 D4 D4 GPIOL0 **
TriSt-UP D4 MIOSI4
18 ADBUS
5 DSR# D5 D5 D5 D5 GPIOL1 **
TriSt-UP D5 MIOSI5
19 ADBUS
6 DCD# D6 D6 D6 D6 GPIOL2 **
TriSt-UP D6 MIOSI6
20 ADBUS
7 RI# D7 D7 D7 D7 GPIOL3 **
TriSt-UP D7 MIOSI7
21 ACBUS
0
*
TXDEN RXF# RXF# ACBUS0 ACBUS0 GPIOH0 **
ACBUS0 CS# SCLK
25 ACBUS
1
**
ACBUS1 TXE# TXE# WRSTB# WRSTB# GPIOH1 **
ACBUS1 A0 SS_n
26 ACBUS
2
**
ACBUS2 RD# RD# RDSTB# RDSTB# GPIOH2 **
ACBUS2 RD# MISO
27 ACBUS
3
*
RXLED# WR# WR# ACBUS3 ACBUS3 GPIOH3 **
ACBUS3 WR# ACBUS3
28 ACBUS
4
*
TXLED# SIWU# SIWU# SIWU# SIWU# GPIOH4 SIWU# Note1 ACBUS4
29 ACBUS
5
**
ACBUS5 CLKOUT ACBUS5 **
ACBUS5
**
ACBUS5 GPIOH5 **
ACBUS5
**
ACBUS
5
ACBUS5
30 ACBUS
6
**
ACBUS6 OE# ACBUS6 ACBUS6 ACBUS6 GPIOH6 **
ACBUS6
**
ACBUS
6
ACBUS6
31 ACBUS
7

WRSAV#
PWRSAV
#
PWRSAV
#
PWRSAV
#
PWRSAV
#
***
GPIOH7 PWRSAV# PWRSA
V#
PWRSAV
#
32 ACBUS
8
**
ACBUS8
**
ACBUS8
**
ACBUS8
**
ACBUS8
**
ACBUS8
**
ACBUS
8
**
ACBUS8
**
ACBUS
8
ACBUS8
33 ACBUS
9
**
ACBUS9
**
ACBUS9
**
ACBUS9
**
ACBUS9
**
ACBUS9
**
ACBUS
9
**
ACBUS9
**
ACBUS
9
ACBUS9
```

### Page 10

```text
Copyright (c) Future Technology Devices International Limited  10
FT232H SINGLE CHANNEL HI-SPEED USB TO MULTIPURPOSE
UART/FIFO IC Datasheet
Version 2.1

Document No.: FT_000288 Clearance No.: FTDI #199

Note1: To wake up the USB device in this mode, put ACBUS0 from "High" to "LOW", set ACBUS1 "High",
and put ACBUS3 from "High" to "LOW".

Note: Initial Pin States - The device will start up as a UART port. Therefore pins which are output
in
UART mode will be driving out. If an application uses MPSSE or bit-bang, ensure that any external
signals
do not drive into these pins and cause contention until the application has configured the mode and
direction of these lines. If a different mode other than UART is set in  the EEPROM, the pins will
change to
the selected mode after the device has read the EEPROM.
```

### Page 11

```text
Copyright (c) Future Technology Devices International Limited  11
FT232H SINGLE CHANNEL HI-SPEED USB TO MULTIPURPOSE
UART/FIFO IC Datasheet
Version 2.1

Document No.: FT_000288 Clearance No.: FTDI #199
3.3 Signal Description
The operation of the following FT232H pins are the same regardless of the configured mode:-

Pin No. Name Type Description
40 **
VREGIN
POWER
input +5.0V or 3V3 power supply input.
37 VCCA POWER
output
+1.8V output.  Should not be used. Terminate with
0.1uF capacitor to GND
38 VCORE POWER
output
+1.8V output.  Should not be used. Terminate with a
0.1uF capacitor to GND
39 **
VCCD
POWER
output
or input
+3.3V output or input.
12, 24, 46 VCCIO POWER
input +3.3V input.  I/O interface power supply input
8 VPLL POWER
Input
+3.3V input. Internal PLL power supply input. It is
recommended that this supply is filtered using an LC
filter. (See figure 6.1)
3 VPHY POWER
Input
+3.3V input. Internal USB PHY power supply input. Note
that this cannot be connected directly to the USB
supply. A +3.3V regulator must be used. It is
recommended that this supply is filtered using an LC
filter.(See figure 6.1)
4,9,41 AGND POWER
Input 0V Ground input.
10,11,22,23,35,36,47,48 GND POWER
Input 0V Ground input.
Table 3.1 Power and Ground

** If pin 40 (VREGIN) is +5.0V, pin 39 becomes an output and If pin 40 (VREGIN) is 3V3 pin 39
becomes
an input.

Pin No. Name Type Description
1 OSCI INPUT Oscillator input.
2 OSCO OUTPUT Oscillator output.
5 REF INPUT Current reference - connect via a 12Kohm resistor @ 1% to
GND.
6 DM I/O USB Data Signal Minus.
7 DP I/O USB Data Signal Plus.
42 TEST INPUT IC test pin - for normal operation must be connected to
GND.
34 RESET# INPUT Reset input (active low).
31 PWRSAV# INPUT
USB Power Save input. This is an EEPROM configurable
option which is set using a 'Suspend on ACBus7 Low' bit in
FT_PROG.  This option is available when the FT232H is on a
self-powered mode and is used to prevent forcing current
down the USB lines when the host or hub is powered off.
PWRSAV# = 1 : Normal Operation
PWRSAV# = 0 : FT232H forced into SUSPEND mode.
PWRSAV# can be connected to VBUS of the USB connector
(via a 39Kohm resistor). When this input goes high, then it
indicates to the FT232H that it is connected to a host PC.
When the host or hub is powered down then the FT232H is
held in SUSPEND mode.
Table 3.2 Common Function Pins
```

### Page 12

```text
Copyright (c) Future Technology Devices International Limited  12
FT232H SINGLE CHANNEL HI-SPEED USB TO MULTIPURPOSE
UART/FIFO IC Datasheet
Version 2.1

Document No.: FT_000288 Clearance No.: FTDI #199
Pin No. Name Type Description
45 EECS I/O EEPROM - Chip Select. Tri-State during device reset.
44 EECLK OUTPUT Clock signal to EEPROM. Tri-State during device reset. When not in
reset, this outputs the EEPROM clock.
43 EEDATA I/O
EEPROM - Data I/O.  Connect directly to Data-in of the EEPROM and to
Data-out of the EEPROM via a 2.2K resistor. Also, pull Data-Out of the
EEPROM to VCCD via a 10K resistor for correct operation. Tri-State
during device reset.
Table 3.3 EEPROM Interface Group

Pin No. Name Type Description
13 ADBUS0 Output Configurable Output Pin, the default configuration is Transmit
Asynchronous Data Output.
14 ADBUS1 Input Configurable Input Pin, the default configuration is Receiving
Asynchronous Data Input.
15 ADBUS2 Output Configurable Output Pin, the default configuration is Request to Send
Control Output / Handshake Signal.
16 ADBUS3 Input Configurable Input Pin, the default configuration is Clear To Send Control
Input / Handshake Signal.
17 ADBUS4 Output Configurable Output Pin, the default configuration is Data Terminal Ready
Control Output / Handshake Signal.
18 ADBUS5 Input Configurable Input Pin, the default configuration is Data Set Ready
Control Input / Handshake Signal.
19 ADBUS6 Input Configurable Input Pin, the default configuration is Data Carrier Detect
Control Input.
20 ADBUS7 Input
Configurable Input Pin, the default configuration is Ring Indicator Control
Input. When remote wake up is enabled in the EEPROM taking RI# low
can be used to resume the PC USB host controller from suspend. (Also
see note 1, 2, 3 in section 4.12)
21 ACBUS0 I/O
Configurable ACBUS I/O Pin. Function of this pin is configured in the
device EEPROM. If the external EEPROM is not fitted the default
configuration is TriSt-PU. See ACBUS Signal Options, Table 3.5.
25 ACBUS1 I/O
Configurable ACBUS I/O Pin. Function of this pin is configured in the
device EEPROM. If the external EEPROM is not fitted the default
configuration is TriSt-PU. See ACBUS Signal Options, Table 3.5.
26 ACBUS2 I/O
Configurable ACBUS I/O Pin. Function of this pin is configured in the
device EEPROM. If the external EEPROM is not fitted the default
configuration is TriSt-PU. See ACBUS Signal Options, Table 3.5.
27 ACBUS3 I/O
Configurable ACBUS I/O Pin. Function of this pin is configured in the
device EEPROM. If the external EEPROM is not fitted the default
configuration is TriSt-PU. See ACBUS Signal Options, Table 3.5.
28 ACBUS4 I/O
Configurable ACBUS I/O Pin. Function of this pin is configured in the
device EEPROM. If the external EEPROM is not fitted the default
configuration is TriSt-PU. See ACBUS Signal Options, Table 3.5.
29 ACBUS5 I/O
Configurable ACBUS I/O Pin. Function of this pin is configured in the
device EEPROM. If the external EEPROM is not fitted the default
configuration is TriSt-PU. See ACBUS Signal Options, Table 3.5.
30 ACBUS6 I/O
Configurable ACBUS I/O Pin. Function of this pin is configured in the
device EEPROM. If the external EEPROM is not fitted the default
configuration is TriSt-PU. See ACBUS Signal Options, Table 3.5.
31 ACBUS7 I/O
Configurable ACBUS I/O Pin. Function of this pin is configured in the
device EEPROM. If the external EEPROM is not fitted the default
configuration is TriSt-PD. See ACBUS Signal Options, Table 3.5.
32 ACBUS8 I/O
Configurable ACBUS I/O Pin. Function of this pin is configured in the
device EEPROM. If the external EEPROM is not fitted the default
configuration is TriSt-PU. See ACBUS Signal Options, Table 3.5.
33 ACBUS9 I/O
Configurable ACBUS I/O Pin. Function of this pin is configured in the
device EEPROM. If the external EEPROM is not fitted the default
configuration is TriSt-PU. See ACBUS Signal Options, Table 3.5.

Table 3.4 UART Interface and ACBUS Group (see note 1)
```

### Page 13

```text
Copyright (c) Future Technology Devices International Limited  13
FT232H SINGLE CHANNEL HI-SPEED USB TO MULTIPURPOSE
UART/FIFO IC Datasheet
Version 2.1

Document No.: FT_000288 Clearance No.: FTDI #199
Notes:

When used in Input Mode, the input pins are pulled to VCCIO via internal 75kohm (approx.) resistors.
These
pins can be programmed to gently pull low during USB suspend (PWREN# = "1") by setting an option in
the EEPROM.

3.4 ACBUS Signal Option
If the external EEPROM is fitted , the following options can be configured on the CBUS I/O pins
using the
software utility FT_PROG which can be downloaded from the FTDI utilities page. CBUS signal options
are
common to both package versions of the FT232H. The default configuration is described in section 7.

ACBUS
Signal
Option
Available On ACBUS Pin Description
TXDEN ACBUS0, ACBUS1, ACBUS2,
ACBUS3, ACBUS4, ACBUS5,
ACBUS6, ACBUS8, ACBUS9
TXDEN = (TTL level). Used with RS485 level converters
to enable the line driver during data transmit.  TXDEN is
active from one bit time before the start bit is
transmitted on TXD until the end of the stop bit.
*PWREN# ACBUS0, ACBUS1, ACBUS2,
ACBUS3, ACBUS4, ACBUS5,
ACBUS6, ACBUS8, ACBUS9
Output is low after the device has been configured by
USB, then high during USB suspend mode. This output
can be used to control power to external logic P-Channel
logic level MOSFET switch. Enable the interface pull-down
option when using the PWREN# in this way.*
TXLED# ACBUS0, ACBUS1, ACBUS2,
ACBUS3, ACBUS4, ACBUS5,
ACBUS6, ACBUS8, ACBUS9
TXLED = Transmit signalling output. Pulses low when
transmitting data (TXD) to the external device. This can
be connected to an LED.
RXLED# ACBUS0, ACBUS1, ACBUS2,
ACBUS3, ACBUS4, ACBUS5,
ACBUS6, ACBUS8, ACBUS9
RXLED = Receive signalling output. Pulses low when
receiving data (RXD) from the external device. This can
be connected to an LED.
TX&RXLED# ACBUS0, ACBUS1, ACBUS2,
ACBUS3, ACBUS4, ACBUS5,
ACBUS6, ACBUS8, ACBUS9
LED drive - pulses low when transmitting or receiving
data from or to the external device.
SLEEP# ACBUS0, ACBUS1, ACBUS2,
ACBUS3, ACBUS4, ACBUS5,
ACBUS6, ACBUS8, ACBUS9
Goes low during USB suspend mode. Typically used to
power down an external TTL to RS232 level converter IC
in USB to RS232 converter designs.
**CLK30 ACBUS0, ACBUS5,
ACBUS6,ACBUS8, ACBUS9
30MHz Clock output.
**CLK15 ACBUS0, ACBUS5,
ACBUS6,ACBUS8, ACBUS9
15MHz Clock output.
**CLK7.5 ACBUS0, ACBUS5,
ACBUS6,ACBUS8, ACBUS9
7.5MHz Clock output.
TriSt-PU ACBUS0, ACBUS1, ACBUS2,
ACBUS3, ACBUS4, ACBUS5,
ACBUS6, ACBUS8, ACBUS9
Input Pull Up
DRIVE 1 ACBUS0, ACBUS5,
ACBUS6,ACBUS8, ACBUS9
Output High
DRIVE 0 ACBUS0, ACBUS1, ACBUS2,
ACBUS3, ACBUS4, ACBUS5,
ACBUS6, ACBUS8, ACBUS9
Output Low
I/O mode ACBUS5, ACBUS6,ACBUS8,
ACBUS9
ACBUS Bit Bang
Table 3.5 ACBUS Configuration Control

* Must be used with a 10kohm resistor pull up.
**When in USB suspend mode the outputs clocks are also suspended.
```

### Page 14

```text
Copyright (c) Future Technology Devices International Limited  14
FT232H SINGLE CHANNEL HI-SPEED USB TO MULTIPURPOSE
UART/FIFO IC Datasheet
Version 2.1

Document No.: FT_000288 Clearance No.: FTDI #199
3.5 Pin Configurations
The following section describes the function of the pins when the device is configured in different
modes
of operation.

3.5.1 FT232H pins used in an UART interface
The FT232H can be configured as a UART interface. When configured in this mode, the pins used and
the
descriptions of the signals are shown in Table 3.6.

Pin
No. Name Type UART Configuration Description
13 TXD OUTPUT TXD = transmitter output
14 RXD INPUT RXD = receiver input
15 RTS# OUTPUT RTS# = Ready To send handshake output
16 CTS# INPUT CTS# = Clear To Send handshake input
17 DTR# OUTPUT DTR# = Data Transmit Ready modem signalling line
18 DSR# INPUT DSR# = Data Set Ready modem signalling line
19 DCD# INPUT DCD# = Data Carrier Detect modem signalling line
20 RI# INPUT
RI# = Ring Indicator Control Input. When the Remote Wake up option is
enabled in the EEPROM, taking RI# low can be used to resume the PC USB
Host controller from suspend.
21 **
TXDEN OUTPUT TXDEN = (TTL level). Use to enable RS485 level converter
27 **
RXLED OUTPUT
RXLED = Receive signalling output. Pulses low when receiving data (RXD)
from the external device (UART Interface). This should be connected to an
LED.
28 **
TXLED OUTPUT TXLED = Transmit signalling output. Pulses low when transmitting data (TXD)
to the external device (UART Interface). This should be connected to an LED.
Table 3.6 UART Configured Pin Descriptions

** ACBUS I/O pins

For a functional description of this mode, please refer to section 4.3

Note: UART is the device default mode.

3.5.2 FT232H Pins used in an FT245 Synchronous FIFO Interface
The FT232H can be configured as a FT245 synchronous FIFO interface. When configured in this mode,
the
pins used and the descriptions of the signals are shown in Table 3.7. To set this mode the external
EEPROM must be set to 245 modes. A software command (FT_SetBitMode) is then sent by the application
to the FTDI D2XX driver to tell the chip to enter 245 synchr onous FIFO mode. In this mode, data is
written or read on the rising edge of the CLKOUT.  Refer to Figure 4.4 for timing details.

Pin No. Name Type FT245 Configuration Description
13,14,15,16,17,18,19,20 ADBUS[7:0] I/O D7 to D0 bidirectional FIFO data. This bus is
normally input unless OE# is low.
21 RXF# OUTPUT
When high, do not read data from the FIFO. When
low, there is data available in the FIFO which can be
read by driving RD# low. When in synchronous
mode, data is transferred on every clock that RXF#
and RD# are both low. Note that the OE# pin must
be driven low at least 1 clock period before asserting
RD# low.
25 TXE# OUTPUT
When high, do not write data into the FIFO. When
low, data can be written into the FIFO by driving
WR# low. When in synchronous mode, data is
transferred on every clock that TXE# and WR# are
```

### Page 15

```text
Copyright (c) Future Technology Devices International Limited  15
FT232H SINGLE CHANNEL HI-SPEED USB TO MULTIPURPOSE
UART/FIFO IC Datasheet
Version 2.1

Document No.: FT_000288 Clearance No.: FTDI #199
both low.
26 RD# INPUT
Enables the current FIFO data byte to be driven onto
D0...D7 when RD# goes low. The next FIFO data
byte (if available) is fetched from the receive FIFO
buffer each CLKOUT cycle until RD# goes high.
27 WR# INPUT
Enables the data byte on the D0...D7 pins to be
written into the transmit FIFO buffer when WR# is
low. The next FIFO data byte is written to the
transmit FIFO buffer each CLKOUT cycle until WR#
goes high.

28
SIWU# INPUT
The Send Immediate / WakeUp signal combines two
functions on a single pin. If USB is in suspend mode
(PWREN# = 1) and remote wakeup is enabled in the
EEPROM, strobing this pin low will cause the device
to request a resume on the USB Bus. Normally, this
can be used to wake up the Host PC.
During normal operation (PWREN# = 0), if this pin is
strobed low any data in the device RX buffer will be
sent out over USB on the next Bulk-IN request from
the drivers regardless of the pending packet size.
This can be used to optimize USB transfer speed for
some applications. Tie this pin to VCCIO if not used.
29 CLKOUT OUTPUT 60 MHz Clock driven from the chip. All signals should
be synchronized to this clock.
30 OE# INPUT
Output enable when low to drive data onto D0-7.
This should be driven low at least 1 clock period
before driving RD# low to allow for data buffer turn-
around.
Table 3.7 FT245 Synchronous FIFO Configured Pin Descriptions

For a functional description of this mode, please refer to section 4.4.

3.5.3 FT232H Pins used in an FT245 Style aynchronous FIFO Interface
The FT232H can be configured as a FT245 style asynchronous FIFO interface. When configured in this
mode, the pins used and the descriptions of the signals are shown in Table 3.8. To enter this mode
the
external EEPROM must be set to 245 asynchronous FIFO mode. In this mode, data is written or read on
the falling edge of the RD# or WR# signals.

Pin No. Name Type FT245 Configuration Description
13, 14, 15, 16, 17,
18, 19,20 ADBUS[7:0] I/O D7 to D0 bidirectional FIFO data. This bus is normally
input unless RD# is low.
21 RXF# OUTPUT
When high, do not read data from the FIFO. When low,
there is data available in the FIFO which can be read by
driving RD# low. When RD# goes high again RXF# will
always go high and only become low again if there is
another byte to read. During reset this signal pin is
tristate, but pulled up to VCCIO via an internal 200kohm
resistor.
25 TXE# OUTPUT
When high, do not write data into the FIFO. When low,
data can be written into the FIFO by strobing WR# high,
then low. During reset this signal pin is tristate, but
pulled up to VCCIO via an internal 200kohm resistor.
26 RD# INPUT
Enables the current FIFO data byte to be driven onto
D0...D7 when RD# goes low. Fetches the next FIFO
data byte (if available) from the receive FIFO buffer
when RD# goes high.
27 WR# INPUT Writes the data byte on the D0...D7 pins into the
transmit FIFO buffer when WR# goes from high to low.

SIWU# INPUT The Send Immediate / WakeUp signal combines two
functions on a single pin. If USB is in suspend mode
```

### Page 16

```text
Copyright (c) Future Technology Devices International Limited  16
FT232H SINGLE CHANNEL HI-SPEED USB TO MULTIPURPOSE
UART/FIFO IC Datasheet
Version 2.1

Document No.: FT_000288 Clearance No.: FTDI #199
28 (PWREN# = 1) and remote wakeup is enabled in the
EEPROM, strobing this pin low will cause the device to
request a resume on the USB Bus. Normally, this can be
used to wake up the Host PC.
During normal operation (PWREN# = 0), if this pin is
strobed low any data in the device RX buffer will be sent
out over USB on the next Bulk-IN request from the
drivers regardless of the pending packet size. This can
be used to optimize USB transfer speed for some
applications. Tie this pin to VCCIO if not used.
Table 3.8 FT245 Style Asynchronous FIFO Configured Pin Descriptions

For a functional description of this mode, please refer to section 4.5.

3.5.4 FT232H Configured as a Synchronous or Asynchronous Bit -Bang
Interface

Bit-bang mode is an FTDI FT232H device mode that changes the 8 IO lines into an 8 bit bi
-directional
data bus. This mode is enabled by sending a software command ( FT_SetBitMode) to the FTDI driver .
When configured in any bi t-bang mode, the pins used and the descriptions of the signals are shown
in
Table 3.9

Pin No. Name Type Configuration Description
13,14,15,16,17,18,19,20 ADBUS[7:0] I/O D7 to D0 bidirectional Bit-Bang parallel I/O data pins

25 WRSTB# OUTPUT
Write strobe, active low output indicates when new
data has been written to the I/O pins from the Host
PC (via the USB interface).

26 RDSTB# OUTPUT
Read strobe, this output rising edge indicates when
data has been read from the parallel I/O pins and
sent to the Host PC (via the USB interface).
28 SIWU# INPUT
The Send Immediate / WakeUp signal combines two
functions on a single pin. If USB is in suspend mode
(PWREN# = 1) and remote wakeup is enabled in the
EEPROM, strobing this pin low will cause the device
to request a resume on the USB Bus. Normally, this
can be used to wake up the Host PC.
During normal operation (PWREN# = 0), if this pin is
strobed low any data in the device RX buffer will be
sent out over USB on the next Bulk-IN request from
the drivers regardless of the pending packet size.
This can be used to optimize USB transfer speed for
some applications. Tie this pin to VCCIO if not used.
Table 3.9 Synchronous or Asynchronous Bit-Bang Configured Pin Descriptions
For functional description of this mode, please refer to section 4.6.

3.5.5 FT232H Pins used in an MPSSE
The FT232H has a Multi-Protocol Synchronous Serial Engine (MPSSE). This mode is enabled by sending a
software command (FT_SetBitMode) to the FTDI D2xx driver. The MPSSE can be configured to a number
of industry standard serial interface protocols such as JTAG, I 2C or SPI (MASTER), or it can be
used to
implement a proprietary bus protocol.  For example, it is possible to connect FT232H's to an SRAM
configurable FPGA such as supplied by Altera or Xilinx. The FPGA device would normally not be
configured
(i.e. have no defined function) at power -up. Application software on the PC could use the MPSSE
(and
D2XX driver) to download configuration data to the FPGA over USB. This data would define the
hardware
function on power up. The MPSSE can be used to control a number of GPIO pins. When configured in
this
mode, the pins used and the descriptions of the signals are shown in Table 3.10

Pin No. Name Type MPSSE Configuration Description
13 TCK/SK OUTPUT Clock Signal Output. For example:
JTAG - TCK, Test interface clock
```

### Page 17

```text
Copyright (c) Future Technology Devices International Limited  17
FT232H SINGLE CHANNEL HI-SPEED USB TO MULTIPURPOSE
UART/FIFO IC Datasheet
Version 2.1

Document No.: FT_000288 Clearance No.: FTDI #199
SPI (MASTER) - SK, Serial Clock
14 TDI/DO OUTPUT
Serial Data Output. For example:
JTAG - TDI, Test Data Input
SPI (MASTER) - DO
15 TDO/DI INPUT
Serial Data Input. For example:
JTAG - TDO, Test Data output
SPI (MASTER) - DI, Serial Data Input
16 TMS/CS OUTPUT
Output Signal Select. For example:
JTAG - TMS, Test Mode Select
SPI (MASTER) - CS, Serial Chip Select
17 GPIOL0 I/O General Purpose input/output
18 GPIOL1 I/O General Purpose input/output
19 GPIOL2 I/O General Purpose input/output
20 GPIOL3 I/O General Purpose input/output
21 GPIOH0 I/O General Purpose input/output
25 GPIOH1 I/O General Purpose input/output
26 GPIOH2 I/O General Purpose input/output
27 GPIOH3 I/O General Purpose input/output
28 GPIOH4 I/O General Purpose input/output
29 GPIOH5 I/O General Purpose input/output
30 GPIOH6 I/O General Purpose input/output
31 GPIOH7 I/O General Purpose input/output
Table 3.10 MPSSE Configured Pin Descriptions

For functional description of this mode, please refer to section 4.8.

3.5.6 FT232H Pins used as a Fast Serial Interface
The FT232H can be configured for use with high -speed bi-directional isolated serial data.  A
proprietary
FTDI protocol designed to allow galvanic isolated devices to communicate synchronously with the
FT232H
using just 4 signal wires (over two dual opt o-isolators), and two power lines. The peripheral
circuitry
controls the data transfer rate in both directions, whilst maintaining full data integrity. 12 Mbps
(USB full
speed) data rates can be achieved  when using the proper high speed opto -isolators (see App Note AN
-
131).  When configured in this mode, the pins used and the descriptions of the signals are shown in
Table
3.11.

Pin
No. Name Type Fast Serial Interface Configuration Description
13 FSDI INPUT Fast serial data input.
14 FSCLK INPUT Fast serial clock input.
Clock input to FT232H chip to clock data in or out.
15 FSDO OUTPUT Fast serial data output.
16 FSCTS OUTPUT Fast serial Clear To Send signal output.
Driven low to indicate that the chip is ready to send data

28 SIWU# INPUT
The Send Immediate / WakeUp signal combines two functions on a single pin.
If USB is in suspend mode (PWREN# = 1) and remote wakeup is enabled in
the EEPROM, strobing this pin low will cause the device to request a resume
on the USB Bus. Normally, this can be used to wake up the Host PC.
During normal operation (PWREN# = 0), if this pin is strobed low any data in
the device RX buffer will be sent out over USB on the next Bulk-IN request
from the drivers regardless of the pending packet size. This can be used to
optimize USB transfer speed for some applications. Tie this pin to VCCIO if not
used.
Table 3.11 Fast Serial Interface Configured Pin Descriptions

For a functional description of this mode, please refer to section 4.9.
```

### Page 18

```text
Copyright (c) Future Technology Devices International Limited  18
FT232H SINGLE CHANNEL HI-SPEED USB TO MULTIPURPOSE
UART/FIFO IC Datasheet
Version 2.1

Document No.: FT_000288 Clearance No.: FTDI #199
3.5.7 FT232H Pins Configured as a CPU-style FIFO Interface
The FT232H can be configured in a CPU-style FIFO interface mode which allows a CPU to interface to
USB
via the FT232H. This mode is enabled in the external EEPROM.  When configured in this mode, the pins
used and the descriptions of the signals are shown in Table 3.12.

Pin No. Name Type Fast Serial Interface Configuration Description
13, 14,
15, 16,
17, 18,
19, 20
ADBUS[7:0]
I/O D7 to D0 bidirectional data bus
21 CS# INPUT Active low chip select input
25 A0 INPUT Address bit A0
26 RD# INPUT Active Low FIFO Read input
27 WR# INPUT Active Low FIFO Write input
28 SI# INPUT
Send Immediate (active low).
During normal operation (PWREN# = 0), if this pin is strobed low any
data in the device RX buffer will be sent out over USB on the next
Bulk-IN request from the drivers regardless of the pending packet
size. This can be used to optimize USB transfer speed for some
applications.
Tie this pin to VCCIO if not used.
Table 3.12 CPU-style FIFO Interface Configured Pin Descriptions

For a functional description of this mode, please refer to section 4.10.

3.5.8 FT232H Pins Configured as a FT1248 Interface
The FT232H can be configured as a proprietary FT1248 interface. This mode is enabled in the external
EEPROM. When co nfigured in this mode, the pins used and the descriptions of the signals are shown
in
Table 3.13.

Pin
No. Name Type UART Configuration Description
13 MIOSIO0 INPUT
/OUTPUT
Bi-directional synchronous command and data bus, bit 0 used to
transmit and receive data from/to the master
14 MIOSIO1 INPUT
/OUTPUT
Bi-directional synchronous command and data bus, bit 1 used to
transmit and receive data from/to the master
15 MIOSIO2 INPUT
/OUTPUT
Bi-directional synchronous command and data bus, bit 2 used to
transmit and receive data from/to the master
16 MIOSIO3 INPUT
/OUTPUT
Bi-directional synchronous command and data bus, bit 3 used to
transmit and receive data from/to the master
17 MIOSIO4 INPUT
/OUTPUT
Bi-directional synchronous command and data bus, bit 4 used to
transmit and receive data from/to the master
18 MIOSIO5 INPUT
/OUTPUT
Bi-directional synchronous command and data bus, bit 5 used to
transmit and receive data from/to the master
19 MIOSIO6 INPUT
/OUTPUT
Bi-directional synchronous command and data bus, bit 6 used to
transmit and receive data from/to the master
20 MIOSIO7 INPUT
/OUTPUT
Bi-directional synchronous command and data bus, bit 7 used to
transmit and receive data from/to the master
21 SCLK INPUT Serial clock used to drive the slave device data
25 SS_n INPUT Active low slave select 0 from master to slave
26 MISO OUTPUT Slave output used to transmit the status of the transmit and receive
buffers are empty and full respectively
Table 3.13 FT1248 Configured Pin Descriptions
For functional description of this mode, please refer to section 4.
```

### Page 19

```text
Copyright (c) Future Technology Devices International Limited  19
FT232H SINGLE CHANNEL HI-SPEED USB TO MULTIPURPOSE
UART/FIFO IC Datasheet
Version 2.1

Document No.: FT_000288 Clearance No.: FTDI #199
4 Function Description
The FT232H USB 2.0 Hi -Speed (480Mb/s) to UART/FIFO is an FTDI's 6 th generation of ICs. It can be
configured in a variety of industry standard serial or parallel interfaces, such as UART, FIFO,
JTAG, SPI
(MASTER) or I2C modes. In addition to these, the FT232H introduces the FT1248 interface and supports
a
CPU-Style FIFO mode, bit-bang and a fast serial interface mode.

4.1 Key Features
USB Hi -Speed to UART/FIFO  Interface. The FT232H provides USB 2.0 Hi -Speed (480Mbits/s) to
flexible and configurable UART/FIFO Interfaces.

Functional Integration . The FT232H integrates a USB protocol engine which controls the physical
Universal Transceiver Macrocell Interface (UTMI) and handles all aspects of the USB 2.0 Hi -Speed
interface. The FT232H includes an integrated +1.8V/3.3V Low Drop -Out (LDO) regulator. It also
includes
1Kbytes Tx and Rx data buffers. The FT232H integrates the entire USB protocol on a chip with no
firmware required.

MPSSE. Multi - Protocol Synchronous Serial Engines (MPSSE), capable of speeds up to 30 Mbits/s,
provides flexible synchronous interface configurations.

FT1248 interface. The FT232H supports a new proprietary half-duplex FT1248 interface with a variable
bi-directional data bus interface that can be configured as 1, 2, 4, or 8 -bits wide and this
enables the
flexibility to expand the size of the data bus to 8 pins.  For details regarding 2-bit, 4-bit and
8-bit modes,
please refer to application note AN_167_FT1248_Serial_Parallel Interface Basics available from the
FTDI
website.

Data Transfer rate.  The FT232H supports a data transfer rate up to 12 Mbaud when configured as an
RS232/RS422/RS485 UART interface up to  40 Mbytes/second over a synchronous 245 parallel FIFO
interface or up to 8 Mbyte/Sec over an asynchronous 245 FIFO interface . Please note the FT232H does
not support the baud rates of 7 Mbaud 9 Mbaud, 10 Mbaud and 11 Mbaud.

Latency Timer. A feature of the driver used as a timeout to transmit short packets of data back to
the
PC. The default is 16ms, but it can be altered between 0ms and 255ms.

Bus (ACBUS) functionality, signal inversion and drive strength selection.  There are 11
configurable ACBUS I/O pins. These configurable options are:

1. TXDEN - transmit enable for RS485 designs.
2. PWREN# - Power control for high power, bus powered designs.
3. TXLED# - for pulsing an LED upon transmission of data.
4. RXLED# - for pulsing an LED upon receiving data.
5. TX&RXLED# - which will pulse an LED upon transmission OR reception of data.
6. SLEEP# - indicates that the device going into USB suspend mode.
7. CLK30 / CLK15 / CLK7.5 - 30MHz, 15MHz and 7.5MHz clock output signal options.
8. TriSt-PU - Input pulled up, not used
9. DRIVE 1 - Output driving high
10. DRIVE 0 - Output driving low
11. I/O mode -  ACBUS Bit Bang

The ACBUS pins can also be individually configured as GPIO pins, similar to asynchronous bit bang
mode.
It is possible to use this mode while the UART interface is being used, thus providing up to 4
general
purpose I/O pins which are available during normal operation.

The ACBUS lines can be configured with any one of these input/output options by setting bits in the
external EEPROM see section 3.4.
```

### Page 20

```text
Copyright (c) Future Technology Devices International Limited  20
FT232H SINGLE CHANNEL HI-SPEED USB TO MULTIPURPOSE
UART/FIFO IC Datasheet
Version 2.1

Document No.: FT_000288 Clearance No.: FTDI #199
4.2 Functional Block Descriptions
Multi-Purpose UART/FIFO Controllers. The FT232H has one independent UART/FIFO Controller. This
controls the UART data, 245 FIFO data, Fast Serial (opto isolation) or Bit -Bang mode which can be
selected by SETUP ( FT_SetBitMode) command.  Each Multi -Purpose UART/FIFO Controller also contains
an MPSSE ( Multi-Protocol Synchronous Serial Engine). Using this MPSSE, the Multi -Purpose UART/FIFO
Controller can be configured under software command, to have one of the MPSSE ( SPI (MASTER), I2C,
and JTAG).

USB Protocol Engine and FIFO control. The USB Protocol Engine controls and manages  the interface
between the UTMI PHY and the FIFOs of the chip. It also handles power management and the USB
protocol specification.

Port FIFO TX Buffer  (1Kbytes). Data from the Host PC is stored in these buffers to be used by the
Multi-purpose UART/FIFO controllers. This is controlled by the USB Protocol Engine and FIFO control
block.

Port FIFO RX Buffer (1K bytes). Data from the Multi-purpose UART/FIFO controllers is stored in these
blocks to be sent back to the Host PC when requested. This is controlled by the USB Protocol Engine
and
FIFO control block.

RESET Generator - The integrated Reset Generator Cell provides a reliable power-on reset to the
device
internal circuitry at power up. The RESET# input pin allows an external device to reset the FT232H.
RESET# should be tied to VCCIO (+3.3V) if not being used.

Baud Rate Generators - The Baud Rate Generators provides an x16 or an x10 clock input to the
UART's from a 120MHz reference clock and consists of a 14 bit pre -scaler and 4 register bits which
provide fine tuning of the baud rate (used to divide by a number plus a fraction). This determines
the
Baud Rate of the UAR T which is programmable from 183 baud to 12 Mbaud. See FTDI application note
AN_120 on the FTDI website for more details.

EEPROM Interface. If the external EEPROM is fitted, the FT2 32H can be configured as an asynchronous
serial UART (default mode), parallel FIFO (245) mode, FT1248, fast serial (opto isolation) or CPU
-Style
FIFO.  The EEPROM should be a 16 bit wide configuration such as a 93LC56B  or equivalent capable of
a
1Mbit/s clock rate at VCCIO = +2.97V to 3.63V. The EEPROM is programmable in -circuit over USB using
a utility program called FT_Prog available from FTDI web site.  Please note that the 93LC46B is not
compatible with the FT232H device.

+1.8/3.3V LDO Regulator. The +3.3/+1.8V LDO regulator generates +1.8 volts for the core and the
USB transceiver cell and +3.3V for the IO and the internal PLL and USB PHY power supply.

UTMI PHY . The Universal Transceiver Macrocell Interface (UTMI) physical interface cell. This block
handles the Ful l speed / Hi -Speed SERDES (serialise - deserialise) function for the USB TX/RX
data. It
also provides the clocks for the rest of the chip. A 12 MHz crystal must be connected to the OSCI
and
OSCO pins or 12 MHz Oscillator must be connected to the OSCI, and the OSCO is left unconnected. A
12K
Ohm resistor should be connected between REF and GND on the PCB.

The UTMI PHY functions include:

- Supports 480 Mbit/s "Hi-Speed" (HS)/ 12 Mbit/s "Full Speed" (FS).
- SYNC/EOP generation and checking
- Data and clock recovery from serial stream on the USB.
- Bit-stuffing/unstuffing; bit stuff error detection.
- Manages USB Resume, Wake Up and Suspend functions.
- Single parallel data clock output with on-chip PLL to generate higher speed serial data clocks.
```

### Page 21

```text
Copyright (c) Future Technology Devices International Limited  21
FT232H SINGLE CHANNEL HI-SPEED USB TO MULTIPURPOSE
UART/FIFO IC Datasheet
Version 2.1

Document No.: FT_000288 Clearance No.: FTDI #199
4.3 FT232 UART Interface Mode Description
The FT232H can be configured as a UART with external line drivers, similar to operation with the
FTDI
FT232R devices. The following examples illustrate how to configure the FT232H with an RS232, RS422
or
RS485 interface.

4.3.1 RS232 Configuration
Figure 4.1 illustrates how the FT232H can be configured with an RS232 UART interface.

Figure 4.1 RS232 Configuration
```

### Page 22

```text
Copyright (c) Future Technology Devices International Limited  22
FT232H SINGLE CHANNEL HI-SPEED USB TO MULTIPURPOSE
UART/FIFO IC Datasheet
Version 2.1

Document No.: FT_000288 Clearance No.: FTDI #199
4.3.2 RS422 Configuration
Figure 4.2 illustrates how the FT232H can be configured as a RS422 interface.

Figure 4.2 Dual RS422 Configuration

In this case the FT232H is configured as UART operating at TTL levels and a level converter device
(full
duplex RS485 transceiver) is used to convert the TTL level signals from the FT232H to RS422 l evels.
The
PWREN# signal is used to power down the level shifters such that they operate in a low quiescent
current
when the USB interface is in suspend mode.
```

### Page 23

```text
Copyright (c) Future Technology Devices International Limited  23
FT232H SINGLE CHANNEL HI-SPEED USB TO MULTIPURPOSE
UART/FIFO IC Datasheet
Version 2.1

Document No.: FT_000288 Clearance No.: FTDI #199
4.3.3 RS485 Configuration
Figure 4.3 illustrates how the FT232H can be configured as a RS485 interface.

Figure 4.3 Dual RS485 Configuration

In this case the FT232H is configured as a UART operating at TTL levels and a level converter device
(half
duplex RS485 transceiver) is used to convert the TTL level signals from the FT232H to RS485 levels.
With
RS485, the transmitter is only enabled when a character is being transmitted from the UART. The
TXDEN
pin on the FT232H is provided for exactly th at purpose, and so the transmitter enables are wired to
the
TXDEN. RS485 is a multi -drop network - i.e. many devices can communicate with each other over a
single two wire cable connection. The RS485 cable requires to be terminated at each end of the cable
.
Links are provided to allow the cable to be terminated if the device is physically positioned at
either end
of the cable.
```

### Page 24

```text
Copyright (c) Future Technology Devices International Limited  24
FT232H SINGLE CHANNEL HI-SPEED USB TO MULTIPURPOSE
UART/FIFO IC Datasheet
Version 2.1

Document No.: FT_000288 Clearance No.: FTDI #199
4.4 FT245 Synchronous FIFO Interface Mode Description

When FT232H is configured in an FT245 Synchronous FIFO interface mode the IO timing of the signals
used are shown in Figure 4.4 which shows details for read and write accesses. The timings are shown
in
Figure 4.4.Note that only a read or a write cycle can be performed at any one time. Data is read or
written on the rising edge of the CLKOUT clock.

Figure 4.4 FT245 Synchronous FIFO Interface Signal Waveforms
```

### Page 25

```text
Copyright (c) Future Technology Devices International Limited  25
FT232H SINGLE CHANNEL HI-SPEED USB TO MULTIPURPOSE
UART/FIFO IC Datasheet
Version 2.1

Document No.: FT_000288 Clearance No.: FTDI #199
Name Min Nom Max Units Comments
t1   16.67   ns CLKOUT period
t2 7.5 8.33 9.17  ns CLKOUT high period
t3 7.5 8.33 9.17  ns CLKOUT low period
t4 0   9 ns CLKOUT to RXF#
t5 0   9 ns CLKOUT to read DATA valid
t6 0   9 ns OE# to read DATA valid
t7 7.5   16.67 ns OE# setup time
t8 0    ns OE# hold time
t9 7.5   16.67 ns RD# setup time to CLKOUT (RD# low after OE# low)
t10 0    ns RD# hold time
t11 0   9 ns CLKOUT TO TXE#
t12 7.5   16.67 ns Write DATA setup time
t13 0     ns Write DATA hold time
t14 7.5    16.67 ns WR# setup time to CLKOUT (WR# low after TXE# low)
t15 0    WR# hold time
Table 4.1 FT245 Synchronous FIFO Interface Signal Timings

This mode uses a synchronous interface to get high data transfer speeds. The chip drives a 60 MHz
CLKOUT clock for the external system to use.

Note that Asynchronous FIFO mode must be selected in the EEPRO M before selecting the Synchronous
FIFO mode in software.

4.4.1 FT245 Synchronous FIFO Read Operation
A read operation is started when the chip drives RXF# low. The external system can then drive OE#
low
to turn the data bus drivers around before acknowledging the data with the RD# signal going low. The
first data byte is on the bus after OE# is low. The external system can burst the data out of the
chip by
keeping RD# low or it can insert wait states in the RD# signal. If there is more data to be read it
will
change on the clock following RD# sampled low. Once all the data has been consumed, the chip will
drive
RXF# high. Any data that appears on the data bus, after RXF# is high, is invalid and should be
ignored.

4.4.2 FT245 Synchronous FIFO Write Operation
A write operation can be started when TXE# is low. WR # is brought low when the data is valid. A
burst
operation can be done on every clock providing TXE# is still low. The external system must monitor
TXE#
and its own WR# to check that data has been accepted. Both TXE# and WR # must be low for data to be
accepted.
```

### Page 26

```text
Copyright (c) Future Technology Devices International Limited  26
FT232H SINGLE CHANNEL HI-SPEED USB TO MULTIPURPOSE
UART/FIFO IC Datasheet
Version 2.1

Document No.: FT_000288 Clearance No.: FTDI #199
4.5 FT245 Style Asynchronous FIFO Interface Mode Description

The FT232H can be configured as an asynchronous FIFO interface. This mode is similar to the
synchronous FIFO interface with the exception that the data is written to or read from the FIFO on t
he
falling edge of the WR# or RD# signals.

This mode does not provide a CLKOUT signal and it does not expect an OE# input signal. The following
diagrams illustrate the asynchronous FIFO mode timing.

Figure 4.5 FT245 Asynchronous FIFO Interface READ Signal Waveforms

Figure 4.6 FT245 Asynchronous FIFO Interface WRITE Signal Waveforms

Time Description Min Max Units
T1 RD# inactive to RXF# 1 14 ns
T2 RXF# inactive after RD# cycle 49  ns
T3 RD# to DATA 1 14 ns
T4 RD# active pulse width  30  ns
T5 RD# active after RXF# 0  ns
T6 WR# active to TXE# inactive 1 14 ns
T7 TXE# active to TXE# after WR# cycle 49  ns
T8 DATA to WR# active setup time 5  ns
T9 DATA hold time after WR# inactive 5  ns
T10 WR# active pulse width  30  ns
T11 WR# active after TXE# 0  ns
Table 4.2 Asynchronous FIFO Timings (based on standard drive level outputs)
```

### Page 27

```text
Copyright (c) Future Technology Devices International Limited  27
FT232H SINGLE CHANNEL HI-SPEED USB TO MULTIPURPOSE
UART/FIFO IC Datasheet
Version 2.1

Document No.: FT_000288 Clearance No.: FTDI #199
4.6 FT1248 Interface Mode Description
The FT232H supports a half-duplex FT1248 Interface that provides a flexible data communication and
high performance interface between the FT232H as a FT1248 slave and an external FT1248 master. The
FT1248 protocol is a dynamic bi-directional data bus interface that can be configured as 1,  2, 4,
or 8-bits
wide.

[7:0]
SCLK
MIOSIO
MISO
SS#
SCLK
MIOSIO
MISO
SS#
FPGA (FT1248 Master) FT232H (FT1248 Slave)

Figure 4.7 FT1248 Bus with Single Master and Slave.

In the FT1248 there are 3 distinct phases:

While SS _n is inactive, the FT1248 reflects the status of  the write buffer and read buffers on the
MIOSIO[0] and MISO wires respectively. Additionally, the FT1248 slave block supports multiple slave
devices where a master can communicate with multiple FT1248 slave devices. When the slave is sharing
buses with ot her FT1248 slave devices, the write and read buffer status cannot be reflected on the
MIOSIO[0] and MISO wires during SS _n inactivity as this would cause bus contention. Therefore, it
is
possible for the user to select whether they wish to have the buffer status switched on or off
during
inactivity. When SS_n is active a command/bus size phase occurs first. Following the command phase
is
the data phase, for each data byte transferred the FT1248 slave drives an ACK/NAK status onto the
MISO
wire. The master c an send multiple data bytes so long as SS _n is active, if a unsuccessful data
transfer
occurs, i.e. a NAK happens on the MISO wire then the master should immediately abort the transfer by
de-asserting SS_n.

BUS TURNAROUND
WRITE DATA
TXE# CMD
CLK
SCLK
SS_n
MIOSIO[0]
RXF#MISO RXF#
RDATA0 RDATA1 RDATA2 TXE# CMD WDATA 0 WDATA 1 TXE#
WRITEREAD
RXF#STATUSSTATUSSTATUSSTATUSSTATUS

Figure 4.8 FT1248 Basic Waveform Protocol

Section 4.6.2 illustrates the FT1248 write and read protocol operating in 1-bit mode. For details
regarding
2-bit, 4 -bit and 8 -bit modes, please refer to application note AN_167_FT1248 Parallel Serial
Interface
Basics available at http://www.ftdichip.com.
```

### Page 28

```text
Copyright (c) Future Technology Devices International Limited  28
FT232H SINGLE CHANNEL HI-SPEED USB TO MULTIPURPOSE
UART/FIFO IC Datasheet
Version 2.1

Document No.: FT_000288 Clearance No.: FTDI #199
4.6.1 Bus Width Protocol Decode
In order for the FT1248 master to determine the bus width within the command phase the bus width is
encoded along with the actual commands on the first active clock edge when SS _n is active and has a
data width of 8-bits.

If any of the MIOSIO [7:4] signals are low then the data transfer width equals 8-bits.

If any of the MIOSIO [3:2] signals are low then the data transfer width equals 4-bits.

If MIOSIO [1] signal is low then the data transfer width equals 2-bits.

Else the bus width is defaulted to 1-bit.

Please note that if both of the MIOSIO bit signals are low then the data transfer width is equal to
the
width of high priority MIOSIO bit signal.  For example if both of the MIOSIO [7:3] signals are low
then
the data transfer width equals 8-bits or if both of the MIOSIO [3:1] signals are low then the data
transfer
width equals 4-bits.

In order to successfully decode the bus width, all MIOSIO signals must have pull up resistors. By
default,
all MIOSIO signals shall be seen by the FT 232H in FT1248 mode as logic '1'. This means that when a
FT1248 master does not wish to use certain MIOSIO signals the slave (FT232H) is still capable of
determining the requested bus width since any unused MIOSIO signals shall be pull up in the slave.

The remaining bits used during the command phase are used to contain the command itself which means
that it is possible to define up to 16 unique commands.

Figure 4.9 FT1248 Command Structure

For more details about FT1248 Interface, please refer to application note AN_167_FT1248 Parallel
Serial
Interface Basics available at http://www.ftdichip.com.

CMD[3] BWID 2-bit BWID 4-bit CMD[2] BWID 8-bit CMD[1] CMD[0] X
LSB MSB
0 1 2 3 4 5 6 7
1-bit Bus
Width CMD[3] X X CMD[2] X CMD[1] CMD[0] X
0 1 2 3 4 5 6 7
2-bit Bus
Width CMD[3] 0 X CMD[2] X CMD[1] CMD[0] X
0 1 2 3 4 5 6 7
4-bit Bus
Width CMD[3] X 0 CMD[2] X CMD[1] CMD[0] X
0 1 2 3 4 5 6 7
8-bit Bus
Width CMD[3] X X CMD[2] 0 CMD[1] CMD[0] X
0 1 2 3 4 5 6 7
```

### Page 29

```text
Copyright (c) Future Technology Devices International Limited  29
FT232H SINGLE CHANNEL HI-SPEED USB TO MULTIPURPOSE
UART/FIFO IC Datasheet
Version 2.1

Document No.: FT_000288 Clearance No.: FTDI #199
4.6.2 FT1248: 1-bit interface
The FT1248 Interface transfer s data over different bus widths (1 -bit, 2-bit, 4-bit and 8-bit).
Figure 4.21
and Figure 4.22 illustrates the waveform detailing the FT1248 write and read protocol operating in 1
-bit
mode with flow control. Please refer  to the application notes AN_167_FT1248 Parallel Serial
Interface
Basics available at http://www.ftdichip.com for more details regarding 1-bit without flow control,
2-bit, 4-
bit and 8-bit modes.
BUS TURNAROUND
WRITE DATACOMMAND PHASE
BUS TURNAROUND
TXE# CMD3 0 0 0CMD2 CMD1 CMD0 B7 B6 B5 B4 B3 B2 B1 B0 TXE#
SCLK
SS_n
MIOSIO[0]
PULLED HIGH
RXF#MISO
MIOSIO[7:1]
TXE# ACK RXF#
BUS TURNAROUND

Figure 4.10 FT1248 1-bit Mode Protocol (WRITE)
BUS TURNAROUND
READ DATACOMMAND PHASE
BUS TURNAROUND
TXE# CMD3 0 0 0CMD2 CMD1 CMD0 B7 B6 B5 B4 B3 B2 B1 B0 TXE#
SCLK
SS_n
MIOSIO[0]
PULLED HIGH
RXF#MISO
MIOSIO[7:1]
RXF# ACK RXF#

Figure 4.11 FT1248 1-bit Mode Protocol (READ)
```

### Page 30

```text
Copyright (c) Future Technology Devices International Limited  30
FT232H SINGLE CHANNEL HI-SPEED USB TO MULTIPURPOSE
UART/FIFO IC Datasheet
Version 2.1

Document No.: FT_000288 Clearance No.: FTDI #199
When SS_n is inactive the write buffer and read buffer status is reflected on the MIOSIO[0] and MISO
signals respectively. When the master wishes to initiate a data transfer, SS_n becomes active. As
soon as
SS_n becomes active the SPI slave immediately stops driving the MIOSIO[0] signal and SPI master is
not
allowed to begin driving the MIOSIO[0] signal until the first clock edge, this ensures that bus
contention
is avoided.

On the first clock edge the command is shifted out for 7 clocks, on the 8 th clock cycle a bus
turnaround is
required. The bus turnaround is required as the slave may be required to drive the MIOSIO[0] bus
with
read data. The data phase occurs in response to the command and so long as SS _n remains active. The
data phase in 1 -bit mode requires 8 c lock cycles where the MIOSIO[0] signal transfers the
requested
write or read data. The MISO signal indicates to the master the success of the transfer with an ACK
or
NAK.

The status is reflected through the whole of the data phase and is valid from the f irst clock edge.
If the
master is writing data to the slave, then on the last clock edge before it de -asserts SS_n must
tristate
the MIOSIO[0] signal to enable the bus to be "turned" around as when SS _n becomes inactive the
FT1248 slave shall begin to driv e the write buffer status onto the MIOSIO[0] signal. When the SPI
slave
is driving the MIOSIO[0] (the master is reading data) no bus turnaround is required as when SS _n
becomes inactive it is required to drive the write buffer status to the FT1248 master.

4.7 Synchronous and Asynchronous Bit-Bang Interface Mode

The FT232H can be configured as a bit -bang interface. There are two types of bit -bang modes:
synchronous and asynchronous.

See application note AN2232-02 Bit Mode Functions for the FT232 for more details and examples of
using
both Synchronous and Asynchronous bit-bang modes.

4.7.1 Asynchronous Bit-Bang Mode
Asynchronous Bit-Bang mode is the same as BM -style Bit-Bang mode, except that the internal RD# and
WR# strobes (RDSTB# and WRSTB#) are now brought out of the device to allow external logic to be
clocked by accesses to the bit-bang IO bus.

Any data written to the device in the normal manner will be self-clocked onto the data pins (those
which
have been configured as outputs). Each pin can be independently set as an input or an output. The
rate
that the data is clocked out at is controlled by the baud rate generator.

New data must be written, and the baud rate c lock should tick to change the data. If no new data is
written to the chip, the pins configured for output will hold the last value written.

Asynchronous Bit-Bang mode is enabled using the FT_SetBitMode D2xx driver command with a hex value
of 0x01.

4.7.2 Synchronous Bit-Bang Mode
The synchronous Bit-Bang mode will only update the output parallel port pins whenever data is sent
from
the USB interface to the parallel interface. When this is done, the WRSTB# will activate to indicate
that
the data has been read f rom the USB Rx FIFO buffer and written out on the pins. Data can only be
received from the parallel pins (to the USB Tx FIFO interface) after the parallel interface has been
written
to.

With Synchronous Bit -Bang mode data will only be sent out by the FT232H if there is space in the
FT232H USB TXFIFO for data to be read from the parallel interface pins. This Synchronous Bit-Bang
mode
will read the data bus parallel I/O pins first, before i t transmits data from the USB RxFIFO. It is
therefore
1 byte behind the output, and so to read the inputs for the byte that you have just sent, another
byte
must be sent.

For example:
Figure 1. Pins start at 0xFF
Send 0x55, 0xAA
```

### Page 31

```text
Copyright (c) Future Technology Devices International Limited  31
FT232H SINGLE CHANNEL HI-SPEED USB TO MULTIPURPOSE
UART/FIFO IC Datasheet
Version 2.1

Document No.: FT_000288 Clearance No.: FTDI #199
Pins go to 0x55 and then to 0xAA
Data read = 0xFF,0x55
(2) Pins start at 0xFF
Send 0x55, 0xAA, 0xAA
(repeat the last byte sent)
Pins go to 0x55 and then to 0xAA
Data read = 0xFF, 0x55, 0xAA

Synchronous Bit-Bang Mode differs from Asynchronous Bit-Bang mode in that the device parallel output
is only read when the parallel output is written to by the USB interface. This mak es it easier for
the
controlling program to measure the response to a USB output stimulus as the data returned t o the
USB
interface is synchronous to the output data.

Synchronous Bit -Bang mode is enabled using Set Bit Bang Mode driver command with a hex value of
0x04.

An example of the synchronous bit-bang mode timing is shown in Figure 4.12
WRSTB#
RDSTB#

Figure 4.12 Synchronous Bit-Bang Mode Timing Interface Example

WRSTB# = this output indicates when new data has been written to the I/O pins from the Host PC (via
the USB interface).

Name Description
t1 Current pin state is read
t2
RDSTB# is set inactive and data on the parallel I/O pins is read and
sent to the USB host.
T3
RDSTB# is set active again, and any pins that are output will change
to their new data
t4 1 clock cycle to allow for data setup
t5
WRSTB# goes active. This indicates that the host PC has written new
data to the I/O parallel data pins
t6 WRSTB# goes inactive
Table 4.3 Synchronous Bit-Bang Mode Timing Interface Example Timings

RDSTB# = this output rising edge indicates when data has been read from the I/O pins and sent to the
Host PC (via the USB interface).

The WRSTB# goes active in t5. The WRSTB# goes active when data is read from the USB RXFIFO (i.e.
sent from the PC). The RDSTB# goes inactive when data is sampled from the pins and written to the
USB
TXFIFO (i.e. sent to the PC). The SETUP comm and to the FT232H is used to setup the bit -mode. This
command also contains a byte wide data mask to set the direction of each bit. The direction on each
pin
doesn't change unless a new SETUP command is used to modify the direction.

The WRSTB# and RDSTB#  strobes are only a guide to what may be happening depending on the
direction of the bus. For example if all pins are configured as inputs, it is still necessary to
write to these
pins in order to get the FT232H to read those pins even though the data writ ten will never appear
on the
pins.
```

### Page 32

```text
Copyright (c) Future Technology Devices International Limited  32
FT232H SINGLE CHANNEL HI-SPEED USB TO MULTIPURPOSE
UART/FIFO IC Datasheet
Version 2.1

Document No.: FT_000288 Clearance No.: FTDI #199
Signals and data-flow are illustrated in Figure 4.13
USB Rx
FIFO/
Buffer
Parallel I/O
data
Parallel
I/O pinsUSB
WRSTB#
RDSTB#
USB Tx
FIFO/
Buffer

Figure 4.13- Bit-bang Mode Dataflow Illustration Diagram

4.8 MPSSE Interface Mode Description

MPSSE Mode is designed to allow the FT232H to interface efficiently with synchronous serial
protocols
such as JTAG, I2C and SPI (MASTER) Bus. It can also be used to program SRAM based FPGA's over USB.
The MPSSE interface is designed to be flexible so that it can be conf igured to allow any
synchronous
serial protocol (industry standard or proprietary) to be implemented using the FT232H.

MPSSE is fully configurable, and is programmed by sending commands down the data stream. These can
be sent individually or more efficiently in packets. MPSSE is capable of a maximum sustained data
rate of
30 Mbits/s.

When the FT232H is configured in MPSSE mode, the IO timing and signals used are shown in  Figure
4.14
and Table 4.4 These show timings for CLKOUT=30MHz. CLKOUT can be divided internally to be provi de a
slower clock.

Figure 4.14 MPSSE Signal Waveforms

Name Min Typ Max Units Comments
t1 32.66 33.33 33.99 ns CLKOUT period
t2 15 16.67 18.33 ns CLKOUT high period
t3 15 16.67 18.33 ns CLKOUT low period
t4 0

7.50 ns CLKOUT to TDI/DO delay
t5 0

ns TDI/DO hold time
t6 11

ns TDI/DO setup time
Table 4.4 MPSSE Signal Timings
```

### Page 33

```text
Copyright (c) Future Technology Devices International Limited  33
FT232H SINGLE CHANNEL HI-SPEED USB TO MULTIPURPOSE
UART/FIFO IC Datasheet
Version 2.1

Document No.: FT_000288 Clearance No.: FTDI #199
MPSSE mode is enabled using the FT_SetBitMode D2xx driver command with a hex value of 0x02.  A hex
value of 0x00 will reset the device. See application note AN135 - MPSSE Basics  for more details and
examples.

The MPSSE command set is fully described in application note AN108 - Command Processor For MPSSE
and MCU Host Bus Emulation Modes.

4.8.1  MPSSE Adaptive Clocking
The Adaptive Clock mode correlates the CLK signal with a return clock RTCK. This is a technique used
by
ARM(R) processors.

The FT232H will assert the TCK line and wait for the RTCK to be returned from the target device to
GPIOL3 line before changing the TDO (data out line).

FT2232H ARM CPU
RTCK
TCK
TDO
GPIOL3

Figure 4.15 Adaptive Clocking Interconnect

TDO
TCK
RTCK
TDO changes on falling
edge of TCK

Figure 4.16 Adaptive Clocking Waveform

Adaptive clocking is not enabled by default.

For further details on MPSSE adaptive clocking please refer to AN_108 Command Processor For MPSSE
and MCU Host Bus Emulation Modes.
```

### Page 34

```text
Copyright (c) Future Technology Devices International Limited  34
FT232H SINGLE CHANNEL HI-SPEED USB TO MULTIPURPOSE
UART/FIFO IC Datasheet
Version 2.1

Document No.: FT_000288 Clearance No.: FTDI #199
4.9 Fast Serial Interface Mode Description

Fast Serial Interface Mode provides a method of communicating with an external device over USB using
4
wires that can have opto -isolators in their path, thus providing galvanic isolation between
systems. Fast
serial mode is enabled by setting the appropriate bits in the external EEPROM . The fast serial mode
can
be held in reset by setting a bit value of 0x10 using the FT_SetBitMode D2XX driver command. While
this
bit is set the device is held reset - data can be sent to the device, but it will not be sent out by
the device
until the device is enabled again. This is done by sending a bit value of 0x00 using the Set Bit
Mode
command.

When the FT232H is configured in Fast Serial Interface mode the IO timing of the signals used are
shown
in Figure 4.17 and the timings are shown in Table 4.5 Fast Serial Interface Signal Timings.

Figure 4.17 Fast Serial Interface Signal Waveforms

Name Minimum Typical Maximu Units Description
t1 5 ns FSDO/FSCTS hold time
t2 5 ns FSDO/FSCTS setup time
t3 5 ns FSDI hold time
t4 10 ns FSDI Setup Time
t5 10 ns FSCLK low
t6 10 ns FSCLK high
t7 20 ns FSCLK Period

Table 4.5 Fast Serial Interface Signal Timings
```

### Page 35

```text
Copyright (c) Future Technology Devices International Limited  35
FT232H SINGLE CHANNEL HI-SPEED USB TO MULTIPURPOSE
UART/FIFO IC Datasheet
Version 2.1

Document No.: FT_000288 Clearance No.: FTDI #199
4.9.1 Outgoing Fast Serial Data
To send fast serial data out of the FT232H, the external device must drive the FSCLK clock. If the
FT232H
has data ready to send, it will drive FSDO output low to indicate the start bit. It will not do this
if it is
currently receiving data from the external device. This is illustrated in Figure 4.18.

Figure 4.18 Fast Serial Interface Output Data
Notes:

1. The first bit output (Start bit) is always 0.
2. FSDO is always sent LSB first.
3. The last serial bit output is the source bit (SRCE) is always 0.
4. If the target device is unable to accept the data when it detects the START bit, it should stop
the
FSCLK until it can accept the data.

4.9.2 Incoming Fast Serial Data
An external device is allow ed to send data into the FT232H if FSCTS is high. On receipt of a zero
START
bit on FSDI, the FT232H will drop FSCTS on the next positive clock edge. The data from bits 0 to 7
are
then clocked in (LSB first). The last bit (DEST) determines where the data w ill be written to.
This bit is
always 0 with the FT232H. This is illustrated in Figure 4.19.

Figure 4.19 Fast Serial Interface Input Data
Notes:

1. The first bit input (Start bit) is always 0.
2. FSDI is always received LSB first.
3. The last received serial bit is the destination bit (DEST) is always 0.
4.  The target device should ensure that FSCTS is high before it sends data. FSCTS goes low after
data bit 0 (D0) and stays low until the chip can accept more data.
FSCLK
FSDO 0 D0 D1 D2 D3 D4 D5 D6 D7 SRCE
Start
Bit Data Bits - LSB first
Source
Bit
FSCLK
FSDI 0 D0 D1 D2 D3 D4 D5 D6 D7 DEST
Start
Bit Data Bits - LSB first
Destination
Bit
FSCTS
```

### Page 36

```text
Copyright (c) Future Technology Devices International Limited  36
FT232H SINGLE CHANNEL HI-SPEED USB TO MULTIPURPOSE
UART/FIFO IC Datasheet
Version 2.1

Document No.: FT_000288 Clearance No.: FTDI #199
4.9.3 Fast Serial Data Interface Example

Figure 4.20 shows example of two Agilent HCPL -2430 (see the semiconductor section at
www.avagotech.com) Hi-Speed opto-couplers used to optically isolate an external device which
interfaced
to USB using the FT232H. In this example VCC5V is the USB VBUS supply and VCCE is the supply to the
external device.

Care must be taken with the voltage used to power the photo -LED. It must be the same voltage as
that
which the FT232H I/Os are driving to , or the LED's may be permanently on. Limiting resistors should
be
fitted in the lines that drive the diodes. The outpu ts of the opto-couplers are open-collector and
require a
pull-up resistor.

Figure 4.20 Fast Serial Interface Example

4.10 CPU-style FIFO Interface Mode Description

CPU-style FIFO interface mode is designed to allow a CPU to interface to USB via the FT232H. This
mode
is enabled in the external EEPROM. The interface is achieved using a chip select bit (CS#) and
address bit
(A0). When the FT232H is in CPU -style Interface mode, the IO signal lines are configured as given
in
Table 4.6. This mode uses a combination of CS# and A0 to determine the operation to be carried out.
The following Truth-Table 4.7 gives the decode values for particular operations.

CS# A0 RD# WR#
1 X X X
0 0 Read Data Pipe Write Data Pipe
0 1 Read Status Send Immediate
Table 4.6 CPU-Style FIFO Interface Operation Select
```

### Page 37

```text
Copyright (c) Future Technology Devices International Limited  37
FT232H SINGLE CHANNEL HI-SPEED USB TO MULTIPURPOSE
UART/FIFO IC Datasheet
Version 2.1

Document No.: FT_000288 Clearance No.: FTDI #199
The Status read is shown in Table 4.7 -

Data Bit Data Status
bit 0 1 Data available (=RXF)
bit 1 1 Space available (=TXE)
bit 2 1 Suspend
bit 3 1 Configured
bit 4 X  X
bit 5 X X
bit 6 X X
bit 7 X X
Table 4.7 CPU-Style FIFO Interface Operation Read Status Description

Note that bits 7 to 4 can be arbitrary values and that X= not used.

The timing of reading and writing in this mode is shown in Figure 4.21 and Table 4.8.

Figure 4.21 CPU-Style FIFO Interface Operation Signal Waveforms

Data Bit Nom Max Units Comment
t1 5  ns A0/CS# setup time to WR#
t2 5  ns A0/CS# hold time after WR# inactive
t3 5  ns A0/CS# setup time to RD#
t4 5  ns A0/CS# hold time after RD# inactive
t5 5  ns D to WR# 37active setup time
t6 5  ns D hold time after WR# inactive
t7 1 14 ns RD# to D
t8 30  ns WR# active pulse width
t9 30  ns RD# active pulse width
Table 4.8 CPU-Style FIFO Interface Operation Signal Timing

An example of the CPU-style FIFO interface connection is shown in Figure 4.22
```

### Page 38

```text
Copyright (c) Future Technology Devices International Limited  38
FT232H SINGLE CHANNEL HI-SPEED USB TO MULTIPURPOSE
UART/FIFO IC Datasheet
Version 2.1

Document No.: FT_000288 Clearance No.: FTDI #199

Figure 4.22 CPU-Style FIFO Interface Example

4.11 RS232 UART Mode LED Interface Description

When configured in UART mode the FT232H has two IO pins dedicated to controlling LED status
indicators, one for transmitted data the other for received data. When data is being transmitted or
received the respective pins drive from tristate to low in order  to provide indication on the LED's
of data
transfer. A digital one-shot timer is used so that even a small percentage of data transfer is
visible to the
end user.

Figure 4.23 Dual LED UART Configuration

Figure 4.23 shows a configuration using two individual LED's - one for transmitted data the other
for
received data.
D
0
D
1
D
2
D
3
D
4
D
5
D
6
D
7
RD
#
CS
#
WR
#
A
0
FT
232
H
IO
10
IO
11
IO
12
IO
13
IO
14
IO
15
IO
16
IO
17
IO
20
IO
23
IO
21
IO
22
Microcontroller
PWREN
#
IO
25
(
Optional
)
IO Port 2           IO Port
1
```

### Page 39

```text
Copyright (c) Future Technology Devices International Limited  39
FT232H SINGLE CHANNEL HI-SPEED USB TO MULTIPURPOSE
UART/FIFO IC Datasheet
Version 2.1

Document No.: FT_000288 Clearance No.: FTDI #199

Figure 4.24 Single LED UART Configuration

In Figure 4.24 transmit and receive LED indicators are wire -OR'ed together to give a single LED
indicator
which indicates any transmit or receive data activity.

Note that the LED's are connected to the same supply as VCCIO.

4.12 Send Immediate/Wake Up (SIWU#)

The SIWU# pin is available in the FIFO modes and in bit bang mode.

The Send Immediate portion is used to flush data from the chip back to the PC. This can be used to
force
short packets of data back to the PC without waiting for the latency timer to expire.

To avoid overrunning, this mechanism should only be used when a process of sending data to the chip
has been stopped.

The data transfer is flagged to the USB host by the falling edge of the SIWU# s ignal.  The USB host
will
schedule the data transfer on the next USB packet.

CLKOUT
WR#
SIWU#
D7-D0

Figure 4.25 Using SIWU#

When the pin is being used for a Wake Up  function to wake up a sleeping PC a 20ms negative pulse on
this pin is required.   When the pin is used to immediately flush the buffer (Send Immediate) a
250ns
negative pulse on this pin is required.
```

### Page 40

```text
Copyright (c) Future Technology Devices International Limited  40
FT232H SINGLE CHANNEL HI-SPEED USB TO MULTIPURPOSE
UART/FIFO IC Datasheet
Version 2.1

Document No.: FT_000288 Clearance No.: FTDI #199
Notes:

1. When using remote wake -up, ensure the resistors are pulled -up in suspend. Also ensure
peripheral
designs do not allow any current sink paths that may partially power the peripheral.
2. If remote wake -up is enabled, a peripheral is allowed to draw up to  2.5mA in suspend. If remote
wake-up is disabled, the peripheral must draw no more than 500uA in suspend.
3. If a Pull-down is enabled, the FT232H will not wake up from suspend when using SIWU#
4. In UART mode the RI# pin acts as the wake up pin.

4.13 FT232H Mode Selection

The FT232H defaults to asynchronous serial interface (UART) mode of operation.

After a reset the required mode is determined by the contents of the external EEPROM which can be
programmed using FT_Prog.

The EEPROM contents determine if the FT232H device is configured as FT232 asynchronous serial
interface, FT245 FIFO interface, CPU-style FIFO interface, FT1248 or Fast Serial Interface.

Following a reset, the EEPROM is read and the FT232H configured for the selected mode. After device
enumeration, the FT_SetBitMode command (refer to D2XX_Programmers_Guide) can be sent to the
USB driver to switch the selected interface into other modes - asynchronous bit-bang, synchronous
bit-
bang or MPSSE - if required.

When in FT245 FIFO mode, the FT_SetBitMode command can be used to select Synchronous FIFO
(FT_SetBitMode = 0x40).  Note that FT 245 FIFO mode must be configured in the EEPROM before
selecting the Synchronous FIFO mode.

The drive strength selection, slew rate and Schmitt input function can also be configured in the
EEPROM.

The MPSSE can be configured directly using the D2XX commands. The D2XX_Programmers_Guide is
available from the FTDI website. The application note AN_108 - Command Processor for MPSSE and MCU
Host Bus Emulation Modes gives further explanation and examples for the MPSSE.

4.14 Modes Configuration

This section summarises what modes are configurable using the external EEPROM or the application
software.

ASYNC
Serial
UART
STYLE
ASYNC
245
FIFO
SYNC
245
PARALLEL
FIFO
FT1248 ASYNC
Bit-
Bang
SYNC
Bit-
Bang
MPSSE Fast
Serial
Interface
CPU-
Style
FIFO
EEPROM
configured YES YES YES YES NO NO NO YES YES
Application
Software
configured
NO NO YES NO YES YES YES RESET NO
Table 4.9 Configuration Using EEPROM and Application Software
Note:

1. The Synchronous 245 FIFO mode requires both the EEPROM and application software mode
settings
2. The application software can be used to reset the fast serial interface controller
```

### Page 41

```text
Copyright (c) Future Technology Devices International Limited  41
FT232H SINGLE CHANNEL HI-SPEED USB TO MULTIPURPOSE
UART/FIFO IC Datasheet
Version 2.1

Document No.: FT_000288 Clearance No.: FTDI #199
5 Devices Characteristics and Ratings
5.1 Absolute Maximum Ratings

The absolute maximum ratings for the FT232H devices are as follows. These are in accordance with the
Absolute Maximum Rating System (IEC 60134). Exceeding these values may cause permanent damage to
the device.

Parameter Value Unit Conditions
Storage Temperature -65 degC to 150 degC Degrees
C

Floor Life (Out of Bag) At Factory
Ambient
(30 degC / 60% Relative Humidity)
168 Hours
(IPC/JEDEC J-STD-033A MSL Level
3 Compliant)*
Hours

Ambient Operating Temperature (Power
Applied) -40 degC to 85 degC Degrees
C

MTTF FT232HL TBD Hours
MTTF FT232HL TBD Hours
VCORE Supply Voltage -0.3 to +2.0 V
VCCIO IO Voltage -0.3 to +4.0 V
DC Input Voltage - USBDP and USBDM -0.5 to  +3.63 V
DC Input Voltage - High Impedance
Bi-directional (ACBUS and ADBUS
powered from VCCIO)
-0.3 to +5.8 V

DC Output Current - Outputs 16 mA
Table 5.1 Absolute Maximum Ratings

* If devices are stored out of the packaging beyond this time limit the devices should be baked
before
use. The devices should be ramped up to a temperature of +125 degC and baked for up to 17 hours.

5.2 DC Characteristics

The I/O pins are +3.3v cells, which are +5V tolerant (except the USB PHY pins).

DC Characteristics (Ambient Temperature = -40 degC to +85 degC)

Parameter Description Minimum Typical Maximum Units Conditions
VCORE VCC Core Operating
Supply Voltage 1.62 1.8 1.98 V
VCCIO* VCCIO Operating
Supply Voltage 2.97  3.63 V Cells are 5V tolerant
VREGIN
5 Volts
VREGIN Voltage
regulator Input 3.6 5 5.5 V 5 volt input to
VREGIN
VREGIN
3.3 Volts
VREGIN Voltage
regulator Input 3.0 3.3 3.6 V 3.3 volt input to
VREGIN (Note 1)
Ireg Regulator Current  54  mA VREGIN +5V
Ireg Regulator Current  52  mA VREGIN +3.3V
Icc1 Core Operating Supply
Current  24  mA VCORE = +1.8V
Normal Operation
Icc1r Core Reset Supply
Current  4.3  mA VCORE = +1.8V
Device in reset state
Icc1s Core Suspend Supply
Current  330  uA VCORE = +1.8V
USB Suspend
Table 5.2 Operating Voltage and Current (except PHY)

Note: Failure to connect all VCCIO pins of the device will have unpredictable behaviour.
Note 1: The 3.3V operation is for Revision C, see the errata for previous revisions
```

### Page 42

```text
Copyright (c) Future Technology Devices International Limited  42
FT232H SINGLE CHANNEL HI-SPEED USB TO MULTIPURPOSE
UART/FIFO IC Datasheet
Version 2.1

Document No.: FT_000288 Clearance No.: FTDI #199
The I/O pins are +3.3v cells, which are +5V tolerant (except the USB PHY pins).

Parameter Description Minimum Typical Maximum Units Conditions
Voh Output Voltage High
2.4 VCCIO VCCIO V
Ioh = +/-2mA
I/O Drive
strength* = 4mA
2.4 VCCIO VCCIO V I/O Drive
strength* = 8mA
2.4 VCCIO VCCIO V
I/O Drive
strength* =
12mA
2.4 VCCIO VCCIO V
I/O Drive
strength* =
16mA
Vol Output Voltage Low
 0 0.4 V
Iol = +/-2mA
I/O Drive
strength* = 4mA
 0 0.4 V I/O Drive
strength* = 8mA
 0 0.4 V
I/O Drive
strength* =
12mA
 0 0.4 V
I/O Drive
strength* =
16mA
Vil Input low Switching
Threshold   0.8 V LVTTL
Vih Input High Switching
Threshold 2.0   V LVTTL
Vt Switching Threshold  1.5  V LVTTL
Vt- Schmitt trigger negative
going threshold voltage 0.8 1.1  V
Vt+ Schmitt trigger positive
going threshold voltage  1.6 2.0 V
Rpu Input pull-up resistance 40 75 190 Kohm Vin = 0
Rpd Input pull-down resistance 40 75 190 Kohm Vin =VCCIO
Iin Input Leakage Current -10 +/-1 10 uA Vin = 0
Ioz Tristate output leakage
current -10 +/-1 10 uA Vin = 5.5V or 0
Table 5.3 I/O Pin Characteristics VCCIO = +3.3V (except USB PHY pins)

* The I/O drive strength and slow slew-rate are configurable in the EEPROM.

DC Characteristics (Ambient Temperature = -40 degC to +85 degC)

Parameter Description Minimum Typical Maximum Units Conditions
VPHY,
VPLL
PHY Operating Supply
Voltage 3.0 3.3 3.6 V 3.3V I/O
Iccphy PHY Operating Supply
Current --- 30 60 mA Hi-speed operation at
480 MHz
Iccphy
(susp)
PHY Operating Supply
Current --- 10 50 uA USB Suspend
Table 5.4 PHY Operating Voltage and Current

Parameter Description Minimum Typical Maximum Units Conditions
Voh Output Voltage High VCORE-0.2   V
Vol Output Voltage Low   0.2 V
Vil Input low Switching Threshold  - 0.8 V
Vih Input High Switching Threshold 2.0 -  V
Table 5.5 PHY I/O Pin Characteristics
```

### Page 43

```text
Copyright (c) Future Technology Devices International Limited  43
FT232H SINGLE CHANNEL HI-SPEED USB TO MULTIPURPOSE
UART/FIFO IC Datasheet
Version 2.1

Document No.: FT_000288 Clearance No.: FTDI #199
5.3 ESD Tolerance
ESD protection for FT232H IO's

Parameter Reference Minimum Typical Maximum Units
Human Body Model
(HBM)
JEDEC EIA/JESD22-A114-B,
Class 2  +/-2kV  kV
Machine Mode (MM) JEDEC EIA/JESD22-A115-A,
Class B  +/-200V  V
Charge Device Model
(CDM)
JEDEC EIA/ JESD22-C101-D,
Class-III  +/-500V  V
Latch-up JESD78, Trigger Class-II  +/-200mA  mA
Table 5.6 ESD Tolerance
```

### Page 44

```text
Copyright (c) Future Technology Devices International Limited  44
FT232H SINGLE CHANNEL HI-SPEED USB TO MULTIPURPOSE
UART/FIFO IC Datasheet
Version 2.1

Document No.: FT_000288 Clearance No.: FTDI #199
6 FT232H Configurations

The following section illustrates possible USB power configurations for the FT232H.

All USB power configurations illustrated apply to both package options for the FT232H device.

6.1 USB Bus Powered Configuration

Bus Powered Application example 1: Bus powered configuration running on +5V.

Figure 6.1 Bus Powered Configuration Example 1

Figure 6.1 illustrates the FT232H in a typical USB bus powered design configuration. A USB bus
powered
device gets its power from the VBUS (+5V) which is connected to VREGIN.  In this application, the
VREGIN is the +5V input to the on chip +3.3V/1.8V regulator. The output of the on chip LDO regulator
(+1.8V) drives pin 38, (VCORE), and pin 37, (VCCA).

The output of the on chip LDO regulator (3.3V) supplies 3.3V to the VCCIOs, VPLL and VPHY through
pin
39, VCCD. Please note that when the FT232H running on +5V (VREGIN), the VCCD becomes an output.

Note:
1. In this application, pin 40 (VREGIN) is the +5V input to the on chip +3.3V/1.8V regulator.
Since the VREGIN is +5.0V, pin 39 (VCCD) becomes 3V3 output and supplies 3.3V to the
VCCIOs, VPLL and VPHY.
2. The output of the on chip LDO +3.3V/1.8V regulator (+1.8V) drives pin 38, the FT232H core
supply (VCORE) and pin 37, the VCCA.
```

### Page 45

```text
Copyright (c) Future Technology Devices International Limited  45
FT232H SINGLE CHANNEL HI-SPEED USB TO MULTIPURPOSE
UART/FIFO IC Datasheet
Version 2.1

Document No.: FT_000288 Clearance No.: FTDI #199
6.2 USB Self Powered Configuration
6.2.1 Self-Powered Application Example 1
Self-powered configuration running on 5V.

Figure 6.2 Self-Powered Configuration Example 1

Figure 6.2 illustrates the FT232H in a typical USB self-powered configuration. A USB self-powered
device
gets its power from its own external power supply which is connected to VREGIN. In this application
the
VREGIN is the +5V input to the on chip +3.3V/1.8V regulator. The output of the on chip LDO regulator
(+1.8V) drives pin 38, VCORE and pin 37, VCCA. The output of the on chip LDO regulator (3.3V)
supplies

3.3V to the VCCIOs, VPLL and VPHY through VCCD.

Please note that when the FT232H running on +5V (VREGIN), the VCCD becomes an output.

Note that in this set -up, the EEPROM should be configured  for self-powered operation and the
option
"suspend on ACBUS7 low" is enabled  in FT_Prog. This configuration uses the ACBUS7  pin, when this
function is enabled ACBUS7 should not be used as a GPIO in MPSSE mode.
```

### Page 46

```text
Copyright (c) Future Technology Devices International Limited  46
FT232H SINGLE CHANNEL HI-SPEED USB TO MULTIPURPOSE
UART/FIFO IC Datasheet
Version 2.1

Document No.: FT_000288 Clearance No.: FTDI #199
6.2.2 Self-Powered Application Example 2
Self-powered configuration running on 3.3V.

Figure 6.3 Self-Powered Configuration Example 2

Figure 6.3 illustrates the FT232H in a typical USB self-powered configuration similar to Figure 6.2.
The
difference here is that the VREGIN is connected to the external 3V3 LDO regulator output which
supplies
3.3V to the VCCIOs, VCCD, VPLL and VPHY. P lease note that when the FT232H running on +3V3
(VREGIN), the VCCD becomes an input. In this application the VREGIN is the +3V3 input to the on
chip+3.3V/1.8V regulator. The output of the on chip LDO regulator (+1.8V) drives pin 38, VCORE and
pin
37, VCCA.

Note that in this set -up, the EEPROM should be configured for self -powered operation and the
option
"suspend on ACBUS7 low" selected in FT_Prog. This configuration uses the ACBUS7  pin, when this
function is enabled ACBUS7 should not be used as a GPIO in MPSSE mode.
```

### Page 47

```text
Copyright (c) Future Technology Devices International Limited  47
FT232H SINGLE CHANNEL HI-SPEED USB TO MULTIPURPOSE
UART/FIFO IC Datasheet
Version 2.1

Document No.: FT_000288 Clearance No.: FTDI #199
6.3 Oscillator Configuration

Figure 6.4 Recommended FT232H Oscillator Configuration

Figure 6.4 illustrates how to connect the FT232H with a 12MHz +/- 0.003% crystal. In this case l
oading
capacitors should to be added between OSCI, OSCO and GND as shown. A value of 27pF is shown as the
capacitor in the example - this will be good for many crystals but it is recommended to select the
loading
capacitor value based on the manufacturer's  recommendations wherever possible. It is recommended to
use a fundamental mode, parallel cut type crystal.

It is also possible to use a 12 MHz Oscillator with the FT232H. In this case the output of the
oscillator
would drive OSCI, and OSCO should be lef t unconnected. The oscillator must have a CMOS output drive
capability.

Parameter Description Minimum Typical Maximum Units Conditions
OSCI Vin Input Voltage 2.97 3.3V 3.63 V
Fin Input Frequency  12MHz  MHz +/- 30ppm
Ji Cycle to cycle jitter  <150  pS
Table 6.1 OSCI Input characteristics
```

### Page 48

```text
Copyright (c) Future Technology Devices International Limited  48
FT232H SINGLE CHANNEL HI-SPEED USB TO MULTIPURPOSE
UART/FIFO IC Datasheet
Version 2.1

Document No.: FT_000288 Clearance No.: FTDI #199
7 EEPROM Configuration
7.1 EEPROM Interface
The FT232H uses configuration data from an external EEPROM. The EEPROM must be 16 bits wide
(93LC56B) and powered from the same net as the core supply of +2.97 to +3.63 volts.   Adding an
external (93LC56B) EEPROM allows the chip  to be configured as a serial UART (RS232 mode), parallel
FIFO (245) mode, FT1248, fast serial (opto isolation) or CPU-Style FIFO.

Figure 7.1 EEPROM Interface

The external EEPROM can also be used to customise the USB VID, PID, Serial Number, Product
Description Strings and Power Descriptor value of the FT232H for OEM applications. Other parameters
controlled by the EEPROM include Remote Wake Up, Soft Pull Down o n Power -Off and I/O pin drive
strength.

If the FT232H is used without an external EEPROM the chip defaults to a USB to asynchronous serial
UART (RS232 mode) port device. If no EEPROM is connected (or the EEPROM is blank), the FT232H uses
its built-in default VID (0403), PID (6014) Product Description and Power Descriptor Value. In this
case,
the device will not have a serial number as part of the USB descriptor.

7.2 Default EEPROM Configuration
The external EEPROM (if it's fitted) can be programmed over USB using FT_Prog. This allows a blank
part
to be soldered onto the PCB and programmed as part of the manufacturing and test pro cess.  Users
who
do not have their own USB Vendor ID but who would like to use a unique Product ID in their design
can
apply to FTDI for a free block of unique PIDs.

Contact FTDI support for this service.

Parameter Value Notes
USB Vendor ID (VID) 0403h FTDI default VID (hex)
USB Product UD (PID) 6014h FTDI default PID (hex)
bcd Device  009h
Serial Number
Enabled?
Yes
Serial Number See Note None
Pull down I/O Pins in
USB Suspend
Disabled Enabling this option will make the device pull down on the UART
interface lines when in USB suspend mode (PWREN# is high).
Manufacturer Name FTDI
Product Description Single
RS232-HS

Max Bus Power
Current
500mA
```

### Page 49

```text
Copyright (c) Future Technology Devices International Limited  49
FT232H SINGLE CHANNEL HI-SPEED USB TO MULTIPURPOSE
UART/FIFO IC Datasheet
Version 2.1

Document No.: FT_000288 Clearance No.: FTDI #199
Parameter Value Notes
Power Source Bus
Powered

Device Type FT232H
USB Version 0200 Returns USB 2.0 device description to the host.
Remote Wake Up Disabled Taking RI# low will wake up the USB host controller from suspend
in approximately 20 Ms. If enabled.
Hardware Interface UART Allows the user to select the hardware mode of the device.
Options include: RS232 UART, 245 FIFO, CPU 245, OPTO Isolate
and FT1248.
FT1248 Settings 00h FT1248 can be configured to set: Clock Polarity High; Bit Order
LSB and Flow Control Not Selected.
Suspend ACBus7 Low Disabled Enters low power state on ACBus7.
High Current I/Os Disabled Enables the high drive level on the UART and ACBUS I/O pins.
Load VCP Driver Enabled Makes the device load the VCP driver interface for the device.
ACBUS0 TriSt-PU Default configuration of ACBUS0 - Input pulled up
ACBUS1 TriSt-PU Default configuration of ACBUS1 - Input pulled up
ACBUS2 TriSt-PU Default configuration of ACBUS2 Input pulled up
ACBUS3 TriSt-PU Default configuration of ACBUS3 - Input pulled up
ACBUS4 TriSt-PU Default configuration of ACBUS4 - Input pulled up
ACBUS5 TriSt-PU Default configuration of ACBUS5 - Input pulled up
ACBUS6 TriSt-PU Default configuration of ACBUS6 - Input pulled up
ACBUS7 TriSt-PD Default configuration of ACBUS7 - Input pulled down
ACBUS8 TriSt-PU Default configuration of ACBUS8 - Input pulled up
ACBUS9 TriSt-PU Default configuration of ACBUS9 - Input pulled up
Table 7.1 Default External EEPROM Configuration
```

### Page 50

```text
Copyright (c) Future Technology Devices International Limited  50
FT232H SINGLE CHANNEL HI-SPEED USB TO MULTIPURPOSE
UART/FIFO IC Datasheet
Version 2.1

Document No.: FT_000288 Clearance No.: FTDI #199
8 Package Parameters

The FT232H is available in two different packages. The FT232HL is the LQFP -48 option and the
FT232HQ
is the QFN-48 package option. The solder reflow profile for both packages is described in section
8.3.

8.1 FT232HQ, QFN-48 Package Dimensions

Figure 8.1 48 pin QFN Package Details

Notes:

1. All dimensions are in mm.
2. The date code format is YYXX where XX = 2 digit week number, YY = 2 digit year number.  This
is followed by the revision number.
3. The code XXXXXXX is the manufacturing LOT code.
4. The central soldering pad is floating.  Connect it to GND.
```

### Page 51

```text
Copyright (c) Future Technology Devices International Limited  51
FT232H SINGLE CHANNEL HI-SPEED USB TO MULTIPURPOSE
UART/FIFO IC Datasheet
Version 2.1

Document No.: FT_000288 Clearance No.: FTDI #199
8.2 FT232HL, LQFP-48 Package Dimensions

Figure 8.2 48 pin LQFP Package Details

Notes:

1. All dimensions are in mm.
2. The date code format is YYXX where XX = 2 digit  week number, YY = 2 digit year number.  This
is followed by the revision number.
3. The code XXXXXXX is the manufacturing LOT code.
```

### Page 52

```text
Copyright (c) Future Technology Devices International Limited  52
FT232H SINGLE CHANNEL HI-SPEED USB TO MULTIPURPOSE
UART/FIFO IC Datasheet
Version 2.1

Document No.: FT_000288 Clearance No.: FTDI #199
8.3 Solder Reflow Profile

Figure 8.3 48 pin LQFP and QFN Reflow Solder Profile

Profile Feature
Pb Free Solder
Process
(green material)
SnPb Eutectic and Pb free (non green
material) Solder Process
 Average Ramp Up Rate (Ts to Tp)   3 degC / second Max. 3 degC / Second Max.
Preheat
- Temperature Min (Ts Min.)
- Temperature Max (Ts Max.)
- Time (ts Min to ts Max)

150 degC
200 degC
60 to 120 seconds

100 degC
150 degC
60 to 120 seconds
 Time Maintained Above Critical
Temperature TL:
- Temperature (TL)
- Time (tL)

217 degC
60 to 150 seconds

183 degC                                                      60
to 150 seconds
 Peak Temperature (Tp)   260 degC
```

### Page 53

```text
Copyright (c) Future Technology Devices International Limited  53
FT232H SINGLE CHANNEL HI-SPEED USB TO MULTIPURPOSE
UART/FIFO IC Datasheet
Version 2.1

Document No.: FT_000288 Clearance No.: FTDI #199
 Time within 5 degC of actual Peak
Temperature (tp)   30 to 40 seconds 20 to 40 seconds
 Ramp Down Rate  6 degC / second Max. 6 degC / second Max.
Time for T= 25 degC to Peak
Temperature, Tp   8 minutes Max. 6 minutes Max.
Table 8.1 Reflow Profile Parameter Values

SnPb Eutectic and Pb free (non green material)
 Package Thickness   Volume mm3 < 350  Volume mm3 >=350
< 2.5 mm  235 +5/-0 deg C  220 +5/-0 deg C
>= 2.5 mm  220 +5/-0 deg C  220 +5/-0 deg C

Pb Free (green material) = 260 +5/-0 deg C
Table 8.2 Package Reflow Peak Temperature
```

### Page 54

```text
Copyright (c) Future Technology Devices International Limited  54
FT232H SINGLE CHANNEL HI-SPEED USB TO MULTIPURPOSE
UART/FIFO IC Datasheet
Version 2.1

Document No.: FT_000288 Clearance No.: FTDI #199
9 Contact Information
Head Office - Glasgow, UK

Future Technology Devices International Limited
Unit 1, 2 Seaward Place, Centurion Business Park
Glasgow G41 1HH
United Kingdom
Tel: +44 (0) 141 429 2777
Fax: +44 (0) 141 429 2758

E-mail (Sales) sales1@ftdichip.com
E-mail (Support) support1@ftdichip.com
E-mail (General Enquiries) admin1@ftdichip.com

Branch Office - Taipei, Taiwan

Future Technology Devices International Limited
(Taiwan)
2F, No. 516, Sec. 1, NeiHu Road
Taipei 114
Taiwan, R.O.C.
Tel: +886 (0) 2 8797 1330
Fax: +886 (0) 2 8751 9737

E-mail (Sales) tw.sales1@ftdichip.com
E-mail (Support) tw.support1@ftdichip.com
E-mail (General Enquiries) tw.admin1@ftdichip.com

Branch Office - Tigard, Oregon, USA

Future Technology Devices International Limited
(USA)
7130 SW Fir Loop
Tigard, OR 97223-8160
USA
Tel: +1 (503) 547 0988
Fax: +1 (503) 547 0987

E-Mail (Sales) us.sales@ftdichip.com
E-Mail (Support) us.support@ftdichip.com
E-Mail (General Enquiries) us.admin@ftdichip.com

Branch Office - Shanghai, China

Future Technology Devices International Limited
(China)
Room 1103, No. 666 West Huaihai Road,
Shanghai, 200052
China
Tel: +86 21 62351596
Fax: +86 21 62351595

E-mail (Sales) cn.sales@ftdichip.com
E-mail (Support) cn.support@ftdichip.com
E-mail (General Enquiries) cn.admin@ftdichip.com

Web Site

http://ftdichip.com

Distributor and Sales Representatives
Please visit the Sales Network page of the FTDI Web site for the contact details of our
distributor(s) and sales
representative(s) in your country.

System and equipment manufacturers and designers are responsible to ensure that their systems, and
any Future Technology
Devices International Ltd (FTDI) devices incorporated in their systems, meet all applicable safety,
regulatory and system -level
performance requirements. All application -related information in this document (including
application descriptions, suggested
FTDI devices and other materials) is provided for reference only. While FTDI has taken care to
assure it is accurate, this
information is subject to  customer confirmation, and FTDI disclaims all liability for system
designs and for any applications
assistance provided by FTDI. Use of FTDI devices in life support and/or safety applications is
entirely at the user's risk, a nd the
user agrees to defend, indemnify and hold harmless FTDI from any and all damages, claims, suits or
expense resulting from
such use. This document is subject to change without notice. No freedom to use patents or other
intellectual property rights is
implied by the publication of  this document. Neither the whole nor any part of the information
contained in, or the product
described in this document, may be adapted or reproduced in any material or electronic form without
the prior written consent
of the copyright holder. Future Tec hnology Devices International Ltd, Unit 1, 2 Seaward Place,
Centurion Business Park,
Glasgow G41 1HH, United Kingdom. Scotland Registered Company Number: SC136640
.
```

### Page 55

```text
Copyright (c) Future Technology Devices International Limited  55
FT232H SINGLE CHANNEL HI-SPEED USB TO MULTIPURPOSE
UART/FIFO IC Datasheet
Version 2.1

Document No.: FT_000288 Clearance No.: FTDI #199
Appendix A - References
Document References
AN_108 - Command Processor for MPSSE and MCU Host Bus Emulation Modes
AN_113 - Interfacing FT2232H Hi-Speed Devices to I2C Bus
AN_114 - Interfacing FT2232H Hi-Speed Devices to SPI Bus
AN_129 - Interfacing FT2232H Hi-Speed Devices to a JTAG TAP
AN_135 - MPSSE Basics
AN_167_FT1248 Parallel Serial Interface Basics

Acronyms and Abbreviations
Terms Description
CPU Central Processing Unit
EEPROM Electrically Erasable Programmable Read Only Memory
ESD Electrostatic Discharge
FIFO First In First Out
I2C Inter-Integrated Circuit
LDO Low Drop Out
LED Light Emitting Diode
LSB Least Significant Bit First
LQFP Low Profile Quad Flat Pack
MPSSE Multi- Protocol Synchronous Serial Engines
QFN Quad Flat Non-leaded package
SPI Serial Peripheral Interface
TTL Transistor-Transistor Logic
USB Universal Serial Bus
UART Universal Asynchronous Receiver / Transmitter
UTMI Universal Transceiver Macrocell Interface
```

### Page 56

```text
Copyright (c) Future Technology Devices International Limited  56
FT232H SINGLE CHANNEL HI-SPEED USB TO MULTIPURPOSE
UART/FIFO IC Datasheet
Version 2.1

Document No.: FT_000288 Clearance No.: FTDI #199
Appendix B - List of Figures and Tables
List of Tables
Table 3.1 Power and Ground
........................................................................................................
11
Table 3.2 Common Function Pins
..................................................................................................
11
Table 3.3 EEPROM Interface Group
............................................................................................... 12
Table 3.4 UART Interface and ACBUS Group (see note 1)
................................................................ 12
Table 3.5 ACBUS Configuration Control
......................................................................................... 13
Table 3.6 UART Configured Pin Descriptions
................................................................................... 14
Table 3.7 FT245 Synchronous FIFO Configured Pin Descriptions
....................................................... 15
Table 3.8 FT245 Style Asynchronous FIFO Configured Pin Descriptions
.............................................. 16
Table 3.9 Synchronous or Asynchronous Bit-Bang Configured Pin Descriptions
................................... 16
Table 3.10 MPSSE Configured Pin Descriptions
............................................................................... 17
Table 3.11 Fast Serial Interface Configured Pin
Descriptions............................................................. 17
Table 3.12 CPU-style FIFO Interface Configured Pin Descriptions
...................................................... 18
Table 3.13 FT1248 Configured Pin Descriptions
.............................................................................. 18
Table 4.1 FT245 Synchronous FIFO Interface Signal Timings
............................................................ 25
Table 4.2 Asynchronous FIFO Timings (based on standard drive level outputs)
................................... 26
Table 4.3 Synchronous Bit-Bang Mode Timing Interface Example Timings
.......................................... 31
Table 4.4 MPSSE Signal Timings
...................................................................................................
32
Table 4.5 Fast Serial Interface Signal Timings
................................................................................ 34
Table 4.6 CPU-Style FIFO Interface Operation Select
....................................................................... 36
Table 4.7 CPU-Style FIFO Interface Operation Read Status Description
.............................................. 37
Table 4.8 CPU-Style FIFO Interface Operation Signal Timing
............................................................ 37
Table 4.9 Configuration Using EEPROM and Application Software
...................................................... 40
Table 5.1 Absolute Maximum Ratings
............................................................................................ 41
Table 5.2 Operating Voltage and Current (except PHY)
.................................................................... 41
Table 5.3 I/O Pin Characteristics VCCIO = +3.3V (except USB PHY pins)
........................................... 42
Table 5.4 PHY Operating Voltage and Current
................................................................................. 42
Table 5.5 PHY I/O Pin Characteristics
............................................................................................ 42
Table 5.6 ESD Tolerance
..............................................................................................................
43
Table 6.1 OSCI Input characteristics
............................................................................................. 47
Table 7.1 Default External EEPROM Configuration
........................................................................... 49
Table 8.1 Reflow Profile Parameter Values
..................................................................................... 53
Table 8.2 Package Reflow Peak Temperature
.................................................................................. 53
```

### Page 57

```text
Copyright (c) Future Technology Devices International Limited  57
FT232H SINGLE CHANNEL HI-SPEED USB TO MULTIPURPOSE
UART/FIFO IC Datasheet
Version 2.1

Document No.: FT_000288 Clearance No.: FTDI #199
List of Figures
Figure 2.1 FT232H Block Diagram
...................................................................................................
4
Figure 3.1 FT232H Schematic Symbol
............................................................................................. 8
Figure 4.1 RS232 Configuration
....................................................................................................
21
Figure 4.2 Dual RS422 Configuration
............................................................................................. 22
Figure 4.3 Dual RS485 Configuration
............................................................................................. 23
Figure 4.4 FT245 Synchronous FIFO Interface Signal Waveforms
...................................................... 24
Figure 4.5 FT245 Asynchronous FIFO Interface READ Signal Waveforms
............................................ 26
Figure 4.6 FT245 Asynchronous FIFO Interface WRITE Signal Waveforms
.......................................... 26
Figure 4.7 FT1248 Bus with Single Master and Slave.
...................................................................... 27
Figure 4.8 FT1248 Basic Waveform Protocol
................................................................................... 27
Figure 4.9 FT1248 Command Structure
......................................................................................... 28
Figure 4.10 FT1248 1-bit Mode Protocol (WRITE)
............................................................................ 29
Figure 4.11 FT1248 1-bit Mode Protocol (READ)
............................................................................. 29
Figure 4.12 Synchronous Bit-Bang Mode Timing Interface Example
................................................... 31
Figure 4.13- Bit-bang Mode Dataflow Illustration Diagram
............................................................... 32
Figure 4.14 MPSSE Signal Waveforms
........................................................................................... 32
Figure 4.15 Adaptive Clocking
Interconnect.................................................................................... 33
Figure 4.16 Adaptive Clocking Waveform
....................................................................................... 33
Figure 4.17 Fast Serial Interface Signal
Waveforms......................................................................... 34
Figure 4.18 Fast Serial Interface Output Data
................................................................................. 35
Figure 4.19 Fast Serial Interface Input Data
................................................................................... 35
Figure 4.20 Fast Serial Interface Example
...................................................................................... 36
Figure 4.21 CPU-Style FIFO Interface Operation Signal Waveforms
................................................... 37
Figure 4.22 CPU-Style FIFO Interface Example
............................................................................... 38
Figure 4.23 Dual LED UART Configuration
...................................................................................... 38
Figure 4.24 Single LED UART Configuration
.................................................................................... 39
Figure 4.25 Using SIWU#
............................................................................................................
39
Figure 6.1 Bus Powered Configuration Example
1............................................................................ 44
Figure 6.2 Self-Powered Configuration Example 1
........................................................................... 45
Figure 6.3 Self-Powered Configuration Example 2
........................................................................... 46
Figure 6.4 Recommended FT232H Oscillator Configuration
............................................................... 47
Figure 7.1 EEPROM Interface
........................................................................................................
48
Figure 8.1 48 pin QFN Package Details
.......................................................................................... 50
Figure 8.2 48 pin LQFP Package Details
......................................................................................... 51
Figure 8.3 48 pin LQFP and QFN Reflow Solder Profile
..................................................................... 52
```

### Page 58

```text
Copyright (c) Future Technology Devices International Limited  58
FT232H SINGLE CHANNEL HI-SPEED USB TO MULTIPURPOSE
UART/FIFO IC Datasheet
Version 2.1

Document No.: FT_000288 Clearance No.: FTDI #199
Appendix C - Revision History
Document Title: FT232H Single Channel Hi-Speed USB to Multipurpose UART/FIFO IC
Datasheet
Document Reference No.: FT_000288
Clearance No.:    FTDI #199
Product Page:   https://ftdichip.com/product-category/products/ic/?series_products=51
Document Feedback:  Send Feedback

Revision Changes Date
Version 1.0 Initial Release 2011-02-24
Version 1.1 Changes made to ACBUS7 details; Updated the reset line of the
schematics; Added USB Compliance logo and TID 2011-04-19
Version 1.2 Corrected TID Number 2011-04-29
Version 1.3 Changed the value of recommended capacitor on the Reset# pin;
Changed signal label of WR to WR#  2011-05-16
Version 1.4 Missing #(active low) on WR signal page 8 and page 40; Enhanced
recommended schematics. 2011-09-08
Version 1.5
Added Pin 31 ACBUS7 Description (Table 0.1); Added Package
Dimension Tolerance in Section 8.2; Added a list of unsupported baud
rates to section 4.1 data transfer rate
2011-11-25
Version 1.6 Updated section 1.1, Linux Version; Updated Timing information, Figure
4.21 and Table 4.8; Updated section 7.2 default descriptors 2012-01-25
Version 1.7 Added a note on Section 4.2, EEPROM interface; 93LC46B is not
compatible with the FT232H 2012-06-21
Version 1.8 Modified the IC mark, Figure 8.1 and Figure 8.2; Update contact
information 2012-12-13
Version 1.81
Added detail to QFN drawing regarding the center pad; Corrected figure
6.4; Added clarification for which signals are 5V tolerant; Clarified
ACBUS default functions  on P8
2013-01-04
Version 1.82 Updated ADBUS7 to ACBUS7 on page 10; Added support for Windows
10; Removed year from the copyright information 2016-02-05
Version 1.83 Corrected the typo error in table 3.13  2017-11-22
Version 1.84 Updated Section 6.2.2 (Self-Powered Application Example 2- ACBUS7
pin function) 2018-05-11
Version 1.85 Correct the MPSSE timing spec in table 4.4 2018-07-23
Version 1.9 Updated Figure 8.1 and Figure 8.2 package dimensions 2019-05-27
Version 2.0 Updated Section 3.5.3 header 2019-11-29
Version 2.1 Updated CPU-Style FIFO wake-up details in section 3.2 and 4.10. In this 07-09-2023
```

### Page 59

```text
Copyright (c) Future Technology Devices International Limited  59
FT232H SINGLE CHANNEL HI-SPEED USB TO MULTIPURPOSE
UART/FIFO IC Datasheet
Version 2.1

Document No.: FT_000288 Clearance No.: FTDI #199
mode, wake-up is requested by the states of ACBUS1/ACBUS1/ACBUS3
instead of by SI/WU#.
In section 5.2 Table 5.2 changed minimum value from 3.3V to 3.0V.
Updated Figures 8.1 and 8.2.
```
