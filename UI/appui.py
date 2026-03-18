import streamlit as st
import requests
import uuid

st.title("Chatbot Agent Chat UI")

# Create session id for conversation
if "session_id" not in st.session_state:
    st.session_state.session_id = str(uuid.uuid4())

# Store chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# Chat input
prompt = st.chat_input("Ask something...")

if prompt:

    # Show user message
    st.session_state.messages.append({
        "role": "user",
        "content": prompt
    })

    with st.chat_message("user"):
        st.write(prompt)

    # Call FastAPI
    url = "https://chatbotwithrag-hxgueweaegaue8b3.centralindia-01.azurewebsites.net/chat"

    payload = {
        "question": prompt,
    }

    params = {
        "session_id": st.session_state.session_id
    }

    try:
        response = requests.post(url, json=payload, params=params)

        if response.status_code == 200:
            reply = response.text

            st.session_state.messages.append({
                "role": "assistant",
                "content": reply
            })

            with st.chat_message("assistant"):
                st.markdown(reply)

        else:
            st.error(f"API Error: {response.status_code}")

    except Exception as e:
        st.error(f"Connection error: {e}")