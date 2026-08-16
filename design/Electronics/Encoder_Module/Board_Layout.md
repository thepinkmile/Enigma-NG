# Encoder Module Board Layout Visualisations

**Status:** In Review
**Project:** Enigma-NG
**Author:** Izzyonstage & GitHub Copilot
**Version:** v.0.1.0
**Associated Hardware Revision:** Rev A
**Last Updated:** 2026-08-14

## 1. Component Areas

```text
TOP VIEW (L1) - 4-Layer / 2oz Copper
 __________________________________________________________________
|                                                                  |
|   [ J1 - 90-PIN plain-bits BtB PLUG ]  <--- Left edge            |
|                                                                  |
|   [ SINGLE CPLD + DIGITAL DEBOUNCE / ROLE LOGIC ]                |
|   (EPM570T100I5N + sampled encode/decode image implementation)   |
|                                                                  |
|   [ J2 - 24-PIN cypher-bits+JTAG BtB PLUG ] <--- Bottom-right    |
|   [ J3 - 10-PIN POWER BtB PLUG ]            <--- Top-right       |
|                                                                  |
|   [ DATA PLATE ] <--- Inverted White Silkscreen on L4            |
|__________________________________________________________________|
```

## 2. Simplified Layout

```text
____________________________________________________________
|                                                           |
|   [ J1 plain-bits ]     [ CPLD ]      [ J2 cypher-bits ]  |
|   (90-pin BtB plug)       (U1)      + JTAG (24-pin plug)  |
|                                        [ J3 power (10p) ] |
|___________________________________________________________|
```

## 1a. J1 - plain-bits Connector (DF40C-90DP-0.4V(51))

> **Connector Definition Owner:** this board (canonical ENC-module BtB pin-mapping reference).
> Mates with the carrier board's DF40C-90DS receptacle. Reused by the Cypher Board (J7/J10/J13/J16),
> Cypher-Input Board (J1), and the future Cypher-Output Board.

2 rows x 45 positions = 90 total pins. 64 plain-bit signal pins (PB) + 26 GND pins, zig-zag
distributed between rows (Bresenham-spread, max signal-only gap = 1 column between any two GND
columns). PB\[0\] is leftmost (LSB convention).

| Col | Row A | Row B |
| :--- | :--- | :--- |
| C01 | PB[0] | PB[1] |
| C02 | GND | PB[2] |
| C03 | PB[3] | GND |
| C04 | PB[4] | PB[5] |
| C05 | GND | PB[6] |
| C06 | PB[7] | PB[8] |
| C07 | PB[9] | GND |
| C08 | PB[10] | PB[11] |
| C09 | GND | PB[12] |
| C10 | PB[13] | GND |
| C11 | PB[14] | PB[15] |
| C12 | GND | PB[16] |
| C13 | PB[17] | PB[18] |
| C14 | PB[19] | GND |
| C15 | PB[20] | PB[21] |
| C16 | GND | PB[22] |
| C17 | PB[23] | GND |
| C18 | PB[24] | PB[25] |
| C19 | GND | PB[26] |
| C20 | PB[27] | PB[28] |
| C21 | PB[29] | GND |
| C22 | GND | PB[30] |
| C23 | PB[31] | PB[32] |
| C24 | PB[33] | GND |
| C25 | PB[34] | PB[35] |
| C26 | GND | PB[36] |
| C27 | PB[37] | PB[38] |
| C28 | PB[39] | GND |
| C29 | GND | PB[40] |
| C30 | PB[41] | PB[42] |
| C31 | PB[43] | GND |
| C32 | PB[44] | PB[45] |
| C33 | GND | PB[46] |
| C34 | PB[47] | PB[48] |
| C35 | PB[49] | GND |
| C36 | GND | PB[50] |
| C37 | PB[51] | PB[52] |
| C38 | PB[53] | GND |
| C39 | PB[54] | PB[55] |
| C40 | GND | PB[56] |
| C41 | PB[57] | PB[58] |
| C42 | PB[59] | GND |
| C43 | GND | PB[60] |
| C44 | PB[61] | PB[62] |
| C45 | PB[63] | GND |

