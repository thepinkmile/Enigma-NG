# Actuation Module (AM) Design Specification

**Status:** Draft
**Project:** Enigma-NG
**Author:** Izzyonstage & GitHub Copilot
**Version:** v.0.1.0
**Associated Hardware Revision:** Rev A
**Last Updated:** 2026-04-26

## 1. Overview

The **Actuation Module (AM)** is a small shared service PCB used anywhere Enigma-NG needs one local
servo-driven single-step actuation cycle without continuous CM5 supervision. The same AM is fitted:

* once on the **Controller** to actuate the main depression bar for virtual keypress injection
* once on each **Extension** to regenerate a group-boundary carry event into a local single-step
  actuation of the next 5-rotor group

The host board only provides power and a single active-low `ACTUATE_REQUEST` line. The AM owns the
power-up homing sequence, request latching / one-shot behaviour, servo PWM generation, and local LED
diagnostics.

## 2. Functional & Design Requirements

### Functional Requirements

| ID | Functional Requirement | Notes | Satisfied By / Cross-Ref |
| :--- | :--- | :--- | :--- |
| FR-AM-01 | Accept a local power feed from a host board | Host provides `5V_MAIN`, `3V3_ENIG`, and multiple `GND` returns | §3 Connectivity; BOM J1 |
| FR-AM-02 | Accept a single active-low `ACTUATE_REQUEST` input from the host board | Same electrical contract works for a CM5-driven request on the Controller and a switch-derived request on an Extension | §3 Connectivity; BOM J2 |
| FR-AM-03 | Auto-home the local servo on power-up without host feedback wires | Host waits a fixed startup window; AM shows local LED state only | §4 Local control behaviour; BOM J4, D1-D3 |
| FR-AM-04 | Convert each valid request into exactly one complete servo cycle | Held request inputs must not retrigger until the current cycle completes and the input has released | §4 Local control behaviour; BOM U1 |
| FR-AM-05 | Drive one external hobby servo through a local loom connection | Servo is mechanically mounted near the actuation bar, not on the AM PCB | §3 Connectivity; BOM J3 |
| FR-AM-06 | Monitor a local home switch through a separate loom connection | Home switch is physically mounted near the mechanism and wired back to the AM | §3 Connectivity; BOM J4 |
| FR-AM-07 | Provide local diagnostic indication without any host-side status return pins | `PWR`, `HOMED`, and `ACT` LEDs are sufficient for bench and service diagnostics and shall remain visible from the AM board edge during maintenance | BOM D1-D3, R1-R3 |
| FR-AM-08 | Provide a dedicated local SWD programming / service header on the AM itself | Required so the STM32 can always be programmed and debugged before first use without depending on the host board | §3.5; BOM J5 |
| FR-AM-09 | Provide a dedicated local UART bootloader / service header on the AM itself | Keep a second programming path available for ad-hoc USB-to-UART use, with explicit boot-entry control exposed on the header pinout | §3.6; BOM J6 |
| FR-AM-10 | Provide a local momentary reset control next to the UART service header | Required so the UART bootloader path can be entered without awkward clip leads on `NRST` | §3.7; BOM SW1 |
| FR-AM-11 | Provide a local momentary `BOOT0` control next to the UART service header | Required so the UART bootloader path can be entered directly at the AM without needing a temporary jumper on the header | §3.8; BOM SW2 |

### Design Requirements

