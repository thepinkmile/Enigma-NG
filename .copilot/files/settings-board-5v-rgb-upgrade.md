# Settings Board 5V RGB LED Upgrade — Design Document

**Date:** 2026-04-17  
**Status:** Draft  
**Author:** Copilot + User  

## Summary

Upgrade Settings Board LED control from 3.3V single-color to 5V full RGB capability using dual MCP23017 I²C expanders with bank-specific routing.

---

## Problem Statement

Current design issues:
1. **Insufficient voltage:** 3V3_ENIG supply marginal for green/blue LEDs (Vf ~3.0-3.3V)
2. **Limited brightness:** MCP23017 GPIO limited to 16mA @ 3.3V; RGB LEDs need 20mA for full brightness
3. **No blue channel:** Current design only uses red/green; no blue resistors/routing
4. **Pin shortage:** Original single-MCP23017 design has only 4 spare GPIO for 6 color rails (3 colors × 2 banks)

---

## Solution Architecture

### **Dual-IC Bank-Specific Design**

- **U_LED_B1 @ 0x40 (MCP23017):** Controls Bank 1 (5 LEDs) — anodes + RGB color rails
- **U_LED_B2 @ 0x41 (MCP23017):** Controls Bank 2 (6 LEDs) — anodes + RGB color rails
- **U_EXP_SW_IN @ 0x26 (MCP23017):** Retains switch reading function (unchanged)

### **Power Supply**

- **5V_LED rail:** Routed from Stator via expanded J_I2C connector (4-pin → 6-pin JST PH)
- **Current budget:** 12 LEDs × 20mA × 1 color typical = 240mA max (one color active per bank)
- **Realistic load:** ~100-150mA average (mixed colors, not all LEDs full brightness)

### **Low-Side Color-Rail Switching**

- **6× BSS138 N-channel MOSFETs:** One per color rail (BNK1_R, BNK1_G, BNK1_B, BNK2_R, BNK2_G, BNK2_B)
- **Gate drivers:** Direct from MCP23017 GPIO (3.3V logic, 10mA gate drive)
- **Drain:** Connected to LED cathodes (color-specific)
- **Source:** GND

---

## Pin Assignments

### **U_LED_B1 @ 0x40 — Bank 1 LED Controller**

| Port | Pin | Signal | Direction | Connected To | Notes |
|---|---|---|---|---|---|
| **GPA** | [0] | **LED_B1_EN_A** | Output | LED_B1_EN anode | Bank 1 enable LED |
| GPA | [1] | **LED_B1_0_A** | Output | LED_B1_0 anode | Bank 1 bit 0 LED |
| GPA | [2] | **LED_B1_1_A** | Output | LED_B1_1 anode | Bank 1 bit 1 LED |
| GPA | [3] | **LED_B1_2_A** | Output | LED_B1_2 anode | Bank 1 bit 2 LED |
| GPA | [4] | **LED_B1_3_A** | Output | LED_B1_3 anode | Bank 1 bit 3 LED |
| GPA | [5] | **BNK1_R** | Output | Q_BNK1_R gate | Red color rail enable |
| GPA | [6] | **BNK1_G** | Output | Q_BNK1_G gate | Green color rail enable |
| GPA | [7] | **BNK1_B** | Output | Q_BNK1_B gate | Blue color rail enable |
| **GPB** | [0:7] | **SPARE_B1[0:7]** | — | — | 8 spare GPIO for future expansion |

**Total GPIOs used:** 8 of 16  
**Spare GPIOs:** 8

---

### **U_LED_B2 @ 0x41 — Bank 2 LED Controller**

