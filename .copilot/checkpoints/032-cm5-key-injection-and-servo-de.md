Good. All existing mechanical files are either **stubs** (empty placeholder) or have real content. Here's the assessment before I write the summary:

**Files with real content:**
- `Keyboard/Design_Spec.md` → moves to `HID_Assembly`
- `Rotor/Design_Spec.md` → moves to `Rotor_Actuation_Assembly`
- `Plugboard/Design_Spec.md` → moves to `Plugboard_Assembly` (direct rename)

**Pure stubs — no content to migrate, just delete:**
- `Stator/Design_Spec.md` — Stator PCB is the rotor stack backplane → logical home is `Rotor_Actuation_Assembly`
- `Encoder/Design_Spec.md` — Encoder PCB is part of keyboard/lightboard → logical home is `HID_Assembly`
- `Reflector/Design_Spec.md` — kept as-is (stub, direct carry-over)
- `Extension/Design_Spec.md` — kept as-is (stub, direct carry-over)
- `Power_Module/Design_Spec.md` — kept as-is (stub, direct carry-over)

**One item needing your decision:**
- `JTAG_Daughterboard/Design_Spec.md` — stub only. The JDB physically mounts on the Controller board. There's no Controller folder in the current mechanical structure, and no "Controller" in your proposed new structure either. The JDB + Controller board assembly would logically live in `Main_Enclosure`. Do you agree, or would you like a separate `Controller_Assembly` entry?

---

Now writing the full checkpoint summary:

<overview>
This session had two major work streams: (1) completing the Power Module backup transient fix and 2S4P supercap upgrade across all design documents, and (2) designing a new "CM5 autonomous key injection" feature for the Enigma-NG that allows the CM5 to programmatically inject keypresses, enabling automated rotor configuration testing and fully autonomous cipher operation. A mechanical design restructuring of the `design/Mechanical/` folder was also requested at the end of the session and is pending implementation.
</overview>

<history>

1. **Background agent completed commit `acae80d`** (from prior session) and the user confirmed readiness to proceed
   - Commit `acae80d` had already applied: eFuse variant lock blocks, Extension U1 root cause fix, supercap stale value sweep, DEC-029 creation

2. **User confirmed: proceed with all pending PM transient fix changes**
   - Launched background agent `pm-changes-commit` to implement all pending work
   - While agent ran, user introduced a new feature idea

3. **New feature: CM5 autonomous key injection**
   - User wants CM5 to be able to inject virtual keypresses for: rotor config testing, autonomous cipher operation, eliminating human error
   - Initial analysis: feasibility confirmed; I2C GPIO expander on Stator is the right approach
   - Established: 6 injection pins (5-bit KEY_ADDR + KEY_EN) + dedicated SOURCE_SEL pin
   - User decided: 2× MCP23017 (32 GPIO total) for headroom, not 1×

4. **Motor requirement identified**
   - User raised need for a motor to actuate the mechanical stepping mechanism
   - Initial incorrect assessment by assistant (said no motor needed because CPLD handles stepping digitally)
   - Corrected after reading rotor mechanical spec: rotors have PHYSICALLY rotating aluminium shrouds read by capacitive encoders — CPLD reads actual encoder position, not a software counter. Motor IS required.
   - Mechanical design (not yet documented): each key press pushes a bar via a dangling lever; the bar connects to a pivot/lever that advances the rotor one step — identical to original Enigma mechanism; servo drives the same bar

5. **Servo motor selection**
   - User has Miuzei Metal Gearbox 90 servo motors (6V/2500RPM, purchased from Amazon)
   - Confirmed 4.8–6V rated → 5V_MAIN is within spec ✓
   - Control approach: 0°→180°→0° per virtual keypress (one mechanical actuation cycle)
   - PWM required → MCP23017 cannot do PWM → add **PCA9685** I²C PWM driver
   - PCA9685 address: **0x60** (user requested "further down" address space for I2C debugging clarity)
   - All-call disable (MODE1 bit 0): done in enigma daemon init, not DT or separate systemd service

6. **SERVO_HOME switch**
   - User requested a homing switch (like 3D printer endstop) to detect servo 0° position
   - SPST normally-open momentary switch, active-low, on Stator PCB (servo is locally mounted on Stator)
   - RC debounce: 10kΩ pull-up + 100nF (same as keyboard switches)
   - Assigned to MCP23017 U_EXP2 GPB[1]

7. **Mechanical design confirmed by user**
   - Servo mounted on Stator board
   - Keyboard keys have dangling levers pushing a common bar at enclosure base
   - Bar connects to lever/pivot → advances rotor stack one step
   - Servo drives same bar → replaces keyboard actuation for CM5 virtual keypresses
   - Carry mechanism is purely mechanical (as per original Enigma)

8. **Background agent completed — commit `6fe5341` confirmed**
   - All PM transient fix and 2S4P cascade changes applied and committed

