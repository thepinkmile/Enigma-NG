# TEMP - Key Mapping Review (moved from Encoder Module Design_Spec.md §6)

**Status:** Draft - pending user review
**Project:** Enigma-NG
**Author:** Izzyonstage & GitHub Copilot
**Version:** v.0.1.0
**Associated Hardware Revision:** Rev A
**Last Updated:** 2026-08-13

---

> **Why this file exists:** this content was formerly `Encoder/Design_Spec.md §6 Key Mapping`. It
> described the 64-character/40-position keyboard mapping when the Encoder board still hosted the
> keyboard switches directly. Now that keyswitches live on the Cypher-Input Board and the Encoder
> Module is a generic CPLD-only interface, this key-mapping content needs to be reviewed against
> the current Cypher-Input variant designs (`Cypher_Input_26_Char_Design.md`,
> `Cypher_Input_64_Char_Design.md`, `Cypher_Input_10_Numeric_Design.md`) before it is folded back
> into the active design docs (or superseded by content already defined there). Placed here
> (Cypher-Input folder) as a temporary holding file per user instruction, pending that review. This
> file is **not** part of the active design and should not be treated as authoritative.

---

## Original Section 6 - Key Mapping (64-Character Code Space with 40-Position HID Layout)

The encode-role Encoder Module maps the HID assembly's physical switch positions to the parallel
6-bit data bus while preserving the machine's 64-character logical repertoire.

> **Variant note:** this section describes the active **64-character keyboard** implementation. The
> same generic Encoder hardware may also support a separate **26-character Enigma-style keyboard**
> variant using only a subset of the 64 available input pins, plus other custom educational
> keyboard mappings. Those alternative mappings require their own dedicated CPLD programming and are
> not fully specified by the active 64-character keyboard logic below.

- **Layout:** QWERTY-derived 40-position HID panel consisting of 38 printable keys
  (`[a-z0-9+=]`) plus Left Shift and Right Shift.
- **Logical repertoire:** the system still exposes 64 unique character codes:
  26 lowercase letters + 26 uppercase letters + 10 digits + `+` + `=`.
- **Signal polarity:** encode-role lines are **active-low**. Each CPLD input shall idle HIGH via
  the MAX II weak pull-up input-bias configuration or an equivalent schematic-level bias method
  chosen during schematic capture. A key press or sensed jack closure then pulls the CPLD input LOW.
- **Activity sideband polarity:** `ENC_ACTIVE_N` is **active-low**. The idle / unconnected / unused
  state is HIGH. `KBD_ENC` drives it LOW only while a debounced keypress is active. `LBD_DEC`
  treats HIGH as "blank all outputs."
- **Weak pull-up justification:** the active design assumes the MAX II weak pull-up setting is
  sufficient for the Encoder input bank because the Stator<->Encoder ribbon link is expected to stay
  short (roughly **5-15 cm** in the finished machine), and prior bench work with a MAX II
  development board already showed stable operation over roughly **25 cm** of ribbon to a
  breadboard. External per-line pull-up resistors are therefore intentionally omitted from the
  active baseline unless prototype boards later demonstrate a real noise problem.
  > **Note:** this rationale predates the BtB-connector redesign (Encoder Module -> Cypher-Input
  > via Hirose DF40C, not a ribbon cable to the Stator) - review whether the short-link assumption
  > still holds for the new interconnect before reusing this justification.
- **Debouncing:** encode-role debounce is performed in CPLD logic using sampled 64-bit bank
  filtering rather than external per-line RC networks. The detailed debounce architecture and
  prototype-tuning requirements live in `design/Software/CPLD_Logic/Encoder_Logic.md`.
- **Shift Logic:** Left Shift and Right Shift act as logic-level triggers for the CPLD state
  machine. When either Shift key is held, alphabetic key positions map to `A-Z` instead of `a-z`.
  Digits and `+` / `=` remain unchanged.
- **Lightboard mapping:** the decode-role lightboard module mirrors the same QWERTY-derived
  printable positions. Uppercase alphabetic outputs illuminate the corresponding alphabetic lamp
  position rather than a separate uppercase-only physical position. When `ENC_ACTIVE_N` is HIGH, all
  lightboard outputs remain inactive regardless of the 6-bit bus value.

> For keyboard switch mechanical specification and panel assembly, see
> `design/Mechanical/Keyboard_Assembly/Design_Spec.md` (also likely stale - references the old
> Encoder-mounted switch architecture; not updated as part of this change).

---

## Review Questions for User

1. Does the 64-Character Cypher-Input variant's key mapping (base64 RFC 4648 alphabet,
   `Cypher_Input_64_Char_Design.md`) supersede this section's 64-character/40-position QWERTY
   mapping entirely, or is some of this logic (e.g. Shift-key state machine description) still
   needed as shared reference material?
2. Does the 26-Char Classic variant's mapping already cover the "26-character Enigma-style
   keyboard" variant mentioned in the note above, making that note redundant?
3. Should the weak-pull-up/short-link justification be re-verified for the new BtB interconnect,
   or superseded by a different justification specific to the Hirose DF40C link?
4. Where should the surviving content (if any) live once reviewed - back into
   `Encoder_Module/Design_Spec.md`, split across the per-variant Cypher-Input design files, or into
   `design/Software/CPLD_Logic/Encoder_Logic.md`?

Once reviewed, this file should be either folded into the appropriate active design doc(s) or moved
to `.recycle-bin/` (with user confirmation) if fully superseded.
