from recall.memory import store_session, store_file

def ingest_session(session_id, decisions, bugs_fixed, code_changes=None, files_modified=None):
    messages = []
    for d in decisions:
        messages.append({"role": "user", "content": f"Decision: {d}"})
    for b in bugs_fixed:
        messages.append({"role": "user", "content": f"Bug fix: {b}"})
    if code_changes:
        messages.append({"role": "user", "content": f"Code changes: {'; '.join(code_changes)}"})
    if files_modified:
        messages.append({"role": "user", "content": f"Files modified: {', '.join(files_modified)}"})
    return store_session(session_id, messages)

def ingest_docs(file_paths):
    for path in file_paths:
        store_file(path)