| Port | Pin | Signal | Direction | Connected To | Notes |
|---|---|---|---|---|---|
| **GPA** | [0] | **LED_B2_EN_A** | Output | LED_B2_EN anode | Bank 2 enable LED |
| GPA | [1] | **LED_B2_0_A** | Output | LED_B2_0 anode | Bank 2 bit 0 LED |
| GPA | [2] | **LED_B2_1_A** | Output | LED_B2_1 anode | Bank 2 bit 1 LED |
| GPA | [3] | **LED_B2_2_A** | Output | LED_B2_2 anode | Bank 2 bit 2 LED |
| GPA | [4] | **LED_B2_3_A** | Output | LED_B2_3 anode | Bank 2 bit 3 LED |
| GPA | [5] | **LED_B2_4_A** | Output | LED_B2_4 anode | Bank 2 bit 4 LED |
| GPA | [6] | **LED_B2_5_A** | Output | LED_B2_5 anode | Bank 2 bit 5 LED |
| GPA | [7] | **BNK2_R** | Output | Q_BNK2_R gate | Red color rail enable |
| **GPB** | [0] | **BNK2_G** | Output | Q_BNK2_G gate | Green color rail enable |
| GPB | [1] | **BNK2_B** | Output | Q_BNK2_B gate | Blue color rail enable |
| GPB | [2:7] | **SPARE_B2[0:5]** | — | — | 6 spare GPIO for future expansion |

**Total GPIOs used:** 10 of 16  
**Spare GPIOs:** 6

---

### **U_EXP_SW_IN @ 0x26 — Switch Input Reader (Unchanged)**

| Port | Pin | Signal | Direction | Connected To | Notes |
|---|---|---|---|---|---|
| **GPA** | [0] | **SW_B1_EN** | Input | Bank 1 enable switch | Pull-up, active LOW |
| GPA | [1] | **SW_B1_0** | Input | Bank 1 bit 0 switch | Pull-up, active LOW |
| GPA | [2] | **SW_B1_1** | Input | Bank 1 bit 1 switch | Pull-up, active LOW |
| GPA | [3] | **SW_B1_2** | Input | Bank 1 bit 2 switch | Pull-up, active LOW |
| GPA | [4] | **SW_B1_3** | Input | Bank 1 bit 3 switch | Pull-up, active LOW |
| GPA | [5:7] | **SPARE_SW[0:2]** | — | — | 3 spare GPIO |
| **GPB** | [0] | **SW_B2_EN** | Input | Bank 2 enable switch | Pull-up, active LOW |
| GPB | [1] | **SW_B2_0** | Input | Bank 2 bit 0 switch | Pull-up, active LOW |
| GPB | [2] | **SW_B2_1** | Input | Bank 2 bit 1 switch | Pull-up, active LOW |
| GPB | [3] | **SW_B2_2** | Input | Bank 2 bit 2 switch | Pull-up, active LOW |
| GPB | [4] | **SW_B2_3** | Input | Bank 2 bit 3 switch | Pull-up, active LOW |
| GPB | [5] | **SW_B2_4** | Input | Bank 2 bit 4 switch | Pull-up, active LOW |
| GPB | [6] | **SW_B2_5** | Input | Bank 2 bit 5 switch | Pull-up, active LOW |
| GPB | [7] | **CFG_APPLY** | Input | Config apply button | Pull-up, active LOW |

**Total GPIOs used:** 13 of 16  
**Spare GPIOs:** 3

---

## I²C Address Map

| Device | Address | Function | Bus Position |
|---|---|---|---|
| U_EXP_SW_IN | **0x26** | Switch input reader | Settings Board |
| U_LED_B1 | **0x40** | Bank 1 LED controller | Settings Board |
| U_LED_B2 | **0x41** | Bank 2 LED controller | Settings Board |
| U_EXP4 | **0x22** | CPLD config driver | Stator Board |

**Note:** U_EXP_LED @ 0x27 is **removed** from design (replaced by U_LED_B1 + U_LED_B2)

---

## LED Circuit Topology

### **Common-Anode Configuration**

Each RGB LED has:
- **Common anode:** Driven HIGH by U_LED_Bx GPIO (sources current from 5V_LED via LED)
- **Red cathode:** Through R_LED_Rx (150Ω) to BNKx_R rail
- **Green cathode:** Through R_LED_Gx (100Ω) to BNKx_G rail
- **Blue cathode:** Through R_LED_Bx (100Ω) to BNKx_B rail

### **Color-Rail MOSFETs (Low-Side Switches)**

