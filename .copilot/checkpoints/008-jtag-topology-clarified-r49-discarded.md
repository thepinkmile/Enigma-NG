<overview>
Following checkpoint 007 (Extension buffer restored, R47-R48 fixes), this checkpoint covers two
further rounds of JTAG documentation clarifications made after the user returned and provided
detailed topology guidance. The user clarified that TCK/TMS/TDI travel via BtB connectors
throughout the entire rotor stack (no ribbon cables within the stack), that JTAG chain termination
occurs at the Reflector (R1=22Ω), and that the Reflector J4 ribbon cable back to the Stator carries
BOTH TTD_RETURN (JTAG, pin 15) AND ENC_IN/ENC_OUT (plugboard configuration, pins 3-14 — NOT JTAG).
R49-retry was discarded (stale known-correct list — all 17 findings were false positives targeting
the correctly-restored Extension U1 buffer).
</overview>

<history>
1. **Extension §2 passive pass-through conflict resolved (commit 6737bc0)**
   - After restoring the Extension buffer in checkpoint 007, lines 95-99 of Extension Design_Spec
     still contained a legacy "passive pass-through only" note and "cable segment" language.
   - Fixed: removed incorrect "passive pass-through only" claim (TCK/TMS are actively buffered by U1).
   - Fixed: changed "cable segment" to "BtB-connected segment" — TCK/TMS/TDI travel via BtB, not cable.
   - Fixed: signal integrity note (95Ω × 30pF) updated to describe BtB connector/trace capacitance
     correctly; removed misleading 95Ω source impedance figure.
2. **User clarified full JTAG topology (key design facts)**
   - TCK/TMS/TDI travel via BtB connectors (ERM8/ERF8 Samtec 0.8mm pitch) through the entire
     rotor stack. NO ribbon cables are used for JTAG signals within the rotor stack.
   - JTAG chain terminates at the Reflector. Reflector R1 (22Ω) is the end-of-chain damping.
   - Reflector J4 → Stator J7 ribbon cable carries: pin 15=TTD_RETURN (JTAG), pins 3-14=ENC_IN/OUT
     (plugboard configuration for Stator CPLD — NOT JTAG). The ribbon does NOT extend the JTAG chain.
   - Extension U1 (SN74LVC2G125DCUR) re-buffers TCK/TMS at each 5-rotor group boundary.
   - Stator R7-R15 (75Ω) and Encoder R7-R8 are for encoder RIBBON CABLE ports (J4/J5/J6) ONLY —
     they do not apply to the BtB rotor stack.
   - The confusion arose because the Reflector J4 ribbon also carries ENC signals, which some agents
     interpreted as the JTAG chain continuing past the Reflector.
3. **JTAG topology documentation overhauled (commit 23aa4a3)**
   - JTAG_Integrity.md §1: distinguish two interconnect types (ribbon for Stator-Encoder ports,
     BtB ERM8/ERF8 for rotor stack).
   - JTAG_Integrity.md topology diagram: expanded to show BtB labels, Extension U1 re-buffer,
     Reflector as "JTAG CHAIN END", TTD_RETURN ribbon path, and explicit note that J4 ENC pins
     3-14 are plugboard config (NOT JTAG).
   - JTAG_Integrity.md §2 note: updated stale "2-layer Reflector/Extension" reference (now 4-layer
     since DEC-017).
   - JTAG_Integrity.md §7.1: added end-of-chain row for Reflector R1 (22Ω).
   - JTAG_Integrity.md §7.3: renamed columns "ribbon cable" vs "BtB"; blockquote notes distinguish
     rotor BtB path (Extension U1 + Reflector R1) from encoder ribbon sub-chains.
   - JTAG_Integrity.md §7.4: encoder port rows now labelled "encoder ribbon port"; Reflector R1
     row annotated as JTAG chain END.
   - Extension Design_Spec §2: corrected wrong claim that Stator R7-R15 / Encoder R7-R8 apply to
     BtB segments — these are for encoder ribbon ports only.
   - Reflector Design_Spec §3: added prominent ⚠️ JTAG chain END warning with explicit J4 pin list.
4. **R49-retry completed — all 17 findings discarded**
   - Agent ran with stale known-correct list (pre-restoration, Extension has no U1 buffer).
   - All 17 findings were false positives asking to remove the correctly-restored U1 buffer,
     FR-EXT-02, DR-EXT-04/05/06, C6, BOM rows, JTAG_Integrity references, etc.
   - None of these changes should be made. The Extension U1 buffer is correct and intentional.
   - A fresh review pass (R50) is required with the corrected known-correct list.
</history>

<work_done>
Files modified since checkpoint 007:

- `design/Electronics/Extension/Design_Spec.md`
  - §2: replaced "passive pass-through only" language with correct BtB description
  - §2: updated signal integrity note (removed misleading 95Ω figure, described BtB capacitance)
  - §2 JTAG TTD_RETURN/TDI note: corrected — Stator R7-R15 / Encoder R7-R8 are for encoder
    ribbon ports only, not the BtB rotor stack; JTAG terminates at Reflector R1
