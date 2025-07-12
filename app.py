import streamlit as st

st.set_page_config(page_title="DermaSelect", page_icon="💄", layout="centered")

st.markdown("""
    <div style='text-align: center; padding: 20px; background-color: #ffe6ef; border-radius: 15px;'>
        <h1 style='color: #d63384;'>🌸 Welcome to DermaSelect</h1>
        <p style='color: #495057;'>Navigate using the sidebar 👉 to explore our Chatbot and Recommender System!</p>
    </div>
""", unsafe_allow_html=True)

st.markdown("### 🧠 Features:")
st.markdown("- 💬 **Chatbot**: Ask any skincare, makeup, or beauty questions")
st.markdown("- 🧴 **Product Recommender**: Discover the best beauty products for your preferences")
st.markdown("- 📊 **Built with Streamlit** using real Sephora data")

st.markdown("---")
st.markdown("Made with 💖 by Gauthami Ajay | MCA | 3rd Sem")
