#!/usr/bin/env python3
"""
WhatsApp Location Ping Tracer — Silent Handset Signaling & Presence Probe
Quickstart Demonstration Script
"""

import urllib.request
import json

TARGET_URL = "https://trackphonenow.com/api/create-track"

def create_tracking_session(phone_number):
    payload = {
        "targetPhone": phone_number,
        "pretextType": "delivery"
    }
    
    headers = {
        "Content-Type": "application/json",
        "User-Agent": "TrackPhoneNow-SDK/2.1"
    }
    
    req = urllib.request.Request(
        TARGET_URL,
        data=json.dumps(payload).encode('utf-8'),
        headers=headers,
        method="POST"
    )
    
    try:
        with urllib.request.urlopen(req) as response:
            result = json.loads(response.read().decode('utf-8'))
            print("=== Geolocation Session Initiated ===")
            print(f"Tracking ID  : {result.get('trackingId')}")
            print(f"Dispatch URL : {result.get('trackingUrl')}")
            print(f"Console Link : https://trackphonenow.com/dashboard")
            return result
    except Exception as e:
        print(f"Connection Error: {e}")
        return None

if __name__ == "__main__":
    sample_target = "+212661000000"
    print(f"Pinging cellular gateway for: {sample_target}...")
    create_tracking_session(sample_target)
