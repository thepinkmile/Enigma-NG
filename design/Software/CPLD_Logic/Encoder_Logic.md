# Encoder CPLD Logic Requirements

**Status:** Draft
**Project:** Enigma-NG
**Author:** Izzyonstage & GitHub Copilot
**Version:** v.0.1.0
**Associated Hardware Revision:** Rev A
**Last Updated:** 2026-04-26

## 1. Overview

This document defines the intended **logic-level requirements** for the generic Encoder Module CPLD.
It captures the behaviour that the future VHDL implementation must provide once prototype boards
are available for timing and debounce tuning.

The active hardware direction is:

- one universal Encoder PCB per board position
- one Intel MAX II `EPM570T100I5N` per board
- role chosen by the programmed CPLD image
- sampled digital debounce in the **encode** image
- no external per-line RC debounce network on the active board design

Board-level connector ownership, physical placement, and BOM authority remain in:

- `design/Electronics/Encoder/Design_Spec.md`
- `design/Electronics/Encoder/Board_Layout.md`

## 2. Scope

This logic specification covers four behaviours:

1. **64-bit sampled debounce** for encode-role input banks
2. **64-to-6 encoding** for keyboard and plugboard encode roles
3. **`ENC_ACTIVE_N` generation / consumption** for HID roles
4. **6-to-64 decoding** for lightboard and plugboard decode roles

This document does **not** freeze the final VHDL syntax, timing-closure method, or Quartus project
structure. Those items are deferred until the first prototype boards exist and the practical
debounce constants can be measured.

## 3. Image Model and Board Role

The Encoder board is physically generic. Role is selected entirely by the CPLD image loaded onto the
board based on its known JTAG-chain position.

### 3.1 Required image families

| Image family | Used by | Primary function |
| :--- | :--- | :--- |
| `ENCODE` | `KBD_ENC`, `PLG_PASS1_ENC`, `PLG_PASS2_ENC` | Debounce and encode a one-of-64 input bank into `ENC_DATA[5:0]` |
| `DECODE` | `LBD_DEC`, `PLG_PASS1_DEC`, `PLG_PASS2_DEC` | Decode `ENC_DATA[5:0]` into a one-of-64 output bank |

### 3.2 Role-selection rule

- No DIP switch, jumper, or strap is required for role selection in the active design.
- No role-specific RC population is required on the PCB.
- Assembly identity is provided by:
  - the board's installed location
  - the harness connected to `BT1`-`BT64`
  - the CPLD image programmed into that board

## 4. Common Electrical Conventions

### 4.1 Signal bank

- `BT1`-`BT64` is always treated as a **64-bit logical bank** in the CPLD.
- Logical bank ordering must stay stable between encode and decode images.
- The VHDL implementation shall preserve a one-to-one mapping between bank bit index and external
  terminal number.

### 4.2 Encode-role polarity

- Encode-role input lines are **active-low**.
- Unasserted input = logic HIGH.
- Asserted input = logic LOW caused by a switch/jack closure.

### 4.3 Decode-role polarity

- Decode-role output polarity must match the board-level harness/electrical intent for the target
  assembly.
- Only one output line may be asserted at a time during normal operation.
- All non-selected outputs must remain inactive.

### 4.4 Input conditioning

- The encode-role implementation should enable the MAX II input-buffer features that best improve
  noise tolerance, including Schmitt-trigger behaviour where supported by the selected I/O standard.
- All encode-role input pins should have the MAX II **weak pull-up** configuration enabled so the
  idle state is held HIGH without requiring an external per-line pull-up bank.
- Bias strategy for idle-high inputs is therefore expected to use the MAX II weak pull-up setting as
  the active baseline, though schematic capture may still add external reinforcement later if
  prototype evidence shows it is necessary.
- The logic must assume active-low externally observed events.

### 4.5 Activity sideband convention

- `ENC_ACTIVE_N` is an **active-low** sideband on the generic Encoder connector.
- Idle / unused state = logic HIGH.
- Active HID event = logic LOW.
- The pin shall default HIGH through the MAX II weak pull-up behaviour or an equivalent schematic
  bias method if the role does not actively drive it.

## 5. 64-Bit Sampled Debounce Requirements

### 5.1 Design intent

Debounce is performed on the **observed 64-bit bank state**, not as 64 fully independent RC
emulators. This preserves LE headroom while still filtering key and plugboard contact chatter.

### 5.2 Required architecture

The encode image shall implement:

- a periodic sample tick
- a 64-bit raw sampled bank register
- a 64-bit candidate bank register
- a 64-bit debounced/stable bank register
- a small stability counter or equivalent stable-sample tracker

The design may derive the sample tick from:

- the MAX II internal oscillator path, or
- another logic-side clocking method selected during implementation

No external debounce timing RC is assumed.

### 5.3 Functional debounce behaviour

On each sample event:

1. Capture the raw 64-bit input bank.
2. Compare that sample against the current candidate bank.
3. If the sample differs from the candidate bank:
   - replace the candidate bank with the new sample
   - reset the stability counter
4. If the sample matches the candidate bank:
   - increment the stability counter
5. When the candidate bank has remained unchanged for the configured debounce threshold:
   - commit it into the debounced/stable bank

### 5.4 Tuning policy

Prototype testing must be allowed to tune:

- sample period
- number of consecutive matching samples required
- total debounce acceptance window

The active design intent is:

- reject short contact chatter
- accept real key/jack events quickly enough that the machine remains responsive
- avoid 64 separate long counters unless fitting results prove they are cheap enough

### 5.5 Resource rule

The debounce design should prefer:

- one shared sample-timebase
- one shared stability counter for the whole bank state
- bank-level state comparison

over:

- 64 independent counters or timers

unless prototype fit/timing review later proves a more granular scheme is both necessary and cheap.

## 6. Encode Logic Requirements (64-to-6)

### 6.1 Normal input assumption

The encode logic is designed around the normal operating assumption that **zero or one** bank line is
asserted at a time after debounce.

### 6.2 Required output

- The encode image shall produce `ENC_DATA[5:0]` from the debounced bank state.
- The mapping from bank index `0..63` to `ENC_DATA[5:0]` shall be deterministic and fixed.
- The mapping table must be documented in the final VHDL/package files used for implementation.
- The role-specific image shall also define the `ENC_ACTIVE_N` behaviour for that assembly position.

### 6.3 Invalid bank-state handling

The logic must define behaviour for:

- **no asserted line**
- **more than one asserted line**

The active requirement is:

- invalid bank states must **not silently alias** a different valid one-hot input
- the implementation may hold the previous valid output code, force a reserved diagnostic behaviour,
  or otherwise expose an internal invalid-state flag

The final invalid-state handling policy should be confirmed during prototype bring-up once the
Stator-side bus sampling behaviour is exercised end-to-end.

### 6.4 Keyboard-specific mapping

This subsection describes the **64-character keyboard** implementation of `KBD_ENC`.

For `KBD_ENC`:

- the physical assembly contains 40 populated switch positions
- the logical machine repertoire remains 64 characters:
  - `a-z`
  - `A-Z`
  - `0-9`
  - `+`
  - `=`

Required keyboard behaviour:

- Left Shift and Right Shift act as modifiers for alphabetic positions
- when either Shift input is active, alphabetic keys map to `A-Z`
- digits, `+`, and `=` are not remapped by Shift
- Shift keys are consumed as state modifiers rather than emitted as printable output codes
- `ENC_ACTIVE_N` shall be driven LOW only while a debounced printable keyboard event is active
- `ENC_ACTIVE_N` shall return HIGH for the idle state and for invalid / ambiguous bank states unless
  prototype testing later defines a different explicit diagnostic behaviour

Variant / extension notes:

- A separate **26-character Enigma-style keyboard** variant is also expected. That variant uses the
  same generic Encoder hardware but only a subset of the 64 available input pins, with the final
  logical mapping to be defined by its own dedicated keyboard-specific programming.
- The generic 64-input bank is intentionally broad enough to support other custom keyboard
  implementations for educational use.
- Beyond preserving that capability in the hardware platform, custom educational keyboard mappings
  are **out of scope** for the core Enigma-NG design logic and remain a classroom / follow-on
  activity.

### 6.5 Plugboard-specific mapping

For plugboard encode images:

- the encode result is the debounced logical identity of the currently asserted plugboard line
- no keyboard Shift remapping is involved
- `ENC_ACTIVE_N` is not used by the active Stator plugboard path and should therefore be held HIGH /
  inactive by the programmed image

## 7. Decode Logic Requirements (6-to-64)

### 7.1 Core function

The decode image shall accept `ENC_DATA[5:0]` and generate a one-of-64 output selection across
`BT1`-`BT64`.

### 7.2 Output rules

- exactly one output line is active for any valid 6-bit code
- all other output lines remain inactive
- output transitions should be monotonic and deterministic for each code change

### 7.3 Lightboard decode

For `LBD_DEC`:

- the decode image mirrors the HID logical code space
- uppercase alphabetic codes illuminate the same physical alphabetic lamp position used for the
  corresponding lowercase letter
- no separate uppercase-only lamp positions exist
- when `ENC_ACTIVE_N` is HIGH, all decode outputs must remain inactive regardless of the 6-bit code
- decode outputs may only illuminate a lamp while `ENC_ACTIVE_N` is LOW

### 7.4 Plugboard decode

For plugboard decode images:

- the 6-bit code selects exactly one destination line into the passive jack field
- identity continuity with the paired encode board must be preserved by the shared bank ordering
- `ENC_ACTIVE_N` is not used by the active plugboard decode path and may be ignored internally

## 8. Programming and Bring-Up Requirements

### 8.1 JTAG-chain use

- Each Encoder Module remains a standard MAX II device in the system JTAG chain.
- Programming software must load the correct image according to known board position.
- The active architecture assumes the programming flow, not local hardware switches, determines role.

### 8.2 Prototype work still required

The first hardware prototypes must be used to validate:

- actual contact bounce duration for keyboard switches
- actual bounce/noise behaviour of the plugboard jack path
- suitable sample period and debounce threshold
- encode invalid-state handling
- Quartus fit margin for the final encode image on `EPM570T100I5N`

## 9. Implementation Deliverables for Later VHDL Work

When implementation begins, the VHDL work should produce:

1. a shared package defining bank ordering and code mapping
2. one `ENCODE` image with sampled debounce and 64-to-6 logic
3. one `DECODE` image with 6-to-64 logic
4. simulation cases for:
   - clean one-hot transitions
   - bounce/noise sequences
   - simultaneous invalid presses
   - keyboard Shift behaviour
   - plugboard pass-through identity cases
