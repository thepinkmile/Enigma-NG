# Checkpoint 011 — PWR_BUT Circuit, SW2 Fix, PMIC_EN Glitch Resolved

**Date:** 2026-04-10
**Session:** Prior session (stub — original file not committed to repo)

---

## Overview

Power Module sanity check continuation. SW2 rewired from GLOBAL_EN to PWR_BUT for graceful
shutdown. R14 threshold raised to 4.644V (ERA-3ARB2872V) to prevent PMIC_EN glitch.
U15 MIC1555 monostable one-shot added to extend PWR_BUT pulse to 3.01 s.
New components: U15 MIC1555YM5-TR (PM=2 total), Q5 BSS138 (PM=2 total),
C33 0.1µF X7R 0402 bypass (PM=15, Total=509).

## Key Commits

See commit log for exact SHAs — original checkpoint file not committed.

## Key Decisions

- SW2 → PWR_BUT (not GLOBAL_EN / hard reset)
- LTC3350 BACKUP threshold: 4.644V via R14=28.7kΩ (ERA-3ARB2872V)
- PWR_GD = telemetry only; does NOT trigger shutdown
- Primary shutdown: LTC3350 /INTB → U15 MIC1555 → Q5 BSS138 → PWR_BUT (3.01 s)
- Link-Alpha pin 48: PWR_BUT (was GND)
