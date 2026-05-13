## Cat Avatar Field

- The `avatar` field in the cat profile contains a URL to the cat's image if set in the app.
- Example:
```json
"avatar": "https://jhc-en.oss-ap-southeast-1.aliyuncs.com/user%2F400114888%2FcatBox%2FJQ01909G25500040268%2F54a9b38ae1c07bf8aaf7d1cb4fd194f3.png?..."
```
- If the field is empty, no avatar is set for the cat.
- You can display this image in your Lovelace card or integration UI.
- If empty, show a default cat icon or placeholder.

---
## Known and Possible Settings

Based on API research and the original integration, the following settings and features are known or likely available:

- Cat profile management (add, update, delete, list)
- Cat weight unit (kg/lb)
- Cat name, gender, birthday, variety, sterilization
- Device cleaning (manual trigger)
- Device status (idle, cleaning, leveling, etc.)
- Litter level, bin state, WiFi RSSI
- Child lock, automatic cover, automatic leveling, silent mode, unstoppable cycle, kitten mode, automatic recovery

**Possible additional settings to check in the app:**
- Device timezone
- Notification preferences (for events, errors, cleaning, etc.)
- Firmware update
- Device sharing (add/remove users)
- Litter type or brand
- Cleaning schedule or timer
- LED/lighting settings
- Sound/volume settings
- Any other advanced or hidden device options

---
## Cat Statistics - Confirmed API Endpoint

**GET** `https://us.neakasa.com/api/catbox/toilet/statistics?user_id=400114888&device_name=JQ01909G25500040268&bind_status=1&start_time=1776087960&end_time=1778679960&zone=-14400&cat_id=202543`

- Returns daily statistics for a specific cat over a time range.
- Each entry includes:
    - `date`: Date of the record
    - `num`: Number of events (e.g., visits)
    - `weight`: Cat weight
    - `unit`: Weight unit (e.g., "lb")
    - `toilet_total_second`: Total time spent in the litter box (seconds)
    - `weight_avg`: Average weight for the day
- Requires authentication headers (`uid`, `token`).

**Success Response:**
- HTTP 200 OK, application/json, with a list of daily statistics

---
## Cat Activity/History - Confirmed API Endpoint

**GET** `https://us.neakasa.com/api/catbox/record?user_id=400114888&device_name=JQ01909G25500040268&bind_status=1&start_time=1778558400&end_time=1778644799`

- Returns a list of cat activity records for the specified device, user, and time range.
- Each record includes:
    - `cat_id`: Cat profile ID (0 if unknown)
    - `start_time`, `end_time`: Timestamps for the event
    - `weight`: Cat weight for the event
    - `unit`: Weight unit (e.g., "lb")
    - `way`: Event type (e.g., entry/exit)
    - `type`, `record_id`: Additional event info
- Requires authentication headers (`uid`, `token`).

**Success Response:**
- HTTP 200 OK, application/json, with a list of event records

---
## Delete Cat - Confirmed API Endpoint

**POST** `https://us.neakasa.com/api/catbox/cat/delete`

**Headers:**
- Charset: UTF-8
- uid: CUtEQY2jlH/4y76Pny01Sw==
- token: [token value]
- Accept-Language: en
- Content-Type: application/json; charset=utf-8
- Host: us.neakasa.com
- User-Agent: okhttp/4.12.0

**JSON Body:**
```json
{
    "device_name": "JQ01909G25500040268",
    "bind_status": 1,
    "id": 202542,
    "user_id": 400114888
}
```

**Success Response:**
- HTTP 200 OK, application/json

---
## List Cats - Confirmed API Endpoint

**GET** `https://us.neakasa.com/api/catbox/cat/list?device_name=JQ01909G25500040268&user_id=400114888`

- Returns a list of all cat profiles for the specified device and user.
- Requires authentication headers (`uid`, `token`).

---
# Neakasa API: Add Cat Request Example

## Add Cat - Confirmed API Endpoint

**POST** `https://us.neakasa.com/api/catbox/cat`

**Headers:**
- Charset: UTF-8
- uid: CUtEQY2jlH/4y76Pny01Sw==
- token: KyWb5BEcmD9iRP+URgZUR3W+oQKS8UsJtDjQUO9rxZpZVnP5YzM3OMbTmVZsOWYM
- Accept-Language: en
- Content-Type: application/json; charset=utf-8
- Host: us.neakasa.com
- User-Agent: okhttp/4.12.0

**JSON Body:**
```json
{
    "device_name": "JQ01909G25500040268",
    "bind_status": 1,
    "unit": "lb",
    "scene": "catDetail",
    "name": "Mayhem",
    "weight": 9.0,
    "user_id": 400114888,
    "birthday": "",
    "variety": -1,
    "gender": 1
}
```

**Success Response:**
- HTTP 200 OK, application/json

---

## Update Cat - Confirmed API Endpoint

**POST** `https://us.neakasa.com/api/catbox/cat/update`

**Headers and JSON body:**
- Same as add cat (see above), but used for updating an existing cat profile.

---
This file documents the structure of the API requests for adding and updating a cat to the Neakasa M1 litter box via the mobile app.