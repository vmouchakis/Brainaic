from langchain_community.llms.ollama import Ollama


llm = Ollama(model="phi3")
result = llm.generate(["Tell me a joke"])
print(result.generations[0][0].text)
