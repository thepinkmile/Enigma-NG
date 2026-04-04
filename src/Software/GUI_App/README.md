# Enigma-NG GUI Application

This is the cross-platform GUI application for the Enigma-NG project, built with Avalonia UI and .NET 10.0.

## Project Structure

The project is located in `src/Software/GUI_App/` with the solution file at `src/EnigmaNG.sln`.

## Supported Platforms

- Windows (x64)
- Linux (ARM64) - Optimized for Raspberry Pi CM5 with Raspberry Pi OS

## Prerequisites

- .NET 10.0 SDK
- For Linux/Raspberry Pi:
  - Raspberry Pi OS (Debian-based)
  - X11 or Wayland display server
  - GTK libraries (install with `sudo apt-get install libgtk-3-0`)

## Building

```bash
dotnet build
```

## Running

```bash
dotnet run
```

## Publishing for Raspberry Pi

To create a self-contained executable for Raspberry Pi CM5:

### Using Publish Profile (Recommended)
```bash
dotnet publish /p:PublishProfile=Properties\PublishProfiles\linux-arm64.pubxml
```

### Using Command Line
```bash
dotnet publish -c Release -r linux-arm64 --self-contained --single-file --trimmed --ready-to-run
```

The output will be in `bin/Release/net10.0/linux-arm64/publish/`.

## Features

- MVVM architecture
- Cross-platform UI with Avalonia
- Hardware-accelerated rendering on Linux
