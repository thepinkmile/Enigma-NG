# Checkpoint 169 — Design Log restructure complete

**Date:** 2026-05-22
**Session:** design-log-restructure workstream closed; extension-mechanical-usage marked in-progress

---

## Overview

Two workstreams resolved this session:

1. **data-plate-standardisation SQL cleanup** — corrected the SQL `INSERT` status block in
   `todo-list.md` (status was still `'pending'`; dep rows for `review-pass-11` were still present).
   Committed as `cad6a88`.

2. **design-log-restructure** — the monolithic `design/Design_Log.md` (83 DEC entries, ~295 KB) was
   split into a directory of per-DEC files. The original file was retired to `.recycle-bin/`.
   All cross-references across active files updated. Split script retired.

---

## Work Done

### data-plate-standardisation SQL fix (committed cad6a88)

- `todo-list.md` line 260: status `'pending'` → `'done'`
- Removed two dep rows `('review-pass-11', 'data-plate-standardisation')` from the SQL block

### design-log-restructure

- Created `design/Design_Log/` directory with 84 files:
  - `index.md` — preamble + table (DEC | Title | Date | Status | Summary) for all 83 decisions
  - `DEC-001_*.md` through `DEC-083_*.md` — one file per DEC, verbatim content from original
  - `DEC-044_fdc2114-internal-oscillator-selected-clkin-gnd.md` — created manually (original had
    malformed heading `## DEC-044-` missing space; regex did not match)
- `design/Design_Log.md` → moved to `.recycle-bin/`
- `.copilot/agent-directives.md` — TERTIARY DIRECTIVE updated at all 3 locations:
  - §3 TERTIARY section body
  - Quick-reference table entry
  - Inline cross-ref in §17 (NONARY) and §19 (UNDECIMARY)
- `plan.md` — Design Log reference updated
- All active cross-references to `design/Design_Log.md` updated (16 files):
  - `.github/copilot-instructions.md` → `design/Design_Log/index.md`
  - `README.md` → `design/Design_Log/index.md`
  - `design/Electronics/Controller/PoE_Power_Analysis_Coilcraft_v2.md` (2 refs)
  - `design/Electronics/Electrical_Design.md`
  - `design/Electronics/Extension/Design_Spec.md`
  - `design/Electronics/JTAG_Module/JTAG_Integrity.md` (2 refs)
  - `design/Electronics/Rotor/Design_Spec.md`
  - `design/Mechanical/Rotor/Design_Spec.md`
  - `design/Mechanical/Rotor_Stack_Assembly/Design_Spec.md` (2 refs)
  - `design/Software/CPLD_Logic/Rotor_Logic.md`
- `.copilot/todos/review-pass-11.md` and `review-pass-12.md` — `Design_Log.md` → `design/Design_Log/`
- `todo-list.md` — `design-log-restructure` → done; `extension-mechanical-usage` → in-progress;
  SQL block updated; dep rows for design-log-restructure removed from review-pass-11
- `.copilot/todos/design-log-restructure.md` → moved to `.recycle-bin/`
- `.copilot/scripts/split_design_log.py` → moved to `.recycle-bin/` (one-time tool)
- `.copilot/scripts/` directory removed (now empty)

### Historical files NOT updated (accurate period records)

`.copilot/checkpoints/` · `.copilot/handoff.md` prior entries · `.copilot/review-report.md`
historical entries — these correctly record the state at the time they were written.

---

## Key Numbers

| Item | Value |
|------|-------|
| Next checkpoint | 169 |
| Next DEC | DEC-084 |
| DEC file naming | `DEC-084_{kebab-title}.md` in `design/Design_Log/` + row in `index.md` |
| review-pass-11 blockers | `copilot-dir-restructure` only (design-log-restructure done ✅) |
| extension-mechanical-usage | in-progress |

---

## Repo State

- **Pass-10:** 91/91 board findings resolved ✅; all INT MINOR/MEDIUM findings closed ✅
- **Design Log:** split into `design/Design_Log/` (83 per-DEC files + index.md)
- **Committed:** cad6a88 (data-plate-standardisation); design-log-restructure NOT YET committed (user controls git)
- **Outstanding todos (unblocked):** `copilot-dir-restructure`, then `review-pass-11`

---

## Next Session Start

Read in order:
1. `.copilot/agent-directives.md` (always first — seed session DB immediately)
2. `.copilot/plan.md`
3. `.copilot/handoff.md` (latest section first)
4. This checkpoint file (`169-design-log-restructure-complete.md`)
5. `.copilot/review-report.md` (Pass-10 fully closed)
