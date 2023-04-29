from langchain.memory import ConversationBufferMemory

class ConversationBufferMem:
    def __init__(self):
        self.memory = ConversationBufferMemory(input_key="question")
