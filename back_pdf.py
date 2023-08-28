import vertexai
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
            retriever = store.as_retriever()
            qa = RetrievalQA.from_chain_type(llm=llm, chain_type='stuff', retriever=retriever)
            return qa.run(query_text)
        else:
            raise ValueError("Invalid file path.")
    except Exception as e:
        print(f"Error: {e}")
        return None