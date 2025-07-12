# pages/Chatbot.py

import streamlit as st
from chatbot import get_bot_response  # ✅ Import from your logic file

st.set_page_config(page_title="Chatbot", page_icon="🤖")
st.title("🤖 Ask DermaBot – Beauty Q&A")

question = st.text_input("💬 Your question:")
if st.button("Ask"):
    if question.strip():
        response = get_bot_response(question)
        st.success("🧠 DermaBot says:")
        st.write(response)
