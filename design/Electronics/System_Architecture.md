# Enigma-NG System Architecture

**Status:** Draft
**Project:** Enigma-NG
**Author:** Izzyonstage & GitHub Copilot
**Version:** v1.0.0
**Associated Hardware Revision:** Rev A
**Last Updated:** 2026-04-05

---

## 1. Board Hierarchy and Physical Structure

The Enigma-NG system comprises the following boards:

- **Controller Board (CM5)** — Raspberry Pi CM5 carrier; hosts the Linux SoC and manages JTAG, GPIO and
  Ethernet.
- **Power Module** — Generates 5V_MAIN and 3V3_ENIG rails from ~12V input; connects to Controller via
  Link-Alpha.
- **Stator** — Central backplane; the first fixed stage of the cipher path. Connects to all other boards.
- **Rotors (×30)** — Arranged in groups of 5, chaining directly output-to-input. An Extension Board sits
  between each group of 5 to re-buffer broadcast signals.
- **Extension Board (up to ×5 within Rev A power budget)** — Bridges between rotor groups;
  re-buffers TCK and TMS. Minimum configuration: Stator → [5 Rotors] → Reflector (0 Extensions,
  5 rotors). Full build: 6 groups of 5 rotors separated by 5 Extension boards, terminated by the
  Reflector (30 rotors total). The 30-rotor / 5-extension limit is a power budget constraint, not a
  physical or architectural limit — the design is theoretically scalable beyond 30 rotors in groups
  of 5 with increased power supply capacity. Rev A prototype validates with 1 Extension board
  (10 rotors). Formula: Extensions = (Rotor groups) − 1; minimum 0, maximum 5 for current budget.
- **Reflector** — End of the rotor chain (after Rotor 30); performs the cipher reversal redirect and
  routes TTD_RETURN back to the Stator.
- **Encoder Boards (×3)** — 1 HID board (keyboard + lightboard), 2 Plugboard encoder boards. Connect to
  Stator J4–J6.
- **JTAG Daughterboard** — USB Blaster II implementation for programming CPLDs.

### Physical Chain

```text
Power Module ←—Link-Alpha (80-pin ERM8)—→ Controller Board
                                               |
                                          Link-Beta (40-pin ERM8)
                                               |
                                            Stator
                                         /    |    \
                              J1–J3    J4–J6   J7
                               |         |      |
                            Rotor 1  Encoders  Extension/Reflector port
                               ·
                            Rotor 5
                               |
                         Extension Board 1   ← (up to 5 Extension boards; each adds one 5-rotor group)
                               |
                            Rotor 6
                               ·
                            Rotor 10
                               |
                         Extension Board 2
                               |
                            Rotor 11
                               ·
                            Rotor 15
                               |
                         Extension Board 3
                               |
                            Rotor 16
                               ·
                            Rotor 20
                               |
                         Extension Board 4
                               |
                            Rotor 21
                               ·
                            Rotor 25
                               |
                         Extension Board 5
                               |
                            Rotor 26
                               ·
                            Rotor 30
                               |
                           Reflector
                               |
                     TTD_RETURN → Stator J7 pin 15
```

> **NOTE — Scalability:** The diagram shows the full 30-rotor / 5-extension configuration
> (maximum within the Rev A power budget). The architecture is theoretically unbounded;
> 30 rotors is a power budget ceiling, not a physical or architectural limit. Minimum
> configuration is Stator → [5 Rotors] → Reflector (0 Extensions). Rev A prototype
> validates with 1 Extension board (10 rotors total).

The Stator is the central backplane:

- Connects to the Controller Board via **Link-Beta** (J8, ERM8-020 40-pin male, 0.8mm pitch).
- Connects to the first Rotor via **J1–J3** (ERF8-005/010 female sockets receive Rotor 1 J1–J3 ERM8
  male).
- Connects to the Extension chain / Reflector via **J7** (16-pin Molex 2.54mm).

Rotors chain directly: Rotor N output (J4–J6 ERF8 female) receives Rotor N+1 input (J1–J3 ERM8 male).
Extension boards bridge between groups of 5 rotors. The Reflector sits at the end of the chain
(Rotor 30 J4–J6 → Reflector J1–J3).

---

## 2. Connector Architecture

All rotor-stack interconnects use the **Samtec Edge-Rate series** 0.8mm pitch board-to-board connectors:

- **ERM8** — male header (originating / input side of a connection).
- **ERF8** — female socket (receiving / output side of a connection).

