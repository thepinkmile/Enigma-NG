<overview>
This session continued the Enigma-NG electronics design documentation review cycle, targeting two consecutive clean deep-dive review passes to formally close the Encoder detailed design phase. The approach was to fix each round's findings, commit, then re-run until two successive passes returned zero findings. The session ran rounds R47–R49, applying fixes after each non-clean pass, but also discovered and corrected a serious pre-existing error (R43 wrongly removed the Extension board's JTAG buffer) that was identified by the user on return.
</overview>

<history>
1. **Session resumed with R47 fixes in progress**
   - R47 found 2 issues in Certification_Evidence §3.5: LDO row was 2.20A (should be 2.11A, consistent with §3.4), and total peak was 9.05A (should be 8.76A).
   - Applied all §3.5 fixes: LDO row, total, LMQ utilisation (75.4%→73.0%), eFuse (4.82A/68.9%→4.67A/66.7%), PoE cold-start (54.9W/76.2%→53.2W/73.9%), OA-02 resolution note.
   - Key outcome: correcting the arithmetic **eliminated both "accepted exceptions"** (LMQ and PoE cold-start now within the ≤75% policy — no exceptions anywhere in the system).
   - Committed `06a4097`. Launched R48.

2. **R48 completed — 12 findings (all downstream propagation of 8.76A correction)**
   - Findings across Design_Log (DEC-003, DEC-004), Cert_Evidence (§3.2 ILIM row, §3.2 soft-start row, §3.3.1 Buck), PM Board_Layout (12V_POE row, 5V_MAIN ×2, battery row, heading), Controller Design_Spec (§9.3), User_Manual (§3.3).
   - Battery row corrected from 4.82A (wrong — was using 12V PoE denominator) to 3.89A (correct — (8.76+1)×5/(0.87×14.4V)).
   - All 12 fixes applied and committed `75d9d2e`. Launched R49.

3. **R49 hit rate limit — re-launched as R49-retry**
   - First attempt rate-limited before completing.
   - Re-launched; still running when user returned.

4. **User returned and identified a critical error: Extension buffer was wrongly removed in R43**
   - R43 had flagged the Extension U1 (SN74LVC2G125DCUR) as stale because the Consolidated_BOM had EXT=— (dash). The reviewer used the BOM as authority and deleted the buffer from the Design_Spec. This was wrong — the BOM was stale, not the Design_Spec.
   - User explained the design rationale: 30-rotor chain needs TCK/TMS re-buffering every 5 rotors; buffer was originally planned per-rotor but moved to Extension board to reduce rotor BOM complexity.
   - User also clarified: TCK/TMS/TDI travel via **BtB connectors** (ERM8/ERF8), NOT ribbon cables. Only power and TTD_RETURN (JTAG TDO) use ribbon cables.

5. **Extension buffer restoration**
   - Used `git checkout 1155015^ -- Extension/Design_Spec.md Extension/Board_Layout.md` to restore pre-R43 state.
   - Fixed Consolidated_BOM: SN74LVC2G125DCUR EXT=1, Total=2; 0.1µF X7R 0402 EXT=1, Total=508.
   - Added U1 re-buffer note to JTAG_Integrity §8 trace table (was missing, unlike JDB row which names U5).
   - Committed `962d765` (Extension restore) and `379949c` (JTAG_Integrity note).
   - Stored memory facts to prevent future agents from repeating this error.

6. **R49-retry is still running with stale known-correct list**
   - The running agent's known-correct list says "Extension: no U1 buffer" — this is now wrong.
   - Results must be discarded; a new review pass needed with corrected known-correct list.

7. **Current §2 state check**
   - Viewed Extension Design_Spec §2 after restoration — confirmed JTAG Signal Buffering section is present (lines 78–88) with full buffer description, signal integrity analysis (30pF load, τ=2.85ns at 10MHz).
   - Lines 95–99 also have a redundant "passive pass-through" JTAG note that conflicts with the buffering section — this is a pre-existing inconsistency in the pre-R43 file that should be corrected.
</history>

<work_done>
Files modified this session:

