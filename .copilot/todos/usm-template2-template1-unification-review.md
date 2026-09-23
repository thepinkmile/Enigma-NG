# Reviewing whether USM hub connector should reuse the HID left-pair pin map for future flexibility

**ID:** usm-template2-template1-unification-review
**Status:** pending
**Category:** Electronics / Architecture Review
**Source:** User request, 2026-09-21

---

## Description

User question raised during USM design review (2026-09-21): the USM Hub Connector Template
(`J1`/`J2`, mating Cypher and Cypher-Plugboard) currently carries a distinct, smaller pin set
(`3V3_ENIG`, the dedicated Cypher-peripherals I2C bus, JTAG) compared to the Cypher Left Pair
Template (the Cypher-to-HID-board left-pair connector, owned by `Cypher/Board_Layout.md`, which
additionally carries `5V_MAIN`, `BOARD_ROLE_ID`, and `ENC_DATA`/`ENC_ACTIVE`).

Since the Hub Connector Template carries a subset of the same signal categories, consider whether
it should instead reuse the Cypher Left Pair Template's full pin map verbatim, marking any pins not
currently needed by the hub connectors (e.g. `5V_MAIN`, `BOARD_ROLE_ID`, `ENC_DATA`/`ENC_ACTIVE`)
as NC for the current implementation.

**Rationale:** this would let future design changes (e.g. moving/adding signals between the hub
and HID boards) happen without reworking connector pinouts, since all board-to-board connectors in
the Cypher HID assembly would share one physical/pin-map standard.

Explicitly NOT to be actioned without further discussion - this todo exists only to capture the
idea for a future review pass.