The convention is: the **input side** of a board carries ERM8 male headers that plug into the ERF8 female
sockets on the **output side** of the previous board.

### Per-Board Connector Assignments

| Board | Input-side connectors | Output-side connectors |
| :--- | :--- | :--- |
| Rotor | J1 ERM8-005, J2 ERM8-005, J3 ERM8-010 (male) | J4 ERF8-005, J5 ERF8-005, J6 ERF8-010 (female) |
| Stator | — (Stator is the chain origin) | J1 ERF8-005, J2 ERF8-005, J3 ERF8-010 (female, receives Rotor 1) |
| Extension | J1 ERM8-005, J2 ERM8-005, J3 ERM8-010 (male, plugs into prev group last Rotor J4–J6) | J4 ERF8-005, J5 ERF8-005, J6 ERF8-010 (female, receives next group Rotor 1) |
| Reflector | J1 ERM8-005, J2 ERM8-005, J3 ERM8-010 (male, plugs into Rotor 30 J4–J6) | J4 16-pin Molex (TTD_RETURN back to Stator J7) |

---

## 3. Power Architecture

The Power Module generates two rails from a ~12V input source:

- **5V_MAIN** — Up to 12A; dual-phase interleaved **LMQ61460-Q1**. Powers the CM5 module. The CM5 requires up
  to 25W (5V @ 5A); the Linux kernel logs undervoltage warnings if supply capacity is below this.
- **3V3_ENIG** — Clean 3.3V; **TPS7A8333P** LDO post-regulator. Unified logic rail for all CPLDs, USB-JTAG
  interface, I2C logic, status indicators, and the full rotor stack.

> **NOTE (DEC-001):** The **3V3_SYSTEM** rail name is retired. **3V3_ENIG** is the single unified 3.3V
> rail throughout the system.

### 3V3_ENIG Power Flow

```text
Power Module (TPS7A8333P LDO)
  → Controller Board (via Link-Alpha pins 39–44)
    → Stator (via Link-Beta)
      → Rotor 1 J2 (PWR input)
        → Rotor 1 J5 (PWR output) → Rotor 2 J2 (PWR input)
          → ... [all 30 rotors chained via J2/J5]
            → Rotor 30 J5 → Reflector J2
```

---

## 4. JTAG Serial Chain (TTD Net)

> **This is the most critical architectural note regarding JTAG topology.**

### TTD Net Name

The JTAG serial chain data pin is designated **TTD** (JTAG Transmission Data) at **pin 6** on all JTAG
connectors (J1 and J4 on rotors). This unified name avoids TDI/TDO direction confusion:

- On the **input side** (J1 pin 6): TTD carries incoming TDI from the previous stage.
- On the **output side** (J4 pin 6): TTD carries outgoing TDO to the next stage's TDI.

### Serial Chain Path (Stator → Reflector → TTD_RETURN)

```text
Stator J1 pin 6 (TTD/TDI out)
  → Rotor 1 J1 pin 6 (TTD/TDI in)
  → [Rotor 1 CPLD processes]
  → Rotor 1 J4 pin 6 (TTD/TDO out) [via R1 75Ω series termination]
  → Rotor 2 J1 pin 6 (TTD/TDI in)
  → ... [repeat for all 30 rotors]
  → Rotor 30 J4 pin 6 (TTD/TDO out)
  → Reflector J1 pin 6 (TTD in) → [R1 22Ω termination]
  → Reflector J4 pin 15 (TTD_RETURN)
  → Stator J7 pin 15 (TTD_RETURN arrives back)
```

### TCK and TMS — Broadcast Signals

**TCK** and **TMS** are broadcast signals. They travel from Stator J1 pins 2 and 4 down the entire rotor
chain **in parallel** (not daisy-chained). Every rotor receives the same TCK and TMS simultaneously.

### TTD_RETURN Path

The JTAG TDO return does **not** travel back through the rotor stack. Instead:

```text
Reflector J4 pin 15 (TTD_RETURN)
  → Extension Port / J7 (16-pin Molex 2.54mm)
    → Stator J7 pin 15 (TTD_RETURN arrives at Controller)
```

Stator J7 and Reflector J4 exist specifically to carry TTD_RETURN directly back to the Stator, bypassing
all rotors. This is architecturally essential for JTAG chain closure.

### Extension Board Signal Buffering

Every 5 rotors, an Extension board re-buffers **TCK** and **TMS** using a **74LVC2G125** dual-buffer IC
(U1). **TTD is NOT buffered at Extensions** — it is a serial chain signal and must pass uninterrupted
through each CPLD. The Extension board draws 3V3_ENIG from its J7/J8 Molex port to power U1.