- `design/Standards/Certification_Evidence.md` — §3.5: LDO=2.11A, total=8.76A/73.0%, LMQ=73.0% (exception removed), eFuse=4.67A/66.7%, PoE cold-start=53.2W/73.9% (exception removed); §3.2 ILIM=8.76A, soft-start PoE note corrected; §3.3.1 Buck=73.0%; OA-02 note updated.
- `design/Design_Log.md` — DEC-003: eFuse 4.67A/66.7%; DEC-004: PoE 73.9%/53.2W, steady 69.9%/50.3W.
- `design/Electronics/Power_Module/Board_Layout.md` — §9: 12V_POE=4.43A/53.2W, 5V_MAIN=8.76A (×2 rows), battery=3.89A, heading=8.76A.
- `design/Electronics/Controller/Design_Spec.md` — §9.3: 5V_MAIN 8.76A worst-case.
- `design/Guides/User_Manual.md` — §3.3: 73.0% within rule (exception language removed).
- `design/Electronics/Extension/Design_Spec.md` — restored to pre-R43 state (U1 buffer, C6, FR-EXT-01/02, DR-EXT-04/05/06, §2 JTAG buffering section).
- `design/Electronics/Extension/Board_Layout.md` — restored to pre-R43 state (U1 in ASCII art and trace table).
- `design/Electronics/Consolidated_BOM.md` — SN74LVC2G125DCUR EXT=1, Total=2; 0.1µF X7R 0402 EXT=1, Total=508.
- `design/Electronics/Investigations/JTAG_Integrity.md` — §8 Extension row: added U1 re-buffer note.
- `.copilot/agent-prompts/r48-review-prompt.txt` and `r49-review-prompt.txt` — created.

Commits this session:
- `06a4097` — R47 fixes (§3.5 peak load 8.76A, exceptions removed)
- `75d9d2e` — R48 fixes (12 downstream propagation fixes)
- `962d765` — Revert R43 error: Extension U1 buffer restored
- `379949c` — JTAG_Integrity §8: Extension U1 re-buffer note added

Work completed:
- [x] R47 fixes applied and committed
- [x] R48 fixes applied and committed
- [x] R49 first attempt (rate-limited, discarded)
- [x] Extension buffer restored (R43 error corrected)
- [x] Consolidated BOM corrected (SN74LVC2G125DCUR and 0.1µF rows)
- [x] JTAG_Integrity updated to note Extension U1
- [ ] R49-retry currently running — results must be **discarded** (stale known-correct list)
- [ ] Need fresh review pass with corrected known-correct list
- [ ] Second consecutive clean pass
- [ ] Encoder marked complete in Design_Log
- [ ] Checkpoint saved
- [ ] Begin Rotor detailed design review
</work_done>

<technical_details>
**8.76A cascade correction:**
The LDO load was 2.20A in §3.5 but 2.11A in §3.4 (known correct since R45). Fixing this cascaded through 18 locations across 5 files. Crucially, it also eliminated two "accepted exceptions" — LMQ at 75.4% and PoE cold-start at 76.2% — both now fall within the ≤75% policy. The system has zero utilisation exceptions.

**Battery row recalculation:**
Old value 4.82A was the PoE/12V eFuse worst-case calculation wrongly applied to the battery row. Correct: (8.76+1)×5/(0.87×14.4V) = 3.89A.

**R43 root cause — Extension buffer removal was wrong:**
R43 reviewer used Consolidated_BOM (EXT=—, stale) as the authority over Extension Design_Spec. Correct approach: Design_Spec is authoritative; BOM must match it. The Extension U1 (SN74LVC2G125DCUR) buffers TCK/TMS at each 5-rotor group boundary in the 30-rotor chain. Rotors have NO individual JTAG buffer. This decision was made to reduce rotor BOM by centralising the re-buffer in the Extension board.

**Interconnect topology (critical):**
- TCK/TMS/TDI travel via **BtB connectors** (ERM8/ERF8 Samtec 0.8mm pitch), NOT ribbon cables.
- Only **power** and **TTD_RETURN** (JTAG TDO return) use ribbon cables via the Extension Port (J7/J8).
- The 95Ω × 30pF = 2.85ns τ signal integrity analysis in the Extension spec is for BtB connector + PCB trace capacitance across 5 CPLD boards.

**Extension Design_Spec §2 inconsistency (unresolved):**
After restoration, lines 78–88 have the correct JTAG Signal Buffering section, but lines 95–99 also have a conflicting "passive pass-through" JTAG note. This is a pre-existing issue in the pre-R43 file that was not addressed — the review should catch and fix it.

**R49-retry agent (running) — discard results:**
The running R49-retry has a known-correct list stating "Extension: no U1 buffer" — this is now wrong after the restoration. Its findings will contain false positives about the Extension buffer. Discard this run entirely and create a fresh review prompt.

**Known-correct list updates needed for next review prompt:**
- Remove: "Extension board: NO U1 buffer; FR-EXT-02 deleted; DR-EXT-04 and DR-EXT-06 deleted"
- Remove: "Consolidated BOM SN74LVC2G125DCUR: JDB=1, EXT=dash, Total=1"
- Remove: "Consolidated BOM 0.1uF X7R 0402 row: EXT=dash, Total=507"
- Add: "Extension board U1 (SN74LVC2G125DCUR) buffers TCK/TMS at rotor group boundary — correct and intentional; EXT=1 in BOM"
- Add: "Consolidated BOM SN74LVC2G125DCUR: JDB=1, EXT=1, Total=2"
- Add: "Consolidated BOM 0.1µF X7R 0402: EXT=1, Total=508 (C6 bypass for U1)"
- Add: "TCK/TMS/TDI travel via BtB connectors (ERM8/ERF8); only power and TTD_RETURN use ribbon cables"
- Keep all R47/R48 known-correct items (8.76A, 73.0%, etc.)

