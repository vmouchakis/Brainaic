from langchain.callbacks.manager import CallbackManager
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
from langchain.chains import LLMChain
from langchain.llms import LlamaCpp
from langchain.prompts import PromptTemplate
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
Question: A rap battle between Stephen Colbert and John Oliver
"""

llm(prompt)
