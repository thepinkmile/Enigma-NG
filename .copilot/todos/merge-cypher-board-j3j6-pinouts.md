# Define full 50-pin allocation for Cypher Board J3-J6 connectors

**ID:** merge-cypher-board-j3j6-pinouts
**Status:** pending
**Category:** Electronics
**Source:** User review 2026-07-05
**Blocked by:** design-discussion-merge

---

## Description

Revisit J3, J4, J5, and J6 on the Cypher Board to define the full 50-pin contact allocation
for each QSS-025 / QTS-025 connector. Current specs define 24-26 contacts; pins 27-50 are
tied to GND as placeholders. User requires symmetric, fully specified allocations.

## Notes

- J3 and J4 have 50 contacts each (QSS-025-01-L-D-A-GP-K); currently 26 and 24 defined. **Still
  open** - this is the remaining scope of this todo.
- J5 and J6 have 50 contacts each (QTS-025-01-L-D-A-GP-K-TR); Entry 19 pin map defines all 50.
  **Resolved (2026-08-19):** both are now fully 50-pin allocated in `Cypher/Board_Layout.md §4`
  (J5 - Power/LED Broadcast/`BOARD_ROLE_ID`; J6 - JTAG/`ENC_DATA`/I2C/PWM, including this
  session's `TTD_HID_IN`/`TTD_HID_PASS`/`TTD_HID_OUT` rename and the I2C passthrough fix on
  Cypher-Output). No further action needed on J5/J6 - remaining scope is J3/J4 only.
- Update Board_Layout.md §2-§3 pinout tables and Design_Spec.md §3 Port Mapping when resolved
  (J3/J4 only - J5/J6 already updated).
- **Update from Cypher-Input session (2026-08-06):** `I2C_SCL_PASS`/`I2C_SDA_PASS` on J5/J6 are
  **no longer documented as a pure Plugboard-only passthrough**. Cypher-Input's own I2C GPIO
  expander (U4, PCA9534A @ 0x38 or 0x39 depending on variant) connects directly to this bus via
  J5, and Cypher-Output will need to do the same via J6 (see `merge-create-cypher-output.md`).
  When resolving this todo, reconcile the J5/J6 pin usage notes in `Cypher/Board_Layout.md §4`
  accordingly - these two pins are active on both Input/Output-Cypher, not NC/reserved.
  **Superseded (2026-08-19):** Cypher-Output's finished design has **no I2C bus connection at
  all** (confirmed, not the "will need to do the same" assumption above) - its own `I2C_SDA`/
  `I2C_SCL` pins on J5/J6 are a straight passthrough only, not consumed locally. This paragraph's
  original assumption is stale; see `Cypher-Output/Design_Spec.md §1`/§6 for the confirmed
  behaviour.
