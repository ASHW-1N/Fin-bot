import streamlit as st
from llama_interface import ask_llama
from financial_news import fetch_and_index_news
from voice_handler import listen_to_user  # Optional

# Page config
st.set_page_config(
    page_title="📈 AI Finance Assistant",
    page_icon="💸",
    layout="wide",
)

# Sidebar
with st.sidebar:
    st.image("assets/logo.png", use_container_width=True)  # ✅ updated
    st.title("💹 Finance Assistant")
    st.markdown("""
Welcome to your personal finance research assistant.

**What I can do:**
- 🧠 Answer finance questions  
- 🔍 Analyze news  
- 📊 Summarize markets  
- 💡 Predict trends

---
**Try asking:**  
- "Top stocks to watch tomorrow"  
- "How did markets in Asia perform today?"  
- "Why is gold rising?"  
""")
    st.markdown("🚀 [View on GitHub](https://github.com/ASHW-1N/Fin-bot.git)")

# Initialize session
if "fetched" not in st.session_state:
    with st.spinner("🔄 Fetching latest financial news..."):
        fetch_and_index_news()
    st.session_state.fetched = True

# Header image
st.image("assets/banner.jpg", use_container_width=True)  # ✅ updated

# Main UI
st.markdown("<h1 style='text-align: center;'>💼 Your AI Finance Assistant</h1>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: center; color: gray;'>Ask anything about the market, and get answers grounded in real news.</h4>", unsafe_allow_html=True)
st.markdown("---")

# Input area
col1, col2 = st.columns([10, 1])
with col1:
    user_input = st.text_input("📝 Type your question here:", placeholder="e.g., What’s driving gold prices today?")
with col2:
    if st.button("🎤"):
        user_input = listen_to_user()
        if user_input:
            st.success(f"🎧 You said: {user_input}")

# Process question
if user_input:
    with st.spinner("💭 Thinking..."):
        response = ask_llama(user_input)

    st.markdown("## 🧠 Assistant Response")
    st.success(response)
    st.markdown("---")

# Featured topics section
st.markdown("### 📌 Trending Market Topics")
col_a, col_b, col_c = st.columns(3)

with col_a:
    st.image("assets/stocks.jpg", use_container_width=True)  # ✅ updated
    st.caption("📈 Today's Top Performing Stocks")

with col_b:
    st.image("assets/commodities.jpg", use_container_width=True)  # ✅ updated
    st.caption("🛢️ Commodities Price Tracker")

with col_c:
    st.image("assets/currency.jpg", use_container_width=True)  # ✅ updated
    st.caption("💱 Currency & Forex Insights")

# Footer
st.markdown("""
---
<p style='text-align: center; color: gray;'>Built with ❤️ using LLaMA 2 + Streamlit + RAG | 100% local, secure, and privacy-friendly</p>
""", unsafe_allow_html=True)