| ID | Design Requirement | Specification | Satisfied By / Cross-Ref |
| :--- | :--- | :--- | :--- |
| DR-AM-01 | PCB stackup | 4-layer, 2oz finished copper (JLC04161H-7628) | `Board_Layout.md` |
| DR-AM-02 | Host power dock | J1 = Samtec ERM8-005-05.0-S-DV-K-TR (module-side male); host uses matching ERF8-005 socket | §3.1; BOM J1 |
| DR-AM-03 | Host trigger dock | J2 = Samtec ERM8-005-05.0-S-DV-K-TR (module-side male); host uses matching ERF8-005 socket | §3.2; BOM J2 |
| DR-AM-04 | Servo loom header | J3 = Adam Tech PH1-05-UA, manually fitted post-PCBA; only pins 1-3 are active in Rev A | §3.3; BOM J3 |
| DR-AM-05 | Home-switch loom header | J4 = Adam Tech PH1-05-UA, manually fitted post-PCBA; twisted-pair wiring required for the active signal and return | §3.4; BOM J4 |
| DR-AM-06 | Local controller architecture | U1 shall be a small 3.3V local controller with native hardware PWM, at least 2 digital inputs, at least 4 spare / LED-capable GPIOs, power-on reset, and a package suitable for low-profile service-module assembly | §4; BOM U1 |
| DR-AM-07 | Diagnostics LED parts and placement | Reuse the existing green 0402 status LED and 330Ω 0402 resistor already used on Encoder boards, but place the LED footprints at the visible board edge on the PCBA side so their light remains observable when the AM is installed upside-down | BOM D1-D3, R1-R3; `Board_Layout.md` |
| DR-AM-08 | Home-input biasing | `ACTUATION_HOME` uses a local 10kΩ pull-up to `3V3_ENIG` plus a 100nF local RC debounce capacitor | BOM R4, C1 |
| DR-AM-09 | Mounting orientation | Module is intended to mount upside-down from the host board, similar to the JDB service-board approach | `Board_Layout.md` |
| DR-AM-10 | SWD service connector | J5 = Adam Tech PH1-05-UA, manually fitted 1x5 2.54mm SWD header using the common compact 5-pin STM32/ST-LINK flying-lead order (`VTref`, `SWCLK`, `GND`, `SWDIO`, `NRST`) | §3.5; BOM J5 |
| DR-AM-11 | Inter-board component envelope | All PCBA-fitted parts on the enclosed connector-facing side of the AM shall remain low profile and shall not exceed 2.0 mm installed height above the PCB; all manual-fit loom / service headers remain on the opposite side | `Board_Layout.md`; §4 |
| DR-AM-12 | UART bootloader connector | J6 = Adam Tech PH1-05-UA, manually fitted 1x5 2.54mm UART bootloader header; pins 1-4 shall follow the common 3.3V TTL serial order (`GND`, `3V3`, `TX`, `RX`) and pin 5 shall expose `BOOT0` | §3.6; BOM J6 |
| DR-AM-13 | Local reset button | SW1 = Omron B3F-1070 or equivalent SPST NO through-hole tactile switch, wired to pull `NRST` low momentarily and placed adjacent to J6 for convenient UART bootloader entry | §3.7; BOM SW1 |
| DR-AM-14 | Local `BOOT0` button | SW2 = Omron B3F-1070 or equivalent SPST NO through-hole tactile switch, wired to assert `BOOT0` HIGH while pressed and placed adjacent to J6 / SW1 for convenient UART bootloader entry | §3.8; BOM SW2 |
| DR-AM-15 | Local decoupling and reservoir caps | AM is exempt from the full 5x bulk-entry-bank rule used on larger boards, but it shall still include local STM32 supply decoupling plus compact 3V3/5V reservoir caps: C2-C3 = 100nF X7R 0402 at the STM32 supply domains, C4 = 4.7uF X7R on `3V3_ENIG`, C5 = 10uF X7R on `5V_MAIN` near the servo/power entry region | §4; BOM C2-C5; `Board_Layout.md` |

## 3. Connectivity

### 3.1 J1 - Host Power Dock

**Module-side part:** Samtec **ERM8-005-05.0-S-DV-K-TR** (male, 2x5, 0.8mm pitch)  
**Host-side mating part:** Samtec **ERF8-005-05.0-S-DV-K-TR** (female, 2x5, 0.8mm pitch)

| Pin | Signal | Direction | Notes |
| :--- | :--- | :--- | :--- |
| 1 | 5V_MAIN | Host -> AM | Servo rail |
| 2 | GND | — | Return |
| 3 | 5V_MAIN | Host -> AM | Additional current path |
| 4 | GND | — | Return |
| 5 | 3V3_ENIG | Host -> AM | Logic rail |
| 6 | GND | — | Logic return |
| 7 | 5V_MAIN | Host -> AM | Additional current path |
| 8 | GND | — | Return |
| 9 | 5V_MAIN | Host -> AM | Additional current path |
| 10 | GND | — | Return |