### Signal Integrity

| Component | Location | Value | Purpose |
| :--- | :--- | :--- | :--- |
| R1 | Each Rotor CPLD TDO → J4 pin 6 | 75Ω series | Controlled-impedance termination on TTD output |
| R1 | Reflector TTD input | 22Ω series | Reflector end-of-chain TTD termination |
| R2 | Each Rotor | 10kΩ pull-up | TMS default-high |
| R3 | Each Rotor | 10kΩ pull-up | TDI default-high |
| R4 | Each Rotor | 10kΩ pull-down | TCK default-low |
| R5 | Each Rotor | 10kΩ pull-up | SYS_RESET_N default-high (inactive) |

---

## 5. Enigma Cipher Data Path (ENC Signals)

> **The ENC signal path is architecturally separate from JTAG and must not be confused with it.**

The **ENC_IN / ENC_OUT** signals carry the actual Enigma cipher path — keypress to lightboard result.

- **Bus width:** 12-bit parallel: ENC_IN[0:5] and ENC_OUT[0:5].
- **Physical connectors:** J3 (20-pin ERM8-010 male, input) and J6 (20-pin ERF8-010 female, output).
- **Pin naming note:** ENC_IN/ENC_OUT names on connectors denote physical connector orientation, **not**
  the cipher data direction. The cipher data **reverses direction at the Reflector** — signals called
  ENC_IN on a connector may carry cipher data flowing in either direction depending on cipher phase.

### Cipher Data Flow

```text
Keypress
  → Stator CPLD (ENC routing and plugboard mapping)
    → Rotor 1 ENC_IN → [CPLD wiring emulation] → Rotor 1 ENC_OUT
      → Rotor 2 … → Rotor 30
        → Reflector (programmed redirect — cipher reversal)
          → Rotor 30 (return path) → … → Rotor 1
            → Stator CPLD
              → Lightboard
```

### Encoder Board Connections (Stator J4–J6)

| Stator Connector | Board | Function |
| :--- | :--- | :--- |
| J4 | HID Encoder | Keyboard matrix input + lightboard output (26-pin THT 2×13 2.54mm) |
| J5 | Plugboard Encoder 1 | Plugboard wiring matrix, bank 1 (26-pin THT 2×13 2.54mm) |
| J6 | Plugboard Encoder 2 | Plugboard wiring matrix, bank 2 (26-pin THT 2×13 2.54mm) |

---

## 6. Inter-Board Link Connectors

| Connector | Type | Pins | Purpose |
| :--- | :--- | :--- | :--- |
| Link-Alpha (PM → Ctrl) | ERM8-040 male / ERF8-040 female | 80 | Power + Ethernet + Telemetry |
| Link-Beta (Ctrl → Stator) | Controller J2 (ERF8-020 female) ↔ Stator J8 (ERM8-020 male) | 40 | 3V3_ENIG + JTAG + Control signals |
| Stator J1–J3 | ERF8-005/010 female | 10/10/20 | Rotor 1 interface |
| Stator J4–J6 | 26-pin THT | 26 | Encoder board connections |
| Stator J7 | 16-pin (Molex 2.54mm) | 16 | Extension/Reflector port (carries TTD_RETURN on pin 15) |
| Stator J8 | ERM8-020 / ERF8-020 | 40 | Link-Beta (Controller Board) |
| Extension J7/J8 | 16-pin (Molex 2.54mm) | 16 | Extension IN/OUT port for chaining |
| Reflector J4 | 16-pin (Molex 2.54mm) | 16 | Stator/Extension return port |

---

## 7. Design Decisions Cross-Reference

See `design/Design_Log.md` for the complete list. Key decisions relevant to system architecture:

| Decision | Summary | DEC # |
| :--- | :--- | :--- |
| 3V3_SYSTEM retired → 3V3_ENIG | Unified rail name used throughout | DEC-001 |
| JTAG serial daisy-chain topology | Not hub-and-spoke; each CPLD in series | DEC-016 |
| JTAG trace 50Ω controlled impedance | JLC04161H-7628 stackup | DEC-016 |
| 4-layer stackup | JLC04161H-7628 | DEC-017 |
| Rotor connector definition ownership | Rotor Design_Spec §3.4 is authoritative | DEC-018 |
| PoE ACF topology | Coilcraft POE600F-12LD | DEC-019 |
