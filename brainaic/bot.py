from langchain.chat_models import ChatOpenAI
from langchain.llms import LlamaCpp
from langchain.document_loaders import DirectoryLoader
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.embeddings import LlamaCppEmbeddings
from langchain.chains.question_answering import load_qa_chain
from langchain.vectorstores import Chroma, FAISS
from brainaic.config import LLAMA_MODEL_PATH
from brainaic.prompt import prompt
# https://plainenglish.io/blog/langchain-streamlit-llama-bringing-conversational-ai-to-your-local-machine
from langchain.callbacks.manager import CallbackManager
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler


class Bot:
    def __init__(self,
                 data_path: str,
                 model_name: str = "gpt",
                 temperature: int = 0):
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
                                   verbose=True,)

    def load_model(self):
        if self.model_name == "gpt":
            # load gpt-3.5-turbo model
            return ChatOpenAI(temperature=self.temperature)
        elif self.model_name == "llama":
            # load llama2-7b model
            callback_manager = CallbackManager([StreamingStdOutCallbackHandler()])
            return LlamaCpp(model_path=str(LLAMA_MODEL_PATH),
                            n_ctx=4096,
                            n_gpu_layers=512,
                            n_batch=30,
                            temperature=self.temperature,
                            callback_manager=callback_manager,
                            verbose=True,
                            f16_kv=True)
        else:
            raise RuntimeError(f"""
                Model '{self.model_name}' is not supported.
                Supported models: 'gpt' (gpt-3.5-turbo), 'llama' (llama2-7b).
            """)

    def load_embeddings(self):
        if self.model_name == "gpt":
            return OpenAIEmbeddings()
        elif self.model_name == "llama":
            return LlamaCppEmbeddings(model_path=LLAMA_MODEL_PATH)
        else:
            raise RuntimeError(f"""
                Model '{self.model_name}' is not supported.
                Supported models: 'gpt' (gpt-3.5-turbo), 'llama' (llama2-7b).
            """)

    def load_prompt(self):
        return prompt(template=self.model_name)

    @staticmethod
    def load_loader(data_path: str):
        return DirectoryLoader(data_path)

    def load_index(self):
        return Chroma.from_documents(
            self.loader.load_and_split(), self.embeddings
        )

    def get_response(self, question: str):
        db = self.index.similarity_search(question)
        response = self.chain.run(input_documents=db, question=question, return_only_outputs=True)
        return response