> **plain-bits usage:** all 64 PB[] positions are generic; how a carrier board wires them (to
> keyswitches, lightboard lamps, or plugboard jack terminals) is defined entirely by the carrier
> board's own design files - see e.g. `Cypher-Input/Board_Layout.md §1`. On Cypher-Input, all 64
> positions are reserved exclusively for cipher-path keyswitches - LED colour selection is
> generated entirely on the carrier board itself and never touches this bus (see
> `Cypher-Input/Design_Spec.md §5`).

## 1b. J2 - cypher-bits + JTAG Connector (DF40C-24DP-0.4V(51))

> **Connector Definition Owner:** this board. Mates with the carrier board's DF40C-24DS receptacle.

2 rows x 12 positions = 24 total pins. 12 signal pins + 12 GND pins, full zig-zag (every signal
flanked by GND at adjacent columns). Signal order left-to-right: CB[0:5], then JTAG (TCK, RST_N,
TMS, TDI, TDO), then `ENC_ACTIVE_N`.

| Col | Row A | Row B |
| :--- | :--- | :--- |
| C01 | CB[0] | GND |
| C02 | GND | CB[1] |
| C03 | CB[2] | GND |
| C04 | GND | CB[3] |
| C05 | CB[4] | GND |
| C06 | GND | CB[5] |
| C07 | TCK | GND |
| C08 | GND | RST_N (`CPLD_RESET_N`) |
| C09 | TMS | GND |
| C10 | GND | TDI |
| C11 | TDO | GND |
| C12 | GND | ENC_ACTIVE_N |

> **This board's usage:** all 12 signals active. `ENC_ACTIVE_N` direction is role-dependent
> (`KBD_ENC` drives it, `LBD_DEC` consumes it, other roles hold it inactive/HIGH) - see
> `Design_Spec.md §3`. `BRIGHTNESS_PWM` (an external 555 oscillator on the carrier board, where
> applicable) feeds the CPLD GCLK0 pin - a dedicated clock input, not part of this 24-pin
> signal/JTAG connector.

## 1c. J3 - Power Connector (DF40C-10DP-0.4V(51))

> **Connector Definition Owner:** this board. Mates with the carrier board's DF40C-10DS receptacle.

2 rows x 5 positions = 10 total pins. Power only, no zig-zag (solid rows). Row A = 3V3_ENIG,
Row B = GND.

| Col | Row A | Row B |
| :--- | :--- | :--- |
| C01 | 3V3_ENIG | GND |
| C02 | 3V3_ENIG | GND |
| C03 | 3V3_ENIG | GND |
| C04 | 3V3_ENIG | GND |
| C05 | 3V3_ENIG | GND |

> **Pin-1 marker (per GRS §7.1):** J1/J2/J3 pin 1 shall each be identified by a triangular
> silkscreen marker adjacent to the pin-1 corner on L1 per
> `design/Standards/Global_Routing_Spec.md §7.1`.

**Power capacity:** 5 x 3V3_ENIG pins x 1 A/pin = 5.0 A. One Encoder Module estimated load ~104 mA
(1x EPM570 CPLD + 1x status LED + local margin) - substantial connector margin.

---

## 4. U1 - Encoder CPLD Signal Map (Logical Pin Budget)

> This is the board-authoritative **logical** signal map for U1. The local MAX II handbook confirms
> `EPM570T100` package availability in TQFP-100, but it points printed device pin-outs to external
> package documentation rather than embedding a fixed package pin table. The map below therefore
> freezes the required board-level connectivity while leaving the exact TQFP pad numbers to schematic
> capture.
>
> Detailed role logic, sampled debounce requirements, and encoder/decoder behaviour are owned by
> `design/Software/CPLD_Logic/Encoder_Logic.md`.

### 4.1 Dedicated device pins

