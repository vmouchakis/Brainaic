from langchain.prompts import PromptTemplate


TEMPLATE = """
Use the following pieces of context and also your knowledge to answer the users question.
If you don't know the answer, just say that you don't know, don't try to make up an answer.

Context:
{context}

Human: {question}
AI: 
"""


LLAMA_TEMPLATE = """
Context: {context}

Based on Context provide me answer for following question.
Question: {question}
Answer:
"""


def prompt(template: str = None):
    templ = LLAMA_TEMPLATE if template == "llama" else TEMPLATE
    return PromptTemplate(
        template=templ,
        input_variables=["context", "question"]
    )
