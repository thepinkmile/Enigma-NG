# Checkpoint 077 — BOM rebuilt, CSD17578Q5A corrected

## Status

All work from this session committed and clean.

## What was done

### Consolidated BOM rebuilt from scratch

`design/Electronics/Consolidated_BOM.md` was completely rebuilt by extracting all component data
from the 10 individual board Design_Spec.md files into `design/Electronics/all_boards_bom.json`
(200 records), then generating the consolidated markdown from that JSON source.

- 200 component rows, 115 unique MPNs
- Section 1: full table (Board, RefDes, MPN, Manufacturer, DigiKey, Mouser, JLCPCB,
  Alt Supplier, Part Spec, Description/Usage, Footprint Available, Footprint Downloaded)
- Section 2: MPN quantity summary (per-board + per-unit total)
- Passes markdownlint clean

### CSD17483F4T → CSD17578Q5A correction

Q1, Q2, Q3 on the Power Module (OR-ing ideal-diode MOSFETs driven by LM74700-Q1) were incorrectly
specified as CSD17483F4T. Local datasheet confirmed this is a 1.5A/260mΩ PICOSTAR FemtoFET —
completely wrong for OR-ing duty.

Correct part: **CSD17578Q5A**

- 30V N-channel NexFET
- 25A continuous (package limited)
- R_DS(on): 5.9mΩ @ V_GS=10V; 7.9mΩ @ V_GS=4.5V
- Package: SON 5×6mm
- DigiKey: `296-48512-1-ND`
- Mouser: `595-CSD17578Q5A`
- JLCPCB: `C2871447`
- Datasheet: `design/Datasheets/TI-csd17578q5a-datasheet.pdf`

### Design Log

DEC-047 written in `design/Design_Log.md` recording the CSD17578Q5A correction with full rationale.

### Other BOM notes confirmed

- Nexperia vs NXP: `74HC157PW-Q100,118` (STA U4/U5) — correctly shows **Nexperia** in BOM.
- LMQ61460AFSQRJRRQ1 Mouser PN `595-Q61460AFSQRJRRQ1` confirmed correct (Mouser drops "LM").
- ERJ-2RKF1001X: two valid JLCPCB codes preserved — `C25705` (PM) and `C242161` (SBD).

## Files changed

| File | Change |
| :--- | :--- |
| `design/Electronics/Consolidated_BOM.md` | Complete rebuild — 200 rows, 115 MPNs |
| `design/Electronics/all_boards_bom.json` | CSD17578Q5A correction applied |
| `design/Electronics/Power_Module/Design_Spec.md` | Q1/Q2/Q3 MPN+PNs updated |
| `design/Design_Log.md` | DEC-047 added |
| `.copilot/handoff.md` | Session 077 summary added |
| `.copilot/checkpoints/077-*.md` | This file |
| `.copilot/checkpoints/index.md` | Row 077 added |

## Open items (not blocking)

- Footprint Downloaded column in BOM — user populates as KiCAD library is built
- `MCP121T-450E/LB` and `TPS75733KTTRG3` need manual KiCAD footprint creation
- Battery connector sourcing (Category C) — still awaiting supplier email responses

## Standing directives

- **PRIMARY DIRECTIVE**: NEVER modify any component MPN or supplier part number without explicit
  user confirmation.
- No web searches for component data. Order: markdown datasheet → local PDF → ask user.
- No version bumps without explicit user instruction.
- `Consolidated_BOM.md` is always derived from board specs, never the reverse.
- BOM source of truth: individual board `Design_Spec.md` files.
