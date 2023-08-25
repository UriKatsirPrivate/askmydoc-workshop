import streamlit as st
import os
import tempfile


# Page title
st.set_page_config(page_title='Ask My Doc App')
st.title('Ask My Doc App')

options = ['Please Select', 'URL', 'File Upload','Python Repository']
selected_option = st.selectbox('Select Document Type', options)

url_text = None
uploaded_file = None
query_text = None
repo_path= None
# temp_file_path = ""
if selected_option == 'URL':
    url_text = st.text_input('Enter your url:', placeholder='Please provide a URL.')
    query_text = st.text_input('Enter your question:', placeholder='Please provide a short summary.')
elif selected_option == 'Python Repository':
    repo_path = st.text_input('Enter your git url:', placeholder='Please provide a git URL.')
    query_text = st.text_input('Enter your question:', placeholder='what will the code perform?')
elif selected_option == 'File Upload':
    uploaded_file = st.file_uploader('Upload an article', type=['csv','txt', 'py', 'tf', 'sh', 'yaml', 'pdf'])
    query_text = st.text_input('Enter your question:', placeholder='Please provide a short summary.')