| MOSFET Ref | Controlled By | Signal | Rail | LEDs Controlled |
|---|---|---|---|---|
| **Q_BNK1_R** | U_LED_B1 GPA[5] | BNK1_R | Red Bank 1 | LED_B1_EN, LED_B1_[0:3] red dies |
| **Q_BNK1_G** | U_LED_B1 GPA[6] | BNK1_G | Green Bank 1 | LED_B1_EN, LED_B1_[0:3] green dies |
| **Q_BNK1_B** | U_LED_B1 GPA[7] | BNK1_B | Blue Bank 1 | LED_B1_EN, LED_B1_[0:3] blue dies |
| **Q_BNK2_R** | U_LED_B2 GPA[7] | BNK2_R | Red Bank 2 | LED_B2_EN, LED_B2_[0:5] red dies |
| **Q_BNK2_G** | U_LED_B2 GPB[0] | BNK2_G | Green Bank 2 | LED_B2_EN, LED_B2_[0:5] green dies |
| **Q_BNK2_B** | U_LED_B2 GPB[1] | BNK2_B | Blue Bank 2 | LED_B2_EN, LED_B2_[0:5] blue dies |

**MOSFET:** BSS138 (Vds 50V, Id 220mA, Vgs(th) 0.8-1.5V, Rds(on) ~3.5Ω @ Vgs=4.5V)

---

## Current-Limiting Resistor Calculations

### **Design Parameters**

- **Supply voltage:** 5.0V (5V_LED rail)
- **Target LED current:** 20mA per die
- **LED forward voltages (Kingbright WP154A4SEJ3VBDZGW/CA):**
  - Red: Vf = 2.0V typical (1.8-2.2V range)
  - Green: Vf = 3.0V typical (2.8-3.4V range)
  - Blue: Vf = 3.0V typical (2.8-3.4V range)

### **Resistor Values**

| Color | Calculation | Standard Value | Actual Current | Power Dissipation |
|---|---|---|---|---|
| **Red** | (5.0V - 2.0V) / 0.020A = 150Ω | **150Ω ±1%** | 20.0mA | 60mW |
| **Green** | (5.0V - 3.0V) / 0.020A = 100Ω | **100Ω ±1%** | 20.0mA | 40mW |
| **Blue** | (5.0V - 3.0V) / 0.020A = 100Ω | **100Ω ±1%** | 20.0mA | 40mW |

**Package:** 0603 thick-film resistor, 1% tolerance, 0.1W rated power (sufficient for 40-60mW dissipation)

### **Recommended MPN**

**Panasonic ERJ-3EKF Series (0603, 1%, thick-film):**
- **R_LED_R1–R12:** ERJ-3EKF1500V (150Ω, DigiKey: P150BYCT-ND, Mouser: 667-ERJ-3EKF1500V)
- **R_LED_G1–G12:** ERJ-3EKF1000V (100Ω, DigiKey: P100BYCT-ND, Mouser: 667-ERJ-3EKF1000V)
- **R_LED_B1–B12:** ERJ-3EKF1000V (100Ω, DigiKey: P100BYCT-ND, Mouser: 667-ERJ-3EKF1000V)

**Total resistors:** 36 (12 LEDs × 3 colors)

---

## Updated J_I2C Connector

### **Connector Change: 4-pin → 6-pin JST PH 2.0mm**

| Pin | Signal | Direction | Purpose | Current Rating |
|---|---|---|---|---|
| 1 | **3V3_ENIG** | Stator → SBD | Logic power for MCP23017s | ~80mA (3× ICs @ ~25mA each) |
| 2 | **5V_LED** | Stator → SBD | LED anode supply | **~240mA max** |
| 3 | **GND** | Common | Logic ground return | — |
| 4 | **SDA** | Bidirectional | I²C data line | — |
| 5 | **SCL** | Stator → SBD | I²C clock line | — |
| 6 | **GND** | Common | LED cathode return | **~240mA max** |

**Why 2× GND pins?**
- Pin 3 (GND): Low-current logic return for MCP23017s (~80mA total)
- Pin 6 (GND): High-current LED return (up to 240mA)
- Separating logic and power grounds reduces noise coupling into I²C signals