### 3.2 J2 - Host Trigger Dock

**Module-side part:** Samtec **ERM8-005-05.0-S-DV-K-TR** (male, 2x5, 0.8mm pitch)  
**Host-side mating part:** Samtec **ERF8-005-05.0-S-DV-K-TR** (female, 2x5, 0.8mm pitch)

`ACTUATE_REQUEST` is **active-low**. The AM provides the local biasing; the host asserts a request by
pulling the line LOW.

| Pin | Signal | Direction | Notes |
| :--- | :--- | :--- | :--- |
| 1 | GND | — | Return / guard |
| 2 | ACTUATE_REQUEST | Host -> AM | Active-low request input |
| 3 | GND | — | Return / guard |
| 4 | GND | — | Reserved as guard |
| 5 | GND | — | Reserved as guard |
| 6 | GND | — | Reserved as guard |
| 7 | GND | — | Reserved as guard |
| 8 | GND | — | Reserved as guard |
| 9 | GND | — | Reserved as guard |
| 10 | GND | — | Reserved as guard |

### 3.3 J3 - Servo Loom Header

**Part:** Adam Tech **PH1-05-UA** - 1x5 2.54mm male pin header, manually fitted after PCB assembly.

| Pin | Signal | Notes |
| :--- | :--- | :--- |
| 1 | 5V_MAIN | Servo supply |
| 2 | GND | Servo return |
| 3 | SERVO_PWM | AM-generated local PWM |
| 4 | NC | Reserved |
| 5 | NC | Reserved |

### 3.4 J4 - Home Switch Loom Header

**Part:** Adam Tech **PH1-05-UA** - 1x5 2.54mm male pin header, manually fitted after PCB assembly.

| Pin | Signal | Notes |
| :--- | :--- | :--- |
| 1 | ACTUATION_HOME | Active-low home-switch input |
| 2 | GND | Twisted-pair return with pin 1 |
| 3 | GND | Spare return |
| 4 | NC | Reserved |
| 5 | NC | Reserved |

### 3.5 J5 - SWD Programming / Service Header

**Part:** Adam Tech **PH1-05-UA** - 1x5 2.54mm male pin header, manually fitted for firmware loading
and bench-service access.

This is the primary programming and debug header for the selected STM32. It uses the common compact
5-pin SWD flying-lead order so an ST-LINK, J-Link, or similar SWD probe can be adapted without
inventing a board-specific pin order.

| Pin | Signal | Notes |
| :--- | :--- | :--- |
| 1 | 3V3_ENIG | Target reference / programming rail |
| 2 | SWCLK | SWD clock |
| 3 | GND | Reference |
| 4 | SWDIO | SWD data I/O |
| 5 | NRST | Target reset |

### 3.6 J6 - UART Bootloader / Service Header

**Part:** Adam Tech **PH1-05-UA** - 1x5 2.54mm male pin header, manually fitted for bench-service
UART access and optional STM32 ROM-bootloader programming.

Pins 1-4 keep the common 3.3V TTL serial order so a simple ad-hoc UART harness can be made easily.
Pin 5 exposes `BOOT0` so the ROM bootloader can still be selected from an external harness when needed.
At the board itself, the AM also provides local tactile buttons for both `NRST` and `BOOT0`. In use,
`BOOT0` is treated as a **momentary operator action with a timing constraint**: hold it active while
reset occurs, then release it after the boot-mode sample point. To make that practical on the bench,
the AM provides a local reset button at SW1 and a local `BOOT0` button at SW2.

| Pin | Signal | Notes |
| :--- | :--- | :--- |
| 1 | GND | Reference |
| 2 | 3V3_ENIG | Target reference / logic rail |
| 3 | UART_TX | AM -> external UART adapter |
| 4 | UART_RX | External UART adapter -> AM |
| 5 | BOOT0 | Assert HIGH during reset to enter the STM32 ROM bootloader |

### 3.7 SW1 - Local Reset Button

