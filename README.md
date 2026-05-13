# Neakasa M1 Home Assistant Integration

A custom Home Assistant integration for the Neakasa M1 smart litter box, supporting advanced cat management, activity tracking, and device control.

## Features
- Add, update, delete, and list cats (with avatars and weight in kg/lb)
+- Each cat is represented as a sensor entity with attributes (weight, avatar, last entry, stats, etc.) for maximum compatibility and flexibility in Home Assistant.
- Add, update, delete, and list cats (with avatars and weight in kg/lb)
- View cat activity and statistics (entries, durations, daily summaries)
- Device status, cleaning, and settings
- Lovelace dashboard card with animated device and cat info
- HACS-compatible for easy installation and updates

## Installation

### HACS (Recommended)
1. Go to HACS > Integrations > Custom repositories
2. Add this repository URL
3. Search for "Neakasa M1" and install
4. Restart Home Assistant

### Manual
1. Copy the `custom_components/neakasa_m1/` folder to your Home Assistant `custom_components` directory
2. Restart Home Assistant

## Configuration
- Set up via Home Assistant UI (Integrations > Add Integration > Neakasa M1)
- Enter your Neakasa account credentials and select your device
- Configure options (units, notifications, etc.) as needed

## Usage
- Entities for each cat and device will be created
- Use the Lovelace card for a visual dashboard
- Services available for cat management and device control

## Troubleshooting
- See the documentation and FAQ for common issues

## Contributing
- Contributions, bug reports, and feature requests are welcome!

## License
MIT

---
*This README is a work in progress. More sections and details will be added as development continues.*