9. **Mechanical folder restructuring requested**
   - User noted current `design/Mechanical/` structure (PCB-named folders) is misleading
   - Requested new assembly-based structure (see next steps)
   - All existing files assessed: 3 have real content, 6 are pure stubs

</history>

<work_done>

Files committed in `6fe5341`:
- `design/Design_Log.md` — DEC-030 added (5V_MAIN backup transient fix: R14/R30/C35, full analysis, component selection rationale, T495 rejected, HZA not selected)
- `design/Electronics/Power_Module/Design_Spec.md` — DR-PM-08 updated (R14 30.1kΩ), DR-PM-10 (C35) and DR-PM-11 (R30) added, 2S4P cascade throughout, BOM updated
- `design/Electronics/Power_Module/Board_Layout.md` — 2×4 supercap grid, 41×81mm shadow zone
- `design/Guides/User_Manual.md` — 8 cells/50F/33.5s/9 min
- `design/Software/Linux_OS/Power_Management.md` — ≥33.5s (×2)
- `design/Electronics/Boards_Overview.md` — 50F/8×/2S4P/33.5s
- `design/Standards/Certification_Evidence.md` — ≥33.5 seconds
- `design/Electronics/Consolidated_BOM.md` — C_SC qty 8, R14 updated, R30 and C35 added

Work completed:
- [x] DEC-030 created with full transient analysis and component selection decisions
- [x] 2S4P cascade applied across all 8 files
- [x] R14 → 30.1kΩ, R30 = 33.2kΩ, C35 = 2× Samsung CL32B226KAJNNNE
- [x] C35 component selection documented (T495 rejected — fails; HZA not selected — existing BOM part sufficient)
- [x] Unwanted datasheets (HZA, T495) removed from disk
- [x] New feature fully designed (all decisions confirmed, no blockers)
- [ ] New feature not yet documented in design files
- [ ] Mechanical folder restructuring not yet implemented

</work_done>

<technical_details>

**PM Transient Fix (committed):**
- 5V_MAIN bulk: C9+C10+C13 = 54µF. Old gap to PWR_GD = 144mV → 2.59µs = 0.52 LTC3350 cycles at 200kHz → FAILS
- Fix: R14→30.1kΩ (gap→312mV) + R30=33.2kΩ (LTC3350 400kHz) + C35=44µF → 98µF×312mV/3A = 10.2µs = 4.1 cycles ✓
- C35 = 2× Samsung CL32B226KAJNNNE (22µF 25V X7R 1210) — existing BOM part

**2S4P Supercap (committed):**
- 8× Abracon ADCR-T02R7SA256MB, 50F at 5.4V, ≥33.5s hold-up at 15W load (CM5 5V×3A)
- Stale values that must NEVER reappear: 2S3P, 37.5F, 6 cells, 24.8s, 5W load, 3 min charge

**CM5 Key Injection Feature (designed, not yet documented):**
- I²C expander architecture on Stator board:
  - U_EXP1: MCP23017 @ 0x20 — GPA[0:5]=ENC_IN monitor (inputs), GPB[0:5]=ENC_OUT monitor (inputs), 4 spare
  - U_EXP2: MCP23017 @ 0x21 — GPA[0:4]=KEY_ADDR[0:4] (out), GPA[5]=KEY_EN (out), GPA[6]=SOURCE_SEL (out), GPA[7]=SYS_RESET_N (out), GPB[0]=SERVO_EN (out), GPB[1]=SERVO_HOME (in), GPB[2:7]=spare
  - U_EXP3: PCA9685 @ 0x60 — Ch0=SERVO_PWM (50Hz); A5→3V3_ENIG, A4–A0→GND; all-call disabled in daemon init
- Servo: Miuzei Metal Gearbox 90, 4.8–6V (5V_MAIN), 0°→180°→0° per virtual keypress
- SERVO_HOME: SPST NO switch, active-low, PCB-mounted on Stator, 10kΩ pull-up + 100nF debounce
- Servo + SERVO_HOME switch physically local to Stator board (no harness needed)
- Homing sequence: assert SERVO_EN → command 0° → poll SERVO_HOME → confirm LOW within timeout
- CPLD change needed: SOURCE_SEL MUX added to Stator CPLD VHDL at J4 ENC_OUT[0:5] entry point
- SYS_RESET_N migrated from CM5 GPIO 26 to expander; R6 pull-up on Stator keeps it HIGH at power-up (safe)
- ENC_IN/ENC_OUT monitoring moved from CM5 GPIO 4–15 → expander (frees 12 CM5 GPIO)
- Total freed: 13 CM5 GPIO (4–15 and 26), 13 LINK-BETA pins
- 5V_MAIN must be added to LINK-BETA (2 pins) using freed slots — servo power
- PCA9685 all-call at 0x70 must be disabled: CM5 writes MODE1 register bit 0 = 0 during daemon init; NOT via DT
- I²C bus has no conflicts: 0x09, 0x0B, 0x20, 0x21, 0x28, 0x40, 0x45, 0x60

