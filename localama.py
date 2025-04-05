from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms import Ollama
import streamlit as st
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Check if Ollama is installed and running
ollama_installed = os.system("ollama list") == 0  # Returns 0 if successful

if not ollama_installed:
    st.error("⚠️ Ollama is not installed or not running. Please install and start Ollama before using this app.")
else:
    # Prompt template
    prompt = ChatPromptTemplate.from_messages([
        ("system", "You are a helpful assistant. Please respond to user queries."),
        ("user", "Question: {question}")
    ])

    # Streamlit UI
    st.title(" LangChain Chatbot with Ollama")
    input_text = st.text_input("Ask a question:")

    # Use Ollama model
    try:
        llm = Ollama(model="gemma:latest")  # Ensure the correct model format
        output_parser = StrOutputParser()
        chain = prompt | llm | output_parser

        # Generate response if input is given
        if input_text:
            response = chain.invoke({"question": input_text})
            st.write("🤖 **Response:**", response)
    except Exception as e:
        st.error(f"⚠️ An error occurred: {str(e)}")
