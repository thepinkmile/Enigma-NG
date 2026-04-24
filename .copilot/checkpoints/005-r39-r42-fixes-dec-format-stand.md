<overview>
This session continued the Enigma-NG electronics design documentation review cycle, with two parallel goals: (1) apply user-directed changes to Design_Log.md (standardise all DEC formats, add Category field, add DEC-025 for deferred software decision) and Power_Management.md (replace polling daemon with deferred note), and (2) achieve two consecutive clean deep-dive review passes to formally close the Encoder detailed design phase. The approach was to fix R39 findings, run the large DEC standardisation agent, then drive the review cycle (R40→R41→R42→R43) to completion, fixing each round's findings before the next pass.
</overview>

<history>
1. **User requested DEC Category field + format consistency**
   - User asked all DEC entries to have a Category field; all existing ones = "Electrical", new DEC-025 = "Software"
   - User also requested all DEC formats be made consistent for future readers
   - User confirmed they were going out for a few days and wanted fully autonomous completion
2. **R39 results read (agent had been running since prior session)**
   - Three genuine findings identified:
     - Cert_Evidence.md §3.1: Iron Curtain filter stages missing from power chain code block
     - User_Manual.md §3.3: Pi-filter described as "on each power path" (wrong — single post-OR-ing bus)
     - Power_Management.md: Phase 1/Phase 2 labels described as reversed (PWR_GD fires first at 4.5V, BACKUP second at 4.40V)
   - User clarified Finding #1: the timing discrepancy is intentional/acceptable — system runs 15-30 min before outage, shutdown is best-effort only; document this in User Manual and don't fix Phase labels
   - Fixes applied and committed (`6fa56c5`): Cert_Evidence iron curtain chain, User_Manual Pi-filter wording, User_Manual §3.6 expanded supercap/shutdown note
3. **DEC standardisation + DEC-025 + Power_Management.md update**
   - First attempt to save agent prompt via PowerShell failed (directory not created)
   - Created `.copilot/agent-prompts/` directory, saved prompt as `dec-standardise-prompt.txt`
   - Agent `dec-standardise-v2` ran successfully and committed (`dfc7118`):
     - All DEC-001–DEC-024 reformatted to canonical dash-list metadata + ### section headings
     - Category: Electrical added to all existing DECs
     - DEC-025 added (Category: Software, deferred to Software PoC stage)
     - Power_Management.md Overview corrected (PWR_GD first, BACKUP second)
     - Phase 1 polling daemon replaced with deferred-decision note + I2C reference table
     - Shutdown Timing Budget row updated

4. **R40 review — first clean pass attempt**
   - One finding: Controller/Board_Layout.md LINK-ALPHA ASCII diagram pins 25-26 labelled `[2oz POWER]` (bleed from GND block above); should be `[3.3V LOGIC]`
   - Fixed and committed (`fe0d2b5`)
   - R41 launched immediately
5. **R41 review — second clean pass attempt**
   - Three findings:
     - Consolidated_BOM.md: SN74LVC2G125DCUR had EXT=1 (wrong column; should be JDB=1)
     - JTAG_Integrity.md §9: referenced "33 Ω 0603 Controller R4-R6" (stale; should be "33 Ω 0402 JDB R6-R8")
     - Design_Log.md DEC-016: strikethrough text said "74LVC1G125" (single-channel); correct is "74LVC2G125" (dual-channel)
   - All three fixed and committed (`01c9913`)
6. **R42 review — new first clean pass attempt**
   - Two findings:
     - Consolidated_BOM.md: R41 fix had placed the SN74LVC2G125DCUR count in the EXT column rather than the JDB column (positional error in the edit)
     - JTAG_Integrity.md §7.4 and trace table: two "See DEC-023" cross-refs should be "See DEC-024" (DEC-023 = JDB grounding decision; DEC-024 = JTAG master/Controller pass-through decision)
   - Both fixed and committed (`6cbb40c`)
   - R43 prompt saved to `.copilot/agent-prompts/r43-review-prompt.txt`
   - R43 agent launched — running at time of compaction
</history>

<work_done>
Files modified this session:

