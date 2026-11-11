
import streamlit as st
import uuid

from chatbot import AIChatbot


st.set_page_config(
    page_title="AI Chatbot",
    page_icon="🤖",
    layout="centered"
)

st.title("🤖 AI Chatbot")
st.caption("Powered by LangGraph and LangChain")

# Initialize chatbot
if "bot" not in st.session_state:
    st.session_state.bot = AIChatbot()

# Initialize conversation
if "session_id" not in st.session_state:
    st.session_state.session_id = str(uuid.uuid4())

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []


# Sidebar
with st.sidebar:
    st.header("Chat Settings")

    st.write("Your conversation is maintained using LangGraph.")

    if st.button("New Conversation"):
        st.session_state.session_id = str(uuid.uuid4())
        st.session_state.chat_history = []
        st.rerun()


# Display previous messages
for message in st.session_state.chat_history:

    with st.chat_message(message["role"]):
        st.markdown(message["content"])


# User input
user_input = st.chat_input("Ask me anything...")

if user_input:

    st.session_state.chat_history.append({
        "role": "user",
        "content": user_input
    })

    with st.chat_message("user"):
        st.markdown(user_input)

    with st.chat_message("assistant"):

        with st.spinner("Thinking..."):

            try:
                response = st.session_state.bot.chat(
                    user_input,
                    st.session_state.session_id
                )

                st.markdown(response)

                st.session_state.chat_history.append({
                    "role": "assistant",
                    "content": response
                })

            except Exception as error:
                st.error(f"Something went wrong: {error}")

