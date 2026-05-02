<overview>
This session continued the Enigma-NG BOM restructure and RefDes cleanup work. The primary goals were: completing minor BOM/RefDes corrections (Stator SW1/SW2 removal, Encoder BT1–BT64 rename to J3–J66), registering a deferred Rotor variant design todo, creating a persistent repo-local todo tracking file (`.copilot/todo-list.md`), and fixing an incorrect design-specific content leak into the SaiBuy jack socket pseudo-datasheet. All work follows strict directives: no commits without explicit "Let's lock this in", Design Log is append-only, and MPNs/supplier PNs must never be modified without user confirmation.
</overview>

<history>

1. **Session resumed from prior compaction (checkpoint 098/099)**
   - Prior sessions had completed: all 10 board-level BOM tables restructured to 12-column format, DEC-028 reverted, DEC-049 appended, agent-directives.md hardened
   - Pending at resumption: Encoder `BT1–BT64` RefDes correction, todo-list.md creation

2. **Stator SW1/SW2 removal** (carried from prior session summary)
   - User noted SW1 and SW2 on the Stator were shown with strikethrough "Removed — relocated to Settings Board"
   - Directive enforced: design specs are current-state-only snapshots; no historical/removed content
   - Both rows fully deleted from `design/Electronics/Stator/Design_Spec.md`

3. **Encoder BT1–BT64 → J3–J66 rename**
   - `BT` is IPC/EDA standard prefix for batteries only; blade terminals should be `J` (connector)
   - J1 = plugboard panel jacks (off-board), J2 = IDC service connector already taken → blade terminals start at J3, end at J66
   - Applied across 6 files / 10 occurrences
   - DEC-050 appended to Design Log with full rationale, alternatives, and impact list

4. **Rotor N=26/N=64 variant todo registered**
   - U3 and U4 are identical parts in different physical positions depending on variant
   - Recommended mechanism: KiCAD board variant / DNF flags (U3 Fit for N=26, U4 Fit for N=64; bypass caps follow same variant)
   - Registered in SQL todos and in new `.copilot/todo-list.md`

5. **`.copilot/todo-list.md` created**
   - User requested a persistent repo-local file to track all deferred items so they survive session compaction
   - Grep run across all non-Design-Log, non-Datasheet design docs to find TODOs/TBDs
   - File created with 5 sections: Open Workstreams, Electronics Deferrals, Mechanical Deferrals, Software Deferrals, Standards & Certification Actions
   - `plan.md` and `handoff.md` updated to reference it
   - Checkpoint 099 written and index updated

6. **SaiBuy datasheet cleanup**
   - User noticed the SaiBuy jack socket pseudo-datasheet (`design/Datasheets/SaiBuy_Ltd_6p35mm_Mono_Jack_Pseudo_Datasheet.md`) contained design-specific content: J3–J66 RefDes, wiring assignments, plugboard role description
   - User stated: datasheets should describe component details only; wiring, RefDes and usage belong in Design_Spec and Board_Layout only
   - Section 2: removed Tip/Sleeve → J3-J66 mapping lines and system quantity (64 sockets); kept component-level terminal type description
   - Section 4: renamed from "Enigma-NG Integration Notes" to "Component Notes"; removed "Wiring" row and "Plugboard role" row; kept Jack type, Normal state (component switch behaviour), and Procurement note
   - Note: the original file had `BT1-BT64` RefDes before the rename — the design-leakage was a pre-existing issue, not introduced by the rename

</history>

<work_done>

Files modified this session:

- `design/Electronics/Stator/Design_Spec.md` — SW1 and SW2 rows fully deleted (were "Removed — relocated to Settings Board" with strikethrough) ✅
- `design/Electronics/Encoder/Design_Spec.md` — BT1–BT64 → J3–J66 in §4 narrative, BOM row, Qty notes ✅
- `design/Electronics/Encoder/Board_Layout.md` — BT1–BT64 → J3–J66 in signal group table ✅
- `design/Software/CPLD_Logic/Encoder_Logic.md` — BT1–BT64 → J3–J66 at 3 locations ✅
- `design/Electronics/Consolidated_BOM.md` — Encoder row RefDes BT1–BT64 → J3–J66 ✅
- `design/Datasheets/SaiBuy_Ltd_6p35mm_Mono_Jack_Pseudo_Datasheet.md` — removed design-specific content (J3-J66 RefDes, wiring, plugboard role, system quantity); §2 simplified to component-level terminal description; §4 renamed to "Component Notes" and stripped to component-only rows ✅
- `design/Design_Log.md` — DEC-050 appended (BT→J rename rationale and impact) ✅
- `.copilot/todo-list.md` — **Created** (new file); 5-section canonical deferred-work tracker ✅
- `.copilot/plan.md` — Next Session Start Point updated to reference `todo-list.md` and checkpoint 099; Critical Notes updated with directive to use `todo-list.md` ✅
- `.copilot/handoff.md` — Standing Directives section updated to reference `todo-list.md` ✅
- `.copilot/checkpoints/099-bt-to-j-rename-todo-list-created.md` — checkpoint written ✅
- `.copilot/checkpoints/index.md` — entry 149 added for checkpoint 099 ✅

Work completed:

