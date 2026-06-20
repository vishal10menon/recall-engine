# The Recall Engine

an AI coding agent that actually remembers stuff.

## what it does

most coding agents are stateless. you tell it something, it forgets next session. Recall Engine fixes that by using [Parcle](https://parcle.ai) as a persistent memory layer.

every decision, every bug fix, every architectural choice gets stored. before the agent writes new code, it searches memory for relevant past context and factors that in.

built on [Enter Pro](https://dbed433cafdf417abe2cb15bcacdb53d.prod.enterapp.pro/) for the hackathon.

## how it works

1. **session ends** -> decisions and fixes get ingested into Parcle
2. **new session starts** -> agent queries memory for relevant context
3. **agent generates code** -> uses recalled context to stay consistent
4. **session ends** -> new decisions get stored, memory grows

## setup

```bash
pip install parcle
export PARCLE_API_KEY="pk_live_..."

from recall.memory import store_session, recall

# store a session
store_session(None, [
    {"role": "dev", "content": "Decision: using JWT with 24h expiry"},
])

# recall it later
result = recall("what auth pattern did we use?")
print(result["answer"])
# -> "You decided on JWT with 24h expiry"

recall/
  memory.py    # parcle read/write/search
  agent.py     # the agent with memory-augmented reasoning
  ingest.py    # session capture
  config.py    # team/project settings
demo/
  run_demo.py  # full 3-session demo
