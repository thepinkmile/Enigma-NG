<overview>
This session completed two major work streams: (1) restructuring the design/Mechanical/ folder from
misleading PCB-named folders to assembly-based folders matching the actual physical machine components,
and (2) fully documenting the CM5 Virtual Keyboard (Key Injection) feature — including DEC-031,
Stator FR/DR updates, Controller GPIO/LINK-BETA/I²C updates, Consolidated BOM additions, and
Power_Management software specification. Both streams were committed cleanly with zero markdownlint
warnings. The Complete_System_Assembly was also expanded into a proper General Assembly reference.
</overview>

## Commits This Session

- `b4fdd9e` — `refactor(mechanical): restructure design/Mechanical/ to assembly-based folders`
- `436e16a` — `Virtual Keyboard Feature + Basic Mechanical Design Refinements`

---

## History

1. **User requested mechanical folder restructure** — current PCB-named structure (Stator/, Controller/, Encoder/ etc.)
   was misleading. Requested assembly-based structure matching how the machine is actually built.

2. **Audit of all existing mechanical files:**
   - `Controller/Mechanical_Design.md` — real content (but actually describes Power Module, not Controller)
   - `Keyboard/Design_Spec.md` — real content (DPDT switches, key mapping); electrical detail to be restored to
     Electronics/Encoder/Design_Spec.md and stripped from mechanical
   - `Plugboard/Design_Spec.md` — real content (¼" jack sockets, harness); same strip/restore treatment
   - `Rotor/Design_Spec.md` — real content (rotor module: shroud, bearings, encoder slots); stays as-is
   - All others: pure stubs → deleted or replaced

3. **Final mechanical structure agreed:**
   - `Rotor/` — rotor module mechanical spec (unchanged)
   - `Rotor_Actuation_Assembly/` — NEW: depression bar, keyboard levers, pivot lever & actuation arm,
     sprung retention bar, servo actuation (one mechanism for human AND CM5 keypresses)
   - `HID_Assembly/` — migrated from Keyboard/, electrical detail stripped
   - `Plugboard_Assembly/` — migrated from Plugboard/, electrical detail stripped
   - `Power_Module/` — replaced stub with Controller/Mechanical_Design.md content (user confirmed that
     content was actually the PM, not Controller)
   - `Main_Enclosure/` — new stub
   - `Complete_System_Assembly/` — new stub → expanded to full General Assembly document
   - `Extension/`, `Reflector/` — kept as-is (stubs)
   - Deleted: `Controller/`, `Keyboard/`, `Plugboard/`, `Encoder/`, `Stator/`, `JTAG_Daughterboard/`
   - JDB: no separate mechanical spec; mentioned in Complete_System_Assembly as Controller hat

4. **Electronics/Encoder/Design_Spec.md** — §6 key mapping and §7 jack-sensing electrical detail restored
   (had previously been incorrectly migrated out to the mechanical specs). Cross-references updated to
   new paths (HID_Assembly/, Plugboard_Assembly/).

5. **CM5 key injection feature documentation** — DEC-031 and all 5 file updates applied:
   - Stator: FR-STA-10–13, DR-STA-12–15, I²C device table, SOURCE_SEL MUX note, servo connector, SERVO_HOME,
     5V_MAIN on LINK-BETA
   - Controller: GPIO 4–15 freed (→ expander), GPIO 26 freed (→ expander), LINK-BETA pins 8/12–24 reassigned
     (SYS_RESET_N and ENC buses → expander; freed slots → 5V_MAIN + spare), I²C topology 0x20/0x21/0x60 added
   - Consolidated BOM: MCP23017 ×2, PCA9685, J_SERVO, SW3 added
   - Power_Management: PCA9685 DT overlay, daemon init sequence (all-call disable, homing),
     virtual keypress sequence documented
   - Complete_System_Assembly: expanded from stub to full General Assembly document

---

## Work Done

### Commits

**b4fdd9e — Mechanical restructure:**
- `design/Electronics/Encoder/Design_Spec.md` — §6/§7 electrical detail restored; cross-refs updated
- `design/Mechanical/Rotor_Actuation_Assembly/Design_Spec.md` — new file (full mechanism spec)
- `design/Mechanical/HID_Assembly/Design_Spec.md` — migrated + electrical stripped
- `design/Mechanical/Plugboard_Assembly/Design_Spec.md` — migrated + electrical stripped
- `design/Mechanical/Power_Module/Design_Spec.md` — replaced stub with Controller/Mechanical_Design.md
- `design/Mechanical/Main_Enclosure/Design_Spec.md` — new stub
- `design/Mechanical/Complete_System_Assembly/Design_Spec.md` — new stub (later expanded)
- Deleted via `git rm`: Controller/, Keyboard/, Plugboard/, Encoder/, Stator/, JTAG_Daughterboard/

**436e16a — CM5 virtual keyboard feature:**
- `design/Design_Log.md` — DEC-031 added
- `design/Electronics/Stator/Design_Spec.md` — FR/DR, I²C table, SOURCE_SEL, SERVO_HOME, BOM
- `design/Electronics/Controller/Design_Spec.md` — GPIO/LINK-BETA/I²C updates
- `design/Electronics/Consolidated_BOM.md` — MCP23017 ×2, PCA9685, J_SERVO, SW3
- `design/Software/Linux_OS/Power_Management.md` — PCA9685 DT overlay + daemon init
- `design/Mechanical/Complete_System_Assembly/Design_Spec.md` — expanded to General Assembly

---

## Technical Decisions

### Mechanical Restructure

- `Rotor/Design_Spec.md` stays separate (rotor module = most complex mechanical part)
- `Rotor_Actuation_Assembly/` covers the full stepping mechanism:
  - Keyboard key levers (dangling lever on each of 64 keys)
  - Depression bar (common bar — pushed by key levers OR servo arm)
  - Pivot lever & actuation arm (converts depression to one-step rotor advance)
  - Sprung retention bar (detent spring ensuring full-step snap; original Enigma-style)
  - Carry mechanism (purely mechanical ratchet, original Enigma-style)
- Controller/Mechanical_Design.md content moved to Power_Module/ (user confirmed it described PM)
- JTAG Daughterboard: no separate mechanical assembly; noted as Controller hat in
  Complete_System_Assembly

### CM5 Key Injection Feature (DEC-031)

| Component | Address | Location | Function |
|:---|:---|:---|:---|
| MCP23017 U_EXP1 | 0x20 | Stator | ENC_IN/ENC_OUT monitoring (16 GPIO) |
| MCP23017 U_EXP2 | 0x21 | Stator | KEY_ADDR/KEY_EN/SOURCE_SEL/SYS_RESET_N/SERVO_EN/SERVO_HOME (16 GPIO) |
| PCA9685 U_EXP3 | 0x60 | Stator | Servo PWM driver, Ch0 = 50Hz SERVO_PWM |

- Servo: Miuzei Metal Gearbox 90, 4.8–6V, 5V_MAIN. One 0°→180°→0° sweep = one virtual keypress
- SERVO_HOME: SPST NO momentary switch, active-low, 10kΩ pull-up + 100nF, PCB-mounted on Stator
- SOURCE_SEL: U_EXP2 GPA[6] → Stator CPLD SOURCE_SEL at J4 ENC_OUT entry (0=keyboard, 1=CM5)
- SYS_RESET_N migrated from CM5 GPIO 26 → U_EXP2 GPA[7]; R6 pull-up on Stator = safe default
- ENC_IN/OUT monitoring migrated from CM5 GPIO 4–15 → U_EXP1; 12 GPIO freed
- Total freed: 13 CM5 GPIO (4–15, 26); 13 LINK-BETA pins reassigned (2× 5V_MAIN + spare)
- PCA9685 all-call (0x70) disabled in enigma daemon init via MODE1 register bit 0 = 0
- I²C bus: 0x09, 0x0B, 0x20, 0x21, 0x28, 0x40, 0x45, 0x60 (no conflicts)

---

## Known Correct (do not re-flag)

All items from checkpoint 032 remain correct, plus:

- `design/Mechanical/` folder structure is now assembly-based (NOT PCB-named)
- `Electronics/Encoder/Design_Spec.md` §6 and §7 contain full electrical detail (no longer in mechanical specs)
- Stator has FR-STA-10–13, DR-STA-12–15, U_EXP1/U_EXP2/U_EXP3 in BOM
- Controller GPIO 4–15 and 26 are FREED (noted as such in GPIO table)
- LINK-BETA pins 8/12–24: SYS_RESET_N and ENC buses removed; 5V_MAIN added
- PCA9685 @ 0x60: A5=HIGH, A4–A0=GND (correct address wiring)

---

## Open Items

- `kicad-setup-docs` (pending) — KiCad setup documentation (not started)
- `rotor-single-side` (pending) — JLCPCB single-side placement constraint resolution
- `rotor-detailed-design` (pending, blocked on rotor-single-side) — Rotor detailed design review
- OWI-001: Test coupons per board
- OWI-002: PAS definitions per board
- OWI-003: VHDL pseudo-code and CPLD config plans
- OWI-018: ENIG rib clearway bonding pad

---

## Next Steps

1. **Discuss JLCPCB single-side constraint** — user has a resolution plan; agree approach, update
   Board_Layout.md and Design_Spec accordingly.
2. **Relocate STGC_Generator.py** — move to `Rotor/`, update algorithm (relaxed unique-only).
3. **Launch Rotor review cycle** — deep-dive R1, fix, R2; repeat until 2 consecutive clean passes.
4. **GUI App cross-reference** — add position display note (DEC-027/FR-ROT-09) when spec started.
