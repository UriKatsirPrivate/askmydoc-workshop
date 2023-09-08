import streamlit as st
from back import generate_response_from_llm

# Use constants for option keys
URL_OPTION = 'URL'
FILE_UPLOAD_OPTION = 'File Upload'

# Define allowed file types as a constant
ALLOWED_FILE_TYPES = {'txt', 'py', 'tf', 'sh', 'yaml'}

# Use a dictionary for option mapping
option_mapping = {
    'Please Select': None,
    FILE_UPLOAD_OPTION: FILE_UPLOAD_OPTION,  # Simplify the mapping
    # Add more options here
}

st.set_page_config(page_title='Ask My Doc App')
st.title('Ask My Doc App')

# Use more descriptive variable names
selected_option_label = st.selectbox('Select Document Type', list(option_mapping.keys()))
selected_option_value = option_mapping[selected_option_label]

uploaded_file = None

if selected_option_value == FILE_UPLOAD_OPTION:
    uploaded_file = st.file_uploader('Upload an article', type=ALLOWED_FILE_TYPES)
    query_text = st.text_input('Enter your question:', value='', help='Please provide a short summary.')

with st.form('myform', clear_on_submit=True):
    submitted = st.form_submit_button('Submit', disabled=not uploaded_file)
    if submitted:
        try:
            if uploaded_file:
                with st.spinner('Generating response...'):
                    response = generate_response_from_llm(uploaded_file, query_text)
                # st.write(response)
                st.text_area('Response', value=response["result"], height=200, max_chars=None, key=None)
                st.text_area('Sources', value=response["source_documents"], height=400, max_chars=None, key=None)
            else:
                st.warning("Please upload a valid file.")  # Use warning for non-blocking notification
        except Exception as e:
            st.error(f"An error occurred: {str(e)}")
