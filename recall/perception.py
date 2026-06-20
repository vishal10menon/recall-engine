import httpx
import json
from recall.memory import store_session

AFFERENS_API = "https://afferens.com/api/v1"

def capture_environment():
    """Query Afferens for live workspace perception data."""
    try:
        response = httpx.get(
            f"{AFFERENS_API}/demo",
            headers={"Accept": "application/json"},
            timeout=10
        )
        if response.status_code == 200:
            return response.json()
        return {"status": response.status_code, "note": "Afferens demo endpoint returned non-200"}
    except Exception as e:
        return {"error": str(e), "note": "Afferens integration configured, endpoint unreachable from this environment"}

def store_environmental_context(session_id=None):
    perception = capture_environment()
    messages = [
        {"role": "user", "content": f"Environmental context: {perception}"},
    ]
    return store_session(session_id, messages)
