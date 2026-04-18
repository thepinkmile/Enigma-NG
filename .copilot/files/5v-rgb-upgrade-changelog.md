# Settings Board 5V RGB Upgrade — Change Summary

**Date:** 2026-04-17  
**Issue:** Settings Board RGB LEDs were underpowered at 3.3V and the older draft did not fully allocate the blue-drive path or enough GPIO for full RGB control

## Summary of Changes

### **Architecture Decision**
- **Power:** 5V_MAIN routed from Controller → Link-Beta (pins 18, 23) → Stator → Settings Board (5V_LED rail)
- **LED Control:** Dual MCP23017 (U_LED_B1 @ 0x40 + U_LED_B2 @ 0x41) replaces single U_EXP_LED @ 0x27
- **Color Rails:** 6× BSS138 MOSFETs (was 4) for full RGB control (red, green, blue per bank)
- **Resistors:** All recalculated for 5V @ 20mA operation

---

## Files Modified

### **1. design/Electronics/Controller/Design_Spec.md**

**Line 8:** Updated Last Updated to 2026-04-17

**Lines 105-106:** Updated Link-Beta pin allocation
```diff
-    * **Pins 14–24:** Previously ENC_IN[0:5] and ENC_OUT[0:5] — now mostly spare (monitoring via I²C expander U_EXP1). Pins 14–17 and 19–24 are **SPARE**; no 5V_MAIN on LINK-BETA.
+    * **Pins 14–17, 19–22, 24:** Previously ENC_IN[0:5] and ENC_OUT[0:5] — now mostly spare (monitoring via I²C expander U_EXP1). These pins remain **SPARE**.
+    * **Pins 18, 23:** 5V_MAIN power delivery (2× pins for current sharing, 0.5A per pin = 1.0A total capacity). Routed to Stator for Settings Board LEDs (5V_LED rail, 240mA) and J_SERVO servo motor power (5V_MAIN, up to 500mA).
```

**Lines 180-182:** Updated I²C address table
```diff
 | 0x26 | MCP23017 (U_EXP_SW_IN) | Settings Board | Switch input reader (DEC-032) |
-| 0x27 | MCP23017 (U_EXP_LED) | Settings Board | LED anode + colour-rail driver (current Settings Board implementation; see DEC-034) |
+| 0x40 | MCP23017 (U_LED_B1) | Settings Board | Bank 1 LED controller: 5× anodes + RGB color-rail drivers (DEC-034) |
+| 0x41 | MCP23017 (U_LED_B2) | Settings Board | Bank 2 LED controller: 6× anodes + RGB color-rail drivers (DEC-034) |
 | 0x60 | PCA9685 (U_EXP3) | Stator | Servo PWM driver (Ch0 = 50Hz SERVO_PWM) |
```

---

### **2. design/Electronics/Stator/Design_Spec.md**

**Line 8:** Updated Last Updated to 2026-04-17

**Line 56 (DR-STA-14):** Solved J_SERVO 5V power issue
```diff
-| DR-STA-14 | Servo connector | J_SERVO = 3-pin JST PH 2.0mm connector; pins: 5V_SERVO_TBD, GND, SERVO_PWM. Servo control is on the Stator; the 5V power source remains an open architecture item because Link-Beta does not carry 5V_MAIN. | BOM J_SERVO |
+| DR-STA-14 | Servo connector | J_SERVO = 3-pin JST PH 2.0mm connector; pins: 5V_MAIN, GND, SERVO_PWM. 5V_MAIN is routed from Controller Board via Link-Beta pins 18 and 23 (1.0A capacity). | BOM J_SERVO |
```

**Line 59 (DR-STA-17):** Upgraded J_CFG connector to 6-pin
```diff
-| DR-STA-17 | J_CFG connector | J_CFG = 4-pin JST PH 2.0mm B4B-PH-K-S(LF)(SN); pins: 3V3_ENIG, GND, SDA, SCL; connects to Settings Board J_I2C via 4-wire ribbon cable | BOM J_CFG |
+| DR-STA-17 | J_CFG connector | J_CFG = 6-pin JST PH 2.0mm B6B-PH-K-S(LF)(SN); pins: 3V3_ENIG, 5V_LED, GND (logic), SDA, SCL, GND (LED); connects to Settings Board J_I2C via 6-wire ribbon cable. 5V_LED is derived from 5V_MAIN (Link-Beta pins 18, 23). | BOM J_CFG |
```

---

### **3. design/Electronics/Settings_Board/Design_Spec.md**

**Line 8:** Updated Last Updated to 2026-04-17

