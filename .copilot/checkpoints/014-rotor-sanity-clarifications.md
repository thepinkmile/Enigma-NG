# Checkpoint 014 — Rotor Sanity Check, Clarifications Identified

**Date:** 2026-04-11
**Session:** Prior session (stub — original file not committed to repo)

---

## Overview

Initial Rotor Board sanity check. Multiple clarifications identified:
- "Threaded rod" description incorrect — rod is plain 8mm metal, horizontal stack only
- DIP switch architecture for notch position (gear shield) missing from spec
- Data bus width should not be hardcoded — defer to variant design files
- ENC bus described as pass-through — incorrect; J3→CPLD→J6 forward, J6→CPLD→J3 return
- UFM map selection via DIP switches (SW2/SW3) with direction bit for reverse map use
- Position encoder (AS5600 magnetic) questioned — single-track Gray code intent recalled

## Key Decisions

- Rotor stack is horizontal (aesthetics matching original Enigma machine)
- Plain 8mm rod = mechanical support only, not threaded
- Variant design files: Rotor_26_Char_Design.md + Rotor_64_Char_Design.md
- SW2 (input/forward) + SW3 (output/return): 5 map bits + 1 direction bit = 42 effective configs
- SW1 (input side only) = ring setting / notch position offset
