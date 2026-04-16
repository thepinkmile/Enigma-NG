<overview>
This session continued the Enigma-NG electronics design documentation review cycle with two parallel goals: (1) achieve two consecutive clean review passes to close the current review cycle, and (2) address user clarifications about software implementation intent. The approach used background review agents (R33–R39) with careful false-positive filtering and direct surgical fixes between each round. The user clarified that all Python daemon code in Power_Management.md is placeholder only — the real shutdown implementation will be interrupt-driven via a custom Linux driver, deferred to the software PoC stage.
</overview>

<history>
1. **Session resumed with R38 results already in** — 3 findings fixed and committed (`a5fa1b5`):
   - User_Manual L2 "differential" → "common-mode"
   - Cert_Evidence L2 row: "differential/common-mode 1kHz–30MHz" → "supplementary CM attenuation >10MHz; L1+L2 pair covers 1kHz–30MHz"
   - PM Board_Layout: removed L2 from USB-C per-input path; added L1→L2→L3 filter stage post-OR-ing in Power Flow ASCII

2. **R39 launched** (still running when compaction triggered) — clean pass attempt 1

3. **User asked about "shutdown daemon latency"** — explained the POLL_HZ=2 / ≤510ms change made autonomously overnight

4. **User clarified software intent:**
   - The shutdown will NOT use polling — a custom Linux driver will use the BACKUP signal as a hardware interrupt
   - Explicitly stated: do not get hung up on software or mechanical specifics; these will be defined during the PoC stage
   - Requested that the polling implementation be replaced with a note that this is deferred to the software PoC stage
   - Requested a DEC entry in Design_Log.md marking this as a deferred design decision

5. **Summary/compaction requested** — capture full state before context window clears
</history>

<work_done>
Commits this session (since prior checkpoint `003`):

- `479b261` — R33 fixes: PM voltage/rib-width consistency (4 findings)
  - Board_Layout §Power Flow: 7-17V → 11–16.9V pre-reg label
  - Board_Layout §Power Flow: ENIG strip 1.0mm → 1.5mm
  - Design_Spec §4 Iron Curtain: 17V → 16.9V voltage margin
  - Design_Spec §3.2 Startup Timeline: 11–17V → 11–16.9V

- `b9acd79` — R34 fixes: INA219 rotor code corrections
  - CONFIG_VALUE: 0x219F (PGA/1 ±40mV wrong) → 0x9F29 (byte-swapped 0x299F = PGA/2 ±80mV)
  - CAL write: 0x0400 → 0x0004 (big-endian swap for smbus2)
  - Current read: added byte-swap consistent with PM INA219 code

- `942e8d0` — R35 fixes: Design_Log DEC-014/015 narrative + INA219 Firmware Note
  - DEC-014 body: J2 corrected ERF8-040→ERF8-020; Stator J1→J8; ERM8-040→ERM8-020
  - DEC-015 Affects: Stator Board J1→J8
  - Power_Management Firmware Note: CAL prose updated to cite 0x0004 (not 0x0400)

- `6e60ebc` — R36 fixes: DEC cross-ref, supercap per-cell F, PM INA219 CONFIG write
  - Controller Design_Spec §2.1: DEC-007→DEC-014
  - PM Board_Layout ASCII: 33F×6 cells → 22F×6 cells (22F/cell; 33F is total bank)
  - Power_Management PM INA219: added missing CONFIG write (0x9F31 = PGA/4 ±160mV)

- `b3ec41b` — R37 fix: Rotor J2 ERM8 pin current 2.2A/pin → 0.5A/pin
  - Rotor Design_Spec §3.4: 5 pins × 0.5A/pin = 2.5A (system-wide Samtec derating)

- `a5fa1b5` — R38 fixes: L1/L2 CMC topology, CM vs differential labels
  - User_Manual §3.3: L2 "differential" → "common-mode"
  - Cert_Evidence §4.1: L2 row corrected
  - PM Board_Layout: L2 removed from USB-C path; L1→L2→L3 added post-OR-ing

**Pending (not yet committed):**
- [ ] Update Power_Management.md to replace polling daemon with interrupt-driven placeholder note
- [ ] Add DEC entry to Design_Log.md for deferred shutdown mechanism decision
- [ ] R39 results not yet read (agent still running at compaction)
- [ ] 2 consecutive clean passes still needed
- [ ] Encoder marked complete in Design_Log
- [ ] Checkpoint `004` saved to `.copilot/checkpoints/`
- [ ] `.copilot/plan.md` updated
</work_done>

