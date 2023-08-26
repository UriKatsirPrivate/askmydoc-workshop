import vertexai
from langchain.agents.agent_toolkits import (
    create_vectorstore_agent,
    # VectorStoreToolkit,
    # VectorStoreInfo
)
from langchain.chains import RetrievalQA
from langchain.document_loaders import PyPDFLoader
from langchain.embeddings import VertexAIEmbeddings
from langchain.vectorstores import Chroma
from initialization import *


llm = initialize_llm()

# Define processing function
def generate_response_from_llm_pdf(temp_file_path, query_text):
    try:
        # Load and process document if file path is valid
        if temp_file_path:
            loader = PyPDFLoader(temp_file_path)
            pages = loader.load_and_split()
            embeddings = VertexAIEmbeddings()
            store = Chroma.from_documents(pages, embeddings, collection_name='Pdf')
            # vectorstore_info = VectorStoreInfo(name="Pdf", description=" A pdf file to answer your questions", vectorstore=store, llm=llm)
            # toolkit = VectorStoreToolkit(vectorstore_info=vectorstore_info,llm=llm)
            # agent_executor = create_vectorstore_agent(llm=llm, toolkit=toolkit, verbose=True)
            retriever = store.as_retriever()
            qa = RetrievalQA.from_chain_type(llm=llm, chain_type='stuff', retriever=retriever)
            return qa.run(query_text)
        else:
            raise ValueError("Invalid file path.")
    except Exception as e:
        print(f"Error: {e}")
        return None