**Lines 20-26:** Updated overview with dual-IC architecture
```diff
-The Settings Board communicates with the Stator Board exclusively via a 4-wire I²C ribbon cable
-(J_I2C → Stator J_CFG), sharing the Stator I²C-1 bus. It hosts two MCP23017 GPIO expanders:
+The Settings Board communicates with the Stator Board exclusively via a 6-wire I²C ribbon cable
+(J_I2C → Stator J_CFG), sharing the Stator I²C-1 bus. It hosts three MCP23017 GPIO expanders:

 * **U_EXP_SW_IN (@ 0x26):** Reads all 12 switch states and the CFG_APPLY momentary button.
-* **U_EXP_LED (@ 0x27):** Drives per-bit LED anodes and per-bank colour-rail low-side sinks.
+* **U_LED_B1 (@ 0x40):** Drives Bank 1 LED anodes (5 LEDs) and RGB color-rail low-side switches.
+* **U_LED_B2 (@ 0x41):** Drives Bank 2 LED anodes (6 LEDs) and RGB color-rail low-side switches.
```

**Lines 45, 54-58 (Design Requirements):** Updated requirements table
```diff
-| FR-SBD-05 | Connect to the Stator Board via a 4-wire I²C ribbon cable (3V3_ENIG, GND, SDA, SCL) | J_I2C = 4-pin JST PH 2.0mm connector; shares Stator I²C-1 bus | §7 Interconnects; BOM J_I2C |
+| FR-SBD-05 | Connect to the Stator Board via a 6-wire I²C ribbon cable (3V3_ENIG, 5V_LED, 2× GND, SDA, SCL) | J_I2C = 6-pin JST PH 2.0mm connector; shares Stator I²C-1 bus; 5V_LED powers RGB LEDs at 20mA per die | §7 Interconnects; BOM J_I2C |

-| DR-SBD-04 | LED output expander | U_EXP_LED = MCP23017T-E/SO @ 0x27; SOIC-28; A2=HIGH, A1=HIGH, A0=HIGH | §4 I²C Devices — U_EXP_LED; BOM U_EXP_LED |
-| DR-SBD-05 | LED colour-rail transistors | 4× BSS138 SOT-23 N-channel MOSFETs (Q_BNK1_G, Q_BNK1_R, Q_BNK2_G, Q_BNK2_R); gate driven from U_EXP_LED GPIO via 1kΩ gate resistor; GPIO HIGH = transistor ON (low-side sink topology) | §5 LED Control Logic; BOM Q_BNK1_G, Q_BNK1_R, Q_BNK2_G, Q_BNK2_R |
-| DR-SBD-06 | CFG_APPLY button | SW_CFG_APPLY = SPST momentary pushbutton, active-low; 10kΩ pull-up to 3V3_ENIG (R_CA1) + 100nF X7R 0402 debounce cap to GND (C_CA1; RC τ = 1ms); connected to U_EXP_SW_IN GPB[7] | §6 CFG_APPLY Button; BOM SW_CFG_APPLY, R_CA1, C_CA1 |
-| DR-SBD-07 | I²C connector | J_I2C = 4-pin JST PH 2.0mm B4B-PH-K-S(LF)(SN); pins: 3V3_ENIG, GND, SDA, SCL; ribbon cable to Stator J_CFG | §7 Interconnects; BOM J_I2C |
-| DR-SBD-08 | Switch input pull-downs | 12× 10kΩ 0603 pull-down resistors on all switch signal inputs to U_EXP_SW_IN (GPA[0:4], GPB[0:6]); HIGH = switch-defined active when switch closed | §4 I²C Devices — U_EXP_SW_IN; BOM R_SW1–R_SW12 |
+| DR-SBD-04 | LED control expanders | U_LED_B1 = MCP23017T-E/SO @ 0x40 (Bank 1); U_LED_B2 = MCP23017T-E/SO @ 0x41 (Bank 2); SOIC-28; full RGB via 6× BSS138 MOSFETs | §4 I²C Devices — U_LED_B1, U_LED_B2; §5 LED Control Logic; BOM U_LED_B1, U_LED_B2 |
+| DR-SBD-05 | LED colour-rail transistors | 6× BSS138 SOT-23 N-channel MOSFETs (Q_BNK1_R/G/B, Q_BNK2_R/G/B); gate driven via 1kΩ resistor; GPIO HIGH = transistor ON | §5 LED Control Logic; BOM Q_BNK1_R, Q_BNK1_G, Q_BNK1_B, Q_BNK2_R, Q_BNK2_G, Q_BNK2_B |
+| DR-SBD-06 | LED power supply | 5V_LED from Stator via J_I2C pin 2; RGB LEDs at 20mA per die; 150Ω (red), 100Ω (green/blue) current-limiting resistors | §7 Interconnects — J_I2C; BOM R_LED_R/G/B |
+| DR-SBD-07 | CFG_APPLY button | SW_CFG_APPLY = SPST momentary, active-low; 10kΩ pull-up to 3V3_ENIG + 100nF debounce cap; U_EXP_SW_IN GPB[7] | §6 CFG_APPLY Button; BOM SW_CFG_APPLY, R_CA1, C_CA1 |
+| DR-SBD-08 | I²C connector | J_I2C = 6-pin JST PH 2.0mm B6B-PH-K-S(LF)(SN); pins: 3V3_ENIG, 5V_LED, 2× GND, SDA, SCL; ribbon to Stator J_CFG | §7 Interconnects; BOM J_I2C |
+| DR-SBD-09 | Switch input pull-downs | 12× 10kΩ 0603 pull-down resistors on all switch inputs to U_EXP_SW_IN (GPA[0:4], GPB[0:6]); HIGH when closed | §4 I²C Devices — U_EXP_SW_IN; BOM R_SW1–R_SW12 |
```

