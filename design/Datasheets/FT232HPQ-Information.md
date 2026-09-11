# Figure 1: HP series

## Source

- **Source PDF:** [FT232HPQ-Information.pdf](FT232HPQ-Information.pdf)
- **Generated Markdown:** `FT232HPQ-Information.md`
- **Page count:** 3
- **Conversion method:** automated local PDF text extraction with pypdf/pdfplumber

## PDF Metadata

| Field | Value |
| :--- | :--- |
| Title |  |
| Author |  |
| Subject |  |
| Creator | Adobe InDesign 20.0 (Windows) |
| Producer | Adobe PDF Library 17.0 |

## Extracted Technical Index

This markdown datasheet is meant to reduce the need to reopen the PDF during design work.
It preserves design-relevant extracted snippets first, followed by page-by-page text so the source content remains locally searchable.

### Part number and ordering information

- (MAX) / PACKAGE / PART NUMBER PACKAGE PACKING PRODUCT CODE NOTE CHANNELS USB / CONNECTOR I/O CONNECTOR / FT232HP Single channel high speed

### Pin, pad, and connection designations

- Designed to eliminate the need for separate data bridge and PD ICs, / it offers efficient data transfer and the ability to power and connect / multiple peripherals through a single port, streaml…
- charging and power sourcing. / \* The HP Series is an enhanced series derived from the original H / Series, offering an upgrade path that adds USB Type-C support. / OVERVIEW / HP Family Series
- HP Family Series / Power Delivery Series / • Up to 2 x USB PD 3.0 Ports. One channel is for power and data / while the other channel is for power only / • Supports 5V3A, 9V3A, 12V3A, 15V3A, 20V3…
- • Up to 2 x USB PD 3.0 Ports. One channel is for power and data / while the other channel is for power only / • Supports 5V3A, 9V3A, 12V3A, 15V3A, 20V3A and more power / profiles / • Single chip…
- • Supports 5V3A, 9V3A, 12V3A, 15V3A, 20V3A and more power / profiles / • Single chip USB to up to 4 data ports / • Entire USB protocol handled on the chip. No USB specific / firmware programming…
- VBUS / CC1/CC2 / Port 1 / Port 2 / • GPIOs block is
- CC1/CC2 / Port 1 / Port 2 / • GPIOs block is / for PD control
- FT2232HP or / FT4232HP do / not include port 2 / \* For description of each / function please refer
- CODE PRODUCT NAME APPLICATION / INTERFACE CHANNELS POWER / DELIVERY PORT EEPROM DATA THROUGHPUT / (MAX) / PACKAGE
- UMFT232HPEV-S No EEPROM so sink is / only at 5V/3A / Single Type-C Two 15-pin, / single row header / FT233HP Single channel high speed
- serial bridging modes of / FT233HPQ / Single Type-C Two 20-pin, / single row header / Two 14-pin,
- Single Type-C Two 20-pin, / single row header / Two 14-pin, / 0.1” inch header / FT2232HP Dual channel high speed USB
- modes can also be / evaluated / Dual Type-C Two 26-pin, 0.1” dual- / row headers / FT4232HP Quad channel high speed
- modes can also be / evaluated / Quad Type-C Two 26-pin, 0.1” dual- / row headers / • Supports PD Specification 3.0
- Quad Type-C Two 26-pin, 0.1” dual- / row headers / • Supports PD Specification 3.0 / • Port 1 supports power role swap function while Port 2 supports / sink mode with charge through function to …
- row headers / • Supports PD Specification 3.0 / • Port 1 supports power role swap function while Port 2 supports / sink mode with charge through function to Port 1 / • Type-C/PD Physical Layer P…
- • Supports PD Specification 3.0 / • Port 1 supports power role swap function while Port 2 supports / sink mode with charge through function to Port 1 / • Type-C/PD Physical Layer Protocol implem…
- • PD policy engine implemented with PD mode configuration / through external EEPROM / • Up to 8 configurable PD GPIO pins support / • Highly integrated design includes +1.2V LDO regulator for / …
- • Smart camera / • Smart home controller / • Sweeping robot / • AI control (artificial intelligence) / • Defibrillator
- TYPICAL APPLICATIONS / HP SERIES (POWER DELIVERY) CHIP COMPARISON TABLE / FTDI Chip offers royalty free VCP (Virtual Com Port) and D2XX direct driver for Windows, Linux, Mac and Android (J2xx/D2…

### Specifications, ratings, and operating conditions

- protocol (USB to JTAG, I2C, SPI or bit-bang) design / • RS232/RS422/RS485 UART transfer data rate up to 12Mbaud / • Low operating USB suspend current / • Extended -40ºC to 85ºC industrial operat…
- Quad Type-C Two 26-pin, 0.1” dual- / row headers / • Supports PD Specification 3.0 / • Port 1 supports power role swap function while Port 2 supports / sink mode with charge through function to …
- • Configurable I/O drive strength (4,8,12 or 16mA) and slew rate / • +3.3V I/O interfacing which is also +5V tolerant / • +3.3V single supply operating voltage range / TECHNICAL SPECIFICATION / …
- • +3.3V I/O interfacing which is also +5V tolerant / • +3.3V single supply operating voltage range / TECHNICAL SPECIFICATION / • Sensor expansion (various sensors within the car, i.e. cameras, /…

### Dimensions, package, and mechanical information

- DELIVERY PORT EEPROM DATA THROUGHPUT / (MAX) / PACKAGE / PART NUMBER PACKAGE PACKING PRODUCT CODE NOTE CHANNELS USB / CONNECTOR I/O CONNECTOR
- (MAX) / PACKAGE / PART NUMBER PACKAGE PACKING PRODUCT CODE NOTE CHANNELS USB / CONNECTOR I/O CONNECTOR / FT232HP Single channel high speed

### Formulas, equations, and configurable calculations

- sink mode with charge through function to Port 1 / • Type-C/PD Physical Layer Protocol implemented / • PD policy engine implemented with PD mode configuration / through external EEPROM / • Up to…

### Reference designs, applications, and examples

- HP SERIES (POWER DELIVERY) CHIP PACKING INFORMATION DEVELOPMENT KIT / PRODUCT / CODE PRODUCT NAME APPLICATION / INTERFACE CHANNELS POWER / DELIVERY PORT EEPROM DATA THROUGHPUT
- • Defibrillator / • Medical X-Ray Machine / TYPICAL APPLICATIONS / HP SERIES (POWER DELIVERY) CHIP COMPARISON TABLE / FTDI Chip offers royalty free VCP (Virtual Com Port) and D2XX direct driver …
- ftdichip.com/drivers/ for the full driver support list including OS versions and legacy OS. / For installation guide, please visit our webpage at <https://ftdichip.com/document/installation-guid…>

## Page-by-Page Extracted Content

### Page 1

```text
FTDI Chip’s HP Series provides a two-in-one solution that seamlessly
integrates USB Type-C with enhanced power delivery and data
bridging. This unique feature allows higher power availability, either
at the connected Host PC to draw more power, or for the HP Series to
provide power to charge the Host PC.
Designed to eliminate the need for separate data bridge and PD ICs,
it offers efficient data transfer and the ability to power and connect
multiple peripherals through a single port, streamlining connectivity
and performance and improving power management for both host PC
charging and power sourcing.
* The HP Series is an enhanced series derived from the original H
Series, offering an upgrade path that adds USB Type-C support.
OVERVIEW
HP Family Series
Power Delivery Series
• Up to 2 x USB PD 3.0 Ports. One channel is for power and data
while the other channel is for power only
• Supports 5V3A, 9V3A, 12V3A, 15V3A, 20V3A and more power
profiles
• Single chip USB to up to 4 data ports
• Entire USB protocol handled on the chip. No USB specific
firmware programming required
• USB 2.0 High Speed (480Mbits/Second) and Full Speed
(12Mbits/second) compatible
• Two Multi-Protocol Synchronous Serial Engine (MPSSE)
on channel A and channel B, to simplify synchronous serial
protocol (USB to JTAG, I2C, SPI or bit-bang) design
• RS232/RS422/RS485 UART transfer data rate up to 12Mbaud
• Low operating USB suspend current
• Extended -40ºC to 85ºC industrial operating temperature range
KEY FEATURES
Figure 1: HP series
block diagram
LDO/CLK I2C GPIOs Config
PD1
PHY/Ctrl
PD policy
Engine
PD2
PHY/Ctrl
ADBUS
BDBUS
CDBUS
DDBUS
USB Protocol
engine
EEPROM
VBUS Power & FET Switches
USB HS
PHY
Type-C
connector
UART/
MPSSE
Type-C
connector
VBUS
CC1/CC2
D+/D-
VBUS
CC1/CC2
Port 1
Port 2
• GPIOs block is
for PD control
only
• FT232HP,
FT2232HP or
FT4232HP do
not include port 2
* For description of each
function please refer
the dedicated product
datasheet
NOTE:
```

### Page 2

```text
HP SERIES (POWER DELIVERY) CHIP PACKING INFORMATION DEVELOPMENT KIT
PRODUCT
CODE PRODUCT NAME APPLICATION
INTERFACE CHANNELS POWER
DELIVERY PORT EEPROM DATA THROUGHPUT
(MAX)
PACKAGE
PART NUMBER PACKAGE PACKING PRODUCT CODE NOTE CHANNELS USB
CONNECTOR I/O CONNECTOR
FT232HP Single channel high speed
USB bridge with Type-C/
PD3.0 Controller
UART
ASYNC FIFO
SYNC FIFO
MPSSE
ASYNC BIT BANG
SYNC BIT BANG
1 1 External 12MBaud
8MByte/s
40MByte/s
30Mbit/s
FT232HPQ-TRAY
FT232HPQ-REEL
56 QFN 260/tray
3,000/reel
UMFT232HPEV-S No EEPROM so sink is
only at 5V/3A
Single Type-C Two 15-pin,
single row header
FT233HP Single channel high speed
USB bridge with Type-C/
PD3.0 Controller
UART
ASYNC FIFO
SYNC FIFO
MPSSE
ASYNC BIT BANG
SYNC BIT BANG
1 2 External 12MBaud
8MByte/s
40MByte/s
30Mbit/s
FT233HPQ-TRAY
FT233HPQ-REEL
64 QFN 260/tray
3,000/reel
UMFT233HPEV-SD
UMFT233HPEV
Sink only but
configurable with
EEPROM
All FTDI Chip power
delivery feature and USB
serial bridging modes of
FT233HPQ
Single Type-C Two 20-pin,
single row header
Two 14-pin,
0.1” inch header
FT2232HP Dual channel high speed USB
bridge with Type-C/PD3.0
Controller
UART
ASYNC FIFO
SYNC FIFO
MPSSE x 2
ASYNC BIT BANG
SYNC BIT BANG
2 1 External 12MBaud
8MByte/s
40MByte/s
30Mbit/s
FT2232HPQ-TRAY
FT2232HPQ-REEL
68 QFN 260/tray
3,000/reel
Not available
FT2233HP Dual channel high speed USB
bridge with Type-C/PD3.0
Controller
UART
ASYNC FIFO
SYNC FIFO
MPSSE x 2
ASYNC BIT BANG
SYNC BIT BANG
2 2 External 12MBaud
8MByte/s
40MByte/s
30Mbit/s
FT2233HPQ-TRAY
FT2233HPQ-REEL
76 QFN 260/tray
3,000/reel
UMFT4233HPEV USB serial bridging
modes can also be
evaluated
Dual Type-C Two 26-pin, 0.1” dual-
row headers
FT4232HP Quad channel high speed
USB bridge with Type-C/
PD3.0 Controller
UART
MPSSE x 2
ASYNC BIT BANG
SYNC BIT BANG
4 1 External 12MBaud
30Mbit/s
FT4232HPQ-TRAY
FT4232HPQ-REEL
68 QFN 260/tray
3,000/reel
Not available
FT4233HP Quad channel high speed
USB bridge with Type-C/
PD3.0 Controller
UART
MPSSE x 2
ASYNC BIT BANG
SYNC BIT BANG
4 2 External 12MBaud
30Mbit/s
FT4233HPQ-TRAY
FT4233HPQ-REEL
76 QFN 260/tray
3,000/reel
UMFT4233HPEV USB serial bridging
modes can also be
evaluated
Quad Type-C Two 26-pin, 0.1” dual-
row headers
• Supports PD Specification 3.0
• Port 1 supports power role swap function while Port 2 supports
sink mode with charge through function to Port 1
• Type-C/PD Physical Layer Protocol implemented
• PD policy engine implemented with PD mode configuration
through external EEPROM
• Up to 8 configurable PD GPIO pins support
• Highly integrated design includes +1.2V LDO regulator for
VCORE, integrated POR function and on chip clock multiplier
PLL (12MHz – 480MHz)
• Configurable I/O drive strength (4,8,12 or 16mA) and slew rate
• +3.3V I/O interfacing which is also +5V tolerant
• +3.3V single supply operating voltage range
TECHNICAL SPECIFICATION
• Sensor expansion (various sensors within the car, i.e. cameras,
ultrasonic sensors, GPS fatigue detection etc)
• BLE expansion (Bluetooth low energy)
• T-Box (Telematics Box)
• Edge computing
• Game controller
• Monitor
• Smart camera
• Smart home controller
• Sweeping robot
• AI control (artificial intelligence)
• Defibrillator
• Medical X-Ray Machine
TYPICAL APPLICATIONS
HP SERIES (POWER DELIVERY) CHIP COMPARISON TABLE
FTDI Chip offers royalty free VCP (Virtual Com Port) and D2XX direct driver for Windows, Linux, Mac and Android (J2xx/D2xx only). Visit http://
ftdichip.com/drivers/ for the full driver support list including OS versions and legacy OS.
For installation guide, please visit our webpage at https://ftdichip.com/document/installation-guides/ for details on how to install the drivers.
Additional installation guides, application notes and technical note are also available.
```

### Page 3

```text
EUROPE, MIDDLE EAST , AFRICA
Future Technology Devices
International Limited
Unit 1, 2 Seaward Place,
Centurion Business Park,
Glasgow, G41 1HH,
United Kingdom
Tel: +44 (0) 141 429 2777
Email: sales1@ftdichip.com
AMERICAS
Future Technology Devices
International Limited (USA)
7130 SW Fir Loop Tigard,
OR97223-8160,
United States of America
Tel: +1 (503) 547-0988
Email: us.sales@ftdichip.com
CHINA
Future Technology Devices
International Limited (China)
Room 1103, No. 666
West Huaihai Road,
200052, Shanghai,
P .R. China
Tel: +86 (21) 62351596
Email: cn.sales@ftdichip.com
ASIA PACIFIC
Future Technology Devices
International Limited (Singapore)
1 Tai Seng Avenue,
Tower A #03-06,
Singapore 536464
Tel: +65 6841 1174
Email: tw.sales1@ftdichip.com
FTDI Chip and FTDI logo are registered trademarks of Future Technology Devices International Limited (FTDI Chip) incorporated in the United Kingdom, United States, Singapore and other
countries. All other trademarks mentioned herein are property of their respective companies. © 2025, FTDI Chip. All Rights Reserved.
04/2025 hp-family-factsheet
FTDI Chip develops innovative silicon solutions that enhance
interaction with the latest global technologies. Our primary objective
is to “bridge technologies” to empower engineers with sophisticated,
feature-rich, robust and easy-to-use product platforms. These
platforms enable creation of high-performance electronic designs with
minimal peripheral components, low power consumption, and efficient
use of board space.
FTDI Chip’s long-established, continuously expanding Universal
Serial Bus (USB) product line features universally recognized brands
ABOUT FTDI CHIP
such as the ubiquitous R-Chip, X-Chip, Hi-Speed, and SuperSpeed
USB 3.0 series.
FTDI Chip is a fabless semiconductor company, partnered with the
world’s leading foundries. Our headquarter is in Glasgow, UK and is
supported with research and development facilities in Glasgow, and
Singapore. We maintain a wide network of sales and technical support
in Glasgow, Tigard (Oregon, USA) and Shanghai (China).
For more information go to: www.ftdichip.com
```
