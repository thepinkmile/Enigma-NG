# Add 6-layer board stackup section to GRS

**ID:** merge-grs-6layer-stackup
**Status:** pending
**Category:** Standards
**Source:** design-discussion-merge; Cypher Board DR-CYP-01
**Blocked by:** design-discussion-merge

---

## Description

Add a new stackup definition section (GRS §2.3.x) to design/Standards/Global_Routing_Spec.md
for 6-layer / 2oz copper boards. The Cypher Board is the first board requiring this stackup.

## Notes

- Reference manufacturer: PCBWay (JLCPCB does not support 6-layer + double-sided assembly).
- Layer mapping TBD; driven by routing density of consolidated Stator + Reflector + JM circuits.
- Once done, update Cypher Board DR-CYP-01 to reference the new GRS section.
