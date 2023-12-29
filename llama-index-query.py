from llama_index.llms import Ollama

#mistral:latest
llm = Ollama(model="mistral:latest")
resp = llm.complete("Who is Paul Graham? answer in 1 line")
print(resp)