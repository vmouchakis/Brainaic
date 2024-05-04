from langchain_community.document_loaders import DirectoryLoader
from langchain_community.embeddings import GPT4AllEmbeddings
from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_community.vectorstores import Chroma
from langchain.text_splitter import RecursiveCharacterTextSplitter
from brainaic.prompt import DEFAULT_PROMPT
from brainaic.llm import Llm
from brainaic.config import DB_PATH


class Bot:
    def __init__(self, data_path: str,
                 model_name: str = "llama2",
                 temperature: float = 0.0,
                 persist_vectors: bool = True,
                 verbose: bool = False):
        self.model_name = model_name
        self.llm = Llm(model_name=model_name, temperature=temperature, verbose=verbose)
        self.prompt = DEFAULT_PROMPT
        self.embeddings = GPT4AllEmbeddings()
        self.vectorstore = self.load_vector_db(data_path, persist_vectors)
        self.chain = self.load_chain()

    @staticmethod
    def load_vector_db(data_path: str, persist_vectors: bool):
        loader = DirectoryLoader(data_path)
        documents = loader.load()
        text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=50)
        texts = text_splitter.split_documents(documents)
        if persist_vectors:
            persist_directory = DB_PATH
        else:
            persist_directory = None
        vectorstore = Chroma.from_documents(documents=texts,
                                            embedding=GPT4AllEmbeddings(),
                                            persist_directory=persist_directory)
        return vectorstore

    def load_chain(self):
        combine_docs_chain = create_stuff_documents_chain(self.llm.llm,
                                                          prompt=self.prompt)
        retrieval_chain = create_retrieval_chain(self.vectorstore.as_retriever(), combine_docs_chain)
        return retrieval_chain

    def get_response(self, question: str):
        resp = self.chain.invoke({'input': question})
        return resp