### **Connector MPN**

**Settings Board (vertical THT):**
- **B6B-PH-K-S(LF)(SN)** — 6-pin JST PH 2.0mm vertical THT receptacle
  - Mouser: 474-B6B-PH-K-S(LF)(SN)
  - DigiKey: 455-1723-ND
  - Rated: 2A per pin

**Stator Board (J_CFG vertical THT):**
- **B6B-PH-K-S(LF)(SN)** — Same as Settings Board

**Cable Assembly:**
- 6-wire ribbon cable with JST PHR-6 crimp housing both ends
- Suggested: 28AWG for 5V_LED/GND (pins 2,6), 30AWG for signals (pins 1,3,4,5)
- Length: TBD based on enclosure layout

---

## Bill of Materials Changes

### **Added Components**

| Ref | Qty | Description | MPN | DigiKey | Mouser | JLCPCB | Notes |
|---|---|---|---|---|---|---|---|
| **U_LED_B1** | 1 | I²C I/O expander, 16-bit, 0x40 base addr | MCP23017T-E/SO | MCP23017T-E/SO-ND | 579-MCP23017T-E/SO | C424072 | Bank 1 LED controller |
| **U_LED_B2** | 1 | I²C I/O expander, 16-bit, 0x40 base addr | MCP23017T-E/SO | MCP23017T-E/SO-ND | 579-MCP23017T-E/SO | C424072 | Bank 2 LED controller |
| **Q_BNK1_B** | 1 | N-channel MOSFET, SOT-23 | BSS138 | BSS138CT-ND | 512-BSS138 | C112239 | Blue low-side switch Bank 1 |
| **Q_BNK2_B** | 1 | N-channel MOSFET, SOT-23 | BSS138 | BSS138CT-ND | 512-BSS138 | C112239 | Blue low-side switch Bank 2 |
| **R_LED_B1–B12** | 12 | Resistor 100Ω 1% 0603 | ERJ-3EKF1000V | P100BYCT-ND | 667-ERJ-3EKF1000V | C22775 | Blue channel current limit |
| **J_I2C** | 1 | 6-pin JST PH 2.0mm vert THT | B6B-PH-K-S(LF)(SN) | 455-1723-ND | 474-B6B-PH-K-S(LF)(SN) | TBD | Replaces 4-pin version |

### **Removed Components**

| Ref | Description | Notes |
|---|---|---|
| **U_EXP_LED @ 0x27** | MCP23017T-E/SO | Replaced by U_LED_B1 + U_LED_B2 |
| **J_I2C (4-pin)** | B4B-PH-K-S(LF)(SN) | Upgraded to 6-pin |

### **Modified Components**

| Ref | Old Value | New Value | MPN | Notes |
|---|---|---|---|---|
| **R_LED_R1–R12** | TBD @ 3.3V | **150Ω ±1%** | ERJ-3EKF1500V | Recalculated for 5V @ 20mA |
| **R_LED_G1–G12** | TBD @ 3.3V | **100Ω ±1%** | ERJ-3EKF1000V | Recalculated for 5V @ 20mA |
| **Q_BNK1_R, Q_BNK1_G, Q_BNK2_R, Q_BNK2_G** | BSS138 (4 total) | BSS138 (4 total) | BSS138 | Unchanged (added Q_BNK1_B + Q_BNK2_B) |

### **Net BOM Changes**

| Component Type | Change | Net Impact |
|---|---|---|
| **MCP23017T-E/SO** | +2 units (U_LED_B1, U_LED_B2) | +2 (was 1, now 3 on Settings Board) |
| **BSS138 MOSFET** | +2 units (Q_BNK1_B, Q_BNK2_B) | +2 (was 4, now 6 on Settings Board) |
| **0603 resistors** | +12 blue resistors | +12 (was 24, now 36 LED resistors) |
| **JST PH connector** | 4-pin → 6-pin | Upgraded (pin count +2) |

**Cost impact:** ~$2-3 per Settings Board (2× MCP23017 + 2× MOSFET + 12× resistor)

---

## Control Flow (CM5 Software Perspective)

### **Initialization**

