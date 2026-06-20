# The Recall Engine

an AI coding agent that actually remembers stuff.

## what it does

most coding agents are stateless. you tell it something, it forgets next session.

Recall Engine fixes that by using [Parcle](https://parcle.ai) as a persistent memory layer.

every decision, every bug fix, every architectural choice gets stored. before the agent writes new code, it searches memory for relevant past context and factors that in.

built on [Enter Pro](https://dbed433cafdf417abe2cb15bcacdb53d.prod.enterapp.pro/) and [Afferens](https://afferens.com) for real-time physical perception.

## live demo

**https://f52d0594a02744348cb0f975caca47bc.prod.enterapp.pro**

## how it works

1. **session ends** -> decisions and fixes get ingested into Parcle
2. **new session starts** -> agent queries memory for relevant context
3. **agent generates code** -> uses recalled context to stay consistent
4. **session ends** -> new decisions get stored, memory grows

## setup

```bash
pip install parcle
export PARCLE_API_KEY="pmem_..."
```

## quick look

```python
from recall.memory import store_session, recall

# store a session
store_session(None, [
    {"role": "user", "content": "Decision: using JWT with 24h expiry"},
])

# recall it later
result = recall("what auth pattern did we use?")
print(result["answer"])
# -> "You decided on JWT with 24h expiry"
```

## project structure

```text
recall/
  memory.py       # parcle read/write/search
  agent.py        # memory-augmented reasoning
  ingest.py       # session capture
  perception.py   # afferens workspace perception
  config.py       # team/project settings
demo/
  run_demo.py     # full 3-session demo
```

## running the demo

```bash
PYTHONPATH=. python demo/run_demo.py
```

walks through 3 sessions: build a feature, build another that depends on the first, then debug a bug that relates back. this is the part that actually blew my mind when i first saw it work.

## tool integration

### Parcle

Parcle is the persistent memory layer. here's how it's used:

- **User management** - `client.create_user()` creates a scoped namespace for memory operations
- **Write path** - `client.ingest_dialog()` stores session data as conversational messages. sessions are incremental, append using `session_id`
- **Read path** - `client.search()` takes a natural language query and returns a synthesized answer with confidence scores and citations
- **File ingestion** - `client.ingest_file()` ingests project docs and design specs into the same memory store

the key thing is Parcle returns cited answers, not raw chunks. the agent gets a concise explanation of what was decided and why, with traceability back to original sessions.

### Afferens

Afferens gives the coding agent real-time physical world perception via its MCP-native API.

- **Workspace perception** - `capture_environment()` pulls live data from Afferens across 6 modalities (vision, spatial, acoustic, environmental, molecular, interoception)
- **Contextual memory** - environmental snapshots are stored alongside code decisions in Parcle, so the agent remembers not just what was decided, but the physical context in which it was decided
- **Free demo endpoint** - the `afferens_demo` tool requires no API key

this is what makes the "sentient engineer" framing literal. the agent perceives the world AND remembers.

### Enter Pro

- **Build** - the React dashboard was built entirely in Enter by vibe-coding. Enter pulled the Python source from GitHub, generated the component structure, and scaffolded the UI
- **Deploy** - published directly through Enter hosting
- **Iterative dev** - the dark terminal look, demo player, and code browser were all refined through conversational prompts

## demo walkthrough

**Session A** - team builds authentication. decisions: JWT, 24h expiry, httpOnly cookies. a CORS bug fix also gets ingested into Parcle.

**Session B** - weeks later, team builds a profile feature. agent queries Parcle, recalls the auth pattern from Session A with **92% confidence**, applies the same architecture.

**Session C** - bug: users logged out randomly. agent recalls token expiry decision from Session A with **98% confidence**, identifies the root cause: token refresh rotation was missing.

## stack

- [Parcle](https://parcle.ai) persistent memory
- [Afferens](https://afferens.com) real-time perception
- [Enter Pro](https://dbed433cafdf417abe2cb15bcacdb53d.prod.enterapp.pro/) dev platform
- Python
- React

## license

MIT