| Function | Source / destination | Notes |
| :--- | :--- | :--- |
| `TCK` | J2 C07 (Row A) -> U1 | Dedicated JTAG clock input |
| `TMS` | J2 C09 (Row A) -> U1 | Dedicated JTAG mode input |
| `TDI` | J2 C10 (Row B) -> U1 | Dedicated JTAG serial input from the carrier board's JTAG chain |
| `TDO` | U1 -> R6 -> J2 C11 (Row A) | Dedicated JTAG serial output back to the carrier board's JTAG chain |
| `DEV_CLR_N` / reset input | J2 C08 (Row B, `RST_N`/`CPLD_RESET_N`) -> U1 | Active-low device reset; held high locally by R5 (vendor pin name `DEV_CLRN` - see `design/Standards/Global_Routing_Spec.md §10`) |

### 4.2 General-purpose signal groups

| Signal group | Pins | U1 direction | Notes |
| :--- | :---: | :--- | :--- |
| `J1` PB[0:63] plain-bits bank | 64 | Role-dependent | Encode-role population reads one asserted line; decode-role population drives one-of-64 output |
| `J2` CB[0:5] cypher-bits | 6 | Role-dependent | Encode role drives the 6-bit bus back to the carrier board; decode role consumes it |
| `ENC_ACTIVE_N` | 1 | Role-dependent | `KBD_ENC` drives keyboard activity LOW when a debounced key is active; `LBD_DEC` consumes it to blank outputs when idle; other roles keep it inactive |
| `D1` status LED | 1 | Output | Active-low debug LED: U1 drives LOW to illuminate |

**Logical budget summary:** 72 general-purpose signal connections total = **64 bank lines + 6 bus
lines + 1 activity sideband + 1 LED**, plus the dedicated JTAG / reset pins above.

**Spare-pin policy:** the active docs do not currently claim any spare U1 user I/O.

---

## 5. Routing - Trace Width Specifications

**Board specs:** 4-layer / 2oz finished copper — stackup per GRS §2.3.1.  
L1 = signal (JTAG/routing); L2 = GND plane; L3 = 3V3_ENIG power pour; L4 = secondary routing /
data plate.

**IPC-2221A basis (2oz copper, external, 10°C rise, 25°C ambient):**  
For 2oz external: ~0.15 mm/A. The 3V3_ENIG inner pour (L3) handles board load without width
constraints. See `Global_Routing_Spec.md §1.1` for the full current-category table.

**Encoder Module current budget:**  
1x EPM570T100I5N CPLD @ 50 mA; 1x status LED @ 4 mA; misc = ~50 mA; total worst-case:
**104 mA** from the 3V3_ENIG rail supplied via J3.

### 5.1 Trace Width Table

| Net | Peak Current | IPC Calc (2oz ext) | Design Min | **Specified Width** | Layer | Notes |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Signal (`plain-bits`, `cypher-bits`) | < 5 mA | < 0.001 mm | per GRS §1.1 | **per GRS §1.1** | L1 | 3.3 V logic; CPLD I/O; J1/J2 traces |
| JTAG signals: TCK, TMS, TDI, TDO (CI) | signal | - | per GRS §2.3.1 | **per GRS §2.3.1 / JLCPCB_Manufacturing.md §1.1** | L1 (external) | 50 Ω controlled impedance over L2 GND plane; per DEC-016 |
| 3V3_ENIG power (J3 -> CPLD + LED) | 104 mA | 0.016 mm | per GRS §1.1 | **per GRS §1.1** | L1 + L3 pour | Canonical 3V3_ENIG width per GRS §1.1 |
| 3V3_ENIG distribution (inner power pour) | 104 mA | - | pour | **copper pour** | L3 | Full uninterrupted 2oz plane |
| GND return (inner GND pour) | - | - | pour | **copper pour** | L2 | Reference plane under all CI traces on L1 |

### 5.2 Notes

* **JTAG CI traces:** 50 Ω controlled impedance on L1 over the L2 GND plane. Trace width per GRS §2.3.1 and `design/Production/JLCPCB_Manufacturing.md §1.1`.
* **Cable-output trace (U1 TDO -> R6 -> J2 C11):** R6 (75 Ω) is placed within 2 mm of U1 TDO;
  the post-R6 trace to the J2 connector pad should be kept short.
* **3V3_ENIG power entry (J3, all 5 Row A pins):** power pins connect to the same L3 copper pour
  via thermal vias; L1 traces from J3 to the via entry points per GRS §1.1.

