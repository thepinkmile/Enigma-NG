# DEC-093 - `ACTUATE_REQUEST` End-to-End Signal Path Defined; J4 Renamed to REF-Specific Nets; Rotor/Stack-Interposer Connectors Extended

|Field|Value|
|:---|:---|
|**Decision ID**|DEC-093|
|**Status**|Decided|
|**Date**|2026-09-02|
|**Author**|Izzyonstage & GitHub Copilot|
|**Amends**|DEC-090 (Stack-Input wiring narrative only — pin positions unchanged), DEC-092 (J4 pin naming only — pin positions unchanged)|
|**Related**|DEC-091, DEC-045, DEC-048|

## Context

DEC-090/091/092 established the `ACTUATE_REQUEST_IN_N`/`ACTUATE_REQUEST_OUT_N` pin positions on
Cypher's `J3`/`J4` and Stack-Input's `J1`/`J2`, but left the actual end-to-end signal path
(through the Rotor boards, Stack-Output, and Stack-Interposer) as an open follow-up. The user
provided the complete logical flow, which mirrors the existing four-pass structure already used
for the `ENC_DATA`/cipher signal (forward via the STA/`J3` chain, reflect at the Stack-Blanking
Board, back via the REF/`J4` chain, CPLD reflection-map processing at Cypher, forward via the REF
chain again, reflect at the Blanking Board again, back via the STA chain in reverse rotor order).

## Decision

### 1. Full end-to-end signal path (originates and terminates at Cypher)

1. **Origination:** Cypher CPLD U1 asserts `ACTUATE_REQUEST_IN_N` on `J3` (pin 16), gated on
   `ENC_ACTIVE_N` (keypress-active, from Cypher-Input) per DEC-091.
2. **Forward pass (STA chain):** propagates through every Rotor Mini-Stack's Stack-Input (front,
   `J1`) → Rotor 1-5 → Stack-Output → Stack-Interposer → back to that same mini-stack's own
   Stack-Input rear connector (`J2`) → next mini-stack's `J1`, repeating until the Stack-Blanking
   Board.
3. **First reflection (Blanking → Cypher, REF chain):** the Stack-Blanking Board redirects the
   signal into the REF-side chain (Stack-Output boards only, direct passthrough, no rotors),
   propagating back through every mini-stack to Cypher's `J4`, arriving as
   `ACTUATE_REQUEST_REF_IN_N` (pin 16).
4. **CPLD reflection:** U1's firmware processes `ACTUATE_REQUEST_REF_IN_N` and drives
   `ACTUATE_REQUEST_REF_OUT_N` (pin 35) in response.
5. **Second forward pass (REF chain):** propagates forward again through the Stack-Output boards
   of every mini-stack back to the Stack-Blanking Board.
6. **Second reflection (Blanking → Cypher, STA chain, reverse rotor order):** the Stack-Blanking
   Board redirects the signal back into the STA-side chain, entering at the *last* mini-stack's
   Stack-Input *rear* connector (`J2` `ACTUATE_REQUEST_IN_N`), traversing the
   Stack-Interposer/Stack-Output/Rotor chain in reverse (right-to-left), back through every
   mini-stack to Mini-Stack 1's Stack-Input front connector (`J1` `ACTUATE_REQUEST_OUT_N`), and
   finally to Cypher's `J3` `ACTUATE_REQUEST_OUT_N` (pin 35), which terminates the loop **NC**.

### 2. Cypher `J4` renamed to REF-specific nets

`J4`'s actuate pins (same physical positions as `J3`: 16/35) are renamed from the generic
`ACTUATE_REQUEST_IN_N`/`OUT_N` (used in DEC-092) to `ACTUATE_REQUEST_REF_IN_N`/
`ACTUATE_REQUEST_REF_OUT_N` — logically distinct nets from `J3`'s, matching the existing
`ENC_IN_REF`/`ENC_OUT_REF` vs `ENC_IN_ROT`/`ENC_OUT_ROT` naming precedent (same connector family,
different port names per role). Pin positions and ESD channel assignments (U16) are unchanged
from DEC-092 — this is a naming-only correction.

### 3. Stack-Input `J1`/`J2` wiring corrected (no pin change)

The DEC-090 "NC" designations on `J1`'s `ACTUATE_REQUEST_OUT_N` and `J2`'s
`ACTUATE_REQUEST_IN_N` were premature (based on an incomplete assumption of a simple front-in/
rear-out passthrough). Per the full path above, **all four pins carry real traffic across two
passes**:

| Net | J1 (front) | J2 (rear) |
| :--- | :--- | :--- |
| `ACTUATE_REQUEST_IN_N` | Pass 1 (forward): received from Cypher/previous mini-stack → U1 (STM32G071) | Pass 2 (return): received from next mini-stack/Blanking Board → routed via this mini-stack's Interposer/Stack-Output/Rotor chain (reverse) to this board's own `J1` `ACTUATE_REQUEST_OUT_N` |
| `ACTUATE_REQUEST_OUT_N` | Pass 2 (return): delivers the signal from this board's own `J2` `ACTUATE_REQUEST_IN_N` onward to the previous mini-stack/Cypher `J3` (terminates NC there) | Pass 1 (forward): sourced from this mini-stack's own Rotor 1-5 chain via Stack-Output/Stack-Interposer; drives next mini-stack's `J1`/Blanking Board |

No connector or pin-count change on Stack-Input — this is a wiring-narrative correction only.

### 4. Rotor boards — `ACTUATE_REQUEST_IN_N`/`ACTUATE_REQUEST_OUT_N` added to `J3`/`J6`

