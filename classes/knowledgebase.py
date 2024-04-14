class Knowledgebase:

    api_key= ""
    pc= ""
    index_name = ""
    text_field = ""
    index = ""
    embed_model = ""
    vectorstore = ""

    def __init__(self,os,Pinecone, time, OpenAIEmbeddings):
        # initialize connection to pinecone (get API key at app.pinecone.io)
        self.api_key = os.getenv("PINECONE_API_KEY") or "YOUR-API-KEY"
        # configure client
        self.pc = Pinecone(api_key=self.api_key)
        self.index_name = 'banking-rag'
        # connect to index
        self.index = self.pc.Index(self.index_name)
        time.sleep(2)
        self.text_field = "answer"

        self.embed_model = OpenAIEmbeddings(model="text-embedding-ada-002") 

    def create_vectorstore(self, Pinecone):

        self.vectorstore = Pinecone(
            self.index, self.embed_model.embed_query, self.text_field
        )

    def augment_prompt(self, query: str):
        # get top 3 results from knowledge base
        results = self.vectorstore.similarity_search(query, k=3)
        # get the text from the results
        source_knowledge = "\n".join([x.page_content for x in results])
        # feed into an augmented prompt
        augmented_prompt = f"""Using the contexts below, answer the query.

        Contexts:
        {source_knowledge}

        Query: {query}"""
        return augmented_prompt
