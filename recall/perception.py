import os
from afferens import Afferens

AFFERENS_KEY = os.environ.get("AFFERENS_API_KEY", "")

def capture_environment():
    """Ingest and perceive workspace data via Afferens."""
    if not AFFERENS_KEY:
        return {"status": "no_key"}
    try:
        client = Afferens(api_key=AFFERENS_KEY)

        # Ingest current workspace state
        client.ingest(
            modality="ENVIRONMENTAL",
            data={"temperature_c": 23.5, "humidity_pct": 45, "noise_level_db": 32, "light_lux": 450},
            classification="workspace_reading",
        )

        # Perceive it back
        data = client.perceive(modality="ENVIRONMENTAL", limit=1)
        return data
    except Exception as e:
        return {"error": str(e)}

def store_environmental_context(session_id=None):
    from recall.memory import store_session
    perception = capture_environment()
    messages = [
        {"role": "user", "content": f"Environmental context: {perception}"},
    ]
    return store_session(session_id, messages)
