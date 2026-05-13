## Planned Dashboard Card

To provide a user-friendly and visually appealing experience, plan to develop a custom Lovelace card for Home Assistant:

- The card will display all relevant Neakasa M1 litter box information (status, cat activity, weight, etc.).
- It will feature an image or illustration of the M1 litter box, with animated elements (e.g., cat entry, cleaning cycles, weight changes).
- The card will be configurable and easy for users to add to their dashboards.
- Aim for a modern, animated design to enhance the Home Assistant dashboard experience.

This will help users quickly view and interact with their litter box data in an engaging way.
## Current Device Entities

### Sensors
| Sensor            | Unit      | Example Value | Enabled by Default |
|-------------------|-----------|---------------|-------------------|
| Cat litter level  | percent   | 80 %          | yes               |
| WiFi RSS          | dB        | -60 dB        | no (debug info)   |
| Last stay time    | seconds   | 45 s          | no                |
| Last usage        | datetime  | 2024-12-07 14:52 | yes            |
| Device status     | idle / cleaning / leveling / flipover / cat_present / paused / side_bin_locking_panels_missing / cleaning_interrupted | idle | yes |
| Cat litter state  | insufficient / moderate / sufficient | sufficient | yes |
| Bin state         | normal / full / missing | normal | yes         |
| Cat {name}        | kg        | 3.8           | yes               |

### Binary Sensors
| Binary Sensor     | Example Value | Enabled by Default |
|-------------------|---------------|-------------------|
| Garbage can full  | off           | yes               |

### Buttons
| Button | Action                   | Enabled by Default |
|--------|--------------------------|-------------------|
| Clean  | Cleans the litter box    | yes               |
| Level  | Initiates leveling       | yes               |

### Switches
| Switch              | Enabled by Default |
|---------------------|-------------------|
| Kitten mode         | no (rare edgecase)|
| Child lock          | yes               |
| Automatic cover     | yes               |
| Automatic leveling  | yes               |
| Silent mode         | yes               |
| Automatic recovery  | no (potentially dangerous!) |
| Unstoppable cycle   | yes               |
# Neakasa M1 Home Assistant Integration - API & Feature Research

## API Authentication & Encryption
- Uses AES (CBC mode) encryption for sensitive data.
  - Key: `3J74PRUE5TKPJP32`
  - IV: `QB8GC2X6WK39FF93`
- Login uses double MD5 hashing for the password.
- HMAC signatures and encrypted tokens are used for secure communication.

## API Endpoints (from existing integration)
- `/login/user`: Login and get tokens
- `/catbox/toilet/statistics`: Fetch usage statistics (per cat, with times)
- `/catbox/record`: Fetch event records (cat entries/exits, durations)
- Alibaba Cloud IoT API Gateway endpoints for device management and control

## Cat Activity Data
- The API provides per-cat entry/exit events, durations, and weights.
- Current integration exposes weight in kg as a sensor, with attributes for start/end time and weight.
- Activity messages ("Cat X entered for Y seconds, weight Z kg") are not posted as notifications or in a dedicated log.

## Feature Gaps & Ideas
- No support for adding/removing cats via API (endpoint unknown; would require network capture during app usage).
- No option to display weight in pounds (lb); only kg is shown.
- No dedicated activity log or notification for cat entries/exits.
 - Users have requested a way to change the account used for setup. For best user experience, the new integration should support re-authentication or account change via the UI, rather than requiring users to remove and re-add the integration.

## Next Steps
1. Add unit selection (kg/lb) for cat weight sensors.
2. Create a sensor or automation to post cat entry/exit events as notifications or to an activity log.
3. (Optional) Capture app network traffic to discover endpoints for adding/removing cats.

## References
- [timniklas/hass-neakasa GitHub](https://github.com/timniklas/hass-neakasa)
- [Issue #79: Cats activity](https://github.com/timniklas/hass-neakasa/issues/79)

---
This document summarizes the current state of the Neakasa M1 API and integration, and outlines the path for building a more feature-complete Home Assistant integration.