# Research USM buzzer/audio hardware options (piezo vs speaker+amp)

**ID:** `usm-buzzer-audio-options`
**Status:** pending
**Category:** Electronics / Architecture Review
**Source:** User request, 2026-09-16 (part of the wider USM redesign discussion)
**Blocked by:** None — informational research todo; feeds into the USM redesign once actioned

---

## Description

The redesigned User Settings Module (USM) is gaining a buzzer/speaker so the CM5 can play
warning tones for conditions like "Invalid Plugboard Configuration" or "Invalid HID Components
Connected". The user wants full user-controlled volume (not just a single fixed loudness), the
ability to go fully quiet, and an authentic "old electromechanical device" sound character even
though the alert is digitally triggered.

This todo tracks producing a pros/cons comparison of the two realistic hardware approaches before
a part/topology decision is made — no decision has been made yet, this is purely a research pass.

## Option A — Simple piezo buzzer

- Single GPIO/PWM-driven piezo element (magnetic or ceramic), driven directly or through a small
  transistor stage.
- Cheap, minimal BOM impact, easy to integrate with whatever expander/CPLD/MCU logic already
  exists on USM for tone-pattern generation (spare pin).
- **Open question:** true continuous volume control is not straightforward on a piezo element —
  loudness is mostly a function of drive voltage/resonant frequency, not amplitude in the way a
  speaker+amp works. Practical volume control options to evaluate:
  - Switched series-resistor ladder (a few discrete volume steps, e.g. 3-4 levels)
  - Digital potentiometer between drive stage and element
  - PWM duty-cycle modulation (has some perceptible effect on piezo elements, but less linear
    than on a true speaker)
- Sound character: piezo elements naturally produce a thin, "electronic beep" tone — may need
  shaping (multiple tone frequencies, envelope shaping) to sound convincingly "old
  electromechanical" rather than a modern smoke-alarm-style chirp.

## Option B — Small speaker + audio amplifier

- Small speaker driven by a dedicated audio amplifier IC (e.g. a simple Class-D or Class-AB mono
  amp), fed either a PWM-synthesised tone or a stored/synthesised audio sample.
- Enables genuine continuous/smooth volume control via standard means (digital volume control on
  the amp IC, or an analog volume pot in the audio path) — matches the user's "full user control
  of volume" requirement more naturally than a piezo.
- Can authentically reproduce an old electromechanical relay/buzzer/bell character (or even a
  short sampled/synthesised sound clip) rather than being limited to simple square-wave tones —
  better fit for the "must sound like an old device" requirement.
- Meaningfully more hardware: amplifier IC, speaker (with associated mounting/enclosure acoustic
  design), decoupling/filtering, and a way to feed it audio (PWM tone generation is simplest;
  actual sampled audio would need more memory/DAC/storage on whatever is driving it).
- Higher BOM cost and board area than Option A.

## What this research pass needs to produce

1. Side-by-side pros/cons table (cost, BOM complexity, board area, achievable volume control
   granularity, achievable sound authenticity, integration complexity with whatever USM control
   logic is chosen).
2. Candidate part(s) for each option (piezo element + driver transistor for A; amplifier IC +
   small speaker for B), with datasheets added to `design/Datasheets/` per the usual convention.
3. A recommendation, left for the user's final decision — this todo does not pre-select an option.

## Notes

- This sits within the wider USM redesign discussion — see `.copilot/discussions/usm-redesign/`
  for the connector topology and LED colour-control context this todo's decision will need to fit
  alongside (e.g. whichever expander/CPLD/MCU ends up driving the buzzer/speaker may already be
  decided by the LED-colour-storage discussion, which could constrain or simplify this choice).
- Requirement re-stated for clarity: (1) full user-controlled volume, (2) must be able to go fully
  quiet, (3) must sound authentically "old device", not modern digital chime.
