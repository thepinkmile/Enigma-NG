# Update CTL Board Design — remove JM and AM sub-systems

**ID:** merge-update-ctl-board
**Status:** pending
**Category:** Electronics
**Source:** design-discussion-merge
**Blocked by:** design-discussion-merge, merge-ctl-dock-usb-allocation

---

## Description

Update design/Electronics/Controller/Design_Spec.md and related files to remove the JTAG
Module circuit (DF40C-20 BtB for JM) and the AM attachment connector (J11, DF40). Add USB
D+/D- routing via J1 CTL dock to Cypher Board.

## Notes

- JM DF40C-20 socket removed from CTL (JM circuit now on Cypher Board).
- AM DF40 J11 removed from CTL entirely — AM is native to Stack-Input Board.
- Link-Beta connector now targets Cypher Board instead of Stator.
- USB D+/D- pin allocation: see merge-ctl-dock-usb-allocation.
