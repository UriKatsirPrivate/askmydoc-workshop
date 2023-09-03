from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import Chroma
from langchain.chains import RetrievalQA
from langchain.embeddings import VertexAIEmbeddings
from langchain.document_loaders import WebBaseLoader
from initialization import *

llm = set_up_llm()

def process_document(url_text):
    try:
        # Load the document and convert it into chunks
        text_splitter = RecursiveCharacterTextSplitter(chunk_size=2000, chunk_overlap=200)
        docs = WebBaseLoader(url_text).load()
        split_texts = text_splitter.split_documents(docs)
        return split_texts
    except Exception as e:
        print("An error occurred while processing the document: ", e)
        return None

def generate_response_from_llm_url(url_text, query_text):
    # Initialize VertexAI and set up the LLM
    try:
        if not url_text:
            return
        split_texts = process_document(url_text)
        
        store = Chroma.from_documents(split_texts, VertexAIEmbeddings(), collection_name="ruff")

        qa = RetrievalQA.from_chain_type(llm=llm, chain_type='stuff', retriever=store.as_retriever())

        return qa.run(query_text)

    except Exception as e:
        print(f"An error occurred: {e}")