**Part:** Omron **B3F-1070** - SPST NO through-hole tactile switch.

SW1 provides a local momentary reset by pulling `NRST` LOW while pressed. Place it next to J6 so the
normal UART bootloader sequence is straightforward:

1. Hold `BOOT0` HIGH on J6 pin 5.
2. Press and release SW1 to reset the STM32.
3. Release `BOOT0` after reset if desired; the MCU will stay in the ROM bootloader until power is
   cycled or the next reset occurs with `BOOT0` LOW.

### 3.8 SW2 - Local `BOOT0` Button

**Part:** Omron **B3F-1070** - SPST NO through-hole tactile switch.

SW2 provides a local momentary `BOOT0` assertion by driving `BOOT0` HIGH while pressed. Place it beside
SW1 so the two-button UART bootloader action is simple and repeatable:

1. Press and hold SW2.
2. Press and release SW1.
3. Release SW2.

This gives the same effect as holding `BOOT0` HIGH on J6 pin 5 during reset, but without needing a
temporary jumper or second hand on the header itself.

## 4. Local Control Behaviour

The AM is intentionally **host-light** and **mechanically local**:

1. Firmware is loaded via J5 (SWD) or, when needed, via J6 plus the local SW1 / SW2 button pair before
   the module is placed into service.
2. On power-up, U1 boots from local non-volatile memory and performs a homing sequence using the
   external home switch on J4.
3. Until homing completes, further actuation requests are ignored.
4. Once homed, each valid low-going `ACTUATE_REQUEST` event is latched and converted into one complete
   servo cycle.
5. A held request input must not cause repeated cycles; the request must release before the next cycle
   can be accepted.
6. The host receives no `BUSY`, `HOMED`, or fault wire. Service state is indicated only by the local
   LEDs.

### Local supply-decoupling note

The AM should follow a **small daughterboard decoupling strategy**, not the full bulk-entry-bank pattern
used by larger mainline boards. The closest precedent is the JTAG Daughterboard (JDB), which is
explicitly exempt from the 5x bulk-entry-bank rule and instead uses per-IC 100nF decoupling plus a
single 4.7uF entry filter.

The AM should follow the same general daughterboard logic, but with one important addition: unlike the
JDB, the AM drives a local servo load from `5V_MAIN`, so it should include a **local 5V reservoir cap**
as well as MCU decoupling. Rev A therefore requires:

* **C2-C3:** 100nF X7R 0402 local decoupling at the STM32 supply domains
* **C4:** 4.7uF X7R local `3V3_ENIG` reservoir / entry filter
* **C5:** 10uF X7R local `5V_MAIN` reservoir near the servo power path

This does **not** replace the host board's upstream bulk decoupling. It is local high-frequency
decoupling and short-burst current support for the AM itself.

### Preferred controller-part requirement

The selected U1 is **STMicroelectronics STM32G071K8T3TR**. This is a 32-pin 3.3V STM32G071 device
with native timer/PWM resources and enough GPIO margin for the AM's homing input, request input,
diagnostic LEDs, and service/programming access. A standalone PWM driver such as the PCA9685 remains a
reviewed part in the repository, but it is **not sufficient on its own** for the AM because the module
also needs autonomous homing, request latching, and cycle sequencing.
The selected STM32 also keeps both requested service paths practical: J5 carries the normal SWD debug
interface, while J6 plus the local SW1 / SW2 button pair exposes a simple UART/`BOOT0` path for
ROM-bootloader use with ad-hoc wiring.
The reviewed STM32 family reference is
[`design/Datasheets/stm32g071.md`](../../Datasheets/stm32g071.md), which links back to the preserved
vendor PDF at `design/Datasheets/stm32g071.pdf`.

Approved supplier references for the selected AM controller are:

* DigiKey: `497-STM32G071K8T3TR-ND`
* Mouser: `511-STM32G071K8T3TR`
* JLCPCB: global sourcing or consignment only

The Mouser product page is also useful during later PCB work because it provides footprint and 3D-model
links for the selected package.

## 5. Software / Firmware Cross-Reference