**Lines 192-236:** Replaced U_EXP_LED @ 0x27 with U_LED_B1 @ 0x40 + U_LED_B2 @ 0x41 pin tables

**Lines 242-248:** Updated color scheme table to include blue
```diff
-| Bank Enable State | Colour Rail Active | Meaning |
+| Bank Enable State | Primary Colour | Meaning |
 | :--- | :--- | :--- |
 | HIGH (switch-defined active) | Green (BNKx_G transistor ON) | Configuration source = physical switches |
 | LOW (CM5-defined override) | Red (BNKx_R transistor ON) | Configuration source = CM5 firmware |
+| Special modes | Blue (BNKx_B transistor ON) | Future use: diagnostic, bootloader, error states |
```

**Lines 266-270:** Updated low-side circuit description to include blue MOSFETs

**Lines 302, 312-337:** Updated J_I2C connector from 4-pin to 6-pin with full pinout

**Lines 348-363:** Updated BOM entries
- Changed C_U_EXP_LED → C_U_LED_B1, C_U_LED_B2
- Changed J_I2C from B4B → B6B (4-pin → 6-pin)
- Added Q_BNK1_B, Q_BNK2_B MOSFETs
- Updated R_LED_R/G/B with final resistor values (150Ω red, 100Ω green/blue)
- Changed R_GATE count from ×4 to ×6
- Replaced U_EXP_LED @ 0x27 with U_LED_B1 @ 0x40, U_LED_B2 @ 0x41

---

## Component Count Changes

| Component | Old Qty | New Qty | Change | Notes |
|---|---|---|---|---|
| **MCP23017T-E/SO** | 2 | 3 | +1 | Added U_LED_B2 for Bank 2 control |
| **BSS138 MOSFET** | 4 | 6 | +2 | Added Q_BNK1_B, Q_BNK2_B for blue channels |
| **0603 Resistors (LED)** | 24 | 36 | +12 | Added 12× R_LED_B (100Ω blue resistors) |
| **0402 Resistors (gate)** | 4 | 6 | +2 | Added 2× gate resistors for new MOSFETs |
| **JST PH Connector** | 4-pin | 6-pin | +2 pins | Upgraded J_I2C for 5V_LED + extra GND |

**Resistor Value Changes:**
- R_LED_R1–R12: TBD → **150Ω ±1%** (ERJ-3EKF1500V)
- R_LED_G1–G12: TBD → **100Ω ±1%** (ERJ-3EKF1000V)
- R_LED_B1–B12: 0Ω debug links → **100Ω ±1%** (ERJ-3EKF1000V)

---

## Power Budget

### **3V3_ENIG (Logic Power)**
- U_EXP_SW_IN: 25mA typical
- U_LED_B1: 25mA typical
- U_LED_B2: 25mA typical
- **Total: 75mA typical, 150mA max**

### **5V_LED (LED Power)**
- Worst-case: 12 LEDs × 20mA × 1 color = **240mA**
- Typical: 6 LEDs × 20mA × 1 color = **120mA**
- Design constraint: Only 1 color active per bank

### **Link-Beta 5V_MAIN Allocation**
- Settings Board LEDs: 240mA max
- Stator J_SERVO: 500mA max (servo motor)
- **Total capacity: 1.0A** (2× pins @ 0.5A each)
- **Margin: 260mA** (36% headroom)

---

## Benefits

✅ **Full RGB capability** — Software can select any color per bank  
✅ **Proper LED brightness** — 5V @ 20mA vs. 3.3V @ 16mA marginal operation  
✅ **Solves J_SERVO power issue** — Stator now has 5V for servo motor  
✅ **Clean architecture** — No boost converters, single 5V source from Controller  
✅ **Future-proof** — Blue channel available for diagnostic/error states  
✅ **Bank-specific routing** — U_LED_B1 drives Bank 1, U_LED_B2 drives Bank 2  

---

## Next Steps (Not Implemented)

- [ ] Update Consolidated_BOM.md with new component counts
- [ ] Update components-todo.md with verified resistor MPNs
- [ ] Update Controller schematic: route 5V_MAIN to Link-Beta pins 18, 23
- [ ] Update Stator schematic: route 5V_MAIN from Link-Beta to J_CFG + J_SERVO
- [ ] Update Settings Board schematic: implement dual-IC architecture
- [ ] Verify Link-Beta has physical routing capacity for 2× additional power pins

---

## Design Document Reference

Full architecture, calculations, and design rationale documented in:
`.copilot/files/settings-board-5v-rgb-upgrade.md`
