# Create Stack-Input Board Design

**ID:** merge-create-stack-input
**Status:** pending
**Category:** Electronics
**Source:** design-discussion-merge
**Blocked by:** design-discussion-merge, merge-grs-6layer-stackup

---

## Description

Create design files for the Stack-Input Board — the input-side board of each Rotor Mini-Stack.
Source circuits: EXT input-side + AM (native, not module-style).

## Notes

- Front (right edge): 1x QTS-025-01-L-D-RA-P male (mates with Cypher J3 or prev stack rear).
- Back (left edge): 1x QSS-025-01-L-D-RA-K female (mates with next stack or blanking board).
- Carries AM circuits natively (STM32G071 + motor driver).
- Ribbon/interposer link to Stack-Output for TTD_RETURN + ENC_DATA return path.