**Pre-existing MD013 lint errors (cannot auto-fix):**
- Consolidated_BOM lines 195–196
- PM Design_Spec line 489
- User_Manual line 134
- Power_Management line 215
- Global_Routing_Spec line 72

**Session state location:** repo-local `.copilot\`
**Resume phrase:** "Please read `.copilot/plan.md` and all files in `.copilot/checkpoints/` to align yourself with the current project state, then continue from where we left off."

**Agent prompt issue:** Backtick characters in task agent prompts cause JSON parse errors — save prompts to `.copilot/agent-prompts/*.txt` and reference by path.

**markdownlint:**
- PATH refresh: `$env:PATH = [System.Environment]::GetEnvironmentVariable("PATH","Machine")+";"+[System.Environment]::GetEnvironmentVariable("PATH","User")`
- Run: `.\node_modules\.bin\markdownlint.cmd --fix "design/**/*.md"` then without `--fix` to confirm.
</technical_details>

<important_files>
- `design/Standards/Certification_Evidence.md`
  - Central certification document; extensively modified this session across §3.2, §3.3.1, §3.5, OA-02.
  - All load budget figures now consistent: LDO=2.11A, total peak=8.76A/73.0%, zero exceptions.

- `design/Electronics/Extension/Design_Spec.md`
  - Wrongly modified by R43 (U1 buffer removed); restored to pre-R43 state via `git checkout 1155015^`.
  - **Known issue:** Lines 95–99 have a conflicting "passive pass-through" JTAG note that contradicts the correct buffering description at lines 78–88 — needs fixing in the next review pass.

- `design/Electronics/Extension/Board_Layout.md`
  - Restored to pre-R43 state; U1 JTAG BUFFER present in ASCII art and trace table.

- `design/Electronics/Consolidated_BOM.md`
  - SN74LVC2G125DCUR: EXT=1, Total=2 (line 29).
  - 0.1µF X7R 0402: EXT=1, Total=508 (line 53).

- `design/Electronics/Investigations/JTAG_Integrity.md`
  - §8 trace table Extension row (line 445): added "U1 (SN74LVC2G125DCUR) re-buffers TCK/TMS at rotor group boundary".

- `design/Design_Log.md`
  - DEC-003 (line 115), DEC-004 (lines 129, 140): all figures updated to 8.76A base.

- `design/Electronics/Power_Module/Board_Layout.md`
  - §9 trace table: 12V_POE=4.43A/53.2W, 5V_MAIN=8.76A (×2), battery=3.89A, heading updated.

- `.copilot/agent-prompts/r49-review-prompt.txt`
  - STALE — contains wrong known-correct items (Extension no buffer, BOM EXT=—).
  - Must be replaced with a corrected prompt before launching the next review pass.
</important_files>

<next_steps>
**Immediate — discard R49-retry, create corrected review prompt:**

1. Wait for R49-retry to complete, then discard its results (wrong known-correct list).
2. Fix Extension Design_Spec §2 conflicting passive pass-through text (lines 95–99): replace with a note that JTAG TDI passes unbuffered and TTD_RETURN passes via Extension Port pin 15; TCK/TMS are re-buffered by U1.
3. Create a corrected R49 (or R50) prompt with:
   - Remove all stale "Extension no buffer" known-correct items
   - Add: Extension U1 buffer correct, EXT=1 in BOM, Total=2 for SN74LVC2G125DCUR, Total=508 for 0.1µF
   - Add: TCK/TMS/TDI via BtB; only power and TTD_RETURN via ribbon cable
   - Keep all R47/R48 corrections in known-correct list
4. Launch fresh review pass. If clean → launch second consecutive pass.

**After two consecutive clean passes:**
1. Add INC entry to Design_Log.md marking Encoder detailed design phase complete.
2. Update `.copilot/plan.md`: Encoder → complete, next = Rotor detailed design review.
3. Save checkpoint to `.copilot/checkpoints/007-encoder-review-complete.md`.
4. Update `.copilot/checkpoints/index.md`.
5. Begin Rotor detailed design review.

**Open question:**
The Extension Design_Spec §2 has a signal integrity note: "95Ω × 30pF = 2.85ns, well within the 50ns half-period at 10MHz TCK". The 95Ω figure needs verification — this should be the source impedance of the buffer output (SN74LVC2G125DCUR Zo ≈ 25–30Ω at 3.3V) plus any series resistor, not 95Ω. This may need correction but has not been flagged by any review agent. Worth checking.
</next_steps>
