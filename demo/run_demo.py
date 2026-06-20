from recall.ingest import ingest_session
from recall.agent import build_context_prompt, after_code_gen
from recall.memory import recall

print("=" * 60)
print("SESSION A: Building the auth feature")
print("=" * 60)

session_id = ingest_session(
    session_id=None,
    decisions=[
        "Chose JWT over session cookies for stateless auth",
        "Set token expiry to 24 hours, refresh token to 7 days",
        "Stored tokens in httpOnly cookies, not localStorage",
    ],
    bugs_fixed=["Fixed CORS issue by adding explicit allowed origins"],
    code_changes=["Created /auth/middleware.py with JWT validation"],
    files_modified=["src/auth/middleware.py", "src/auth/routes.py"],
)
print(f"Stored session: {session_id}")

print("\n" + "=" * 60)
print("SESSION B: Building the profile feature")
print("=" * 60)

result = recall("What auth pattern did we use?")
print(f"Memory recall: {result['answer']}")
print(f"Confidence: {result['confidence']:.0%}")

print("\n" + "=" * 60)
print("SESSION C: Debugging a token expiry bug")
print("=" * 60)

result = recall("What did we decide about token expiry?")
print(f"Memory recall: {result['answer']}")
print(f"Confidence: {result['confidence']:.0%}")

ingest_session(
    session_id=None,
    decisions=[],
    bugs_fixed=["Bug: users logged out due to token not rotating. Fix: added rotation on refresh."],
    files_modified=["src/auth/routes.py"],
)
print("Fix recorded.")