1. CM5 configures U_EXP_SW_IN @ 0x26: all GPIO as inputs with pull-ups
2. CM5 configures U_LED_B1 @ 0x40: all GPIO as outputs, initialized LOW
3. CM5 configures U_LED_B2 @ 0x41: all GPIO as outputs, initialized LOW
4. CM5 configures Stator U_EXP4 @ 0x22: configure CPLD config pins + STATOR_CFG_RDY output

### **Normal Operation Loop**

1. **Read switches:** CM5 reads U_EXP_SW_IN @ 0x26 (13 switches: bank enables + config bits)
2. **Evaluate mode:**
   - If `SW_B1_EN == HIGH`: Bank 1 is switch-defined → use switch values
   - If `SW_B1_EN == LOW`: Bank 1 is CM5-override → use CM5-calculated config
   - Same logic for Bank 2 via `SW_B2_EN`
3. **Write config:** CM5 writes final configuration to Stator U_EXP4 @ 0x22 (CPLD config pins)
4. **Update LEDs:**
   - For each bank, determine active color (e.g., green=switch-mode, red=CM5-mode, blue=special)
   - Write anode states to U_LED_Bx (HIGH = LED on, LOW = LED off)
   - Write color-rail gates to U_LED_Bx (HIGH = MOSFET on, color active)
5. **Trigger reload (two options):**
   - **User-initiated:** CM5 polls CFG_APPLY button via U_EXP_SW_IN GPB[7]; when pressed, pulse Stator U_EXP4 STATOR_CFG_RDY output HIGH for 100ms
   - **CM5-initiated:** CM5 directly pulses Stator U_EXP4 STATOR_CFG_RDY output HIGH for 100ms to force reload without button press
6. **CPLD latches config:** Stator CPLD detects rising edge on STATOR_CFG_RDY, latches new configuration from U_EXP4

**Note:** STATOR_CFG_RDY signal is generated by **Stator U_EXP4 @ 0x22**, NOT by Settings Board. This keeps the reload logic co-located with the CPLD config driver.

### **Example: Bank 1 in Switch Mode, Config = 0b0101**

**U_LED_B1 @ 0x40 write:**
```
GPA[0] = LOW   // LED_B1_EN_A = off (enable switch not shown)
GPA[1] = HIGH  // LED_B1_0_A = on (bit 0 is SET)
GPA[2] = LOW   // LED_B1_1_A = off (bit 1 is CLEAR)
GPA[3] = HIGH  // LED_B1_2_A = on (bit 2 is SET)
GPA[4] = LOW   // LED_B1_3_A = off (bit 3 is CLEAR)
GPA[5] = LOW   // BNK1_R = off (not in CM5 mode)
GPA[6] = HIGH  // BNK1_G = on (switch mode = green)
GPA[7] = LOW   // BNK1_B = off (not in special mode)
```

**Result:** LED_B1_0 and LED_B1_2 glow **green** (bits SET in switch-defined config)

### **Example: Programmatic Reload Sequence**

```
1. Write config to Stator U_EXP4 @ 0x22 config pins
2. Pulse Stator U_EXP4 STATOR_CFG_RDY output = HIGH (trigger reload)
3. Wait 100ms
4. Pulse Stator U_EXP4 STATOR_CFG_RDY output = LOW (return to idle)
```

---

## Power Budget

### **Logic Power (3V3_ENIG)**

| Device | Typ Current | Max Current | Notes |
|---|---|---|---|
| U_EXP_SW_IN | 25mA | 50mA | Input port, pull-ups enabled |
| U_LED_B1 | 25mA | 50mA | Output port, driving MOSFETs |
| U_LED_B2 | 25mA | 50mA | Output port, driving MOSFETs |
| **Total** | **75mA** | **150mA** | Well within J_I2C 3V3 capability |

### **LED Power (5V_LED)**