- `design/Standards/Certification_Evidence.md` — §3.1 power chain: L1 CMC → L2 CMC → L3+C Pi-filter stages added between OR-ing and TCO F1
- `design/Guides/User_Manual.md` — §3.3: Pi-filter wording fixed; §3.6: supercap note expanded with 15-30 min uptime and best-effort shutdown intent
- `design/Design_Log.md` — All DEC-001–DEC-024 reformatted to canonical format; Category field added to all; DEC-025 added; DEC-016 strikethrough text fixed (74LVC1G125 → 74LVC2G125)
- `design/Software/Linux_OS/Power_Management.md` — Overview corrected (PWR_GD fires first); Phase 1 polling daemon replaced with deferred note + DEC-025 reference; Shutdown Timing Budget row updated
- `design/Electronics/Controller/Board_Layout.md` — LINK-ALPHA ASCII diagram pins 25-26: `[2oz POWER]` → `[3.3V LOGIC]`
- `design/Electronics/Consolidated_BOM.md` — SN74LVC2G125DCUR row: corrected to JDB=1, EXT=—, Total=1
- `design/Electronics/Investigations/JTAG_Integrity.md` — §9: 33 Ω reference updated to 0402 JDB R6-R8; §7.4 and trace table: two DEC-023 → DEC-024 cross-ref fixes
- `.copilot/agent-prompts/dec-standardise-prompt.txt` — Created (DEC standardisation instructions)
- `.copilot/agent-prompts/r42-review-prompt.txt` — Created (R42 review prompt)
- `.copilot/agent-prompts/r43-review-prompt.txt` — Created (R43 review prompt)

Commits this session:
- `6fa56c5` — R39 fixes (3 findings)
- `dfc7118` — DEC standardisation + DEC-025 + PM deferred note
- `fe0d2b5` — R40 fix (1 finding)
- `01c9913` — R41 fixes (3 findings)
- `6cbb40c` — R42 fixes (2 findings)

Work completed:
- [x] R39 findings applied
- [x] User Manual §3.6 supercap/shutdown best-effort note
- [x] DEC-001–DEC-024 format standardised
- [x] Category field added to all DECs
- [x] DEC-025 added (Software category, deferred to PoC)
- [x] Power_Management.md Phase 1 replaced with deferred note
- [x] R40 finding fixed
- [x] R41 findings fixed
- [x] R42 findings fixed
- [ ] R43 clean pass — agent running at compaction
- [ ] R43 second consecutive clean pass (R44) — pending R43 result
- [ ] Encoder marked complete in Design_Log
- [ ] Checkpoint 004 saved to `.copilot/checkpoints/`
- [ ] `.copilot/plan.md` updated
- [ ] Begin Rotor detailed design review
</work_done>

<technical_details>
**DEC canonical format (now applied to all entries):**
```
## DEC-NNN — Title
- **Status:** value
- **Date:** value
- **Category:** Electrical (or Software for DEC-025)
- **Area:** value
### Decision
### Rationale
### Impact (optional)
### Alternatives Considered (optional)
---
```

**DEC-025 — CM5 Shutdown Mechanism (Software, Deferred):**
- Final implementation: custom Linux kernel driver using LTC3350 BACKUP signal as hardware interrupt
- PWR_GD (GPIO 27, gpio-shutdown overlay) remains the active interim backstop
- Deferred to Software PoC stage — hardware must be available for testing
- Do NOT flag polling latency, POLL_HZ, or daemon specifics — all replaced/deferred

**Power_Management.md shutdown signal order (CORRECT as of dfc7118):**
- PWR_GD fires FIRST at 5V_MAIN < 4.5V (~10ms after mains loss)
- LTC3350 BACKUP fires SECOND at 5V_MAIN < 4.40V (shortly after PWR_GD)
- Hold-up window (≥21.7s) begins when BACKUP asserts
- R39 Finding #1 (Phase label reversal) was explicitly NOT fixed per user direction — timing gap is acceptable because system runs 15-30 min before any outage

**SN74LVC2G125DCUR BOM placement (CORRECT as of 6cbb40c):**
- JDB=1, EXT=—, CTL=—, Total=1
- Per DEC-024: moved from Controller to JDB only; never on Extension board

