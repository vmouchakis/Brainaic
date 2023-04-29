from langchain.memory import ConversationBufferMemory, ConversationBufferWindowMemory


class ConversationBufferMem:
    def __init__(self):
        self.memory = ConversationBufferMemory(input_key="question")


class ConversationBufferWindMem:
    def __init__(self):
        self.memory = ConversationBufferWindowMemory(input_key="question", k=2)
