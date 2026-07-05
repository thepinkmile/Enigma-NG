# Define USB D+/D- pin allocation in Cypher Board J1 CTL dock

**ID:** merge-ctl-dock-usb-allocation
**Status:** pending
**Category:** Electronics
**Source:** Design_Spec.md; User review 2026-07-05
**Blocked by:** design-discussion-merge

---

## Description

Define the exact pin allocation for USB D+/D- within the J1 (5V power dock, Molex 2195620015)
on the Cypher Board. USB D+/D- must travel via the CTL dock to reach the CM5 USB 2.0 port.

## Notes

- USB D+/D- confirmed on J1 (power dock) per Board_Layout.md §1 2026-07-05 edit.
- CTL Board must be updated to route USB D+/D- from Cypher Board J1 to CM5.
- Exact J1 blade/signal contact assignment to be defined alongside CTL Board update.
- See merge-update-ctl-board which depends on this todo.
