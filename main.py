import streamlit as st
import requests
from langchain_community.llms import Ollama

#Declaring Ollama for llama3
llm = Ollama(model="llama3")

# Streamlit App title and description
st.title('Text Summarizer App')

# Input box for user to enter text
user_input = st.text_area("Enter text to summarize:")

if st.button("Summarize"):
    if user_input:
        # Display loading indicator
        with st.spinner('Generating summary...'):
             summary = llm(f"Summarize the content: {user_input}")
             if summary:
                st.subheader("Summary:")
                st.write(summary)
    else:
        st.warning("Please enter some text to summarize.")
