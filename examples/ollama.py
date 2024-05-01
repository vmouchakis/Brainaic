from langchain_community.llms.ollama import Ollama
from brainaic.prompt import LLAMA_TEMPLATE, PHI3_TEMPLATE


llm = Ollama(model="llama2:7b")
system_prompt = """
You're are a helpful Assistant, and you only response to the "Assistant"
Remember, maintain a natural tone. Be precise, concise, and casual.
"""
prompt = "What do you know about the LOTR trilogy? Answer in only three short sentences."
result = llm.generate([LLAMA_TEMPLATE.format(system_prompt=system_prompt, prompt=prompt)])
# result = llm.generate([PHI3_TEMPLATE.format(prompt=prompt)], stop=["<|end|>"])
print(result.generations[0][0].text)
