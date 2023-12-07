from langchain.prompts import PromptTemplate


TEMPLATE = """
Use the following pieces of context and also your knowledge to answer the users question.
If you don't know the answer, just say that you don't know, don't try to make up an answer.

Context:
{context}

Conversation history:
{history}

Human: {question}
AI: 
"""


LLAMA_TEMPLATE = """
<s>[INST] <<SYS>>
You are a helpful, respectful and honest assistant.
If you don't know the answer to a question, please don't share false information.
<</SYS>>

Context:
{context}

Conversation history:
{history}

Human: {question}
# AI: 
[/INST]
"""


def prompt(template: str = None):
    templ = LLAMA_TEMPLATE if template else TEMPLATE
    return PromptTemplate(
        template=templ,
        input_variables=["context", "history", "question"]
    )
