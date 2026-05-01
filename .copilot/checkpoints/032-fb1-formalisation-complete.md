# Checkpoint 032 — FB1 Formalisation Complete

**Status:** FB1 part selection and formalisation complete. Pass 2 BOM/refdes backlog pending.

## What was done

FB1 (GND↔GND_CHASSIS single-point bond ferrite bead) on the Power Module is now fully
specified and documented.

### Files changed

- `design/Datasheets/TE-DS_1773178-3_A3-datasheet.md` — **created** (10-page BMC-Q series
  datasheet, reviewed summary + page-by-page extraction)
- `design/Datasheets/_generated_markdown_inventory.json` — TE-DS entry added to
  `pdf_to_markdown` array (alphabetical position: between TE-2007435-1 and TI-sn74lvc1g08)
- `design/Electronics/Power_Module/Design_Spec.md` — FB1 prose updated (lines 327-329):
  "part to be selected" replaced with "BMC-Q2AY0600M / TE 2-2176748-1"; BOM row added
  after F1 with full specs and datasheet cross-reference
- `design/Electronics/Consolidated_BOM.md` — FB1 row added after F1 (line 50)

### FB1 confirmed part

| Field | Value |
| :--- | :--- |
| MPN | BMC-Q2AY0600M (2-2176748-1) |
| Manufacturer | TE Connectivity |
| DigiKey | 1712-2-2176748-1CT-ND |
| Mouser | 279-BMC-Q2AY0600M |
| JLCPCB | Global sourcing / consignment only |
| Z @ 100 MHz | 600 Ω ±25% |
| DCR max | 0.100 Ω |
| Rated current | 2000 mA |
| Package | 0805 |
| Qualification | AEC-Q200 Grade 1, MIL-STD-202 env. tested |

### Lint result

Two pre-existing MD060 errors on J1-J3 rows (missing space after `|`) in both files —
not introduced by this session. New rows lint clean.

## Still pending (Pass 2 backlog)

### BOM ordering / refdes simplification

Identified issues (read-only analysis from prior session — not yet actioned):

**JTAG Daughterboard (Design_Spec.md BOM)**
- C10–C12 rows appear after U rows; should precede U rows (alpha order)
- Simplifiable: C10-C11 (consecutive)

**Encoder Board (Design_Spec.md BOM)**
- BT, D, R row ordering issues (need to verify exact order)

**Rotor Board A + B**
- User decision needed: functional grouping vs strict alpha-numeric ordering

**Stator Board**
- R33–R38 position incorrect
- Simplifiable: R39-R41, R42-R43

**Power Module**
- Major reorder needed (multiple ref prefix groups out of order)

**Settings Board**
- Q1–Q6: user decision needed — individual rows vs range row

**Consolidated_BOM.md** (same ordering issues reflected from board specs)

### Other Pass 2 items

- Settings_Board → User_Settings_Module rename (~17 files + Design_Log DEC entry)
- Mark CSD17578Q5A and TPS25751DREFR footprints as downloaded in Consolidated BOM

### Commit

All accumulated Pass 2 fixes awaiting "Let's lock this in" confirmation.

## Decisions & directives carried forward

- Murata: banned manufacturer (all families) — in agent-directives.md
- No component additions/changes without user confirmation — PRIMARY directive
- TDK and Würth not banned; "no military" boilerplate is universal, not a disqualifier
- TE BMC-Q series tests to MIL-STD-202 methods despite commercial disclaimer
- Version metadata: only update when user explicitly requests it
