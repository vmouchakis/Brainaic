from langchain.chat_models import ChatOpenAI
from langchain.llms import LlamaCpp
from langchain.document_loaders import DirectoryLoader
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.embeddings import LlamaCppEmbeddings
from langchain.chains.question_answering import load_qa_chain
from langchain.vectorstores import Chroma, FAISS

from langchain.chains.qa_with_sources import load_qa_with_sources_chain


class Bot():
    def __init__(self, data_path: str, temperature: int = 0):
        self.temperature = temperature
        self.embeddings = OpenAIEmbeddings()
        self.load_model()
        self.load_loader(data_path=data_path)
        self.load_index()
        self.chain = load_qa_chain(self.model)

    def load_model(self, model_name: str = ""):
        # load gpt-3.5-turbo model
        self.model = ChatOpenAI(temperature=self.temperature)

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
        response = self.chain({"input_documents": db, "question": prompt}, return_only_outputs=False)
        return response["output_text"]

    