**JTAG_Integrity.md DEC cross-refs (CORRECT as of 6cbb40c):**
- DEC-023 = JDB GND_CHASSIS omitted (grounding decision)
- DEC-024 = JDB is complete JTAG master; Controller is pass-through
- §7.4 and trace table references to Controller pass-through must cite DEC-024, not DEC-023

**Agent prompt JSON escaping issue:**
- The `task` tool fails with "Unterminated string in JSON" when the prompt contains backtick characters
- Workaround: save prompt to a `.txt` file in `.copilot/agent-prompts/` and reference it in the agent prompt
- The `.copilot/agent-prompts/` directory must be explicitly created first (New-Item)

**Review cycle rules:**
- Two consecutive clean passes required to close the Encoder detailed design phase
- Each pass reads all ~17 files in full
- R42 was the first pass after all fixes; R43 (currently running) needs to be clean; then R44 must also be clean
- Known false positives list must be maintained and passed to each review agent

**Stale values never to reappear:**
- TPS259807ONRGER (wrong eFuse; correct = TPS259804ONRGER)
- ERA-3ARB2100V 0.1% thin-film for R_ILIM (wrong; correct = ERJ-3EKF2100V 1% thick-film)
- 74LVC1G125 (single-channel; correct = 74LVC2G125 dual-channel)
- EXT column for SN74LVC2G125DCUR (not on Extension board)
- DEC-023 for Controller JTAG pass-through (should be DEC-024)

**Session state location:** repo-local `.copilot\`
Resume phrase: "Please read `.copilot/plan.md` and all files in `.copilot/checkpoints/` to align yourself with the current project state, then continue from where we left off."
</technical_details>

<important_files>
- `design/Design_Log.md`
  - Master decision log; source of truth for all DEC entries
  - All DEC-001–DEC-024 reformatted; Category field added; DEC-025 added; DEC-016 strikethrough fixed
  - DEC-025 is at the end before ## Open Questions section
- `design/Software/Linux_OS/Power_Management.md`
  - CM5 shutdown mechanism documentation
  - Phase 1 now a deferred-decision note (no polling code); Overview corrected; Timing Budget updated
  - All Python daemon code removed from Phase 1 — this is correct and intentional
- `design/Electronics/Consolidated_BOM.md`
  - System-wide component usage table
  - SN74LVC2G125DCUR: now correctly shows JDB=1, EXT=—, Total=1
- `design/Electronics/Investigations/JTAG_Integrity.md`
  - Full JTAG signal integrity investigation
  - §9 cost table: 33 Ω now references 0402 JDB R6-R8 (not 0603 CTL R4-R6)
  - §7.4 and trace table: DEC-023 → DEC-024 for Controller pass-through cross-refs
- `design/Electronics/Controller/Board_Layout.md`
  - Controller board layout including LINK-ALPHA ASCII diagram
  - Pins 25-26 signal type fixed to [3.3V LOGIC]
- `design/Standards/Certification_Evidence.md`
  - §3.1 power chain now correctly includes L1 CMC → L2 CMC → L3+C Pi-filter stages
- `design/Guides/User_Manual.md`
  - §3.3: Pi-filter topology corrected; §3.6: supercap/shutdown intent documented
- `.copilot/agent-prompts/r43-review-prompt.txt`
  - R43 review prompt — already passed to the running r43-review agent
  - Contains full KNOWN CORRECT list updated through R42 fixes
</important_files>

<next_steps>
Immediate (R43 agent running):
- Read R43 results when agent completes
- If R43 clean → launch R44 immediately (second consecutive clean pass needed)
- If R43 has findings → fix all, commit, then restart consecutive clean pass count with R44+R45

After two consecutive clean passes:
1. Add entry to Design_Log.md marking Encoder detailed design phase complete (INC or narrative note)
2. Update `.copilot/plan.md`: Encoder → complete, next phase = Rotor detailed design review
3. Save checkpoint 004 to `.copilot/checkpoints/004-encoder-complete-review-cycle-closed.md`
4. Update `.copilot/checkpoints/index.md` with checkpoint 004 entry
5. Begin Rotor detailed design review

Open questions (none blocking — user away, working autonomously):
- None; all user questions answered before they left
</next_steps>
