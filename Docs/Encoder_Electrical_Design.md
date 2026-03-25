# I/O CPLD Electrical Design

### 1. Power Requirements
*   **Core:** 3.3V (Logic) & 1.8V (Internal) if required by CPLD variant. 
*   **Filtering:** Dedicated 0.1µF X7R decoupling per VCC pin.
*   **Protection:** AP22652 current-limited 3.3V rail from the Controller Board.

### 2. The Shift Mechanism
*   **Implementation:** The Shift keys (Left/Right) act as logic-level triggers for the CPLD state machine.
*   **LED Drive:** CPLDs directly drive the **Shift Status LEDs** and the 64-character lamp matrix (via MOSFET arrays).

### 3. Plugboard Jack-Sensing
*   **Logic:** The CPLD monitors 64 "Interrupt" lines from the Jack-Sensing sockets. 
*   **Latency:** Sub-microsecond detection of "Stecker" cable insertion, updating the internal encryption matrix instantly.