<technical_details>
**eFuse — TPS259804ONRGER IS CORRECT. NEVER flag.**
- Silicon-fixed 16.9V OVLO; R3 = R_ILIM = 210Ω ERJ-3EKF2100V (1% thick-film)
- Battery max 16.4V (4.1V/cell × 4); input window 11–16.9V
- FALSE POSITIVE: ERA-3ARB2100V / 0.1% thin-film for R_ILIM — always discard

**INA219 smbus2 byte-swap pattern (CRITICAL)**
- smbus2 `write_word_data` sends LSB first (little-endian); INA219 expects big-endian (MSB first)
- To write logical value V to INA219: pass byte-swapped value = `((V & 0xFF) << 8) | (V >> 8)`
- To read: apply `raw = ((raw & 0xFF) << 8) | ((raw >> 8) & 0xFF)` after read_word_data
- Rotor INA219 CONFIG: logical 0x299F (PGA/2 ±80mV) → smbus2 value 0x9F29
- Rotor INA219 CAL: logical 0x0400 (1024) → smbus2 value 0x0004
- PM INA219 CONFIG: logical 0x319F (PGA/4 ±160mV) → smbus2 value 0x9F31
- PM INA219 CAL: logical 0x0200 (512) → smbus2 value 0x0002

**INA219 CONFIG bit fields (from MSB):**
- bit 13: BRNG (1=32V bus range)
- bits[12:11]: PG — 00=÷1(±40mV), 01=÷2(±80mV), 10=÷4(±160mV), 11=÷8(±320mV, default)
- bits[10:7]: BADC (0011=12-bit)
- bits[6:3]: SADC (0011=12-bit)
- bits[2:0]: MODE (111=shunt+bus continuous)

**PM filter topology (L1, L2, L3 ALL post-OR-ing on VIN_RAW)**
- L1 CMC (Würth WE-CMBNC) → L2 CMC (Würth WE-CMBNC) → L3+C1–C6 Pi-filter
- CMCs attenuate common-mode noise; Pi-filter attenuates differential noise
- L1+L2 pair together covers 1kHz–30MHz CM; L2 alone covers >10MHz supplementary
- L1 and L2 are NOT per-input filters; they are NOT in the PoE or USB-C per-input paths

**Power_Management.md software intent (USER CLARIFICATION)**
- All Python daemon code is PLACEHOLDER only — not the final implementation
- Real shutdown will use a custom Linux driver treating BACKUP signal as hardware interrupt
- This is DEFERRED to the software PoC stage (pending hardware availability for testing)
- Do NOT treat POLL_HZ, timing latency, or any daemon specifics as requirements

**DEC numbering (current)**
- DEC-020 = PM rib clearway
- DEC-021 = Supercap bank 2S3P
- DEC-022 = JDB crystal clock
- DEC-023 = JDB GND_CHASSIS
- DEC-024 = JDB JTAG buffer/master
- Next available: DEC-025 (for shutdown mechanism deferred decision)

**Encoder two-half architecture (correct)**
- Decode Half (U1/CPLD A): ENC_IN[0:5] → 64 lines → BT1–64
- Encode Half (U2/CPLD B): BT65–128 → 64 lines → ENC_OUT[0:5]
- J2 is ONLY inter-half connection (power + both 6-bit buses + JTAG)
- JTAG chain: J2 TDI → U1 → R7(33Ω) → U2 → R8(75Ω) → J2 TDO
- Jack: Tip+Switch → BT1–64; Sleeve → BT65–128; max 32 cables
- Keystone 1285-ST: Mouser 534-1285-ST, DigiKey 36-1285-ST-ND, JLCPCB C5370868

**Supercap bank**
- 6× Tecate TPLH-2R7/22WR12X31; 22F/2.7V per cell; 2S3P = 33F/5.4V total
- PM Board_Layout ASCII: `(22F×6 cells, 2S3P)` — 33F is TOTAL not per-cell

**Samtec ERM8/ERF8 derating**
- 0.5A/pin system-wide (per Cert_Evidence §5, Controller Board_Layout, PM DR-PM-02)
- Rotor J2 (ERM8-005): 5 pins × 0.5A/pin = 2.5A capacity