| Scenario | LEDs Active | Colors | Current | Notes |
|---|---|---|---|---|
| **Worst-case** | 12 LEDs | 1 color | 12 × 20mA = **240mA** | All LEDs on, single color (red/green/blue) |
| **Typical** | 6 LEDs | 1 color | 6 × 20mA = **120mA** | Half LEDs on (average config density) |
| **Mixed colors** | 12 LEDs | 2 colors | 12 × 40mA = **480mA** | Both banks active, different colors |
| **Full RGB** | 12 LEDs | 3 colors | 12 × 60mA = **720mA** | UNREALISTIC: software should limit to 1-2 colors active |

**Design target:** 240mA max per J_I2C spec (JST PH rated 2A per pin, conservative 240mA limit)

**Software constraint:** CM5 should enforce "only 1 color active per bank" to stay within 240mA budget.

---

## 5V Power Routing — SELECTED OPTION

**Decision:** Route 5V_MAIN from Controller through Link-Beta to Stator, then forward to Settings Board.

### **Architecture: Controller → Link-Beta → Stator → Settings Board**

```
Controller Board:
  5V_MAIN (TPS259804 eFuse output, 3A capable)
    ↓
  Link-Beta pins 18 + 23 (2× parallel pins for current sharing)
    ↓
Stator Board:
  5V_MAIN (pass-through, no local consumption)
    ↓
  J_CFG pin 2 (6-pin JST PH connector)
    ↓
Settings Board:
  5V_LED rail (powers 12× RGB LED anodes via U_LED_B1/B2)
  Load: 240mA max (12 LEDs × 20mA × 1 color)
```

### **Link-Beta Pin Allocation (Samtec ERF8-020/ERM8-020, 40-pin)**

**Current spare pins (Controller Design_Spec.md line 105):**
- Pins 14–17: SPARE (previously ENC_IN monitoring)
- Pins 19–24: SPARE (previously ENC_OUT monitoring)

**Proposed allocation for 5V_MAIN:**
- **Pin 18:** 5V_MAIN power (0.5A capability per pin)
- **Pin 23:** 5V_MAIN power (0.5A capability per pin, parallel with pin 18)
- **Total capacity:** 2× 0.5A = **1.0A** (240mA Settings Board + 760mA margin for future J_SERVO @ 5V)

**Why 2 pins?**
- Current sharing reduces trace heating and connector stress
- Provides 1A total capacity (4× margin over 240mA Settings Board load)
- Leaves capacity for future 5V_SERVO servo motor (stall current ~500mA typical)

### **Benefits of This Approach**

✅ **No boost converter needed** — simpler, cheaper, more efficient  
✅ **Solves J_SERVO 5V_TBD** — Stator now has 5V for servo control (Stator DR-STA-14)  
✅ **Minimal BOM impact** — no new ICs, just connector pin reassignment  
✅ **Clean power path** — regulated 5V_MAIN from Controller eFuse, no multiple boost stages  
✅ **Future-proof** — 1A capacity supports Settings Board (240mA) + servo (500mA) + margin

### **Required Design Changes**

**Controller Board (Link-Beta J8):**
- Reassign pins 18, 23 from SPARE → 5V_MAIN
- Route 5V_MAIN from TPS259804 U1 output to ERM8-020 pins 18, 23
- Update Controller Design_Spec.md §2.2 Link-Beta pin table

**Stator Board:**
- Reassign Link-Beta pins 18, 23 from SPARE → 5V_MAIN
- Route 5V_MAIN from ERF8-020 pins 18, 23 to J_CFG pin 2
- Expand J_CFG from 4-pin → 6-pin JST PH
- Update Stator Design_Spec.md DR-STA-14 (J_SERVO now gets 5V_MAIN)
- Update Stator Design_Spec.md DR-STA-17 (J_CFG now 6-pin with 5V_MAIN)

**Settings Board:**
- J_I2C receives 5V_LED via pin 2 (from Stator J_CFG)
- No changes needed (already designed for 6-pin connector)

---

## Design Review Checklist

