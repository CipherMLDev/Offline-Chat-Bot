# Offline-Chat-Bot
This chatbot is a web-based AI assistant built using Streamlit and Langchain. It leverages a language model, specifically the Ollama model, to respond to user queries in real time. The chatbot maintains conversation context by using ConversationBufferMemory, ensuring that the dialogue feels continuous and coherent.



# Streamlined AI Chatbot

This project is a Streamlit-based AI chatbot application that uses the Ollama language model. Follow the steps below to set up and run the application.

## Prerequisites

1. **Download Ollama**:

   - Visit the [Ollama website](https://www.ollama.com/) and follow the instructions to download and install Ollama on your machine.

2. **Pull the Required Model**:

   - After installing Ollama, open your terminal and run the following command to pull the required model:

     ollama pull qwen2:0.5b

## Installation

1. **Clone the Repository**:

   - Clone this repository to your local machine using the following command:

     git clone https://github.com/S0uviK-R0Y/Offline-Chat-Bot
     cd https://github.com/S0uviK-R0Y/Offline-Chat-Bot

2. **Create a Virtual Environment** (optional but recommended):

   - Create a virtual environment to manage your dependencies:

     python -m venv venv
     source venv/bin/activate  # On Windows use `venv\Scripts\activate`

3. **Install Dependencies**:

   - Install the required Python libraries using `pip`:

     pip install -r requirements.txt

## Usage

1. **Run the Streamlit Application**:

   - Start the Streamlit app by running the following command:

     streamlit run app.py

2. **Interact with the Chatbot**:

   - Open your web browser and navigate to `http://localhost:8501`. You should see the Streamlined AI Chatbot interface.
   - Type your questions into the input box and receive responses from the AI assistant.

## Project Structure

- `app.py`: The main application file that sets up and runs the Streamlit chatbot.
- `requirements.txt`: A file containing all the required Python libraries.

## Detailed Code Explanation

The application uses the following key components:

- **Streamlit**: A framework for creating web applications in Python.
- **Ollama**: A language model used for generating responses.
- **Langchain**: A library that facilitates the creation of language model chains.
- **Asyncio**: A library to handle asynchronous operations, used here to simulate typing.

## Key Functions

- `get_chain()`: Initializes and caches the language model chain.
- `simulate_typing(message_placeholder, full_response)`: Simulates typing for the AI assistant's responses.

## Contact

For any questions or issues, please open an issue in the repository or contact the maintainer at [souvikroy.cse.tcea@gmail.com].

Enjoy using the Streamlined AI Chatbot!