**Canonical session state**
- Lives at repo-local `.copilot\`
- Resume phrase: "Please read `.copilot/plan.md` and all files in `.copilot/checkpoints/` to align yourself with the current project state, then continue from where we left off."

**Review cycle lint method**
- `ide-get_diagnostics` ONLY — Node.js not reliably on PATH
- Two consecutive clean passes required to close the Encoder detailed design phase

**Board_Layout ASCII edits**
- The `edit` tool often fails on ASCII art due to leading-space mismatches
- Use PowerShell `(Get-Content -Raw) -replace ... | Set-Content -NoNewline` for ASCII blocks
- Use regex `-replace` for multi-line blocks with CRLF line endings

**False positive patterns (always filter)**
- TPS259804ONRGER → never flag (correct eFuse)
- ERJ-3EKF2100V / 1% thick-film for R_ILIM → never flag (correct)
- ERA-3ARB2100V / 0.1% thin-film for R_ILIM → always discard
- DEC-010 "deferred" status → correct, not stale
</technical_details>

<important_files>
- `design/Design_Log.md`
  - Master log of DEC/INC/QUE entries; cross-reference source of truth
  - DEC-014/015 narrative fixed (connector designators and part numbers)
  - Needs new DEC-025 entry for deferred shutdown mechanism decision

- `design/Electronics/Power_Module/Design_Spec.md`
  - Core PM spec; eFuse, supercap, filter topology
  - Fixed: 17V → 16.9V in §4 and §3.2; rib clearway 1.0mm → 1.5mm

- `design/Electronics/Power_Module/Board_Layout.md`
  - PM board layout including Power Flow and input source ASCII diagrams
  - Fixed: pre-reg label 7-17V → 11–16.9V; 33F×6 → 22F×6; L1/L2 moved post-OR-ing; L2 removed from USB-C path

- `design/Electronics/Encoder/Design_Spec.md`
  - Fully rewritten earlier in session (two-half architecture)
  - Stale ESD bullet removed in §8

- `design/Electronics/Rotor/Design_Spec.md`
  - J2 pin current fixed: 2.2A/pin → 0.5A/pin = 2.5A capacity

- `design/Electronics/Controller/Design_Spec.md`
  - §2.1 DEC cross-ref: DEC-007 → DEC-014
  - (DEC-TBD) correctly annotated for 3V3_ENIG tap

- `design/Software/Linux_OS/Power_Management.md`
  - Contains placeholder Python daemon code (NOT final implementation)
  - INA219 rotor code fixed: CONFIG 0x9F29, CAL 0x0004, byte-swap on read
  - PM INA219 code fixed: CONFIG write 0x9F31 added; Firmware Note updated
  - NEEDS UPDATE: replace polling daemon section with interrupt-driven placeholder + DEC-025 reference

- `design/Guides/User_Manual.md`
  - L2 description fixed: "differential" → "common-mode"

- `design/Standards/Certification_Evidence.md`
  - L2 row in §4.1 fixed: correct CM-only description

- `.copilot/plan.md`
  - Canonical session plan (in repo root, gitignored)
  - Needs updating after clean passes and checkpoint save

- `.copilot/checkpoints/index.md`
  - Needs checkpoint `004` entry after clean passes complete
</important_files>

<next_steps>
**Immediate — pending user clarification commit:**
1. Update `Power_Management.md` — replace the POLL_HZ polling daemon with a high-level placeholder note that the shutdown mechanism will be interrupt-driven via a custom Linux driver, deferred to software PoC stage
2. Add `DEC-025` to `Design_Log.md` — "CM5 Shutdown Mechanism: Interrupt-Driven via Custom Linux Driver (Deferred to Software PoC)"
3. Commit both changes

**Review cycle — still need 2 consecutive clean passes:**
4. Read R39 results (agent was running at compaction — check immediately on resume)
5. If R39 clean → launch R40 (second consecutive clean pass needed)
6. If R39 has findings → fix, then continue until 2 consecutive clean passes

**After two consecutive clean passes:**
7. Add Design_Log entry marking Encoder detailed design complete
8. Update `.copilot/plan.md`: Encoder → complete, next phase = Rotor detailed design review
9. Save checkpoint `004` to `.copilot/checkpoints/`
10. Update `.copilot/checkpoints/index.md`
11. Begin Rotor detailed design review

**Open questions (none blocking):**
- None — user has clarified all pending questions
</next_steps>
