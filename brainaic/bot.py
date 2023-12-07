from langchain.chat_models import ChatOpenAI
from langchain.llms import LlamaCpp
from langchain.document_loaders import DirectoryLoader
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.embeddings import LlamaCppEmbeddings
from langchain.chains.question_answering import load_qa_chain
from langchain.chains.qa_with_sources import load_qa_with_sources_chain
from langchain.vectorstores import Chroma, FAISS
from brainaic.memory import ConversationBufferMem, ConversationBufferWindMem
from brainaic.config import LLAMA_MODEL_PATH
from brainaic.prompt import prompt
from langchain.chains.conversational_retrieval.prompts import QA_PROMPT
# https://plainenglish.io/blog/langchain-streamlit-llama-bringing-conversational-ai-to-your-local-machine
from langchain.callbacks.manager import CallbackManager
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
from langchain.chains import LLMChain



class Bot():
    def __init__(self,
                 data_path: str,
                 model_name: str = "gpt",
                 temperature: int = 0.5):
        self.model_name = model_name
        self.temperature = temperature
        self.prompt = self.load_prompt()
        self.model = self.load_model()
        self.embeddings = self.load_embeddings()
        self.loader = self.load_loader(data_path=data_path)
        self.index = self.load_index()
        self.chain = load_qa_chain(llm=self.model,
                                   chain_type="stuff",
                                   prompt=self.prompt,
                                   verbose=True,
                                   memory=ConversationBufferMem().memory)

    def load_model(self):
        if self.model_name == "gpt":
            # load gpt-3.5-turbo model
            return ChatOpenAI(temperature=self.temperature)
        elif self.model_name == "llama":
            callback_manager = CallbackManager([StreamingStdOutCallbackHandler()])
            return LlamaCpp(model_path=LLAMA_MODEL_PATH,
                            n_ctx=2048,
                            temperature=0,
                            callback_manager=callback_manager,
                            verbose=True,
                            f16_kv=True)
        else: 
            exit(0)

    def load_embeddings(self):
        if self.model_name == "gpt":
            return OpenAIEmbeddings()
        elif self.model_name == "llama":
            return LlamaCppEmbeddings(model_path=LLAMA_MODEL_PATH)
        else:
            exit(0)

    def load_prompt(self):
        if self.model_name=="gpt": return prompt()
        else: return prompt(template="llama")

    def load_loader(self, data_path: str):
        return DirectoryLoader(data_path)

    def load_index(self):
        return Chroma.from_documents(
            self.loader.load_and_split(), self.embeddings
        )

    def get_response(self, prompt: str):
        db = self.index.similarity_search(prompt)
        response = self.chain.run(input_documents=db, question=prompt, return_only_outputs=False)
        return response
