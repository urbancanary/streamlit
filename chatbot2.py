from openai import OpenAI
import streamlit as st

# Use the key from st.secrets
api_key = st.secrets["general"]["OPENAI_API_KEY"]

# Initialize the OpenAI client with the API key
client = OpenAI(api_key=api_key)

# Set up the page title
st.title("ChatGPT-like clone")

# Initialize session state variables
if "openai_model" not in st.session_state:
    st.session_state["openai_model"] = "gpt-3.5-turbo"

if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Chat input
if prompt := st.chat_input("What is up?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Generate and display assistant response
    response = client.chat.completions.create(
        model=st.session_state["openai_model"],
        messages=[
            {"role": m["role"], "content": m["content"]}
            for m in st.session_state.messages
        ]
    )

    assistant_reply = response.choices[0].message.content
    st.session_state.messages.append({"role": "assistant", "content": assistant_reply})
    
    with st.chat_message("assistant"):
        st.markdown(assistant_reply)

