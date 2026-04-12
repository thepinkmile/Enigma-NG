# Checkpoint 016 — Stator Reflector Map, Position Encoder Open

**Date:** 2026-04-11
**Session:** Prior session (stub — original file not committed to repo)

---

## Overview

Stator CPLD upgraded to EPM570T100I5N (matching Rotor). Internal reflector map capability added
to Stator: SW2 on Stator selects an active substitution map from UFM to apply to reflector-bound
data (mimicking the original Enigma reflector swap — 3 original reflector variants). One DIP
switch enables the map or passes data directly. Position encoder technology for Rotor left open
pending discussion (AS5600 magnetic vs single-track capacitive).

## Key Decisions

- Stator CPLD EPM240 → EPM570T100I5N
- Stator SW2 (new): enables internal reflector map substitution
- Reflector map: 1 enable switch + map-select switches; fallback = direct pass-through
- Position encoder decision: DEFERRED (open question going into checkpoint 017)