- [x] Stator SW1/SW2 removed from Design_Spec
- [x] BT1–BT64 → J3–J66 rename across all 6 files
- [x] DEC-050 appended to Design Log
- [x] All changed files linted clean (exit 0)
- [x] Rotor variant deferred todo added to SQL and todo-list.md
- [x] `.copilot/todo-list.md` created
- [x] `plan.md` and `handoff.md` updated to reference todo-list.md
- [x] Checkpoint 099 written
- [x] SaiBuy datasheet cleaned of design-specific content

**NOT YET COMMITTED** — awaiting explicit "Let's lock this in" from user

</work_done>

<technical_details>

- **BT RefDes convention**: `BT` is the IPC/EDA standard prefix for batteries only. PCB-mount spade/blade terminals are `J` (connector). Encoder J1 = plugboard panel jacks (off-board), J2 = IDC service connector; blade terminal bank is J3–J66.
- **Design spec "current state only" rule**: Design specs are snapshots of the current design — no historical, removed, or deprecated content. Items relocated/removed must be fully deleted, not annotated with strikethrough or "Removed" notes.
- **Datasheet content rule**: Datasheets describe component properties only. Wiring, RefDes assignments, system quantities, and usage context belong exclusively in Design_Spec.md and Board_Layout.md. The SaiBuy pseudo-datasheet had this issue pre-existing (with `BT1-BT64` references before the rename).
- **Design Log is append-only**: Existing DEC entries are read-only. New entries only; amendments require a new DEC with `Amends: DEC-NNN` field. DEC-050 is now the last entry before `## Open Questions`.
- **Rotor N=26 vs N=64 variant handling**: U3 (Board A sensor) and U4 (Board B sensor) are the same MPN but at different physical positions. KiCAD board variant / DNF flags is the correct mechanism — U3 Fit for N=26 variant, U4 Fit for N=64 variant; bypass caps follow same variant flag. Deferred to schematic capture.
- **Markdownlint on dotfolders**: The `.copilot/` directory requires `--dot` flag: `.\node_modules\.bin\markdownlint.cmd --dot .copilot\<file>.md`
- **Controller BT1 must NOT be renamed**: CR2032 holder on Controller board is a legitimate battery RefDes — not affected by the BT→J rename.
- **Consolidated BOM Section 2 is read-only**: Lines 239+ are the per-unit MPN qty summary; must not be modified.
- **todo-list.md is the canonical deferred-work tracker**: Future sessions should consult `.copilot/todo-list.md` rather than re-scanning the repo for TODOs. Update it when new items are identified or existing items are closed.

</technical_details>

<important_files>

- **`.copilot/todo-list.md`**
  - Newly created canonical deferred-work and open-action tracker
  - 5 sections: Open Workstreams, Electronics Deferrals, Mechanical Deferrals, Software Deferrals, Standards & Certification Actions
  - Referenced from plan.md and handoff.md; must be updated when items are opened or closed

- **`.copilot/agent-directives.md`**
  - Primary session directives; SECONDARY (no unauthorised git commits) and TERTIARY (Design Log integrity) both carry ⚠️ CRITICAL INTEGRITY VIOLATION warnings
  - Must be read at every session start

- **`.copilot/plan.md`**
  - Updated: Next Session Start Point now lists todo-list.md as step 3; Critical Notes warns to use it
  - "Next Session Start Point" section directs reading checkpoint 099

- **`.copilot/handoff.md`**
  - Updated: Standing Directives section references todo-list.md
  - Contains session-to-session context, open review items, and pointer to agent-directives.md

- **`design/Design_Log.md`**
  - Append-only audit log; DEC-050 is now the last entry (BT→J rename rationale)
  - Existing entries are READ-ONLY — critical integrity rule

- **`design/Electronics/Consolidated_BOM.md`**
  - Encoder row RefDes updated (BT1–BT64 → J3–J66) at line 206
  - Section 2 (lines 239+) per-unit MPN qty summary — must NOT be modified
  - Controller BT1 (line 101) is a legitimate battery RefDes — do not rename

- **`design/Datasheets/SaiBuy_Ltd_6p35mm_Mono_Jack_Pseudo_Datasheet.md`**
  - Cleaned of design-specific content: §2 J3-J66 Tip/Sleeve/Switch mapping removed, system qty removed; §4 renamed "Component Notes", Wiring and Plugboard role rows removed
  - Now describes component properties only; wiring/usage lives in Encoder Design_Spec and Board_Layout

- **`design/Software/CPLD_Logic/Encoder_Logic.md`**
  - BT1–BT64 → J3–J66 at 3 locations (role identity §3, signal bank §4.1, decode §7.1)

- **`.copilot/checkpoints/099-bt-to-j-rename-todo-list-created.md`**
  - Latest checkpoint; full record of all files changed this session

</important_files>

<next_steps>

Remaining work:

- All planned work for this session is complete
- **DO NOT COMMIT** — awaiting explicit "Let's lock this in" from user before any git commit

After user authorises commit:

- Stage and commit all modified files with appropriate commit message
- After commit: decide on next workstream (Pass 3 review, KiCAD library prep, schematic capture prep, etc.)
- Consult `.copilot/todo-list.md` for the full deferred-work backlog

Immediate next session start:

1. Read `.copilot/agent-directives.md`
2. Read `.copilot/plan.md`
3. Read `.copilot/handoff.md`
4. Read `.copilot/todo-list.md`
5. Read `.copilot/checkpoints/099-bt-to-j-rename-todo-list-created.md`

</next_steps>