import streamlit as st
from SimplerLLM.language.llm import LLM, LLMProvider
from SimplerLLM.tools.generic_loader import load_content

# Sidebar for API Key input
st.sidebar.title("Configuration")
api_key = st.sidebar.text_input("Enter your Google Gemini API Key", type="password")
model_name = "gemini-1.5-pro"  # Fixed model name for Gemini 1.5 Pro

# Main section for input and summarization
st.title("AI Agent with Google Gemini")

# Input field for URL
url = st.text_input("Enter the URL to summarize", "https://learnwithhasan.com/create-ai-agents-with-python/")

# Button to trigger the summarization
if st.button("Generate Summary"):
    if api_key:
        # Initialize the LLM instance with Google Gemini API
        llm_instance = LLM.create(provider=LLMProvider.GAMINI, model_name=model_name, api_key=api_key)
        
        # Load content from the provided URL
        content = load_content(url).content
        
        # Create summarization prompt
        summarize_prompt = f"Generate a bullet point summary for the following: {content}"
        
        # Generate response using the LLM
        generated_text = llm_instance.generate_response(prompt=summarize_prompt)
        
        # Display the generated summary
        st.subheader("Generated Summary:")
        st.write(generated_text)
    else:
        st.error("Please provide your Google Gemini API Key in the sidebar.")