Per the user's decision, these two nets are added to the **ENC data connector** (`J3` input side,
`J6` output side — 20-pin ERM8-010/ERF8-010), not the JTAG connector (`J1`/`J4`), since they are
logically part of the ENC/actuation control group rather than JTAG, and the JTAG connector has
insufficient spare capacity (only 1 spare pin per side vs. the 2 needed). The ENC connector's
existing 8 GND-fill pins (13-20) provide ample headroom:

- **`J3` (input, mates upstream):** pin 13 = `ACTUATE_REQUEST_IN_N` (forward pass, received from
  upstream), pin 14 = `ACTUATE_REQUEST_OUT_N` (return pass, driven back upstream) — mirrors the
  existing `ENC_IN`/`ENC_OUT` dual-direction pattern already used on this same connector.
- **`J6` (output, mates downstream):** pin 13 = `ACTUATE_REQUEST_IN_N` (return pass, received
  from downstream), pin 14 = `ACTUATE_REQUEST_OUT_N` (forward pass, driven to downstream).
- Both wired to CPLD U1; exact synthesis-time propagation logic (how a given Rotor decides IN→OUT
  routing per pass) is firmware-configurable and left for a future design pass, consistent with
  this system's fully-reconfigurable cipher-chain architecture (any Rotor can occupy any position;
  the CPLD's programmed configuration determines behaviour, not fixed wiring).
- **New ESD components required** (2 new channels needed per side; existing ENC-connector ESD
  arrays were fully utilised): **U12** (Board A, 4th ESD array on `J3`, 2 channels used/2 spare)
  and **U13** (Board B, 4th ESD array on `J6`, 2 channels used/2 spare) — both extra counts of the
  existing `TPD4E05U06QDQARQ1` part already used for U3-U10, no new part number.

### 5. Stack-Interposer — `ACTUATE_REQUEST` forward/return hop added

The passive 30-pin interposer connector (`J1`/`J2`, TMMH-115-01-L-D-ES) had ample spare GND-fill
capacity (pins 15-17, previously all GND guard around the `TTD` signal). Two of those three pins
are reused: pin 15 = `ACTUATE_REQUEST` forward (SIG-BLOCK-G, Stack-Output → Stack-Input), pin 16
= `ACTUATE_REQUEST` return (SIG-BLOCK-H, Stack-Input → Stack-Output); pin 17 remains GND guard.
No new component required — pure passive pin-to-pin connection, consistent with this board's
existing role.

## Rationale

- The `ACTUATE_REQUEST` signal's quad-pass structure deliberately mirrors the already-implemented
  `ENC_DATA`/cipher signal path, keeping the system's two "reconfigurable pipeline" signals
  (cipher data and actuation trigger) architecturally consistent.
- Placing the new Rotor-side signals on the ENC connector (not JTAG) keeps them associated with
  the connector family that already has spare capacity and matches their conceptual grouping
  (control signal accompanying the cipher/actuation data path, not the JTAG programming chain).
- Reusing existing spare GND-fill pins wherever available (Rotor's ENC connector, the
  Stack-Interposer connector) avoids new connectors/pin-count changes; where genuinely no spare
  ESD channel capacity existed (Rotor's ENC-side ESD arrays), reusing the same
  `TPD4E05U06QDQARQ1` part as an extra count (U12/U13) avoids introducing a new component.

## Open Item (Not Resolved by This Decision)

Firmware/CPLD synthesis-level propagation logic (exactly how each Rotor's CPLD, and Cypher's own
U1, decide `IN`→`OUT` routing for each of the two passes) is not defined here — this decision
only establishes the physical signal path and connector/pin allocations. Given this system's
fully-reconfigurable architecture (supporting arbitrary historical Enigma variant configurations
as well as the user's own 64-character variant), this propagation logic is expected to be
firmware-configurable rather than fixed.

**Next planned step:** review Stack-Output's own `J1`/`J2` stacking connectors (REF-side chain
equivalent of Cypher's `J4`) pin-by-pin, to place `ACTUATE_REQUEST_REF_IN_N`/
`ACTUATE_REQUEST_REF_OUT_N` there.

## Impact

- `Cypher/Board_Layout.md §3` (J4) — pins 16/35 renamed to `ACTUATE_REQUEST_REF_IN_N`/
  `ACTUATE_REQUEST_REF_OUT_N`; wiring note updated.
- `Cypher/Design_Spec.md §3, §4` — new full end-to-end path description; J4 ESD/wiring notes
  updated with renamed signals.
- `Stack-Input/Design_Spec.md` (FR-SIN-03/04, DR-EXT-02, DR-SIN-01, DR-SIN-02, §4 Actuation
  Request Chain, §6 Interconnects, mermaid diagram) and `Board_Layout.md` (§1, §2, §4) — NC
  designations removed, two-pass wiring described.
- `Rotor/Design_Spec.md` (§3.4 J3/J6 pin tables, §6 ESD section, BOM) and `Board_Layout.md`
  (§2.1/§3.1 component summaries, §5.1 connector summary, §6 CPLD signal map) — new
  `ACTUATE_REQUEST_IN_N`/`OUT_N` pins on J3/J6; new U12/U13 ESD components.
- `Stack-Interposer/Design_Spec.md` and `Board_Layout.md` — new SIG-BLOCK-G/H signals on pins
  15/16 of J1/J2.
- `merge-actuate-request-routing` todo — Cypher/Stack-Input/Rotor/Stack-Interposer legs resolved;
  Stack-Output leg remains open (see Next Planned Step above).
