# DEC-094 - Connector Ownership Reassignment for Reused Chain Templates (Amends DEC-018)

|Field|Value|
|:---|:---|
|**Decision ID**|DEC-094|
|**Status**|Decided|
|**Date**|2026-09-02|
|**Author**|Izzyonstage & GitHub Copilot|
|**Amends**|DEC-018 (Connector Pinout Ownership Model) — extends the Ownership Register for the current Cypher-family board set; does not change the underlying single-owner/cross-reference rule|

## Context

DEC-018 established that every multi-board connector interface must have a single **Definition
Owner** board holding the authoritative pin table, with every other board carrying only a short
cross-reference note — never a duplicated table. In practice, for the connectors introduced by the
Cypher-Stack architecture (DEC-084 onward), this rule was not being followed correctly:

- Cypher's `Board_Layout.md` held the full pin tables for `J3` (IC-STA-CHAIN) and `J4`
  (IC-REF-CHAIN), with Stack-Input and Stack-Output cross-referencing *back* to Cypher.
- When Cypher's side was updated (DEC-090 through DEC-093), Stack-Output's own documentation
  went stale — it still read "pending... see `merge-cypher-board-j3j6-pinouts`" for a todo that
  had already been closed, and its `J6` interposer cross-reference still said "TBD — board not
  yet created" for a board that already exists.

The user identified the root cause: `J3`/`J4` are not simple two-board point-to-point links (the
case DEC-018's original register was designed around) — they are **templates reused identically
at every junction along a variable-length chain** (Cypher → Stack-Input/Stack-Output → next
mini-stack → ... → Stack-Blanking Board). Ownership should sit with the board that is the
**repeatedly-instantiated element** of the chain, not the singular endpoint (Cypher), since that
is the board whose own connectors (front *and* rear) must already stay internally consistent with
each other.

## Decision

The DEC-018 Ownership Register is extended with the following entries for the Cypher-family
board set:

| Interface | Connector(s) | Definition Owner | Authoritative Section |
| :--- | :--- | :--- | :--- |
| **IC-STA-CHAIN** | Cypher `J3` ↔ every Stack-Input `J1`/`J2` ↔ Stack-Blanking Board (QSS/QTS-025, 50-pin) | **Stack-Input** | `Stack-Input/Board_Layout.md §1` |
| **IC-REF-CHAIN** | Cypher `J4` ↔ every Stack-Output `J1`/`J2` ↔ Stack-Blanking Board (QSS/QTS-025, 50-pin) | **Stack-Output** | `Stack-Output/Board_Layout.md §1` |
| **IC-ROT-JTAG** | Rotor `J1`/`J4` ↔ Stack-Input `J3` ↔ Stack-Output `J3` (ERM8/ERF8-005, 10-pin) | **Rotor** *(unchanged — already correct per DEC-018)* | `Rotor/Design_Spec.md §3.4` |
| **IC-ROT-ENC** | Rotor `J3`/`J6` ↔ Stack-Input `J5` ↔ Stack-Output `J5` (ERM8/ERF8-010, 20-pin) | **Rotor** *(unchanged)* | `Rotor/Design_Spec.md §3.4` |
| **IC-ROT-PWR** | Rotor `J2`/`J5` ↔ Stack-Input `J4` ↔ Stack-Output `J4` (ERM8/ERF8-005, 10-pin) | **Rotor** *(unchanged)* | `Rotor/Design_Spec.md §3.4` |
| **IC-INTERPOSER** | Stack-Input `J6` ↔ Stack-Interposer `J2`; Stack-Output `J6` ↔ Stack-Interposer `J1` (SQT-115/TMMH-115/2BHR-30-VUA, 30-pin) | **Stack-Interposer** *(confirmed — corrects a stale "TBD, board not yet created" cross-reference)* | `Stack-Interposer/Board_Layout.md §1`/§2 |
| **IC-HID** | Cypher `J5`/`J6` ↔ Cypher-Input/Cypher-Output (QSS/QTS-025, 50-pin) | **Cypher** *(unchanged — already correct per existing practice)* | `Cypher/Board_Layout.md §4` |

The underlying DEC-018 rule (single owner, no duplicated tables, short cross-reference elsewhere)
is unchanged — this decision only reassigns *which* board is the owner for `IC-STA-CHAIN` and
`IC-REF-CHAIN`, and confirms/corrects the existing entries for the other four interfaces.

## Rationale

- **Repeatedly-instantiated board owns the template.** Stack-Input's own `J1` and `J2` must
  already be mutually consistent (same template, I/O inverted) independent of Cypher — Cypher is
  just one of several boards that mate with this template (the others being every subsequent
  Stack-Input in the chain). The same logic already existed in DEC-018 for the Rotor Interface
  ("the Rotor defines its own physical interface... Stator/Extension/Reflector must comply with
  the Rotor's mechanical interface, not the other way round") — this decision applies that same
  reasoning consistently to `IC-STA-CHAIN`/`IC-REF-CHAIN`.
- **No new central document.** A single shared "Connector Interface Contracts" document was
  considered and rejected, consistent with DEC-018's own prior rejection of a central
  `Interfaces.md` — keeping each canonical table on the board that owns it (not in a separate
  document) keeps definitions next to the schematic/layout work that depends on them.
- **Correcting the drift found in this pass** (stale Stack-Output references) is a direct
  consequence of putting the tables in the correct place rather than the wrong one — the previous
  ownership direction actively made it easy to forget to update the "downstream" boards.

## Impact

- `Cypher/Board_Layout.md §2/§3` — `J3`/`J4` sections reduced to a cross-reference + Cypher's own
  local wiring notes only; full pin tables removed (moved to the new owners).
- `Stack-Input/Board_Layout.md §1` — now holds the canonical IC-STA-CHAIN pin table (moved from
  Cypher), plus this board's own wiring notes for `J1`/`J2`.
- `Stack-Output/Board_Layout.md §1`, `Design_Spec.md` — now holds the canonical IC-REF-CHAIN pin
  table (moved from Cypher); stale "pending `merge-cypher-board-j3j6-pinouts`" and "TBD — board
  not yet created" references corrected. `ACTUATE_REQUEST_REF_IN_N`/`REF_OUT_N` internal wiring
  on this board is explicitly flagged as not yet defined (tracked in `merge-actuate-request-routing`).
- No pin position, signal name, or electrical change of any kind — this is a documentation
  ownership/location correction only.
