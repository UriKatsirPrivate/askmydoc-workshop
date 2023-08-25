from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import Chroma
from langchain.chains import RetrievalQA
from langchain.embeddings import VertexAIEmbeddings
from initialization import *


llm = initialize_llm()

def process_document(file):
    try:
        # Load the document and convert it into chunks
        document = [file.read().decode()]
        text_splitter = CharacterTextSplitter(chunk_size=2000, chunk_overlap=200)
        texts = text_splitter.create_documents(document)
        return texts
    except Exception as e:
        print("An error occurred while processing the document: ", e)
        return None

def generate_response_from_llm(uploaded_file, query_text):
    try:
        # Load document if file is uploaded
        if uploaded_file is not None:
            texts = process_document(uploaded_file)
            if texts is None:
                return "Error in processing document"

            # Select embeddings
            embeddings = VertexAIEmbeddings()
            # Create a vectorstore from documents
            db = Chroma.from_documents(texts, embeddings)
            # Create retriever interface
            retriever = db.as_retriever()
            # Create QA chain
            qa = RetrievalQA.from_chain_type(llm=llm, chain_type='stuff', retriever=retriever)

            return qa.run(query_text)
    except Exception as e:
        print("An error occurred while generating response: ", e)
        return None