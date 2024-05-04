from langchain_community.llms.ollama import Ollama
from brainaic.prompt import DEFAULT_SYSTEM_PROMPT, LLAMA_TEMPLATE


llm = Ollama(model="llama2:7b")
prompt = "What do you know about the LOTR trilogy? Answer in only three short sentences."
result = llm.generate([LLAMA_TEMPLATE.format(system_prompt=DEFAULT_SYSTEM_PROMPT, prompt=prompt)])
print(result.generations[0][0].text)
