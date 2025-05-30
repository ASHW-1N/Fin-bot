# Fin-bot
# 📈 AI Finance Assistant 🤖💰

An intelligent, real-time financial question-answering assistant built using **LLaMA 2** and **Retrieval-Augmented Generation (RAG)**. This project blends the power of **open-source large language models** with **real-world financial news** to deliver smart, context-aware insights in natural human language — without hallucination or fluff.

> Think of it as ChatGPT for financial news, but fully local and under your control. 💻🔐

---

## 🔍 What It Does

When you ask a financial question like:

> *"How did Asian markets perform today?"*

The assistant will:

1. Retrieve **relevant news snippets** from a local database of articles.
2. Use those snippets to **build an intelligent context**.
3. Feed that context into a local **LLaMA 2 model** using a smart prompt.
4. Return a **concise, well-reasoned answer** based on actual financial news.

It’s Retrieval-Augmented Generation done right — fast, grounded, and transparent.

---

## 🚀 Features

### ✅ Retrieval-Augmented Generation (RAG)
- Dynamically retrieves **top relevant news** articles using **FAISS vector similarity search**.
- Embeds queries and documents using **`sentence-transformers`** (`all-MiniLM-L6-v2`).

### 🧠 LLaMA 2 Integration (Offline, Local)
- Powered by Meta's **LLaMA 2 7B Chat** model (quantized `.gguf`).
- Fully local via [`llama.cpp`](https://github.com/ggerganov/llama.cpp) Python bindings.
- Custom prompt template ensures **factual**, **honest**, and **non-hallucinated** responses.

### 📚 Real-Time Financial Knowledge
- Loads news from a local `news.json` file (can be automated with RSS or APIs).
- Formats news into concise summaries for improved grounding.

### 🖥️ Built with Streamlit
- Clean, minimal, and interactive UI.
- Type in your query and get a real-time AI response with retrieved context.

### 💡 Thoughtful Prompting
- Uses advanced prompt engineering techniques:
  - Adds clear system role: “You are a financial assistant...”
  - Includes fallback logic: “If data is missing, say so.”
  - Avoids bluffing or hallucinating future events.

---

## 🛠️ Tech Stack

| Layer         | Tool/Library              | Purpose                                 |
|---------------|---------------------------|-----------------------------------------|
| 💬 LLM        | `llama.cpp` (LLaMA 2 Chat)| Natural Language Response Generation    |
| 📄 Embeddings | `sentence-transformers`   | Semantic embedding for RAG              |
| 🔍 Search     | `faiss`                   | Fast approximate nearest neighbors search|
| 🌐 UI         | `Streamlit`               | Interactive frontend for user queries   |
| 📦 Data       | JSON (news.json)          | Financial article context store         |

---

## 📂 Project Structure

inance-assistant/
├── app.py # Streamlit app entry point
├── llama_interface.py # Handles LLaMA prompting logic
├── financial_news.py # FAISS-based news retrieval
├── news.json # Source news articles
├── models/ # Contains LLaMA GGUF model
│ └── llama-2-7b-chat.Q8_0.gguf
├── README.md # This file
└── requirements.txt # Dependencies


---

## 📌 Example Queries You Can Try

- “Top stocks to watch next week?”
- “What’s driving gold prices today?”
- “How did European markets react to the Fed announcement?”
- “Any news on Indian tech sector performance?”
- “Has there been a rise in crude oil prices?”

---

## 🔒 Privacy & Local Execution

This project is **fully offline**:
- No API calls
- No cloud services
- No user data shared

Perfect for **local research**, **personal finance analysis**, or **air-gapped environments**.

---

## 🧠 How It Works – Under the Hood

### Step-by-step Flow:
1. 📰 **Load Articles** → From `news.json`.
2. 🔍 **Vector Indexing** → Create dense vectors with `sentence-transformers`, indexed via `faiss`.
3. ✏️ **User Query** → Entered in the Streamlit UI.
4. 🔎 **Retrieve Top Matches** → FAISS finds top-k most relevant articles.
5. 🧠 **LLaMA Prompting** → Query + context fed into `llama.cpp` model.
6. 📤 **Answer Returned** → Displayed in natural-sounding text.

---

## 📥 Installation

```bash
git clone https://github.com/your-username/finance-assistant
cd finance-assistant

# Create virtual environment
python -m venv venv
venv\Scripts\activate  # Windows

# Install dependencies
pip install -r requirements.txt

# Place your GGUF model in /models/
# you can download the Llama quantized Model from --https://huggingface.co/TheBloke/finance-LLM-GGUF
# and place it in your /models folder

# Run the app
streamlit run app.py


