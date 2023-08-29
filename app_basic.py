import streamlit as st

# Constants
ACCEPTED_FILE_TYPES = ['txt', 'py', 'tf', 'sh', 'yaml']
DOCUMENT_OPTIONS = ['Please Select', 'URL', 'File Upload']

# Function to get user input based on selected option
def get_user_input(selected_option):
    query_text = st.text_input('Enter your question:', placeholder='Please provide a short summary.')

    if selected_option == 'URL':
        url_text = st.text_input('Enter your URL:', placeholder='Please provide a URL.')
        return url_text, query_text
    elif selected_option == 'File Upload':
        uploaded_file = st.file_uploader('Upload an article', type=ACCEPTED_FILE_TYPES)
        return uploaded_file, query_text
    else:
        return None, query_text

# Page setup
st.set_page_config(page_title='Ask My Doc App')
st.title('Ask My Doc App')

# Document type selection
selected_option = st.selectbox('Select Document Type', DOCUMENT_OPTIONS)

# Get user input
document_data, query_text = get_user_input(selected_option)

# Process user input
if document_data is not None:
    # Process the document data (URL or uploaded file)
    st.write(f"Document data: {document_data}")

# Process the user's query
if query_text:
    st.write(f"User's query: {query_text}")
