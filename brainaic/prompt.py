from langchain import PromptTemplate


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
The following is a friendly conversation between a human and an AI. 
The AI is talkative and provides lots of specific details from its context, and only its context. 
If the AI does not know the answer to a question, it truthfully says it does not know.

Context:
{context}

Conversation history:
{history}

Human: {question}
AI:
"""


def prompt(template: str = None):
    templ = LLAMA_TEMPLATE if template else TEMPLATE
    PROMPT = PromptTemplate(
        template=templ,
        input_variables=["context", "history", "question"]
    )

    return PROMPT
