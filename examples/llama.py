from langchain.callbacks.manager import CallbackManager
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
from langchain.llms import LlamaCpp
from brainaic.config import LLAMA_MODEL_PATH


callback_manager = CallbackManager([StreamingStdOutCallbackHandler()])

llm = LlamaCpp(
    model_path=LLAMA_MODEL_PATH,
    temperature=0.75,
    max_tokens=2000,
    top_p=1,
    callback_manager=callback_manager,
    verbose=False,  # Verbose is required to pass to the callback manager
)

prompt = """
<s>[INST] <<SYS>>
You are a helpful, respectful and honest assistant.
If a question does not make any sense, or is not factually coherent, explain why instead of answering something not correct. If you don't know the answer to a question, please don't share false information.
<</SYS>>

Vasilis was born in 1997. The current year is 2023. 

Question: How old is Vasilis? [/INST]
"""

llm(prompt)
