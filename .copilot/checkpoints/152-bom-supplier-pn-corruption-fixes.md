# Checkpoint 152 — BOM supplier PN corruption fixes complete

**Date:** 2026-05-02
**Status:** All file edits complete, lint clean. Awaiting user review and commit.

---

## What was done

Three component supplier PN corruption issues (introduced by a prior package-size-reduction session) identified and fully fixed across all affected BOM tables:

### Issue 1 — ERJ-2RKF1001X (1kΩ 1% Thick-Film 0402)

Correct PNs: DigiKey `P1.00KLCT-ND` | Mouser `667-ERJ-2RKF1001X` | JLCPCB `C242161`

Corrupt codes removed:
- `C25705` (was for a 62kΩ 1210 resistor)
- `P1.00KLBCT-ND` (invalid PN)

Files fixed:
- `design/Electronics/Consolidated_BOM.md` — PM + SBD rows merged into single row with correct PNs; obsolete BOM Notes bullet removed
- `design/Electronics/Power_Module/Design_Spec.md` — DigiKey + JLCPCB corrected
- `design/Electronics/Settings_Board/Design_Spec.md` — R12-R17 + R54-R65 rows merged; PNs corrected

### Issue 2 — CL05B104KB5NNNC (100nF X7R 50V 0402)

Correct PNs: DigiKey `1276-CL05B104KB5NNNCCT-ND` | Mouser `187-CL05B104KB5NNNC` | JLCPCB `C960916`

Corrupt codes removed:
- `1276-1009-1-ND` (was for a 10000pF X7R 50V 0603 capacitor)
- `C1525` (was for CL05B104K**O**5NNNC — different MPN, 16V not 50V)

Files fixed:
- `design/Electronics/Consolidated_BOM.md`
- `design/Electronics/Power_Module/Design_Spec.md`
- `design/Electronics/Controller/Design_Spec.md`
- `design/Electronics/JTAG_Daughterboard/Design_Spec.md`
- `design/Electronics/Settings_Board/Design_Spec.md` — C1-C3 + C4 rows merged
- `design/Electronics/Encoder/Design_Spec.md`
- `design/Electronics/Actuation_Module/Design_Spec.md`
- `design/Electronics/Stator/Design_Spec.md`
- `design/Electronics/Extension/Design_Spec.md`
- `design/Electronics/Rotor/Design_Spec.md`
- `design/Electronics/Rotor/Rotor_26_Char_Design.md`
- `design/Electronics/Rotor/Rotor_64_Char_Design.md`

### Issue 3 — ERJ-2RKF10R0X (10Ω 1% Thin-Film 0402)

Correct PNs: DigiKey `P10.0LCT-ND` | Mouser `667-ERJ-2RKF10R0X` | JLCPCB `C413044`

- `design/Electronics/Consolidated_BOM.md` — obsolete contradictory note removed from Notes column
- `design/Electronics/Power_Module/Design_Spec.md` — JLCPCB `Global sourcing / consignment` → `C413044`; Alt Supplier `Global sourcing` → `—`

---

## Additional fixes

- `design/Electronics/Settings_Board/Design_Spec.md` — empty Notes cells `|  |` (two spaces) corrected to `| — |` to resolve MD060 lint errors
- `design/Electronics/Rotor/Design_Spec.md` — blank line inside blockquote (MD028) fixed
- `design/Electronics/Consolidated_BOM.md` — missing space after pipe on line 120 (MD060) fixed
- `.copilot/todo-list.md` — `full-pn-review` deferred item added to Electronics Deferrals table

---

## Git incident note

A background agent during this session ran `git reset HEAD` mid-task, unstaging all previously staged changes. The agent was stopped immediately. All file content was preserved — only staging was lost. User elected to re-review all changes from scratch before staging manually.

**Rule added:** Future background agents must never run any git commands.

---

## Pending

- [ ] User manual review of all modified files
- [ ] User stages and commits (SECONDARY DIRECTIVE: never commit without explicit user confirmation)
- [ ] Full supplier PN sweep before schematic capture (todo id: `full-pn-review`)
