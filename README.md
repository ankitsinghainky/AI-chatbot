
# LangGraph AI Chatbot

A simple conversational AI chatbot built with Python, LangGraph, LangChain and OpenAI. The main idea behind this project was to understand how LangGraph manages conversation flow and how an LLM can use previous messages to generate context-aware responses.

The chatbot keeps track of conversation history, so users can ask follow-up questions without having to repeat the entire context.

## Features

- Chat with an AI assistant using natural language.
- Maintains conversation history during a session.
- Uses LangGraph to manage the chatbot workflow.
- Handles follow-up questions using previous messages.
- Separate conversation sessions using thread IDs.
- Simple web interface built with Streamlit.

## Technologies Used

- Python
- LangGraph
- LangChain
- OpenAI API
- Streamlit

## Project Structure

```text
langgraph-ai-chatbot/
│
├── app.py
├── chatbot.py
├── requirements.txt
├── .env.example
├── .gitignore
└── README.md
```

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/YOUR-USERNAME/langgraph-ai-chatbot.git

cd langgraph-ai-chatbot
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

Activate it:

**Windows**
```bash
.venv\Scripts\activate
```

**Mac/Linux**
```bash
source .venv/bin/activate
```

### 3. Install the required packages

```bash
pip install -r requirements.txt
```

### 4. Set up the API key

Create a `.env` file in the project directory and add your OpenAI API key.

```env
OPENAI_API_KEY=your_api_key
```

Do not share or upload your API key.

### 5. Start the application

```bash
streamlit run app.py
```

The chatbot will open in your browser.

## How It Works

The application uses LangGraph to manage the conversation.

When a user sends a message, it is added to the conversation state. The chatbot node receives the available message history and sends it to the OpenAI model. The generated response is then added to the state.

LangGraph uses a thread ID to keep different conversations separate. For this project, `MemorySaver` is used to maintain conversation checkpoints while the application is running.

## What I Learned

While working on this project, I explored:

- Building a basic chatbot workflow with LangGraph.
- Managing conversation state using `StateGraph`.
- Working with messages and reducers in LangGraph.
- Maintaining conversation history using checkpoints.
- Connecting an LLM through LangChain.
- Building a basic chatbot interface with Streamlit.

## Current Limitations

- Conversation history is stored in memory and is lost when the application restarts.
- An OpenAI API key is required.
- Long-term memory and database integration are not included yet.

## Future Work

I would like to extend this project by adding persistent conversation storage, RAG-based document querying and support for multiple LLM providers.

## Author

**Ankit Singh**

B.Tech, Information Technology

Interested in Python, Generative AI, LLMs and AI application development.