The AM firmware specification now lives under the software tree at
[`design/Software/Actuation_Module/Design_Spec.md`](../../Software/Actuation_Module/Design_Spec.md).

That software document is the source of truth for:

* the SWD and UART boot / programming paths
* the SW1 / SW2 UART bootloader button sequence
* the STM32 firmware state machine
* homing, actuation, and fault behavior
* firmware bring-up order and implementation notes

This hardware design spec remains the source of truth for the AM's electrical interface, connector
pinouts, mechanical constraints, and BOM.

## 6. Bill of Materials

| Ref | Component | Value | Package | Mouser Part # | DigiKey Part # | JLCPCB Part # |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| C1 | Home-input debounce capacitor | 100nF X7R 50V | 0402 | 187-CL05B104KB5NNNC | 1276-1009-1-ND | C1525 |
| C2-C3 | STM32 local supply decoupling | 100nF X7R 50V | 0402 | 187-CL05B104KB5NNNC | 1276-1009-1-ND | C1525 |
| C4 | `3V3_ENIG` local reservoir / entry filter | 4.7uF X7R (CGA6P3X7R1H475K250AD) | 1210 | 810-CGA6P3X7R1H475KD | 445-10040-1-ND | C3877549 |
| C5 | `5V_MAIN` local reservoir near servo power path | 10uF X7R 50V | 1206 | 187-CL31B106KBHNNNE | 1276-6767-1-ND | C89632 |
| D1-D3 | Local diagnostic LEDs (`PWR`, `HOMED`, `ACT`) | Wurth 150060VS75000 — Green SMD LED | 0402 | 710-150060VS75000 | 732-4980-1-ND | C6848499 |
| J1 | Host power dock (module side) | Samtec ERM8-005-05.0-S-DV-K-TR | SMT 0.8mm pitch | 200-ERM8005050SDVKTR | 612-ERM8-005-05.0-S-DV-K-TRCT-ND | C3649741 |
| J2 | Host trigger dock (module side) | Samtec ERM8-005-05.0-S-DV-K-TR | SMT 0.8mm pitch | 200-ERM8005050SDVKTR | 612-ERM8-005-05.0-S-DV-K-TRCT-ND | C3649741 |
| J3 | Servo loom header - manual fit | Adam Tech PH1-05-UA — 1x5 2.54mm male header | THT | 737-PH1-05-UA | 2057-PH1-05-UA-ND | C5374051 |
| J4 | Home-switch loom header - manual fit | Adam Tech PH1-05-UA — 1x5 2.54mm male header | THT | 737-PH1-05-UA | 2057-PH1-05-UA-ND | C5374051 |
| J5 | SWD programming / service header - manual fit | Adam Tech PH1-05-UA — 1x5 2.54mm male header | THT | 737-PH1-05-UA | 2057-PH1-05-UA-ND | C5374051 |
| J6 | UART bootloader / service header - manual fit | Adam Tech PH1-05-UA — 1x5 2.54mm male header | THT | 737-PH1-05-UA | 2057-PH1-05-UA-ND | C5374051 |
| SW1 | Local reset pushbutton | Omron B3F-1070 — SPST NO through-hole tactile switch | THT tactile | 653-B3F-1070 | SW406-ND | C726011 |
| SW2 | Local `BOOT0` pushbutton | Omron B3F-1070 — SPST NO through-hole tactile switch | THT tactile | 653-B3F-1070 | SW406-ND | C726011 |
| R1-R3 | LED current-limit resistors | 330Ω 1% | 0402 | 667-ERJ-2RKF3300X | P330LCT-ND | C278592 |
| R4 | Home-input pull-up resistor | 10kΩ 1% | 0402 | 667-ERJ-2RKF1002X | P10.0KLCT-ND | C191123 |
| U1 | Local actuation controller | STMicroelectronics STM32G071K8T3TR | LQFP32 | 511-STM32G071K8T3TR | 497-STM32G071K8T3TR-ND | Global sourcing / consignment only |

The servo motor and the home switch are off-board electromechanical items and are therefore specified
by the host mechanical assembly rather than as AM PCB-fitted BOM rows.
