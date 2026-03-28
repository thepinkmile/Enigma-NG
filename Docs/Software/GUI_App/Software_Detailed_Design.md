# GUI Detailed Design & UX Decisions

### 1. Aesthetic (The "Digital Museum" Look)
*   **Font:** Authentic "Typewriter" monospaced font for all data readouts.
*   **Colour Palette:** "Enigma Green" (#004D40), Slate Grey, and Amber highlights.
*   **Bilingual Toggle:** A one-click switch to toggle all UI text between **DEUTSCH** and **ENGLISH**.

### 2. Diagnostic "Logic Analyser" View
*   **Feature:** A software-based logic analyser that mirrors the physical 2x8 Gold Diagnostic Bank.
*   **Usage:** Students can click a "Probe" button in the GUI to see the digital waveform of the D0-D11 bus in real-time.

### 3. Error Handling & Safety
*   **Rotor Jam Alert:** If the **AS5600** encoder detects a physical thumbwheel movement that doesn't align with the internal logic, the GUI flashes a **MECHANISCHE STÖRUNG** (Mechanical Jam) warning.
*   **Overload Trip:** If the **TPS259474L eFuse** trips, the GUI enters "Emergency Mode," displaying the fault reason (Over-current / Over-voltage).

### 4. Logging & History
*   **The "Daily Key":** Ability to export/import the machine configuration (Rotor order, Ring settings, Plugboard patches) as a "Codebook" PDF or JSON file.
