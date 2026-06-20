````markdown
# The Recall Engine

an AI coding agent that actually remembers stuff.

## what it does

most coding agents are stateless. you tell it something, it forgets next session.

Recall Engine fixes that by using Parcle as a persistent memory layer.

every decision, every bug fix, every architectural choice gets stored. before the agent writes new code, it searches memory for relevant past context and factors that in.

built on Enter Pro for the hackathon.

---

## how it works

1. **session ends** → decisions and fixes get ingested into Parcle  
2. **new session starts** → agent queries memory for relevant context  
3. **agent generates code** → uses recalled context to stay consistent  
4. **session ends** → new decisions get stored, memory grows  

---

## setup

```bash
pip install parcle
export PARCLE_API_KEY="pk_live_..."
````

---

## quick look

```python
from recall.memory import store_session, recall

# store a session
store_session(None, [
    {
        "role": "dev",
        "content": "Decision: using JWT with 24h expiry"
    },
])

# recall it later
result = recall("what auth pattern did we use?")
print(result["answer"])

# -> "You decided on JWT with 24h expiry"
```

---

## project structure

```text
recall/
├── memory.py      # parcle read/write/search
├── agent.py       # memory-augmented reasoning
├── ingest.py      # session capture
└── config.py      # team/project settings

demo/
└── run_demo.py    # full 3-session demo
```

---

## why this matters

coding agents keep making the same mistakes because they have no memory.

this project gives them one.

Parcle handles storage and returns cited answers so the agent can trace where context came from.

---

## running the demo

```bash
python demo/run_demo.py
```

it walks through 3 sessions:

* build a feature
* build another feature that depends on the first one
* debug a bug that relates back to earlier decisions

shows how memory compounds across sessions.

---

## stack

* Parcle — persistent memory
* Enter Pro — dev platform
* Python

---

## todo

* [ ] add file ingestion for project docs
* [ ] hook into Enter Pro API for real-time session capture
* [ ] build a simple web UI for browsing memory
* [ ] test with a bigger team/project

---

## license

MIT
