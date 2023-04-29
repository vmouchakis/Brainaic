from langchain.memory import ConversationBufferMemory, ConversationBufferWindowMemory


class ConversationBufferMem:
    def __init__(self):
        self.memory = ConversationBufferMemory(memory_key="history", input_key="question")


class ConversationBufferWindMem:
    def __init__(self):
        self.memory = ConversationBufferWindowMemory(memory_key="history", input_key="question", k=2)
