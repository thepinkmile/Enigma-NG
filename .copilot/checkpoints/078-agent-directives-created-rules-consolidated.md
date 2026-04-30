# Checkpoint 078 — Agent directives file created, operational rules consolidated

## Status

All work committed and clean. Commit: `75a77b3`

## What was done

### `.copilot/agent-directives.md` created

A new canonical file consolidates all standing operational rules that govern how the agent must
behave on this repository:

- **PRIMARY DIRECTIVE** — never modify any MPN or supplier part number without explicit user confirmation
- Component data lookup order (markdown datasheet → local PDF → ask user; no web searches)
- Version metadata policy (no bumps unless user explicitly requests)
- Design document content rules (current state only; no package-size blocking pre-layout)
- BOM authority rules (board specs are authoritative; consolidated BOM is derived)
- Supplier PN conventions (Mouser prefix-dropping patterns)
- Repo-local state rules (`.copilot/` sync, checkpoint hygiene, path sanitisation)
- Review suppression list (PM-H5 battery connector review deferred pending supplier response)

### Plan and handoff updated

- `plan.md` session-start instructions now reference `agent-directives.md`
- `plan.md` Component/MPN and lookup-order bullet points replaced with a cross-reference to avoid duplication
- `handoff.md` Documentation policy and Review suppression sections replaced with a single
  "Standing Directives" reference block pointing at `agent-directives.md`

### BOM PRIMARY DIRECTIVE removed

The PRIMARY DIRECTIVE line was removed from `design/Electronics/Consolidated_BOM.md`
Notes and Conventions section. It is an agent rule, not a design convention, and has no place
in a design document.

## Files changed

| File | Change |
| --- | --- |
| `.copilot/agent-directives.md` | Created — canonical agent rules file |
| `.copilot/plan.md` | Added agent-directives reference; removed duplicate rule bullets |
| `.copilot/handoff.md` | Replaced policy/suppression sections with Standing Directives block |
| `design/Electronics/Consolidated_BOM.md` | Removed PRIMARY DIRECTIVE from Notes section |

## Next session

- Read `.copilot/agent-directives.md` at session start alongside plan.md and handoff.md
- Next checkpoint: 079
- Next DEC: DEC-048
- Remaining open work: KiCAD library footprint downloads (user populates Footprint Downloaded column),
  `MCP121T-450E/LB` and `TPS75733KTTRG3` manual footprint creation, PM-H5 battery connector
  resolution pending supplier responses
