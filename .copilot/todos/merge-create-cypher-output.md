# Create Cypher-Output Board Design

**ID:** merge-create-cypher-output
**Status:** pending
**Category:** Electronics
**Source:** design-discussion-merge
**Blocked by:** design-discussion-merge, merge-grs-6layer-stackup

---

## Description

Create design files for the Cypher-Output Board — the lightboard panel board. Accepts 1 ENC
module via Hirose DF40C BtB connectors. Carries LEDs on opposite face.

## Notes

- Mirror shape/layout to Cypher-Input board.
- Bottom edge: QTS-025-01-L-D-RA-P male connectors.
- Top edge: QSS-025-01-L-D-RA-K female connectors.
- 26 LEDs (Kingbright APFA2507Y2G2C-C2); active-low from ENC outputs.
- LED brightness dial: shared PWM from Cypher-Input GREEN_PWM_N / YELLOW_PWM_N.
