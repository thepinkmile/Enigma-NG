# Create Cypher-Input Board Design

**ID:** merge-create-cypher-input
**Status:** pending
**Category:** Electronics
**Source:** design-discussion-merge
**Blocked by:** design-discussion-merge, merge-grs-6layer-stackup

---

## Description

Create design files for the Cypher-Input Board — the keyboard panel board. Accepts 1 ENC
module via Hirose DF40C BtB connectors. Carries MX-compatible keyboard switches on
opposite face with Kailh PG151101S11 hot-swap sockets.

## Notes

- Bottom edge: QTS-025-01-L-D-RA-P male connectors (chain to Cypher Board or Cypher-Output).
- Top edge: QSS-025-01-L-D-RA-K female connectors.
- 555 astable PWM oscillator for LED brightness (dial: Bourns 3310P-001-503L).
- 26 LEDs (Kingbright APFA2507Y2G2C-C2); P-MOSFET high-side switching (SQ2319ADS-T1_BE3).
- ENC module mounts: DF40C-90DS + DF40C-24DS + DF40C-10DS.
