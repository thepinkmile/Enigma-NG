# Enigma-NG Board Architecture

The Enigma-NG system consists of two primary interconnected PCBs designed for "Museum-Grade" durability and high-speed encryption logic.

### 1. Controller Board (Master)
*   **Role:** System brain, power management, and user interface.
*   **Core:** Raspberry Pi CM5.
*   **Key Features:** 6-layer ENIG stackup, 11V–17V protected power rail, HDMI/USB/PoE connectivity.

### 2. Stator Board (Interface & Distribution)
*   **Role:** High-current distribution to the 30-rotor stack and external I/O.
*   **Mating:** Samtec CLP-RA (Right-angle female) connector.
*   **Key Features:** EMI ferrite filtering per rotor, mechanical mounting for rotor assembly, and JTAG pass-through.
