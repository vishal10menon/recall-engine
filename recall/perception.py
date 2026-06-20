import httpx
from recall.memory import store_session

AFFERENS_URL = "https://api.afferens.com/v1/demo"

def capture_environment():
    try:
        response = httpx.get(AFFERENS_URL, timeout=10)
        return response.json()
    except Exception:
        return {"error": "Afferens unreachable"}

def store_environmental_context(session_id=None):
    perception = capture_environment()
    messages = [
        {"role": "user", "content": f"Environmental context: {perception}"},
    ]
    return store_session(session_id, messages)
