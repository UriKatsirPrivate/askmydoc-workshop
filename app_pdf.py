import streamlit as st
import tempfile
from back import generate_response_from_llm
from back_url import generate_response_from_llm_url
from back_pdf import generate_response_from_llm_pdf
import os

# Constants
ACCEPTED_FILE_TYPES = ['pdf','txt', 'py', 'tf', 'sh', 'yaml']
DOCUMENT_OPTIONS = ['Please Select', 'URL', 'File Upload']

# Page title
st.set_page_config(page_title='Ask My Doc App')
st.title('Ask My Doc App')

# options = ['Please Select','File Upload','URL']
selected_option = st.selectbox('Select Document Type', DOCUMENT_OPTIONS)

url_text = None
uploaded_file = None
query_text = None

if selected_option == 'URL':
    url_text = st.text_input('Enter your url:', placeholder='Please provide a URL.')
    query_text = st.text_input('Enter your question:', placeholder='Please provide a short summary.')
elif selected_option == 'File Upload':
    uploaded_file = st.file_uploader('Upload an article', type=ACCEPTED_FILE_TYPES)
    query_text = st.text_input('Enter your question:', placeholder='Please provide a short summary.')

# for pdf files and any other files that require temp file path for the langchain loader
temp_file_path = os.getcwd()
if uploaded_file is not None:
    if uploaded_file.type == 'application/pdf' or uploaded_file.type == 'text/csv':
        try:
            temp_dir = tempfile.TemporaryDirectory()
            temp_file_path = os.path.join(temp_dir.name, uploaded_file.name)
            with open(temp_file_path, "wb") as temp_file:
                temp_file.write(uploaded_file.read())
        except Exception as e:
            st.error(f"Error during file handling: {str(e)}")

# Form input and query
with st.form('myform', clear_on_submit=True):
    submitted = st.form_submit_button('Submit', disabled=not (uploaded_file or url_text))
    if submitted:
        try:
            with st.spinner('Thinking...'):
                if selected_option == 'URL':
                    response = generate_response_from_llm_url(url_text, query_text)
                elif uploaded_file.type == 'application/pdf':
                    response = generate_response_from_llm_pdf(temp_file_path, query_text)
                else:
                    response = generate_response_from_llm(uploaded_file, query_text)
            # st.write(response)
            st.text_area('Response', value=response["result"], height=200, max_chars=None, key=None)
            st.text_area('Sources', value=response["source_documents"], height=400, max_chars=None, key=None)
            
        except Exception as e:
            st.error(f"Error during query generation or processing: {str(e)}")