- `design/Electronics/Investigations/JTAG_Integrity.md`
  - §1 intro: two-interconnect-type description (ribbon vs BtB)
  - §1 topology diagram: expanded rotor stack section (BtB labels, Extension U1, Reflector END,
    TTD_RETURN ribbon path, ENC pin clarification)
  - §1 post-diagram text: TCK/TMS broadcast covers both encoder ribbon ports and rotor BtB
  - §2 stale 2-layer Reflector/Extension note updated to 4-layer (DEC-017)
  - §7.1: added Reflector R1 end-of-chain row
  - §7.3: ribbon vs BtB columns; rotor BtB and encoder sub-chain blockquote notes
  - §7.4: "encoder ribbon port" labels; Reflector R1 annotated as JTAG chain END
- `design/Electronics/Reflector/Design_Spec.md`
  - §3: added ⚠️ JTAG chain END blockquote with explicit J4 pin-by-pin description
  - §3: J4 now clearly documents which pins are JTAG (pin 15 TTD_RETURN only) vs ENC config
    (pins 3-14, NOT JTAG)

Commits since checkpoint 007:
- `6737bc0` — Extension §2: fix JTAG section — BtB connectors, not ribbon cables
- `23aa4a3` — JTAG topology: clarify BtB rotor stack vs ribbon cable segments

R49-retry results: DISCARDED — all 17 findings were false positives (stale known-correct list).

Work completed since checkpoint 007:
- [x] Extension §2 passive pass-through conflict resolved
- [x] JTAG topology documented comprehensively in JTAG_Integrity.md
- [x] Reflector §3 JTAG chain END warning added
- [x] Two key JTAG topology facts stored to agent memory
- [ ] Fresh review pass (R50) with corrected known-correct list — NEXT
- [ ] Second consecutive clean pass (R51)
- [ ] Encoder marked complete in Design_Log
- [ ] Checkpoint 009 saved
- [ ] Begin Rotor detailed design review
</work_done>

<technical_details>
**JTAG chain topology — definitive reference:**

```
FT232H (JDB) → LINK-BETA (BtB) → Stator CPLD
    │
    ├─ [Encoder sub-chains via RIBBON CABLE, J4/J5/J6]
    │  Each: 75Ω source R (Stator) → IDC ~100Ω ribbon → Encoder CPLD1/CPLD2 → 75Ω TDO back
    │
    └─ [Rotor stack via BtB (ERM8/ERF8 0.8mm pitch) — NO ribbon cable within rotor stack]
       Stator J1-J3 → Rotor 1 → ... → Rotor 5 → Extension board
                                                  U1: SN74LVC2G125DCUR re-buffers TCK/TMS
                                               → Rotor 6 → ... → Rotor 30 → Reflector
                                                                              JTAG CHAIN END
                                                                              R1 22Ω end-of-chain

       TTD_RETURN ribbon: Reflector J4 pin 15 → Stator J7 pin 15 → LINK-BETA pin 26 → FT232H
       NOTE: Reflector J4 ALSO carries ENC_IN[0:5]/ENC_OUT[0:5] (pins 3-14) for Stator CPLD
             plugboard-pass configuration — these are NOT JTAG signals.
```

**Termination rules by segment type:**
- Ribbon cable (~100Ω IDC): 75Ω source series R at driving output
- BtB intra-board or LINK-BETA: 33Ω source series R
- Rotor BtB stack: Extension U1 re-buffers TCK/TMS every 5 rotors; TDI passes unbuffered;
  Reflector R1 (22Ω) is the end-of-chain TDO damping resistor
- Stator R7-R15: encoder ribbon ports ONLY (J4/J5/J6) — NOT applicable to rotor BtB stack
- Encoder R7-R8: encoder boards ONLY — NOT applicable to rotor BtB stack

**Extension U1 buffer — must NEVER be removed by review agents:**
- SN74LVC2G125DCUR (VSSOP-8) on Extension board buffers TCK and TMS
- Re-buffering every 5-rotor group is required due to cumulative capacitive loading in 30-rotor chain
- Buffer was originally planned per-rotor; moved to Extension board to reduce Rotor BOM
- C6 (0.1µF X7R 0402) is the bypass capacitor for U1 VCC
- Consolidated BOM: SN74LVC2G125DCUR EXT=1, Total=2; 0.1µF X7R 0402 EXT=1, Total=508
- FR-EXT-01/02 and DR-EXT-04/05/06 in Extension Design_Spec §1 are all CORRECT and INTENTIONAL

**R49-retry false positive root cause:**
The R49-retry agent was launched before the Extension buffer was restored. Its known-correct list
stated "Extension board: NO U1 buffer." After restoration in commits 962d765/379949c, the agent's
known-correct list became stale. All 17 findings attempted to remove the correctly-restored buffer.
Future review agents must include the corrected known-correct items listed below.

