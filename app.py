import streamlit as st
from langchain_community.llms import Ollama
from langchain.chains import LLMChain
from langchain.memory import ConversationBufferMemory
from langchain.prompts import PromptTemplate
import asyncio

# Constants
MODEL_NAME = "gemma2:2b"
TYPING_SPEED = 0.02  # seconds per word

# Initialize Ollama LLM
@st.cache_resource
def get_llm():
    return Ollama(model=MODEL_NAME)

# Define prompt template
TEMPLATE = """You are a helpful AI assistant. Answer the question based on the context provided.

Context: {history}

Question: {human_input}

Instructions:
1. Use bullet points or numbers for lists.
2. Break long answers into short paragraphs.
3. Be concise and clear.

Answer:
"""

# Initialize LLM chain
@st.cache_resource
def get_chain():
    llm = get_llm()
    prompt = PromptTemplate(input_variables=["history", "human_input"], template=TEMPLATE)
    memory = ConversationBufferMemory(input_key="human_input", memory_key="history")
    return LLMChain(llm=llm, prompt=prompt, memory=memory, verbose=True)

# Simulate typing effect
async def simulate_typing(message_placeholder, full_response):
    displayed_response = ""
    for word in full_response.split():
        displayed_response += word + " "
        message_placeholder.markdown(displayed_response + "▌")
        await asyncio.sleep(TYPING_SPEED)
    message_placeholder.markdown(full_response)

# Main function to run the chatbot
def run_chatbot():
    st.title("Optimized AI Chatbot")

    chain = get_chain()

    # Initialize chat history
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Display chat messages from history on app rerun
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # React to user input
    if user_input := st.chat_input("What is your question?"):
        st.chat_message("user").markdown(user_input)
        st.session_state.messages.append({"role": "user", "content": user_input})

        with st.chat_message("assistant"):
            message_placeholder = st.empty()
            full_response = chain.predict(human_input=user_input)
            
            # Use asyncio to simulate typing effect
            asyncio.run(simulate_typing(message_placeholder, full_response))

        st.session_state.messages.append({"role": "assistant", "content": full_response})

if __name__ == "__main__":
    run_chatbot()