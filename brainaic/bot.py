from langchain.chat_models import ChatOpenAI
from langchain.llms import LlamaCpp
from langchain.document_loaders import DirectoryLoader
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.embeddings import LlamaCppEmbeddings
from langchain.chains.question_answering import load_qa_chain
from langchain.chains.qa_with_sources import load_qa_with_sources_chain
from langchain.vectorstores import Chroma, FAISS
from brainaic.memory import ConversationBufferMem, ConversationBufferWindMem
from brainaic.config import *
from brainaic.prompt import prompt
from langchain.chains.conversational_retrieval.prompts import QA_PROMPT



class Bot():
    def __init__(self,
                 data_path: str,
                 model_name: str = "gpt",
                 temperature: int = 0.5):
        self.model_name = model_name
        self.temperature = temperature
        # self.prompt = PROMPT if self.model_name == "gpt" else QA_PROMPT
        self.prompt = prompt() if self.model_name=="gpt" else prompt(template="llama")
        self.embeddings = self.load_embeddings()
        self.model = self.load_model()
        self.load_loader(data_path=data_path)
        self.load_index()
        self.chain = load_qa_chain(llm=self.model,
                                   chain_type="stuff",
                                   prompt=self.prompt,
                                   verbose=True,
                                   memory=ConversationBufferWindMem().memory)

    def load_model(self):
        if self.model_name == "gpt":
            # load gpt-3.5-turbo model
            return ChatOpenAI(temperature=self.temperature)
        elif self.model_name == "llama":
            return LlamaCpp(model_path=LLAMA_MODEL_PATH, n_ctx=2048, verbose=False)
        else: 
            exit(0)

    def load_embeddings(self):
        if self.model_name == "gpt":
            return OpenAIEmbeddings()
        elif self.model_name == "llama":
            return LlamaCppEmbeddings(model_path=LLAMA_MODEL_PATH)
        else:
            exit(0)

    def load_loader(self, data_path: str):
        self.loader = DirectoryLoader(data_path)
        # print the num of documents in the data directory, just for sanity check
        # print(len(self.loader.load()))

    def load_index(self):
        self.index = FAISS.from_documents(
            self.loader.load_and_split(), self.embeddings
        )

    def get_response(self, prompt: str):
        db = self.index.similarity_search(prompt)
        response = self.chain.run(input_documents=db, question=prompt)
        return response

    