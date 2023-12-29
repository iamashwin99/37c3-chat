# 29/12/23
4am: use json from https://fahrplan.events.ccc.de/congress/2023/fahrplan/schedule.json
for llm use ollama, preferably with a token limit on the server side ( to prevent spamming)
for the client side, use streamlit web app.
Load data and build an index on the server side, and then use the index to search for talk and address to users queries.
perhaps use panel instead from https://github.com/yeyu2/Youtube_demos
index the llm using https://docs.llamaindex.ai/en/latest/getting_started/starter_example.html