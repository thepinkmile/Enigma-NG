# CPLD production replacement review

**ID:** `cpld-production-replacement`
**Status:** pending
**Category:** Electronics
**Source:** OA-04, `design/Standards/Certification_Evidence.md`
**Blocked by:** None — unblocked 2026-09-11, no longer deferred to v2.0

---

## Description

Review replacement CPLD for production stage (current MAX II EPM570 is a prototype-grade
selection); update Certification Evidence §7.1 when confirmed.

Now active: this discussion is part of the `max-10-fpga-details` and (partially) the
`rp2040-discussion` discussion threads (see `.copilot/discussions/max-10-fpga-details/` and
`.copilot/discussions/rp2040-discussion/`).

## Notes

User has started looking at the MAX 10 device as a replacement.
The aim is to increase the LEs available to allow more versitility and include an I2C state machine within the CPLD to allow for direct configuration using less wires.
