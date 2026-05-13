# Neakasa Cat Profile & API Endpoint Research

## Cat Profile JSON Example
```json
[
    {
        "id": 202048,
        "name": "RedRed",
        "weight": 11.7,
        "unit": "lb",
        "avatar": "",
        "birthday": "",
        "variety": -1,
        "gender": 1,
        "sterilization": 1,
        "enabled": 1,
        "path": ""
    }
]
```
- Cat profiles include: name, weight, unit (kg/lb), gender, sterilization, birthday, and more.
- The API supports both kilograms and pounds for weight.

## Example API Request (Captured)
```
POST /[endpoint] HTTP/1.1
Host: us.neakasa.com
request-id: SLZAGZHNBSUXSAPTCA+QDOLFIAQWEKA4HZQJ86JI2BO=
brand: samsung
model: SM-F966U1
version: 202060001
timestamp: 1778678117
accept: */*
Content-Type: application/x-www-form-urlencoded
Charset: UTF-8
uid: CUtEQY2jlH/4y76Pny01Sw==
token: KyWb5BEcmD9iRP+URgZUR3W+oQKS8UsJtDjQUO9rxZrh6V/sDkcu+4U0OHxyiuCC
Accept-Language: en
User-Agent: okhttp/4.12.0

Body:
device_name=JQ01909G25500040268&user_id=400114888&bind_status=1
```
- Authenticated with `uid` and `token` headers.
- Parameters include device name, user ID, and bind status.
- Host: `us.neakasa.com` (API endpoint)

## Implications for Integration
- The API supports retrieving and updating cat profiles, including weight units.
- With the correct endpoint and payload, it should be possible to add, edit, or remove cats from the integration.
- Displaying weight in pounds (lb) or kilograms (kg) can be supported based on the `unit` field.

## Next Steps
- Capture the full endpoint URL and response when adding/editing a cat in the app.
- Use this structure to implement full cat management in the Home Assistant integration.
- Document any additional fields or behaviors discovered.

---
This file summarizes findings about cat profile management and related API requests for the Neakasa M1 integration.