**Corrected known-correct list for R50 prompt (additions over R48 list):**
- Extension board U1 (SN74LVC2G125DCUR) buffers TCK/TMS at each 5-rotor group boundary — CORRECT
- Extension FR-EXT-01 cross-refs U1 — CORRECT
- Extension FR-EXT-02 (buffer TCK/TMS) present — CORRECT
- Extension DR-EXT-04 (JTAG buffer U1), DR-EXT-05 (buffer pin assignment), DR-EXT-06 (C6 bypass) — CORRECT
- Extension §2 JTAG Signal Buffering section (74LVC2G125, TCK/TMS only) — CORRECT
- Extension §4 C6 placement rule — CORRECT
- Extension BOM: C6 (100nF X7R) and U1 (SN74LVC2G125DCUR) rows — CORRECT
- Extension Board_Layout U1 JTAG BUFFER in ASCII diagram and trace table — CORRECT
- Consolidated BOM SN74LVC2G125DCUR: JDB=1, EXT=1, Total=2 — CORRECT
- Consolidated BOM 0.1µF X7R 0402: EXT=1, Total=508 — CORRECT
- TCK/TMS/TDI travel via BtB (ERM8/ERF8) in rotor stack — no ribbon cable for JTAG in rotor stack
- Reflector J4 pin 15 = TTD_RETURN (only JTAG signal on J4); pins 3-14 = ENC plugboard config
- JTAG chain terminates at Reflector; Reflector R1 (22Ω) is the end-of-chain damping
- Stator R7-R15 (75Ω) and Encoder R7-R8 apply to encoder ribbon ports J4-J6 ONLY
- All 8.76A / 73.0% figures in Cert_Evidence, Design_Log, PM Board_Layout, CTL Design_Spec,
  User_Manual — CORRECT (corrected in R47-R48)
- LDO current = 2.11A in §3.4 and §3.5 — CORRECT
- Battery row 3.89A in PM Board_Layout §9 — CORRECT
- Zero utilisation exceptions in the system — CORRECT (LMQ 73.0%, PoE cold-start 73.9%)

**Pre-existing MD013 lint errors (acceptable, cannot auto-fix with markdownlint):**
- Consolidated_BOM lines 195-196
- PM Design_Spec line 489
- User_Manual line 134
- Power_Management line 215
- Global_Routing_Spec line 72

**markdownlint commands:**
```
$env:PATH = [System.Environment]::GetEnvironmentVariable("PATH","Machine")+";"+[System.Environment]::GetEnvironmentVariable("PATH","User")
.\node_modules\.bin\markdownlint.cmd --fix "design/**/*.md"
.\node_modules\.bin\markdownlint.cmd "design/**/*.md"
```
</technical_details>

<important_files>
- `design/Electronics/Extension/Design_Spec.md`
  - U1 buffer fully restored and §2 JTAG section now consistent — no conflicts.
  - FR-EXT-01/02, DR-EXT-04/05/06, §4 C6 rule, BOM U1+C6 rows all present and correct.
- `design/Electronics/Extension/Board_Layout.md`
  - U1 in ASCII art and §9 trace table — correct.
- `design/Electronics/Investigations/JTAG_Integrity.md`
  - §1 now has full BtB/ribbon topology description and expanded diagram.
  - §7.3/7.4 clearly separate ribbon (encoder) from BtB (rotor stack) termination.
  - §8 trace table Extension row names U1 re-buffer.
- `design/Electronics/Reflector/Design_Spec.md`
  - §3 has ⚠️ JTAG chain END blockquote with J4 pin-by-pin breakdown.
- `design/Electronics/Consolidated_BOM.md`
  - SN74LVC2G125DCUR: EXT=1, Total=2 — correct.
  - 0.1µF X7R 0402: EXT=1, Total=508 — correct.
</important_files>

<next_steps>
**Immediate — launch R50 with corrected known-correct list:**

1. Create `.copilot/agent-prompts/r50-review-prompt.txt` with:
   - Full corrected known-correct list from technical_details above
   - Deep-dive all design docs under design/Electronics/ and design/Standards/
   - Report findings as numbered table: file / section / issue / current / correct
   - Do NOT flag any Extension U1 buffer items as issues — they are all correct
2. Launch R50 general-purpose review agent.
3. If R50 is clean → launch R51 (second consecutive clean pass).
4. Both clean → proceed to close out.

**After two consecutive clean passes:**
1. Add INC entry to Design_Log.md: "Encoder detailed design review phase complete."
2. Update plan.md: Encoder → complete, next = Rotor detailed design review.
3. Save checkpoint 009.
4. Update checkpoint index.
5. Begin Rotor detailed design review.

**Board design status:**
| Board | Status |
|-------|--------|
| Power Module | ✅ Complete |
| Stator | ✅ Complete |
| Reflector | ✅ Complete |
| Extension | ✅ Complete |
| JDB | ✅ Complete |
| Controller | ✅ Complete |
| Encoder | 🔄 In review — awaiting R50+R51 clean passes |
| Rotor | ⏳ Pending |
</next_steps>
