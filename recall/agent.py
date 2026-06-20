from recall.memory import recall
from recall.ingest import ingest_session

def build_context_prompt(task, project_files=""):
    queries = [
        f"What decisions were made related to: {task}",
        f"What bugs or issues relate to: {task}",
        f"What architectural patterns apply to: {task}",
    ]
    context_parts = []
    for q in queries:
        result = recall(q)
        if result["confidence"] > 0.5:
            context_parts.append(
                f"[Memory | confidence={result['confidence']:.0%}]\n{result['answer']}"
            )
    memory_block = "\n\n".join(context_parts) if context_parts else "No relevant memory found."
    return f"""You are a coding agent with persistent memory.

## Relevant Past Context
{memory_block}

## Current Task
{task}

## Project Files
{project_files}

Based on the past context, implement this task. If a past decision conflicts, flag it."""

def after_code_gen(task, decisions, bugs_fixed):
    ingest_session(
        session_id=None,
        decisions=decisions,
        bugs_fixed=bugs_fixed,
    )