**Mechanical stepping mechanism (user described, not yet documented):**
- Physical rotors: aluminium shroud physically rotates; CPLD reads Gray code capacitive encoder for actual position
- Motor is REQUIRED (not just a software counter increment)
- Keyboard levers push a common bar → pivot/lever → advances rotor stack one step (identical to original Enigma)
- Servo drives same bar as keyboard → one full 0°→180°→0° sweep = one rotor step
- Carry mechanism is purely mechanical (original Enigma-style ratchet notch)

**Mechanical folder — existing file content assessment:**
- `Keyboard/Design_Spec.md`: real content (DPDT switches, key mapping, RC debounce) → moves to `HID_Assembly`
- `Rotor/Design_Spec.md`: real content (shroud, bearings, encoder slots, assembly) → moves to `Rotor_Actuation_Assembly`
- `Plugboard/Design_Spec.md`: real content (¼" jacks, Stecker interface) → moves to `Plugboard_Assembly`
- `Stator/`, `Encoder/`, `JTAG_Daughterboard/`, `Reflector/`, `Extension/`, `Power_Module/`: all pure stubs — delete; their components are acknowledged within new assembly files
- OPEN DECISION: JDB + Controller board mechanical details → user confirmed they go in `Main_Enclosure` (no separate Controller_Assembly needed — awaiting explicit confirmation)

</technical_details>

<important_files>

- `design/Design_Log.md`
  - Contains all DECs including DEC-029 (2S4P supercap), DEC-030 (PM transient fix)
  - New DEC-031 needed for CM5 key injection feature
  - New DEC for mechanical restructuring may be needed

- `design/Electronics/Stator/Design_Spec.md`
  - Primary file needing updates for new feature: add 3× I²C expanders to BOM and FR/DR, add SOURCE_SEL MUX note to CPLD section, add servo connector and SERVO_HOME switch, add 5V_MAIN to LINK-BETA pin table
  - I²C table needs 0x20, 0x21, 0x60 entries

- `design/Electronics/Controller/Design_Spec.md`
  - GPIO table needs updating: GPIO 4–15 freed (ENC monitoring → expander), GPIO 26 freed (SYS_RESET_N → expander)
  - LINK-BETA pin table: remove 12 monitoring pins, remove SYS_RESET_N pin, add 2× 5V_MAIN pins
  - I²C bus topology table: add 0x20, 0x21, 0x60

- `design/Electronics/Consolidated_BOM.md`
  - Add: 2× MCP23017T-E/SO (SOIC-28), 1× PCA9685 (SSOP-28), 1× SPST micro switch (SERVO_HOME), 1× servo connector (3-pin), servo motor note
  - Update: LINK-BETA pin allocation narrative

- `design/Software/Linux_OS/Power_Management.md`
  - Add: PCA9685 DT overlay config (pwm-pca9685 at 0x60, 50Hz)
  - Add: Enigma daemon hardware init sequence (ALLCALL disable, MODE1 config, SERVO_HOME homing sequence)

- `design/Mechanical/` (entire folder restructure pending)
  - Current: 9 files, 3 with content, 6 pure stubs
  - Target: Power_Module, Extension, Reflector, Rotor_Actuation_Assembly, HID_Assembly, Plugboard_Assembly, Main_Enclosure, Complete_System_Assembly

</important_files>

<next_steps>

**Immediate blocker to resolve first:**
- Confirm: JDB + Controller board mechanical details → `Main_Enclosure`? (user has not explicitly confirmed yet)

**Implementation order once confirmed:**

1. **Mechanical folder restructure:**
   - Create new folders: `Rotor_Actuation_Assembly`, `HID_Assembly`, `Plugboard_Assembly`, `Main_Enclosure`, `Complete_System_Assembly`
   - Migrate: `Keyboard/` → `HID_Assembly/`; `Rotor/` → `Rotor_Actuation_Assembly/`; `Plugboard/` → `Plugboard_Assembly/`
   - Delete stubs: `Stator/`, `Encoder/`, `JTAG_Daughterboard/`
   - Keep stubs: `Reflector/`, `Extension/`, `Power_Module/`
   - Add servo/stepping mechanism description to `Rotor_Actuation_Assembly/Design_Spec.md`

2. **DEC-031 in Design_Log.md** — CM5 key injection feature decision (architecture, component selection, I²C addresses, servo choice)

3. **Stator Design_Spec.md** — Add FR/DR for expanders, PCA9685, SERVO_HOME, SOURCE_SEL MUX, 5V_MAIN on LINK-BETA, servo connector

4. **Controller Design_Spec.md** — GPIO table (free 13 pins), LINK-BETA pin table (remove 13, add 5V_MAIN), I²C topology table (add 0x20, 0x21, 0x60)

5. **Consolidated_BOM.md** — Add MCP23017 ×2, PCA9685, SERVO_HOME switch, servo connector

6. **Power_Management.md** — PCA9685 DT overlay + daemon init sequence

7. **markdownlint fix → clean check → git commit**

8. Create checkpoint 032

</next_steps>