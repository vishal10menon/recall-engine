from parcle import Parcle
from recall.config import PARCLE_API_KEY, TEAM_ID

client = Parcle(api_key=PARCLE_API_KEY)

# Create the user on first run (idempotent)
try:
    client.create_user(user_id=TEAM_ID)
    print(f"Created user: {TEAM_ID}")
except Exception:
    pass  # user already exists

def store_session(session_id, messages):
    result = client.ingest_dialog(
        user_id=TEAM_ID,
        session_id=session_id,
        messages=messages,
    )
    return result.session_id

def store_file(file_path):
    client.ingest_file(user_id=TEAM_ID, file=file_path)

def recall(query):
    result = client.search(user_id=TEAM_ID, query=query)
    return {
        "answer": result.answer,
        "confidence": result.confidence,
        "citations": result.citations,
    }
