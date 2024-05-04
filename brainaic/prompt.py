from langchain.prompts import PromptTemplate


DEFAULT_PROMPT = PromptTemplate.from_template(
    """
    Use the following pieces of context to answer the question at the end. If you 
    don't know the answer, just say that you don't know, don't try to make up an 
    answer.

    {context}

    Question: {input}
    Helpful Answer:
    """
)

DEFAULT_SYSTEM_PROMPT = """
You're are a helpful Assistant, and you only response to the prompt.
Remember, maintain a natural tone. Be precise, concise, and casual.
"""

TEMPLATE = """
Use the following pieces of context and also your knowledge to answer the users question.
If you don't know the answer, just say that you don't know, don't try to make up an answer.

Context:
{context}

Human: {question}
AI: 
"""

# TODO: Add context in prompt templates
LLAMA_TEMPLATE = """
<<SYS>>
{system_prompt}
<</SYS>>
[INST] 
User: {prompt} 
[/INST]\n
Assistant:
"""

PHI3_TEMPLATE = "<|user|>\n {prompt} <|end|>\n <|assistant|>"

GEMMA_TEMPLATE = """
<start_of_turn>user
{this is system} {this is prompt}
<end_of_turn>
<start_of_turn>model
<end_of_turn>
"""

MISTRAL_TEMPLATE = "[INST] {system_prompt} {prompt} [/INST]"

templates = {
    'llama2': LLAMA_TEMPLATE,
    'gemma': GEMMA_TEMPLATE,
    'mistral': MISTRAL_TEMPLATE,
    'phi3': PHI3_TEMPLATE
}

# maybe do this for all the params, instead for only the stop
stop_words = {
    'llama2': ["[INST]", "[/INST]", "<<SYS>>", "<</SYS>>"],
    'gemma': ["<start_of_turn>", "<end_of_turn>"],
    'mistral': ["[INST]", "[/INST]"],
    'phi3': ["<|user|>", "<|assistant|>", "<|system|>", "<|end|>", "<|endoftext|>"]
}


def prompt(model_name: str) -> str:
    try:
        return templates.get(model_name)
    except KeyError:
        raise RuntimeError(f"Model {model_name} not recognized")
