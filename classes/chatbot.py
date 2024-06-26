class Chatbot:

    llm= ""
    memory= ""

    def __init__(self, os, ChatOpenAI, ConversationBufferWindowMemory):
    
        os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY") or "YOUR-API-KEY"
        
        self.llm = ChatOpenAI(
            openai_api_key = os.environ["OPENAI_API_KEY"],
            model = 'gpt-3.5-turbo'
        )
        
        self.memory = ConversationBufferWindowMemory(memory_key="chat_history", k=4)
  
