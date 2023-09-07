import streamlit as st
from back import generate_response_from_llm
from back_url import generate_response_from_llm_url

# Constants
ACCEPTED_FILE_TYPES = ['txt', 'py', 'tf', 'sh', 'yaml']
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

# Form input and query
with st.form('myform', clear_on_submit=True):
    submitted = st.form_submit_button('Submit', disabled=not (uploaded_file or url_text))
    if submitted:
        try:
            with st.spinner('Thinking...'):
                if selected_option == 'URL':
                    response = generate_response_from_llm_url(url_text, query_text)
                else:
                    response = generate_response_from_llm(uploaded_file, query_text)
            # st.write(response)
            st.text_area('Response', value=response["result"], height=200, max_chars=None, key=None)
            st.text_area('Sources', value=response["source_documents"], height=400, max_chars=None, key=None)
            
        except Exception as e:
            st.error(f"Error during query generation or processing: {str(e)}")