- [x] Pin assignments complete for U_LED_B1, U_LED_B2
- [x] I²C address conflict check (0x40, 0x41 available)
- [x] Resistor values calculated and verified (150Ω red, 100Ω green, 100Ω blue)
- [x] MOSFET count updated (4 → 6 units)
- [x] J_I2C connector upgraded (4-pin → 6-pin)
- [x] Power budget calculated (3V3: 150mA max, 5V_LED: 240mA max)
- [x] BOM impact documented (+2 IC, +2 MOSFET, +12 resistor)
- [x] CPLD reload signal architecture confirmed (via Stator U_EXP4, not Settings Board)
- [x] 5V power routing selected: Controller → Link-Beta (pins 18, 23) → Stator → Settings Board
- [ ] Verify U_EXP_LED @ 0x27 removal doesn't break other board references
- [ ] Update Controller Design_Spec.md Link-Beta pin table (assign pins 18, 23 to 5V_MAIN)
- [ ] Route 5V_MAIN from Controller TPS259804 to Link-Beta pins 18, 23
- [ ] Update Stator Design_Spec.md Link-Beta receiver (pins 18, 23 = 5V_MAIN)
- [ ] Update Stator Design_Spec.md DR-STA-14 (J_SERVO now has 5V_MAIN available)
- [ ] Update Stator Design_Spec.md DR-STA-17 (J_CFG upgraded to 6-pin with 5V_MAIN)
- [ ] Update Settings Board schematic (KiCAD)
- [ ] Update Stator schematic if 5V boost added (KiCAD)
- [ ] Update Controller Design_Spec.md I²C address table
- [ ] Update Consolidated_BOM.md with new part counts

---

## Next Steps

1. **Update Controller Design_Spec.md:**
   - Reassign Link-Beta pins 18, 23 from SPARE → 5V_MAIN in pin table (§2.2)
   - Add note: "5V_MAIN routed to Stator for Settings Board LEDs and J_SERVO"
   - Update schematic: route 5V_MAIN from TPS259804 to ERF8-020 pins 18, 23
2. **Update Stator Design_Spec.md:**
   - Update Link-Beta receiver section: pins 18, 23 = 5V_MAIN (not SPARE)
   - Update DR-STA-14 (J_SERVO): Replace "5V_SERVO_TBD" with "5V_MAIN" (now available)
   - Update DR-STA-17 (J_CFG): Upgrade from 4-pin → 6-pin JST PH (add 5V_MAIN, extra GND)
   - Add 5V_MAIN rail routing: Link-Beta → J_CFG → J_SERVO
   - Update schematic: route 5V_MAIN from ERF8-020 to J_CFG pin 2 and J_SERVO pin 1
3. **Update Settings Board Design_Spec.md:**
   - Replace U_EXP_LED section with U_LED_B1 + U_LED_B2
   - Update BOM with new resistor values, 6× MOSFETs, 6-pin connector
   - Update LED Control Logic section with dual-IC architecture
   - Add 5V_LED rail to power section
3. **Update Stator Design_Spec.md:**
   - Add 5V boost circuit (if Option B selected)
   - Update J_CFG connector to 6-pin
   - Update BOM
   - Confirm U_EXP4 @ 0x22 has STATOR_CFG_RDY output pin assignment
4. **Update Consolidated_BOM.md:**
   - MCP23017: Settings Board qty 1 → 3 (U_EXP_SW_IN, U_LED_B1, U_LED_B2)
   - BSS138: Settings Board qty 4 → 6
   - ERJ-3EKF1500V: Add 12 units (R_LED_R1–R12)
   - ERJ-3EKF1000V: Add 24 units (R_LED_G1–G12, R_LED_B1–B12)
5. **Update Controller Design_Spec.md I²C address table:**
   - Remove U_EXP_LED @ 0x27
   - Add U_LED_B1 @ 0x40, U_LED_B2 @ 0x41
6. **Update components-todo.md:**
   - Mark LED resistors VERIFIED with final MPN values
   - Add U_LED_B1, U_LED_B2 entries
   - Update BSS138 MOSFET count

---

## Revision History

| Date | Ver | Author | Changes |
|---|---|---|---|
| 2026-04-17 | 0.2 | Copilot | Corrected reload signal architecture — uses Stator U_EXP4, not Settings Board |
| 2026-04-17 | 0.1 | Copilot | Initial draft — dual-IC architecture, resistor calculations, BOM impact |

