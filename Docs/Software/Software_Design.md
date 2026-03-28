# Software Design Requirements

### 1. Core Framework
*   **Platform:** .NET 10.0 (C#) running on Raspberry Pi OS (64-bit).
*   **UI:** Cross-platform XAML/Avalonia-based "Museum" Dashboard.

### 2. Power Management
*   **Telemetry:** INA219 monitoring (I2C) for live rotor mA/Wattage display.
*   **Smart Battery:** SBS Linux driver integration for "Time-to-Empty" calculations.
*   **Shutdown:** GPIO-controlled "Safe Shutdown" sequence for the 3.3V Rotor rail.

### 3. Status Logic
*   **Heartbeat:** PWM-driven RGB LED fading between status colours.
*   **Diagnostics:** Real-time data bus visualisation on the GUI mirrors the physical loops.
