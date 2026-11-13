"""Small, dependency-free ANVI event client. Set ANVI_API_KEY in your host secrets."""
import json
import os
import urllib.request

ANVI_ENDPOINT = os.getenv("ANVI_ENDPOINT", "https://YOUR-ANVI-DOMAIN/api/v1/events")

def track(event, user_id=None, properties=None):
    key = os.getenv("ANVI_API_KEY")
    if not key: return False
    payload = json.dumps({"event": event, "user_id": str(user_id) if user_id is not None else None, "properties": properties or {}}).encode()
    req = urllib.request.Request(ANVI_ENDPOINT, data=payload, headers={"Authorization": "Bearer " + key, "Content-Type": "application/json"}, method="POST")
    try:
        with urllib.request.urlopen(req, timeout=3) as response: return 200 <= response.status < 300
    except Exception: return False
