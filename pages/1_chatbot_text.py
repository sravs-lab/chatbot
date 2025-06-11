import os
import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import google.generativeai as genai
import google.api_core.exceptions


load_dotenv()

google_api_key = os.getenv('GOOGLE_API_KEY')
#print(google_api_key)
genai.configure(api_key=google_api_key)

#llm = ChatGoogleGenerativeAI(model="gemini-pro", api_key=google_api_key)

llm = genai.GenerativeModel('gemini-2.0-flash')

st.set_page_config(page_title="Chatbot Text Demo", page_icon="📈")

st.title("Chatbot Text Demo")
st.sidebar.header("Chatbot Text Demo")

st.divider()

query = st.text_input('Enter Your Query here..')

if st.button('Submit'):
    User = 'User'
    Chatbot = 'Chatbot'
    st.write(f'{User} - {query}')
    #response = llm.invoke(query)
    try:
        response = llm.generate_content(query)
        st.write(f'{Chatbot} - {response.text}')
    except google.api_core.exceptions.ResourceExhausted as e:
        st.error(f"Error occurred: {e}")
    #st.write(f'{Chatbot} - {response.content}')
    st.write(f'{Chatbot} - {response.text}')