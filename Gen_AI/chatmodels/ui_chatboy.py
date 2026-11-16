
import streamlit as st
from dotenv import load_dotenv

from langchain_groq import ChatGroq
from langchain_core.messages import (
    AIMessage,
    SystemMessage,
    HumanMessage
)

load_dotenv()

# ------------------------------------------
# Initialize Chat Model
# ------------------------------------------

model = ChatGroq(
    model="openai/gpt-oss-120b",
    temperature=0.7,
    max_retries=3
)

# ------------------------------------------
# Page Configuration
# ------------------------------------------

st.set_page_config(
    page_title="AI Personality Chatbot",
    page_icon="🤖",
    layout="centered"
)

# ------------------------------------------
# Custom CSS
# ------------------------------------------

st.markdown("""
<style>

.stApp {
    background: linear-gradient(135deg, #101827, #202b42);
}

.main-title {
    text-align: center;
    font-size: 36px;
    font-weight: bold;
    color: white;
}

.subtitle {
    text-align: center;
    color: #aab8d0;
    font-size: 16px;
}

.personality-card {
    background: #263650;
    padding: 18px;
    border-radius: 15px;
    text-align: center;
    border: 1px solid #40516d;
    margin-bottom: 12px;
}

.personality-card h3 {
    color: white;
}

.personality-card p {
    color: #b9c6da;
    font-size: 13px;
}

div[data-testid="stChatMessage"] {
    border-radius: 15px;
    padding: 12px;
}

</style>
""", unsafe_allow_html=True)


# ------------------------------------------
# Application Heading
# ------------------------------------------

st.markdown(
    '<div class="main-title">🤖 AI Personality Chatbot</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">Choose your AI personality and start chatting!</div>',
    unsafe_allow_html=True
)

st.write("")


# ------------------------------------------
# Personality Selection
# ------------------------------------------

st.subheader("🎭 Choose Your AI Agent")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="personality-card">
        <h3>😢 Sad AI</h3>
        <p>Always replies in a sad way.</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="personality-card">
        <h3>😂 Funny AI</h3>
        <p>Always replies humorously.</p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="personality-card">
        <h3>😡 Angry AI</h3>
        <p>Always replies angrily.</p>
    </div>
    """, unsafe_allow_html=True)


choice = st.radio(
    "Select your personality:",
    ["Sad AI 😢", "Funny AI 😂", "Angry AI 😡"],
    horizontal=True,
    label_visibility="collapsed"
)


# ------------------------------------------
# Set System Message
# ------------------------------------------

if choice == "Sad AI 😢":
    mode = "You are a sad AI Agent and reply every message in very sad way"

elif choice == "Funny AI 😂":
    mode = "You are a funny AI Agent and reply every message in very funny way"

elif choice == "Angry AI 😡":
    mode = "You are an angry AI Agent and reply every message in very angry way"


# ------------------------------------------
# Initialize Session State
# ------------------------------------------

if "messages" not in st.session_state:

    st.session_state.messages = [
        SystemMessage(content=mode)
    ]

if "chat_ended" not in st.session_state:
    st.session_state.chat_ended = False


# Update SystemMessage when personality changes

st.session_state.messages[0].content = mode


# ------------------------------------------
# Display Selected Personality
# ------------------------------------------

st.write("")

st.info(f"Current AI Personality: {choice}")


# ------------------------------------------
# Display Previous Conversation
# ------------------------------------------

for message in st.session_state.messages:

    if isinstance(message, HumanMessage):

        with st.chat_message("user"):
            st.markdown(message.content)

    elif isinstance(message, AIMessage):

        with st.chat_message("assistant"):
            st.markdown(message.content)


# ------------------------------------------
# Chat Input
# ------------------------------------------

prompt = st.chat_input(
    "Type your message here...",
    disabled=st.session_state.chat_ended
)


if prompt:

    # Exit Condition

    if prompt == "0":

        st.session_state.chat_ended = True

        with st.chat_message("assistant"):
            st.markdown("👋 Exiting the chatbot. Goodbye!")

    else:

        # Display Human Message

        with st.chat_message("user"):
            st.markdown(prompt)

        # Add Human Message

        st.session_state.messages.append(
            HumanMessage(content=prompt)
        )

        # Generate AI Response

        with st.chat_message("assistant"):

            with st.spinner("AI is thinking... 🤔"):

                response = model.invoke(
                    st.session_state.messages
                )

                st.markdown(response.content)

        # Add AI Message

        st.session_state.messages.append(
            AIMessage(content=response.content)
        )
