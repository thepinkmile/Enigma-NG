# Agent Directives — Enigma-NG

This file is the canonical list of standing rules and directives that govern how GitHub Copilot
(and any other AI agent) must behave when working on this repository. These rules take precedence
over any general defaults and must be loaded and followed in every session.

Read this file at session start alongside `.copilot/plan.md` and `.copilot/handoff.md`.

---

## PRIMARY DIRECTIVE — Part Number Protection

**NEVER modify any component MPN or supplier part number (Mouser SKU, DigiKey PN, JLCPCB C-number,
or any Alternative Supplier code) without explicit user confirmation.**

Every approved code in the design files and BOM is intentional and has been verified by the user.
Mouser in particular uses non-obvious abbreviations (e.g. dropping leading letters from TI MPNs).
These are correct. Do not "fix" them.

---

## Component Data Lookup Order

When researching any component, always use sources in this order:

1. **Reviewed markdown datasheet** — `design/Datasheets/<part>-datasheet.md`
2. **Local PDF datasheet** — `design/Datasheets/<part>-datasheet.pdf`
3. **Ask the user directly** — only if local sources are missing or insufficient

Do **not** perform web searches for component or supplier data. You will be rate-limited or blocked
and it wastes context budget. The user will provide any information that is not locally available.

---

## Version Metadata

Do **not** update any document `Version` field unless the user explicitly requests it. Do not infer
version bumps from the scope or significance of changes. The current baseline for all active docs
is `v.0.1.0`.

---

## Design Document Content Rules

- Design specs contain **current design only**. Do not preserve historical details in spec files.
- History belongs in `.copilot/checkpoints/` and `design/Design_Log.md`.
- Never change a component MPN without a corresponding local datasheet review in `design/Datasheets/`.
- Do not raise package-family or footprint-size differences as blocking issues until the user
  explicitly says schematic capture and layout have started. They are irrelevant at the pre-layout stage.
- Connector and mechanical-drawing datasheet markdowns can remain lightweight; fuller detail can
  wait until the initial KiCAD library generation phase.

---

## BOM Authority Rules

- Individual board `Design_Spec.md` files are the **authoritative source** for all component data.
- `design/Electronics/Consolidated_BOM.md` is a **derived document** — always rebuilt from board
  specs via `design/Electronics/all_boards_bom.json`. Never edit the consolidated BOM as a primary
  source and then work backwards.
- Supplier PN conventions confirmed by the user:
  - `TPD4E05U06QDQARQ1` → Mouser `595-PD4E05U06QDQARQ1` (drops leading `T`)
  - `LMQ61460AFSQRJRRQ1` → Mouser `595-Q61460AFSQRJRRQ1` (drops leading `LM`)
  - These are correct. Do not alter them.

---

## Repo-Local State Rules

- `.copilot/` is tracked in git and must stay in sync with meaningful design-state changes.
- At session start, read `.copilot/plan.md`, `.copilot/handoff.md`, and the latest relevant
  checkpoint(s) in `.copilot/checkpoints/`.
- A checkpoint is not complete until all of these are updated and consistent:
  - the new checkpoint file in `.copilot/checkpoints/`
  - `.copilot/checkpoints/index.md`
  - `.copilot/plan.md`
  - `.copilot/handoff.md`
- Sanitize all `.copilot/` content for version control: use repo-relative paths or
  `%USERPROFILE%` placeholders instead of machine-specific absolute paths. Do not persist raw
  usernames or session IDs.
- Repo-local helper scripts that should persist across sessions belong in `.copilot/agent-scripts/`.
  `design/Datasheets/_generated_markdown_inventory.json` is the full datasheet index — treat it as
  such, not as a partial single-run artifact.

---

## Review Suppression

The following items are intentionally suppressed from automated review cycles. Do not raise them
as findings until the referenced pre-condition is complete.

- **PM-H5 — battery connector suitability review:** The Molex 43650-0519 versus Glenair/ODU
  military replacement review is ongoing; supplier responses are still pending. Do not flag this
  as an issue until the connector review is complete and a decision is recorded in the Design Log.
  See `design/Electronics/Power_Module/Millitary_Battery_Connection_Option.md` for background.
