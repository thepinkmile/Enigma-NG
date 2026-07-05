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

- J3 and J4 have 50 contacts each (QSS-025-01-L-D-A-GP-K); currently 26 and 24 defined.
- J5 and J6 have 50 contacts each (QTS-025-01-L-D-A-GP-K-TR); Entry 19 pin map defines all 50.
- Update Board_Layout.md §2-§4 pinout tables and Design_Spec.md §3 Port Mapping when resolved.
